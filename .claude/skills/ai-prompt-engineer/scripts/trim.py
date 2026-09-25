#!/usr/bin/env python3
"""E11 trim pass — cut dead air and breaths from a dialogue clip or a voice file.

Usage:
  trim.py IN.(mp4|mp3|wav|m4a) [--out OUT] [--keep START:END ...] [--model small.en]
          [--pre 0.06] [--post 0.08] [--entry-breath 0] [--cut-all]
          [--mute-under 0.15] [--breath-drop 15] [--min-breath 0.06] [--dry-run]

Breaths are found in the audio itself (V7.60.8), not from the transcript: a
breath is a run of >= --min-breath seconds with no voiced pitch, sitting
--breath-drop dB or more under the speech level, outside every word's voiced
core. Word edges are snapped to where the voice starts and stops, so a breath
that Whisper folded into a word is still removed.

Removal: head and tail are always cut. Between words, a clip with picture has
each removed stretch shorter than --mute-under muted (picture untouched, no
micro jump cut) and every longer one cut. Audio-only files, and --cut-all,
cut every stretch.

Writes <IN>.trim.<ext> (never overwrites the input) and prints a JSON report:
cut list, mute list, breaths in/out and the E1 verification. Exit 0 = pass,
2 = TRIM_FAIL (E2), 1 = error.

Setup (per session): pip install imageio-ffmpeg faster-whisper
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

import imageio_ffmpeg
import numpy as np

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
NOISE_DB = -40      # E1 / §28G silence threshold
MAX_GAP = 0.4       # E1: no silence > 0.4s except keep-list
ENTRY_CAP = 0.5     # §28G: first word inside 0.5s
TAIL_CAP = 0.3      # E1: tail ends <= 0.3s after the last word

SR = 16000          # analysis rate
WIN = 0.025         # analysis window (s)
HOP = 0.010         # analysis hop (s)
VOICED_R = 0.45     # normalised autocorrelation peak that counts as pitch
CORE_GUARD = 0.04   # kept either side of a word's voiced core (consonant onset/release)
MUTE_GAIN = 0.018   # about -35 dB: a muted breath drops under the breath floor


def probe(path):
    return subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)],
                          capture_output=True, text=True).stderr


def duration(path):
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", probe(path)).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def has_video(path):
    return bool(re.search(r"Stream #.*Video:", probe(path)))


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


# --- breath detection -------------------------------------------------------

def frames(path):
    """Per-frame level (dBFS) and voicing, from 16 kHz mono PCM."""
    raw = subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-i", str(path),
                          "-vn", "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    win, hop = int(WIN * SR), int(HOP * SR)
    n = max(0, 1 + (len(x) - win) // hop)
    lo, hi = SR // 400, SR // 75            # pitch lags for 75-400 Hz
    db = np.full(n, -120.0)
    voiced = np.zeros(n, dtype=bool)
    for i in range(n):
        f = x[i * hop:i * hop + win]
        rms = float(np.sqrt(np.mean(f * f)))
        if rms < 1e-6:
            continue
        db[i] = 20 * np.log10(rms)
        f = f - f.mean()
        ac = np.correlate(f, f, mode="full")[win - 1:]
        if ac[0] > 0:
            voiced[i] = ac[lo:hi].max() / ac[0] >= VOICED_R
    return db, voiced


def runs(mask):
    out, start = [], None
    for i, m in enumerate(mask):
        if m and start is None:
            start = i
        elif not m and start is not None:
            out.append((start, i))
            start = None
    if start is not None:
        out.append((start, len(mask)))
    return out


def cores(ws, voiced, total):
    """Each word's voiced core, widened by CORE_GUARD for unvoiced consonants."""
    out = []
    for a, b, _ in ws:
        i0, i1 = int(a / HOP), min(len(voiced), int(b / HOP) + 1)
        idx = np.flatnonzero(voiced[i0:i1])
        if len(idx):
            a, b = (i0 + idx[0]) * HOP, (i0 + idx[-1]) * HOP + WIN
        out.append((max(0.0, a - CORE_GUARD), min(total, b + CORE_GUARD)))
    return merge(out)


def breaths(db, voiced, word_cores, drop, min_len):
    """Unvoiced runs well under speech level, outside every word core."""
    if not voiced.any():
        return []
    speech = float(np.median(db[voiced]))
    cand = (~voiced) & (db <= speech - drop) & (db >= speech - 40)
    t = np.arange(len(db)) * HOP
    for a, b in word_cores:
        cand[(t + WIN > a) & (t < b)] = False
    return [(round(s * HOP, 3), round(e * HOP + WIN - HOP, 3))
            for s, e in runs(cand) if (e - s) * HOP >= min_len]


# --- planning ---------------------------------------------------------------

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


def overlaps(span, spans):
    return any(a < span[1] and b > span[0] for a, b in spans)


