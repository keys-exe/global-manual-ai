#!/usr/bin/env python3
"""T-04a Fix (user 2026-10-02: "SHE SHOULD NOT BE THE ONLY ONE ON THE DANCE FLOOR") — an image edit of the confirmed T-04a v3 A
frame (FP14, §24O rule 7): everything kept, the dance floor filled with guests around Loretta. Pair v5/v6."""
import json, subprocess, sys
from pathlib import Path
H = Path(__file__).parent
PF = H / "../../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(H.parent / "work/actmap_rows.json"))}
line = rows["T-04a"]["line"]
B = "stryde-71-stairs-pixar-song__"
FR = {"label": "T-04a frame v3 A (confirmed) — the picture to keep", "kind": "frame", "job": "cecea849-ec9a-4bc4-86b6-ed76c3abf53c", "ref": B + "T-04a"}
ST = {"label": "P-05c frame v5 A (confirmed) — the style: render, materials, light, proportions", "kind": "style", "job": "5b40a12a-24f5-4d12-8650-016a8b0384ae", "ref": B + "P-05c"}
pr = f'''For the line "{line}": Keep this photo exactly as it is — the seated woman, her burgundy dress, gold hoop and hand on her knee, the table, the hall, the lights, the dancer in fuchsia — and fill the dance floor around that dancer with guests. Image 1 is the photo to keep. Image 2 is the style — the same render, materials and light.
Medium shot over the seated woman's right shoulder at eye level, sharp on the dancer: on the parquet beyond the table, around the woman in fuchsia, eight wedding guests dance in couples and in a short line, in suits and party dresses, some facing the lens, some in profile; the woman in fuchsia stays where she is, arms up, among them. The seated woman stays in lost profile facing frame right, looking at the dance floor, lips closed, her right hand on her knee, four chunky fingers and a thumb. Scale true to the set: the dancers come up to the second row of string lights.
In frame: the seated woman, the table, the dance floor full of dancers; every other surface as in Image 1.
A final frame from a 3D animated feature film, stylized storybook render, warm evening light. No lettering, logos or labels.'''
c = {"beat": "T-04a", "kind": "image", "mode": 2, "prompt": pr, "script_line": line, "face": True, "room": True, "body": True,
     "refs": [{"label": r["label"], "kind": r["kind"]} for r in (FR, ST)], "match": "frame", "edit_of": FR["job"],
     "taste": ["HT03", "HT08", "HT12", "HT17", "HT22", "HT25", "FP14"], "anatomy": False, "anat_style": None, "pair": ["nano_banana_pro", "nano_banana_pro"],
     "alt_reason": None, "fix_note": 'user 2026-10-02 Fix: "SHE SHOULD NOT BE THE ONLY ONE ON THE DANCE FLOOR" → an edit of the confirmed v3 A frame, the floor filled with guests around Loretta',
     "product": False, "medias": [FR["job"], ST["job"]], "board_refs": [{"label": r["label"], "kind": r["kind"], "ref": r["ref"], "role": f"Image {i + 1}"} for i, r in enumerate((FR, ST))]}
(H / "T-04a.v5.prompt.txt").write_text(pr); (H / "T-04a.v5.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
r = subprocess.run([sys.executable, str(PF), str(H / "T-04a.v5.preflight.json")], capture_output=True, text=True)
print(f"T-04a: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
sys.exit(r.returncode)
