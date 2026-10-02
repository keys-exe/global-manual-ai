#!/usr/bin/env python3
"""Act 4 (M-01a…M-06a) image pairs + the Act 3 Fix pairs R-04a v7 and R-07a v7 (user's board notes, 2026-10-02).
 - R-04a "this should be the right knee" → both knees front-on, the strap on her RIGHT knee at frame left, her left knee bare at frame right (Loretta's R-03b frame for skin/clothes, HT27).
 - R-07a "she should be at the 2nd floor" → an image edit of the v2 frame (her own staircase): she moves up to the top step at the second-floor landing.
 - Act 4 anatomy styles (§12A-1, new beats): M-02a S2 X-ray card (T-03a X-ray as the style), M-03a S1 Ghost (the S1 reference as the style, V7.86.1),
   M-05a S7 cross-section, M-05b S1 Ghost — S1 on two of four, never back to back; angles FRONT · LAT · LAT-WIDE · LOW34.
Writes <dir>/<BEAT>.<v>.prompt.txt + .preflight.json and runs preflight.py."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent; B3 = H.parent / "body3"
PF = H / "../../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(H.parent / "work/actmap_rows.json"))}
M = json.load(open(B3 / "media.json"))
def L(b): return re.sub(r'["“”]', "", rows[b]["line"])
ID = "stryde-71-stairs-pixar-song__"
def ref(label, kind, job, r): return {"label": label, "kind": kind, "job": job, "ref": r}
P0 = ref("P0-PROP-N plate (confirmed) — her hall and staircase", "location", "377f63fd-7b11-4db2-a663-052e8c0637e8", ID + "P0-PROP-N")
P2 = ref("P2-KITCHEN plate v2 (confirmed)", "location", "2484470e-dbda-4935-b1f2-0897e8418066", ID + "P2-KITCHEN")
P7 = ref("P7-CLINIC plate (confirmed)", "location", "593880dc-2b40-44b6-a884-a8277d888d3a", ID + "P7-CLINIC")
L_FR = ref("R-03b frame v1 A (confirmed) — Loretta's skin, rolled khaki trouser, teal blouse (HT27)", "frame", "179dfe8a-7ef0-4b2e-8ebd-f8558f58a15f", ID + "R-03b")
N_FR = ref("R-06a frame v2 B (confirmed) — N's skin and day-three clothes (HT27)", "frame", "37cf0d7a-06aa-4d40-ad45-821191a13086", ID + "R-06a")
N_PT = ref("P-04b frame v3 (confirmed) — N on the PT table, the clinic day's clothes (HT27)", "character", "d6e85763-5356-4351-8f90-f4fc5eec9aa8", ID + "P-04b")
R07 = ref("R-07a frame v2 A (to check) — her own staircase from the hall", "frame", "cae28c19-5ab2-4745-90a7-c5cb98963343", ID + "R-07a")
P04A = ref("P-04a frame v3 (confirmed) — the routine laid out on her kitchen table, from above", "frame", "e05783fd-e5e1-4e31-b247-3a8c950954b6", ID + "P-04a")
STH = ref("P-04a frame v3 (confirmed, hands on her table, no outfit in it) — the style", "style", "e05783fd-e5e1-4e31-b247-3a8c950954b6", ID + "P-04a")
XR = ref("T-03a frame v4 B (confirmed) — the film's X-ray look", "style", "3398f2c7-07d9-4166-bc1b-2424a8b2aad7", ID + "T-03a")
S1 = ref("S1 Ghost reference (references/anatomy/S1_ghost.webp) — the house anatomy look", "style", "64644b4c-c8c8-47ee-bceb-d6ac81b441ab", ".claude/skills/ai-prompt-engineer/references/anatomy/S1_ghost.webp")
FRONT = ref("front.webp — the strap, front (product photo)", "product", M["front"], "products/stryde/stryde_refs/front.webp")
BACK = ref("back.webp — the strap, back (product photo)", "product", M["back"], "products/stryde/stryde_refs/back.webp")
WORN = ref("worn_front.jpg — the strap worn, front-on (product photo)", "product", M["worn_front"], "products/stryde/stryde_refs/worn_front.jpg")
KIT = "A final frame from a 3D animated feature film, stylized storybook render, soft morning window light."
HALL = "A final frame from a 3D animated feature film, stylized storybook render, warm afternoon sun from the door."
CLIN = "A final frame from a 3D animated feature film, stylized storybook render, soft clinic daylight."
ANIM = "A final frame from a 3D animated feature film, stylized storybook render."
SPLIT = "The strap alone in real materials, in the same light."
SHAPE = "the strap of Image 1 copied exactly — a black shell, two pointed peaks round a notch, a chrome slide at each end —"
PLAIN = "No lettering, logos or labels but its wordmark."
TASTE = ["HT03", "HT04", "HT08", "HT12", "HT17", "HT21", "HT22", "HT25", "HT26", "HT27", "FP13", "FP14", "FP17"]
TASTE_P = TASTE + ["FP01", "FP02", "FP03", "FP05", "FP06", "FP07", "FP10", "FP11", "FP12"]
TASTE_A = ["HT11", "HT18", "HT21", "FP03", "FP13"]
J = {}   # beat: (dir, tag, prompt, refs, face, body, room, product, edit_of, anatomy, style, fix_note)
J["R-04a"] = (B3, "v7", f'''For the line "{L("R-04a")}": A tall 9:16 frame. Image 1 is the strap, Image 2 its back, Image 3 it worn front-on. Image 4 is the visitor — her deep brown skin, rolled khaki trousers and teal blouse exactly as in Image 4. Image 5 is the style.
Close-up front-on at knee height, seated, both knees facing the lens side by side, sharp on the strap: the visitor's two bare knees, her khaki trousers rolled above both; on her RIGHT knee — on the left of the frame — {SHAPE} 12 × 5 cm, the shell a third of the frame wide, the kneecap's lower edge in its notch, the wordmark level; her LEFT knee on the right of the frame bare, no strap; her right fingertip taps the shell, four chunky fingers and a thumb. Scale true to the set: the knees fill the frame side to side.
In frame: two knees, one strap, one hand; every other surface plain.
{KIT} {SPLIT} {PLAIN}''', [FRONT, BACK, WORN, L_FR, STH], False, True, False, True, None, False, None,
 'user Fix "this should be the right knee" → both knees front-on, the strap on her right knee (frame left), her left knee bare (frame right)')
J["R-07a"] = (B3, "v8", f'''For the line "{L("R-07a")}": Keep this photo exactly as it is — the staircase, runner, rods, newel, photo wall, viewpoint and woman — and move her all the way up: she stands on the second-floor landing at the head of the flight, at the top of the frame. Image 1 is the photo. Image 2 is the strap. Image 3 is the style.
Full shot, sharp on her: the woman of Image 1 small on the landing at the top, facing the lens, right foot reaching for the first step down, hands loose off the rail, four chunky fingers and a thumb, tan slippers; on her bare right knee the strap of Image 2, below the kneecap; a proud closed-mouth smile, looking down at the next step. Every step below her empty, the newel at the bottom of the frame. Scale: she stands as tall as four steps.
In frame: her, the full flight; the rest as Image 1.
{HALL} {SPLIT} {PLAIN}''', [R07, FRONT, STH], True, True, True, False, R07, False, None,
 'user Fix "she should be at the 2nd floor" → an edit of the v2 frame (her own staircase), she starts on the second-floor landing at the head of the flight · v7 kept off: B left her mid-flight, A failed on Higgsfield → the landing named as the top of the frame, every step below her empty')
J["M-01a"] = (H, "v1", f'''For the line "{L("M-01a")}": Treatment room of Image 1, tall 9:16. Image 2 is the woman — her face, silver twist-out and the clinic day's clothes exactly as in Image 2. Image 3 is the style.
Medium shot from directly overhead, sharp on her face: the same woman as Image 2, seventy-one, lying back on the padded treatment table, head on a small pillow, eyes closed, mouth closed, facing up to the lens; a grey heat pad folded over her right knee, her two hands resting on her stomach, four chunky fingers and a thumb on each. Scale true to the set: the table is a little longer than she is tall.
In frame: her, the table, the heat pad; every other surface bare.
{CLIN} Walls and table plain — no lettering, logos or labels.''', [P7, N_PT, STH], True, True, True, False, None, False, None, None)
J["M-02a"] = (H, "v1", f'''For the line "{L("M-02a")}": An X-ray card in the film's world, tall 9:16. Image 1 is the strap. Image 2 is the style — the film's X-ray look, copied exactly.
Two knees side by side, front-on, level, bright blue-white bone on a deep black field, soft tissue faint grey, each knee a third of the frame wide. The LEFT knee wears a full knee sleeve, drawn as a faint grey outline over the whole joint, a soft amber haze spread evenly across all of it. The RIGHT knee wears {SHAPE} 12 × 5 cm, crisp and dark on the X-ray, seated just under the kneecap on the tendon, and one small warm glow on that one spot.
In frame: two knees, the sleeve outline, the strap; every other area plain dark.
{ANIM} {SPLIT} Film plain — no lettering, labels or measurement marks.''', [FRONT, XR], False, False, False, True, None, True, "S2", None)
J["M-03a"] = (H, "v1", f'''For the line "{L("M-03a")}": Image 1 is the style — copy its look exactly: a smoky see-through outline of the right knee like soft mist, no skin or muscle, warm ivory-peach bones with a soft inner glow, pearly white tendons and ligaments, a deep navy-black field with faint particles.
Close-up in true side profile from a little below the joint, the leg running up the frame, sharp on the tendon under the kneecap: the kneecap, the thigh-bone end, the shin-bone top and the pearly patellar tendon between them; on that tendon, a finger's width under the kneecap, one small round red point glowing, the size of a coin, the only colour in the frame. Scale: the kneecap about a quarter of the frame wide.
In frame: the knee outline, the bones, the tendon, the red point; every other area plain dark.
{ANIM} No lettering, labels or arrows.''', [S1], False, False, False, False, None, True, "S1", None)
J["M-04a"] = (H, "v1", f'''For the line "{L("M-04a")}": Keep this photo exactly as it is — the kitchen table from above, the cloth, the light, the braces, sleeves, pill bottles and gel tube in their places — and take her hands out of it; add one small plain white box of syringes beside the pill bottles. Image 1 is the photo. Image 2 is the style.
Overhead, sharp on the heap: the whole routine laid out on the table — braces, sleeves, pill bottles, the gel tube, an ice pack and the syringe box — the heap filling the middle half of the frame, nobody in the frame.
In frame: the table, the heap; every other surface bare.
{KIT} Bottles, box and packs plain — no lettering, logos or labels.''', [P04A, STH], False, False, True, False, P04A, False, None, None)
J["M-05a"] = (H, "v1", f'''For the line "{L("M-05a")}": A clean 3D cross-section of the right knee, cut along one plane like a layered cake on a neutral grey field: the outer contour, soft tissue, the patellar tendon and the bones in order. Image 1 is the style — the same render and materials.
Medium shot in true side profile, the whole leg from mid-thigh to mid-shin running up the frame, sharp on the tendon under the kneecap: a knee sleeve drawn as a faint outline round the whole joint; one small red point glowing on the tendon just under the kneecap, shining through the sleeve; three soft red pressure lines running down the thigh into that point. Scale: the knee about a third of the frame wide.
In frame: the cut leg, the sleeve outline, the red point and lines; every other area plain grey.
{ANIM} No lettering, labels or arrows.''', [STH], False, False, False, False, None, True, "S7", None)
J["M-05b"] = (H, "v1", f'''For the line "{L("M-05b")}": Image 1 is the strap. Image 2 is the style — copy its look exactly: a smoky see-through outline of the right knee like soft mist, no skin or muscle, warm ivory-peach bones with a soft inner glow, pearly white tendons, a deep navy-black field with faint particles.
Close-up from a low three-quarter angle, sharp on the strap: {SHAPE} 12 × 5 cm, a third of the frame wide, seated on the patellar tendon just under the kneecap, its pad pressed on the spot; under the pad the last of a red glow fading into a calm soft blue that spreads along the tendon. Scale: the kneecap the width of the shell.
In frame: the knee outline, the bones, the tendon, the strap; every other area plain dark.
{ANIM} {SPLIT} {PLAIN}''', [FRONT, S1], False, False, False, True, None, True, "S1", None)
J["M-06a"] = (H, "v1", f'''For the line "{L("M-06a")}": Staircase of Image 3, tall 9:16. Image 1 is the strap, Image 2 it worn. Image 4 is the woman — her deep brown skin, denim skirt and tan slippers. Image 5 is the style.
Close-up from the step below at ground level, looking up, sharp on the strap: her right foot in a tan slipper landing flat on the top step's carpet runner, a brass rod beside it; above it her bare right shin and knee with {SHAPE} 12 × 5 cm, a third of the frame wide, the kneecap's lower edge in its notch, the hem of the denim skirt just above; her arms at her sides above the frame, each hand four chunky fingers and a thumb; the family photos soft and small far behind. Scale true to the set: the slipper as long as the tread is deep, her shin facing the lens.
In frame: one foot, one leg, the strap, the top step; the rest as Image 3, soft.
{HALL} {SPLIT} {PLAIN}''', [FRONT, WORN, P0, N_FR, STH], False, True, True, True, None, False, None, None)
J["M-02a"] = (H, "v2", f'''For the line "{L("M-02a")}": An X-ray card in the film's world, tall 9:16. Image 1 is the strap, Image 2 it worn front-on — copy its shape and where it sits exactly. Image 3 is the style — the film's X-ray look.
Two knees side by side, front-on, level, blue-white bone on a black field, each knee a third of the frame wide. The LEFT knee wears a full knee sleeve, a faint grey outline over the whole joint, a soft amber haze across all of it. On the RIGHT knee, drawn solid in real materials over the X-ray, {SHAPE} 12 × 5 cm, as wide as the knee, its front to the lens, the wordmark level: the kneecap's lower edge sits in its notch, the shell on the tendon just under the kneecap, the band round the back of the leg; one small warm glow under the shell.
In frame: two knees, the sleeve outline, one strap; every other area plain dark.
{ANIM} {SPLIT} Film plain — no lettering, labels or measurement marks.''', [FRONT, WORN, XR], False, False, False, True, None, True, "S2",
 'user Fix "fix the product and palcement" → the worn-strap photo as Image 2 for its placement, the strap drawn solid in real materials over the X-ray, the kneecap\'s lower edge in its notch, the shell on the tendon just under the kneecap')
# ---- user 2026-10-02: "about all the anatomy here we will use the normal anatomy" → every anatomy beat is the S3 natural-colour anatomical model
NORM = "A clean 3D medical anatomy model of the right knee on a pale grey seamless background, in natural tissue colours — red muscle, white tendons and ligaments, ivory bone — soft even light, textbook clarity."
NA = 'user 2026-10-02: "about all the anatomy here we will use the normal anatomy" → the natural-colour anatomical model (S3) on a pale grey background'
J["M-02a"] = (H, "v3", f'''For the line "{L("M-02a")}": {NORM} Image 1 is the strap, Image 2 it worn front-on — copy its shape and where it sits exactly. Image 3 sets the light only.
Two knee models side by side, front-on, level, each a third of the frame wide. The LEFT knee wears a full knee sleeve, a faint grey outline with a soft amber haze over the whole joint. On the RIGHT knee, {SHAPE} 12 × 5 cm, as wide as the knee, its front to the lens, the wordmark level: the kneecap's lower edge sits in its notch, the shell on the tendon just under the kneecap, the band round the back; one small warm glow under the shell.
In frame: two knee models, the sleeve outline, one strap; every other area plain grey.
{ANIM} {SPLIT} No lettering, labels or arrows.''', [FRONT, WORN, STH], False, False, False, True, None, True, "S3",
 NA + ' · and the earlier Fix "fix the product and palcement": the worn-strap photo for its placement, the kneecap\'s lower edge in its notch')
J["M-02a"] = (H, "v4", f'''For the line "{L("M-02a")}": {NORM} Image 1 is the strap. Image 2 sets the light only.
Two knee models side by side, front-on, level, each cut just above and below the joint, each a third of the frame wide. The LEFT knee wears a full knee sleeve, a faint grey outline with a soft amber haze over the whole joint. On the RIGHT knee, {SHAPE} 12 × 5 cm, as wide as the knee, its front to the lens, the wordmark level: the kneecap's lower edge sits in its notch, the shell on the white tendon just under the kneecap, the band round the back; one small warm glow under the shell.
In frame: two knee models, the sleeve outline, one strap; every other area plain grey, no skin.
{ANIM} {SPLIT} No lettering, labels or arrows.''', [FRONT, STH], False, False, False, True, None, True, "S3",
 NA + ' · v3 kept off: the worn-strap photo printed a real hairy leg and a room under both models → the worn photo dropped, each model cut above and below the joint on plain grey')
J["M-03a"] = (H, "v2", f'''For the line "{L("M-03a")}": {NORM} Image 1 sets the light only.
Close-up in true side profile from a little below the joint, the leg running up the frame, sharp on the tendon under the kneecap: the thigh muscles, the kneecap, the thigh-bone end, the shin-bone top and the white patellar tendon between them; on that tendon, a finger's width under the kneecap, one small round red point glowing, the size of a coin. Scale: the kneecap about a quarter of the frame wide.
In frame: the knee model, the red point; every other area plain grey.
{ANIM} No lettering, labels or arrows.''', [STH], False, False, False, False, None, True, "S3", NA)
J["M-05a"] = (H, "v2", f'''For the line "{L("M-05a")}": {NORM} Image 1 sets the light only.
Medium shot in true side profile, the whole leg from mid-thigh to mid-shin running up the frame, sharp on the tendon under the kneecap: a knee sleeve drawn as a faint grey outline round the whole joint; one small red point glowing on the white tendon just under the kneecap, shining through the sleeve; three soft red pressure lines running down the thigh muscles into that point. Scale: the knee about a third of the frame wide.
In frame: the leg model, the sleeve outline, the red point and lines; every other area plain grey.
{ANIM} No lettering, labels or arrows.''', [STH], False, False, False, False, None, True, "S3", NA)
J["M-05b"] = (H, "v2", f'''For the line "{L("M-05b")}": {NORM} Image 1 is the strap, Image 2 it worn. Image 3 sets the light only.
Close-up from a low three-quarter angle, sharp on the strap: {SHAPE} 12 × 5 cm, a third of the frame wide, its pad pressed on the white patellar tendon just under the kneecap, the kneecap's lower edge in its notch; under the pad the last of a red glow fading into a calm soft blue spreading along the tendon. Scale: the kneecap the width of the shell.
In frame: the knee model, the strap; every other area plain grey.
{ANIM} {SPLIT} {PLAIN}''', [FRONT, WORN, STH], False, False, False, True, None, True, "S3", NA)
L_ED = ref("R-03b frame v1 A (confirmed) — Loretta at the kitchen table, the strap on her right knee", "frame", "179dfe8a-7ef0-4b2e-8ebd-f8558f58a15f", ID + "R-03b")
J["R-03b"] = (B3, "v4", f'''For the line "{L("R-03b")}": Keep this photo exactly as it is — the kitchen, chair, woman, teal blouse, rolled khaki trousers — change only her pose: she shows the strap off. Image 1 is the photo. Image 2 is the strap. Image 3 is the style.
Medium shot, sharp on the strap: the same woman as Image 1 — her face, skin and silver bob exactly as in Image 1 — seated, her right leg, on the left of the frame, stretched out toward the lens, heel down in its white slipper; on that right knee the strap of Image 2 copied exactly — a black shell, two pointed peaks round a notch, a chrome slide at each end — 12 × 5 cm, a quarter of the frame wide, its front to the lens; her left knee, on the right of the frame, bare; both hands open beside it, presenting it, four chunky fingers and a thumb on each; a proud closed-mouth grin, eyes on the lens. Scale: the chair seat level with her knee.
In frame: her, the chair, one strap; the rest as Image 1.
{KIT} {SPLIT} {PLAIN}''', [L_ED, FRONT, STH], True, True, True, True, L_ED, False, None,
 'user Fix "make her look like she is showing the stryde strap like flexing it" → an edit of her confirmed R-03b frame: the right leg (frame left) stretched toward the lens, both hands presenting the strap, a proud grin · v3 kept off: A a different woman, B the strap on her left knee (FP18) → her face named from Image 1, the sides named in the frame')
# ---- Pixar anatomy (user 2026-10-02 10:5x: "use the new pixar anatomy for all the anatomy / lets re do all the anatomy") — §12A-1 V7.90.2:
# ANAT-PIX opens, then ANAT-PIX-S3 (the team's locked no-muscle "normal anatomy", references/anatomy/S3_pixar_locked.jpg — the look in words, never attached, L32)
ANAT_PIX = "A final frame from a 3D animated feature film, stylized storybook render. The anatomy is drawn the way this film's own animators would draw it: simple, rounded, readable shapes. A clean model of the right knee on a soft plain pale grey backdrop, no muscle anywhere: smooth ivory bones with a soft inner glow, white ribbon tendons and ligaments, the kneecap, inside a soft see-through peach outline of the leg with a cool blue rim on one side; warm key, cool fill, rim."
PIX_S3 = ""   # merged into ANAT_PIX above: ANAT-PIX + ANAT-PIX-S3 in one paragraph (both strings run ~790 chars, over the §6A budget with the beat)
PX = 'user 2026-10-02: "use the new pixar anatomy for all the anatomy / lets re do all the anatomy" → the Pixar S3 normal anatomy (no muscle, the team’s locked pick)'
J["M-02a"] = (H, "v5", f'''For the line "{L("M-02a")}": {ANAT_PIX}
Two such knee models side by side, front-on, level, each a third of the frame wide. The LEFT knee wears a full sleeve, a faint grey outline, a soft amber haze across the joint. On the RIGHT knee, {SHAPE} 12 × 5 cm, as wide as the knee: the kneecap's lower edge in its notch, the shell on the tendon, one small warm glow under it. Image 2 sets the light only.
In frame: two knee models, one sleeve outline, one strap; the rest plain grey. {SPLIT} {PLAIN}''', [FRONT, STH], False, False, False, True, None, True, "S3",
 PX + ' · and the earlier Fix "fix the product and palcement": the strap named with its shape, the kneecap in its notch')
J["M-03a"] = (H, "v3", f'''For the line "{L("M-03a")}": {ANAT_PIX}
Close-up in true side profile from a little below the joint, the leg running up the frame, sharp on the tendon: the kneecap a quarter of the frame wide, the tendon ribbon below it to the shin bone, and on that ribbon a finger's width under the kneecap one small soft warm glow the size of a coin. Image 1 sets the light only.
In frame: the knee model and the glow; the rest plain grey. No lettering, labels or arrows.''', [STH], False, False, False, False, None, True, "S3", PX)
J["M-05a"] = (H, "v3", f'''For the line "{L("M-05a")}": {ANAT_PIX}
Medium shot in true side profile, the leg from mid-thigh to mid-shin running up the frame, the knee a third of the frame wide, sharp on the tendon: a knee sleeve drawn as a faint grey outline round the whole joint; one small soft warm glow on the tendon just under the kneecap, shining through the sleeve; three thin soft warm lines running down the thigh into it. Image 1 sets the light only.
In frame: the leg model, the sleeve outline, the glow and lines; the rest plain grey. No lettering, labels or arrows.''', [STH], False, False, False, False, None, True, "S3", PX)
J["M-05b"] = (H, "v3", f'''For the line "{L("M-05b")}": {ANAT_PIX}
Close-up from a low three-quarter angle, sharp on the strap: {SHAPE} 12 × 5 cm, a third of the frame wide, its pad pressed on the tendon just under the kneecap, the kneecap's lower edge in its notch; under the pad the last of the warm glow fading into a soft cool blue along the tendon. Image 2 sets the light only.
In frame: the knee model, the strap; the rest plain grey. {SPLIT} {PLAIN}''', [FRONT, STH], False, False, False, True, None, True, "S3", PX)
N_R07 = ref("R-07a frame v8 A (confirmed) — N on her own stairs in the day-three clothes: pink cardigan, denim skirt, tan slippers, silver twist-out (HT27)", "character", "11b8a6bb-8c4a-4739-86ce-0c779f413c53", ID + "R-07a")
J["M-06a"] = (H, "v2", f'''For the line "{L("M-06a")}": Staircase of Image 2, tall 9:16. Image 1 is the strap. Image 3 is the woman — her face, silver twist-out, deep brown skin, pink cardigan, denim skirt and slippers exactly as in Image 3. Image 4 is the style.
Low angle from two steps below her, looking up the flight, she faces the lens, sharp on the strap: her right slipper landing flat on the step's runner close to the lens, a brass rod beside it; her bare right knee above with {SHAPE} 12 × 5 cm, a quarter of the frame wide, the kneecap's lower edge in its notch; above, her denim skirt, her pink cardigan, her hands loose at her sides, four chunky fingers and a thumb each, her face at the top, a proud closed-mouth smile, looking down at the step. Scale true to the set: the slipper as long as the tread is deep.
In frame: her, one strap, the steps; the rest as Image 2.
{HALL} {SPLIT} {PLAIN}''', [FRONT, P0, N_R07, STH], True, True, True, True, None, False, None,
 'user Fix "wrong person" → N herself in frame: a low angle from two steps below, her strapped knee and slipper close to the lens, her cardigan, skirt and smiling face above (her confirmed R-07a frame as the woman, HT27)')
B2 = H.parent / "body2"
J["T-03a"] = (B2, "v5", f'''For the line "{L("T-03a")}": {ANAT_PIX}
Two such knee models side by side, front-on, level, each a third of the frame wide, sharp on the joints: in each knee the thigh bone's rounded end resting straight on the top of the shin bone, the gap between them gone, and where the two bones touch one small soft warm glow. The kneecaps above, the tendon ribbons in front. Image 1 sets the light only.
In frame: two knee models and their two glows; the rest plain grey. No lettering, labels or arrows.''', [STH], False, False, False, False, None, True, "S3",
 'user 2026-10-02: "the t03a too" — the Pixar S3 normal anatomy (no muscle) for this bone-on-bone beat as for the Act 4 anatomy; the confirmed S2 X-ray v4 kept on Old 2')
# re-render slots without the scene frame (V7.90.3, L36): M-02a v5 A, M-05a v3 B, T-03a v5 A drew the kitchen table, hands and brace of P-04a
NOFR = ' · kept off: the P-04a frame attached to set the light drew its kitchen table, hands and brace around the models → that frame dropped, the look in words only'
_J = {}
for _b, _t, _old in (("M-02a", "v6", " Image 2 sets the light only."), ("M-05a", "v4", " Image 1 sets the light only."), ("T-03a", "v6", " Image 1 sets the light only.")):
    _d, _tag, _pr, _refs, *_rest = J[_b]
    assert _old in _pr
    _J[_b] = (_d, _t, _pr.replace(_old, ""), [r for r in _refs if r is not STH], *_rest[:-1], _rest[-1] + NOFR)
J.update(_J)
# ---- 2026-10-02 ~11:30 board Fixes: M-03a / M-05a "the point is the patellar tendon" (FP21), M-06a "i want a close up shot of the feet"
PT = "the patellar tendon, drawn as a broad white ribbon from the bottom tip of the kneecap straight down to the bump at the front of the shin bone, about as long as the kneecap, with one small soft warm glow on the middle of that ribbon, below the kneecap and above the bump"
M03P = ref("M-03a v5 A (your pick) — the Pixar anatomy frame, side profile", "frame", "19b8bce7-3e00-47e1-ac1d-d8b96ff50188", ID + "M-03a")
J["M-03a"] = (H, "v7", f'''For the line "{L("M-03a")}": Keep this picture exactly as it is — the knee model, bones, kneecap, see-through outline and grey backdrop, the same side view — and change only the tendon and the glow. Image 1 is the picture, its anatomy drawn the way this film's own animators would draw it: simple, rounded, readable shapes, no muscle anywhere.
At the front of the knee, {PT}. The kneecap itself plain ivory with no glow on it; the joint line between the two big bones plain, no glow there.
In frame: the knee model, the tendon ribbon, the one glow; the rest as Image 1. Warm key, cool fill, rim. A final frame from a 3D animated feature film, stylized storybook render. No lettering, labels or arrows.''', [M03P], False, False, False, False, M03P, True, "S3",
 'user Fix "the poin is the patellar tendon" (on the pick v5) → an edit of v5: the tendon drawn as a broad ribbon from the kneecap tip to the shin bump, the glow on its middle, none on the kneecap (FP21)')
J["M-05a"] = (H, "v5", f'''For the line "{L("M-05a")}": {ANAT_PIX}
Side profile, mid-thigh to mid-shin, the knee a third of the frame wide: a faint grey sleeve outline round the whole joint; at the front of the knee, {PT}; three thin warm lines down the thigh into that glow. No glow on the kneecap.
In frame: the leg model, the sleeve outline, the tendon, glow and lines; the rest plain grey. No lettering, labels or arrows.''', [], False, False, False, False, None, True, "S3",
 'user Fix "the point is the patellar tendon" → the tendon drawn as a broad ribbon from the kneecap tip to the shin bump, the glow on its middle, none on the kneecap (FP21)')
N_R07F = ref("R-07a frame v8 A (confirmed) — N on her own stairs: her skin, tan slippers, denim skirt (HT27)", "frame", "11b8a6bb-8c4a-4739-86ce-0c779f413c53", ID + "R-07a")
J["M-06a"] = (H, "v3", f'''For the line "{L("M-06a")}": Staircase of Image 2, tall 9:16. Image 1 is the strap. Image 3 is the woman — her deep brown skin, tan slippers and denim skirt exactly as in Image 3. Image 4 is the style.
Close-up of her feet from the step below at ground level, she faces the lens, sharp on her feet: her right foot in its tan slipper landing flat on the step's carpet runner close to the lens, a brass rod beside it, her left slipper on the step above; her two bare shins rising up the frame, and at the top of the frame her right knee, on the left of the frame, with {SHAPE} 12 × 5 cm, a quarter of the frame wide, the kneecap's lower edge in its notch; her hands out of frame at her sides. Scale true to the set: each slipper as long as the tread is deep.
In frame: two feet, two shins, one strap, two steps; the rest as Image 2, soft.
{HALL} {SPLIT} {PLAIN}''', [FRONT, P0, N_R07F, STH], False, True, True, True, None, False, None,
 'user Fix "i want a close up shot of the feet" → a ground-level close-up of her slippered feet landing on the step, her shins and the strap on her right knee at the top of the frame; earlier Fix "wrong person" still in force: her own skin and slippers from her confirmed R-07a frame (HT27)')
fails = 0
ONLY = [x for x in sys.argv[1:]]
for b, (d, tag, pr, refs, face, body, room, prod, eo, anat, st, fn) in J.items():
    if ONLY and b not in ONLY: continue
    risk = "hand_product" if b in ("R-04a",) else ("stairs" if b in ("R-07a", "M-06a") else None)
    c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(b), "face": face, "room": room, "body": body,
         "refs": [{"label": r["label"], "kind": r["kind"]} for r in refs], "match": ("frame" if eo["kind"] == "frame" else "plate") if eo else None, "edit_of": eo["job"] if eo else None,
         "taste": TASTE_A if anat else (TASTE_P if prod else TASTE), "anatomy": anat, "anat_style": st, "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None,
         "fix_note": fn, "product": prod, "risk_class": risk, "first_frame": False, "pixar_anatomy": bool(anat and "drawn the way this film's own animators" in pr),
         "medias": [r["job"] for r in refs], "board_refs": [{"label": r["label"], "kind": r["kind"], "ref": r["ref"], "role": f"Image {i + 1}"} for i, r in enumerate(refs)]}
    (d / f"{b}.{tag}.prompt.txt").write_text(pr); (d / f"{b}.{tag}.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(d / f"{b}.{tag}.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
