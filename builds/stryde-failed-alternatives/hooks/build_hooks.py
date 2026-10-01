#!/usr/bin/env python3
"""Step 6 hook 1 start images (HK1-01, HK-BR) for stryde-failed-alternatives, from Appendix A and the Product Sheet by ID."""
import re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
sys.path.insert(0, str(ROOT / "products/stryde")); import stryde_product_sheet as P
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
def ANG(h, side, subj, fg=""):
    return (S("ANGLE-LINE").replace("[HEIGHT CLAUSE from §30I]", h).replace("[SIDE]", side).replace("[SUBJECT]", subj)
            .replace("[, looking past FOREGROUND, soft in the near foreground | , seen in REFLECTION]", fg))
def FOC(plane, depth):
    return (S("FOCUS-LINE").replace("[PLANE — the nearest eye of NAME / the hands and what they hold / the product and its wordmark / the foreground / everything]", plane)
            .replace("[DEPTH — the room behind falls to a soft, recognisable shape | everything from near to far stays sharp]", depth))
def LIGHT(src, subj, side, q, lit_clause):
    return (S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", src).replace("[SUBJECT]", subj)
            .replace("[SCREEN SIDE]", side).replace("[TIME-OF-DAY QUALITY and the act's light state]", q).replace("[SIDE]", "the " + side)
            .replace(", so the face has a lit side toward the " + side + " and a softer shadow side, with a small catchlight in the eyes", lit_clause))
def COLOUR(light, k, sets, who, ward, acc, sat):
    return (S("COLOUR-KEY").replace("[LIGHT COLOUR]", light).replace("[KELVIN]", str(k)).replace("[SET COLOURS]", sets).replace("[WHO]", who)
            .replace("[WARDROBE COLOURS]", ward).replace("[ACCENT]", acc).replace("[SATURATION AND CONTRAST IN CAMERA]", sat))
NEGS = lambda *extra: "AVOID: " + ", ".join([S("NEG-M1"), S("NEG-FILE"), S("NEG-LIGHT"), S("NEG-SCENE"), S("NEG-HAND")] + list(extra))

# ---- HK1-01: Bernadette's hand pushes the hall-dresser drawer of old supports shut (start: mid-push, drawer still open) ----
SUPPORTS = ("crammed full of old knee supports that did not work, tangled together: black and grey stretch knee sleeves, a beige elastic wrap, "
            "a hinged knee brace with metal side bars and black velcro straps, a blue gel knee wrap, a neoprene sleeve with a hole for the kneecap, "
            "all plain, worn and unbranded, spilling up above the drawer's edge")
HK1 = "\n\n".join([
 S("CAM-LOCK"),
 ANG("a high camera looking down at about forty-five degrees", "three-quarter, from her right,", "her hand and the open drawer"),
 FOC("the foreground", "the room behind falls to a soft, recognisable shape"),
 "Nobody's face is seen. THE SAME HALL as the attached location plate: the dark oak hall dresser against the left-hand wall with its mirror above, the red, cream and black encaustic floor tiles below, the green stair carpet soft in the background. "
 "The dresser's wide top drawer is pulled fully open towards the camera and is " + SUPPORTS + ". "
 "Her right hand — the hand of THE SAME WOMAN as the attached reference sheet, a Black British woman of sixty-nine, small and slight, darker skin over the knuckles, short plain nails, the rust-orange roll-neck cuff at her wrist under the sleeve of a cream chunky cardigan — "
 "is flat against the drawer's front edge, caught mid-push: the drawer has just started to move back in, about a hand's width shut, the pile of supports shifting with it, her fingers spread and pressing, the wrist bent with the effort. "
 "One strap end of the hinged brace hangs over the drawer's edge.",
 LIGHT("the bright morning wash through the stained-glass front-door panel behind the camera", "the drawer and her hand", "left",
       "bright morning daylight down the hall", ", so the hand and the pile of supports have a lit side toward the left and a softer shadow side"),
 COLOUR("bright east-facing morning daylight, warm-neutral", 5600,
        "faded cream embossed wallpaper, dark oak, red, cream and black encaustic tiles, the deep green stair carpet", "she", "a rust-orange roll-neck under a cream chunky cardigan",
        "the black, grey, beige and blue of the old supports", "natural, lightly saturated"),
 S("CAP-A"), S("CAP-FILE"),
 NEGS("no brand names or logos on any support, no readable text, no labels, no stryde strap anywhere in the drawer, no product, no face in frame, no second hand, no hand inside the drawer"),
])

# ---- HK-BR: the surgeon's hands seat the strap on Delroy's right knee in the clinic (start: strap at mid-shin, hands on the shell) ----
SEAT = P.SEAT_LOCK.replace(" Fingers are just beginning to lift away at the cut, still in contact, the movement unfinished.", "")
START = ("Caught at the start of the move: the strap is still at mid-shin, a hand's width below the kneecap, both of her hands on the shell's two sides ready to slide it up.")
HKBR = "\n\n".join([
 S("CAM-LOCK"),
 ANG("a low, knee-height camera", "three-quarter, from the front and to his right,", "his right knee and her hands"),
 FOC("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
 "THE SAME CONSULTING ROOM as the attached location plate: the padded navy examination couch with its paper roll against the sage-green wall, the light oak desk and the tall window with white blinds soft in the background. "
 "THE SAME MAN as the attached reference sheet — a Black British man of sixty, tall and heavy with a broad chest and thick legs, in a light blue short-sleeved shirt and navy shorts ending above the knee — sits on the edge of the couch, his right leg straight out in front of him, heel resting on the low step, his knee bare. "
 "His face is out of frame above; only his right leg from mid-thigh to ankle, and the hands, are in the picture. "
 "An orthopaedic surgeon crouches beside his leg — only her hands and forearms are seen: a white woman's hands of about fifty, short plain nails, no rings, the cuffs of a soft grey blouse rolled at the wrist. "
 + P.REF_PROD + " " + SEAT.split(". Both hands")[0] + ". " + START + " " + P.WORDMARK_LOCK + " "
 "The strap is worn on the right leg. " + P.LEG_SKIN.replace("of about sixty", "of sixty, Black skin"),
 LIGHT("bright overcast daylight through the tall window on the left-hand wall", "his knee and her hands", "left",
       "bright, even midday overcast light", ", so the knee, the shell and her hands have a lit side toward the left and a softer shadow side"),
 COLOUR("bright overcast midday daylight, neutral to slightly cool", 6500,
        "soft white walls, the sage-green feature wall, the navy couch, light oak, light grey vinyl floor", "he", "a light blue shirt and navy shorts; her cuffs are soft grey",
        "the matte-black strap with its chrome slides", "natural, clean"),
 S("CAP-A"), S("CAP-FILE"),
 NEGS(P.NEG_SEAT.replace("no second person, ", "").replace("no product coming to rest low on the shin, ", ""), P.NEG_WORDMARK, "no strap already seated at the knee", "no strap on the left leg", "no face in frame", "no white coat", "no gloves",
      "no readable text other than the stryde wordmark", "no logos", "no second strap"),
])
for k, v in {"HK1-01": HK1, "HK-BR": HKBR}.items():
    assert "[" not in v, re.findall(r"\[[^\]]*\]", v)[:3]
    pathlib.Path(f"{k}_start.prompt.txt").write_text(v); print(k, len(v))
