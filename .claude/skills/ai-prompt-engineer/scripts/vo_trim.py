#!/usr/bin/env python3
"""VO trim — shorten air and remove inhales in an audio-only voice take, from the waveform.

Why not trim.py (transcript word edges): Whisper ends words early (clips the decay of the last
word) and starts them early (swallows the inhale into the word). Here:
  * frames every 10 ms: level (dBFS), spectral centroid, flatness, share of energy 80–400 Hz
  * KEEP = level above FLOOR (-60 dBFS) — every word keeps its natural decay
  * BREATH = a run >= BREATH_MIN (0.12 s) of frames that are quiet (-62..-34 dB), noise-like
    (flatness >= 0.18), mid-band (centroid 1.2–3.4 kHz) and not voiced-low (80–400 Hz share < 0.18).
    Sibilants (centroid > 3.4 kHz), stop releases (< 0.12 s) and word decays (low-band share) are not
    breaths. Breaths are removed from KEEP.
  * a breath is only cut at a phrase boundary (the word before it closes a phrase with , . ? ! in the
    script): mid-phrase fricatives like the "th" of "through" match the breath profile and must stay.
  * silences shorter than MERGE (0.08 s) stay as they are (stop closures, rhythm inside a phrase);
    longer ones become PAUSE_SENT (0.28 s) after . ? ! , and PAUSE_WORD (0.10 s) elsewhere, never longer
    than they were. Sentence ends are the only thing taken from the transcript.
  * head: 10 ms before the first kept frame; tail: until the level stays under FLOOR, + 30 ms, 20 ms fade.
Report + verification on the output: breaths left, tail level, gaps > 0.4 s.
"""
import argparse, json, subprocess, sys
import numpy as np, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
SR, HOP, WIN = 16000, 160, 480
FLOOR, BREATH_MIN, MERGE = -60.0, 0.12, 0.08
PAUSE_SENT, PAUSE_WORD, HEAD, TAIL = 0.28, 0.10, 0.01, 0.03

