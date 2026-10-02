"""Screenplay parse for stryde-the-impression: every spoken line verbatim with its speaker, block and
parenthetical (the §27F visual notes). Speaker labels, parentheticals and the story/visual prose are never voiced."""
import re, json
raw = open("intake/SCRIPT.docx.extracted.txt").read().split("\n")
start = next(i for i, l in enumerate(raw) if l.strip().startswith("HOOK A"))
BLOCKS = ["HK-A1 The impression", "HK-A2 The promise", "B01 The film", "B02 The pharmacy",
          "B03 The drawer + the hill (July)", "B04 The car", "B05 The gate", "B06 Wendy",
          "B07 The price", "B08 The stairs (inner VO)", "B09 The witnesses — hill (August)",
          "B10 The witnesses — the hall (end of August)", "B11 Roy", "B12 The first day", "B13 The close"]
bi = -1; out = []; vn = []; n = 0; sect = None; prev_blank = True
for l in raw[start:]:
    s = l.strip()
    if not s:
        prev_blank = True; continue
    if s.startswith("HOOK A"): sect = "HOOK A"; bi = 0; prev_blank = False; continue
    if s == "BODY": sect = "BODY"; prev_blank = True; continue
    if prev_blank and out and not (sect == "HOOK A" and bi == 0 and not out):
        # a blank line opens the next block (the first BODY block opens at BODY)
        pass
    if prev_blank and (out or vn):
        if not (len(out) == 0): bi += 1 if not (sect == "BODY" and bi < 2 and out[-1]["block"].startswith("HK") and False) else 0
    prev_blank = False
    m = re.match(r"^\((.*)\)$", s)
    if m:
        vn.append(dict(id=f"VN{len(vn)+1:02d}", block=BLOCKS[bi], line=n + 1, speaker=None, note=m.group(1), kind="parenthetical")); continue
    m = re.match(r"^([A-Z][A-Z0-9 ]+?)(?:\s*\(([^)]*)\))?:\s*“(.*)”\s*$", s)
    if not m: print("UNPARSED", s); continue
    spk, note, text = m.group(1).strip(), m.group(2), m.group(3)
    n += 1
    row = dict(n=n, id=f"L{n:03d}", block=BLOCKS[bi], speaker=spk, text=text)
    if note: row["delivery"] = note
    out.append(row)
json.dump(dict(lines=out, visual=vn), open("work/lines.json", "w"), indent=1, ensure_ascii=False)
from collections import Counter
print(len(out), "lines ·", sum(len(r["text"].split()) for r in out), "words ·", len(vn), "notes")
print(Counter(r["speaker"] for r in out))
for b in dict.fromkeys(r["block"] for r in out):
    rs=[r for r in out if r["block"] == b]
    print(f'{b:45s} {rs[0]["id"]}-{rs[-1]["id"]} {sum(len(r["text"].split()) for r in rs)}w')
