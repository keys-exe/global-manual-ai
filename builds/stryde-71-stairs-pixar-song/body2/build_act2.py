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
P["T-01a"] = (f'''For the line "{L("T-01a")}": Keep this photo exactly as it is — the banquet hall, the round tables and gold chairs, the string lights and chandeliers, the evening light — at a table by the dance floor, a tall 9:16 crop, and add the bride and two guests. Image 1 is the hall. Image 2 is the style — the same render, materials, light and proportions.
Medium shot at eye level, sharp on the bride: a young Black bride in a white gown, seated at the round table in three-quarter view facing frame left toward an older guest, a wide closed-mouth smile, eyes crinkled, looking at the guest; her right hand on the guest's forearm, her left hand on the tablecloth, four chunky fingers and a thumb on each; two older guests in dark suits beside her, smiling, hands on the table. Scale true to the set: the chair back comes up to her shoulders.
In frame: the bride, two guests, one table with glasses and a hydrangea centrepiece, the hall of Image 1 soft beyond; every other surface bare.
{TAIL} Gown and decor plain — no lettering, logos or labels.''', [R_P3, R_ST], True, True, P3)
P["T-01b"] = (f'''For the line "{L("T-01b")}": Keep this photo exactly as it is — the hall, the parquet dance floor, the string lights and chandeliers, the evening light — at the edge of the dance floor, a tall 9:16 crop, and add the woman. Image 1 is the hall. Image 2 is the woman. Image 3 is the style — the same render, materials, light and proportions.
Medium close-up from low, sharp on her face: the same woman as Image 2, seventy-four, her silver bob as in Image 2, in a royal-blue satin dress to the knee, in three-quarter view facing frame right toward the dancers, clapping on the beat, both hands meeting at chest height, four chunky fingers and a thumb on each, a big closed-mouth grin, eyes on the dance floor. Scale true to the set: the chair backs behind her come up to her hip.
In frame: the woman from the waist up, the dance floor and lights of Image 1 soft behind her; every other surface bare.
{TAIL} Dress and decor plain — no lettering, logos or labels.''', [R_P3, R_C1, R_ST], True, True, P3)
P["T-02a"] = (f'''For the line "{L("T-02a")}": Keep this photo exactly as it is — the hall, the parquet dance floor, the tables, the string lights and chandeliers, the evening light — wide on the dance floor, a tall 9:16 crop, and add the dancers. Image 1 is the hall. Image 2 is the style — the same render, materials, light and proportions.
Wide shot at eye level from behind a table, gold chair backs soft in the near foreground, sharp on the line: six wedding guests in a line on the parquet, all facing the lens, mid side-step to their right in unison; in the middle an older Black woman with a silver bob in a royal-blue satin dress to the knee and white slip-on sneakers; arms loose, every hand open, four chunky fingers and a thumb. Scale true to the set: the table edges come up to their hips.
In frame: six dancers, the dance floor, the DJ booth and lights of Image 1 beyond; every other surface as in Image 1.
{TAIL} Clothing and decor plain — no lettering, logos or labels.''', [R_P3, R_ST], False, True, P3)
P["T-02b"] = (f'''For the line "{L("T-02b")}": Keep this photo exactly as it is — the parquet dance floor, the evening light of the string lights — in close at floor level on the dance floor, a tall 9:16 crop, and add the feet. Image 1 is the hall. Image 2 is the style — the same render, materials, light and proportions.
Close-up at floor level, front-on, sharp on the shoes: a row of dancers' feet on the parquet, all facing the lens, stepping back together in unison — black dress shoes, silver heels, and in the middle a pair of white slip-on sneakers under the hem of a royal-blue satin dress, brown ankles; legs from the knee down, every foot whole and flat on the floor. Scale true to the set: the dress hem comes up to her knee.
In frame: the row of feet, the parquet, the lights soft behind; nothing else on the floor.
{TAIL} Shoes and dress plain — no lettering, logos or labels.''', [R_P3, R_ST], False, False, P3)
P["T-03a"] = (f'''For the line "{L("T-03a")}": An X-ray frame in the film's world: a glowing radiograph of an older woman's two knees in profile, facing frame left, one just behind the other, bright blue-white bone on a deep navy-black field, soft tissue a faint grey; in each knee the gap between thigh bone and shin bone is gone, the bones touching, and where bone meets bone a warm red-orange glow. Image 1 is the style — the same render, materials, light and proportions; a stylized storybook X-ray.
Close-up, sharp on the two joints, the near knee about a third of the frame wide, the two knees level with each other.
In frame: two knees — the thigh-bone ends, the shin-bone tops, the kneecaps faint; every other area plain dark.
A final frame from a 3D animated feature film, stylized storybook render. Film plain — no lettering, logos, labels or measurement marks.''', [R_ST], False, False, None)
P["T-04a"] = (f'''For the line "{L("T-04a")}": Keep this photo exactly as it is — the hall, the tables, the dance floor, the lights — from above a table by the floor, a tall 9:16 crop, and add her. Image 1 is the hall. Image 2 is the woman. Image 3 is the style — the same render, materials, light and proportions.
Medium shot from high, through the gold chair backs, sharp on her: the same woman as Image 2, seventy-one, seated alone at the table in a lavender chiffon dress and pearl studs, in three-quarter view facing frame left, eyes on the dancers far off, mouth closed; her right hand on her right knee under the table edge, her left hand on the tablecloth, four chunky fingers and a thumb on each. Scale true to the set: the table edge comes up to her waist. Far off on the floor, small and soft, a woman in royal blue dancing.
In frame: her, one table with two glasses, the floor of Image 1 beyond; every other surface bare.
{TAIL} Dress and decor plain — no lettering, logos or labels.''', [R_P3, R_N, R_ST], True, True, P3)
P["T-04b"] = (f'''For the line "{L("T-04b")}": Keep this photo exactly as it is — the parquet floor, the gold chair legs, the evening light — low under a table edge, a tall 9:16 crop, and add her knee and hand. Image 1 is the hall. Image 2 is the style — the same render, materials, light and proportions.
Close-up low, in profile facing frame left, sharp on the knee: an older Black woman's right knee under the lavender chiffon of her dress, her brown right hand rubbing the knee through the fabric, four chunky fingers and a thumb; her left hand resting in her lap at the top edge; beyond, soft and out of focus, dancing feet on the parquet. Scale true to the set: the tablecloth hem comes up to her knee.
In frame: one knee, one hand on it, the tablecloth edge, a chair leg, the dancers soft beyond; every other surface bare.
{TAIL} Dress and tablecloth plain — no lettering, logos or labels.''', [R_P3, R_ST], False, True, P3)
ANAT = {"T-03a": "S2"}
fails = 0
for b, (pr, refs, face, body, eo) in P.items():
    c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(b), "face": face, "room": eo is not None, "body": body,
         "refs": [{k: v for k, v in r.items() if k != "job"} for r in refs], "match": "plate" if eo else None, "edit_of": eo, "taste": TASTE,
         "anatomy": b in ANAT, "anat_style": ANAT.get(b), "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None, "fix_note": None, "product": False,
         "medias": [r["job"] for r in refs]}
    (H / f"{b}.v1.prompt.txt").write_text(pr); (H / f"{b}.v1.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v1.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
