#!/usr/bin/env python3
"""§19 avatar-sheet prompts for stryde-regrets, assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

CAST = {
 "N-NARR": dict(sex="WOMAN", side="right", wall="soft sage green", floor="worn mid-oak floorboards",
   face="A long narrow face with high flat cheekbones, clear grey-blue eyes set a little deep, a long straight nose with a slight bump at the bridge and a thin, level, kind mouth — a calm, trustworthy face that listens before it speaks. A small dark mole just above the left corner of the upper lip — her one marker. The left eyebrow sits a touch higher than the right",
   hair="A chin-length silver-grey bob, straight and blunt-cut, with a short straight fringe just above the eyebrows, the same silver and the same length in every panel",
   body="A white British woman. Slim and upright, narrow shoulders, long neck, average height, sixty-two years old",
   ward="A moss-green fine-knit cardigan over a plain cream round-neck blouse, straight charcoal trousers and black leather loafers",
   age="fine lines fanning from the outer eyes, soft vertical lines above the upper lip, light crepe on the eyelids, a faint sun-freckling on the cheekbones, the skin of the neck a little loose"),
 "C1-GRAHAM": dict(sex="MAN", side="left", wall="pale grey", floor="a worn oatmeal bedroom carpet",
   face="A long, lean face with hollow cheeks, heavy-lidded grey eyes, a high hooked nose and a narrow jaw. A thin white scar cuts through his left eyebrow, leaving a gap in the hair — his one marker. The right side of the mouth turns down a little more than the left",
   hair="Thinning grey hair combed straight back from a high forehead, and a neat clipped grey moustache, the same tone and the same length in every panel",
   body="A white British man. Tall, lean and wiry, long arms, bony knees, sixty-seven years old",
   ward="A burgundy cotton polo shirt, khaki chino shorts ending just above the knee so both knees are bare, and brown leather boat shoes",
   age="deep vertical lines between the brows, long folds from the nose to the mouth, weathered skin on the neck, age spots on the temples and the backs of the hands"),
 "C2-LORRAINE": dict(sex="WOMAN", side="left", wall="warm buttermilk", floor="light grey laminate",
   face="A square face with a strong jaw, wide-set green eyes, a short broad nose and a wide mouth that shows a small gap between her two front teeth when it opens — her one marker. The right eye is a fraction narrower than the left",
   hair="Chin-length hair dyed a deep auburn, grown out so an inch of grey shows at the roots and the parting, tucked behind the ears, the same auburn, the same roots and the same length in every panel",
   body="A white British woman. Tall and broad-shouldered, a former sporty frame gone a little soft, strong calves, fifty-nine years old",
   ward="A teal zip-up fleece over a white T-shirt, dark denim shorts ending just above the knee so both knees are bare, and white trainers",
   age="fine lines at the corners of the eyes, a crease between the brows, soft lines from the nose to the mouth, light crepe under the eyes"),
 "C3-KEN": dict(sex="MAN", side="right", wall="warm cream", floor="a patterned brown-and-rust living-room rug on dark boards",
   face="A round moon face with full rosy cheeks, small twinkling pale-blue eyes, a short button nose and a small mouth. His ears are large and stick out from the head — his one marker. The left ear sits slightly higher than the right",
   hair="Thick white hair with a neat side parting on the left, combed flat, bushy white eyebrows, clean-shaven, the same in every panel",
   body="A white British man. Short and round, a rounded belly, short sturdy legs, seventy-two years old",
   ward="A mustard-yellow V-neck wool jumper over a white collared shirt, beige cotton shorts ending just above the knee so both knees are bare, and brown leather walking sandals with grey socks",
   age="deep laugh lines at the eyes, soft jowls, broken capillaries across the cheeks, age spots on the forehead and the backs of the hands, loose soft skin at the knees"),
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
