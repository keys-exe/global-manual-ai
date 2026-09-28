#!/usr/bin/env python3
"""stryde-lost-moments — beat T2I prompts (step 6/7), assembled from Appendix A and the Product Sheet by ID.

Order per §30E Part 3 / §30I–§30K: CAM-LOCK → ANGLE-LINE → FOCUS-LINE → PROP-REF/PROP-SHELL or SCENE-REF → SUBJ-REF
(+ FACE-SEED on FACE beats) → the beat's frame (caught mid-action, §27G rule 4) → wardrobe → product strings (worn/seat:
PLACE-LOCK / SEAT-LOCK, ORIENT-C, FIT_SNUG, SIZE_WORN, WORDMARK-LOCK) → LIGHT-SHOT → BROLL-REAL → PHYS-FRAME-C → CAP-A →
CAP-FILE → AVOID (NEG-SUBJ, NEG-PROP, NEG-LIGHT, NEG-M1, NEG-FILE, product negatives).
Usage: beats.py A-HKa A-HKb …   → work/prompts/<beat>.t2i.txt + work/prompts/<beat>.refs.json
"""
import re, json, sys, pathlib, importlib.util
HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[2]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    if not m: raise KeyError(i)
    return m.group(1).strip()
spec = importlib.util.spec_from_file_location("ps", ROOT / "products/stryde/stryde_product_sheet.py")
PS = importlib.util.module_from_spec(spec); spec.loader.exec_module(PS)
ROWS = {r["beat"]: r for r in json.load(open(HERE / "actmap_rows.json"))}
SIDE = "right"

HEIGHT = {"ground": "the lens a few centimetres off the floor, looking along it and slightly up",
          "low": "the lens at hip height, looking up at the subject", "eye": "the lens at the subject's eye height, level",
          "high": "the lens above head height, looking down at the subject", "overhead": "the lens directly above, looking straight down"}
SIDE_W = {"front": "the front", "three-quarter": "a three-quarter angle", "profile": "the side, in profile",
          "three-quarter-back": "a three-quarter angle from behind", "behind": "directly behind", "ots": "over the near shoulder"}

# Property / subject facts used by the beats (Build Sheet + Property Sheets; confirmed renders)
PROP_G_CARRIED = ("buttermilk-yellow plaster walls, chipped white gloss torus skirting, stripped-pine four-panel doors with black iron levers, "
                  "red-and-cream encaustic hall tiles, the deep-red stair runner with brass rods, white spindles and the dark mahogany handrail")
PROP_G_SHELL = {
 "[WALL FINISH AND COLOUR]": "slightly uneven painted plaster walls in a soft buttermilk yellow, scuffed at hip height along the stairs",
 "[SKIRTING — profile, height, colour]": "tall torus-profile wooden skirting painted in chipped white gloss",
 "[ARCHITRAVE]": "wide moulded architraves in the same chipped white gloss",
 "[INTERNAL DOOR — style, colour, handle]": "Victorian four-panel doors stripped to honey-coloured pine with black iron lever handles",
 "[CEILING]": "a high white ceiling with a plaster cornice",
 "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": "red-and-cream Victorian encaustic tiles in the hall, changing at the foot of the stairs to a deep-red patterned stair runner held by brass rods",
 "[RADIATOR TYPE]": "a white column radiator",
 "[SWITCHES AND SOCKETS]": "old white plastic switches",
}
SUBJ = {
 "C1": dict(sheet_job="ded1fa0c-1546-421d-adb5-94c1baee2800", name="Gloria",
            markers="short silver-white natural hair in small neat twists, tall and slender with a slight stoop, a thin pale scar through the outer end of her left eyebrow",
            skin="a Black British woman of seventy-three, dark brown skin, soft wrinkled skin over bony knees"),
}
WARD = {
 "G-D1": "a lilac knitted cardigan over a white blouse, a navy-and-green floral cotton skirt ending a hand's width above the knee so both knees are bare, and flat burgundy house slippers",
}

def fillp(s, d):
    for k, v in d.items(): s = s.replace(k, v)
    assert "[" not in s, s[:160]; return s

def angle_line(r, subject):
    a = r["angle"]
    fg = {"clean": "", "through": ", looking past the white banister spindles, soft in the near foreground", "reflection": ", seen in reflection"}[a["fg"]]
    return (S("ANGLE-LINE").replace("[HEIGHT CLAUSE from §30I]", HEIGHT[a["height"]]).replace("[SIDE]", SIDE_W[a["side"]])
            .replace("[SUBJECT]", subject).replace("[, looking past FOREGROUND, soft in the near foreground | , seen in REFLECTION]", fg))

def focus_line(r, name):
    f = r["focus"]
    plane = {"eyes": "the nearest eye of " + name, "hands": "the hands and what they hold", "product": "the product and its wordmark",
             "foreground": "the foreground", "background": "the background", "deep": "everything"}[f["plane"]]
    depth = ("everything from near to far stays sharp" if f["dof"] == "deep" else "the room behind falls to a soft, recognisable shape")
    return (S("FOCUS-LINE").replace("[PLANE — the nearest eye of NAME / the hands and what they hold / the product and its wordmark / the foreground / everything]", plane)
            .replace("[DEPTH — the room behind falls to a soft, recognisable shape | everything from near to far stays sharp]", depth))

def light_line(r, subject, quality):
    side = {"L": "left", "R": "right", "back": "back", "front": "front"}[r["light"]["key_side"]]
    return (S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", "the " + r["light"]["source"])
            .replace("[SUBJECT]", subject).replace("[SCREEN SIDE]", side).replace("[TIME-OF-DAY QUALITY and the act's light state]", quality)
            .replace("[SIDE]", side))

