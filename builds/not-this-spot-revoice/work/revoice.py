"""Re-voice one finished video on its own timings.
revoice.py X plan|gen|build
  plan : align script units to the original vocals (wordsX.json) -> planX.json
  gen  : TTS each chunk (eleven_multilingual_v2, Doctor-NTS, continuity context) -> gen/X_cNN.mp3
  build: cut the chunks into units, fit each to its original span, place, mix with the music -> outX.wav
"""
import json, re, sys, subprocess, difflib, os
import numpy as np, soundfile as sf
sys.path.insert(0, os.path.dirname(__file__))
from tts import tts

X, STEP = sys.argv[1], sys.argv[2]
SPEED = float(os.environ.get("SPEED", "1.1"))
SR = 44100
NUM = {"17": "seventeen", "34%": "thirty four percent", "10": "ten", "48": "forty eight", "60": "sixty",
       "71": "seventy one", "200": "two hundred", "000": "thousand", "200,000": "two hundred thousand", "34": "thirty four", "%": "percent",
       "1": "one", "2": "two", "3": "three", "71 year old": "seventy one year old"}


def toks(s):
    s = s.lower().replace("-", " ").replace("’", "'")
    out = []
    for t in s.split():
        t = t.strip('.,?!:;"')
        if t in NUM:
            out += NUM[t].split()
        elif t:
            out.append(re.sub(r"[^a-z0-9']", "", t))
    return [t for t in out if t]


def units():
    blocks, cur = {}, None
    for line in open("script.txt"):
        line = line.strip()
        if line.startswith("#"):
            cur = line[1:]; blocks[cur] = []
        elif line:
            blocks[cur].append(line)
    return blocks[X] + blocks["BODY"]


def align(unit_list, words):
    """words: [(start,end,text)] -> per unit (start,end) of its first/last matched word."""
    wt, wi = [], []
    for k, (s, e, t) in enumerate(words):
        for tk in toks(t):
            wt.append(tk); wi.append(k)
    ut, ui = [], []
    for u, line in enumerate(unit_list):
        for tk in toks(line):
            ut.append(tk); ui.append(u)
    sm = difflib.SequenceMatcher(None, ut, wt, autojunk=False)
    m = {}
    for a, b, n in sm.get_matching_blocks():
        for j in range(n):
            m[a + j] = wi[b + j]
    res = []
    for u in range(len(unit_list)):
        idx = [m[i] for i in range(len(ut)) if ui[i] == u and i in m]
        n = sum(1 for i in range(len(ut)) if ui[i] == u)
        res.append((words[min(idx)][0], words[max(idx)][1]) if idx and len(idx) >= 0.6 * n else None)
    return res


def fill(res):
    for u, r in enumerate(res):
        if r is None:
            p = next((res[k][1] for k in range(u - 1, -1, -1) if res[k]), 0.0)
            n = next((res[k][0] for k in range(u + 1, len(res)) if res[k]), p + 2)
            res[u] = (p + 0.1, n - 0.1)
    return res


def whisper_words(path):
    from faster_whisper import WhisperModel
    m = WhisperModel("medium.en", compute_type="int8")
    segs, _ = m.transcribe(path, word_timestamps=True)
    return [(w.start, w.end, w.word) for s in segs for w in s.words]


def load(path):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", path, "-ac", "1", "-ar", str(SR), f"/tmp/_{X}_l.wav"], check=True)
    a, _ = sf.read(f"/tmp/_{X}_l.wav", dtype="float32")
    return a


def tighten(a, lo, hi, db=-42):
    """move lo forward / hi back to where the voice is actually present (10 ms frames)."""
    fr = int(0.01 * SR); thr = 10 ** (db / 20)
    seg = a[lo:hi]
    if len(seg) < fr: return lo, hi
    rms = np.array([np.sqrt(np.mean(seg[i:i + fr] ** 2)) for i in range(0, len(seg) - fr, fr)])
    on = np.where(rms > thr)[0]
    if not len(on): return lo, hi
    return lo + max(0, on[0] - 1) * fr, lo + min(len(rms), on[-1] + 3) * fr


def stretch(a, factor):
    """factor = new_len / old_len (rubberband, pitch kept)."""
    if abs(factor - 1) < 0.01: return a
    sf.write(f"/tmp/_{X}_s.wav", a, SR)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"/tmp/_{X}_s.wav", "-af",
                    f"rubberband=tempo={1 / factor:.5f}:pitchq=quality:formant=preserved", f"/tmp/_{X}_t.wav"], check=True)
    b, _ = sf.read(f"/tmp/_{X}_t.wav", dtype="float32")
    return b


