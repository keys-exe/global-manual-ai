#!/usr/bin/env python3
"""§19 avatar-sheet prompts for stryde-not-your-cartilage, assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

CAST = {
 "N-NARR": dict(sex="WOMAN", side="right", wall="pale duck-egg blue", floor="grey-brown carpet",
   face="A round soft face with full cheeks that have dropped a little at the jaw, deep-set dark brown eyes under low heavy brows, a short upturned nose and a small full mouth with a deep cupid's bow — a warm, knowing, unhurried face. A short pale scar across the tip of her nose — her one marker. The right eye sits very slightly lower than the left",
   hair="Dark brown hair threaded with grey, pulled back into a low loose bun at the nape with a few strands escaping at the temples, the same in every panel",
   body="A white British woman from the West Midlands. Short and solid, round shoulders, a soft full figure, sixty-one years old",
   ward="A mustard-yellow cardigan buttoned over a navy-and-white striped Breton top, dark indigo straight jeans and brown suede ankle boots",
   age="soft creases fanning from the outer eyes, a pair of short vertical lines between the brows, loose skin gathering along the jaw, faint thread veins on the cheeks, deep folds from the nose to the mouth, looser skin at the neck"),
 "R1-FOLAKE": dict(sex="WOMAN", side="left", wall="warm cream", floor="dark walnut floorboards",
   face="A wide face with very high, prominent cheekbones tapering to a narrow pointed chin, narrow deep-set dark eyes, straight dark-grey brows, a broad flat nose and a wide mouth with a full lower lip. A small raised keloid bump on the top rim of her right ear — her one marker. The left cheekbone sits a little higher than the right",
   hair="Long thin box braids, grey and black mixed, tied back in a low ponytail at the nape, the same length and the same grey in every panel",
   body="A Black British woman of Nigerian heritage. Medium height, slim and wiry, a long neck, narrow hips, sixty-six years old",
   ward="A plum-purple long-sleeved cotton top, a grey knitted waistcoat, mid-grey cotton shorts ending just above the knee so both knees are bare, black leather slip-on shoes",
   age="soft creases under the eyes, fine lines at the outer eyes, folds from the nose to the corners of the mouth, a few dark raised spots at the temples, darker, looser skin over the knuckles and the knees, thin skin along the neck"),
 "R2-DEREK": dict(sex="MAN", side="right", wall="pale grey", floor="worn beige lino",
   face="A broad square face, heavy-lidded pale grey eyes, bushy white brows, a wide flattened nose, a thin wide mouth inside a short neatly clipped white beard. The top joint of his left index finger is missing, an old workshop accident — his one marker. The left side of his beard grows a little thinner than the right",
   hair="White hair, thick and wavy, combed back from a high forehead and a little long over the collar, the same in every panel",
   body="A white British man from the north-east of England. Big-framed and heavy in the chest and shoulders, a round belly, thick legs, seventy-four years old",
   ward="A bottle-green quilted gilet over a grey marl sweatshirt, stone-coloured cotton shorts ending just above the knee so both knees are bare, black trail walking shoes with thick grey socks",
   age="deep creases across the forehead and around the eyes, a red weathered flush over the nose and cheeks, heavy bags under the eyes, liver spots on the backs of the hands, loose folds at the throat, knobbly swollen knees"),
 "R3-HASSAN": dict(sex="MAN", side="left", wall="soft buttermilk", floor="light grey laminate",
   face="A long face with a heavy square jaw, hollow cheeks and a prominent forehead, deep-set eyes under a heavy brow ridge, a long nose broad at the tip, a wide mouth with thin lips, clean-shaven with grey stubble shadow. A thin pale scar running two centimetres along his right jawline — his one marker. His right ear sits a little further out from the head than the left",
   hair="Grey hair grown into a short rounded afro, thinning and receding at the crown, the same shape and the same grey in every panel",
   body="A Black British man of Sudanese heritage, very dark skin. Very tall and thin, long arms and legs, a slight stoop at the shoulders, seventy-two years old",
   ward="A sky-blue short-sleeved cotton shirt, buttoned, tucked into navy chino shorts ending just above the knee so both knees are bare, brown leather lace-up shoes with dark socks",
   age="deep lines across the forehead, heavy creases at the outer eyes, folds from the nose to the mouth, a few grey hairs in the brows, darker, drier skin over the knuckles and the knees, loose skin at the throat"),
 "R4-ELAINE": dict(sex="WOMAN", side="right", wall="light stone", floor="pale ash floorboards",
   face="A narrow heart-shaped face with a pointed chin, bright blue eyes set wide apart, fine fair brows, a long thin nose with a slight bump, a narrow mouth with thin lips. A small cluster of three pale freckle-sized moles under her left eye — her one marker. Her smile lines sit deeper on the right than on the left",
   hair="Straight fine blonde hair gone ash-grey, cut in a short layered pixie that sits flat and a little tousled, the same in every panel",
   body="A white British woman of Welsh heritage. Petite and slim, narrow shoulders, thin legs, sixty-three years old",
   ward="A rust-orange lightweight zip-up jacket over a cream T-shirt, black cotton shorts ending just above the knee so both knees are bare, white-and-grey running trainers",
   age="fine lines around the eyes and mouth, a crease between the brows, thin crepey skin on the eyelids and neck, faint sun spots on the cheeks and backs of the hands, thin skin over the knees"),
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
