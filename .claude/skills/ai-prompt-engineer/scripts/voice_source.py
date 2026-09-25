#!/usr/bin/env python3
"""§22U steps 3-5 — build the ElevenLabs clone source from the 10s Seedance clip.

Usage:
  voice_source.py SEEDANCE.mp4 --name KEYWORD [--outdir DIR] [--speed 1.2] [--min 30]

Steps: E11 trim (trim.py --cut-all: every breath cut) -> atempo speed-up (pitch preserved) -> loop the whole
sped clip until the total is >= --min seconds -> <KEYWORD>_clone_source.mp3.
Prints a JSON report. Exit 0 = pass, 2 = fail (trim failed or source too short).

Setup (per session): pip install imageio-ffmpeg faster-whisper
"""
import argparse, json, math, subprocess, sys
from pathlib import Path

import imageio_ffmpeg

sys.path.insert(0, str(Path(__file__).parent))
from trim import FFMPEG, duration, silences, MAX_GAP  # noqa: E402

HERE = Path(__file__).parent


def run(*args):
    subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", *args], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--name", required=True, help="voice name: one keyword from the script title")
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--speed", type=float, default=1.2)
    ap.add_argument("--min", type=float, default=30.0)
    ap.add_argument("--model", default="small.en")
    a = ap.parse_args()

    src = Path(a.src)
    out = Path(a.outdir) if a.outdir else src.parent
    out.mkdir(parents=True, exist_ok=True)
    trimmed = out / f"{a.name}_source.trim.mp4"
    sped = out / f"{a.name}_source.x{a.speed}.wav"
    final = out / f"{a.name}_clone_source.mp3"

    # Step 3 — trim dead air and every breath (E11, --cut-all)
    r = subprocess.run([sys.executable, str(HERE / "trim.py"), str(src), "--out", str(trimmed),
                        "--model", a.model, "--cut-all"], capture_output=True, text=True)
    trim_report = json.loads(r.stdout) if r.stdout.strip() else {"error": r.stderr[-500:]}
    if r.returncode != 0:
        print(json.dumps({"status": "FAIL", "step": 3, "trim": trim_report}, indent=2))
        sys.exit(2)

    # Step 4 — speed x1.2, pitch preserved; audio only
    run("-i", str(trimmed), "-vn", "-af", f"atempo={a.speed}", "-ac", "1", "-ar", "44100", str(sped))
    one = duration(sped)

    # Step 5 — loop the whole clip until >= min seconds; never cut mid-clip
    reps = max(1, math.ceil(a.min / one))
    run("-stream_loop", str(reps - 1), "-i", str(sped), "-c:a", "libmp3lame", "-b:a", "192k", str(final))
    total = duration(final)
    gaps = [(round(s, 3), round(e, 3)) for s, e in silences(final) if e - s > MAX_GAP]

    ok = total >= a.min and not gaps
    print(json.dumps({
        "status": "PASS" if ok else "FAIL",
        "voice_name": a.name,
        "clone_source": str(final),
        "seedance_in_s": round(duration(src), 3),
        "after_trim_s": trim_report.get("duration_out_s"),
        "after_speed_s": round(one, 3),
        "repeats": reps,
        "total_s": round(total, 3),
        "gaps_over_0.4s": gaps,
        "transcript": trim_report.get("transcript"),
    }, indent=2))
    sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()
