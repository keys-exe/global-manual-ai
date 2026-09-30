#!/usr/bin/env python3
"""E11 trim pass — cut dead air and inhales from a dialogue clip.

Usage:
  trim.py IN.mp4 [--out OUT.mp4] [--keep START:END ...] [--model base.en]
          [--pre 0.12] [--post 0.25] [--entry-breath 0.12]
          [--style natural|medium|tight] [--sentence-pause S] [--comma-pause S]
          [--word-pause S] [--max-wpm 210] [--dry-run]

Styles (§22U, 2026-09-29): natural (default, talking heads — 0.45/0.25/0.3s),
medium (the Kling voice-clone source, §22U step 3 — 0.25/0.15/0.15s), tight (0/0/0).
An explicit --sentence-pause / --comma-pause / --word-pause overrides the style.

Natural pace (E11, 2026-09-28 — "the trimming should not be too fast"): after the
cut, each sentence end keeps --sentence-pause, each comma/colon/semicolon/dash
--comma-pause, and every other word gap up to --word-pause (or the original gap,
if shorter). No speed change.

No tight cuts (E11, 2026-09-28 — "I don't like tight cuts… let it finish what she is
saying"): every word keeps --pre before and --post after its transcript edges, its
decay is kept down to QUIET_DB (-50 dB, not -40), a pause inside a phrase stays as
voiced up to --word-pause, and every cut fades out over 40 ms, never a click-cut.

Writes <IN>.trim.mp4 (never overwrites the input) and prints a JSON report:
cut list, keep-spans and the E1 verification result. Exit code 0 = pass,
2 = TRIM_FAIL (E2), 1 = error.

Setup (per session): pip install imageio-ffmpeg faster-whisper
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

import imageio_ffmpeg

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

# pauses kept after a sentence end, a comma, and inside a phrase (s)
STYLES = {"natural": (0.45, 0.25, 0.3), "medium": (0.25, 0.15, 0.15), "tight": (0.0, 0.0, 0.0)}
NOISE_DB = -40      # E1 / §28G silence threshold
QUIET_DB = -50      # E11 no tight cuts: only audio below this is cut — a word's decay is kept
MAX_GAP = 0.6       # E1: no silence > 0.6s except keep-list (same limit as the VO house cut)
FADE_IN, FADE_OUT = 0.01, 0.04
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


SENTENCE_END = (".", "?", "!")
CLAUSE_END = (",", ";", ":", "-", "\u2014", "\u2013")


def pause_after(word, pace):
    w = word.rstrip("\"')\u201d\u2019")
    if w.endswith(SENTENCE_END):
        return pace["sentence"]
    if w.endswith(CLAUSE_END):
        return pace["comma"]
    return pace["word"]


def plan(ws, total, keep, pre, post, entry_breath, quiet, pace=None):
    spans = [(max(0.0, a - pre), min(total, b + post)) for a, b, _ in ws]
    # §28G ENTRY CAP / BREATH-A: keep the last slice of the entry inhale
    spans[0] = (max(0.0, ws[0][0] - entry_breath), spans[0][1])
    spans = merge(spans)
    # Whisper stretches word edges over adjacent silence: remove measured
    # silence from inside the word spans, leaving the padding either side.
    holes = [(s + post, e - pre) for s, e in quiet if e - pre - (s + post) > 0.05]
    spans = [(a, b) for a, b in subtract(spans, holes) if b - a > 0.05]
    if pace:  # E11 natural pace: give each word its pause back, never more than the gap
        for (_, end, w), nxt in zip(ws, ws[1:]):  # none after the last word (E1 tail cap)
            limit = nxt[0] - pre
            p = pause_after(w, pace)
            if limit > end and p > 0:
                spans.append((end, min(end + p, limit)))
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
                     f"afade=t=in:d={FADE_IN},afade=t=out:st={max(0, b - a - FADE_OUT)}:d={FADE_OUT}[a{i}];")
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


def verify(dst, keep_count, model_name, post=0.0):
    ws = words(dst, model_name)
    total = duration(dst)
    gaps = [s for s in silences(dst) if s[1] - s[0] > MAX_GAP]
    report = {
        "first_word_s": round(ws[0][0], 3) if ws else None,
        "tail_after_last_word_s": round(total - ws[-1][1], 3) if ws else None,
        "gaps_over_0.6s": [(round(a, 3), round(b, 3)) for a, b in gaps],
    }
    ok = bool(ws) and ws[0][0] <= ENTRY_CAP and total - ws[-1][1] <= TAIL_CAP + post + 0.1 \
        and len(gaps) <= keep_count
    return ok, report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--out")
    ap.add_argument("--keep", nargs="*", default=[], help="designed silences START:END (s)")
    ap.add_argument("--model", default="base.en")
    ap.add_argument("--pre", type=float, default=0.12, help="kept before each word (no tight cuts)")
    ap.add_argument("--post", type=float, default=0.25, help="kept after each word so it finishes (no tight cuts)")
    ap.add_argument("--entry-breath", type=float, default=0.12)
    ap.add_argument("--style", choices=sorted(STYLES), default="natural",
                    help="pause preset: natural (talking heads), medium (voice-clone source), tight")
    ap.add_argument("--sentence-pause", type=float, default=None, help="pause kept after . ? ! (overrides --style)")
    ap.add_argument("--comma-pause", type=float, default=None, help="pause kept after , ; : dash (overrides --style)")
    ap.add_argument("--word-pause", type=float, default=None, help="max pause kept inside a phrase (overrides --style)")
    ap.add_argument("--max-wpm", type=int, default=210,
                    help="pace ceiling on the trimmed clip, gated when it runs 30s or more (§22U step 14)")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--mode", type=int, default=1, help="§18A mode of the build; 4 and 5 are refused (§24L)")
    a = ap.parse_args()
    if a.mode in (4, 5):
        print(json.dumps({"status": "REFUSED", "reason": "no trimming in the film modes (§24L): Mode 4/5 clips play whole"}))
        sys.exit(2)

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
    # Air is what is below QUIET_DB (-50 dB, so a word's decay is kept), plus any gap longer than MAX_GAP
    # below NOISE_DB (-40 dB): verify() fails such a gap, so room tone between -50 and -40 dB in a long
    # pause must be cut too (the --pre/--post padding still keeps every word ending) (2026-09-29).
    quiet = merge(silences(src, noise_db=QUIET_DB, min_dur=0.15) + silences(src, noise_db=NOISE_DB, min_dur=MAX_GAP))
    st = STYLES[a.style]
    pace = {"style": a.style,
            "sentence": st[0] if a.sentence_pause is None else a.sentence_pause,
            "comma": st[1] if a.comma_pause is None else a.comma_pause,
            "word": st[2] if a.word_pause is None else a.word_pause}
    spans, cuts = plan(ws, total, keep, a.pre, a.post, a.entry_breath, quiet, pace)
    result = {"src": str(src), "out": str(dst), "duration_in_s": round(total, 3),
              "pace": pace, "cuts": cuts, "cut_total_s": round(sum(b - x for x, b in cuts), 3),
              "transcript": " ".join(w for _, _, w in ws)}
    if a.dry_run:
        print(json.dumps(result, indent=2))
        return
    render(src, dst, spans)
    # the tail may hold the --post padding the trim itself keeps after the last word (no tight cuts)
    ok, check = verify(dst, len(keep), a.model, a.post)
    out_s = duration(dst)
    wpm = round(len(ws) / out_s * 60, 1) if out_s else None
    check["wpm"] = wpm
    if a.style == "natural" and out_s >= 30 and wpm and wpm > a.max_wpm:
        ok = False
        check["pace_fail"] = f"{wpm} wpm > {a.max_wpm}: re-voice slower (§22U step 9), never trim tighter"
    result.update({"duration_out_s": round(out_s, 3), "verify": check,
                   "status": "PASS" if ok else "TRIM_FAIL"})
    print(json.dumps(result, indent=2))
    sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()
