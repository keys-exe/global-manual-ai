#!/usr/bin/env python3
"""§19 avatar-sheet prompts for stryde-what-changed, assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

CAST = {
 "H-HOST": dict(sex="WOMAN", side="left", wall="exposed London stock brick", floor="dark stained floorboards",
   face="An oval face with a long straight nose, dark brown almond eyes under straight thick brows, a wide mouth with a fuller lower lip and a firm, slightly squared chin — an open, level, capable face. A single streak of grey running back from her left temple through the dark hair — her one marker. The left brow sits a touch higher than the right",
   hair="Dark brown-black hair with loose waves to just below the shoulders, parted slightly off-centre to the right, the grey streak from the left temple visible in every panel, the same length and the same tone in every panel",
   body="A British woman of Indian heritage. Medium height, slim with straight shoulders, forty-eight years old",
   ward="A forest-green fine-knit crew-neck jumper, dark indigo straight jeans and tan suede ankle boots",
   age="fine lines fanning from the outer eyes, soft folds from the nose to the corners of the mouth, faint creasing across the forehead, slight darkening under the eyes, a few grey hairs at the parting"),
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
