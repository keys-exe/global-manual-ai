#!/usr/bin/env python3
"""Act 2 Fix round (user 2026-10-02): T-02a "this should be loreta", T-02b "wrong person".
Loretta's confirmed T-01b frame (v3 A — her face, silver bob, the fuchsia satin dress with long sleeves, her build) goes in as Image 2,
so the dancer and the feet are hers. Writes body2/<BEAT>.v5.prompt.txt + .preflight.json (pair v5/v6) and runs preflight.py."""
import json, subprocess, sys
from pathlib import Path
H = Path(__file__).parent
PF = H / "../../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(H.parent / "work/actmap_rows.json"))}
def L(b): return rows[b]["line"]
P3 = "7cdda7ff-68a8-4e54-ab1c-2d80fbe93822"      # P3-RECEPTION plate (confirmed)
LOR = "83cdaecf-f772-4501-8f6c-1a725ed4d7b1"     # T-01b v3 A (confirmed) — Loretta in her N-D2 dress
STYLE = "5b40a12a-24f5-4d12-8650-016a8b0384ae"   # P-05c v5 A (confirmed) — the style frame
R_P3 = {"label": "P3-RECEPTION plate (confirmed)", "kind": "location", "job": P3, "ref": "stryde-71-stairs-pixar-song__P3-RECEPTION"}
R_LOR = {"label": "T-01b frame v3 A (confirmed) — Loretta: face, silver bob, the fuchsia dress, her build", "kind": "character", "job": LOR, "ref": "stryde-71-stairs-pixar-song__T-01b"}
R_ST = {"label": "P-05c frame v5 A (confirmed) — the style: render, materials, light, proportions", "kind": "style", "job": STYLE, "ref": "stryde-71-stairs-pixar-song__P-05c"}
TAIL = "A final frame from a 3D animated feature film, stylized storybook render in the warm glow of the string lights and chandeliers, evening."
TASTE = ["HT03", "HT04", "HT08", "HT12", "HT17", "HT21", "HT22", "HT25", "HT26", "FP13", "FP14", "FP17"]
FIX = {"T-02a": 'user 2026-10-02 Fix: "this should be loreta" → Loretta\'s confirmed T-01b frame as Image 2, and she leads the line at the front, nearest the lens, her face clear',
       "T-02b": 'user 2026-10-02 Fix: "wrong person" → Loretta\'s confirmed T-01b frame as Image 2: her legs, skin, build and dress; the slip-ons on her'}
P = {}
P["T-02a"] = (f'''For the line "{L("T-02a")}": Keep this photo exactly as it is — the hall, the parquet dance floor, the tables, the lights — seen from a little above the floor's edge, a tall 9:16 crop, and add the dancers. Image 1 is the hall. Image 2 is Loretta — the same woman, face, silver bob, build and fuchsia satin dress as in Image 2. Image 3 is the style — the same render, materials, light and proportions.
Wide shot from high, sharp on Loretta: the same woman as Image 2, seventy-four, leads a line dance at the front of the line, nearest the lens and largest in frame, facing the lens, mid side-step to her right, a big grin with lips closed, eyes on the floor ahead; white slip-on sneakers; four guests in a row behind her step with her. Arms loose, every hand open, four chunky fingers and a thumb. Scale true to the set: she comes up to the second row of string lights.
In frame: Loretta, four dancers behind her, the parquet, the lights of Image 1; every other surface as in Image 1.
{TAIL} No lettering, logos or labels.''', [R_P3, R_LOR, R_ST], True, True, P3)
R_LORF = dict(R_LOR, kind="frame", label="T-01b frame v3 A (confirmed) — Loretta: the legs, skin, build and dress to copy (no face in this shot)")
P["T-02b"] = (f'''For the line "{L("T-02b")}": Keep this photo exactly as it is — the parquet dance floor, the evening light of the string lights — in close at floor level on the dance floor, a tall 9:16 crop, and add the feet. Image 1 is the hall. Image 2 is Loretta — her skin, build and fuchsia satin dress. Image 3 is the style — the same render, materials, light and proportions.
Close-up at floor level from the side, sharp on her white sneakers: nearest the lens, Loretta's legs from Image 2, seventy-four — medium-brown skin, full sturdy calves, thick ankles — under the hem of her fuchsia satin dress, in white slip-on sneakers, pointing frame right, mid step forward; beyond, other dancers' dress shoes and gold heels step with her. Legs from the knee down, every foot whole on the floor. Scale true to the set: her hem comes down to just below her knee.
In frame: her legs and sneakers, the row of feet, the parquet, the lights soft behind; nothing else on the floor.
{TAIL} No lettering, logos or labels.''', [R_P3, R_LORF, R_ST], False, False, P3)
VER = 5
fails = 0
for b, (pr, refs, face, body, eo) in P.items():
    c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(b), "face": face, "room": True, "body": body,
         "refs": [{k: v for k, v in r.items() if k not in ("job", "ref")} for r in refs], "match": "plate", "edit_of": eo, "taste": TASTE,
         "anatomy": False, "anat_style": None, "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None, "fix_note": FIX[b], "product": False,
         "medias": [r["job"] for r in refs], "board_refs": [{k: v for k, v in r.items() if k != "job"} for r in refs]}
    (H / f"{b}.v{VER}.prompt.txt").write_text(pr); (H / f"{b}.v{VER}.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v{VER}.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
