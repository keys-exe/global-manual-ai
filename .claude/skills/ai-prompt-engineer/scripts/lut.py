#!/usr/bin/env python3
"""§40 / §24G field 5 — the film's one LUT as a real file: make it, check it, preview it, apply it.

Usage:
  lut.py make GRADE.json -o LUT-<BUILD>.cube [--size 33]     # Look Sheet field 5 numbers -> .cube
  lut.py check LUT.cube [--json]                              # skin, neutrals and range sanity
  lut.py preview LUT.cube FRAME.png -o BEFORE_AFTER.png       # the scene master, ungraded | graded
  lut.py apply LUT.cube IN.mp4|IN.png -o OUT --mode 4|5 [--grain 7]

GRADE.json — Look Sheet field 5 as numbers (every field optional; the default is no change):
  {"warmth": 0.02,                      # −0.1…0.1  whole-image warm (+) / cool (−) shift
   "contrast": 1.12,                    # 0.8…1.4   S-curve around mid-grey (1 = none)
   "saturation": 0.9,                   # 0.6…1.3
   "shadow_tint": [200, 0.04],          # [hue°, amount 0…0.15]  e.g. 200 = teal-blue shadows
   "highlight_tint": [40, 0.03],        # [hue°, amount 0…0.15]  e.g. 40 = warm amber highlights
   "black_lift": 0.03,                  # 0…0.08    faded blacks, the print-film floor
   "white_point": 0.97,                 # 0.9…1.0   highlight roll-off ceiling
   "skin_protect": 0.7}                 # 0…1       how much of the tint and saturation change skin is spared

make:    writes a 3D LUT (.cube, R fastest) — the same file CapCut imports (Manual: Adjust → LUT → import;
         CapCut desktop — the team edits on desktop only) and `apply` uses (Automatic), so both run modes grade identically.
check:   FAIL if the neutral grey ramp is not monotonic (a tone inversion), a reference skin tone's hue moves
         more than 8° or its saturation more than ±25%, or any value leaves 0–1. Reports the grey ramp's tint.
preview: before | after, side by side — shown with the LUT on the board's Plan tab (Manual) or read by the
         agent (Automatic) before the LUT touches the cut.
apply:   ffmpeg lut3d on a clip or a frame, audio copied, resolution unchanged (720×1280 stays 720×1280, no
         upscale, §24G). --grain adds the Mode 4 grain pass (ffmpeg temporal noise, strength 1–20) after the
         LUT. Modes 1–3 are refused: they are matched only, never graded with a LUT (§40, §12). Mode 5 takes no
         grain. The LUT goes on the picture-locked, scene-matched cut only (§40 steps 1–2).
"""
import argparse, colorsys, json, subprocess, sys
from pathlib import Path

import imageio_ffmpeg
import numpy as np

FF = imageio_ffmpeg.get_ffmpeg_exe()
SKIN = [(0.87, 0.67, 0.55), (0.71, 0.49, 0.37), (0.45, 0.30, 0.22)]  # light, medium, deep reference skin (sRGB)


def luma(x):
    return 0.2126 * x[..., 0] + 0.7152 * x[..., 1] + 0.0722 * x[..., 2]


def tint_vec(hue):
    r, g, b = colorsys.hsv_to_rgb((hue % 360) / 360, 1, 1)
    v = np.array([r, g, b]) - (0.2126 * r + 0.7152 * g + 0.0722 * b)
    return v / max(np.abs(v).max(), 1e-6)


def contrast(v, c, p=0.45):
    if c < 1:
        return p + (v - p) * c
    k = 8.0
    sig = lambda t: 1 / (1 + np.exp(-k * (t - p)))
    s = (sig(v) - sig(0)) / (sig(1) - sig(0))
    return v + (s - v) * min(1.0, (c - 1) * 2.5)


def grade(x, g):
    """x: (..., 3) in 0–1. Returns the graded values."""
    x = x.astype(np.float64)
    w = g.get("warmth", 0.0)
    base = x + np.array([w / 2, 0, -w / 2])
    base = contrast(np.clip(base, 0, 1), g.get("contrast", 1.0))
    y = base.copy()
    L = luma(y)[..., None]
    y = L + (y - L) * g.get("saturation", 1.0)
    L = np.clip(luma(y), 0, 1)[..., None]
    for key, weight in (("shadow_tint", (1 - L) ** 2), ("highlight_tint", L ** 2)):
        if g.get(key):
            hue, amt = g[key]
            y = y + weight * amt * tint_vec(hue)
    prot = g.get("skin_protect", 0.0)
    if prot:
        mx, mn = x.max(-1), x.min(-1)
        sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
        r, gg, b = x[..., 0], x[..., 1], x[..., 2]
        hue = (np.degrees(np.arctan2(np.sqrt(3) * (gg - b), 2 * r - gg - b)) + 360) % 360
        dh = np.minimum(np.abs(hue - 25), 360 - np.abs(hue - 25))
        mask = np.exp(-(dh / 18) ** 2) * np.clip((sat - 0.1) / 0.1, 0, 1) * np.clip((0.75 - sat) / 0.15, 0, 1)
        m = (prot * mask)[..., None]
        y = y * (1 - m) + base * m
    lift, white = g.get("black_lift", 0.0), g.get("white_point", 1.0)
    return np.clip(lift + np.clip(y, 0, 1) * (white - lift), 0, 1)


def read_cube(path):
    n, rows = None, []
    for line in Path(path).read_text().splitlines():
        t = line.strip()
        if t.startswith("LUT_3D_SIZE"):
            n = int(t.split()[1])
        elif t and (t[0].isdigit() or t[0] in "-."):
            rows.append([float(v) for v in t.split()])
    a = np.array(rows).reshape(n, n, n, 3)  # [b][g][r]
    return n, a


