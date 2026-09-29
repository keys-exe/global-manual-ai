#!/usr/bin/env python3
"""§19 avatar-sheet prompts for stryde-what-changed, assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

CAST = {
 "H-HOST": dict(host=True, sex="WOMAN", side="left", wall="exposed London stock brick", floor="dark stained floorboards",
   face="A soft heart-shaped face with round apple cheeks, wide-set bright hazel-green eyes that crinkle easily at the corners, gently arched light-brown brows, a small straight nose with a slightly upturned tip, a wide generous mouth with full lips and a small rounded chin — an open, friendly, naturally pretty face. A light scatter of freckles across the nose and cheeks, and one small dark beauty mark high on the left cheekbone — her one marker. The right eye crinkles a touch more than the left. WARM AND LIKEABLE — the face of a presenter people are glad to listen to: the eyes bright, kind and engaged, the lids relaxed, fine laugh lines at their corners; the brow at rest and open; the mouth closed but soft, its corners turned slightly up as if she has just heard something that amused her; the head held easily, relaxed and confident. Friendly, down-to-earth and self-assured, never stern, never cold, not a posed smile",
   hair="Honey-blonde hair with darker roots, a soft shoulder-length cut with loose natural waves and a little volume, tucked behind the right ear, the same length and the same tone in every panel",
   body="A white British woman. Medium height, softly athletic with a natural healthy figure, relaxed open posture, forty-one years old",
   ward="A soft oatmeal-cream chunky cable-knit jumper, mid-blue straight jeans and dark brown leather Chelsea boots",
   age="fine laugh lines at the outer eyes, faint soft folds from the nose to the corners of the mouth, a faint crease across the forehead, a light scatter of freckles"),
 "R1-MAUREEN": dict(sex="WOMAN", side="right", wall="pale sage green", floor="a worn beige hall carpet",
   face="A heart-shaped face with a broad forehead narrowing to a small pointed chin, round light-blue eyes, a short straight nose and thin lips with a pronounced cupid's bow. A small raised brown mole just above the right corner of her upper lip — her one marker. The right eye sits a little lower than the left",
   hair="Soft white hair cut in a short layered crop with a little lift at the crown, the same white and the same shape in every panel",
   body="A white British woman. Short and slight, narrow shoulders, a small rounded back, thin legs, sixty-nine years old",
   ward="A dusty-pink cotton cardigan over a navy-and-white striped Breton top, a navy cotton A-line skirt ending just above the knee so both knees are bare, white canvas plimsolls",
   age="fine crepe across the cheeks and under the eyes, deep vertical lines on the upper lip, pale freckling and age spots on the forehead and the backs of the hands, loose soft skin at the jaw and neck, thin skin over bony knees"),
 "R2-DESMOND": dict(sex="MAN", side="left", wall="light grey painted", floor="scuffed pale oak floorboards",
   face="A long rectangular face with a strong square jaw, deep-set dark brown eyes, a broad straight nose and a wide firm mouth. A short pale scar across the bridge of his nose from an old football knock — his one marker. The left side of his mouth sits a touch lower than the right",
   hair="Close-cropped grey-white natural hair with a clean line-up at the temples and a short neat salt-and-pepper beard, the same length and the same grey in every panel",
   body="A Black British man of Jamaican heritage. Tall and still athletic, broad shoulders, a thickened middle, strong thighs, sixty-six years old",
   ward="A navy zip-neck sports top over a white T-shirt, dark grey jogging shorts ending just above the knee so both knees are bare, white trainers with navy trim",
   age="deep lines across the forehead, heavy creases at the outer eyes, folds from the nose to the mouth, grey in the brows, darker skin over the knuckles and the knees"),
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
    if c.get("host"):                         # same Fix: realistic skin kept, the "unflattering" instruction dropped
        skin = skin.replace(" Bare skin, no makeup, unflattering.", " Bare skin, no makeup.")
    ndf = S("NEG-DEFAULT-FACE")
    if c.get("host"):                         # user Fix 2026-09-29 (§34, H-HOST only): "more attractive / pleasing personality"
        ndf = ndf.replace(", no catalogue-model bone structure", "").replace(", no soft agreeable features throughout, not a face that could advertise anything", "")
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
