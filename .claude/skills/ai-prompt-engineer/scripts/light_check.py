#!/usr/bin/env python3
"""§30K / §30L — light and colour continuity by instrument.

Usage:
  light_check.py scene FRAME1.png FRAME2.png ... [--json]              # a scene's approved frames, in shot order
  light_check.py colour --ref MASTER.png FRAME_OR_CLIP ... [--json]    # §30L strict scene colour lock
  light_check.py clip CLIP.mp4 [--json]                                # one clip

colour: every frame (or clip — averaged over one frame per second) against the scene's master frame:
        warmth ±0.04, tint (green–magenta) ±0.04, saturation ±15%, luminance ±12% — any breach flags.
        Palette distance (colour histogram, 0 = identical) is reported, never failed: a close-up legitimately
        holds different colours from the wide master. A flag on a frame filled by one COLOUR-KEY object
        (a red jumper in close-up) is read by eye against the key before any regeneration (§30L). Run on the approved frames before any
        video, on each clip after generation, and on the scene's clips in the edit after the grade.
        (Thresholds unverified — tuned on the first build; tighten, never loosen, without the user.)

scene: per frame, mean luminance, warmth (R−B balance) and which half of the frame is brighter.
       Flags a frame whose luminance or warmth jumps from the scene's median — a relit shot
       (luma ±15%, warmth ±0.06; thresholds unverified, tuned on the first build).
clip:  per-frame luminance across the clip. Flags flicker (a frame-to-frame jump > 4%)
       and drift (first vs last second > 12%) — the light changing inside a clip.
Exit 1 on any flag. Key-side flips are reported for the reader to compare with the light plan
(a reverse angle legitimately flips the screen side, §30K) — never failed on their own.
"""
import argparse, json, subprocess, sys
from statistics import median

import imageio_ffmpeg
import numpy as np

FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H = 90, 160  # analysis size, 9:16


def frames(path, fps=None):
    vf = f"scale={W}:{H}" + (f",fps={fps}" if fps else "")
    raw = subprocess.run([FF, "-v", "error", "-i", path, "-vf", vf, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         capture_output=True, check=True).stdout
    a = np.frombuffer(raw, np.uint8)
    return a.reshape(-1, H, W, 3).astype(np.float32) / 255.0


def stats(img):
    luma = 0.2126 * img[..., 0] + 0.7152 * img[..., 1] + 0.0722 * img[..., 2]
    l, r = luma[:, : W // 2].mean(), luma[:, W // 2:].mean()
    return {"luma": round(float(luma.mean()), 4),
            "warmth": round(float(img[..., 0].mean() - img[..., 2].mean()), 4),
            "bright_side": "L" if l > r * 1.08 else "R" if r > l * 1.08 else "even"}


def colour_stats(img):
    r, g, b = img[..., 0], img[..., 1], img[..., 2]
    luma = 0.2126 * r + 0.7152 * g + 0.0722 * b
    mx, mn = img.max(axis=-1), img.min(axis=-1)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-3), 0)
    q = np.clip((img * 7.999).astype(int), 0, 7)
    hist = np.bincount((q[..., 0] * 64 + q[..., 1] * 8 + q[..., 2]).ravel(), minlength=512).astype(np.float64)
    return {"luma": float(luma.mean()), "warmth": float(r.mean() - b.mean()),
            "tint": float(g.mean() - (r.mean() + b.mean()) / 2), "sat": float(sat.mean()), "hist": hist / hist.sum()}


def load_mean(path):
    fr = frames(path, fps=1 if not path.lower().endswith((".png", ".jpg", ".jpeg", ".webp")) else None)
    st = [colour_stats(f) for f in fr]
    out = {k: float(np.mean([x[k] for x in st])) for k in ("luma", "warmth", "tint", "sat")}
    out["hist"] = np.mean([x["hist"] for x in st], axis=0)
    return out


def colour(ref, paths):
    R = load_mean(ref)
    rows, flags = [], []
    for p in paths:
        S = load_mean(p)
        dist = float(0.5 * np.abs(S["hist"] - R["hist"]).sum())
        row = {"frame": p, "warmth": round(S["warmth"] - R["warmth"], 4), "tint": round(S["tint"] - R["tint"], 4),
               "sat": round((S["sat"] - R["sat"]) / max(R["sat"], 1e-3), 3),
               "luma": round((S["luma"] - R["luma"]) / max(R["luma"], 1e-3), 3), "palette": round(dist, 3)}
        rows.append(row)
        for k, lim in (("warmth", 0.04), ("tint", 0.04), ("sat", 0.15), ("luma", 0.12)):
            if abs(row[k]) > lim:
                flags.append({"frame": p, "flag": k.upper(), "detail": f"{row[k]:+} (limit ±{lim}) vs master"})
    return {"ref": ref, "frames": rows, "flags": flags}


def scene(paths):
    rows = [{"frame": p, **stats(frames(p)[0])} for p in paths]
    ml, mw = median(r["luma"] for r in rows), median(r["warmth"] for r in rows)
    flags = []
    for r in rows:
        if ml and abs(r["luma"] - ml) / ml > 0.15:
            flags.append({"frame": r["frame"], "flag": "LUMA", "detail": f"{r['luma']} vs scene {ml:.4f}"})
        if abs(r["warmth"] - mw) > 0.06:
            flags.append({"frame": r["frame"], "flag": "WARMTH", "detail": f"{r['warmth']} vs scene {mw:.4f}"})
    return {"frames": rows, "flags": flags}


def clip(path):
    fr = frames(path)
    luma = (0.2126 * fr[..., 0] + 0.7152 * fr[..., 1] + 0.0722 * fr[..., 2]).mean(axis=(1, 2))
    flags = []
    jumps = np.abs(np.diff(luma)) / np.maximum(luma[:-1], 1e-3)
    for i in np.where(jumps > 0.04)[0][:10]:
        flags.append({"flag": "FLICKER", "detail": f"frame {i}→{i + 1}: {jumps[i] * 100:.1f}%"})
    n = max(1, min(24, len(luma) // 4))
    a, b = luma[:n].mean(), luma[-n:].mean()
    if a and abs(b - a) / a > 0.12:
        flags.append({"flag": "DRIFT", "detail": f"start {a:.3f} → end {b:.3f}"})
    return {"frames": int(len(luma)), "luma_first": round(float(a), 4), "luma_last": round(float(b), 4), "flags": flags}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("what", choices=["scene", "clip", "colour"])
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--ref")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.what == "colour" and not a.ref:
        ap.error("colour needs --ref <the scene's master frame>")
    res = scene(a.paths) if a.what == "scene" else colour(a.ref, a.paths) if a.what == "colour" else clip(a.paths[0])
    if a.json:
        print(json.dumps(res, indent=1))
    else:
        for r in res.get("frames", []) if a.what == "scene" else []:
            print(f"{r['frame']}: luma {r['luma']}  warmth {r['warmth']}  brighter {r['bright_side']}")
        for r in res.get("frames", []) if a.what == "colour" else []:
            print(f"{r['frame']}: warmth {r['warmth']:+}  tint {r['tint']:+}  sat {r['sat']:+}  luma {r['luma']:+}  palette {r['palette']}")
        for f in res["flags"]:
            print(f"FLAG  {f['flag']:8} {f.get('frame', '')} {f['detail']}")
        print(("COLOUR" if a.what == "colour" else "LIGHT") + (" PASS" if not res["flags"] else f" FLAGS ({len(res['flags'])})"))
    sys.exit(1 if res["flags"] else 0)


if __name__ == "__main__":
    main()
