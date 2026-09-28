#!/usr/bin/env python3
"""§19 avatar-sheet prompts for stryde-thirty-years, assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

CAST = {
 "C1-MAKER": dict(sex="MAN", side="left", wall="pale grey-painted brick", floor="a grey concrete workshop floor, scuffed",
   face="A narrow, hollow-cheeked face with a long jaw, deep-set pale grey eyes under a low brow, and a neat grey moustache, no beard. His one marker: a hooked nose broken once and set crooked, a hard bump on the bridge and the tip bent clearly to his left. The left side of the mouth sits a little higher than the right",
   hair="Thin grey hair combed straight back, the pink scalp showing through across the crown, grey at the temples, the same tone and the same combed line in every panel",
   body="A white British man. Short and wiry, narrow shoulders, sinewy forearms, big-knuckled working hands, sixty-two years old",
   ward="A faded navy canvas work apron over a green-and-brown checked flannel shirt with the sleeves rolled to the elbow, grey work trousers and brown leather work shoes",
   age="deep vertical lines between the brows, crow's feet cut deep at both eyes, hollows under the cheekbones, a crease across the bridge of the nose from reading glasses, sun spots on the temples and the backs of the hands"),
 "S1-WEARER": dict(sex="WOMAN", side="right", wall="warm cream", floor="a pale fawn stair carpet landing",
   face="A long, angular face with a strong straight nose, high flat cheekbones, wide-set blue eyes and a thin wide mouth. Her one marker: large ears that stand well out from the head, clearly visible with the hair tucked behind them. The right eyebrow sits a little higher than the left",
   hair="Chin-length straight hair dyed dark brown and grown out, two inches of silver roots at the parting, tucked behind the ears, the same tone and the same length in every panel",
   body="A white British woman. Tall and lean, long legs, a slightly forward stoop at the shoulders, sixty-nine years old",
   ward="A mustard-yellow lambswool crew-neck jumper, a navy corduroy A-line skirt ending a hand's width above the knee so both knees are bare, and tan leather ankle boots",
   age="fine lines across the forehead, soft folds from the nose to the corners of the mouth, crepe on the eyelids, a few age spots on the cheekbones, thin skin at the knees with a few fine veins"),
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
