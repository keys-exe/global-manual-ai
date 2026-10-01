#!/usr/bin/env python3
"""Act 2 (the turn — the wedding, N-D2) — §6A short beat prompts, Mode 2, A/B pair on nano_banana_pro.
Every reception shot is an image edit of the confirmed P3-RECEPTION plate (Image 1); the build's style frame is attached (§24O rule 2).
Writes body2/<BEAT>.v1.prompt.txt + .preflight.json and runs preflight.py."""
import json, subprocess, sys
from pathlib import Path
H = Path(__file__).parent
PF = H / "../../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(H.parent / "work/actmap_rows.json"))}
def L(b): return rows[b]["line"]
P3 = "7cdda7ff-68a8-4e54-ab1c-2d80fbe93822"      # P3-RECEPTION plate (confirmed) — job id
C1 = "fce3f6cb-9ef5-47b5-996b-f9c62e893bc8"      # C1-LORETTA sheet v2 (confirmed)
N = "32b8bfc2-4538-4c28-b485-3fd28fc5d489"       # N-NARR sheet v2 (confirmed)
STYLE = "5b40a12a-24f5-4d12-8650-016a8b0384ae"   # P-05c v5 A (confirmed beat frame) — the build's style frame
R_P3 = {"label": "P3-RECEPTION plate (confirmed)", "kind": "location", "job": P3}
R_C1 = {"label": "C1-LORETTA sheet v2 (confirmed)", "kind": "character", "job": C1}
R_N = {"label": "N-NARR sheet v2 (confirmed)", "kind": "character", "job": N}
R_ST = {"label": "P-05c frame v5 A (confirmed) — the style: render, materials, light, proportions", "kind": "style", "job": STYLE}
TAIL = "A final frame from a 3D animated feature film, stylized storybook render in the warm glow of the string lights and chandeliers, evening."
TASTE = ["HT03", "HT04", "HT08", "HT12", "HT17", "HT21", "HT22", "HT25", "FP13", "FP14", "FP17"]
P = {}
# v3/v4 (user 2026-10-01: "I WANT NEW IMAGES IN ALL OF THEM I WANT NEW WARDROBE TOO") — new N-D2 wardrobe (N burgundy chiffon, gold hoops;
# Loretta fuchsia satin, white slip-ons) and new compositions from the re-staged act-map rows. Sheets go in for the face only (HT26): the sheet's clothes are named as not worn.
NW = "a burgundy chiffon dress to mid-calf with flutter sleeves, gold hoop earrings"
LW = "a fuchsia satin dress to the knee"
NWU = "a burgundy chiffon dress with flutter sleeves, gold hoop earrings"  # waist-up shots
TAIL2 = "A final frame from a 3D animated feature film, stylized storybook render, warm evening light."
P["T-01a"] = (f'''For the line "{L("T-01a")}": Keep this photo exactly as it is — the hall, the dance floor, the lights — at the edge of the floor, a tall 9:16 crop; add the bride and her grandmother. Image 1 is the hall. Image 2 is the grandmother — her face and silver twist-out only. Image 3 is the style — the same render, materials, light and proportions.
Medium shot at eye level, sharp on both faces: a young Black bride in a white gown, in three-quarter view facing frame right, hugging the same woman as Image 2, seventy-one, in {NWU}, her cheek on the bride's shoulder, facing frame left; both smiling, lips closed, eyes closed; the bride's arms round her, her hands on the bride's back, four chunky fingers and a thumb on each. Scale true to the set: the grandmother comes up to the bride's chin.
In frame: the two from the waist up, the lights soft behind; every other surface bare.
{TAIL2} No lettering, logos or labels; not the mustard top or denim skirt of Image 2.''', [R_P3, R_N, R_ST], True, True, P3)
P["T-01b"] = (f'''For the line "{L("T-01b")}": Keep this photo exactly as it is — the hall, the parquet dance floor, the string lights and chandeliers, the evening light — out on the dance floor, a tall 9:16 crop, and add the woman. Image 1 is the hall. Image 2 is the woman — her face and silver bob only. Image 3 is the style — the same render, materials, light and proportions.
Medium close-up from low, sharp on her face: the same woman as Image 2, seventy-four, in {LW}, in three-quarter view facing frame left, both arms raised above her head, hands open and waving to the beat, four chunky fingers and a thumb on each, a big grin with lips closed, looking at the dancers beside her. Scale true to the set: the chandelier behind her is no bigger than her head.
In frame: the woman from the waist up, her raised hands, the string lights of Image 1 soft behind her; every other surface bare.
{TAIL} Dress and decor plain — no lettering, logos or labels; not the teal blouse or khaki shorts of Image 2.''', [R_P3, R_C1, R_ST], True, True, P3)
P["T-02a"] = (f'''For the line "{L("T-02a")}": Keep this photo exactly as it is — the hall, the parquet dance floor, the tables, the string lights and chandeliers, the evening light — seen from high above the tables, a tall 9:16 crop, and add the dancers. Image 1 is the hall. Image 2 is the style — the same render, materials, light and proportions.
Wide shot from high, looking down on the floor, sharp on the line: seven wedding guests in a line on the parquet, all facing the lens, mid side-step to their right in unison; in the middle an older Black woman with a silver bob in {LW} and white slip-on sneakers; arms loose, every hand open, four chunky fingers and a thumb. Scale true to the set: the dancers come up to the bottom of the string lights.
In frame: seven dancers, the dance floor, the edge of the round tables and the lights of Image 1; every other surface as in Image 1.
{TAIL} Clothing and decor plain — no lettering, logos or labels.''', [R_P3, R_ST], False, True, P3)
P["T-02b"] = (f'''For the line "{L("T-02b")}": Keep this photo exactly as it is — the parquet dance floor, the evening light of the string lights — in close at floor level on the dance floor, a tall 9:16 crop, and add the feet. Image 1 is the hall. Image 2 is the style — the same render, materials, light and proportions.
Close-up at floor level from the side, sharp on the white sneakers: a row of dancers' feet in profile on the parquet, all pointing frame right, stepping forward together in unison — black dress shoes, gold heels, and nearest the lens a pair of white slip-on sneakers under the hem of {LW}, brown ankles; legs from the knee down, every foot whole on the floor. Scale true to the set: the fuchsia hem comes up to her knee.
In frame: the row of feet, the parquet, the lights soft behind; nothing else on the floor.
{TAIL} Shoes and dress plain — no lettering, logos or labels.''', [R_P3, R_ST], False, False, P3)
P["T-03a"] = (f'''For the line "{L("T-03a")}": An X-ray frame in the film's world: a glowing radiograph of an older woman's two knees side by side, front-on, facing the lens, bright blue-white bone on a deep navy-black field, soft tissue a faint grey; in each knee the gap between thigh bone and shin bone is gone on both sides of the joint, the bones touching, and where bone meets bone a warm red-orange glow. Image 1 is the style — the same render, materials, light and proportions; a stylized storybook X-ray.
Close-up, sharp on the two joints, the knees level with each other, each knee about a third of the frame wide.
In frame: two knees — the thigh-bone ends, the shin-bone tops, the kneecaps faint over the joints; every other area plain dark.
A final frame from a 3D animated feature film, stylized storybook render. Film plain — no lettering, logos, labels or measurement marks.''', [R_ST], False, False, None)
P["T-04a"] = (f'''For the line "{L("T-04a")}": Keep this photo exactly as it is — the hall, the tables, the floor, the lights — from behind her seat, a tall 9:16 crop; add her and the dancer. Image 1 is the hall. Image 2 is the seated woman — her face and silver twist-out only. Image 3 is the style — the same render, materials, light and proportions.
Medium shot over her right shoulder at eye level, sharp on the dancer: the same woman as Image 2, seventy-one, seated in {NWU}, her back three-quarter to us, her face in lost profile facing frame right, looking at the dance floor, lips closed; her right hand on her right knee, four chunky fingers and a thumb. Beyond, in focus, an older Black woman with a silver bob in {LW} dancing, arms up. Scale true to the set: the table edge comes up to her waist.
In frame: her shoulder and hair, one table with two glasses, the dancer, the floor beyond; every other surface bare.
{TAIL2} No lettering, logos or labels; not the mustard top of Image 2.''', [R_P3, R_N, R_ST], True, True, P3)
P["T-04b"] = (f'''For the line "{L("T-04b")}": Keep this photo exactly as it is — the parquet floor, the gold chair legs, the evening light — low under a table edge, a tall 9:16 crop, and add her knee and hand. Image 1 is the hall. Image 2 is the style — the same render, materials, light and proportions.
Close-up low and front-on, facing the lens, sharp on the knee: an older Black woman seated, her right knee under the burgundy chiffon of her dress, her brown right hand on the knee rubbing it through the fabric, four chunky fingers and a thumb; a gold heel on the parquet below; behind her chair, soft and out of focus, dancing feet on the parquet. Scale true to the set: the tablecloth hem comes down to just above her knee.
In frame: one knee, one hand on it, the tablecloth edge at the top, a chair leg, the dancers soft beyond; every other surface bare.
{TAIL} Dress and tablecloth plain — no lettering, logos or labels.''', [R_P3, R_ST], False, True, P3)
ANAT = {"T-03a": "S2"}
VER = 3
fails = 0
for b, (pr, refs, face, body, eo) in P.items():
    c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(b), "face": face, "room": eo is not None, "body": body,
         "refs": [{k: v for k, v in r.items() if k != "job"} for r in refs], "match": "plate" if eo else None, "edit_of": eo, "taste": TASTE,
         "anatomy": b in ANAT, "anat_style": ANAT.get(b), "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None, "fix_note": "user 2026-10-01: I WANT NEW IMAGES IN ALL OF THEM I WANT NEW WARDROBE TOO", "product": False,
         "medias": [r["job"] for r in refs]}
    (H / f"{b}.v{VER}.prompt.txt").write_text(pr); (H / f"{b}.v{VER}.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v{VER}.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
