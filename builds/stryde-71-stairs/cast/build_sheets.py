#!/usr/bin/env python3
"""§19 avatar-sheet prompts for stryde-71-stairs, assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

CAST = {
 "N-NARR": dict(sex="WOMAN", side="left", wall="warm white", floor="a worn beige stair-landing carpet",
   face="A heart-shaped face, wide across the cheekbones and narrowing to a small pointed chin, almond-shaped dark brown eyes set under full, slightly hooded lids, a short wide nose with a rounded tip, full lips with a deeper upper lip, and deep laugh lines already set at the eye corners. A small raised dark mole high on her left cheekbone, just below the outer eye — her one marker. The right eyebrow arches a touch higher than the left",
   hair="Natural hair, mostly silver-grey with some black left at the nape, set in a short rounded tapered cut close at the sides and fuller on top, the same grey and the same height in every panel",
   body="A Black American woman from the South, deep brown skin. Medium height, soft and full through the hips and middle, rounded shoulders, sturdy calves, seventy-one years old",
   ward="A coral short-sleeved knit top under an open cream cotton cardigan, dark navy stretch trousers ending at the ankle, and plain black flat slip-on shoes",
   age="deep laugh folds from the nose to the mouth, fine creases fanning from the outer eyes, darker skin pooling under the eyes, a few small dark raised spots on the cheeks and temples, softening skin at the jawline and neck"),
 "C1-LORETTA": dict(sex="WOMAN", side="right", wall="pale butter-yellow", floor="honey oak floorboards",
   face="A long oval face with high sharp cheekbones, bright, wide-open dark eyes under thin arched brows, a long nose with a slight hook at the bridge, a wide mouth that sits a little crooked, lifting higher on the right, and a strong square chin. A thin pale scar cutting down through the middle of her right eyebrow — her one marker. The left eye sits slightly lower than the right",
   hair="A short silver-white natural curly crop, tight coils close to the head, the same silver and the same height in every panel",
   body="A Black American woman from the South, medium-brown skin with warm undertones. Tall and lean, straight-backed, long arms and legs, seventy-four years old",
   ward="A plum-coloured blouse with a small collar, loose khaki cotton trousers that can be rolled above the knee, and white canvas slip-on sneakers",
   age="long vertical creases on the cheeks, fine lines crossing the forehead, thin crepey skin on the neck and the backs of the hands, a scatter of dark spots along the cheekbones"),
 "C2-DAUGHTER": dict(sex="WOMAN", side="left", wall="soft grey", floor="a worn beige stair-landing carpet",
   face="A round face with full cheeks, deep-set dark brown eyes, straight thick brows, a broad nose and full lips, a softly rounded jaw. A small crescent-shaped scar on her chin, left of centre — her one marker. The left corner of her mouth sits a touch lower than the right",
   hair="Shoulder-length natural hair in medium box braids, dark brown, gathered loosely back at the nape, the same length in every panel",
   body="A Black American woman, medium-deep brown skin. Medium height, sturdy and broad-shouldered, forty-six years old",
   ward="A heather-grey crewneck sweatshirt, dark blue jeans and white trainers",
   age="fine lines at the eye corners, a faint crease between the brows, a few small dark spots under the eyes"),
}

def build(k, c):
    sheet = S("AVATAR-SHEET")
    if c.get("pro"):                          # §19B face register (correction 2026-09-26)
        c = dict(c, face=c["face"] + ". " + S("APPROACH-PRO").rstrip("."))
    first, rest = sheet.split(". ", 1)          # SHEET-GRID pasted after the opening sheet sentence
    sheet = first + ". " + S("SHEET-GRID") + " " + rest
    for a, b in [("[WOMAN/MAN]", c["sex"]), ("[FACE — architecture in three or four plain sentences, the one marker, the asymmetries]", c["face"]),
                 ("[HAIR — colour, roots, how worn, the same tone and the same height in every panel]", c["hair"]),
                 ("[BODY — build, height impression]", c["body"]), ("[WARDROBE — BASE, LOWER, FOOT]", c["ward"]),
                 ("[SIDE]", c["side"]), ("[WALL COLOUR]", c["wall"]), ("[FLOOR]", c["floor"])]:
        sheet = sheet.replace(a, b)
    assert "[" not in sheet, k
    skin = "IN THE FACE CLOSE-UP: " + S("SKIN-T").replace("[AGE-FEATURES]", c["age"])
    ndf = S("NEG-DEFAULT-FACE")
    if c.get("pro"):                          # §19B: drop the last two clauses
        ndf = ndf.replace(", no soft agreeable features throughout, not a face that could advertise anything", "")
    neg = ", ".join([S("NEG-SHEET"), S("NEG-GRID"), S("NEG-FILE"), ndf])
    return "\n\n".join([S("CAM-LOCK"), sheet, skin, S("CAP-SHARP"), S("CAP-FILE"), "AVOID: " + neg + "."])

out = {}
for k, c in CAST.items():
    p = build(k, c); out[k] = p
    pathlib.Path(f"{k}.prompt.txt").write_text(p)
    print(k, len(p))
json.dump(out, open("prompts.json", "w"), indent=1)