# ---------------------------------------------------------------- the beats
BEATS = {}

def a_hka():
    r = ROWS["A-HKa"]; s = SUBJ["C1"]
    body = [S("CAM-LOCK"),
     angle_line(r, "her legs on the stairs"), focus_line(r, "Gloria"),
     S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", PROP_G_CARRIED) + " " + fillp(S("PROP-SHELL"), PROP_G_SHELL),
     "THE HALL AND STAIRS of the attached property reference, seen from the hall floor beside the foot of the staircase, looking at the stairs side-on through the open spindle side: the flight rises from right to left across the frame along the left-hand wall, the white spindles and the dark mahogany handrail running diagonally across the upper part of the frame, the deep-red runner on the treads.",
     S("SUBJ-REF").replace("[two or three named markers: hair, build, one distinctive feature]", s["markers"]),
     "Seen from the side and waist-down: she is coming DOWN the stairs SIDEWAYS, her body turned side-on to the flight, her right foot already lowered onto the next step down and taking her weight, her left foot still on the step above, knees stiff and slightly bent. "
     "BOTH HANDS clamp the mahogany handrail at hip height, knuckles pale, arms taking her weight. Her bare knees show below the hem of the skirt. Nothing on either knee. "
     "The frame is cropped at her waist; her face is not in the frame.",
     "Wearing " + WARD["G-D1"] + ".",
     "Real unretouched skin: " + s["skin"] + ", visible pores and creases at the knees, faint dry patches on the shins.",
     light_line(r, "her legs and the stairs", "grey morning light, soft and indirect from above — the problem state, flat and cool, never moody"),
     S("BROLL-REAL"), S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
     "AVOID: " + ", ".join([S("NEG-SUBJ"), S("NEG-PROP"), S("NEG-LIGHT"), S("NEG-M1"), S("NEG-FILE"),
       "no face in frame, no product anywhere, no knee strap, no knee support, no walking stick, no stairlift, no person facing down the stairs, no second person"])]
    return dict(model="nano_banana_2", refs=[("C1 sheet", s["sheet_job"]), ("P0-PROP-G plate", "faf039cb-e64f-4a3c-9772-85b0cb5c26f1")],
                face="NOFACE", body=body)
BEATS["A-HKa"] = a_hka

def a_hkb():
    r = ROWS["A-HKb"]; s = SUBJ["C1"]
    body = [S("CAM-LOCK"),
     angle_line(r, "her right knee"), focus_line(r, "Gloria"),
     S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", PROP_G_CARRIED),
     "At the foot of the stairs in the attached property reference: she sits on the bottom stair, the deep-red runner under her, the turned newel post and the first white spindles beside her, the red-and-cream hall tiles at her feet.",
     S("SUBJ-REF").replace("[two or three named markers: hair, build, one distinctive feature]", s["markers"]),
     "Close from above and to the side, looking down at her right knee as she sees it: her right leg straight out in front of her, heel on the tiles. "
     + PS.REF_PROD + " a single unit. " + PS.fill(PS.SEAT_LOCK, side=SIDE)
     .replace("sitting clearly off-position at mid-shin, well below the knee, on a straight leg.", "caught partway up the shin, a hand's width below the knee and still travelling, on a straight leg.")
     .replace("Fingers are just beginning to lift away at the cut, still in contact, the movement unfinished.", "Both hands are on it mid-slide, the movement unfinished."),
     PS.WORDMARK_LOCK, PS.SIZE_WORN,
     "Her face is out of frame above; the frame holds her hands, her right knee and shin, the hem of her skirt and the bottom step.",
     "Wearing " + WARD["G-D1"] + ".",
     "Real unretouched skin: " + s["skin"] + ", knuckles creased, veins on the backs of the hands, short unpolished nails.",
     light_line(r, "her knee and hands", "morning daylight through the door glass — the turn, the window side, soft and clean"),
     S("BROLL-REAL"), S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
     "AVOID: " + ", ".join([S("NEG-SUBJ"), S("NEG-PROP"), S("NEG-LIGHT"), S("NEG-M1"), S("NEG-FILE"), PS.fill(PS.NEG_SEAT, side=SIDE),
       PS.NEG_WORDMARK, PS.NEG_ADJUST, "no strap on the left knee, no second strap, no face in frame"])]
    refs = [("front.webp", "products/stryde/stryde_refs/front.webp"), ("back.webp", "products/stryde/stryde_refs/back.webp"),
            ("worn_front.jpg", "products/stryde/stryde_refs/worn_front.jpg"),
            ("C1 sheet", s["sheet_job"]), ("P0-PROP-G plate", "faf039cb-e64f-4a3c-9772-85b0cb5c26f1")]
    return dict(model="nano_banana_pro", refs=refs, face="NOFACE", body=body)
BEATS["A-HKb"] = a_hkb

if __name__ == "__main__":
    out = HERE / "prompts"; out.mkdir(exist_ok=True)
    for b in sys.argv[1:] or BEATS:
        d = BEATS[b](); p = "\n\n".join(d["body"])
        (out / f"{b}.t2i.txt").write_text(p)
        (out / f"{b}.refs.json").write_text(json.dumps(dict(model=d["model"], face=d["face"], refs=d["refs"]), indent=1))
        print(b, d["model"], len(p), "chars", [x[0] for x in d["refs"]])
