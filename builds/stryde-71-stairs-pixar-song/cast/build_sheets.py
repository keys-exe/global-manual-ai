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
 "N-NARR": dict(sex="WOMAN", side="left", wall="warm white", floor="a worn beige stair-landing carpet", heads="five and a half heads tall with a gently compressed, settled posture",
   shape="ROUND is her dominant shape: a round head, round cheeks, rounded shoulders and a soft round middle, rounded hands — the silhouette a stack of soft circles. The one contrasting shape is her small pointed chin, a single triangle under all that roundness",
   face="A wide, soft face with full round cheeks, big heavy-lidded dark-brown eyes with a warm, knowing look, a short broad nose with a rounded tip, full lips with a deeper upper lip, and deep laugh folds set at the corners of the eyes and mouth. Her charm marker: a cluster of three small raised dark spots high on her LEFT cheekbone, just under the outer corner of the eye, on the left side only. The right eyebrow arches a touch higher than the left",
   hair="Natural hair, mostly silver-grey with a little black left at the nape, in a short rounded tapered cut, close at the sides and fuller on top — the same grey and the same height in every panel",
   body="A Black American grandmother from the South, deep brown skin, seventy-one years old. Medium height, soft and full through the hips and middle, sturdy calves",
   ward="A coral short-sleeved knit top under an open cream cotton cardigan, a navy A-line skirt ending a hand above the knee so both knees are bare, and plain black flat slip-on shoes",
   age="deep laugh folds from the nose to the mouth, fine creases fanning from the outer eyes, a softening jawline and neck, a few small dark spots on the cheeks and temples — all stylized, drawn as shape, never as pores"),
 "C1-LORETTA": dict(sex="WOMAN", side="right", wall="pale butter-yellow", floor="honey oak floorboards", heads="six heads tall, straight-backed",
   shape="SQUARE is her dominant shape: a long rectangular head with a square chin, square shoulders, a straight upright torso and long straight limbs — the silhouette a tall narrow rectangle. The one contrasting shape is her round silver crop of hair, a single circle on top of all those straight lines",
   face="A long oval face with high sharp cheekbones, bright wide-open dark eyes under thin arched brows, a long nose with a slight hook at the bridge, a wide mouth that sits a little crooked, lifting higher on the right, and a strong square chin. Her charm marker: a thin pale scar cutting straight down through the middle of her RIGHT eyebrow. The left eye sits slightly lower than the right",
   hair="A short silver-white natural curly crop, tight coils close to the head — the same silver and the same height in every panel",
   body="A Black American woman from the South, medium-brown skin with warm undertones, seventy-four years old. Tall and lean, straight-backed, long arms and legs",
   ward="A plum-coloured blouse with a small collar and the sleeves rolled, loose khaki cotton shorts ending above the knee so both knees are bare, and white canvas slip-on sneakers",
   age="long vertical creases on the cheeks, fine lines across the forehead, a scatter of dark spots along the cheekbones, thin crepey skin suggested on the neck and the backs of the hands — all stylized, drawn as shape, never as pores"),
 "C2-DAUGHTER": dict(sex="WOMAN", side="left", wall="soft grey", floor="a worn beige stair-landing carpet", heads="six heads tall",
   shape="ROUND is her dominant shape: a round face with full round cheeks, a rounded jaw, broad rounded shoulders and a solid rounded build — the silhouette a sturdy oval. The one contrasting shape is the long straight lines of her box braids gathered in a ponytail, a single set of straight lines against the roundness",
   face="A round face with full cheeks, deep-set dark-brown eyes, thick straight brows, a broad nose and full lips, a softly rounded jaw. Her charm marker: a small crescent-shaped scar on her chin, left of centre. The left corner of her mouth sits a touch lower than the right",
   hair="Shoulder-length natural hair in medium box braids, dark brown, gathered loosely back at the nape in a low ponytail — the same length in every panel",
   body="A Black American woman, medium-deep brown skin, forty-six years old. Medium height, sturdy and broad-shouldered",
   ward="A heather-grey crewneck sweatshirt, dark blue denim shorts ending above the knee so both knees are bare, and white trainers",
   age="fine lines at the eye corners, a faint crease between the brows, a few small dark spots under the eyes — all stylized, drawn as shape, never as pores"),
}

def build(k, c):
    opening = (f"A character reference sheet from a finished 3D animated feature film: FIVE RENDERS OF THE SAME ONE {c['sex']}, "
               "tiled edge to edge on a single tall 9:16 canvas with thin seams between them, all rendered within the same minute in the same spare room "
               "from a virtual camera standing where the door is, at standing eye level, deep focus, nothing stylized about the camera itself. "
               "A final render from the film — not concept art, not a storyboard, not a game and not a toy.")
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
    neg = ", ".join([ns, S("NEG-GRID"), S("NEG-PIX"), S("NEG-DEFAULT-FACE"), "no live-action photograph, no photoreal human, no phone photo look"])
    return "\n\n".join([opening, "THE SHEET. " + S("SHEET-GRID"), body, pix, eyes, light, cap, "AVOID: " + neg + "."])

out = {}
for k, c in CAST.items():
    p = build(k, c); out[k] = p
    pathlib.Path(__file__).parent.joinpath(f"{k}.prompt.txt").write_text(p)
    print(k, len(p))
json.dump(out, open(pathlib.Path(__file__).parent / "prompts.json", "w"), indent=1)
