#!/usr/bin/env python3
"""§30K — light continuity by instrument.

Usage:
  light_check.py scene FRAME1.png FRAME2.png ... [--json]    # a scene's approved frames, in shot order
  light_check.py clip CLIP.mp4 [--json]                      # one clip

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
    ap.add_argument("what", choices=["scene", "clip"])
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    res = scene(a.paths) if a.what == "scene" else clip(a.paths[0])
    if a.json:
        print(json.dumps(res, indent=1))
    else:
        for r in res.get("frames", []) if a.what == "scene" else []:
            print(f"{r['frame']}: luma {r['luma']}  warmth {r['warmth']}  brighter {r['bright_side']}")
        for f in res["flags"]:
            print(f"FLAG  {f['flag']:8} {f.get('frame', '')} {f['detail']}")
        print("LIGHT PASS" if not res["flags"] else f"LIGHT FLAGS ({len(res['flags'])})")
    sys.exit(1 if res["flags"] else 0)


if __name__ == "__main__":
    main()
