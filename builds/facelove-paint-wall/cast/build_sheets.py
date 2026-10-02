#!/usr/bin/env python3
"""§19 Mode 1 avatar-sheet prompts for facelove-paint-wall, assembled from Appendix A by ID (never retyped).
Mode 1 sheet (§19): CAM-LOCK + AVATAR-SHEET (SHEET-GRID pasted after its first sentence) + SKIN-T in the close-up + CAP-SHARP + CAP-FILE;
negatives NEG-SHEET + NEG-GRID + NEG-FILE (NEG-DEFAULT-FACE dropped: the face is the client's, copied).
Supplied face (§7, authority layer 1): the client's avatar.png is attached as Image 1 and its face copied exactly (flag F1)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

FACE_REF = ("Image 1 is this woman's face. Copy the face in Image 1 exactly in every panel — the same face shape, eyes, brows, nose, "
            "mouth, jaw, hairline and hair colour, the same age; nothing redesigned, nothing made younger. "
            "Take only the face, its bone structure and the hair from Image 1, never its makeup, lashes, lip gloss, light or background.")

FACE = ("A long oval face with high cheekbones and a firm, defined jaw tapering to a softly rounded chin, light grey-green almond eyes under full, softly arched brown brows, "
        "a straight narrow nose with a softly rounded tip, and full lips with a defined bow. Her one marker: a faint scatter of sun freckles across the upper chest and the bridge of the nose. "
        "The left brow arches a touch higher than the right")
HAIR = ("Mid-brown hair to just below the shoulders, cut in soft long layers, with warm caramel-blonde highlights through the lengths and a little silver showing at the roots along the parting, "
        "worn loose and straight with a soft side parting, the front falling forward over the left side of her face, the same tone and the same length in every panel")
BODY = "A white American woman with light warm-beige skin. Medium height, slim and toned, fifty-seven years old"
WARD = ("An oatmeal textured-linen single-breasted blazer worn open over a white ribbed scoop-neck tank, cream wide-leg tailored trousers and nude leather block-heel mules")
AGE = ("deep crow's feet fanning in three or four creases from each outer eye, three horizontal lines across the forehead, "
       "two vertical frown lines between the brows, deep folds from the nose to the mouth, fine lines running down from the mouth corners, "
       "fine vertical lines on the upper lip, crepe and fine lines under the eyes with deep brownish-violet dark circles, "
       "dull, uneven, slightly sallow skin with a few faint brown sun spots on the cheekbones, two faint horizontal lines across the neck")

CAST = {
 "N-BEFORE": dict(title="The narrator — bare tired face, before (Scene 2 mirror look, the caking macros)", after=False, age=AGE,
                  wrinkles="Her face shows its fifty-seven years plainly and looks tired: deep crow's feet, forehead lines, frown lines, deep folds from the nose to the mouth and deep dark circles, visible in every panel and deepest in the close-up."),
 "N-AFTER": dict(title="The narrator — the stick blended in, every line kept (presenter scenes, after, CTA)", after=True),
}

def build(k, c):
    face, hair, body, ward = c.get("face", FACE), c.get("hair", HAIR), c.get("body", BODY), c.get("ward", WARD)
    sheet = S("AVATAR-SHEET")
    first, rest = sheet.split(". ", 1)
    sheet = first + ". " + S("SHEET-GRID") + " " + rest
    for a, b in [("[WOMAN/MAN]", "WOMAN"), ("[FACE — architecture in three or four plain sentences, the one marker, the asymmetries]", face),
                 ("[HAIR — colour, roots, how worn, the same tone and the same height in every panel]", hair),
                 ("[BODY — build, height impression]", body), ("[WARDROBE — BASE, LOWER, FOOT]", ward),
                 ("[SIDE]", c.get("side", "left")), ("[WALL COLOUR]", c.get("wall", "pale warm grey")), ("[FLOOR]", c.get("floor", "worn oak floorboards"))]:
        sheet = sheet.replace(a, b)
    neg_sheet = S("NEG-SHEET").replace("no skin patches, ", "")   # the brown patches and redness are the script's problem — wanted
    if c["after"]:   # the after look IS the product on her face: an even, natural foundation finish, terrain unchanged (cover, not erase)
        sheet = sheet.replace("Bare face, no makeup, in every panel including the close-up.",
            "In every panel including the close-up she wears one thin, even layer of a natural foundation exactly matched to her light warm-beige skin and nothing else — no eye makeup, no lipstick: the dullness, the dark circles and the sun spots are evened out, every line and crease is still there, the skin still reads as skin.")
        neg_sheet = neg_sheet.replace("no makeup, ", "no heavy makeup, no eye makeup, no lipstick colour, no contour, no glowing skin, ")
        skin = ("IN THE FACE CLOSE-UP: real mature skin under a thin, even foundation exactly matched to her light warm-beige skin — the tone even, the dark circles and the sun spots covered, "
                "pores still visible on the nose and cheeks, the fine crow's feet, the forehead lines and the folds from the nose to the mouth still there and still visible, "
                "the foundation lying evenly across the lines and not sitting in them; the neck the same tone as the face; no smoothing, no blur, no airbrushed finish.")
    else:
        skin = "IN THE FACE CLOSE-UP: " + S("SKIN-T").replace("[AGE-FEATURES]", c.get("age", AGE))
        if c.get("young"):   # SKIN-T is written for mature skin; a woman under 35 keeps its texture without the deep creases
            skin = skin.replace("three deep horizontal creases and a fine crosshatch of smaller ones", "two faint horizontal lines").replace("Neck looser and more creped than the face. ", "")
        if c.get("wrinkles"):
            sheet = sheet.replace("Bare face, no makeup, in every panel including the close-up.", "Bare face, no makeup, in every panel including the close-up. " + c["wrinkles"])
    assert "[" not in sheet, k
    neg = ", ".join([neg_sheet, S("NEG-GRID"), S("NEG-FILE")] + ([] if c.get("ref", True) else [S("NEG-DEFAULT-FACE")]))
    head = [FACE_REF] if c.get("ref", True) else []
    return "\n\n".join(head + [S("CAM-LOCK"), sheet, skin, S("CAP-SHARP"), S("CAP-FILE"), "AVOID: " + neg + "."])

if __name__ == "__main__":
    out = {}
    import sys
    only = sys.argv[1:] or list(CAST)
    for k, c in CAST.items():
        if k not in only: continue
        p = build(k, c); out[k] = {"prompt": p, "title": c["title"]}
        (pathlib.Path(__file__).parent / f"{k}.prompt.txt").write_text(p)
        print(k, len(p))
    json.dump(out, open(pathlib.Path(__file__).parent / "prompts.json", "w"), indent=1, ensure_ascii=False)