def load(path, sr=SR):
    raw = subprocess.run([FF, "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"], capture_output=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768

def features(x):
    n = max(0, (len(x) - WIN) // HOP + 1)
    fr = np.fft.rfftfreq(WIN, 1 / SR); w = np.hanning(WIN); band = (fr > 80) & (fr < 400)
    db = np.empty(n); cen = np.empty(n); flat = np.empty(n); low = np.empty(n)
    for i in range(n):
        s = x[i * HOP:i * HOP + WIN]
        db[i] = 20 * np.log10(np.sqrt((s ** 2).mean()) + 1e-9)
        S = np.abs(np.fft.rfft(s * w)) + 1e-9
        cen[i] = (S * fr).sum() / S.sum(); flat[i] = np.exp(np.log(S).mean()) / S.mean(); low[i] = S[band].sum() / S.sum()
    return db, cen, flat, low

def runs(mask):
    out, i, n = [], 0, len(mask)
    while i < n:
        if mask[i]:
            j = i
            while j < n and mask[j]: j += 1
            out.append((i, j)); i = j
        else: i += 1
    return out

def t(i): return i * HOP / SR

def breaths(db, cen, flat, low, min_len=BREATH_MIN):
    cand = (db > -62) & (db < -34) & (flat >= 0.18) & (cen > 1200) & (cen < 3400) & (low < 0.18)
    # allow 1-frame holes inside a breath
    c = cand.copy()
    for i in range(1, len(c) - 1):
        if not cand[i] and cand[i - 1] and cand[i + 1]: c[i] = True
    return [(a, b) for a, b in runs(c) if t(b) - t(a) >= min_len]

_MODEL = None
def boundaries(path, script):
    """Ends of words that close a phrase (, . ? ! in the SCRIPT, aligned to the transcript)."""
    import difflib, re
    from faster_whisper import WhisperModel
    global _MODEL
    _MODEL = _MODEL or WhisperModel("medium.en", compute_type="int8")
    segs, _ = _MODEL.transcribe(path, word_timestamps=True, language="en")
    ws = [(w.end, w.word.strip()) for s in segs for w in s.words]
    norm = lambda s: re.sub(r"[^a-z0-9']", "", s.lower())
    if not script:
        return [e for e, w in ws if w[-1:] in ".?!,"]
    toks = open(script).read().split()
    sm = difflib.SequenceMatcher(None, [norm(t) for t in toks], [norm(w) for _, w in ws], autojunk=False)
    ends = []
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            if toks[blk.a + k].rstrip('"')[-1:] in ".?!,": ends.append(ws[blk.b + k][0])
    return ends

def at_boundary(a, b, ends):
    # a breath is only taken at a phrase boundary: a phrase-closing word ended shortly before it
    return any(t(a) - 0.6 <= e <= t(a) + 0.1 for e in ends)

def plan(x, path, script):
    db, cen, flat, low = features(x)
    keep = db > FLOOR
    ends = boundaries(path, script)
    br = [(a, b) for a, b in breaths(db, cen, flat, low) if at_boundary(a, b, ends)]
    for a, b in br: keep[max(0, a - 1):b + 1] = False
    spans = [(a, b) for a, b in runs(keep) if t(b) - t(a) >= 0.03]   # drop clicks
    merged = []
    for a, b in spans:
        if merged and t(a) - t(merged[-1][1]) < MERGE: merged[-1] = (merged[-1][0], b)
        else: merged.append((a, b))
    return [(t(a), t(b) + WIN / SR) for a, b in merged], [(round(t(a), 2), round(t(b), 2)) for a, b in br], ends

def render(src, dst, spans, sents, total):
    pieces, prev = [], None
    for k, (a, b) in enumerate(spans):
        if k == 0: a = max(0.0, a - HEAD)
        if k == len(spans) - 1: b = min(total, b + TAIL)
        if prev is not None:
            sent = any(prev - 0.4 <= s <= a + 0.05 for s in sents)
            pieces.append(("gap", min(a - prev, PAUSE_SENT if sent else PAUSE_WORD)))
        pieces.append(("seg", a, b)); prev = b
    parts, labels = [], []
    for n, pc in enumerate(pieces):
        if pc[0] == "seg":
            a, b = pc[1], pc[2]; d = b - a
            last = n == len(pieces) - 1
            fade_out = f",afade=t=out:st={max(0, d - 0.02):.4f}:d=0.02" if last else f",afade=t=out:st={max(0, d - 0.006):.4f}:d=0.006"
            parts.append(f"[0:a]atrim={a:.4f}:{b:.4f},asetpts=PTS-STARTPTS,aresample=44100,aformat=channel_layouts=mono,afade=t=in:d=0.006{fade_out}[s{n}];")
        else:
            parts.append(f"anullsrc=r=44100:cl=mono,atrim=0:{max(0.001, pc[1]):.4f}[s{n}];")
        labels.append(f"[s{n}]")
    graph = "".join(parts) + "".join(labels) + f"concat=n={len(pieces)}:v=0:a=1[a]"
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-i", src, "-filter_complex", graph,
                    "-map", "[a]", "-c:a", "libmp3lame", "-b:a", "192k", dst], check=True)

def verify(dst, script):
    x = load(dst); db, cen, flat, low = features(x)
    ends = boundaries(dst, script)
    left = [(round(t(a), 2), round(t(b), 2)) for a, b in breaths(db, cen, flat, low, BREATH_MIN + 0.02) if at_boundary(a, b, ends)]
    quiet = db < -70
    gaps = [(round(t(a), 2), round(t(b), 2)) for a, b in runs(quiet) if t(b) - t(a) > 0.4 and a > 0 and b < len(db)]
    # the word ended by itself: level before the final fade already near the floor
    last_kept = np.where(db > FLOOR)[0]
    tail_ok = bool(len(last_kept)) and db[last_kept[-1]] < -45
    return dict(duration_s=round(len(x) / SR, 3), breaths_left=left, gaps_over_0_4=gaps,
                tail_last_db=round(float(db[last_kept[-1]]), 1) if len(last_kept) else None,
                status="PASS" if not left and not gaps and tail_ok else "FAIL")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("--out", required=True)
    ap.add_argument("--script", help="the part's script lines (punctuation marks the phrase boundaries)")
    a = ap.parse_args()
    x = load(a.src); total = len(x) / SR
    db0 = features(x)[0]
    spans, br, sents = plan(x, a.src, a.script)
    render(a.src, a.out, spans, sents, total)
    rep = dict(src=a.src, out=a.out, duration_in_s=round(total, 3), breaths_cut=br,
               source_end_db=round(float(db0[-1]), 1), source_end_clipped=bool(db0[-1] > -45),
               verify=verify(a.out, a.script))
    print(json.dumps(rep)); sys.exit(0 if rep["verify"]["status"] == "PASS" else 2)
