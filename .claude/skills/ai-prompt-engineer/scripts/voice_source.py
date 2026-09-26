#!/usr/bin/env python3
"""§22U steps 3-5 — build the ElevenLabs clone source from the Kling voice source clips.

Usage:
  voice_source.py KLING_1.mp4 KLING_2.mp4 [...] --name KEYWORD [--outdir DIR]
                  [--speed 1.2] [--min 30] [--max-pitch-diff 0.10]

At least two Kling generations (step 2), in script order. Each one:
E11 trim (trim.py) -> atempo speed-up (pitch preserved). Then the sped takes
are joined in order and the whole joined sequence is looped until the total
is >= --min seconds -> <KEYWORD>_clone_source.mp3.
Same-voice check: each take's pitch median must sit within --max-pitch-diff
of the first take's (the takes must be one person, or the clone blends two).
Prints a JSON report. Exit 0 = pass, 2 = fail (trim failed, voices differ,
fewer than two takes or source too short).

Setup (per session): pip install imageio-ffmpeg faster-whisper numpy
"""
import argparse, json, math, subprocess, sys
from pathlib import Path

import imageio_ffmpeg
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from trim import FFMPEG, duration, silences, MAX_GAP  # noqa: E402

HERE = Path(__file__).parent
SR = 16000


def run(*args):
    subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", *args], check=True)


def pitch_median(path):
    """Median F0 (Hz) over voiced frames, by autocorrelation, 70-400 Hz."""
    raw = subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-i", str(path),
                          "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    win, hop = int(0.04 * SR), int(0.01 * SR)
    lo, hi = SR // 400, SR // 70
    if len(x) < win:
        return None
    rms_all = np.sqrt(np.mean(x ** 2)) or 1e-9
    f0 = []
    for i in range(0, len(x) - win, hop):
        fr = x[i:i + win] * np.hanning(win)
        if np.sqrt(np.mean(fr ** 2)) < 0.5 * rms_all:
            continue
        ac = np.correlate(fr, fr, "full")[win - 1:]
        if ac[0] <= 0:
            continue
        lag = lo + int(np.argmax(ac[lo:hi]))
        if ac[lag] / ac[0] > 0.45:
            f0.append(SR / lag)
    return round(float(np.median(f0)), 1) if f0 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src", nargs="+", help="the Kling voice source clips, in script order (two or more)")
    ap.add_argument("--name", required=True, help="voice name: one keyword from the script title")
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--speed", type=float, default=1.2)
    ap.add_argument("--min", type=float, default=30.0)
    ap.add_argument("--max-pitch-diff", type=float, default=0.10)
    ap.add_argument("--model", default="base.en")
    a = ap.parse_args()

    srcs = [Path(s) for s in a.src]
    if len(srcs) < 2:
        print(json.dumps({"status": "FAIL", "step": 2,
                          "error": "at least two Kling generations are required"}, indent=2))
        sys.exit(2)
    out = Path(a.outdir) if a.outdir else srcs[0].parent
    out.mkdir(parents=True, exist_ok=True)
    final = out / f"{a.name}_clone_source.mp3"

    takes = []
    for n, src in enumerate(srcs, 1):
        trimmed = out / f"{a.name}_source{n}.trim.mp4"
        sped = out / f"{a.name}_source{n}.x{a.speed}.wav"
        # Step 3 — trim dead air and inhales (E11)
        r = subprocess.run([sys.executable, str(HERE / "trim.py"), str(src), "--out", str(trimmed),
                            "--model", a.model], capture_output=True, text=True)
        rep = json.loads(r.stdout) if r.stdout.strip() else {"error": r.stderr[-500:]}
        if r.returncode != 0:
            print(json.dumps({"status": "FAIL", "step": 3, "take": n, "src": str(src), "trim": rep}, indent=2))
            sys.exit(2)
        # Step 4 — speed x1.2, pitch preserved; audio only
        run("-i", str(trimmed), "-vn", "-af", f"atempo={a.speed}", "-ac", "1", "-ar", "44100", str(sped))
        takes.append({"take": n, "src": str(src), "in_s": round(duration(src), 3),
                      "after_trim_s": rep.get("duration_out_s"), "after_speed_s": round(duration(sped), 3),
                      "pitch_median_hz": pitch_median(sped), "transcript": rep.get("transcript"),
                      "_sped": sped})

    # Same-voice check against take 1
    ref = takes[0]["pitch_median_hz"]
    mismatched = []
    for t in takes:
        p = t["pitch_median_hz"]
        t["pitch_diff"] = round(abs(p - ref) / ref, 3) if p and ref else None
        if t["pitch_diff"] is None or t["pitch_diff"] > a.max_pitch_diff:
            mismatched.append(t["take"])

    # Step 5 — join the takes in order, then loop the whole joined sequence to >= min
    joined = out / f"{a.name}_source.joined.wav"
    lst = out / f"{a.name}_source.list.txt"
    lst.write_text("".join(f"file '{t['_sped'].resolve()}'\n" for t in takes))
    run("-f", "concat", "-safe", "0", "-i", str(lst), "-c:a", "pcm_s16le", str(joined))
    one = duration(joined)
    reps = max(1, math.ceil(a.min / one))
    run("-stream_loop", str(reps - 1), "-i", str(joined), "-c:a", "libmp3lame", "-b:a", "192k", str(final))
    total = duration(final)
    gaps = [(round(s, 3), round(e, 3)) for s, e in silences(final) if e - s > MAX_GAP]

    for t in takes:
        t.pop("_sped")
    ok = total >= a.min and not gaps and not mismatched
    print(json.dumps({
        "status": "PASS" if ok else "FAIL",
        "voice_name": a.name,
        "clone_source": str(final),
        "takes": takes,
        "voice_mismatch_takes": mismatched,
        "joined_s": round(one, 3),
        "repeats": reps,
        "total_s": round(total, 3),
        "gaps_over_0.4s": gaps,
    }, indent=2))
    sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()
