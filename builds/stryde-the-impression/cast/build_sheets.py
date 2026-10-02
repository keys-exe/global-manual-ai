#!/usr/bin/env python3
"""§19 Mode 4 avatar-sheet prompts for stryde-the-impression, assembled from Appendix A by ID (never retyped).
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
  "A British family drama shot like a prestige streaming series — a stone terraced house on a steep Yorkshire hill, a Sunday lunch, a high-street chemist, a primary-school gate at the top of the hill, watched with warmth and restraint").replace(
  "[PALETTE: the dominant colours of the sets and wardrobe]",
  "Lived-in domestic colour: overcast grey-blue daylight and warm tungsten lamps in the rooms of the Before; muted sage, navy, oatmeal, gritstone and brick, one pillar-box red on the hill; warming to clear summer daylight, soft greens, cream and honey in the After").replace(
  "[OPTICAL TEXTURE: highlight roll-off, halation, lens softness]",
  "Highlights roll off softly with a faint warm halation around bulbs and bright windows; clean modern glass with a gentle fall-off toward the frame edges")
CAM = (S("CAM-FILM").replace("[CAMERA AND FORMAT]", "an ARRI Alexa 35")
       .replace("[LENS FAMILY]", "a Cooke S4/i prime").replace("[FOCAL]", "50").replace("[STOP]", "T4")
       .replace("[COLOUR SCIENCE]", "ARRI").replace("[RIG]", "a locked tripod at standing eye height"))
CAPF = S("CAP-FILM").replace("[HIGHLIGHT BEHAVIOUR]", "rolling off softly into white with a faint warm halation around bulbs and bright windows, never clipping to a hard edge")
NEGF = S("NEG-FILM").replace(", no actor looking into the lens", "")

# Script CASTING (layer 4) holds: Hazel 67 (grey bob, a good cardigan, kind face — her face is NOT aged), Roy 70,
# Emma 39, Dan 41, Oscar 4, Wendy 74 (not a small woman), a pharmacy assistant 25, a mum with a buggy, the lollipop lady.
# Everything else is derived and §19A-cleared (axis table in BUILD_SHEET.md §3).
CAST = {
 "N-HAZEL": dict(sex="WOMAN", side="left", wall="pale duck-egg blue", floor="worn mid-brown carpet",
   face="A soft round face with full cheeks and wide cheekbones, warm hazel-brown eyes that crinkle at the corners, gently arched light-brown brows gone partly grey, a short rounded nose and a full soft mouth that rests turned up at the corners — a kind face. A small brown mole on her left cheek, halfway between the nose and the ear — her one marker. The left eye sits a touch lower than the right",
   hair="Soft silver-grey hair in a layered jaw-length bob with a side parting on the left, tucked behind the right ear, the same grey and the same length in every panel",
   body="A white English woman from West Yorkshire. Average height, soft and a little rounded, sixty-seven years old and looking exactly sixty-seven, standing straight, plain knees with soft skin",
   ward="A good oatmeal cable-knit cardigan buttoned over a plain navy round-neck top, a mid-grey wool skirt ending just above the knee so both knees are bare, and navy low-heeled leather loafers",
   age="soft laughter lines at the outer eyes, light creasing under the eyes, gentle lines from the nose to the mouth, a few faint freckles and sun spots on the cheekbones, faint lines across the forehead"),
 "C1-ROY": dict(sex="MAN", side="right", wall="warm magnolia", floor="light oak laminate",
   face="A long, lean face with a high domed forehead, deep-set grey eyes under bushy salt-and-pepper brows, a long nose with a slight bend to the left from an old break, large ears and a thin wide mouth that smiles easily. A deep vertical dimple in his chin — his one marker. His right eyebrow sits higher than his left",
   hair="Thinning white hair, closely cut, receding at the temples with the pink scalp showing on top, clean-shaven, the same in every panel",
   body="A white English man from West Yorkshire. Tall and long-limbed, slightly stooped at the shoulders, wiry, seventy years old",
   ward="A navy quilted gilet over a pale blue Oxford-cotton shirt with the sleeves rolled once, tan chinos and brown suede desert boots",
   age="deep horizontal furrows on the high forehead, crow's feet fanning far from the eyes, weathered ruddy skin over the cheekbones, deep folds from the nose to the mouth, loose skin at the neck, liver spots on the temples"),
 "C2-EMMA": dict(sex="WOMAN", side="left", wall="pale grey", floor="grey carpet tiles",
   face="Her mother's round face made longer, wide cheekbones, hazel-green eyes, straight brown brows, a short nose with a light dusting of freckles and a wide expressive mouth. A small white scar through the outer end of her left eyebrow — her one marker. Her smile pulls higher on the right",
   hair="Mid-brown hair to the shoulders with grown-out honey highlights, worn in a messy high ponytail with loose strands at the front, the same colour and height in every panel",
   body="A white English woman. Medium height, slim and quick, thirty-nine years old",
   ward="A grey marl crew-neck sweatshirt, dark blue straight jeans and white canvas trainers, a thin gold chain at the neck",
   age="faint lines across the forehead, the first crow's feet, slight tired shadows under the eyes, smooth cheeks"),
 "C3-DAN": dict(sex="MAN", side="right", wall="pale sage green", floor="honey-coloured floorboards",
   face="A broad square face with a strong jaw, warm dark brown eyes under thick straight black brows, a broad nose and a full mouth, a neat short black beard. A small round scar high on his right cheekbone — his one marker. His left ear sits a touch lower than his right",
   hair="Thick black hair, short at the sides and a little longer and swept back on top, a few grey hairs at the temples, the same in every panel",
   body="A British Indian man of Punjabi heritage. Tall, broad-shouldered and solid, forty-one years old",
   ward="A dark green half-zip knitted jumper over a white T-shirt, charcoal chinos and brown leather trainers",
   age="faint lines across the forehead, laughter lines at the outer eyes, a little grey at the temples and in the beard"),
 "C4-OSCAR": dict(sex="BOY", side="left", wall="pale yellow", floor="worn mid-brown carpet",
   face="A round little face with full cheeks, big dark brown eyes with long lashes, a small button nose and a wide gap-toothed grin held closed. A tiny dark freckle on the tip of his nose — his one marker. A cowlick at the front of his hair",
   hair="Thick dark brown curly hair, short and a little untidy, the same in every panel",
   body="A four-year-old boy of mixed heritage, white English and British Indian, light-brown skin. Small for a four-year-old, sturdy legs, a round tummy",
   ward="A red-and-navy striped long-sleeve T-shirt, navy shorts to just above the knee, white socks and blue Velcro trainers",
   age=None),
 "C5-WENDY": dict(sex="WOMAN", side="right", wall="cream", floor="worn red-and-brown patterned carpet",
   face="A broad, strong face with high rounded cheekbones, bright dark-brown eyes under thin arched brows, a broad nose, a wide full mouth and a firm square chin. A gold front tooth that shows when she talks — her one marker. Her left cheek is a touch fuller than her right",
   hair="Close-cropped natural hair gone completely white, neat and rounded to the head, the same in every panel",
   body="A Black British woman of Barbadian heritage. Tall and heavyset, broad hips and shoulders, strong legs, upright and brisk, seventy-four years old",
   ward="A cobalt-blue light cotton mac worn open over a navy-and-white spotted shirt dress that ends just below the knee, and black leather walking shoes, a canvas book bag on one shoulder",
   age="fine lines at the outer eyes, soft folds from the nose to the mouth, small dark raised spots across the cheekbones, a slight softening under the jaw"),
 "X1-ASSISTANT": dict(sex="WOMAN", side="left", wall="clinical white", floor="grey speckled vinyl",
   face="A narrow oval face with large dark-brown eyes, thick dark brows, a long straight nose, a small mouth and a pointed chin. A small dark mole just above the right corner of her mouth — her one marker. Her right eye is a touch narrower than her left",
   hair="Covered by a plain navy jersey hijab pinned neatly under the chin, the same in every panel",
   body="A British Bangladeshi woman. Petite and slight, twenty-five years old",
   ward="A navy pharmacy-assistant tunic with short sleeves over a white long-sleeve top, black trousers and black trainers, a plain white name badge with no writing",
   age="smooth young skin, faint shadows under the eyes"),
 "X2-MUM": dict(sex="WOMAN", side="right", wall="warm white", floor="light grey laminate",
   face="A long freckled face with pale blue eyes, sandy brows, a long straight nose, a wide thin mouth and a pointed chin. A small silver stud in her left nostril — her one marker. Her left eyebrow is a little higher than her right",
   hair="Copper-red hair pulled back into a low ponytail with short wisps escaping at the temples, the same in every panel",
   body="A white English woman. Tall and lean, thirty-two years old",
   ward="A faded light-blue denim jacket over a white T-shirt, black leggings and grey running trainers, a small cross-body bag",
   age="freckles across the nose and cheeks, faint lines at the outer eyes, tired shadows under the eyes"),
 "X3-LOLLIPOP": dict(sex="WOMAN", side="left", wall="pale blue", floor="worn brown carpet",
   face="A small, round, pink-cheeked face with bright blue eyes behind round tortoiseshell glasses, a small upturned nose and a thin smiling mouth. A dimple in her right cheek only — her one marker. Her glasses sit slightly crooked, lower on the left",
   hair="Short dyed-auburn hair in a set wave, a little grey at the roots, under a white peaked cap with a plain black band, the same in every panel",
   body="A white English woman from West Yorkshire. Short and round, sixty-three years old",
   ward="A long fluorescent yellow-green high-visibility coat with two silver reflective bands round the body and arms, buttoned to the neck, black trousers and black lace-up shoes, no writing anywhere on the coat",
   age="soft lines all over the cheeks, crow's feet behind the glasses, rosy thread veins across the cheeks, a soft double chin"),
}

CHILD_SKIN = ("IN THE FACE CLOSE-UP: real young child's skin — soft and matte, faint downy hair catching the window light, "
              "slight natural redness on the cheeks and the tip of the nose, a few tiny pores on the nose, lips a little chapped, "
              "the skin even but never airbrushed or doll-like. A real child, not a model.")

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
    skin = CHILD_SKIN if c["age"] is None else "IN THE FACE CLOSE-UP: " + S("SKIN-T").replace("[AGE-FEATURES]", c["age"])
    negd = S("NEG-DEFAULT-FACE")
    if c["age"] is None:   # a child: the retiree anti-defaults don't apply; keep the anti-catalogue ones
        negd = "no catalogue child model, no doll-like face, no perfect symmetrical face, no airbrushed skin"
    negs = S("NEG-SHEET")
    if "glasses" in c["face"]: negs = negs.replace("no glasses, ", "")          # her glasses are part of her
    if "chain" in c["ward"] or "stud" in c["face"]: negs = negs.replace("no jewellery, ", "")   # the chain / the stud are hers
    neg = ", ".join([negs, S("NEG-GRID"), NEGF, negd])
    return "\n\n".join([CAM, sheet, skin, LOOK, CAPF, "AVOID: " + neg + "."])

if __name__ == "__main__":
    out = {}
    for k, c in CAST.items():
        p = build(k, c); out[k] = p
        (pathlib.Path(__file__).parent / f"{k}.prompt.txt").write_text(p)
        print(k, len(p))
    json.dump(out, open(pathlib.Path(__file__).parent / "prompts.json", "w"), indent=1)
    (pathlib.Path(__file__).parent / "LOOK.txt").write_text(LOOK)