if STEP == "plan":
    U = units()
    W = [tuple(w) for w in json.load(open(f"words{X}.json"))]
    span = align(U, W)
    # units whisper-medium skipped: take them from the first transcript
    miss = [u for u in range(len(U)) if span[u] is None or span[u][1] - span[u][0] > 0.55 * len(U[u].split()) + 0.8]
    if miss:
        W2 = [tuple(w) for seg in json.load(open(f"hook{X}.json")) for w in seg["w"]]
        span2 = align(U, W2)
        for u in miss:
            if span2[u]: span[u] = span2[u]
        print("from first transcript:", miss)
    # tighten to where the original voice is audible
    ov = load(f"sep/htdemucs/full{X}/vocals.wav")
    fr = int(0.01 * SR); r = np.array([np.sqrt(np.mean(ov[i:i + fr] ** 2)) for i in range(0, len(ov) - fr, fr)])
    thr = 0.1 * np.sqrt(np.mean(r[r > np.percentile(r, 50)] ** 2))
    for u in range(len(U)):
        a0, a1 = int(span[u][0] * 100), int(span[u][1] * 100)
        on = np.where(r[max(0, a0 - 5):a1 + 5] > thr)[0]
        if len(on): span[u] = (max(0, a0 - 5) / 100 + on[0] / 100, max(0, a0 - 5) / 100 + (on[-1] + 1) / 100)
    span = fill(span)
    chunks, cur, chars = [], [], 0
    for u, line in enumerate(U):
        gap = span[u][0] - span[u - 1][1] if u else 0
        if cur and (chars + len(line) > 260 or gap > 0.7):
            chunks.append(cur); cur, chars = [], 0
        cur.append(u); chars += len(line) + 1
    chunks.append(cur)
    json.dump({"units": U, "span": span, "chunks": chunks}, open(f"plan{X}.json", "w"), indent=1)
    for c in chunks:
        print(f"{span[c[0]][0]:6.2f}-{span[c[-1]][1]:6.2f}", " | ".join(U[u] for u in c)[:120])

elif STEP == "gen":
    P = json.load(open(f"plan{X}.json")); U = P["units"]; os.makedirs("gen", exist_ok=True)
    only = set(map(int, sys.argv[3].split(","))) if len(sys.argv) > 3 else None
    for k, c in enumerate(P["chunks"]):
        out = f"gen/{X}_c{k:02d}.mp3"
        if (only is None and os.path.exists(out)) or (only is not None and k not in only): continue
        txt = " ".join(U[u] for u in c)
        prev = " ".join(U[u] for u in P["chunks"][k - 1]) if k else None
        nxt = " ".join(U[u] for u in P["chunks"][k + 1]) if k + 1 < len(P["chunks"]) else None
        tts(txt, out, SPEED, "eleven_multilingual_v2", prev=prev, nxt=nxt)
        print("gen", k, len(txt))

elif STEP == "build":
    P = json.load(open(f"plan{X}.json")); U = P["units"]; span = P["span"]
    orig = load(f"sep/htdemucs/full{X}/vocals.wav")
    total = len(orig)
    track = np.zeros(total + SR * 5, np.float32)
    report = []
    for k, c in enumerate(P["chunks"]):
        cands = []
        for path in [f"gen/{X}_c{k:02d}.mp3", f"gen/{X}_c{k:02d}.s110.mp3"]:
            if not os.path.exists(path): continue
            a = load(path)
            cache = path.rsplit(".mp3", 1)[0] + ".words.json"
            if not os.path.exists(cache):
                json.dump(whisper_words(path), open(cache, "w"))
            cw = [tuple(w) for w in json.load(open(cache))]
            sub = fill(align([U[u] for u in c], cw))
            # cut points: middle of the gap between units
            pieces = []
            for i in range(len(c)):
                s = sub[i][0] if i == 0 else (sub[i - 1][1] + sub[i][0]) / 2
                e = sub[i][1] if i == len(c) - 1 else (sub[i][1] + sub[i + 1][0]) / 2
                lo, hi = tighten(a, 0 if i == 0 else int(s * SR), len(a) if i == len(c) - 1 else int(e * SR))
                pieces.append(a[lo:hi].copy())
            cands.append((path, pieces))
        for i, u in enumerate(c):
            o0, o1 = span[u]
            target = o1 - o0 + 0.04
            nxt = span[u + 1][0] if u + 1 < len(U) else o1 + 1.0
            room = nxt - o0 - 0.05
            # the read that needs the least stretching for this sentence
            path, pieces = min(cands, key=lambda cp: abs(np.log(target / (len(cp[1][i]) / SR))))
            force = dict(x.split(":") for x in os.environ.get("FORCE", "").split(",") if x)
            if str(u) in force:
                path, pieces = next(cp for cp in cands if force[str(u)] in cp[0])
            piece = pieces[i]
            f = target / (len(piece) / SR)            # >1 slows, <1 speeds up
            f = min(max(f, 0.80), 1.15)
            if len(piece) / SR * f > room: f = room / (len(piece) / SR)
            piece = stretch(piece, f)
            fade = int(0.012 * SR)
            piece[:fade] *= np.linspace(0, 1, fade); piece[-fade:] *= np.linspace(1, 0, fade)
            st = int((o0 - 0.02) * SR)
            track[st:st + len(piece)] += piece
            report.append({"u": u, "t": round(o0, 2), "tempo": round(1 / f, 3), "len": round(len(piece) / SR, 2),
                           "orig": round(o1 - o0, 2), "src": path[-9:], "text": U[u][:50]})
    track = track[:total]
    # loudness match to the original voice (speech-active RMS)
    def arms(x):
        fr = int(0.05 * SR); r = np.array([np.sqrt(np.mean(x[i:i + fr] ** 2)) for i in range(0, len(x) - fr, fr)])
        return np.sqrt(np.mean(r[r > np.percentile(r, 60)] ** 2))
    track *= arms(orig) / arms(track)
    sf.write(f"vo{X}.wav", track, SR)
    json.dump(report, open(f"report{X}.json", "w"), indent=1)
    t = [r["tempo"] for r in report]
    print(f"units {len(t)} | tempo min {min(t)} max {max(t)} median {np.median(t):.3f} | >1.10: {sum(x > 1.10 for x in t)}")
