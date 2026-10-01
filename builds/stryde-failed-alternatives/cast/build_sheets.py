#!/usr/bin/env python3
"""§19 avatar-sheet prompts for stryde-failed-alternatives, assembled from Appendix A by ID (never retyped)."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

CAST = {
 "N-NARR": dict(sex="WOMAN", side="right", wall="pale buttermilk", floor="worn beige carpet",
   face="A broad round face with full soft cheeks, heavy-lidded pale blue eyes, a short snub nose and a wide mouth with a fuller lower lip — a warm, no-nonsense face. A small round pitted chickenpox scar in the middle of her forehead just above the brows — her one marker. The right eye sits very slightly lower than the left",
   hair="Short white hair cut close at the back and sides and pushed up at the front in a soft spiky crop, the same length and the same white in every panel",
   body="A white British woman. Short and heavyset, a round middle and solid arms, sixty-one years old",
   ward="A bottle-green wool cardigan open over a navy-and-white striped Breton top, dark blue straight jeans and navy canvas slip-on shoes",
   age="fine lines fanning from the outer eyes, soft creases across the forehead, deep folds from the nose to the mouth, a soft double chin, faint thread veins on the cheeks, slightly crepey skin at the throat"),
 "R1-PATRICIA": dict(sex="WOMAN", side="left", wall="soft duck-egg blue", floor="patterned red-and-cream hall carpet",
   face="A long oval face with a high rounded forehead, wide-set dark brown eyes, a broad nose and full lips. Her left eye turns very slightly outward — her one marker. The right cheek sits a touch fuller than the left",
   hair="Short silver-grey hair set in soft rollered waves close to the head, the same shape and the same silver in every panel",
   body="A Black British woman of Jamaican heritage. Tall and big-hipped, heavy through the thighs, upright, seventy-four years old",
   ward="A cerise-pink cardigan buttoned over a cream blouse, a navy A-line skirt ending just above the knee so both knees are bare, black low-heeled lace-up shoes",
   age="soft creases at the outer eyes, folds from the nose to the mouth, a few small dark raised spots under the eyes, loose skin at the jaw and the throat, darker skin over the knuckles and knees"),
 "R2-GORDON": dict(sex="MAN", side="right", wall="nicotine-yellowed cream", floor="brown lino tiles",
   face="A broad flat face with heavy jowls, small dark eyes under one thick dark eyebrow that runs unbroken across the bridge of his nose — his one marker — a short wide nose and a thin straight mouth. The left side of his mouth pulls a little lower than the right",
   hair="Thick salt-and-pepper hair, still mostly dark, cut short and brushed forward into a short fringe, the same in every panel",
   body="A white British man. Medium height with a round pot belly, heavy shoulders and thin legs, sixty-three years old",
   ward="A navy Harrington jacket zipped halfway over a grey marl T-shirt, black knee-length football shorts ending just above the knee so both knees are bare, scuffed white leather trainers",
   age="deep creases across the forehead, pouches under the eyes, open pores across the nose and cheeks, a heavy fold under the jaw, grey stubble at the chin, rough red skin over the knees"),
 "R3-EMMANUEL": dict(sex="MAN", side="left", wall="warm terracotta", floor="dark stained floorboards",
   face="A round face with heavy jowls, a broad flat nose, large dark eyes with heavy lower lids and a wide full mouth, a short neat white beard along the jaw. A small V-shaped notch missing from the top edge of his left ear from an old injury — his one marker. The right ear sits a little higher than the left",
   hair="Short white hair cropped close all over, with a short neat white beard, the same length and the same white in every panel",
   body="A Black British man of Ghanaian heritage. Short and stocky, wide-shouldered, thick forearms, seventy-eight years old",
   ward="A mustard-yellow knitted cardigan over a white collared shirt, tan cotton shorts ending just above the knee so both knees are bare, brown leather sandals worn with no socks",
   age="deep lines across the forehead, heavy creases at the outer eyes, folds from the nose to the mouth, loose skin at the throat, a few small dark raised spots on the cheeks, darker, drier skin over the knuckles and knees"),
 "R4-SIAN": dict(sex="WOMAN", side="right", wall="cool grey", floor="pale grey laminate",
   face="An angular face with narrow grey eyes, a long straight nose, a slight overbite that shows the tips of her top teeth when her mouth is relaxed, and a sharp narrow chin. A shiny pale burn scar across the back of her left hand — her one marker. The left brow sits higher than the right",
   hair="Long straight grey-blonde hair worn in a single plait down her back, the same length and the same tone in every panel",
   body="A white British woman of Welsh heritage. Tall and very thin, bony shoulders and long thin legs, fifty-seven years old",
   ward="A purple waterproof jacket zipped to the chest over a black base layer, black running shorts ending just above the knee so both knees are bare, grey trail shoes",
   age="weathered lines around the eyes from outdoor light, fine lines across the forehead and around the mouth, freckling on the forearms, thin skin over the knees and the backs of the hands"),
 "R1-BERNADETTE": dict(sex="WOMAN", side="left", wall="pale lilac", floor="worn green hall carpet",
   face="A wide face with a broad flat forehead, round full cheeks, small deep-set dark eyes, a short broad nose and a small neat mouth. Three small dark moles in a row along her left jawline — her one marker. The left cheek sits a touch higher than the right",
   hair="Grey-and-black hair in short locs that reach her jaw, worn loose, the same length and the same grey in every panel",
   body="A Black British woman of Nigerian heritage. Small and slight, narrow shoulders, thin arms, sixty-nine years old",
   ward="A rust-orange roll-neck jumper under an olive-green quilted gilet, a charcoal jersey skirt ending just above the knee so both knees are bare, burgundy suede trainers",
   age="soft creases at the outer eyes, fine lines across the forehead, folds from the nose to the mouth, a few small dark raised spots on the cheekbones, loose skin at the throat, darker skin over the knuckles and knees"),
 "R3-DELROY": dict(sex="MAN", side="right", wall="pale mint green", floor="scuffed parquet",
   face="A long rectangular face with a heavy brow ridge, deep-set dark eyes, a wide nose and a broad mouth, clean-shaven. A thick raised scar running down the outside of his right forearm — his one marker. The right side of his jaw is a little heavier than the left",
   hair="Salt-and-pepper hair, still mostly black, cut in a short flat-top with the sides faded close, the same shape and the same grey in every panel",
   body="A Black British man of Jamaican heritage. Tall and heavy, a broad chest and a big belly, thick legs, sixty years old",
   ward="A royal-blue tracksuit top zipped halfway over a white T-shirt, grey jersey shorts ending just above the knee so both knees are bare, black-and-white leather trainers",
   age="deep lines across the forehead, creases at the outer eyes, heavy folds from the nose to the mouth, a few small dark raised spots on the cheeks, a soft fold under the jaw, darker, drier skin over the knuckles and knees")

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
