import json
import broll
from motions import M
OUT = broll.PR / "clips"; OUT.mkdir(exist_ok=True)
for b, r in broll.ROWS.items():
    subj, mot = M[b]
    j = broll.kling(r, mot, subj)
    (OUT / f"{b}.kling.json").write_text(j)
    print(b, len(j), r["duration"] if isinstance(r["duration"], int) else r.get("duration"))
