#!/usr/bin/env python3
"""§19 avatar-sheet prompts for stryde-three-regrets, assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

CAST = {
 "N-NARR": dict(sex="WOMAN", side="left", wall="pale sage green", floor="a worn oatmeal cord carpet",
   face="A long, narrow face with high flat cheekbones, deep-set grey-green eyes under a low straight brow, a long nose with a small hook at the bridge and a thin wide mouth — a quick, dry, listening face. A clear gap between her two front teeth, her one marker, showing whenever her lips part. The left eyebrow sits a touch higher than the right",
   hair="Straight hair once dyed dark chestnut, grown out so the top four centimetres are steel grey, pulled back into a low loose knot at the nape, the same grey line and the same knot in every panel",
   body="A white British woman. Tall and wiry, long arms, narrow shoulders held a little forward, fifty-seven years old",
   ward="A rust-orange needlecord overshirt worn open over a plain cream crew-neck T-shirt, straight dark indigo jeans and tan leather lace-up shoes",
   age="fine crow's feet at both eyes, two vertical lines between the brows, a soft fold from the nose to each corner of the mouth, faint freckling across the cheekbones"),
 "R1-GAIL": dict(sex="WOMAN", side="right", wall="warm magnolia", floor="light oak laminate",
   face="A broad, square, heavy-jawed face with full cheeks, round prominent pale-blue eyes, a short upturned nose and a wide full mouth. A hard bunion bulging at the base of each big toe, pushing out the side of each sandal strap, her one marker, visible in every full-length panel. The right side of the mouth sits slightly higher than the left",
   hair="Fine, thin hair dyed coppery auburn, cut in a chin-length bob with a side parting where the pale scalp shows through, the same copper and the same parting in every panel",
   body="A white British woman. Tall and big-boned, broad shoulders, heavy through the hips and thighs, sixty-two years old",
   ward="An olive-green zip fleece over a navy-and-white checked shirt, stone-coloured cotton shorts ending a hand above the knee, grey walking socks and brown walking sandals",
   age="soft creases across the forehead, deep smile lines, loose skin under the jaw, a scatter of age spots on the backs of the hands"),
 "R2-KEN": dict(sex="MAN", side="left", wall="pale cool grey", floor="dark red quarry tiles",
   face="A thin, long face with hollow cheeks, small narrow dark-brown eyes under one heavy, unbroken dark-grey brow, and a nose broken long ago and set crooked to the right, his one marker. A thin-lipped mouth and a small pointed chin. The left eye is slightly narrower than the right",
   hair="Sparse white hair, short and neatly combed straight back, pink scalp visible through it on the crown, clean-shaven, the same in every panel",
   body="A white British man. Small and wiry, straight-backed like an ex-serviceman, thin forearms with ropey veins, seventy-two years old",
   ward="A pressed pale-blue short-sleeved checked shirt tucked into navy chino shorts ending just above the knee, a brown leather belt, navy socks and polished brown leather shoes",
   age="deep grooves from the nose to the mouth, crêpey skin at the neck, heavy horizontal forehead lines, the skin thin and shiny over the knuckles"),
 "R3-JOAN": dict(sex="WOMAN", side="right", wall="faded primrose yellow", floor="a red-and-cream patterned hallway runner on dark boards",
   face="A small, round, soft face with plump cheeks, small bright hazel eyes set close, a small button nose and a small chin, a gentle rosebud mouth. A thin white scar running up through her right eyebrow, splitting it in two, her one marker. The left cheek is a little fuller than the right",
   hair="Thick pure-white hair cut short in a tidy pixie crop, full at the crown, the same white and the same height in every panel",
   body="A white British woman. Small and slight, narrow shoulders, a slight forward lean from the upper back, seventy-nine years old",
   warm="FRIENDLY AND NATURAL — a kind, easy face you would stop to chat with at the bus stop: the eyes bright and soft, the lids relaxed, crow's feet fanning from the corners as if she has just been told something nice; the brow at rest and open; the mouth closed but soft, its corners turned very slightly up, never pulled down; the jaw loose, the head tilted a touch, the shoulders dropped and easy, standing the way she would stand in her own hallway — relaxed, not posed, not stiff, not stern, not a posed smile",
   ward="A mustard-yellow cable-knit cardigan buttoned over a teal-and-cream floral cotton dress ending just above the knee, bare legs, and navy slip-on canvas shoes",
   age="fine lines all over the face, deep crow's feet, soft hollows at the temples, thin papery skin on the backs of the hands with raised blue veins"),
}

def build(k, c):
    sheet = S("AVATAR-SHEET")
    if c.get("warm"):                         # Fix note 2026-09-28 (user): "make it look friendly and natural"
        c = dict(c, face=c["face"] + ". " + c["warm"])
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
    if c.get("pro") or c.get("warm"):         # §19B: drop the last two clauses (they fight a friendly face)
        ndf = ndf.replace(", no soft agreeable features throughout, not a face that could advertise anything", "")
    neg = ", ".join([S("NEG-SHEET"), S("NEG-GRID"), S("NEG-FILE"), ndf])
    return "\n\n".join([S("CAM-LOCK"), sheet, skin, S("CAP-SHARP"), S("CAP-FILE"), "AVOID: " + neg + "."])

out = {}
for k, c in CAST.items():
    p = build(k, c); out[k] = p
    pathlib.Path(f"{k}.prompt.txt").write_text(p)
    print(k, len(p))
json.dump(out, open("prompts.json", "w"), indent=1)
