#!/usr/bin/env python3
"""HK1-02c v5 — the user's note on v4, 2026-09-29 ~13:00 UTC: "that is good but dont make the braces magically going to the trash bag she should be putting them there".
v4 kept (strap apart on the table, sharp; her behind, soft); only the action changes: she PUTS one brace into the bag by hand, the rest still in the open drawer.
Nothing in mid-air."""
import json, pathlib
here = pathlib.Path(__file__).parent
v6 = json.load(open(here / "hooks_v6.json"))["HK1-02c"]
p = v6["prompt"]
old = p[p.index("stands at the dresser holding a black bin bag open"):p.index("Her face is soft")]
new = ("stands at the dresser beside its top drawer, pulled open and still heaped with old knee supports — black sleeves, beige wraps, a hinged brace with metal side bars. "
       "Her left hand holds a black bin bag open by its rim against the side of the dresser; her right hand is PUTTING one grey hinged knee brace into the bag herself, "
       "gripping it by its strap, the brace already half inside the bag's mouth, her fingers still on it. Every brace is either in the drawer, in her hand or in the bag — "
       "nothing falling, nothing in the air. ")
p = p.replace(old, new)
p = p.replace("no strap in her hands,", "no braces flying or falling through the air, no braces in mid-air, no drawer tipped up, no strap in her hands,")
out = dict(v6, prompt=p, chars=len(p))
(here / "HK1-02c.image.v7.prompt.txt").write_text(p)
json.dump({"HK1-02c": out}, open(here / "hooks_v7.json", "w"), indent=1)
print(len(p))
