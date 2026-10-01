#!/usr/bin/env python3
"""Take check (§22U step 10, talking-head task): transcript vs script word for word + HK1|HK2|HK3|BODY cut points.
In-build helper because cut_points.py's number map lacks 5,000 / 70 million. Usage (in vo/): take_check.py T2.mp3"""
import json, re, sys, difflib
from faster_whisper import WhisperModel
SRC = sys.argv[1]
TOK = {"5": "five", ",000": "thousand", "70": "seventy", "17": "seventeen", "34": "thirty four", "40": "forty", "30": "thirty",
       "60": "sixty", "10": "ten", "2": "two", "3": "three", "200": "two hundred", "%": "percent"}
SAME = {("body", "weight"): "bodyweight", ("any", "more"): "anymore"}
def norm(s):
    s = s.lower().replace("-", " ").replace("%", " percent").replace("bodyweight", "body weight").replace("any more", "anymore")
    return re.sub(r"[^a-z' ]", " ", s).split()
def ntok(w):
    k = w.strip().strip(".").strip()
    return TOK[k].split() if k in TOK else norm(w)
parts = {k: norm(open(f"{k}.lines.txt").read()) for k in ["HK1", "HK2", "HK3", "BODY"]}
ref = sum(parts.values(), [])
m = WhisperModel("small.en", compute_type="int8")
segs, info = m.transcribe(SRC, word_timestamps=True, language="en")
W = [(t, w.start, w.end) for s in segs for w in s.words for t in ntok(w.word)]
hyp = [w[0] for w in W]
sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
IGN = {("patellar", "patella"), ("stryde", "stride"), ("two centimetres", "cm"), ("sores", "saws")}
diff = [(t, " ".join(ref[a:b]), " ".join(hyp[c:d])) for t, a, b, c, d in sm.get_opcodes() if t != "equal"]
real = [x for x in diff if (x[1], x[2]) not in IGN]
rmap = {blk.a + k: blk.b + k for blk in sm.get_matching_blocks() for k in range(blk.size)}
cuts, i = [], 0
for k in ["HK1", "HK2", "HK3"]:
    i += len(parts[k]); cuts.append(round((W[rmap[i - 1]][2] + W[rmap[i]][1]) / 2, 3))
out = {"src": SRC, "duration": round(info.duration, 3), "cuts": cuts,
       "ranges": {"HK1": [0.0, cuts[0]], "HK2": [cuts[0], cuts[1]], "HK3": [cuts[1], cuts[2]], "BODY": [cuts[2], round(info.duration, 3)]},
       "diff": diff, "possible_missing_or_changed": real}
json.dump(out, open(SRC + ".cuts.json", "w"), indent=1)
print(json.dumps({"src": SRC, "cuts": cuts, "possible_missing_or_changed": real}))