def plan(word_cores, total, keep, pre, post, entry_breath, quiet, found, mute_under):
    spans = [(max(0.0, a - pre), min(total, b + post)) for a, b in word_cores]
    if entry_breath > 0:   # optional: keep the tail of the entry inhale (default 0, V7.60.8)
        spans[0] = (max(0.0, word_cores[0][0] - entry_breath), spans[0][1])
    spans = merge(spans)
    # Measured silence and detected breaths come out of the padded spans;
    # the voiced cores never do (breaths are found outside them).
    holes = [(s + post, e - pre) for s, e in quiet if e - pre - (s + post) > 0.05]
    holes = merge(holes + [b for b in found if not overlaps(b, keep)])
    spans = [(a, b) for a, b in subtract(spans, holes) if b - a > 0.05]
    spans = merge(spans + keep)  # §28G designed-silence list survives the trim
    segs, cuts, mutes, cursor = [], [], [], 0.0
    for i, (a, b) in enumerate(spans):
        gap = (round(cursor, 3), round(a, 3))
        if gap[1] - gap[0] > 0.01:
            interior = i > 0
            if interior and gap[1] - gap[0] < mute_under:
                mutes.append(gap)
                segs.append((gap[0], gap[1], MUTE_GAIN))
            else:
                cuts.append(gap)
        segs.append((a, b, 1.0))
        cursor = b
    if total - cursor > 0.01:
        cuts.append((round(cursor, 3), round(total, 3)))
    return segs, cuts, mutes


def render(src, dst, segs, video):
    n, parts, labels = len(segs), [], []
    for i, (a, b, g) in enumerate(segs):
        if video:
            parts.append(f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v{i}];")
        parts.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,volume={g},"
                     f"afade=t=in:d=0.01,afade=t=out:st={max(0, b - a - 0.01)}:d=0.01[a{i}];")
        labels.append(f"[v{i}][a{i}]" if video else f"[a{i}]")
    graph = "".join(parts) + "".join(labels) + \
        (f"concat=n={n}:v=1:a=1[v][a]" if video else f"concat=n={n}:v=0:a=1[a]")
    ext = dst.suffix.lower()
    if video:
        codec = ["-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "16",
                 "-preset", "medium", "-c:a", "aac", "-b:a", "192k"]
    elif ext == ".mp3":
        codec = ["-map", "[a]", "-c:a", "libmp3lame", "-b:a", "192k"]
    elif ext == ".wav":
        codec = ["-map", "[a]", "-c:a", "pcm_s16le"]
    else:
        codec = ["-map", "[a]", "-c:a", "aac", "-b:a", "192k"]
    subprocess.run([FFMPEG, "-hide_banner", "-loglevel", "error", "-y", "-i", str(src),
                    "-filter_complex", graph, *codec, str(dst)], check=True)


def verify(dst, keep_count, kept_breaths, model_name, drop, min_len):
    ws = words(dst, model_name)
    total = duration(dst)
    gaps = [s for s in silences(dst) if s[1] - s[0] > MAX_GAP]
    left = []
    if ws:
        db, voiced = frames(dst)
        left = breaths(db, voiced, cores(ws, voiced, total), drop, min_len)
    report = {
        "first_word_s": round(ws[0][0], 3) if ws else None,
        "tail_after_last_word_s": round(total - ws[-1][1], 3) if ws else None,
        "gaps_over_0.4s": [(round(a, 3), round(b, 3)) for a, b in gaps],
        "breaths_out": left,
    }
    ok = bool(ws) and ws[0][0] <= ENTRY_CAP and total - ws[-1][1] <= TAIL_CAP + 0.1 \
        and len(gaps) <= keep_count and len(left) <= kept_breaths
    return ok, report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--out")
    ap.add_argument("--keep", nargs="*", default=[], help="designed silences START:END (s)")
    ap.add_argument("--model", default="small.en")
    ap.add_argument("--pre", type=float, default=0.06)
    ap.add_argument("--post", type=float, default=0.08)
    ap.add_argument("--entry-breath", type=float, default=0.0)
    ap.add_argument("--cut-all", action="store_true", help="cut every breath, never mute")
    ap.add_argument("--mute-under", type=float, default=0.15)
    ap.add_argument("--breath-drop", type=float, default=15.0,
                    help="dB under the speech level a breath sits (lower = more sensitive)")
    ap.add_argument("--min-breath", type=float, default=0.06)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    src = Path(a.src)
    dst = Path(a.out) if a.out else src.with_suffix(".trim" + src.suffix)
    if dst.resolve() == src.resolve():
        sys.exit("refusing to overwrite the original (E11)")
    keep = [tuple(float(x) for x in k.split(":")) for k in a.keep]
    video = has_video(src) and dst.suffix.lower() in (".mp4", ".mov", ".m4v")
    mute_under = 0.0 if (a.cut_all or not video) else a.mute_under

    ws = words(src, a.model)
    if not ws:
        print(json.dumps({"status": "TRIM_FAIL", "reason": "no words detected"}))
        sys.exit(2)
    total = duration(src)
    db, voiced = frames(src)
    word_cores = cores(ws, voiced, total)
    found = breaths(db, voiced, word_cores, a.breath_drop, a.min_breath)
    kept_breaths = sum(overlaps(b, keep) for b in found)
    quiet = silences(src, min_dur=0.15)
    segs, cuts, mutes = plan(word_cores, total, keep, a.pre, a.post, a.entry_breath,
                             quiet, found, mute_under)
    result = {"src": str(src), "out": str(dst), "video": video,
              "duration_in_s": round(total, 3), "breaths_in": found,
              "cuts": cuts, "mutes": mutes,
              "cut_total_s": round(sum(b - x for x, b in cuts), 3),
              "transcript": " ".join(w for _, _, w in ws)}
    if a.dry_run:
        print(json.dumps(result, indent=2))
        return
    render(src, dst, segs, video)
    ok, check = verify(dst, len(keep), kept_breaths, a.model, a.breath_drop, a.min_breath)
    result.update({"duration_out_s": round(duration(dst), 3), "verify": check,
                   "status": "PASS" if ok else "TRIM_FAIL"})
    print(json.dumps(result, indent=2))
    sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()
