#!/usr/bin/env python3
"""E11 trim pass — cut dead air and inhales from a dialogue clip.

Usage:
  trim.py IN.mp4 [--out OUT.mp4] [--keep START:END ...] [--model base.en]
          [--pre 0.06] [--post 0.08] [--entry-breath 0.12] [--dry-run]

Writes <IN>.trim.mp4 (never overwrites the input) and prints a JSON report:
cut list, keep-spans and the E1 verification result. Exit code 0 = pass,
2 = TRIM_FAIL (E2), 1 = error.

Setup (per session): pip install imageio-ffmpeg faster-whisper
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
NOISE_DB = -40      # E1 / §28G silence threshold
MAX_GAP = 0.4       # E1: no silence > 0.4s except keep-list
ENTRY_CAP = 0.5     # §28G: first word inside 0.5s
TAIL_CAP = 0.3      # E1: tail ends <= 0.3s after the last word


def duration(path):
    out = subprocess.run([FFMPEG, "-i", str(path)], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def silences(path, noise_db=NOISE_DB, min_dur=MAX_GAP):
    err = subprocess.run(
        [FFMPEG, "-hide_banner", "-i", str(path), "-af",
         f"silencedetect=noise={noise_db}dB:d={min_dur}", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", err)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", err)]
    total = duration(path)
    return [(s, ends[i] if i < len(ends) else total) for i, s in enumerate(starts)]


def words(path, model_name):
    from faster_whisper import WhisperModel
    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segs, _ = model.transcribe(str(path), word_timestamps=True, vad_filter=False)
    return [(w.start, w.end, w.word.strip()) for s in segs for w in (s.words or [])]


def merge(spans):
    spans = sorted(spans)
    out = []
    for a, b in spans:
        if out and a <= out[-1][1]:
            out[-1] = (out[-1][0], max(out[-1][1], b))
        else:
            out.append((a, b))
    return out


def subtract(spans, holes):
    out = []
    for a, b in spans:
        for h0, h1 in holes:
            if h1 <= a or h0 >= b:
                continue
            if h0 > a:
                out.append((a, h0))
            a = max(a, h1)
            if a >= b:
                break
        if a < b:
            out.append((a, b))
    return out


def plan(ws, total, keep, pre, post, entry_breath, quiet):
    spans = [(max(0.0, a - pre), min(total, b + post)) for a, b, _ in ws]
    # §28G ENTRY CAP / BREATH-A: keep the last slice of the entry inhale
    spans[0] = (max(0.0, ws[0][0] - entry_breath), spans[0][1])
    spans = merge(spans)
    # Whisper stretches word edges over adjacent silence: remove measured
    # silence from inside the word spans, leaving the padding either side.
    holes = [(s + post, e - pre) for s, e in quiet if e - pre - (s + post) > 0.05]
    spans = [(a, b) for a, b in subtract(spans, holes) if b - a > 0.05]
    spans = merge(spans + keep)  # §28G designed-silence list survives the trim
    cuts, cursor = [], 0.0
    for a, b in spans:
        if a - cursor > 0.01:
            cuts.append((round(cursor, 3), round(a, 3)))
        cursor = b
    if total - cursor > 0.01:
        cuts.append((round(cursor, 3), round(total, 3)))
    return spans, cuts


def has_video(src):
    probe = subprocess.run([FFMPEG, "-hide_banner", "-i", str(src)], capture_output=True, text=True).stderr
    return "Video:" in probe


def render(src, dst, spans):
    video = has_video(src)  # audio-only masters (§22U voice) have no video stream
    parts, labels = [], []
    for i, (a, b) in enumerate(spans):
        if video:
            parts.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}];")
        parts.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,"
                     f"afade=t=in:d=0.01,afade=t=out:st={max(0, b - a - 0.01)}:d=0.01[a{i}];")
        labels.append(f"[v{i}][a{i}]" if video else f"[a{i}]")
    if video:
        graph = "".join(parts) + "".join(labels) + f"concat=n={len(spans)}:v=1:a=1[v][a]"
        maps = ["-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "16", "-preset", "medium",
                "-c:a", "aac", "-b:a", "192k"]
    else:
        graph = "".join(parts) + "".join(labels) + f"concat=n={len(spans)}:v=0:a=1[a]"
        codec = ["-c:a", "libmp3lame", "-b:a", "192k"] if str(dst).endswith(".mp3") else ["-c:a", "aac", "-b:a", "192k"]
        maps = ["-map", "[a]"] + codec
    subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-i", str(src),
                    "-filter_complex", graph] + maps + [str(dst)], check=True)


def verify(dst, keep_count, model_name):
    ws = words(dst, model_name)
    total = duration(dst)
    gaps = [s for s in silences(dst) if s[1] - s[0] > MAX_GAP]
    report = {
        "first_word_s": round(ws[0][0], 3) if ws else None,
        "tail_after_last_word_s": round(total - ws[-1][1], 3) if ws else None,
        "gaps_over_0.4s": [(round(a, 3), round(b, 3)) for a, b in gaps],
    }
    ok = bool(ws) and ws[0][0] <= ENTRY_CAP and total - ws[-1][1] <= TAIL_CAP + 0.1 \
        and len(gaps) <= keep_count
    return ok, report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--out")
    ap.add_argument("--keep", nargs="*", default=[], help="designed silences START:END (s)")
    ap.add_argument("--model", default="base.en")
    ap.add_argument("--pre", type=float, default=0.06)
    ap.add_argument("--post", type=float, default=0.08)
    ap.add_argument("--entry-breath", type=float, default=0.12)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    src = Path(a.src)
    dst = Path(a.out) if a.out else src.with_suffix(".trim.mp4")
    if dst.resolve() == src.resolve():
        sys.exit("refusing to overwrite the original (E11)")
    keep = [tuple(float(x) for x in k.split(":")) for k in a.keep]

    ws = words(src, a.model)
    if not ws:
        print(json.dumps({"status": "TRIM_FAIL", "reason": "no words detected"}))
        sys.exit(2)
    total = duration(src)
    quiet = silences(src, min_dur=0.15)
    spans, cuts = plan(ws, total, keep, a.pre, a.post, a.entry_breath, quiet)
    result = {"src": str(src), "out": str(dst), "duration_in_s": round(total, 3),
              "cuts": cuts, "cut_total_s": round(sum(b - x for x, b in cuts), 3),
              "transcript": " ".join(w for _, _, w in ws)}
    if a.dry_run:
        print(json.dumps(result, indent=2))
        return
    render(src, dst, spans)
    ok, check = verify(dst, len(keep), a.model)
    result.update({"duration_out_s": round(duration(dst), 3), "verify": check,
                   "status": "PASS" if ok else "TRIM_FAIL"})
    print(json.dumps(result, indent=2))
    sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()
