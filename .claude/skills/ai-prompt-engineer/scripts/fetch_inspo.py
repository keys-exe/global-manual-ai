#!/usr/bin/env python3
"""§18B / §42 Part 1 — fetch every INSPO link and run the measure-before-read instruments.

Usage:
  fetch_inspo.py BUILD URL_OR_PATH [URL_OR_PATH ...]

Downloads each link into builds/<BUILD>/intake/ (yt-dlp for social links, a local
path is used as-is), then reports per file: duration, resolution, aspect, fps,
scene cuts (shot count, mean shot length, cut times) and silences at two
thresholds. Saves two frames per shot — just after the cut and mid-shot — to
builds/<BUILD>/intake/frames/<video>/S01_in.jpg, S01_mid.jpg … and lists them per
shot, plus contact sheets of one frame per second (sheet_01.jpg …, 6x5 tiles =
30 seconds each, left to right, top to bottom). The per-second sheets catch what
scene detection misses: a split-screen or picture-in-picture that appears over a
held shot changes only part of the frame and does not score as a cut. The agent reads the §42 Part 3A Edit Grammar (how each shot is laid out —
full-frame, split-screen, picture-in-picture, punch-in, captions) off these frames.
Prints JSON. A link that fails to download is reported, never skipped
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


def shot_frames(path, cut_list, dur, outdir):
    """Two frames per shot (just after the cut, mid-shot); returns the shot table."""
    outdir.mkdir(parents=True, exist_ok=True)
    edges = [0.0] + [c for c in cut_list if 0 < c < dur] + [dur]
    shots = []
    for n in range(len(edges) - 1):
        t0, t1 = edges[n], edges[n + 1]
        sid = f"S{n + 1:02d}"
        frames = {}
        for tag, t in (("in", t0 + min(0.15, (t1 - t0) / 4)), ("mid", (t0 + t1) / 2)):
            f = outdir / f"{sid}_{tag}.jpg"
            subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{t:.3f}",
                            "-i", str(path), "-frames:v", "1", "-vf", "scale=540:-2", "-q:v", "3", str(f)])
            frames[tag] = str(f) if f.exists() else None
        shots.append({"shot": sid, "t_in": round(t0, 2), "t_out": round(t1, 2),
                      "len_s": round(t1 - t0, 2), "frame_in": frames["in"], "frame_mid": frames["mid"]})
    return shots


def second_sheets(path, outdir):
    """One frame per second, tiled 6x5 (30s per sheet)."""
    subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-i", str(path), "-vf",
                    "fps=1,scale=180:-2,tile=6x5:padding=4:color=white", "-q:v", "3",
                    str(outdir / "sheet_%02d.jpg")])
    return sorted(str(p) for p in outdir.glob("sheet_*.jpg"))


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
            "shots": shot_frames(path, c, dur, dest / "frames" / path.stem),
            "second_sheets": second_sheets(path, dest / "frames" / path.stem),
        })
    print(json.dumps(out, indent=2))
    sys.exit(0 if all(o["status"] == "OK" for o in out) else 2)


if __name__ == "__main__":
    main()
