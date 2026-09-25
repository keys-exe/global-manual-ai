#!/usr/bin/env python3
"""§22W — one image per clip so the agent can judge the whole motion at once.

Usage:
  contact_sheet.py CLIP.mp4 [--frames 8] [--out SHEET.jpg] [--full]

Tiles N frames evenly spaced from the first frame to the last (always both) into
one JPEG, each tile stamped with its timestamp. --full also saves every tile as its
own full-resolution PNG next to the sheet, for zooming into hands, product and text.
Prints JSON: duration, fps, resolution, aspect, audio present, frozen-frame runs
(freezedetect), black frames, and the files written.
"""
import argparse, json, re, subprocess
from pathlib import Path

import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clip")
    ap.add_argument("--frames", type=int, default=8)
    ap.add_argument("--out")
    ap.add_argument("--full", action="store_true")
    a = ap.parse_args()
    clip = Path(a.clip)
    info = subprocess.run([FF, "-hide_banner", "-i", str(clip)], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", info).groups()
    dur = int(h) * 3600 + int(m) * 60 + float(s)
    v = re.search(r"Video: .*?(\d{2,5})x(\d{2,5}).*?([\d.]+) fps", info)
    w, hh, fps = int(v.group(1)), int(v.group(2)), float(v.group(3))
    n = max(2, a.frames)
    times = [round(min(dur - 1 / fps, dur * k / (n - 1)), 3) for k in range(n)]
    out = Path(a.out) if a.out else clip.with_suffix(".sheet.jpg")
    tiles = []
    for k, t in enumerate(times):
        tp = out.with_name(f"{clip.stem}.t{k:02d}.png")
        if k == n - 1:  # the true last frame: read the tail and keep the final decoded frame
            subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-sseof", "-0.5", "-i", str(clip),
                            "-update", "1", "-q:v", "1", str(tp)], check=True)
            times[k] = round(dur, 3)
        else:
            subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-ss", str(t), "-i", str(clip),
                            "-frames:v", "1", str(tp)], check=True)
        if not tp.exists():
            raise SystemExit(json.dumps({"error": f"could not extract frame at {t}s"}))
        tiles.append(tp)
    cols = min(n, 4)
    rows = (n + cols - 1) // cols
    ins = sum([["-i", str(t)] for t in tiles], [])
    lab = ";".join(f"[{k}:v]scale=360:-2,drawtext=text='{times[k]:.2f}s':x=8:y=8:fontsize=28:"
                   f"fontcolor=white:box=1:boxcolor=black@0.6[t{k}]" for k in range(n))
    pads = "".join(f"[t{k}]" for k in range(n))
    th = int(360 * hh / w) // 2 * 2
    layout = "|".join(f"{(k % cols) * 360}_{(k // cols) * th}" for k in range(n))
    graph = f"{lab};{pads}xstack=inputs={n}:layout={layout}:fill=black[o]"
    r = subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", *ins, "-filter_complex", graph,
                        "-map", "[o]", "-frames:v", "1", "-q:v", "3", str(out)], capture_output=True, text=True)
    if r.returncode != 0:  # drawtext needs a font; fall back to unlabeled tiles
        lab = ";".join(f"[{k}:v]scale=360:-2[t{k}]" for k in range(n))
        graph = f"{lab};{pads}xstack=inputs={n}:layout={layout}:fill=black[o]"
        subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", *ins, "-filter_complex", graph,
                        "-map", "[o]", "-frames:v", "1", "-q:v", "3", str(out)], check=True)
    if not a.full:
        for t in tiles:
            t.unlink()
    an = subprocess.run([FF, "-hide_banner", "-i", str(clip), "-vf",
                         "freezedetect=n=0.003:d=0.5,blackdetect=d=0.1:pic_th=0.98", "-an", "-f", "null", "-"],
                        capture_output=True, text=True).stderr
    freezes = re.findall(r"freeze_start: ([\d.]+)[\s\S]*?freeze_end: ([\d.]+)", an)
    black = re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", an)
    print(json.dumps({
        "clip": str(clip), "duration_s": round(dur, 3), "fps": fps, "resolution": f"{w}x{hh}",
        "aspect_9x16": abs(w / hh - 9 / 16) < 0.02, "has_audio": "Audio:" in info,
        "sheet": str(out), "sheet_times_s": times, "frame_files": [str(t) for t in tiles] if a.full else [],
        "frozen_runs_s": [(float(x), float(y)) for x, y in freezes],
        "black_runs_s": [(float(x), float(y)) for x, y in black],
    }, indent=2))


if __name__ == "__main__":
    main()