def sample(n, a, rgb):
    """Trilinear lookup, as ffmpeg's lut3d and CapCut interpolate."""
    p = np.clip(np.array(rgb, float), 0, 1) * (n - 1)
    i0 = np.minimum(np.floor(p).astype(int), n - 2)
    f = p - i0
    out = np.zeros(3)
    for dr in (0, 1):
        for dg in (0, 1):
            for db in (0, 1):
                w = (f[0] if dr else 1 - f[0]) * (f[1] if dg else 1 - f[1]) * (f[2] if db else 1 - f[2])
                out += w * a[i0[2] + db, i0[1] + dg, i0[0] + dr]
    return out


def hsv(c):
    return colorsys.rgb_to_hsv(*[float(v) for v in c])


def cmd_make(a):
    g = json.loads(Path(a.grade).read_text())
    n = a.size
    t = np.linspace(0, 1, n)
    b, gg, r = np.meshgrid(t, t, t, indexing="ij")
    out = grade(np.stack([r, gg, b], -1), g).reshape(-1, 3)
    lines = [f'TITLE "{Path(a.o).stem}"', f"# §24G field 5: {json.dumps(g)}", f"LUT_3D_SIZE {n}",
             "DOMAIN_MIN 0.0 0.0 0.0", "DOMAIN_MAX 1.0 1.0 1.0"]
    lines += [f"{v[0]:.6f} {v[1]:.6f} {v[2]:.6f}" for v in out]
    Path(a.o).write_text("\n".join(lines) + "\n")
    print(f"wrote {a.o} ({n}³)")


def cmd_check(a):
    n, lut = read_cube(a.lut)
    fails, rep = [], {}
    grey = [sample(n, lut, (v, v, v)) for v in np.linspace(0, 1, n)]
    L = [float(luma(np.array(c))) for c in grey]
    if any(L[i + 1] < L[i] - 1e-4 for i in range(len(L) - 1)):
        fails.append("grey ramp not monotonic — a tone inversion")
    rep["grey_tint_shadow"] = [round(float(v), 3) for v in grey[n // 5] - luma(grey[n // 5])]
    rep["grey_tint_highlight"] = [round(float(v), 3) for v in grey[4 * n // 5] - luma(grey[4 * n // 5])]
    rep["black"], rep["white"] = round(L[0], 3), round(L[-1], 3)
    for s in SKIN:
        h0, s0, _ = hsv(s)
        h1, s1, _ = hsv(sample(n, lut, s))
        dh = min(abs(h1 - h0), 1 - abs(h1 - h0)) * 360
        ds = (s1 - s0) / max(s0, 1e-6)
        rep[f"skin {s}"] = {"hue_shift_deg": round(dh, 1), "sat_change": f"{ds:+.0%}"}
        if dh > 8:
            fails.append(f"skin {s} hue moves {dh:.1f}° (> 8°)")
        if abs(ds) > 0.25:
            fails.append(f"skin {s} saturation {ds:+.0%} (> ±25%)")
    if lut.min() < 0 or lut.max() > 1:
        fails.append("values outside 0–1")
    if a.json:
        print(json.dumps({"pass": not fails, "fails": fails, "report": rep}, indent=1))
    else:
        for k, v in rep.items():
            print(f"  {k}: {v}")
        for f in fails:
            print(f"FAIL  {f}")
        print("LUT PASS" if not fails else f"LUT FAIL ({len(fails)})")
    sys.exit(1 if fails else 0)


def lutfilter(path):
    p = str(Path(path).resolve()).replace("\\", "/").replace(":", "\\:").replace("'", "\\'")
    return f"lut3d=file='{p}'"


def cmd_preview(a):
    fc = f"[0:v]split[a][b];[b]{lutfilter(a.lut)}[g];[a][g]hstack=inputs=2"
    subprocess.run([FF, "-v", "error", "-y", "-i", a.frame, "-filter_complex", fc, "-frames:v", "1", a.o], check=True)
    print(f"wrote {a.o} (ungraded | graded)")


def cmd_apply(a):
    if a.mode in (1, 2, 3):
        sys.exit(f"REFUSED: Mode {a.mode} is matched only, never graded with a LUT (§40, §12)")
    if a.grain and a.mode != 4:
        sys.exit("REFUSED: the grain pass is Mode 4 only (§40 step 3)")
    vf = lutfilter(a.lut) + (f",noise=alls={a.grain}:allf=t" if a.grain else "")
    img = Path(a.input).suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")
    cmd = [FF, "-v", "error", "-y", "-i", a.input, "-vf", vf]
    cmd += ["-frames:v", "1"] if img else ["-c:v", "libx264", "-crf", "16", "-preset", "slow", "-pix_fmt", "yuv420p",
                                           "-c:a", "copy", "-movflags", "+faststart"]
    subprocess.run(cmd + [a.o], check=True)
    print(f"wrote {a.o}")


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    m = sp.add_parser("make"); m.add_argument("grade"); m.add_argument("-o", required=True); m.add_argument("--size", type=int, default=33)
    c = sp.add_parser("check"); c.add_argument("lut"); c.add_argument("--json", action="store_true")
    p = sp.add_parser("preview"); p.add_argument("lut"); p.add_argument("frame"); p.add_argument("-o", required=True)
    y = sp.add_parser("apply"); y.add_argument("lut"); y.add_argument("input"); y.add_argument("-o", required=True)
    y.add_argument("--mode", type=int, required=True); y.add_argument("--grain", type=float, default=0)
    a = ap.parse_args()
    {"make": cmd_make, "check": cmd_check, "preview": cmd_preview, "apply": cmd_apply}[a.cmd](a)


if __name__ == "__main__":
    main()
