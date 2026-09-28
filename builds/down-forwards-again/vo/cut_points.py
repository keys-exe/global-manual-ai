#!/usr/bin/env python3
"""Hook/body boundaries in a one-pass house-cut take (§22U step 12, one go): transcribe with word timestamps,
align to HK1+HK2+HK3+BODY, cut mid-gap after each hook. Usage: cut_points.py cut/T1.ALL.mp3"""
import sys, json, difflib, importlib.util
from faster_whisper import WhisperModel
spec = importlib.util.spec_from_file_location("sv", "split_vo.py")
src = open("split_vo.py").read(); norm_src = src[:src.index("if __name__")]
ns = {}; exec(norm_src.split("parts = ")[0], ns); norm = ns["norm"]
parts = {k: norm(open(f"{k}.lines.txt").read().replace("\n", " ")) for k in ["HK1", "HK2", "HK3", "BODY"]}
ref = parts["HK1"] + parts["HK2"] + parts["HK3"] + parts["BODY"]
f = sys.argv[1]
segs, info = WhisperModel("medium.en", compute_type="int8").transcribe(f, word_timestamps=True, language="en")
words = [(t, w.start, w.end) for s in segs for w in s.words for t in norm(w.word)]
hyp = [w[0] for w in words]
sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
rmap = {blk.a + k: blk.b + k for blk in sm.get_matching_blocks() for k in range(blk.size)}
diff = [(t, " ".join(ref[a:b]), " ".join(hyp[c:d])) for t, a, b, c, d in sm.get_opcodes() if t != "equal"]
cuts, i = [], 0
for k in ["HK1", "HK2", "HK3"]:
    i += len(parts[k]); a, b = words[rmap[i - 1]][2], words[rmap[i]][1]; cuts.append(round((a + b) / 2, 3))
out = dict(file=f, duration=round(info.duration, 3), cuts=dict(HK1=[0, cuts[0]], HK2=[cuts[0], cuts[1]], HK3=[cuts[1], cuts[2]], BODY=[cuts[2], round(info.duration, 3)]),
           diff=diff, words=[[w[0], round(w[1], 3), round(w[2], 3)] for w in words])
json.dump(out, open(f + ".cuts.json", "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k != "words"}, indent=1))
