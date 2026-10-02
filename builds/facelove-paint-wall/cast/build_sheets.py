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

# Fix round 1 (user's board Fix on N-BEFORE v1, 2026-10-02, owner-marked: "FIX THE IMAGE, MAKE MORE OLD LOOKING, MAKE THE DARK CIRCLE VISIBLE,
# PUT SOME WRINGKLES AND DULL TIRED SKIN"). Cause: FACE_REF kept Image 1's age ("the same age… nothing made younger") and the avatar is a
# glossy, made-up photo that reads younger, so v1 copied its youth; SKIN-T's greasy forehead added shine against "dull".
FACE_REF_OLDER = ("Image 1 is this woman's face. Copy only its bone structure in every panel — the same face shape, eye shape and colour, brows, nose, "
            "mouth, jaw, hairline and hair colour — so she is plainly the same woman. She is older and more tired than in Image 1: "
            "fifty-seven, bare-faced, after years of poor sleep, her skin aged well past the photo. "
            "Take nothing else from Image 1 — never its smooth skin, its glow, its makeup, lashes, lip gloss, light or background.")
AGE_V2 = ("clearly visible deep brownish-purple dark circles under both eyes, dark enough to read from across the room, with puffy under-eye bags and hollows below them, "
          "deep crow's feet fanning in four or five creases from each outer eye, four deep horizontal lines across the forehead, "
          "two deep vertical frown lines between the brows, deep folds from the nose to the mouth, marionette lines running down from the mouth corners to the chin, "
          "fine vertical lines on the upper lip and thinner lips, crepe and fine lines under the eyes, slightly hooded upper lids, a softening jawline with slight jowls, "
          "a crepey neck with three horizontal lines, dull, flat, greyish-sallow skin with no glow anywhere, uneven tone and a few faint brown sun spots on the cheekbones")

CAST = {
 "N-BEFORE": dict(title="The narrator — bare tired face, before (Scene 2 mirror look, the caking macros)", after=False, age=AGE_V2, older=True,
                  wrinkles="She looks every one of her fifty-seven years and exhausted: dark circles clearly visible under both eyes, deep crow's feet, forehead lines, frown lines, deep folds from the nose to the mouth and marionette lines, dull grey-sallow skin with no glow — visible even in the full-length panels and deepest in the close-up."),
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
    if c.get("older"):   # Fix round 1: dull, not oily — SKIN-T's greasy forehead sheen taken out
        skin = skin.replace("greasy, and the light on it does not make one smooth sheen: the sebum highlight is broken into hundreds of separate pinpoint glints with dark pits between them", "dry and dull, matte with no sheen")
    if c.get("older"): neg = neg.replace("no wet skin, ", "no wet skin, no glowing skin, no dewy skin, no smooth young skin, ")
    head = ([FACE_REF_OLDER] if c.get("older") else [FACE_REF]) if c.get("ref", True) else []
    return "\n\n".join(head + [S("CAM-LOCK"), sheet, skin, S("CAP-SHARP"), S("CAP-FILE"), "AVOID: " + neg + "."])

if __name__ == "__main__":
    out = {}
    import sys
    only = [a for a in sys.argv[1:] if not a.startswith("--")] or list(CAST)
    for k, c in CAST.items():
        if k not in only: continue
        p = build(k, c); out[k] = {"prompt": p, "title": c["title"]}
        (pathlib.Path(__file__).parent / f"{k}.prompt.txt").write_text(p)
        print(k, len(p))
    json.dump(out, open(pathlib.Path(__file__).parent / "prompts.json", "w"), indent=1, ensure_ascii=False)

# Fix round 2 (user's board Fix on N-BEFORE v2, 2026-10-02, owner-marked: "MAKE THE DARK CIRCLE AROUND THE EYES VISIBLE").
# Cause: the dark circles were one item mid-list in AGE_V2 and the bright 45-degree window + Smart HDR lifted the under-eye shadow.
# v2 is otherwise as asked, so v3 is an image edit of v2 (§6A rule 3) changing only the eye area, the circles named as a colour band.
EDIT_DARK_CIRCLES = (
 "Image 1 is a character sheet of one woman. Keep this picture exactly as it is — the same five panels, the same face, hair, wrinkles, "
 "skin texture, clothes, pose, light, wall and floor, nothing moved, nothing redrawn — and change only the skin around her eyes, in every panel where her face shows. "
 "Add clearly visible dark circles around both eyes: a deep brownish-plum band under each eye from the inner corner to the outer corner, "
 "plainly darker than her cheek, a grey-violet shadow in the inner corners beside the nose and a faint brownish darkening on the upper lids, "
 "with puffy bags and a hollow below the lower lids. The window light does not wash the dark circles out: they read even on the lit side of the face, "
 "strongest in the face close-up, and are clearly visible in the front view. Bare skin, no makeup — the darkness is her own skin, never eyeshadow or a bruise. "
 "No other change anywhere: no younger face, no smoothing, no new lines removed, no change of expression, no change of colour elsewhere.")
if __name__ == "__main__" and "--edit-v3" in __import__("sys").argv:
    (pathlib.Path(__file__).parent / "N-BEFORE.v3.edit.prompt.txt").write_text(EDIT_DARK_CIRCLES); print(len(EDIT_DARK_CIRCLES))

# Fix round 3 (user's board Fix on N-BEFORE v3, 2026-10-02, owner-marked: "PUT WRINGKLES"). v3's dark circles read; its lines were still
# fine and shallow (they were described, never made deep enough to carry a shadow). v4 is an image edit of v3 changing only the creases.
EDIT_WRINKLES = (
 "Image 1 is a character sheet of one woman. Keep this picture exactly as it is — the same five panels, the same face, the same dark circles under her eyes, "
 "hair, clothes, pose, light, wall and floor, nothing moved, nothing redrawn — and change only the lines in her skin, in every panel where her face or neck shows. "
 "Make her wrinkles deep and plainly visible, each one a real crease with a dark shadow inside it: four deep furrows across the forehead, "
 "two deep vertical frown lines between the brows, crow's feet cut in four or five deep creases from each outer eye even with her face at rest, "
 "creased crepey skin under the eyes below the dark circles, deep folds from the nose to the mouth corners, deep marionette lines from the mouth corners to the chin, "
 "fine vertical lines all along the upper lip, a crease across the chin, and three deep rings around the neck. "
 "They read as a tired fifty-seven-year-old face in the face close-up and can be seen in the front view. Bare skin, no makeup. "
 "No other change anywhere: the dark circles stay as they are, no younger face, no smoothing, no change of expression, no change of colour elsewhere.")
if __name__ == "__main__" and "--edit-v4" in __import__("sys").argv:
    (pathlib.Path(__file__).parent / "N-BEFORE.v4.edit.prompt.txt").write_text(EDIT_WRINKLES); print(len(EDIT_WRINKLES))
