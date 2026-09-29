#!/usr/bin/env python3
"""§19 avatar-sheet prompts for stryde-lost-moments, assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

CAST = {
 "N-NARR": dict(sex="WOMAN", side="left", wall="warm white", floor="worn honey-coloured floorboards",
   face="A round face with high, full cheekbones, deep-set dark brown eyes, a broad nose with a low bridge, full lips and a soft rounded chin — a friendly, capable face. A scatter of small dark raised spots across both cheekbones and under the eyes — her one marker. The left eyebrow sits slightly higher than the right",
   hair="Short natural hair cropped close to the head, black threaded thickly with grey, grey heaviest at the temples, the same length and the same grey in every panel",
   body="A Black British woman of Caribbean heritage. Medium height, full-figured with a soft middle and rounded shoulders, sixty-two years old",
   ward="A mustard-yellow knitted cardigan buttoned over a cream round-neck top, dark blue straight jeans and tan leather loafers",
   age="soft folds from the nose to the corners of the mouth, fine lines fanning from the outer eyes, slight hollowing under the eyes, a faint crease across the lower forehead, a few more of the small dark raised spots at the temples"),
 "C1-GLORIA": dict(sex="WOMAN", side="right", wall="pale cream", floor="a worn oatmeal stair-landing carpet",
   face="A long, narrow face with a high forehead, prominent wide-set eyes with heavy upper lids, a long straight nose, a narrow jaw and thin lips. A thin pale scar cutting through the outer end of her left eyebrow — her one marker. The right eye sits a touch narrower than the left",
   hair="Short silver-white natural hair in small neat twists close to the head, the same silver and the same height in every panel",
   body="A Black British woman of Caribbean heritage. Tall and slender, long-limbed, a little stooped at the upper back, seventy-three years old",
   ward="A lilac knitted cardigan over a white blouse, a navy-and-green floral cotton skirt ending a hand's width above the knee so both knees are bare, and flat burgundy house slippers",
   age="deep folds from the nose to the mouth, fine vertical lines on the upper lip, loose creped skin on the neck, hollowed temples, heavy creasing across the eyelids, soft wrinkled skin over bony knees"),
 "C2-SHEILA": dict(sex="WOMAN", side="left", wall="scuffed off-white", floor="grey slate-effect vinyl",
   face="A broad, square face with a heavy jaw, small pale-blue eyes, a short upturned nose and a wide thin mouth. A flat brown mole on her chin, left of centre — her one marker. The left side of the mouth sits a little higher than the right",
   hair="A short cropped grey pixie cut with a slightly darker nape, thin enough to show the scalp at the crown, the same grey and length in every panel",
   body="A white British woman. Short and stocky, broad shoulders, a thick waist, strong calves, sixty-eight years old",
   ward="A teal lightweight rain jacket open over a grey marl T-shirt, khaki cotton walking shorts ending just above the knee so both knees are bare, grey trainers",
   age="ruddy weathered cheeks with fine broken capillaries, deep crow's feet from squinting, crepe under the eyes, two deep lines between the brows, loose skin at the jaw"),
 "C3-WINSTON": dict(sex="MAN", side="right", wall="dark green painted", floor="worn red quarry tiles",
   face="A broad, heavy-jawed face with heavy-lidded dark eyes, a wide flat nose, full lips and a strong low brow. A small raised dark mole beside the left nostril — his one marker. The right cheek is fuller than the left",
   hair="A shaved head, the scalp smooth and dark, and a short full grey beard, white at the chin, the same length in every panel",
   body="A Black British man of Caribbean heritage. Tall and broad, heavy shoulders, a solid belly, big hands, sixty-seven years old",
   ward="An olive waxed cotton jacket open over a red-and-navy checked flannel shirt, navy cotton shorts ending just above the knee so both knees are bare, grey wool socks and brown leather walking boots",
   age="deep furrows across the forehead, heavy folds from the nose to the mouth, loose skin under the jaw, deep creases at the outer eyes, darker skin over the knuckles and the knees"),
 "C4-GRAHAM": dict(sex="MAN", side="left", wall="pale grey", floor="light grey carpet tiles",
   face="A long, lean face with sharp cheekbones, narrow pale-grey eyes, thin lips and a small pointed chin. His nose is crooked — broken once and set slightly to the left, a bump on the bridge — his one marker. The left eye sits a touch lower than the right",
   hair="Sandy hair gone mostly grey, thinning at the temples, combed in a neat side parting on the left, the same tone and parting in every panel, clean-shaven",
   body="A white British man. Tall and wiry, narrow shoulders, long thin legs, sixty-four years old",
   ward="A navy golf polo shirt, stone-coloured golf shorts ending just above the knee so both knees are bare, white ankle socks and white-and-tan golf shoes",
   age="a deep golfer's tan on the face and forearms with a pale band at the hairline, deep crow's feet, weathered creased forehead, sun spots on the cheekbones and the backs of the hands"),
 "C5-CLIFTON": dict(sex="MAN", side="right", wall="warm beige", floor="honey oak laminate",
   face="A round, full face with soft heavy cheeks, small warm brown eyes behind pouched lids, a broad button nose and a wide full mouth. Large ears that stand out from the head — his one marker. The right side of the mouth sits a little lower than the left",
   hair="Short grey-and-white natural hair cropped close, receding high at both temples, and a neat grey moustache, the same in every panel",
   body="A Black British man of Caribbean heritage. Short and heavyset, a round belly, sturdy thick legs, seventy years old",
   ward="A burgundy cardigan over a plain white T-shirt, grey cotton jersey shorts ending just above the knee so both knees are bare, and navy canvas slippers",
   age="heavy pouches under the eyes, deep smile folds from the nose to the mouth, a soft double chin, fine lines across the forehead, a scatter of small dark raised spots on the cheeks"),
 "C6-SURGEON": dict(pro=True, sex="WOMAN", side="left", wall="pale blue-grey", floor="grey hard-wearing clinic flooring",
   face="An oval face with a strong Roman nose — her one marker — clear hazel eyes that crease easily at the corners, softly arched brows sitting relaxed, a wide mouth and a rounded chin. The right cheekbone sits a touch higher than the left",
   hair="A chin-length auburn bob gone grey at the roots and temples, tucked behind the left ear, the same in every panel",
   body="A white British woman. Medium height, strong-shouldered and upright, fifty-six years old",
   ward="Navy surgical scrubs with a short-sleeved tunic and straight trousers and black clinic clogs",
   age="fine laugh lines at the outer eyes, soft lines across the forehead, light crepe under the eyes, freckling on the forearms"),
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
