#!/usr/bin/env python3
"""Act 3 (the reveal + payoff, N-D3a/N-D3) — §6A short beat prompts, Mode 2, A/B pair on nano_banana_pro.
Non-product beats are image edits of the confirmed plate (HT17). Product beats (PIX-SPLIT) attach the strap photos first
(FP01, FP12: front, back, + the angle's photo), the strap at least a quarter of the frame (FP11), true size (FP02), placement (FP03).
Writes body3/<BEAT>.v1.prompt.txt + .preflight.json and runs preflight.py."""
import json, subprocess, sys
from pathlib import Path
H = Path(__file__).parent
PF = H / "../../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(H.parent / "work/actmap_rows.json"))}
M = json.load(open(H / "media.json"))
def L(b):
    t = rows[b]["line"]; out = []; q = 0
    for ch in t:   # curly quotes inside the line, so the prompt's own "…" stays intact (EDIT_OPEN)
        if ch == '"': out.append("“" if q % 2 == 0 else "”"); q += 1
        else: out.append(ch)
    return "".join(out)
B = "stryde-71-stairs-pixar-song__"
P0 = {"label": "P0-PROP-N plate (confirmed) — the hall and staircase", "kind": "location", "job": "377f63fd-7b11-4db2-a663-052e8c0637e8", "ref": B + "P0-PROP-N"}
P2 = {"label": "P2-KITCHEN plate v2 (confirmed)", "kind": "location", "job": "2484470e-dbda-4935-b1f2-0897e8418066", "ref": B + "P2-KITCHEN"}
C1 = {"label": "C1-LORETTA sheet v2 (confirmed) — face and hair only (HT26)", "kind": "character", "job": "fce3f6cb-9ef5-47b5-996b-f9c62e893bc8", "ref": B + "C1-LORETTA"}
C1L = {"label": "C1-LORETTA sheet v2 (confirmed) — her legs and skin only (no face in this shot)", "kind": "frame", "job": "fce3f6cb-9ef5-47b5-996b-f9c62e893bc8", "ref": B + "C1-LORETTA"}
N = {"label": "N-NARR sheet v2 (confirmed) — face and hair only (HT26)", "kind": "character", "job": "32b8bfc2-4538-4c28-b485-3fd28fc5d489", "ref": B + "N-NARR"}
ST = {"label": "P-05c frame v5 A (confirmed) — the style: render, materials, light, proportions", "kind": "style", "job": "5b40a12a-24f5-4d12-8650-016a8b0384ae", "ref": B + "P-05c"}
BRACE = {"label": "P-03b frame v11 A (confirmed) — the old hinged brace", "kind": "frame", "job": "6ca76930-8e96-4da8-8f1c-de4465a37d80", "ref": B + "P-03b"}
FRONT = {"label": "front.webp — the strap, front (product photo)", "kind": "product", "job": M["front"], "ref": "products/stryde/stryde_refs/front.webp"}
BACK = {"label": "back.webp — the strap, back (product photo)", "kind": "product", "job": M["back"], "ref": "products/stryde/stryde_refs/back.webp"}
WORN = {"label": "worn_front.jpg — the strap worn, front-on (product photo)", "kind": "product", "job": M["worn_front"], "ref": "products/stryde/stryde_refs/worn_front.jpg"}
TQ = {"label": "product_tq_left.jpg — the strap, three-quarter (product photo)", "kind": "product", "job": M["product_tq_left"], "ref": "products/stryde/stryde_refs/product_tq_left.jpg"}
KIT = "A final frame from a 3D animated feature film, stylized storybook render, soft morning window light."
HALL = "A final frame from a 3D animated feature film, stylized storybook render, warm afternoon sun from the door."
SPLIT = "The strap alone in real materials, matte shell, chrome slides, knit band, in the same light."
STRAP = "the strap of Image 1 copied exactly,"
PLACE = "the kneecap's lower edge in its notch"
LW = "a teal three-quarter-sleeve blouse, khaki trousers"
NW = "a rose-pink short-sleeve blouse, a denim skirt ending above the knee"
PLAIN = "No lettering, logos or labels but its wordmark."
TASTE = ["HT03", "HT04", "HT08", "HT12", "HT17", "HT21", "HT22", "HT25", "HT26", "FP13", "FP14", "FP17"]
TASTE_P = TASTE + ["FP01", "FP02", "FP03", "FP05", "FP06", "FP07", "FP10", "FP11", "FP12"]
P = {}
# (prompt, refs, face, body, room, product, edit_of)
P["R-01a"] = (f'''For the line "{L("R-01a")}": Keep this photo exactly as it is — the hall, the front door, the staircase, the photo wall, the floor — seen from the foot of the stairs toward the open front door, a tall 9:16 crop, and add the visitor. Image 1 is the hall. Image 2 is the visitor — her face and silver bob only. Image 3 is the style — the same render, materials, light and proportions.
Medium shot at eye level, sharp on her: the same woman as Image 2, seventy-four, stepping in over the threshold of the open door, facing the lens, in {LW} and white canvas slip-ons, a small brown overnight bag in her right hand, her left hand on the door edge, four chunky fingers and a thumb on each, a warm closed-mouth smile, eyes on the staircase. Scale true to the set: the door handle comes up to her hip.
In frame: her, the open door with sun in the sidelights, the coat stand and the newel of Image 1; every other surface as in Image 1.
{HALL} No lettering, logos or labels; not the khaki shorts of Image 2.''', [P0, C1, ST], True, True, True, False, P0)
P["R-02a"] = (f'''For the line "{L("R-02a")}": Keep this photo exactly as it is — the kitchen, the round table and its lace cloth, the chairs, the window light — across the table, a tall 9:16 crop; add two women. Image 1 is the kitchen. Image 2 is the visitor, Image 3 the host — face and hair only. Image 4 is the style.
Medium shot over the visitor's right shoulder, sharp on the table: soft in the near foreground the same woman as Image 2, her back three-quarter to us, in a teal blouse, a mug in both hands; across the table, facing the lens, the same woman as Image 3, seventy-one, in a rose-pink blouse, setting a white gel tube down by two pill bottles, a glass of water and a folded black brace, her other hand on the cloth, four chunky fingers and a thumb on each, eyes on the tube, lips closed. Scale true to the set: the table edge comes up to her waist.
In frame: the two women, those things on the cloth, the kitchen beyond; every other surface bare.
{KIT} No lettering, logos or labels; not the mustard top of Image 3.''', [P2, C1, N, ST], True, True, True, False, P2)
P["R-02b"] = (f'''For the line "{L("R-02b")}": Keep this photo exactly as it is — the round table, its lace cloth, the window light — straight down from above onto the table, a tall 9:16 crop, and lay out her routine. Image 1 is the kitchen. Image 2 is the old brace — the same black hinged knee brace. Image 3 is the style — the same render, materials and light.
Overhead close-up of the table of Image 1, sharp on her hands, her fingertips facing the lens's top edge: her brown left hand squeezes a plain white gel tube, a line of gel landing on the fingers of her right hand, four chunky fingers and a thumb on each; around them two white tablets on the cloth, a glass of water, the brace of Image 2 folded flat, and a blue ice pack. Scale true to the set: the tube reaches from her wrist to her fingertips.
In frame: two hands, the tube, two tablets, the glass, the brace, the ice pack, the lace cloth; every other surface bare.
{KIT} Tube, brace and ice pack plain — no lettering, logos or labels.''', [P2, BRACE, ST], False, True, True, False, P2)
P["R-03a"] = (f'''For the line "{L("R-03a")}": Keep this photo exactly as it is — the kitchen, the round table and its lace cloth, the window light — across the table, a tall 9:16 crop, and add the visitor. Image 1 is the kitchen. Image 2 is the visitor — her face and silver bob only. Image 3 is the style — the same render, materials and light.
Medium close-up from low, sharp on her face: the same woman as Image 2, seventy-four, seated across the table in a teal three-quarter-sleeve blouse, in three-quarter view facing frame left, leaning in over the cloth with a half smile, lips closed, looking away past the lens; her right arm reaching down below the table edge toward her own knee, her left hand flat on the cloth beside a white mug, four chunky fingers and a thumb on each. Scale true to the set: the table edge comes up to her chest.
In frame: her from the chest up, the mug, the table edge, the kitchen of Image 1 behind; every other surface bare.
{KIT} No lettering, logos or labels; not the khaki shorts of Image 2.''', [P2, C1, ST], True, True, True, False, P2)
P["R-03b"] = (f'''For the line "{L("R-03b")}": Kitchen of Image 4, tall 9:16. Image 1 is the strap, Image 2 its back, Image 3 it worn. Image 5 is the visitor's face and bob only. Image 6 is the style.
Close shot from low at knee height, sharp on her right knee: the same woman as Image 5, seventy-four, seated, chair turned out from the table, facing the lens, right leg forward, both hands rolling her khaki trouser leg above the bare knee, four chunky fingers and a thumb on each; on the knee {STRAP} 12 × 5 cm, the shell about a third of the frame wide, {PLACE}; her face above, a knowing half smile, lips closed, looking away past the lens. Scale true to the set: the table edge comes up to her chest.
In frame: knee, hands, face, the table edge; every other surface bare.
{KIT} {SPLIT} {PLAIN}''', [FRONT, BACK, WORN, P2, C1, ST], True, True, True, True, None)
P["R-04a"] = (f'''For the line "{L("R-04a")}": A tall 9:16 frame. Image 1 is the strap, Image 2 its back, Image 3 it worn front-on. Image 4 is the leg and skin to copy. Image 5 is the style — the same render, materials and light.
Extreme close-up front-on at knee height, the knee facing the lens, sharp on the strap: a seated older woman's bare right knee, medium-brown skin, filling the frame; on it {STRAP} 12 × 5 cm, the shell half the frame wide, {PLACE}, its top edge level with the kneecap's lower edge, the wordmark level; her right fingertip taps the top of the shell, four chunky fingers and a thumb; a soft warm kitchen far behind.
In frame: the knee, the strap, one hand; every other surface plain.
{KIT} {SPLIT} {PLAIN}''', [FRONT, BACK, WORN, C1L, ST], False, True, False, True, None)
P["R-05a"] = (f'''For the line "{L("R-05a")}": At the table of Image 3, tall 9:16. Image 1 is the strap, Image 2 its back. Image 4 is the woman's face and twist-out only. Image 5 is the style.
Close-up from high, her own view, sharp on her palm: {STRAP} resting across the open right palm of the same woman as Image 4, front up, 12 × 5 cm, no longer than her palm, about a third of the frame wide, her thumb beside the shell, four chunky fingers and a thumb; her face soft above in a rose-pink blouse, eyebrows raised, doubtful, lips closed, eyes on the strap, facing the lens. Scale true to the set: her hand comes up to her chest.
In frame: her hand, the strap, her face, the lace cloth below; every other surface bare.
{KIT} {SPLIT} {PLAIN} Not the mustard top of Image 4.''', [FRONT, BACK, P2, N, ST], True, True, True, True, None)
P["R-06a"] = (f'''For the line "{L("R-06a")}": Kitchen of Image 3, tall 9:16. Image 1 is the strap, Image 2 its back. Image 4 is the host, Image 5 the visitor — face and hair only. Image 6 is the style.
Two-shot across the table, both in profile, sharp on the strap: the same woman as Image 4, seventy-one, rose-pink blouse, facing frame right, holds {STRAP} up on her open right palm between them, front to the lens, 12 × 5 cm, a quarter of the frame wide; one eyebrow up, lips closed, eyes on the strap. Across, the same woman as Image 5, teal blouse, facing frame left, unbothered, hands round a mug, eyes on her. Four chunky fingers and a thumb on every hand. Scale true to the set: the table edge comes up to their waists.
In frame: two women, the strap, a mug, the cloth; every other surface bare.
{KIT} {SPLIT} {PLAIN}''', [FRONT, BACK, P2, N, C1, ST], True, True, True, True, None)
P["R-06b"] = (f'''For the line "{L("R-06b")}": Kitchen of Image 4, tall 9:16. Image 1 is the strap, Image 2 its back, Image 3 its three-quarter view. Image 5 is the style.
Close-up from high three-quarter, her own view, sharp on the strap: a seated older Black woman's bare right shin and knee, the denim skirt hem just above the knee, both hands sliding {STRAP} up the shin, 12 × 5 cm, a third of the frame wide, its top edge reaching the kneecap's lower edge, the band round the leg; four chunky fingers and a thumb on each; a tan slipper below. Scale true to the set: the hem comes to her knee.
In frame: one leg, two hands, the strap, a chair edge, the floor; every other surface bare.
{KIT} {SPLIT} {PLAIN}''', [FRONT, BACK, TQ, P2, ST], False, True, True, True, None)
P["R-07a"] = (f'''For the line "{L("R-07a")}": Staircase of Image 4, tall 9:16. Image 1 is the strap, Image 2 its back, Image 3 it worn. Image 5 is the woman's face and twist-out only. Image 6 is the style.
Low from three steps below, looking up, sharp on her right knee: the same woman as Image 5, seventy-one, stepping down from the top step facing forwards toward the lens, right foot landing flat on the next step, hands loose at her sides, four chunky fingers and a thumb; {NW}, tan slippers; on her bare right knee {STRAP} 12 × 5 cm, the shell a quarter of the frame wide, {PLACE}; a proud closed-mouth smile, eyes on the step. Scale true to the set: her knee is level with the newel cap.
In frame: her, the flight, the rail; the rest as in Image 4.
{HALL} {SPLIT} {PLAIN} Not the mustard top of Image 5.''', [FRONT, BACK, WORN, P0, N, ST], True, True, True, True, None)
P["R-07c"] = (f'''For the line "{L("R-07c")}": Staircase of Image 4, tall 9:16. Image 1 is the strap, Image 2 its back, Image 3 it worn. Image 5 is the woman's face and twist-out only. Image 6 is the style.
From the hall floor, three-quarter, sharp on her right knee: the same woman as Image 5, seventy-one, coming down the last steps facing the lens, right foot flat on the bottom step, hands free at her sides, four chunky fingers and a thumb; {NW}, tan slippers; on her bare right knee {STRAP} 12 × 5 cm, the shell a quarter of the frame wide, {PLACE}; a closed-mouth smile, eyes on the hall. A teal shoulder soft in front. Scale true to the set: the newel comes up to her waist.
In frame: her, the bottom steps, the newel; the rest as in Image 4.
{HALL} {SPLIT} {PLAIN} Not the mustard top of Image 5.''', [FRONT, BACK, WORN, P0, N, ST], True, True, True, True, None)
fails = 0
only = set(sys.argv[1:])
for b, (pr, refs, face, body, room, prod, eo) in P.items():
    if only and b not in only: continue
    risk = "hand_product" if prod and b in ("R-04a", "R-05a", "R-06a", "R-06b") else ("stairs" if b in ("R-07a", "R-07c") else None)
    c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(b), "face": face, "room": room, "body": body,
         "refs": [{"label": r["label"], "kind": r["kind"]} for r in refs], "match": "plate" if eo else None, "edit_of": eo["job"] if eo else None, "taste": TASTE_P if prod else TASTE,
         "anatomy": False, "anat_style": None, "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None, "fix_note": None, "product": prod, "risk_class": risk,
         "medias": [r["job"] for r in refs], "board_refs": [{"label": r["label"], "kind": r["kind"], "ref": r["ref"], "role": f"Image {i + 1}"} for i, r in enumerate(refs)]}
    (H / f"{b}.v1.prompt.txt").write_text(pr); (H / f"{b}.v1.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v1.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
