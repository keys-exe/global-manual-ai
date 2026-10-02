#!/usr/bin/env python3
"""Act 3 Fix round (user's board notes, 2026-10-02):
 - R-04a "this should be loreta same clothes too" → her confirmed R-03b frame (v1 A) as Image 4: her skin, her rolled khaki trouser leg, her teal blouse (HT27);
 - R-05a "product too small and wrong product" → product photos first, the shell's shape named, the strap half the frame wide, N from her confirmed R-06a frame (v2 B, HT27);
 - R-06b "wrong product and this is not the pixar anymore" → the confirmed R-03b frame as the style (a stylized leg with the right strap), the leg called smooth and simplified, N's skin and clothes from her R-06a frame;
 - R-07a "wrong stairs" + R-07c "this should be part of the r07a so it should be one take only" → one take for both lines: an image edit of the confirmed
   P0-PROP-N plate (her own staircase: carpet runner, brass rods, white balusters, oak rail, square newel, photo wall), N from her R-06a frame.
Writes body3/<BEAT>.v5.prompt.txt + .preflight.json and runs preflight.py."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent
PF = H / "../../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(H.parent / "work/actmap_rows.json"))}
M = json.load(open(H / "media.json"))
def L(b): return re.sub(r'["“”]', "", rows[b]["line"])
B = "stryde-71-stairs-pixar-song__"
P0 = {"label": "P0-PROP-N plate (confirmed) — her hall and staircase", "kind": "location", "job": "377f63fd-7b11-4db2-a663-052e8c0637e8", "ref": B + "P0-PROP-N"}
P2 = {"label": "P2-KITCHEN plate v2 (confirmed)", "kind": "location", "job": "2484470e-dbda-4935-b1f2-0897e8418066", "ref": B + "P2-KITCHEN"}
R03B = "179dfe8a-7ef0-4b2e-8ebd-f8558f58a15f"; R06A = "37cf0d7a-06aa-4d40-ad45-821191a13086"
L_FR = {"label": "R-03b frame v1 A (confirmed) — Loretta's knee, skin, rolled khaki trouser and teal blouse (HT27)", "kind": "frame", "job": R03B, "ref": B + "R-03b"}
L_ST = {"label": "R-03b frame v1 A (confirmed) — the style: a stylized leg with the strap drawn right", "kind": "style", "job": R03B, "ref": B + "R-03b"}
N_CH = {"label": "R-06a frame v2 B (confirmed) — N in the day's rose-pink blouse (HT27)", "kind": "character", "job": R06A, "ref": B + "R-06a"}
N_FR = {"label": "R-06a frame v2 B (confirmed) — N's skin and day clothes (HT27)", "kind": "frame", "job": R06A, "ref": B + "R-06a"}
STH = {"label": "P-04a frame v3 (confirmed, hands on her table, no outfit in it) — the style", "kind": "style", "job": "e05783fd-e5e1-4e31-b247-3a8c950954b6", "ref": B + "P-04a"}
FRONT = {"label": "front.webp — the strap, front (product photo)", "kind": "product", "job": M["front"], "ref": "products/stryde/stryde_refs/front.webp"}
BACK = {"label": "back.webp — the strap, back (product photo)", "kind": "product", "job": M["back"], "ref": "products/stryde/stryde_refs/back.webp"}
WORN = {"label": "worn_front.jpg — the strap worn, front-on (product photo)", "kind": "product", "job": M["worn_front"], "ref": "products/stryde/stryde_refs/worn_front.jpg"}
TQ = {"label": "product_tq_left.jpg — the strap, three-quarter (product photo)", "kind": "product", "job": M["product_tq_left"], "ref": "products/stryde/stryde_refs/product_tq_left.jpg"}
KIT = "A final frame from a 3D animated feature film, stylized storybook render, soft morning window light."
HALL = "A final frame from a 3D animated feature film, stylized storybook render, warm afternoon sun from the door."
SPLIT = "The strap alone in real materials, in the same light."
SHAPE = "the strap of Image 1 copied exactly — a black shell, two pointed peaks round a notch, a chrome slide at each end —"
PLACE = "the kneecap's lower edge in its notch"
PLAIN = "No lettering, logos or labels but its wordmark."
TASTE = ["HT03", "HT04", "HT08", "HT12", "HT17", "HT21", "HT22", "HT25", "HT26", "HT27", "FP13", "FP14", "FP17"]
TASTE_P = TASTE + ["FP01", "FP02", "FP03", "FP05", "FP06", "FP07", "FP10", "FP11", "FP12"]
FIX = {"R-04a": 'user Fix "this should be loreta same clothes too" → her confirmed R-03b frame as Image 4 (skin, rolled khaki trouser, teal blouse), HT27',
       "R-05a": 'user Fix "product too small and wrong product" → product photos first with the shell\'s shape named, the strap half the frame wide, N from her confirmed R-06a frame (HT27)',
       "R-06b": 'user Fix "wrong product and this is not the pixar anymore" → the confirmed R-03b frame as the style (stylized leg, strap drawn right), the leg called smooth and simplified, N\'s skin and clothes from her R-06a frame',
       "R-07a": 'user Fix "wrong stairs" + R-07c "this should be part of the r07a so it should be one take only" → an image edit of the confirmed P0-PROP-N plate (her own staircase), N from her R-06a frame, one take for both lines'}
LINE7 = L("R-07a")  # the act map now carries both lines on R-07a (R-07c merged, one take)
P = {}
P["R-04a"] = (f'''For the line "{L("R-04a")}": A tall 9:16 frame. Image 1 is the strap, Image 2 its back, Image 3 it worn front-on. Image 4 is the visitor — her knee, deep brown skin, rolled khaki trouser leg and teal blouse exactly as in Image 4. Image 5 is the style.
Extreme close-up front-on at knee height, seated, the knee facing the lens, sharp on the strap: the visitor's bare right knee from Image 4, filling the frame, her khaki trouser leg rolled above it exactly as in Image 4; on it {SHAPE} 12 × 5 cm, the shell half the frame wide, {PLACE}, the wordmark level; her right fingertip taps the top of the shell, four chunky fingers and a thumb, the teal sleeve at the top edge. Scale true to the set: the shell's top edge is level with the kneecap's lower edge.
In frame: the knee, the strap, one hand; every other surface plain.
{KIT} {SPLIT} {PLAIN}''', [FRONT, BACK, WORN, L_FR, STH], False, True, False, True, None)
P["R-05a"] = (f'''For the line "{L("R-05a")}": At the table of Image 5, tall 9:16. Image 1 is the strap, Image 2 its back, Image 3 its three-quarter view. Image 4 is the woman — her face, twist-out and rose-pink blouse exactly as in Image 4. Image 6 is the style.
Close-up across the table at hand height, sharp on her palm: {SHAPE} 12 × 5 cm, front up, the wordmark level, lying across the open right palm of the same woman as Image 4, longer than her palm is wide, the shell half the frame wide, her thumb beside a chrome slide, four chunky fingers and a thumb; her face soft above, eyebrows raised, doubtful, lips closed, eyes on the strap. Scale true to the set: her hand fills the lower half of the frame.
In frame: her hand, the strap, her face, the lace cloth below; every other surface bare.
{KIT} {SPLIT} {PLAIN}''', [FRONT, BACK, TQ, N_CH, P2, STH], True, True, True, True, None)
P["R-06b"] = (f'''For the line "{L("R-06b")}": Kitchen of Image 5, tall 9:16. Image 1 is the strap, Image 2 its back, Image 3 its three-quarter view. Image 4 is the woman — her deep brown skin, rose-pink blouse and denim skirt exactly as in Image 4. Image 6 is the style — its leg and its strap.
Close-up from high three-quarter, her own view, sharp on the strap: her bare right shin and knee, the denim skirt hem just above the knee, both hands sliding {SHAPE} up the shin, its front to the lens, 12 × 5 cm, a third of the frame wide, its top edge reaching the kneecap's lower edge; four chunky fingers and a thumb on each; a tan slipper below. Her leg and hands smooth and simplified as in Image 6. Scale true to the set: the hem comes to her knee.
In frame: one leg, two hands, the strap, a chair edge, the floor; every other surface bare.
{KIT} {SPLIT} {PLAIN}''', [FRONT, BACK, TQ, N_FR, P2, L_ST], False, True, True, True, None)
P["R-07a"] = (f'''For the line "{LINE7}": Keep this photo exactly as it is — the staircase, its carpet runner and brass rods, balusters, oak rail, square newel and photo wall — same viewpoint, a tall 9:16 crop from the newel to the top step; add her. Image 1 is the hall. Image 2 is the strap, Image 3 its back. Image 4 is the woman: her face and pink blouse; a denim skirt. Image 5 is the style.
Full shot, sharp on her: the woman of Image 4 on the ninth step up, coming down three-quarter toward the lens, right foot onto the next step, hands loose off the rail, four chunky fingers and a thumb; on her bare right knee the strap of Image 2 copied exactly, 12 × 5 cm, {PLACE}; a proud closed-mouth smile, looking down at the next step. Scale: her head level with the lowest photo frame.
In frame: her, the flight; the rest as Image 1.
{HALL} {SPLIT} {PLAIN}''', [P0, FRONT, BACK, N_CH, STH], True, True, True, False, P0)
P7B = (f'''For the line "{LINE7}": Keep this photo exactly as it is — the staircase, runner, brass rods, balusters, rail, newel and photo wall — same viewpoint, a tall 9:16 crop from the newel to the top step; add her. Image 1 is the hall. Image 2 is the strap, Image 3 it worn. Image 4 is the woman: her face and pink blouse; a denim skirt. Image 5 is the style.
Full shot, sharp on her: the woman of Image 4 on the ninth step up, coming down toward the lens, right foot onto the next step, hands loose off the rail, four chunky fingers and a thumb, tan slippers; on her bare right knee the one strap of Image 3 copied exactly, 12 × 5 cm, below the kneecap, the kneecap bare; a proud closed-mouth smile, looking down at the next step. Scale: her head level with the lowest photo frame.
In frame: her, the flight; the rest as Image 1.
{HALL} {SPLIT} {PLAIN}''', [P0, FRONT, WORN, N_CH, STH], True, True, True, False, P0)
fails = 0
if "--r07a-v6" in sys.argv:
    P = {"R-07a": P7B}; VTAG = "v6"
else:
    VTAG = "v5"
for b, (pr, refs, face, body, room, prod, eo) in P.items():
    risk = "hand_product" if prod and b in ("R-04a", "R-06b") else ("stairs" if b == "R-07a" else None)
    c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": LINE7 if b == "R-07a" else L(b), "face": face, "room": room, "body": body,
         "refs": [{"label": r["label"], "kind": r["kind"]} for r in refs], "match": "plate" if eo else None, "edit_of": eo["job"] if eo else None, "taste": TASTE_P if prod or b == "R-07a" else TASTE,
         "anatomy": False, "anat_style": None, "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None, "fix_note": FIX[b] + (" · first v5 pair kept off (L16): A drew an open-kneecap sleeve with two shells → the worn photo as Image 3, one shell below the kneecap, the kneecap bare" if VTAG == "v6" else ""), "product": prod, "risk_class": risk,
         "medias": [r["job"] for r in refs], "board_refs": [{"label": r["label"], "kind": r["kind"], "ref": r["ref"], "role": f"Image {i + 1}"} for i, r in enumerate(refs)]}
    (H / f"{b}.{VTAG}.prompt.txt").write_text(pr); (H / f"{b}.{VTAG}.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.{VTAG}.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
