#!/usr/bin/env python3
"""Act 3 re-renders of the frames kept off the board (L16) on 2026-10-02 — causes fixed at source:
 - the day's clothes leaked from the cast sheet (R-03a shorts; R-06b the N-D1 dress from the style frame) → HT26: a face-and-hair
   crop of the confirmed sheet (cast/*_face.png, no clothes) and a style frame with no outfit in it (P-04a v3, hands on the table);
 - the strap drawn as a plain band, a box or a hinged brace (R-04a A, R-06b B, R-07a B, R-07c A) → FP01: the shell's shape named
   (two pointed peaks round a centre notch, a chrome slide at each end) beside "copied exactly";
 - the lyric printed as a caption (R-06b A) → the line's quote marks dropped from the prompt (the line itself stays, §6A).
Writes body3/<BEAT>.v3.prompt.txt + .preflight.json and runs preflight.py."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent
PF = H / "../../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(H.parent / "work/actmap_rows.json"))}
M = json.load(open(H / "media.json"))
def L(b): return re.sub(r'["“”]', "", rows[b]["line"])
B = "stryde-71-stairs-pixar-song__"
P0 = {"label": "P0-PROP-N plate (confirmed) — the hall and staircase", "kind": "location", "job": "377f63fd-7b11-4db2-a663-052e8c0637e8", "ref": B + "P0-PROP-N"}
P2 = {"label": "P2-KITCHEN plate v2 (confirmed)", "kind": "location", "job": "2484470e-dbda-4935-b1f2-0897e8418066", "ref": B + "P2-KITCHEN"}
C1F = {"label": "C1-LORETTA face-and-hair crop of the confirmed sheet v2 (HT26, no clothes)", "kind": "character", "job": M["C1_face"], "ref": B + "C1-LORETTA"}
NF = {"label": "N-NARR face-and-hair crop of the confirmed sheet v2 (HT26, no clothes)", "kind": "character", "job": M["N_face"], "ref": B + "N-NARR"}
C1L = {"label": "C1-LORETTA sheet v2 (confirmed) — her legs and skin only (no face in this shot)", "kind": "frame", "job": "fce3f6cb-9ef5-47b5-996b-f9c62e893bc8", "ref": B + "C1-LORETTA"}
ST = {"label": "P-05c frame v5 A (confirmed) — the style: render, materials, light, proportions", "kind": "style", "job": "5b40a12a-24f5-4d12-8650-016a8b0384ae", "ref": B + "P-05c"}
STH = {"label": "P-04a frame v3 (confirmed, hands on her table, no outfit in it) — the style", "kind": "style", "job": "e05783fd-e5e1-4e31-b247-3a8c950954b6", "ref": B + "P-04a"}
FRONT = {"label": "front.webp — the strap, front (product photo)", "kind": "product", "job": M["front"], "ref": "products/stryde/stryde_refs/front.webp"}
BACK = {"label": "back.webp — the strap, back (product photo)", "kind": "product", "job": M["back"], "ref": "products/stryde/stryde_refs/back.webp"}
WORN = {"label": "worn_front.jpg — the strap worn, front-on (product photo)", "kind": "product", "job": M["worn_front"], "ref": "products/stryde/stryde_refs/worn_front.jpg"}
TQ = {"label": "product_tq_left.jpg — the strap, three-quarter (product photo)", "kind": "product", "job": M["product_tq_left"], "ref": "products/stryde/stryde_refs/product_tq_left.jpg"}
KIT = "A final frame from a 3D animated feature film, stylized storybook render, soft morning window light."
HALL = "A final frame from a 3D animated feature film, stylized storybook render, warm afternoon sun from the door."
SPLIT = "The strap alone in real materials, in the same light."
SHAPE = "the strap of Image 1 copied exactly — one black shell rising in two pointed peaks round a centre notch, a chrome slide at each end, a knit band —"
PLACE = "the kneecap's lower edge in its notch"
NW = "a rose-pink short-sleeve blouse, a denim skirt ending above the knee"
PLAIN = "No lettering, logos or labels but its wordmark."
TASTE = ["HT03", "HT04", "HT08", "HT12", "HT17", "HT21", "HT22", "HT25", "HT26", "FP13", "FP14", "FP17"]
TASTE_P = TASTE + ["FP01", "FP02", "FP03", "FP05", "FP06", "FP07", "FP10", "FP11", "FP12"]
FIX = {"R-03a": "kept off (L16): both first renders put her in the cast sheet's khaki shorts — the next beat needs the trouser leg (wardrobe map N-D3, F14) → HT26 face-and-hair crop, trousers named",
       "R-04a": "kept off (L16): A drew a plain rounded band, not the strap (FP01) → the shell's shape named",
       "R-06b": "kept off (L16): A printed the lyric as a caption and wore the N-D1 dress from the style frame; B drew the strap as a box (FP01) → quotes dropped, a style frame with no outfit, the shell's shape named",
       "R-07a": "kept off (L16): B drew a hinged brace (FP01, FP11) → face crop (HT26), the shell's shape named",
       "R-07c": "kept off (L16): A drew an open-kneecap sleeve brace (FP01, FP11) → face crop (HT26), the shell's shape named"}
P = {}
P["R-03a"] = (f'''For the line "{L("R-03a")}": Keep this photo exactly as it is — the kitchen, the round table and its lace cloth, the window light — across the table, a tall 9:16 crop, and add the visitor. Image 1 is the kitchen. Image 2 is the visitor's face and silver bob. Image 3 is the style — the same render, materials and light.
Medium close-up from low, sharp on her face: the same woman as Image 2, seventy-four, seated across the table in a teal three-quarter-sleeve blouse and khaki trousers to the ankle, in three-quarter view facing frame left, leaning in over the cloth with a half smile, lips closed, looking away past the lens; her right arm reaching down below the table edge toward her own knee, her left hand flat on the cloth beside a white mug, four chunky fingers and a thumb on each. Scale true to the set: the table edge comes up to her chest.
In frame: her from the chest up, the mug, the table edge, the kitchen of Image 1 behind; every other surface bare.
{KIT} No lettering, logos or labels; no shorts.''', [P2, C1F, ST], True, True, True, False, P2)
P["R-04a"] = (f'''For the line "{L("R-04a")}": A tall 9:16 frame. Image 1 is the strap, Image 2 its back, Image 3 it worn front-on. Image 4 is the leg and skin to copy. Image 5 is the style — the same render, materials and light.
Extreme close-up front-on at knee height, the knee facing the lens, sharp on the strap: a seated older woman's bare right knee, medium-brown skin, filling the frame; on it {SHAPE} 12 × 5 cm, the shell half the frame wide, {PLACE}, the wordmark level; her right fingertip taps the top of the shell, four chunky fingers and a thumb; a rolled khaki hem far above, a soft warm kitchen far behind. Scale true to the set: the shell's top edge is level with the kneecap's lower edge.
In frame: the knee, the strap, one hand; every other surface plain.
{KIT} {SPLIT} {PLAIN}''', [FRONT, BACK, WORN, C1L, ST], False, True, False, True, None)
P["R-06b"] = (f'''For the line "{L("R-06b")}": Kitchen of Image 4, tall 9:16. Image 1 is the strap, Image 2 its back, Image 3 its three-quarter view. Image 5 is the style.
Close-up from high three-quarter, her own view, sharp on the strap: a seated older Black woman's bare right shin and knee, the hem of her denim skirt just above the knee, a rose-pink blouse sleeve at the top edge, both hands sliding {SHAPE} up the shin, 12 × 5 cm, a third of the frame wide, its top edge reaching the kneecap's lower edge; four chunky fingers and a thumb on each; a tan slipper below. Scale true to the set: the hem comes to her knee.
In frame: one leg, two hands, the strap, a chair edge, the floor; every other surface bare.
{KIT} {SPLIT} No lettering, logos or labels but its wordmark; no caption.''', [FRONT, BACK, TQ, P2, STH], False, True, True, True, None)
P["R-07a"] = (f'''For the line "{L("R-07a")}": Staircase of Image 4, tall 9:16. Image 1 is the strap, Image 2 its back, Image 3 it worn. Image 5 is her face. Image 6 is the style.
Low from three steps below, sharp on her right knee: the same woman as Image 5, seventy-one, stepping down from the top step facing forwards toward the lens, right foot landing flat on the next step, hands loose at her sides, four chunky fingers and a thumb; {NW}, tan slippers; on her bare right knee {SHAPE} 12 × 5 cm, a quarter of the frame wide, {PLACE}; a proud closed-mouth smile, eyes on the step. Scale true to the set: her knee is level with the newel cap.
In frame: her, the flight; the rest as in Image 4.
{HALL} {SPLIT} {PLAIN} Not a brace.''', [FRONT, BACK, WORN, P0, NF, ST], True, True, True, True, None)
P["R-07c"] = (f'''For the line "{L("R-07c")}": Staircase of Image 4, tall 9:16. Image 1 is the strap, Image 2 its back, Image 3 it worn. Image 5 is her face. Image 6 is the style.
From the hall floor, three-quarter, sharp on her right knee: the same woman as Image 5, seventy-one, coming down the last steps facing the lens, right foot flat on the bottom step, hands free at her sides, four chunky fingers and a thumb; {NW}, tan slippers; on her bare right knee {SHAPE} 12 × 5 cm, a quarter of the frame wide, {PLACE}; a closed-mouth smile, eyes on the hall. Scale true to the set: the newel comes up to her waist.
In frame: her, the bottom steps, the newel; the rest as in Image 4.
{HALL} {SPLIT} {PLAIN} Not a brace.''', [FRONT, BACK, WORN, P0, NF, ST], True, True, True, True, None)
fails = 0
for b, (pr, refs, face, body, room, prod, eo) in P.items():
    risk = "hand_product" if prod and b in ("R-04a", "R-06b") else ("stairs" if b in ("R-07a", "R-07c") else None)
    c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(b), "face": face, "room": room, "body": body,
         "refs": [{"label": r["label"], "kind": r["kind"]} for r in refs], "match": "plate" if eo else None, "edit_of": eo["job"] if eo else None, "taste": TASTE_P if prod else TASTE,
         "anatomy": False, "anat_style": None, "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None, "fix_note": FIX[b], "product": prod, "risk_class": risk,
         "medias": [r["job"] for r in refs], "board_refs": [{"label": r["label"], "kind": r["kind"], "ref": r["ref"], "role": f"Image {i + 1}"} for i, r in enumerate(refs)]}
    (H / f"{b}.v3.prompt.txt").write_text(pr); (H / f"{b}.v3.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v3.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
