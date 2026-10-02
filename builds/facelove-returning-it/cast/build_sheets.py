#!/usr/bin/env python3
"""§19 Mode 1 avatar-sheet prompts for facelove-returning-it, assembled from Appendix A by ID (never retyped).
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
            "Take only the face, its bone structure and the hair from Image 1, never its makeup, lashes, lip gloss, clothes, jewellery, light or background.")

FACE = ("A long oval face with high, full cheekbones, warm brown almond eyes under softly arched dark-brown brows, a straight slim nose with a softly rounded tip, "
        "full lips with a defined bow and a smooth, defined jaw tapering to a soft chin. Her one marker: the fold from the left side of the nose to the mouth sits a touch deeper than the right. "
        "The left brow arches a touch higher than the right")
HAIR = ("Long, thick dark-brown hair to the mid-chest with warm caramel highlights through the lengths, worn loose in big soft waves with a deep side parting, "
        "the same tone and the same length in every panel")
BODY = "A Latina American woman with warm olive-tan skin. Medium height, slim with soft curves, forty-six years old"
WARD = "A cream-white fluffy sherpa bathrobe with a wide shawl collar, tied at the waist, over a plain white cotton camisole, bare lower legs and cream fluffy slides"
AGE = ("fine crow's feet at the outer eyes, two faint horizontal lines across the forehead, soft folds from the nose to the mouth, "
       "brownish-violet dark circles and fine crepe under the eyes, blotchy redness across both cheeks and around the nostrils, "
       "uneven patches of darker brown pigmentation high on the cheekbones and the forehead, a scatter of small flat brown post-acne marks along the jawline and the chin")

CAST = {
 "N-BEFORE": dict(title="The creator — bare skin, before the stick (talking head + application start)", after=False),
 "N-AFTER": dict(title="The creator — after: the stick blended in, every line kept (talking head end + after beats)", after=True),
}

def build(k, c):
    sheet = S("AVATAR-SHEET")
    first, rest = sheet.split(". ", 1)
    sheet = first + ". " + S("SHEET-GRID") + " " + rest
    for a, b in [("[WOMAN/MAN]", "WOMAN"), ("[FACE — architecture in three or four plain sentences, the one marker, the asymmetries]", FACE),
                 ("[HAIR — colour, roots, how worn, the same tone and the same height in every panel]", HAIR),
                 ("[BODY — build, height impression]", BODY), ("[WARDROBE — BASE, LOWER, FOOT]", WARD),
                 ("[SIDE]", "left"), ("[WALL COLOUR]", "pale warm grey"), ("[FLOOR]", "worn oak floorboards")]:
        sheet = sheet.replace(a, b)
    neg_sheet = S("NEG-SHEET").replace("no skin patches, ", "")   # the brown patches and redness are the script's problem — wanted
    if c["after"]:   # the after look IS the product on her face: an even, natural foundation finish, terrain unchanged (cover, not erase)
        sheet = sheet.replace("Bare face, no makeup, in every panel including the close-up.",
            "In every panel including the close-up she wears one thin, even layer of a natural foundation exactly matched to her olive-tan skin and nothing else — no eye makeup, no lipstick: the redness and the brown patches are evened out, every line and crease is still there, the skin still reads as skin.")
        neg_sheet = neg_sheet.replace("no makeup, ", "no heavy makeup, no eye makeup, no lipstick colour, no contour, no glowing skin, ")
        skin = ("IN THE FACE CLOSE-UP: real mature skin under a thin, even foundation exactly matched to her olive-tan skin — the tone even, the redness and the brown patches covered, "
                "pores still visible on the nose and cheeks, the fine crow's feet, the forehead lines and the folds from the nose to the mouth still there and still visible, "
                "the foundation lying evenly across the lines and not sitting in them; the neck the same tone as the face; no smoothing, no blur, no airbrushed finish.")
    else:
        skin = "IN THE FACE CLOSE-UP: " + S("SKIN-T").replace("[AGE-FEATURES]", AGE)
    assert "[" not in sheet, k
    neg = ", ".join([neg_sheet, S("NEG-GRID"), S("NEG-FILE")])
    return "\n\n".join([FACE_REF, S("CAM-LOCK"), sheet, skin, S("CAP-SHARP"), S("CAP-FILE"), "AVOID: " + neg + "."])

if __name__ == "__main__":
    out = {}
    for k, c in CAST.items():
        p = build(k, c); out[k] = {"prompt": p, "title": c["title"]}
        (pathlib.Path(__file__).parent / f"{k}.prompt.txt").write_text(p)
        print(k, len(p))
    json.dump(out, open(pathlib.Path(__file__).parent / "prompts.json", "w"), indent=1, ensure_ascii=False)
