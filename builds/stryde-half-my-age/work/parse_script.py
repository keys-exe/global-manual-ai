"""Screenplay parse for stryde-half-my-age: every spoken line verbatim with its speaker, scene and
parenthetical (the §27F visual notes). Speaker labels and parentheticals are never voiced."""
import re, json
L = [l.strip() for l in open("work/script.txt") if l.strip()]
scene = None; out = []; vn = []; n = 0
for l in L[3:]:
    if re.match(r"^(HOOK|SCENE)\b", l):
        scene = l; continue
    m = re.match(r"^([A-Z][A-Z0-9 ]+?)(?:\s*\(([^)]*)\))?:\s*(“.*)$", l)
    if not m: print("UNPARSED", l); continue
    spk, note, rest = m.group(1).strip(), m.group(2), m.group(3)
    q = re.match(r"^“(.*)”\s*(?:\((.*)\))?\s*$", rest)
    text, tail = q.group(1), q.group(2)
    n += 1
    row = dict(n=n, scene=scene, speaker=spk, text=text)
    for t in (note, tail):
        if t:
            vn.append(dict(id=f"VN{len(vn)+1:02d}", scene=scene, line=n, speaker=spk, note=t)); row.setdefault("vn", []).append(vn[-1]["id"])
    out.append(row)
json.dump(dict(lines=out, visual=vn), open("work/lines.json", "w"), indent=1, ensure_ascii=False)
from collections import Counter
print(len(out), "lines ·", sum(len(r["text"].split()) for r in out), "words ·", len(vn), "notes")
print(Counter(r["speaker"] for r in out))
for s in dict.fromkeys(r["scene"] for r in out):
    print(s, sum(len(r["text"].split()) for r in out if r["scene"] == s))
