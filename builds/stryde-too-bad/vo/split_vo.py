#!/usr/bin/env python3
"""stryde-too-bad: find HK1|BODY1|HK2|BODY2 in one take (word timestamps, cut mid-gap) — the build-local
form of cut_points.py for two hooks each with its own body. Usage: split_vo.py TAKE.mp3 -> TAKE.mp3.cuts.json"""
import sys, re, json, difflib
from faster_whisper import WhisperModel
SRC = sys.argv[1]; ORDER = sys.argv[2].split(",") if len(sys.argv) > 2 else ["HK1", "BODY1", "HK2", "BODY2"]
NUM = {",000": "", "200": "two hundred thousand", "200000": "two hundred thousand", "17": "seventeen", "34": "thirty four", "60": "sixty"}
def norm(s):
    s = s.lower().replace("%", " percent").replace("-", " ")
    s = re.sub(r"(\d)[, ](\d{3})", r"\1\2", s)
    for k, v in NUM.items(): s = re.sub(rf"\b{k}\b", v, s)
    return re.sub(r"[^a-z' ]", " ", s).split()
parts = {k: norm(open(f"{k}.lines.txt").read().replace("\n", " ")) for k in ORDER}
ref = sum((parts[k] for k in ORDER), [])
m = WhisperModel("medium.en", compute_type="int8")
segs, info = m.transcribe(SRC, word_timestamps=True, language="en", beam_size=5)
W = [(t, w.start, w.end) for s in segs for w in s.words for t in norm(w.word)]
hyp = [w[0] for w in W]
sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
rmap = {blk.a + k: blk.b + k for blk in sm.get_matching_blocks() for k in range(blk.size)}
cuts, i = [], 0
for k in ORDER[:-1]:
    i += len(parts[k])
    last, first = rmap[i - 1], rmap[i]
    cuts.append(round((W[last][2] + W[first][1]) / 2, 3))
b = [0.0] + cuts + [round(info.duration, 3)]
out = {"src": SRC, "duration": round(info.duration, 3), "cuts": cuts, "ranges": {k: [b[j], b[j + 1]] for j, k in enumerate(ORDER)},
       "diff": [(t, " ".join(ref[a:b_]), " ".join(hyp[c:d])) for t, a, b_, c, d in sm.get_opcodes() if t != "equal"]}
json.dump(out, open(SRC + ".cuts.json", "w"), indent=1)  # optional 2nd arg: part order, e.g. HK1,BODY1
print(json.dumps({k: out[k] for k in ("duration", "cuts")}), out["diff"])
