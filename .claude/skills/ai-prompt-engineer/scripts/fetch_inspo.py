#!/usr/bin/env python3
"""§18B / §42 Part 1 — fetch every INSPO link and run the measure-before-read instruments.

Usage:
  fetch_inspo.py BUILD URL_OR_PATH [URL_OR_PATH ...]

Downloads each link into builds/<BUILD>/intake/ (yt-dlp for social links, a local
path is used as-is), then reports per file: duration, resolution, aspect, fps,
scene cuts (shot count, mean shot length, cut times) and silences at two
thresholds. Prints JSON. A link that fails to download is reported, never skipped
silently.

Setup (per session): pip install -q imageio-ffmpeg yt-dlp
"""
import json, re, subprocess, sys
from pathlib import Path

import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


def fetch(url, dest):
    p = Path(url)
    if p.exists():
        return p, None
    dest.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(["yt-dlp", "--no-playlist", "--ffmpeg-location", FFMPEG,
                        "-f", "bv*+ba/b", "--merge-output-format", "mp4",
                        "-o", str(dest / "%(extractor)s_%(id)s.%(ext)s"),
                        "--print", "after_move:filepath", url],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return None, (r.stderr.strip().splitlines() or ["unknown error"])[-1]
    return Path(r.stdout.strip().splitlines()[-1]), None


def probe(path):
    err = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err).groups()
    dur = int(h) * 3600 + int(m) * 60 + float(s)
    v = re.search(r"Video: .*?(\d{2,5})x(\d{2,5}).*?([\d.]+) fps", err)
    w, hgt, fps = (int(v.group(1)), int(v.group(2)), float(v.group(3))) if v else (None, None, None)
    return dur, w, hgt, fps, "Audio:" in err


def cuts(path, threshold=0.3):
    err = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path), "-vf",
                          f"select='gt(scene,{threshold})',showinfo", "-an", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return [round(float(t), 2) for t in re.findall(r"pts_time:([\d.]+)", err)]


def silences(path, db, dur=0.3):
    err = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path), "-af",
                          f"silencedetect=noise={db}dB:d={dur}", "-vn", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", err)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", err)]
    return [(round(a, 2), round(en[i], 2) if i < len(en) else None) for i, a in enumerate(st)]


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    build, links = sys.argv[1], sys.argv[2:]
    dest = Path("builds") / build / "intake"
    out = []
    for i, url in enumerate(links):
        role = "primary" if i == 0 else "secondary"
        path, err = fetch(url, dest)
        if err:
            out.append({"link": url, "role": role, "status": "FETCH_FAILED", "error": err})
            continue
        dur, w, h, fps, has_audio = probe(path)
        c = cuts(path)
        shots = len(c) + 1
        out.append({
            "link": url, "role": role, "status": "OK", "file": str(path),
            "duration_s": round(dur, 2), "resolution": f"{w}x{h}" if w else None,
            "aspect": ("9:16" if w and abs(w / h - 9 / 16) < 0.02 else f"{w}:{h}") if w else None,
            "fps": fps, "has_audio": has_audio,
            "shot_count": shots, "mean_shot_s": round(dur / shots, 2), "cut_times_s": c,
            "silences_-40dB": silences(path, -40) if has_audio else [],
            "silences_-30dB": silences(path, -30) if has_audio else [],
        })
    print(json.dumps(out, indent=2))
    sys.exit(0 if all(o["status"] == "OK" for o in out) else 2)


if __name__ == "__main__":
    main()
