#!/usr/bin/env python3
"""§18C — fetch a Loom brief, transcribe it, pull frames, and list its instructions.

Usage:
  fetch_loom.py BUILD LOOM_URL_OR_PATH [--every SECONDS] [--model base|small|medium]

Downloads the Loom (yt-dlp; a local .mp4 is used as-is) into
builds/<BUILD>/intake/loom/, then:
  - transcribes the voice with timestamps (faster-whisper)
  - saves a frame every N seconds (default 5) and at every scene cut, so what the
    Loom shows on screen (script highlights, reference clips, drawings) is read,
    not only what it says
  - writes loom.json and loom.md: one numbered row per spoken segment (LM01, LM02...)
    with its time and the frames on screen while it is said
The agent reads loom.md plus the frames and turns the rows into Loom instructions in
the §27F Visual Instruction Ledger. A private or password-protected Loom will not
download: it is reported as FETCH_FAILED, never skipped silently.

Setup (per session): pip install -q imageio-ffmpeg yt-dlp faster-whisper
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


def fetch(src, dest):
    p = Path(src)
    if p.exists():
        return p, None
    dest.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(["yt-dlp", "--no-playlist", "--ffmpeg-location", FFMPEG,
                        "-f", "bv*+ba/b", "--merge-output-format", "mp4",
                        "-o", str(dest / "loom_%(id)s.%(ext)s"),
                        "--print", "after_move:filepath", src],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return None, (r.stderr.strip().splitlines() or ["unknown error"])[-1]
    return Path(r.stdout.strip().splitlines()[-1]), None


def duration(path):
    err = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err).groups()
    return int(h) * 3600 + int(m) * 60 + float(s), "Audio:" in err


def cuts(path, threshold=0.3):
    err = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path), "-vf",
                          f"select='gt(scene,{threshold})',showinfo", "-an", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return [round(float(t), 2) for t in re.findall(r"pts_time:([\d.]+)", err)]


def frame(path, t, out):
    subprocess.run([FFMPEG, "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", str(path),
                    "-frames:v", "1", "-vf", "scale=1280:-2", str(out)], check=True)


def transcribe(path, work, model):
    wav = work / "loom_audio.wav"
    subprocess.run([FFMPEG, "-v", "error", "-y", "-i", str(path), "-vn", "-ac", "1", "-ar", "16000",
                    str(wav)], check=True)
    from faster_whisper import WhisperModel
    segs, _ = WhisperModel(model, compute_type="int8").transcribe(str(wav), vad_filter=True)
    return [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()} for s in segs]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("build")
    ap.add_argument("loom")
    ap.add_argument("--every", type=float, default=5.0)
    ap.add_argument("--model", default="base")
    a = ap.parse_args()

    work = Path("builds") / a.build / "intake" / "loom"
    path, err = fetch(a.loom, work)
    if err:
        print(json.dumps({"link": a.loom, "status": "FETCH_FAILED", "error": err,
                          "fix": "set the Loom to 'anyone with the link' or put the MP4 in the Drive folder"},
                         indent=2))
        sys.exit(1)

    dur, has_audio = duration(path)
    fdir = work / "frames"
    fdir.mkdir(parents=True, exist_ok=True)
    times = sorted({round(t, 2) for t in [x * a.every for x in range(int(dur // a.every) + 1)] + cuts(path)
                    if t < dur})
    frames = []
    for t in times:
        f = fdir / f"t{t:07.2f}.jpg"
        frame(path, t, f)
        frames.append({"t": t, "file": str(f)})

    segs = transcribe(path, work, a.model) if has_audio else []
    rows = []
    for i, s in enumerate(segs, 1):
        on = [f["file"] for f in frames if s["start"] - a.every < f["t"] <= s["end"]]
        rows.append({"id": f"LM{i:02d}", **s, "frames": on})

    report = {"link": a.loom, "status": "OK", "file": str(path), "duration_s": round(dur, 2),
              "audio": has_audio, "segments": len(rows), "frames": len(frames), "rows": rows,
              "all_frames": frames}
    (work / "loom.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    md = [f"# Loom brief — {a.build}", "", f"Source: {a.loom}  ·  {dur:.1f}s  ·  {len(frames)} frames", "",
          "| ID | Time | Said | Frames |", "|---|---|---|---|"]
    for r in rows:
        fr = ", ".join(Path(x).name for x in r["frames"]) or "—"
        md.append(f"| {r['id']} | {r['start']:.1f}–{r['end']:.1f}s | {r['text']} | {fr} |")
    if not rows:
        md.append("| — | — | *(no speech — read the frames)* | all |")
    (work / "loom.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "all_frames"}, indent=2))


if __name__ == "__main__":
    main()
