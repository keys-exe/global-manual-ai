"""§22U step 12 — find the HK1|HK2|HK3|BODY boundaries in one house-cut take by word timestamps (cut mid-gap).

Usage (run in the build's vo/ folder, next to HK1.lines.txt … BODY.lines.txt): cut_points.py TAKE.mp3 -> TAKE.mp3.cuts.json
"""
import json, re, sys, difflib
from faster_whisper import WhisperModel
SRC = sys.argv[1]
NUM = {"200000": "two hundred thousand", "17": "seventeen", "34": "thirty four", "30": "thirty", "60": "sixty", "10": "ten", "2": "two"}
def norm(s):
    s = s.lower().replace("%", " percent").replace("-", " ")
    s = re.sub(r"(\d)[, ](\d{3})", r"\1\2", s)
    for k, v in NUM.items(): s = re.sub(rf"\b{k}\b", v, s)
    return re.sub(r"[^a-z' ]", " ", s).split()
parts = {k: norm(open(f"{k}.lines.txt").read().replace("\n", " ")) for k in ["HK1", "HK2", "HK3", "BODY"]}
ref = parts["HK1"] + parts["HK2"] + parts["HK3"] + parts["BODY"]
m = WhisperModel("medium.en", compute_type="int8")
segs, info = m.transcribe(SRC, word_timestamps=True, language="en", beam_size=5)
W = [(t, w.start, w.end) for s in segs for w in s.words for t in norm(w.word)]
hyp = [w[0] for w in W]
sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
rmap = {blk.a + k: blk.b + k for blk in sm.get_matching_blocks() for k in range(blk.size)}
cuts, i = [], 0
for k in ["HK1", "HK2", "HK3"]:
    i += len(parts[k])
    last, first = rmap[i - 1], rmap[i]
    cuts.append(round((W[last][2] + W[first][1]) / 2, 3))
out = {"src": SRC, "duration": round(info.duration, 3), "cuts": cuts,
       "ranges": {"HK1": [0.0, cuts[0]], "HK2": [cuts[0], cuts[1]], "HK3": [cuts[1], cuts[2]], "BODY": [cuts[2], round(info.duration, 3)]},
       "diff": [(t, " ".join(ref[a:b]), " ".join(hyp[c:d])) for t, a, b, c, d in sm.get_opcodes() if t != "equal"]}
json.dump(out, open(SRC + ".cuts.json", "w"), indent=1)
print(json.dumps({k: out[k] for k in ("duration", "cuts", "ranges")}), out["diff"])
