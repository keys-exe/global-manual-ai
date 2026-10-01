#!/usr/bin/env python3
"""§19 avatar-sheet prompts for stryde-71-stairs-pixar-song — Mode 2 (3D Pixar), assembled from Appendix A by ID.
Mode 2 adaptation of the §19 sheet (the master has a Mode 5 recipe, none for Mode 2): a render opening in place of
CAM-LOCK (no photographic language in Mode 2, §2), SHEET-GRID verbatim, AVATAR-SHEET's sameness / light / room clauses
with "photograph"/"phone" read as render/camera, PIX-SHAPE + PIX-EYES + PIX-LIGHT + CAP-ANIM (§24, §19 Mode 5 sheets),
negatives NEG-SHEET (without its two anti-render clauses) + NEG-GRID + NEG-PIX + NEG-DEFAULT-FACE. Recorded as F10."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

# Same people as the Mode 1 build stryde-71-stairs (the brief: "same Afro American Black Woman and entourage"), recast in Mode 2.
CAST = {
 # v2 (user 2026-10-01: "i want new ones and loretta should not be too thin they should be the same size as the narrator") — three new people,
 # Loretta at the narrator's build. v1 prompts are in cast/v1/.
 "N-NARR": dict(sex="WOMAN", side="left", wall="warm white", floor="a worn beige stair-landing carpet", heads="five and a half heads tall with a gently compressed, settled posture",
   shape="ROUND is her dominant shape: a round head, round full cheeks, rounded shoulders, a soft round middle and rounded hands — the silhouette a stack of soft circles. The one contrasting shape is her straight, level brows, a single horizontal line across all that roundness",
   face="An oval face with full cheeks and a long upper lip, wide-set dark-brown eyes with a warm, knowing look under straight level brows, a broad nose with a low flat bridge, and a full lower lip. Her charm marker: ONE small raised dark mole beside the LEFT side of her nose, at the crease of the nostril — on the left side only, the right side of her face plain. Her left eye sits a touch lower than the right",
   hair="Natural hair in a short silver-grey twist-out, mostly silver with a little black at the nape, close at the sides and a little fuller on top — the same silver and the same height in every panel",
   body="A Black American grandmother from the South, deep brown skin, seventy-one years old. Medium height, soft and full through the hips and middle, rounded shoulders, sturdy calves",
   ward="A mustard-yellow short-sleeved cotton blouse with a small round collar, a mid-blue denim A-line skirt ending a hand above the knee so both knees are bare, and plain white slip-on canvas shoes",
   age="deep laugh folds from the nose to the mouth, fine creases fanning from the outer eyes, a softening jawline and neck, a few small dark spots on the temples — all stylized, drawn as shape, never as pores"),
 "C1-LORETTA": dict(sex="WOMAN", side="right", wall="pale butter-yellow", floor="honey oak floorboards", heads="five and a half heads tall with a gently compressed, settled posture",
   shape="SQUARE is her dominant shape: a broad square head with a strong square jaw, broad square shoulders and a solid, full, boxy torso — the silhouette a wide, full rectangle. The one contrasting shape is her rounded silver bob, a single soft circle on top of all those straight lines",
   face="A broad square face with a strong chin, soft full cheeks, hooded dark eyes under thick arched brows, a short wide nose, and a wide mouth with deep smile lines bracketing it. Her charm marker: ONE raised dark beauty mark just above the RIGHT corner of her upper lip — on the right side only, the left side of her face plain. Her right eyebrow sits a touch higher than the left",
   hair="A short silver-grey pressed bob, chin length, tucked behind the ears, with a soft side part — the same silver and the same length in every panel",
   body="A Black American woman from the South, medium-brown skin with warm undertones, seventy-four years old. THE SAME SIZE AS THE NARRATOR: medium height, soft and full through the hips and middle, rounded full shoulders, sturdy arms and calves — never thin, never lean, never tall and willowy",
   ward="A teal three-quarter-sleeve blouse, loose khaki cotton shorts ending above the knee so both knees are bare, and white canvas slip-on sneakers",
   age="deep smile lines from the nose to the mouth, fine lines across the forehead, a soft double chin, a scatter of dark spots along the cheekbones — all stylized, drawn as shape, never as pores"),
 "C2-DAUGHTER": dict(sex="WOMAN", side="left", wall="soft grey", floor="a worn beige stair-landing carpet", heads="six heads tall",
   shape="TRIANGULAR is her dominant shape: a heart-shaped face wide at the cheekbones narrowing to a pointed chin, broad shoulders tapering to the waist, long tapering limbs — the silhouette an inverted triangle. The one contrasting shape is her round afro puff, a single circle on top of the points",
   face="A heart-shaped face with high cheekbones, almond-shaped dark-brown eyes, softly arched brows, a slim straight nose and a small pointed chin, full lips. Her charm marker: ONE small dark mole under her LEFT eye, high on the cheekbone — on the left side only, the right cheek plain. The right corner of her mouth lifts a touch higher than the left",
   hair="Natural dark-brown curly hair gathered up into one high round afro puff on the crown, the edges smoothed back, the same size and height in every panel",
   body="A Black American woman, medium-deep brown skin, forty-six years old. Medium height, athletic and broad-shouldered, strong calves",
   ward="An olive-green crewneck sweatshirt, black denim shorts ending above the knee so both knees are bare, and white trainers",
   age="fine lines at the eye corners, a faint crease between the brows — all stylized, drawn as shape, never as pores"),
}

def build(k, c):
    opening = (f"A character reference sheet from a finished 3D animated feature film: FIVE RENDERS OF THE SAME ONE {c['sex']}, "
               "tiled edge to edge on a single tall 9:16 canvas with thin seams between them, all rendered within the same minute in the same spare room "
               "from a virtual camera standing where the door is, at standing eye level, deep focus, nothing stylized about the camera itself. "
               "A final render from the film — not concept art, not a storyboard, not a game and not a toy. NO WRITING ANYWHERE ON THE CANVAS: no panel titles, no captions, no labels, no text of any kind.")
    sheet = S("AVATAR-SHEET")
    first, rest = sheet.split(". ", 1)                      # drop AVATAR-SHEET's opening sentence (the Mode 1 photograph framing) → the render opening above
    body = rest.replace("facing the phone", "facing the camera").replace("TOP ROW, three equal panels", "TOP ROW, three equal panels")
    for a, b in [("[FACE — architecture in three or four plain sentences, the one marker, the asymmetries]", c["face"]),
                 ("[HAIR — colour, roots, how worn, the same tone and the same height in every panel]", c["hair"]),
                 ("[BODY — build, height impression]", c["body"] + ", drawn " + c["heads"] + " (§24A elder/adult proportion)"),
                 ("[WARDROBE — BASE, LOWER, FOOT]", c["ward"]),
                 ("[SIDE]", c["side"]), ("[WALL COLOUR]", c["wall"]), ("[FLOOR]", c["floor"])]:
        body = body.replace(a, b)
    assert "[" not in body, k
    pix = ("SHAPE LANGUAGE. " + c["shape"] + ". " + S("PIX-SHAPE") + " "
           "The face is stylized the Pixar way — larger emotive eyes, a softened rounded facial structure, appealing exaggeration — "
           "and it is unmistakably an older Black American woman, her age carried in shape: " + c["age"] + ".")
    eyes = "EYES. " + S("PIX-EYES")
    light = ("LIGHT. " + S("PIX-LIGHT") + " Here the key IS the one window to the " + c["side"] + " described above (warm daylight), "
             "the fill a cool quarter-strength bounce off the far wall, the rim a thin pale edge separating her from the wall — the same three sources, "
             "the same side, in all five panels.")
    cap = "RENDER. " + S("CAP-ANIM") + " The skin is stylized animation skin: smooth subsurface warmth, no pores, no photographic texture."
    ns = S("NEG-SHEET").replace(", no 3D render, no CGI", "")   # Mode 2 adaptation: the sheet IS a render
    neg = ", ".join([ns, S("NEG-GRID"), S("NEG-PIX"), S("NEG-DEFAULT-FACE"), "no live-action photograph, no photoreal human, no phone photo look, no panel titles, no words on the canvas, no matching marks on both sides of the face, no second mole, no freckle scatter"])
    return "\n\n".join([opening, "THE SHEET. " + S("SHEET-GRID"), body, pix, eyes, light, cap, "AVOID: " + neg + "."])

out = {}
for k, c in CAST.items():
    p = build(k, c); out[k] = p
    pathlib.Path(__file__).parent.joinpath(f"{k}.v2.prompt.txt").write_text(p)
    print(k, len(p))
json.dump(out, open(pathlib.Path(__file__).parent / "prompts.v2.json", "w"), indent=1)
