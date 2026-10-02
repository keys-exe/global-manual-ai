#!/usr/bin/env python3
"""§19 Mode 4 avatar-sheet prompts for facelove-my-mother, assembled from Appendix A by ID (never retyped).
Mode 4 sheet (§19): CAM-FILM (tripod, portrait focal) + AVATAR-SHEET/SHEET-GRID + SKIN-T + LOOK-MYMOTHER + CAP-FILM;
negatives NEG-SHEET + NEG-GRID + NEG-FILM (lens clause dropped: the sheet's close-up looks at the lens) + NEG-DEFAULT-FACE.
Supplied faces (§7, authority layer 1): the client's cast picture is attached as Image 1 and its face is copied exactly
(flag F1 in BUILD_SHEET.md: §19 normally attaches nothing; the advertiser's own cast pictures outrank it)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

# Film Look Sheet fields 1, 4, 6 (BUILD_SHEET.md §1b) — pasted verbatim, never reworded
LOOK = S("LOOK-PATTERN").replace("[GENRE AND REFERENCE, one plain sentence]",
  "An American suburban family drama shot like a prestige streaming series — a backyard anniversary party under string lights, a quiet two-storey family house and a bedroom vanity, watched with warmth and restraint").replace(
  "[PALETTE: the dominant colours of the sets and wardrobe]",
  "Honey and amber golden-hour light and warm string-light bulbs at the party; cool blue-grey dusk and lamplit tungsten in the house of the Before; soft warm window daylight at the vanity; dusty blue, cream, sage, oatmeal and wine in the sets and clothes").replace(
  "[OPTICAL TEXTURE: highlight roll-off, halation, lens softness]",
  "Highlights roll off softly with a faint warm halation around bulbs and bright windows; clean modern glass with a gentle fall-off toward the frame edges")
CAM = (S("CAM-FILM").replace("[CAMERA AND FORMAT]", "an ARRI Alexa Mini LF in large format")
       .replace("[LENS FAMILY]", "an ARRI Signature Prime").replace("[FOCAL]", "50").replace("[STOP]", "T4")
       .replace("[COLOUR SCIENCE]", "ARRI").replace("[RIG]", "a locked tripod at standing eye height"))
CAPF = S("CAP-FILM").replace("[HIGHLIGHT BEHAVIOUR]", "rolling off softly into white with a faint warm halation around bulbs and bright windows, never clipping to a hard edge")
NEGF = S("NEG-FILM").replace(", no actor looking into the lens", "")

FACE_REF = ("Image 1 is this {who}'s face. Copy the face in Image 1 exactly in every panel — the same face shape, eyes, brows, nose, "
            "mouth, jaw, hairline and every line and mark of the skin, the same age; nothing redesigned, nothing made younger or prettier. "
            "Take only the face and hair from Image 1, never its clothes, jewellery, light or background.")

CAST = {
 "N-SUSAN": dict(ref="SUSAN_OLD.png", who="woman", sex="WOMAN", side="left", wall="pale warm grey", floor="worn oak floorboards",
   face="A long oval face with high flat cheekbones, hazel-green eyes under slightly heavy lids, straight brows, a long straight nose and a thin mouth whose corners turn down. A few small freckles across the nose and upper chest — her one marker. The right eyebrow sits a touch higher than the left",
   hair="Shoulder-length layered honey-brown hair with blonde streaks and grey at the roots and temples, worn loose and a little limp with a side parting, the same tone and the same length in every panel",
   body="A white American woman. Medium height, slim, slightly rounded shoulders, forty-nine years old",
   ward="A dusty-blue loose chiffon blouse with a soft V neck, cream straight linen trousers and nude leather flat shoes",
   age="deep horizontal forehead lines, vertical frown lines between the brows, crow's feet, soft crepe and grey shadows under the eyes, deep folds from the nose to the mouth, small lines from the mouth corners down to the chin"),
 "N-SUSAN-AFTER": dict(ref="SUSAN_NEW.png", who="woman", sex="WOMAN", side="left", wall="pale warm grey", floor="worn oak floorboards", after=True,
   face="The same long oval face with high flat cheekbones, hazel-green eyes, straight brows, a long straight nose and a thin mouth, now relaxed. A few small freckles across the nose and upper chest — her one marker. The right eyebrow sits a touch higher than the left",
   hair="Shoulder-length layered honey-brown hair with blonde streaks and grey at the roots, now washed and styled in soft loose waves with body at the crown and a side parting, the same tone and the same length in every panel",
   body="A white American woman. Medium height, slim, standing taller, shoulders back, forty-nine years old",
   ward="A wine-red satin sleeveless top with a draped neckline, slim black ankle trousers and black low-heeled leather pumps",
   age="the same forehead lines, crow's feet and folds from the nose to the mouth, still there and still visible"),
 "C1-GREG": dict(ref="GREG.png", who="man", sex="MAN", side="right", wall="pale blue-grey", floor="dark stained floorboards",
   face="A long rectangular face with a strong square jaw, deep-set blue-grey eyes under straight brows, a straight nose and a wide mouth with thin lips. A deep crease down each cheek when the face is still — his one marker. The left side of his mouth sits a touch higher than the right",
   hair="Thick salt-and-pepper hair, darker on top and grey at the sides, combed back and to the side from the forehead, the same in every panel",
   body="A white American man. Tall, broad-shouldered, a little thick at the waist, fifty-two years old, a tanned outdoor complexion",
   ward="A navy textured linen-wool blazer over a pale blue open-collar cotton shirt, khaki chinos and brown leather loafers",
   age="deep crow's feet fanning from the outer eyes, heavy lines across the forehead, folds from the nose to the mouth, weathered sun-damaged skin on the cheeks and nose"),
 "C2-PAULA": dict(ref="PAULA.png", who="woman", sex="WOMAN", side="right", wall="warm cream", floor="light oak floorboards",
   face="An oval face with high cheekbones, warm brown almond eyes, softly arched dark brows, a straight nose and a full mouth. A smooth, unlined forehead and smooth skin between the brows against the lines elsewhere on her face — her one marker. The left eye sits a touch lower than the right",
   hair="Chin-length wavy chestnut-brown bob with a streak of grey at the left temple, worn with a side parting, the same tone and the same length in every panel",
   body="A white American woman of Italian heritage. Medium height, slim, upright, forty-nine years old, olive skin",
   ward="A plum satin sleeveless top with a cowl neck, slim charcoal trousers and black leather mules",
   age="fine crow's feet, soft folds from the nose to the mouth, faint lines on the neck, the forehead smooth"),
 "C3-BETH": dict(ref="BETH.png", who="woman", sex="WOMAN", side="left", wall="soft sage", floor="pale ash floorboards",
   face="A long oval face with a long straight nose, bright blue eyes, straight light-brown brows, a wide mouth and a pointed chin. A light dusting of freckles across the cheekbones and nose — her one marker. The right corner of her mouth lifts a touch higher than the left",
   hair="Straight shoulder-length honey-brown hair with fine blonde highlights, centre-parted, falling smooth to the collarbones, the same tone and the same length in every panel",
   body="A white American woman. Tall, slim, long-limbed, easy upright posture, forty-nine years old",
   ward="An emerald-green satin square-neck top with short puffed sleeves, straight dark indigo jeans and tan leather ballet flats",
   age="fine crow's feet, soft lines from the nose to the mouth, faint lines across the forehead"),
 "C4-DAUGHTER": dict(sex="WOMAN", side="right", wall="pale grey", floor="grey carpet",
   face="An oval face with her mother's long straight nose, hazel-green eyes, thick straight dark-blonde brows, a full lower lip and a small rounded chin. A small dark mole just below the right corner of her mouth — her one marker. The left eye is a touch narrower than the right",
   hair="Long dark-blonde hair, darker at the roots, worn loose past the shoulders with a centre parting, the same tone and the same length in every panel",
   body="A white American woman. Medium height, slim, athletic shoulders, twenty-six years old",
   ward="A cream ribbed knit cardigan over a white cotton T-shirt, light-wash straight jeans and white canvas trainers",
   age="smooth young skin with faint freckles across the nose, a few fine lines at the outer eyes when she squints"),
 "C5-FRIEND-A": dict(sex="WOMAN", side="left", wall="light warm beige", floor="honey-coloured floorboards",
   face="A round face with full cheeks, small dark brown eyes behind no glasses, thick dark brows, a broad short nose and a wide mouth with full lips. A small raised mole on her left cheek beside the nose — her one marker. The right cheek is a touch fuller than the left",
   hair="Short dark brown hair with grey at the temples, cut in a chin-length layered bob tucked behind the ears, the same tone and the same length in every panel",
   body="A Black American woman. Short and full-figured, round shoulders, fifty-one years old",
   ward="A mustard-yellow linen wrap dress to the knee and tan leather sandals",
   age="soft folds from the nose to the mouth, fine lines at the outer eyes, slight hollows under the eyes, a scatter of small dark raised spots on the cheeks"),
 "C6-FRIEND-B": dict(sex="WOMAN", side="right", wall="pale blue", floor="light grey floorboards",
   face="A narrow heart-shaped face with a pointed chin, pale grey eyes set close under thin arched brows, a small upturned nose and a thin mouth. A pale thin scar through the outer end of her left eyebrow — her one marker. The left corner of her mouth sits a touch lower than the right",
   hair="Platinum-blonde hair cut in a sleek straight bob to the jaw, darker at the roots, the same tone and the same length in every panel",
   body="A white American woman. Tall and thin, narrow shoulders, long neck, fifty years old",
   ward="A pale pink silk shirt with long sleeves, white wide-leg linen trousers and nude strappy heeled sandals",
   age="fine vertical lines on the upper lip, crow's feet, crepe under the eyes, a thin sagging line along the jaw"),
}

def build(k, c):
    sheet = S("AVATAR-SHEET").replace("facing the phone", "facing the camera")
    first, rest = sheet.split(". ", 1)          # SHEET-GRID pasted after the opening sheet sentence
    sheet = first + ". " + S("SHEET-GRID") + " " + rest
    for a, b in [("[WOMAN/MAN]", c["sex"]), ("[FACE — architecture in three or four plain sentences, the one marker, the asymmetries]", c["face"]),
                 ("[HAIR — colour, roots, how worn, the same tone and the same height in every panel]", c["hair"]),
                 ("[BODY — build, height impression]", c["body"]), ("[WARDROBE — BASE, LOWER, FOOT]", c["ward"]),
                 ("[SIDE]", c["side"]), ("[WALL COLOUR]", c["wall"]), ("[FLOOR]", c["floor"])]:
        sheet = sheet.replace(a, b)
    neg_sheet = S("NEG-SHEET")
    if c.get("after"):   # the after look IS the product on her face: an even, natural foundation finish, terrain unchanged (cover, not erase)
        sheet = sheet.replace("Bare face, no makeup, in every panel including the close-up.",
            "In every panel including the close-up she wears a light, natural foundation that evens out her skin tone and takes down redness, and nothing else but a little mascara; every line and crease of her face is still there, the skin still reads as skin.")
        neg_sheet = neg_sheet.replace("no makeup, ", "no heavy makeup, no lipstick colour, no contour, ")
        skin = ("IN THE FACE CLOSE-UP: real mature skin under a thin even foundation — the tone even, redness gone, pores still visible on the nose and cheeks, "
                + c["age"] + ", the fine lines on the upper lip still there, the neck looser than the face; the film lies evenly across the lines and does not sit in them; no smoothing, no blur, no airbrushed finish.")
    else:
        skin = "IN THE FACE CLOSE-UP: " + S("SKIN-T").replace("[AGE-FEATURES]", c["age"])
    assert "[" not in sheet, k
    neg = ", ".join([neg_sheet, S("NEG-GRID"), NEGF] + ([] if c.get("ref") else [S("NEG-DEFAULT-FACE")]))
    parts = [CAM, sheet, skin, LOOK, CAPF, "AVOID: " + neg + "."]
    if c.get("ref"):
        parts.insert(0, FACE_REF.format(who=c["who"]))
    return "\n\n".join(parts)

if __name__ == "__main__":
    out = {}
    for k, c in CAST.items():
        p = build(k, c); out[k] = {"prompt": p, "ref": c.get("ref")}
        (pathlib.Path(__file__).parent / f"{k}.prompt.txt").write_text(p)
        print(k, len(p), c.get("ref"))
    json.dump(out, open(pathlib.Path(__file__).parent / "prompts.json", "w"), indent=1)
    (pathlib.Path(__file__).parent / "LOOK.txt").write_text(LOOK)
