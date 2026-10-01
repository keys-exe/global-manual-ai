#!/usr/bin/env python3
"""§19 Mode 4 avatar-sheet prompts for stryde-half-my-age, assembled from Appendix A by ID (never retyped).
Mode 4 sheet (§19): CAM-FILM (tripod, portrait focal) + AVATAR-SHEET/SHEET-GRID + SKIN-T + LOOK-HALFMYAGE + CAP-FILM;
negatives NEG-SHEET + NEG-GRID + NEG-FILM (lens clause dropped: the sheet's close-up looks at the lens) + NEG-DEFAULT-FACE."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

# Film Look Sheet fields 1, 2, 4, 6 (BUILD_SHEET.md §1b) — pasted verbatim, never reworded
LOOK = S("LOOK-PATTERN").replace("[GENRE AND REFERENCE, one plain sentence]",
  "A British family drama shot like a prestige streaming series — an ordinary semi-detached house, a railway station, a wedding and a high-street café, watched with warmth and restraint").replace(
  "[PALETTE: the dominant colours of the sets and wardrobe]",
  "Lived-in domestic colour: cool blue-grey dusk and night in the rooms of the Before, lit by warm tungsten lamps; muted sage, navy, oatmeal and brick; warming to honeyed daylight, soft greens and cream in the After").replace(
  "[OPTICAL TEXTURE: highlight roll-off, halation, lens softness]",
  "Highlights roll off softly with a faint warm halation around bulbs and bright windows; clean modern glass with a gentle fall-off toward the frame edges")
CAM = (S("CAM-FILM").replace("[CAMERA AND FORMAT]", "an ARRI Alexa Mini LF in large format")
       .replace("[LENS FAMILY]", "an ARRI Signature Prime").replace("[FOCAL]", "50").replace("[STOP]", "T4")
       .replace("[COLOUR SCIENCE]", "ARRI").replace("[RIG]", "a locked tripod at standing eye height"))
CAPF = S("CAP-FILM").replace("[HIGHLIGHT BEHAVIOUR]", "rolling off softly into white with a faint warm halation around bulbs and bright windows, never clipping to a hard edge")
NEGF = S("NEG-FILM").replace(", no actor looking into the lens", "")

CAST = {
 "N-HER": dict(sex="WOMAN", side="left", wall="pale sage-green", floor="worn oatmeal carpet",
   face="A long oval face with a high-bridged, slightly beaked nose, pale blue-grey eyes under heavy hooded lids, a wide thin mouth and a small firm chin. A small pale raised mole on the right side of her jaw, just below the ear — her one marker. The right eyebrow sits a little higher than the left",
   hair="Thick steel-grey hair cut to a blunt chin-length bob with a heavy straight fringe, the same grey and the same length in every panel",
   body="A white English woman from the north of England. Small and slight, narrow shoulders, thin wrists, a little rounded at the upper back, seventy-one years old, knobbly knees with loose soft skin",
   ward="A heather-green crew-neck lambswool jumper, a charcoal wool A-line skirt ending a hand's width above the knee so both knees are bare, and black low-heeled leather shoes",
   age="fine freckling and faint sun spots across both cheeks, deep crow's feet, soft crepe under the eyes, fine vertical lines on the upper lip, two creases across the forehead"),
 "C1-BARBARA": dict(sex="WOMAN", side="right", wall="warm magnolia", floor="light oak laminate",
   face="A broad square face with strong cheekbones, wide-set dark brown eyes, straight dark brows gone only partly grey, a short straight nose and a wide generous mouth. A thin white scar across the bridge of her nose — her one marker. The left side of her mouth sits a touch higher than the right",
   hair="Short white hair cropped close at the sides and left a little spiky on top, the same white and the same height in every panel",
   body="A white English woman. Tall and big-boned, broad strong shoulders, sturdy legs, upright and lively, seventy-four years old, weathered skin over the knees",
   ward="A cobalt-blue quilted gilet over a white long-sleeve cotton top, navy cotton culottes ending just above the knee so both knees are bare, and white leather trainers",
   age="deep laughter lines fanning from the outer eyes, heavy folds from the nose to the mouth, loose skin under the jaw, a scatter of age spots on the temples"),
 "C2-DAUGHTER": dict(sex="WOMAN", side="left", wall="pale grey", floor="grey carpet tiles",
   face="An oval face with her mother's high-bridged nose, grey-blue eyes, light freckles across the nose, a straight mouth and a softly rounded jaw. A small dark mole above the left corner of her upper lip — her one marker. The left eye sits a touch lower than the right",
   hair="Dark brown shoulder-length hair with a few grey strands at the parting, pulled back into a loose low bun with strands falling at the temples, the same in every panel",
   body="A white English woman. Medium height, sturdy, strong shoulders, forty-six years old",
   ward="An olive-green hooded parka worn open over a cream cable-knit jumper, dark indigo straight jeans and tan leather ankle boots",
   age="faint lines across the forehead, the start of crow's feet, slight shadows under the eyes, a first softening under the jaw"),
 "C3-HUSBAND": dict(sex="MAN", side="right", wall="pale blue", floor="worn brown carpet",
   face="A broad, heavy face with full jowls, small pale watery-blue eyes under thick white brows, a large bulbous nose and a wide thin mouth. A short pale scar on the point of his chin — his one marker. The right side of his face droops a little lower than the left",
   hair="Thick iron-grey hair swept straight back from the forehead, and a short neatly trimmed grey beard, the same tone and length in every panel",
   body="A white English man. Medium height, round-shouldered, a soft paunch, thin legs, seventy-four years old",
   ward="A brown V-neck wool cardigan over a blue-and-white checked cotton shirt, grey flannel trousers and brown leather slippers",
   age="deep furrows across the forehead, heavy pouches under the eyes, broken veins across the cheeks and nose, loose folds under the jaw, liver spots on the backs of the hands"),
 "C4-SISTER": dict(sex="WOMAN", side="left", wall="cream", floor="worn red-and-brown patterned carpet",
   face="A round, soft face with rosy cheeks, small bright hazel eyes, a short upturned nose, a small pursed mouth and a double chin. A brown mole high on her left cheekbone — her one marker. The left eye is a touch narrower than the right",
   hair="Short permed curls, strawberry-blonde fading to grey at the roots, set close to the head, the same tone and height in every panel",
   body="A white English woman. Short and heavy, a wide waist, thick ankles, a little bow-legged, sixty-eight years old",
   ward="A lilac zip-up fleece jacket over a navy-and-white floral blouse, navy elasticated cotton trousers and beige walking shoes",
   age="fine lines all over the cheeks, crow's feet, a soft sagging jawline, thin lips with vertical lines above them, rosy thread veins across the cheeks"),
 "C5-FRIEND1": dict(sex="WOMAN", side="right", wall="warm white", floor="honey-coloured floorboards",   # v2 — user Fix "I WANT A NEW ONE HERE"
   face="A long, narrow, angular face with sharp high cheekbones, pale green eyes set deep under straight sandy-grey brows, a long thin nose with a slight bump at the bridge, thin lips and a narrow pointed chin, freckles across the nose and cheekbones. A small pale scar on her left cheek, just below the cheekbone — her one marker. The left corner of her mouth sits a touch lower than the right",
   hair="Hennaed copper-red hair cut short and layered close to the head, a little grey showing at the parting, the same copper and the same length in every panel",
   body="A white Irish woman. Tall, lean and wiry, long arms, straight-backed, sixty-nine years old",
   ward="A navy wool pea coat worn open over a red-and-cream Breton striped top, charcoal slim trousers and tan leather brogues",
   age="deep lines across the forehead, crow's feet fanning from the outer eyes, fine crepe under the eyes, lines from the nose to the mouth, sun freckling and a few age spots on the cheekbones"),
 "C6-FRIEND2": dict(sex="WOMAN", side="left", wall="light grey-green", floor="worn grey vinyl",
   face="A round full face with high round cheeks, warm dark brown eyes under low straight brows, a broad nose and a full wide mouth. A small raised dark mole under her left eye — her one marker. The left cheek is a touch fuller than the right",
   hair="Short salt-and-pepper natural hair in a close rounded afro, more salt at the temples, the same shape and tone in every panel",
   body="A Black British woman of Jamaican heritage. Short and full-figured, round shoulders, seventy-two years old",
   ward="A mustard corduroy jacket over a black polo-neck jumper, dark green wide-leg trousers and burgundy leather loafers",
   age="soft folds from the nose to the mouth, fine lines at the outer eyes, slight hollows under the eyes, a scatter of small dark raised spots on the cheeks"),
  "X2-COMMUTER": dict(sex="MAN", side="right", wall="pale grey", floor="grey-flecked lino",   # Hook C one-off, two beats (HKC-SH01, SH02) → §13 sheet
   face="A narrow face with a long straight nose, dark brown eyes under thick straight dark brows, a short dark beard trimmed close along the jaw and a slightly heavy lower lip. A small healed nick through the outer end of his right eyebrow — his one marker. His right ear sits a touch higher than his left",
   hair="Short dark brown hair, faded at the sides and a little longer and tousled on top, the same cut and the same height in every panel",
   body="A white British man in his late twenties. Average height, slim, slightly rounded shoulders from a desk job",
   ward="A plain mid-grey zip-up hoodie over a white T-shirt, black slim trousers and black-and-white canvas trainers, a black backpack on both shoulders",
   age="smooth young skin with a few faint lines at the outer eyes, light stubble shadow above the beard line, faint shadows under the eyes from early starts"),
}

def build(k, c):
    sheet = S("AVATAR-SHEET").replace("facing the phone", "facing the camera")
    first, rest = sheet.split(". ", 1)          # SHEET-GRID pasted after the opening sheet sentence
    sheet = first + ". " + S("SHEET-GRID") + " " + rest
    for a, b in [("[WOMAN/MAN]", c["sex"]), ("[FACE — architecture in three or four plain sentences, the one marker, the asymmetries]", c["face"]),
                 ("[HAIR — colour, roots, how worn, the same tone and the same height in every panel]", c["hair"]),
                 ("[BODY — build, height impression]", c["body"]), ("[WARDROBE — BASE, LOWER, FOOT]", c["ward"]),
                 ("[SIDE]", c["side"]), ("[WALL COLOUR]", c["wall"]), ("[FLOOR]", c["floor"])]:
        sheet = sheet.replace(a, b)
    assert "[" not in sheet, k
    skin = "IN THE FACE CLOSE-UP: " + S("SKIN-T").replace("[AGE-FEATURES]", c["age"])
    neg = ", ".join([S("NEG-SHEET"), S("NEG-GRID"), NEGF, S("NEG-DEFAULT-FACE")])
    return "\n\n".join([CAM, sheet, skin, LOOK, CAPF, "AVOID: " + neg + "."])

if __name__ == "__main__":
    out = {}
    for k, c in CAST.items():
        p = build(k, c); out[k] = p
        (pathlib.Path(__file__).parent / f"{k}.prompt.txt").write_text(p)
        print(k, len(p))
    json.dump(out, open(pathlib.Path(__file__).parent / "prompts.json", "w"), indent=1)
    (pathlib.Path(__file__).parent / "LOOK.txt").write_text(LOOK)
