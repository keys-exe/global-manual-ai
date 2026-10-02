#!/usr/bin/env python3
"""Every lyric word gets a sung time: the script's lyric words (work/lyrics.txt order) aligned to the medium.en
words (edit/words_medium.json) by sequence match; an unmatched word is placed between its matched neighbours.
Out: edit/lyric_words.json = [{line, i, w, t, end, matched}] and each line's first-word onset."""
import json, re, difflib
from pathlib import Path
H = Path(__file__).parent; B = H.parent
norm = lambda w: re.sub(r"[^a-z0-9]", "", w.lower())
lines = [l["line"] for l in json.load(open(B / "work/lyrics.timed.json"))]
lw = [(n + 1, k, w) for n, l in enumerate(lines) for k, w in enumerate(l.split())]
heard = json.load(open(H / "words_medium.json"))
a = [norm(w) for _, _, w in lw]; b = [norm(x["w"]) for x in heard]
sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
t = [None] * len(lw); e = [None] * len(lw)
for blk in sm.get_matching_blocks():
    for j in range(blk.size):
        t[blk.a + j] = heard[blk.b + j]["s"]; e[blk.a + j] = heard[blk.b + j]["e"]
matched = [x is not None for x in t]
# fill gaps linearly between matched neighbours
idx = [i for i, x in enumerate(t) if x is not None]
for i in range(len(t)):
    if t[i] is None:
        lo = max([j for j in idx if j < i], default=None); hi = min([j for j in idx if j > i], default=None)
        if lo is None: t[i] = e[i] = heard[0]["s"]
        elif hi is None: t[i] = e[lo]; e[i] = e[lo] + 0.3
        else:
            f = (i - lo) / (hi - lo); t[i] = round(e[lo] + f * (t[hi] - e[lo]), 3); e[i] = round(t[i] + 0.25, 3)
out = [{"line": n, "i": k, "w": w, "t": t[x], "end": e[x], "matched": matched[x]} for x, (n, k, w) in enumerate(lw)]
(H / "lyric_words.json").write_text(json.dumps(out))
print(f"{sum(matched)}/{len(lw)} lyric words matched to medium.en")
