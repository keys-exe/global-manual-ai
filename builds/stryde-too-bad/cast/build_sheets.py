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
 "R1-GRACE": dict(sex="WOMAN", side="right", wall="pale duck-egg blue", floor="a worn grey hall carpet",
   face="A round full face with wide cheekbones, large dark brown eyes under thin arched brows, a broad short nose and full lips. A clear gap between her two front teeth — her one marker. The right eye is a little narrower than the left",
   hair="Short natural hair, tightly coiled, cropped close to the head and mostly grey with darker patches at the nape, the same length and the same grey in every panel",
   body="A Black British woman of Nigerian heritage. Tall and full-figured, broad hips, strong calves, sixty-two years old",
   ward="A mustard-yellow chunky cotton cardigan over a plain black round-neck top, stone-coloured cotton shorts ending just above the knee so both knees are bare, white leather trainers",
   age="soft lines under the eyes and at their outer corners, deepening folds from the nose to the mouth, small dark raised spots across the cheekbones, a slight softness under the jaw, darker skin over the knees"),
 "R2-ALAN": dict(sex="MAN", side="left", wall="plain magnolia", floor="scuffed red quarry tiles",
   face="A long thin face with sunken cheeks, small pale blue eyes set close together under wiry white brows, a large nose with a visible crook to the left from an old break — his one marker — and large ears. The left ear sits a little lower than the right",
   hair="Bald on top with a short white fringe of hair around the back and sides, the same in every panel",
   body="A white British man. Short and wiry, thin arms, a slight bow in the legs, seventy-two years old",
   ward="A faded red-and-green checked flannel shirt with the sleeves rolled to the elbow, khaki cotton shorts ending just above the knee so both knees are bare, brown leather walking shoes with grey socks",
   age="deep weathered lines across the forehead and around the eyes, sun-damaged mottled skin on the scalp and forearms, broken veins on the cheeks, loose skin at the neck, knobbly knees"),
 "R3-KOFI": dict(sex="MAN", side="right", wall="light warm grey", floor="pale beech floorboards",
   face="A broad square face with a heavy brow, deep-set dark eyes, a wide flat nose and a full mouth, a strong chin. A short clean notch cut through the middle of his left eyebrow — his one marker. The right cheek is a little fuller than the left",
   hair="Clean-shaved bald head and a short neat grey goatee, the same in every panel",
   body="A Black British man of Ghanaian heritage. Medium height, stocky and barrel-chested, thick forearms, a solid belly, fifty-eight years old",
   ward="A heather-grey zip hoodie over a navy T-shirt, navy cotton work shorts ending just above the knee so both knees are bare, black work boots with grey socks",
   age="deep horizontal lines across the forehead, creases at the outer eyes, a few grey hairs in the brows, darker patches of skin on the cheeks, rough dry skin over the knuckles and knees"),
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
