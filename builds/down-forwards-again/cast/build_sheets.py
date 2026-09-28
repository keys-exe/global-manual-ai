#!/usr/bin/env python3
"""§19 avatar-sheet prompts for down-forwards-again, assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

CAST = {
 "D-DOC": dict(sex="MAN", side="left", wall="pale clinic grey-white", floor="light grey vinyl clinic flooring", pro=True,
   face="A broad, square face with a wide flat forehead, light blue-grey eyes set wide apart under fair, straight brows, a short snub nose with a rounded tip, a wide mouth with a thin upper lip, and a softly rounded chin with a shallow cleft. A small flat brown mole high on his right cheekbone, just below the outer corner of the eye — his one marker. The right brow sits a little higher than the left",
   hair="Short sandy-red hair going grey through the sides, the ginger still showing on top, cut short and neat with a side parting on the left; clean-shaven with a faint reddish shadow along the jaw, the same colour and the same length in every panel",
   body="A white British man, fair ruddy skin with a scatter of faded freckles across the nose and cheeks. Medium height, stocky and broad through the chest and shoulders, a solid middle, fifty-four years old",
   ward="A white knee-length doctor's coat worn open over a pale blue button-down shirt with the top button undone and no tie, a black stethoscope hung around the neck, charcoal wool trousers and brown leather lace-up shoes",
   age="soft creases fanning from the outer eyes, two fine horizontal forehead lines, slightly puffy skin under the eyes, a few faded freckles on the cheekbones, a little softening along the jawline and under the chin"),
 "P-PATIENT": dict(sex="WOMAN", side="right", wall="soft sage green", floor="a worn oatmeal hallway carpet",
   face="A small, fine-boned oval face with a narrow pointed chin, pale grey-blue eyes set slightly close under thin sandy brows, a small straight nose, a thin upper lip over a fuller lower lip, and rosy thread-veined cheeks. A small raised flesh-coloured mole just above the right corner of her upper lip — her one marker. The right eye sits a touch narrower than the left",
   hair="Chin-length fine hair dyed a soft chestnut brown with about a centimetre of silver-white roots showing at the parting, cut in a short layered style tucked behind the ears, the same colour, the same roots and the same length in every panel",
   body="A white British woman, fair skin that freckles. Short and petite, narrow-shouldered, slim arms and legs, a slight forward stoop, sixty-nine years old",
   ward="A soft duck-egg blue crew-neck knitted jumper, a knee-length navy-and-cream check wool skirt, flesh-tone tights, and dark brown low-heeled suede ankle boots",
   age="fine vertical lines above the upper lip, crepey skin on the eyelids and neck, a scatter of pale age spots on the temples and backs of the hands, soft folds from the nose to the mouth corners"),
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
