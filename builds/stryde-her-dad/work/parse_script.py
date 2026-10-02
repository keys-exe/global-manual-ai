#!/usr/bin/env python3
"""Screenplay parse for stryde-her-dad: SPEAKER (note): "line" -> lines.json (verbatim, §22U)."""
import re, json, pathlib
here = pathlib.Path(__file__).parent
txt = (here / "script.txt").read_text().splitlines()
start = next(i for i, l in enumerate(txt) if l.strip().startswith("HOOK: THE VAN"))
# scene boundaries by the first line of each staged scene (THE STORY section); act per §3B
SCENES = [  # (first line text startswith, scene, act (§3B), place)
 ("TONY: “Sue! SUE!”", "SC01", "HK", "garden-centre car park — the van"),
 ("SUE (VO, inner): “He has no idea", "SC02", "BF", "the car, straight after"),
 ("TONY (VO): “Sixty-four.", "SC03", "PB", "rock bottom — his stairs sideways, the drawer, waiting in the car"),
 ("GP: “Your bloods", "SC04", "PB", "GP consulting room"),
 ("TONY: “Gary. I’ve got to ask.", "SC05", "TN", "builders' yard — Gary"),
 ("SUE: “What’s that?”", "SC06", "TN", "home — Sue finds the strap"),
 ("TONY (VO): “First time in two years", "SC07", "AF", "stairs forwards · the yard · the street"),
 ("SUE: “Tony…”", "SC08", "AF", "back garden — the new patio"),
 ("SUE: “Why are we stopping here?”", "SC09", "AF", "the same car park, weeks later — the mirror"),
 ("VO: “If your knees", "SC10", "OC", "narrator over strap, stairs, patio, pack"),
]
rows, sc = [], None
pat = re.compile(r"^([A-Z][A-Z ]+?)(?: \(([^)]*)\))?: “(.*)”\s*$")
for l in txt[start:]:
    s = l.strip()
    for key, scn, act, place in SCENES:
        if s.startswith(key): sc = (scn, act, place)
    m = pat.match(s)
    if not m: continue
    spk, note, line = m.group(1), m.group(2), m.group(3)
    vo = bool(note and "VO" in note) or spk == "VO"
    rows.append(dict(id=f"L{len(rows)+1:03d}", scene=sc[0], act=sc[1], place=sc[2], speaker=spk,
                     note=note, disp="VO" if vo else "SH", line=line, words=len(line.split())))
json.dump(rows, open(here / "lines.json", "w"), indent=1, ensure_ascii=False)
(here / "script.lines.txt").write_text("\n".join(r["line"] for r in rows) + "\n")
hw = sum(r["words"] for r in rows if r["scene"] == "SC01"); tw = sum(r["words"] for r in rows)
print(len(rows), "lines,", tw, "words; hook", hw, "body", tw - hw)
for r in rows: print(r["id"], r["scene"], r["speaker"], r["disp"], r["line"][:70])
