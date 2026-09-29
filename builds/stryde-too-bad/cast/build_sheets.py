#!/usr/bin/env python3
"""§19 avatar-sheet prompts for stryde-too-bad, assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

CAST = {
 "N-NARR": dict(sex="WOMAN", side="left", wall="warm off-white", floor="mid-oak laminate",
   face="A long narrow face with high flat cheekbones, hooded grey-green eyes, a slightly hooked narrow nose and a thin straight mouth that turns down a little at the corners — a dry, level, sensible face. A small white scar through the outer end of her right eyebrow, breaking it — her one marker. The left side of her mouth sits a touch higher than the right",
   hair="Ash-blonde hair gone mostly silver, cut in a blunt chin-length bob with a straight fringe, the same length and the same tone in every panel",
   body="A white British woman. Tall and narrow, long neck, slightly stooped shoulders, fifty-seven years old",
   ward="A charcoal-grey merino V-neck jumper over a white T-shirt, black straight-leg trousers and black leather loafers",
   age="fine lines at the outer eyes and across the forehead, a deep vertical line between the brows, soft folds from the nose to the mouth, faint sun spots on the cheekbones, slightly crepey skin on the neck"),
 "R1-DENISE": dict(sex="WOMAN", side="right", wall="soft warm beige", floor="honey-coloured hardwood",
   face="A square face with a broad, strong jaw and full rounded cheeks, wide-set warm brown eyes under full straight dark-grey brows, a wide nose with a low bridge and a generous full mouth. A single short deep dimple in her left cheek — her one marker. The right side of her jaw is a little fuller than the left",
   hair="Chin-length natural hair in soft grey-and-black twist-out curls with volume at the crown, the same shape, length and grey in every panel",
   body="An African-American woman from the American South. Medium height, sturdy and broad-shouldered, a full bust and a soft middle, strong legs, sixty-four years old",
   ward="A coral-red cotton crew-neck T-shirt under an open chambray denim shirt, white cotton shorts ending just above the knee so both knees are bare, white canvas lace-up sneakers",
   age="small dark raised spots across both cheekbones, soft creases at the outer eyes, folds from the nose to the corners of the mouth, a few fine lines across the forehead, a slight softness under the jaw, darker skin over the knuckles and knees"),
 "R2-ALAN": dict(sex="MAN", side="left", wall="plain magnolia", floor="scuffed red quarry tiles",
   face="A long thin face with sunken cheeks, small pale blue eyes set close together under wiry white brows, a large nose with a visible crook to the left from an old break — his one marker — and large ears. The left ear sits a little lower than the right",
   hair="Bald on top with a short white fringe of hair around the back and sides, the same in every panel",
   body="A white British man. Short and wiry, thin arms, a slight bow in the legs, seventy-two years old",
   ward="A faded red-and-green checked flannel shirt with the sleeves rolled to the elbow, khaki cotton shorts ending just above the knee so both knees are bare, brown leather walking shoes with grey socks",
   age="deep weathered lines across the forehead and around the eyes, sun-damaged mottled skin on the scalp and forearms, broken veins on the cheeks, loose skin at the neck, knobbly knees"),
 "R3-CLIVE": dict(sex="MAN", side="right", wall="pale stone", floor="dark grey vinyl tiles",
   face="A long lean face with high sharp cheekbones, hooded dark brown eyes, a long straight nose and a wide thin-lipped mouth under a neat white moustache, a narrow chin, clean-shaven apart from the moustache. A small raised scar on his left earlobe — his one marker. The right brow sits lower than the left",
   hair="Short grey-white natural hair, tightly coiled, with a receding hairline high at both temples, the same length and the same grey in every panel",
   body="A Black British man of Trinidadian heritage. Tall and lean, long arms, narrow hips, long thin legs, sixty-seven years old",
   ward="A burgundy cotton polo shirt, beige chino shorts ending just above the knee so both knees are bare, tan suede desert boots",
   age="deep lines across the forehead, heavy creases at the outer eyes, folds from the nose to the mouth, a few grey hairs in the brows, darker skin over the knuckles and the knees, loose skin at the throat"),
 "R4-FIONA": dict(sex="WOMAN", side="left", wall="soft sage", floor="light oak floorboards",
   face="A wide oval face with a strong jaw, light hazel eyes, a straight nose with a rounded tip and a wide mouth, freckles across the nose and cheeks. A small pale scar on the point of her chin — her one marker. The left brow arches higher than the right",
   hair="Shoulder-length curly hair, faded copper-red going grey at the temples, worn loose, the same length, the same curl and the same tone in every panel",
   body="A white British woman of Scottish heritage. Tall and strong-shouldered, long-limbed, sixty-six years old",
   ward="A teal fleece zip-neck top over a white T-shirt, navy cotton shorts ending just above the knee so both knees are bare, grey trail trainers",
   age="freckles and sun spots across the face and forearms, fine lines around the eyes and mouth, a crease between the brows, looser skin at the jaw and neck, thin skin over the knees"),
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
