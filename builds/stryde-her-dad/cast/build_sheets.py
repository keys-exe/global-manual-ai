#!/usr/bin/env python3
"""§19 Mode 4 avatar-sheet prompts for stryde-her-dad, assembled from Appendix A by ID (never retyped).
Mode 4 sheet (§19): CAM-FILM (tripod, portrait focal) + AVATAR-SHEET/SHEET-GRID + SKIN-T + LOOK-HERDAD + CAP-FILM;
negatives NEG-SHEET + NEG-GRID + NEG-FILM (lens clause dropped: the sheet's close-up looks at the lens) + NEG-DEFAULT-FACE."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

# Film Look Sheet fields 1, 2, 4, 6 (BUILD_SHEET.md §1b) — pasted verbatim, never reworded
LOOK = S("LOOK-PATTERN").replace("[GENRE AND REFERENCE, one plain sentence]",
  "A British working-class family drama shot like a prestige streaming series — a garden-centre car park, a terraced house with a steep narrow staircase, a GP's consulting room, a builders' yard and a back garden, watched with warmth and restraint").replace(
  "[PALETTE: the dominant colours of the sets and wardrobe]",
  "Overcast English daylight and lived-in colour: slate-grey skies, wet tarmac, red brick, khaki and navy workwear and the greens of garden-centre plants; the evenings at home cool blue-grey lit by warm tungsten lamps; warming to low honeyed sun, fresh greens and pale sandstone paving in the After").replace(
  "[OPTICAL TEXTURE: highlight roll-off, halation, lens softness]",
  "Highlights roll off softly with a faint warm halation around bulbs and bright windows; clean modern glass with a gentle fall-off toward the frame edges")
CAM = (S("CAM-FILM").replace("[CAMERA AND FORMAT]", "an ARRI Alexa Mini LF in large format")
       .replace("[LENS FAMILY]", "an ARRI Signature Prime").replace("[FOCAL]", "50").replace("[STOP]", "T4")
       .replace("[COLOUR SCIENCE]", "ARRI").replace("[RIG]", "a locked tripod at standing eye height"))
CAPF = S("CAP-FILM").replace("[HIGHLIGHT BEHAVIOUR]", "rolling off softly into white with a faint warm halation around bulbs and bright windows, never clipping to a hard edge")
NEGF = S("NEG-FILM").replace(", no actor looking into the lens", "")

CAST = {
 "C1-TONY": dict(sex="MAN", side="left", wall="pale putty-grey", floor="worn grey-brown carpet",
   face="A broad, weathered square face with a heavy brow, deep-set grey-blue eyes, a nose broken once and set slightly crooked to the left, high flat cheekbones and a wide firm mouth with a thin upper lip, clean-shaven with a day of grey stubble. A short white scar through the outer end of his left eyebrow — his one marker. The left side of his jaw is a touch squarer than the right",
   hair="Thick salt-and-pepper hair, more salt at the temples, cut short at the back and sides and a little longer on top, combed to the side with a left parting, the same grey and the same length in every panel",
   body="A white English man from the south of England, a builder all his working life. Broad shoulders, a thick neck, strong heavy forearms and big rough builder's hands with thick fingers and short nails, a solid middle, sixty-four years old, a slight stoop at the shoulders, weathered skin over the knees",
   ward="A navy crew-neck sweatshirt with the sleeves pushed to the forearms over a grey marl T-shirt, faded olive canvas work shorts ending just above the knee so both knees are bare, grey work socks and worn tan leather work boots",
   age="deep outdoor creases fanning from the outer eyes, three deep lines across the forehead, sun-darkened leathery skin on the cheeks and neck, heavy folds from the nose to the mouth, a few broken veins on the nose, age spots on the temples"),
 "C2-SUE": dict(skin="SKIN-A", sex="WOMAN", side="right", wall="warm off-white", floor="pale oak floorboards",
   face="A heart-shaped face with wide-set green-hazel eyes, neat arched brows, a small straight nose, defined cheekbones and a full, slightly wide mouth with a pronounced Cupid's bow. A small dark beauty spot high on her right cheekbone — her one marker. Her right eyebrow arches a touch higher than her left",
   hair="Warm chestnut-brown hair with soft caramel highlights, a layered cut just past the shoulders, tucked behind the ears, the same colour and the same length in every panel",
   body="A white English woman. Medium height, slim and toned, quick and upright, fifty-two years old and looking about forty-six, active and well kept",
   ward="A fitted sage-green quilted jacket worn open over a cream fine-knit crew-neck jumper, slim dark-indigo jeans and clean white leather trainers",
   age="fine lines at the outer eyes when she is still, faint lines across the forehead, a slight softness under the eyes, a light scatter of freckles across the nose, the skin otherwise firm and cared for"),
 "C3-GARY": dict(sex="MAN", side="left", wall="pale stone", floor="grey concrete",
   face="A long lean face with a strong hooked nose, sharp cheekbones, small bright pale-blue eyes under bushy white brows, a thin mouth and a short neat white beard trimmed close along a strong jaw. A small notch missing from the top rim of his right ear — his one marker. His left ear sticks out a touch more than his right",
   hair="A completely shaved, tanned bald head with a little white stubble at the sides, the same in every panel",
   body="A white English man. Tall, lean and wiry, long ropey arms with visible veins, flat stomach, straight-backed and springy on his feet, seventy years old and fit — a man who still lifts paving slabs on his own, weathered skin over the knees",
   ward="An open red-and-black buffalo-check flannel overshirt with the sleeves rolled to the elbow over a plain charcoal T-shirt, navy canvas work shorts ending just above the knee so both knees are bare, rolled grey socks and scuffed brown rigger boots",
   age="deep tanned creases across the forehead and around the eyes, hollow temples, loose skin at the throat, sun spots on the scalp and the backs of the hands, fine lines on the upper lip under the beard"),
 "C4-LAD": dict(skin="SKIN-A", sex="MAN", side="right", wall="light grey-green", floor="grey-flecked lino",
   face="A narrow oval face with high cheekbones, warm brown eyes under thick dark brows, a broad straight nose, full lips and a light patchy moustache. A small dark mole on the left side of his neck, below the ear — his one marker. His right eye is a touch narrower than his left",
   hair="Dark brown tight curls kept short, faded close at the sides, the same shape and the same height in every panel",
   body="A mixed-race British young man, Black Caribbean and white English. Tall and lanky, long legs, narrow shoulders, nineteen years old, quick and light on his feet",
   ward="A plain bottle-green polo shirt with no logo and no lettering, a plain dark-green zip fleece worn open over it, black cotton work trousers and black trainers",
   age="smooth young skin with a few faint spots along the jaw, faint shadows under the eyes"),
 "C5-GP": dict(sex="WOMAN", side="left", wall="pale clinical blue-grey", floor="grey speckled vinyl",
   face="An oval face with dark brown almond-shaped eyes, straight dark brows, a long straight nose and a calm closed mouth. A small dark mole on her left jaw, just below the corner of the mouth — her one marker. Her left eyebrow sits a touch lower than her right",
   hair="Black hair with a few grey threads, pulled back into a neat low bun with a centre parting, the same in every panel",
   body="A British Indian woman, a family doctor. Medium height, slim, composed, forty-eight years old",
   ward="A navy fine-knit cardigan over a pale-blue cotton blouse buttoned to the collar, charcoal tailored trousers and black low flat shoes, no lanyard, no badge, no stethoscope",
   age="fine lines at the outer eyes, faint lines across the forehead, soft shadows under the eyes, a little greying at the temples"),
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
    assert "[" not in sheet, (k, re.findall(r"\[[^\]]*\]", sheet))
    skin = "IN THE FACE CLOSE-UP: " + S(c.get("skin", "SKIN-T")).replace("[AGE-FEATURES]", c["age"])   # SKIN-A where the script casts younger-looking (Sue) or young (Lad)
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
