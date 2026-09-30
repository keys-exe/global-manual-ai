#!/usr/bin/env python3
"""stryde-what-changed — beat start images (steps 6–7), assembled from Appendix A and the STRYDE Product Sheet by ID.

Mode 1 lifestyle beats: CAM-LOCK → prose (plate, subject, frame caught mid-action) → product blocks → ANGLE-LINE → FOCUS-LINE →
LIGHT-SHOT → COLOUR-KEY → CAP-FILE → AVOID. Anatomy: ANAT-BASE + ANAT-LIGHT + ANAT-FIELD + ANAT-A (Product Sheet ANATOMY_LOOK) +
the beat's state + ANAT_A_POINT_TIGHT. Rows from work/actmap_rows.json.
Usage: beats.py HK1-a HK1-b …  → work/prompts/<beat>.t2i.txt + <beat>.refs.json
"""
import json, re, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
BUILD = HERE.parent
ROOT = BUILD.parents[1]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
sys.path.insert(0, str(ROOT / "products/stryde"))
import stryde_product_sheet as P  # noqa: E402


def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    if not m: raise KeyError(i)
    return m.group(1).strip()


ROWS = {r["beat"]: r for r in json.loads((HERE / "actmap_rows.json").read_text())}

# ── people (identity strings read off the confirmed sheets, BUILD_SHEET §3) ──────────
R1 = ("THE SAME WOMAN exactly as in the attached character sheet of her — a heart-shaped face with a broad forehead and a small pointed chin, "
      "round light-blue eyes, a short straight nose, thin lips, a small dark mole at the corner of her mouth, soft white hair in a short layered crop "
      "lifted at the crown; a white British woman of sixty-nine, short and slight with a small rounded back — unchanged in face, age and build.")
R1_LEGS = "Her legs: thin, pale, faintly freckled older skin, soft creases over bony knees, a few thread veins on the shins, real unretouched skin."
R2 = ("THE SAME MAN exactly as in the attached character sheet of him — a long square-jawed face, deep-set dark eyes, a broad straight nose, "
      "close-cropped grey-white hair and a short grey-white beard; a Black British man of sixty-six, tall, broad-shouldered, strong thighs, "
      "a thickened middle — unchanged in face, age and build.")
WARD = {
    "M-D1": "a dusty-pink cotton cardigan over a navy-and-white striped Breton top, a navy cotton A-line skirt ending just above the knee so both knees are bare, white canvas plimsolls",
    "M-D2": "a sage-green cardigan over a white T-shirt, a mid-blue denim skirt ending just above the knee so both knees are bare, white canvas plimsolls",
    "D-D1": "a navy zip-neck sports top over a white T-shirt, dark grey jogging shorts ending just above the knee so both knees are bare, plain white trainers with navy trim",
    "D-D2": "a burgundy polo shirt, khaki cotton shorts ending just above the knee, plain white trainers with navy trim",
}

# ── places (confirmed plates) ────────────────────────────────────────────────────────
M_STAIRS = ("THE SAME HALL AND STAIRS as the attached house plate: pale duck-egg blue walls, tall white ogee skirting scuffed along the bottom stair, "
            "a worn oatmeal wool carpet on the hall floor and up the stairs, plain white-painted spindles and a honey-coloured oak handrail ending in a "
            "square newel post; the straight flight rises along the RIGHT-hand wall as you face in from the front door, a half-landing window at the top.")
D_STAIRS = ("THE SAME HALL AND STAIRS as the attached house plate: warm mid-grey walls, deep white gloss skirting, a charcoal-grey stair carpet with a "
            "white stripe at each nosing, square white spindles and a dark-stained handrail; black-framed amateur football team photos up the stair wall; "
            "the straight flight rises along the LEFT-hand wall as you face in from the front door.")
STREET = ("THE SAME STREET as the attached location plate: a long grey paving-slab pavement, cracked and patched, low front-garden walls and privet "
          "hedges on one side, parked cars along the kerb, a row of 1930s semis with bay windows going away.")

KITCHEN = ("THE SAME KITCHEN as the attached location plate: a lived-in 1990s British family kitchen, a square pale-oak table with a linen "
           "runner and a jug of garden flowers, sage-green shaker units and a speckled grey worktop, a window over the sink, an open shelf of "
           "mugs and jars.")
LIGHT = {  # source, screen side, quality
    "M-GREY-L": ("the half-landing window at the top of the flight", "left", "grey morning light, soft and indirect from above — the problem state, flat and cool, never moody"),
    "STREET-AM-L": ("the broad overcast morning sky", "left", "flat, grey, cool morning light"),
    "KITCH-L": ("the kitchen window over the sink", "left", "cool overcast daylight, flat and broad"),
    "KITCH-R": ("the kitchen window over the sink", "right", "cool overcast daylight, flat and broad"),
    "M-GREY-R": ("the half-landing window at the top of the flight", "right", "grey morning light, soft and indirect from above — the problem state, flat and cool, never moody"),
    "D-GREY-R": ("the landing window at the top of the flight", "right", "grey morning light, soft and indirect from above — the problem state, flat and cool, never moody"),
    "D-GREY-L": ("the landing window at the top of the flight", "left", "grey morning light, soft and indirect from above — the problem state, flat and cool, never moody"),
}
COLOUR = {
    "M-STAIRS-AM": ("soft grey morning daylight, cool-neutral", "pale duck-egg blue walls, oatmeal carpet, white spindles and skirting, honey oak handrail",
                    "a dusty-pink cardigan, navy-and-white stripes and a navy skirt", "the honey oak handrail", "true to life, slightly muted"),
    "STREET-AM": ("flat overcast morning daylight, cool", "grey paving, green privet, pebble-dash and brick semis", "navy skirt and white plimsolls",
                  "the green privet", "muted"),
    "D-STAIRS-AM": ("soft grey morning daylight, cool-neutral", "warm mid-grey walls, charcoal carpet with white nosing stripes, white spindles and skirting",
                    "a navy zip-neck top, dark grey shorts and white trainers with navy trim", "the white nosing stripes", "true to life, slightly muted"),
}
COLOUR["KITCH-AM"] = ("cool overcast daylight", "pale oak table, linen runner, sage-green units, speckled grey worktop",
                       "a dusty-pink cardigan cuff and a yellowed photo album", "the faded orange of the old photograph", "slightly flat, true to life")
KELVIN = {"KITCH-AM": 6500, "M-STAIRS-AM": 6500, "STREET-AM": 6500, "D-STAIRS-AM": 6500}


def light(key, subj):
    src, side, q = LIGHT[key]
    out = (S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", src)
           .replace("[SUBJECT]", subj).replace("[SCREEN SIDE]", side).replace("[TIME-OF-DAY QUALITY and the act's light state]", q)
           .replace("[SIDE]", "the " + side))
    return out.replace("so the face has a lit side toward the " + side + " and a softer shadow side, with a small catchlight in the eyes",
                       "so it has a lit side toward the " + side + " and a softer shadow side")


def colour(key):
    lc, sc, wc, ac, sat = COLOUR[key]
    s = (S("COLOUR-KEY").replace("[LIGHT COLOUR]", lc).replace("[SET COLOURS]", sc).replace("[WHO] wears [WARDROBE COLOURS]", "the wardrobe is " + wc)
         .replace("[ACCENT]", "the accent is " + ac).replace("[SATURATION AND CONTRAST IN CAMERA]", sat)
         .replace(", exactly as in the attached master frame", ""))
    return s.replace("[KELVIN]", str(KELVIN[key]))


HEIGHT = {"overhead": "an overhead camera looking straight down", "high": "a high camera looking down", "eye": "an eye-level camera",
          "low": "a low camera close to the floor looking up", "ground": "a camera at ground level"}
SIDE = {"front": "the front", "three-quarter": "three-quarter", "profile": "the side, in profile", "three-quarter-back": "three-quarter behind",
        "behind": "directly behind", "ots": "over the shoulder"}


def angle(beat, subj, fg=""):
    a = ROWS[beat]["angle"]
    return (S("ANGLE-LINE").replace("[HEIGHT CLAUSE from §30I]", HEIGHT[a["height"]]).replace("[SIDE]", SIDE[a["side"]]).replace("[SUBJECT]", subj)
            .replace("[, looking past FOREGROUND, soft in the near foreground | , seen in REFLECTION]", fg)
            .replace(", not a straight-on eye-level view", "" if a["height"] == "eye" else ", not a straight-on eye-level view"))


def focus(plane, deep=True):
    return (S("FOCUS-LINE").replace("[PLANE — the nearest eye of NAME / the hands and what they hold / the product and its wordmark / the foreground / everything]", plane)
            .replace("[DEPTH — the room behind falls to a soft, recognisable shape | everything from near to far stays sharp]",
                     "everything from near to far stays sharp" if deep else "the room behind falls to a soft, recognisable shape"))


NEG_BASE = ("no readable text, no logos, no AI face, no plastic skin, no extra fingers, no fused fingers, no extra toes, no polished render, "
            "no advertising image, no studio lighting, no vignette, no glowing skin, no light from nowhere, no shadows falling in two directions, no lens flare")


def photo(parts, avoid):
    body = [S("CAM-LOCK")] + [p for p in parts if p] + [S("CAP-FILE")]
    return "\n\n".join(body + ["AVOID: " + avoid + ", " + NEG_BASE])


ANAT_SLOTS = {"[REGION]": "knee", "[STACK]": "quadriceps, hamstrings and calf", "[BONES]": "femur, patella and tibia",
              "[TARGET]": "the patellar tendon", "[TARGET JOINT]": "the knee joint", "[SITE]": "the patellar tendon immediately below the kneecap"}
ANAT_NEG_T2I = ("no arrows, no force arrows, no motion lines, no diagram markings, no text overlays, no labels, no numbers, no annotations, "
                "no UI, no watermark, no individual muscle fibres, no surface veins, no emission on the bone shafts, no glow on the tibial "
                "tuberosity, no glow spreading down the shin, no second limb, no clothing, no hands, no people, no x-ray look, no flat "
                "illustration, no cartoon look, no vignette, no darkened frame corners, no limb falling off into darkness, no product")


def anat(state, view=None, stack="ANAT-A", slots=None):
    base = S("ANAT-BASE")
    if view:
        base = base.replace("viewed from a low three-quarter angle, foreshortened, [TARGET JOINT] sitting slightly off-centre and dominating the frame", view)
    t = "\n\n".join([base, S("ANAT-LIGHT"), S("ANAT-FIELD"), S(stack), state, "AVOID: " + ANAT_NEG_T2I + ", " + S("NEG-EXTERNAL")])
    for k, v in dict(ANAT_SLOTS, **(slots or {})).items():
        t = t.replace(k, v)
    return t


NBP, NB2 = "nano_banana_pro", "nano_banana_2"
REFS = {"R1": ("R1-MAUREEN sheet", "fd75b478-6a1b-4a8f-ba80-d20f272f65b0"), "R2": ("R2-DESMOND sheet", "9f0903d2-b148-4273-93b6-e4227a87d9f6"),
        "P1": ("P1-PROP-M plate", "520de2e7-e577-4afe-b18c-b79dbed0acf0"), "P2": ("P2-PROP-D plate", "68ddef76-e5b0-4947-966f-cda7e00335c2"),
        "P3": ("P3-STREET plate", "c19e14a9-5146-4444-8b83-e765dfdc3f8f"),
        "P4": ("P4-KITCHEN plate", "0bedfad5-bf20-4ebd-a862-fed90b55601a"),
        "K9": ("B09-BR v1 (the sleeve and brace as already shown)", "f986eef2-5bbd-465a-920b-fd552b19e4e5")}
B = {}  # beat -> (model, [ref keys], prompt)

# ── Hook 1 ──────────────────────────────────────────────────────────────────────────
B["HK1-a"] = (NB2, ["R1", "P1"], photo([
    "A snapshot from a phone held low on the hall floor beside the foot of the stairs, looking side-on at the flight through the open spindle "
    "side. She is coming DOWN her stairs, caught mid-step: her right foot planted flat on the second stair from the bottom and taking her "
    "weight, the right knee bending under the load, her left foot lifting off the step above and already travelling down; her left hand "
    "rests on the oak handrail at hip height. The frame is cropped at her waist — her face is not in the frame; it holds her skirt hem, her "
    "bare knees and shins, her plimsolls and the stair treads.",
    R1 + " Wearing " + WARD["M-D1"] + ". " + R1_LEGS,
    M_STAIRS,
    angle("HK1-a", "her legs on the stairs", ", looking past the white spindles, soft in the near foreground"),
    focus("the foreground", deep=False),
    light("M-GREY-L", "her legs and the stairs"), colour("M-STAIRS-AM")],
    "no face in frame, no product anywhere, no knee strap, no knee support, no walking stick, no stairlift, no second person, "
    "no person going up the stairs, no person sideways on the stairs, no wrong number of legs"))

B["HK1-b"] = (NB2, [], anat(
    "Seen from the side, in profile, the knee mid-stride with the foot planted and the limb carrying the body's weight. "
    + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from the side, in profile, the whole knee joint in the middle of the frame with the thigh above and the shin below"))

# ── Hook 2 ──────────────────────────────────────────────────────────────────────────
# HK2-a v3 — user Fixes "GIVE ME DIFFERENT BROLL" then "I WANT ANATOMY B ROLL HERE": anatomy again, but an ECU of the tendon
# itself as a band (HK1-b is the whole knee in profile with the spot); the glow stays ANAT_A_POINT_TIGHT.
B["HK2-a"] = (NB2, [], anat(
    "Seen from a high three-quarter angle, close in: the lower edge of the kneecap at the top of the frame and, running down from it to "
    "the top of the shin, the patellar tendon laid out as one thick, flat, satin-white band of tissue about the width of the kneecap's "
    "lower edge, its long fibres visible as broad grain running along it, clearly separate from the bone behind it — the band is the "
    "subject and fills the middle of the frame. No thumb, no hand, no ruler, nothing held against it for scale. "
    + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed close from a high three-quarter angle looking down along the front of the knee, the lower kneecap and the tendon below it "
         "filling the frame, the upper shin at the bottom edge"))

# HK2-b v2 — user Fix "GIVE ME DIFFERENT BROLL HERE" (was one step up onto the bottom stair): strength — rising out of a deep squat with a load.
# HK2-b v4 — user Fixes "FIX THIS", "FIX THE BROLL": front-on kept pulling the face in and the box floated with the hands on the knees →
# side-on, cropped at the waist, both hands under the box's bottom corners. No face identity text (legs, skin and build only).
R2_LEGS = ("THE SAME MAN as in the attached character sheet of him — the same dark brown skin, the same tall broad build and strong thighs, "
           "sixty-six years old. His legs and hands: dark brown older skin, strong thighs and calves, a few grey hairs on the shins, ashy knees "
           "with soft creases, thick knuckles, real unretouched skin.")
B["HK2-b"] = (NB2, ["R2", "P2"], photo([
    "A snapshot from a phone held low near the hall floor, side-on to him, about two metres away. He is in his hall by the foot of the stairs, "
    "caught at the bottom of a lift: squatting deep with his feet flat on the floor, both knees bent hard and pushed forward, his thighs "
    "angled down towards the floor, lifting a heavy plain cardboard box off the floor in front of his shins. BOTH HANDS ARE UNDER THE BOX — "
    "his fingers hooked under its two bottom corners, his forearms along its sides, the box just clear of the floor, tight in against his "
    "shins. THE FRAME IS CROPPED AT HIS WAIST: the top edge crosses at his waistband, so his chest, shoulders, head and face are all above "
    "the frame and not in the picture. The frame holds his waistband, his hands and forearms, the box, his shorts, his bent right knee "
    "nearest the lens in clear side profile, both shins, his trainers, the bottom stairs behind him and the hall floor.",
    R2_LEGS + " Wearing dark grey jogging shorts ending just above the knee so the knee is bare, the hem of a navy zip-neck top at his "
    "waist, and PLAIN white leather trainers with navy laces and a plain navy heel tab — no logo, no stripe, no swoosh, no brand mark.",
    D_STAIRS + " A plain unmarked brown cardboard box, taped shut, no writing, no labels, no marker pen on any side.",
    angle("HK2-b", "his bent right knee and the box"),
    focus("his right knee", deep=False),
    light("D-GREY-L", "his knee and the box"), colour("D-STAIRS-AM")],
    "no face in frame, no head, no chin, no beard, no chest, no shoulders in frame, no product anywhere, no knee strap, no knee support, "
    "no writing on the box, no words, no letters, no logos on the trainers, no Nike swoosh, no brand marks, no stripes on the trainers, "
    "no box floating, no hands resting on the knees, no box between the legs, no box held at the chest, no standing upright, no half squat, "
    "no second person, no wrong number of legs, no extra hands, no posterised colour, no banding"))

# ── Hook 3 ──────────────────────────────────────────────────────────────────────────
# Faceless beats carry no face identity text (HK2-b lesson: face text pulls the face into frame).
R1_BODY = ("THE SAME WOMAN as in the attached character sheet of her — the same pale, faintly freckled older skin, the same short slight build "
           "and thin legs, sixty-nine years old.")
B["HK3-a"] = (NB2, ["R1", "P3"], photo([
    "A snapshot from a phone lying almost on the pavement, pointing along it, at ground level. She is walking along the pavement straight "
    "towards the lens at an ordinary pace, about two metres away, caught mid-stride: her right foot planted flat on a paving slab and "
    "taking her weight, the right knee bending a little under it, her left foot lifting off behind at the heel. THE FRAME IS CROPPED AT "
    "HER WAIST — her body above the waist, her head and face are above the frame and not in the picture. It holds her skirt hem, both "
    "bare knees and shins, her plimsolls, the paving slabs running away behind her, the low garden walls and hedges on one side and the "
    "parked cars on the other going soft into the distance.",
    R1_BODY + " " + R1_LEGS + " Wearing a navy cotton A-line skirt ending just above the knee so both knees are bare, and white canvas "
    "plimsolls, plain, no logo.",
    STREET,
    angle("HK3-a", "her feet and knees coming towards the lens"),
    focus("her planted right foot and knee", deep=False).replace("the room behind", "the street behind"),
    light("STREET-AM-L", "her legs and the pavement"), colour("STREET-AM")],
    "no face in frame, no head, no torso above the waist, no product anywhere, no knee strap, no knee support, no walking stick, no dog, "
    "no second person, no house numbers, no readable signs, no number plates, no logos on the plimsolls, no wrong number of legs"))

# HK3-b v3 — user Fix "ANATOMY BROLL HERE" (after the worn-stairs v2): anatomy, a look not used yet — low front three-quarter,
# the knee bent mid-step as the foot lands, the one spot hot.
B["HK3-b"] = (NB2, [], anat(
    "Seen from a low front three-quarter angle, close: the knee bent under a landing step, the foot below it just striking the ground out of frame and the "
    "thigh above angled forward, the whole weight of the body coming down through the joint. The kneecap sits in the upper middle of the "
    "frame and the spot just below it is the hottest point in the picture. " + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from a low front three-quarter angle looking up at the bent knee, the joint large in the middle of the frame, the lower "
         "thigh above and the shin angling down towards the landing foot"))

# ── Act 1 (step 7 body B-roll) ─────────────────────────────────────────────────────────
# Faceless beats carry no face identity text; beats that show the face carry R1 / R2 in full. Plain trainers, no writing.
R2_BODY = ("THE SAME MAN as in the attached character sheet of him — the same dark brown skin, the same tall broad build and strong thighs, "
           "sixty-six years old. His legs: dark brown older skin, strong calves, a few grey hairs on the shins, ashy knees with soft creases, "
           "real unretouched skin.")
PLAIN_SHOES = "no logos on the shoes, no swoosh, no stripes, no brand marks"
NO_FACE = "no face in frame, no head"

# B01a — "That band is the patellar tendon." ANAT-B ghost limb: bones and the tendon only (a look no hook used).
B["B01a"] = (NB2, [], anat(
    "Seen from eye level, three-quarter front, close: the knee straight and standing, the kneecap in the upper third and the patellar "
    "tendon running down from its lower edge to the top of the shin as one clear pearly band — the one structure the eye goes to. "
    + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from eye level, three-quarter front, the knee joint large in the middle of the frame with the lower thigh above and the "
         "upper shin below", stack="ANAT-B", slots={"[STACK]": "the surrounding soft tissue"}))

# B01b v2 — user "PUT DIFFERENT BROLLS HERE": the line split in two. First half — where it is: the ridge under the skin, front on.
B["B01b"] = (NB2, ["R2", "P2"], photo([
    "A snapshot from a phone held at knee height just in front of him. He stands in his hall with his weight on his right leg, the bare "
    "right knee straight and nearest the lens. Very close, straight on to the front of the knee: the kneecap in the upper part of the frame "
    "and, just below it, the band of the tendon standing out under the skin as a firm vertical ridge running down to the top of the shin, "
    "catching the light along its edge. The frame holds only the knee from the bottom of the shorts hem to the upper shin.",
    R2_BODY + " Wearing dark grey jogging shorts ending just above the knee.",
    D_STAIRS,
    angle("B01b", "his bare right knee"),
    focus("the ridge just below his kneecap", deep=False).replace("the room behind", "the hall behind"),
    light("D-GREY-L", "his knee"), colour("D-STAIRS-AM")],
    NO_FACE + ", no torso, no hands, no product anywhere, no knee strap, no knee support, no marks drawn on the skin, no ruler, "
    "no tape measure, no second person, no wrong number of legs"))

# B01c — second half: "and every step you take lands on it." Maureen stepping down off a kerb, ground level, side-on.
B["B01c"] = (NB2, ["R1", "P3"], photo([
    "A snapshot from a phone lying on the road surface at the kerb, side-on. She is stepping down off the pavement kerb onto the road, "
    "caught at the landing: her right plimsoll just landed flat on the tarmac, the right knee bending as it takes her weight, her left "
    "foot still up on the kerb behind. The frame holds her feet, shins and bare knees and the skirt hem — nothing above the hem — with "
    "the grey kerb stone, the pavement slabs and the road surface.",
    R1_BODY + " " + R1_LEGS + " Wearing a navy cotton A-line skirt ending just above the knee and white canvas plimsolls, plain, no logo.",
    STREET,
    angle("B01c", "her feet stepping down off the kerb"),
    focus("her landing plimsoll", deep=False).replace("the room behind", "the street behind"),
    light("STREET-AM-L", "her legs and the kerb"), colour("STREET-AM")],
    NO_FACE + ", no torso, no product anywhere, no knee strap, no walking stick, no second person, no cars moving, no road markings with "
    "text, no number plates, no logos on the plimsolls, no wrong number of legs"))

# B02 — "That is the one." Maureen on her bottom stair, fingertip just below her kneecap.
B["B02"] = (NB2, ["R1", "P1"], photo([   # v3 — user Fixes: v1 finger above the kneecap; v2 side-on, finger on the side of the knee →
    # "SHOW THE FRONT OF THE KNEE POINTING THE 'BELOW KNEECAP / KNEE TENDON'": front-on, fingertip on the midline tendon.
    "A snapshot from a phone held at knee height directly in front of her, square on to the FRONT of her knee. She sits on the bottom "
    "stair of her hall with her right foot flat on the hall floor and her bare right knee bent, the knee facing straight at the lens. The "
    "front of the knee fills the middle of the frame: the round kneecap centred and facing the camera, and straight below it, on the front "
    "midline of the leg, the tendon running down to the bony bump at the top of the shin. Her right index finger points straight at that "
    "tendon and rests on it, just under the bottom edge of the kneecap, in the middle of the front of the leg — the fingertip below the "
    "kneecap, centred, clearly on the front, not at the side. Close: the frame holds the front of her knee, the kneecap, the fingertip on "
    "the tendon, her hand, the navy skirt hem at the top edge — her face is not in the frame.",
    R1_BODY + " Her hands: slim older hands, thin skin over the knuckles, a plain gold wedding ring. " + R1_LEGS
    + " Wearing a navy cotton A-line skirt ending just above the knee.",
    M_STAIRS,
    angle("B02", "her bent right knee"),
    focus("her fingertip on the tendon below the kneecap", deep=False).replace("the room behind", "the stairs behind"),
    light("M-GREY-R", "her knee and hand"), colour("M-STAIRS-AM")],
    NO_FACE + ", no side view of the knee, no profile, no finger at the side of the knee, no finger above the kneecap, no finger on the "
    "thigh, no finger on the kneecap, no product anywhere, no knee strap, no knee support, no second person, no extra fingers, "
    "no wrong number of hands"))

# B04a v2 — user Fix "NEGATIVE BROLL, STRUGGLING TO Going up the stairs.": Desmond struggling up, face in frame.
B["B04a"] = (NB2, ["R2", "P2"], photo([
    "A snapshot from a phone at eye height in the hall, three-quarter on to the stairs. He is part-way up his stairs, struggling: his "
    "right hand gripping the dark handrail hard, his left hand pressed flat on his left thigh pushing down to lever himself up onto the "
    "next tread, his body leaning forward over the bent knee, his mouth set and his brow drawn with effort — tired, not in agony. "
    "Medium shot, the whole of him from head to the treads below his feet.",
    R2 + " Wearing " + WARD["D-D1"] + ".",
    D_STAIRS,
    angle("B04a", "him struggling up the stairs"),
    focus("his nearest eye", deep=False).replace("the room behind", "the stair wall behind"),
    light("D-GREY-R", "him and the stairs"), colour("D-STAIRS-AM")],
    "no crying, no screaming, no falling, no looking at the camera, no product anywhere, no knee strap, no walking stick, no second person, "
    + PLAIN_SHOES + ", no going down the stairs"))

# B04b v4 — user Fix "HIGHER LAYER IN STAIR, STRUGGLING A LITTLE BIT" (v3 halfway); v3 — user Fix "SHE'S GOING DOWN THE STAIR, NOT YET AT THE LAST STEP" (v2 near the bottom); v2 — user Fix "GOING DOWN WHILE HOLDING THE BANISTER, CHANGE THE BROLL": Maureen coming down towards the lens, gripping the rail.
B["B04b"] = (NB2, ["R1", "P1"], photo([
    "A snapshot from a phone held on the lower stairs, looking up the flight. She is NEAR THE TOP OF HER STAIRS, just a few treads below "
    "the half-landing, coming DOWN towards the lens, struggling a little: her right hand gripping the honey oak handrail tightly, her left "
    "hand braced flat against the wall for support, her weight held back, her right foot lowering carefully onto the next tread while the "
    "left knee bends to take her, her face showing a small tired wince of effort — uncomfortable, not in agony. Most of the flight lies "
    "empty below her between her and the lens; the half-landing window is just above and behind her. The whole of her from head to "
    "plimsolls.",
    R1 + " Wearing " + WARD["M-D1"] + ".",
    M_STAIRS,
    angle("B04b", "her coming down the stairs"),
    focus("her face and her hand on the rail", deep=False).replace("the room behind", "the stairs behind"),
    light("M-GREY-L", "her and the stairs"), colour("M-STAIRS-AM")],
    "no falling, no wincing in agony, no looking at the camera, no product anywhere, no knee strap, no walking stick, no stairlift, "
    "no second person, no logos on the plimsolls, no going up the stairs, no standing on the bottom step, no standing on the hall floor"))

# B04c v2 — user Fix "WALKING DOWN THE STAIR": the silhouette figure, waist-down, walking down a visible flight of steps.
B["B04c"] = (NB2, [], anat(
    "Seen from a high three-quarter angle: a translucent anatomical figure from the waist down WALKING DOWN A SHORT FLIGHT OF STAIRS — "
    "four or five simple dark translucent steps descending across the frame, faintly edge-lit so each step reads clearly. The figure is "
    "caught mid-stride going down: the trailing foot on the upper step, the leading foot just landing flat on the step below, that knee "
    "bent to catch the body's weight; both legs are dark translucent silhouettes with only the patellar tendon legible inside the leading "
    "knee, glowing where the landing loads it. " + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from a high three-quarter angle, a figure from the waist down walking down a short flight of steps, both legs in frame, "
         "the leading knee in the middle of the frame", stack="ANAT-C", slots={"[STACK]": "the surrounding soft tissue"})
    .replace("A stylised anatomical model of a single knee", "A stylised anatomical model of a figure from the waist down")
    .replace("no second limb, ", "").replace("no people, ", "")
    .replace(", the limb falling away out of frame at both ends", ", the feet on the steps"))

# B05 — cartilage thins. ANAT-B ghost limb, the joint cut away, target = the cartilage. No glow — a condition beat.
B["B05"] = (NB2, [], anat(
    "Seen from the side, in profile, the joint opened in a clean cutaway: the rounded end of the femur above, the flat top of the tibia "
    "below, and between them the smooth pale cartilage layer lining both bone ends — pearly, slightly translucent, visibly thinner at the "
    "front of the joint where the load lands than at the back. Calm, no glow, no emission; the thinning reads by thickness alone.",
    view="viewed from the side, in profile, the knee joint large in the middle of the frame, cut away cleanly so the inside of the joint "
         "is visible", stack="ANAT-B",
    slots={"[TARGET]": "the cartilage lining the joint surfaces"}).replace("the patellar tendon crisp", "the cartilage crisp"))

# B06 v6 — user Fix 'ADD MORE EFFECT' (on v5): five wave-fronts, energy threads, heat glow, big impact burst.
# B06 v5 — "Seventeen times your bodyweight is still arriving, every step," User 'MORE EFFECTS, MAKE IT 2 BROLLS HERE' (v4: force
# arrows down the thigh + pointer; confirmed, two videos made). Now the first half of the line: the whole leg mid-step, glowing waves of
# force pouring down through the thigh INSIDE the limb and bursting as a bright ripple at the tendon spot. Effects stay inside the body.
EFX_OK = lambda s: (s.replace("no shockwave, no burst, ", "").replace("no arrows, no force arrows, ", "")
                     .replace("no volumetric emission floating outside the structures, ", "")
                     .replace("no sparks, ", "").replace("no explosion, ", "")
                     .replace("mid-intensity and clearly glowing — not at peak, leaving headroom to escalate", "at full, blazing intensity")
                     .replace(", sharp-edged and small, never spreading down onto the shin bone or across the joint; the bones and muscles around it stay calm", ", the centre of all the effects"))
# B06 v7 — user Fix 'REROLL THIS IMAGE / FOCUS ON THE KNEE / CLOSE UP / ADD MORE EFFECTS' (v6: the whole leg mid-step). Now a
# close-up of the knee joint itself, low three-quarter, under a step's load, with more effects — all inside the limb. Pip kept.
B["B06"] = (NB2, [], EFX_OK(anat(
    "Seen from a low three-quarter angle, CLOSE UP ON THE KNEE: the knee joint fills most of the frame — the lower thigh entering from "
    "the top, the kneecap, the patellar tendon as a taut banded ribbon, the top of the shin leaving at the bottom — flexed and taking a "
    "step's full load, in rich anatomical detail with fine striation on the quadriceps tendon and the worn thin cartilage in the joint. "
    "THE EFFECTS, BOLD AND DRAMATIC, ALL AROUND THE KNEE: brilliant white-gold wave-fronts of force pour down through the lower thigh "
    "into the joint, one behind another, each trailing a streaming glow; bright threads of energy race along the tendon fibres; a hot "
    "red-orange heat glow floods the joint space; and at the patellar tendon just below the kneecap a big impact flare BURSTS — a "
    "blazing white core, four wide rings of light rippling out through the tendon and the translucent tissue, arcs of light "
    "crackling across the joint surfaces, and a swirl of hundreds of glowing particles spinning around the knee inside the body shell. "
    "All of the light lives INSIDE the leg: nothing flies in from outside. The knee sits slightly right of centre; the lower-left corner "
    "stays calm, empty field (a person will be placed there later). "
    + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from a low three-quarter angle, close up on the knee joint, which fills most of the frame slightly right of centre")
    .replace("no individual muscle fibres, ", "").replace("never fine striation and never individual fibres", "fine striation readable")))

# B06b v2 — user Fix 'ADD MORE EFFECT': five rings, fibre streaks, heat halo, particle swirl.
# B06b — "in exactly the same place." (second half of the B06 line). ECU front-on of the patellar tendon just below the kneecap: one
# tight glowing target spot, concentric rings of light rippling out through the tendon fibres as each impact lands on the same point.
B["B06b"] = (NB2, [], EFX_OK(anat(
    "Seen straight from the front, very close: the lower edge of the kneecap at the top of the frame and the patellar tendon below it as "
    "a broad satin-white band of long fibres filling the frame. Dead centre on the tendon, just below the kneecap: ONE BLAZING "
    "NEAR-WHITE CORE, like the bullseye of a target, and around it FIVE bold CONCENTRIC RINGS OF LIGHT rippling outward through the "
    "tendon fibres — the marks of impact after impact landing on exactly the same point. Bright streaks of light race along the tendon "
    "fibres into the core, a hot red-orange heat halo pulses around it, and a swirl of hundreds of glowing particles circles the spot "
    "inside the tissue, the brightest, most dramatic thing in the frame. All of the light lives INSIDE the tendon and the tissue: nothing flies in from outside. "
    + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed straight from the front, very close on the patellar tendon just below the kneecap, the tendon filling the frame")
    .replace("no individual muscle fibres, ", "").replace("never fine striation and never individual fibres", "fine striation readable")))

# B07-BRa — user "The cushion gets thinner. (CUSHION IN KNEE GETS THINNER)". ANAT-B, front-on and closer than B05 (profile cutaway):
# the cartilage cushion in the joint gap, visibly thin. No glow — a condition beat.
B["B07-BRa"] = (NB2, [], anat(
    "Seen straight from the front, close in on the gap between the thigh bone and the shin bone: the rounded ends of the femur above and "
    "the flat top of the tibia below, and between them THE CUSHION — the smooth, pearly, slightly translucent cartilage pad lining both bone "
    "ends and the two crescent menisci at its edges. The cushion is visibly THIN and worn: a narrow pale band, frayed and slightly rough at "
    "its surface, patchy where it has worn furthest, so the two bone ends sit close together with only a sliver of cushion between them. "
    "The joint gap and the thin cushion fill the middle of the frame. Calm, no glow, no emission; the thinning reads by thickness alone.",
    view="viewed straight from the front, close in, the knee joint gap large in the middle of the frame, cut away cleanly so the cushion "
         "between the bones is visible", stack="ANAT-B",
    slots={"[TARGET]": "the cartilage cushion between the bones"}).replace("the patellar tendon crisp", "the cartilage cushion crisp"))

# B07-BRb — user "The weight stays exactly the same. MAKE ME A BROLL HERE". Maureen, faceless, low front at the foot of her stairs,
# coming down with a full laundry basket on her hip: the whole weight landing on the knee. Replaces the planned worn-plimsoll shot.
B["B07-BRb"] = (NB2, ["R1", "P1"], photo([
    "A snapshot from a phone held low at the foot of her stairs, pointing up the flight, from the front. She is coming DOWN her stairs "
    "towards the lens carrying a full plastic laundry basket of folded towels on her left hip, her right hand on the oak handrail, caught "
    "mid-step: her right foot landing flat on the tread nearest the lens and taking her whole weight, the right knee bending under it, her "
    "left foot still on the tread above. THE FRAME IS CROPPED AT HER WAIST — her face and head are above the frame and not in the picture. "
    "It holds the bottom of the basket at her hip, her skirt hem, both bare knees and shins, her plimsolls and the treads.",
    R1_BODY + " " + R1_LEGS + " Wearing " + WARD["M-D1"] + ".",
    M_STAIRS,
    angle("B07-BRb", "her knees and feet coming down the stairs"),
    focus("her landing right foot and knee", deep=False).replace("the room behind", "the stairs behind"),
    light("M-GREY-L", "her legs and the stairs"), colour("M-STAIRS-AM")],
    "no face in frame, no head, no product anywhere, no knee strap, no knee support, no walking stick, no stairlift, no second person, "
    "no going up the stairs, no falling, no readable labels on the basket, " + PLAIN_SHOES + ", no wrong number of legs, no extra hands"))

# B07 v2 — "That is why it feels like it arrived overnight." User Fix 'GIVE ME DIFFERENT BROLL HERE' (v1: top of her stairs, stopping).
# First thing in the morning in her kitchen: she half-rises from the table and stops, hand to her knee, a small surprised frown.
B["B07"] = (NB2, ["R1", "P4"], photo([
    "A snapshot from a phone at eye height across her kitchen table, three-quarter on, first thing in the morning. She is half-risen from "
    "her chair at the pale-oak table, a cup of tea and a plate with a slice of toast in front of her, and has stopped partway up: one hand "
    "on the table edge, the other pressed to the front of her right knee, looking down at it with a small puzzled frown — not pain, just "
    "surprise, as if it was fine yesterday. Medium close-up from the waist up with her hand on her knee in frame at the bottom edge.",
    R1 + " Wearing " + WARD["M-D1"] + ".",
    KITCHEN,
    angle("B07", "her at the kitchen table"),
    focus("her nearest eye", deep=False).replace("the room behind", "the kitchen behind"),
    light("KITCH-L", "her face and hands"), colour("KITCH-AM").replace("a dusty-pink cardigan cuff and a yellowed photo album", "a dusty-pink cardigan and a navy-and-white striped top")
    .replace("the faded orange of the old photograph", "the jug of garden flowers")],
    "no crying, no wincing, no grimace, no product anywhere, no knee strap, no walking stick, no second person, no looking at the camera, "
    "no readable text, no logos on the mug"))

# B08a v4 — "Some of the people it happens to have never run a mile in their life." User Fix 'CREATE NEW IMAGE FOR THIS LINE'
# (v1 keys; v2 tartan trolley; v3 unworn trainers). Maureen seated at the bus stop on her street, handbag on her lap. Face in frame.
B["B08a"] = (NB2, ["R1", "P3"], photo([
    "A snapshot from a phone at eye height on the pavement, three-quarter on to a plain bus shelter on her street. She sits on the "
    "shelter bench waiting for the bus, her handbag on her lap with both hands resting on it, knees together, feet side by side, calm and "
    "still, glancing up the road for the bus — an ordinary, unhurried, unsporty life. Medium shot, the whole of her seated, the shelter "
    "around her and the pavement and houses beyond.",
    R1 + " Wearing " + WARD["M-D1"] + ".",
    STREET + " A plain bus shelter with a bench and a post, no adverts, no signs, no timetable text.",
    angle("B08a", "her seated at the bus stop"),
    focus("her nearest eye", deep=False).replace("the room behind", "the street behind"),
    light("STREET-AM-L", "her and the shelter"), colour("STREET-AM").replace("navy skirt and white plimsolls", "a dusty-pink cardigan, a navy skirt and white plimsolls")],
    "no running, no sports clothes, no product anywhere, no knee strap, no walking stick, no second person, no bus, no looking at the "
    "camera, no readable text, no adverts, no timetable, no number plates, no readable signs"))

# B08b v7 — "Others played sport for thirty years." User Fix 'POV ANGLE' on v6 (him holding the old team photo, three-quarter).
# POV from his own eyes, seated on his stairs: his hands hold the old faded 1980s team photo, his bare knees below. Faceless.
B["B08b"] = (NB2, ["R2", "P2"], photo([
    "A point-of-view snapshot, as if through his own eyes, looking down from where he sits on his stairs. His two hands hold an old, "
    "faded colour photograph out in front of him: a 1980s amateur football team posed in two rows on a muddy park pitch in plain "
    "navy-and-white kit, a young Black man with a short afro in the front row among them. The corners of the print are soft and curled, "
    "his thumb resting at its edge. Below the photo, his own bare knees and dark grey shorts, and further down the charcoal stair carpet "
    "with its white nosing stripe and his white trainers on the step below. His face is not in the frame — we are seeing through his eyes.",
    R2_BODY + " His hands: dark brown older skin, thick knuckles, real unretouched skin, the cuffs of a navy zip-neck sports top at the "
    "wrists. Wearing dark grey jogging shorts ending just above the knee.",
    D_STAIRS,
    angle("B08b", "his hands, the photo and his knees").replace("seen from the front of", "looking straight down at"),
    focus("the photograph", deep=False).replace("the room behind", "the stairs below"),
    light("D-GREY-R", "his hands and the photo"), colour("D-STAIRS-AM")],
    NO_FACE + ", no product anywhere, no knee strap, no readable text, no writing on the photo, no names, no dates, no badges, no logos, "
    + PLAIN_SHOES + ", no extra fingers, no extra hands, no extra knees"))

# B08c v3 — "It is coming from standing up and walking." User Fix 'CHANGE TO FROM SITTING TO STAND UP AND WALK, OUTSIDE' (v1 Desmond
# rising off his stair; v2 Maureen rising from her kitchen chair). Desmond on his street, pushing up from a low front-garden wall.
B["B08c"] = (NB2, ["R2", "P3"], photo([
    "A snapshot from a phone at eye height on the pavement, three-quarter on. He has been sitting on a low brick front-garden wall and is "
    "getting up to walk on, caught halfway: his weight coming forward over his feet, one hand pushing off the top of the wall, both bare "
    "knees bent and straightening as they take his weight, his face three-quarter to the camera, looking ahead up the pavement, "
    "matter-of-fact. Medium shot, the whole of him from head to trainers, the wall and hedge behind him and the pavement running away.",
    R2 + " Wearing " + WARD["D-D1"] + ".",
    STREET,
    angle("B08c", "him getting up off the wall"),
    focus("his nearest eye", deep=False).replace("the room behind", "the street behind"),
    light("STREET-AM-L", "him and the pavement"), colour("STREET-AM").replace("navy skirt and white plimsolls", "a navy zip-neck top, dark grey shorts and white trainers")],
    "no wincing, no pain face, no product anywhere, no knee strap, no walking stick, no second person, no looking at the camera, no "
    "readable text, no number plates, " + PLAIN_SHOES + ", no wrong number of legs"))

# B08-BR2 — "It makes almost no difference," (user 'BROLLS HERE', first half of B08-TH2). Desmond's hand sets his old muddy football
# boots down on the shoe rack by his front door. Faceless close-up.
B["B08-BR2"] = (NB2, ["R2", "P2"], photo([
    "A snapshot from a phone held above, looking down at the shoe rack by his front door. His hand sets a pair of old black leather "
    "football boots down on the rack, dried mud on the studs and caked along the soles, the leather creased and scuffed from years of "
    "Saturdays. Close-up: his hand and the boots fill the frame, the wooden rack and a doormat below, the white front door frame at the edge.",
    "His hand: THE SAME MAN as in the attached character sheet — dark brown older skin, thick knuckles, real unretouched skin, the cuff of "
    "a navy zip-neck sports top at the wrist.",
    D_STAIRS,
    angle("B08-BR2", "his hand and the boots"),
    focus("his hand and the boots", deep=False).replace("the room behind", "the floor below"),
    light("D-GREY-L", "his hand and the boots"), colour("D-STAIRS-AM").replace("a navy zip-neck top, dark grey shorts and white trainers with navy trim", "old black boots and dried brown mud")],
    NO_FACE + ", no person beyond his hand, no product anywhere, no readable text, no logos on the boots, no stripes on the boots, no "
    "swoosh, no brand marks, no second hand, no extra fingers"))

# B08-BR3 — "because the load is not coming from what you did." (second half of B08-TH2). Floor level, side-on: Maureen's plimsoll
# steps over her front doorstep, the bare knee above bending as it takes her weight. Faceless.
B["B08-BR3"] = (NB2, ["R1", "P1"], photo([
    "A snapshot from a phone lying on the hall floor by the open front door, side-on, at floor level. She is stepping out over her front "
    "doorstep: her right plimsoll just landing on the step outside, her bare right knee above it bending as it takes her weight, her left "
    "foot still on the hall carpet behind. Close: the frame holds her feet, shins and the knee — nothing above the knee — with the "
    "painted doorstep, the threshold strip and the path beyond going soft.",
    R1_BODY + " " + R1_LEGS + " Wearing white canvas plimsolls, plain, no logo, and the hem of a navy skirt just visible above the knee.",
    M_STAIRS + " The white front door with its glass panel stands open onto a short front path.",
    angle("B08-BR3", "her step over the doorstep"),
    focus("her landing plimsoll and knee", deep=False).replace("the room behind", "the path beyond"),
    light("M-GREY-R", "her legs and the doorstep"), colour("M-STAIRS-AM")],
    NO_FACE + ", no torso, no product anywhere, no knee strap, no walking stick, no second person, no readable text, no house number, "
    "no logos on the plimsolls, no wrong number of legs"))

# B03-BR — covers B03-TH "It is not a big thing … since you were a teenager." (user: "BROLL HERE"). F2: no thumb shown against anything.
B["B03c"] = (NB2, ["R1", "P4"], photo([   # was B03-BR; now the third part of the B03 line
    "A snapshot from a phone held straight above the kitchen table, looking down. A family photo album lies open on the pale-oak table, "
    "its thick card pages yellowed, a few old colour photographs held in by corner mounts. The main photograph, faded to warm oranges and "
    "soft blues the way 1970s prints fade: a teenage girl of about fifteen with white-blonde hair mid-stride along a seaside promenade in "
    "summer, laughing, bare legs, sandals, the sea wall and railings behind her. An older woman's hand rests on the edge of the page, "
    "about to turn it. Close: the frame holds the open album, the photographs and her hand — nothing else of her.",
    "Her hand: THE SAME WOMAN as in the attached character sheet — slim, pale, faintly freckled older skin, thin skin over the knuckles, a "
    "plain gold wedding ring, the dusty-pink cardigan cuff at the wrist.",
    KITCHEN,
    angle("B03c", "the open album"),
    focus("the teenage girl's photograph", deep=False).replace("the room behind", "the table around it"),
    light("KITCH-L", "the album and her hand"), colour("KITCH-AM")],
    "no thumb held against anything, no measuring, no readable text, no handwriting, no captions, no dates, no names, no logos, no face of "
    "the older woman, no second hand, no extra fingers, no product anywhere, no knee strap"))

# B03a — "It is not a big thing. It is about as wide as your thumb," (user: "PUT DIFFERENT BROLLS HERE"): how small the band is
# next to the thigh muscle above it. F2: no thumb, nothing held against it.
B["B03a"] = (NB2, [], anat(
    "Seen from a low front angle, standing: the big quadriceps muscle of the thigh fills the upper half of the frame, broad and heavy, and "
    "narrows down over the kneecap into the one small band of the patellar tendon below it — the size difference is the picture: the huge "
    "muscle above, the slim band below carrying what it sends down. No thumb, no hand, no ruler, nothing held against it for scale. "
    + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from a low front angle looking up the standing leg, the whole thigh above and the knee in the lower middle of the frame, "
         "the upper shin at the bottom edge"))

# B03b — "and it has been quietly taking your whole bodyweight, multiplied," Maureen lifting a heavy pot from a low cupboard.
B["B03b"] = (NB2, ["R1", "P4"], photo([
    "A snapshot from a phone at eye height in the kitchen, three-quarter on to her. She is bending at the knees in front of a low sage-green "
    "cupboard, caught as she starts to rise with a heavy orange cast-iron casserole pot held in both hands, her knees deeply bent and "
    "pushed forward and taking the load, her back fairly straight, her face turned down towards the pot in three-quarter profile. Medium "
    "shot, the whole of her from head to plimsolls, the open cupboard door beside her.",
    R1 + " Wearing " + WARD["M-D1"] + ".",
    KITCHEN,
    angle("B03b", "her lifting the pot"),
    focus("everything", deep=True),
    light("KITCH-L", "her and the cupboard"), colour("KITCH-AM").replace("a dusty-pink cardigan cuff and a yellowed photo album", "a dusty-pink cardigan, navy-and-white stripes and a navy skirt").replace("the faded orange of the old photograph", "the orange cast-iron pot")],
    "no looking at the camera, no wincing, no pain face, no product anywhere, no knee strap, no second person, no brand name on the pot, "
    "no readable text, no logos, no extra hands"))

# B06-BR — "It happens to everybody." (user: "2 OR 3 PEOPLE HAVING PROBLEM IN THEIR KNEE", "NOT SAME AGE") — three one-off extras of
# different ages at a bus stop, each with knee trouble.
B["B06-BR"] = (NB2, ["P3"], photo([
    "A snapshot from a phone at eye height on the pavement, three-quarter on to a bus stop on the same residential street. Three people of "
    "clearly DIFFERENT AGES, each with trouble in a knee, none of them looking at the lens: on the shelter bench, a white-haired white "
    "British man in his mid-seventies in a grey anorak sits forward rubbing his right knee with both hands; beside the shelter, a Black "
    "British woman in her mid-forties in a camel coat with a work bag on her shoulder leans one hand on the shelter post and eases her "
    "weight off her left knee, lifting that foot slightly; and in the foreground, a young South Asian British man of about twenty-five in "
    "running tights, shorts and a light running jacket walks past with a slight limp, one hand pressed on his thigh above the knee. "
    "Ordinary, unposed, a grey weekday morning. Medium shot, all three in frame, the pavement and the bus shelter around them.",
    STREET + " A plain bus shelter with a bench and a post, no adverts, no signs, no timetable text.",
    angle("B06-BR", "the three people at the bus stop"),
    focus("everything", deep=True),
    light("STREET-AM-L", "the three people and the bus stop"),
    colour("STREET-AM").replace("navy skirt and white plimsolls", "a grey anorak, a camel coat and dark running kit")],
    "no three people of the same age, no looking at the camera, no one in obvious agony, no crying, no walking sticks, no wheelchairs, "
    "no knee straps, no knee supports, no product anywhere, no adverts, no readable signs, no timetable, no bus, no number plates, "
    "no logos, no brand marks on the running kit, no more than three people, no children"))

# B09-BR — "Which is why most of what gets sold for this cannot work." (user 'BROLL HERE', covers B09-TH). Maureen's kitchen table:
# the things she has tried, laid out together; her hand sets the last one down. All plain and unbranded (F6); nothing like a strap.
B["B09-BR"] = (NB2, ["R1", "P4"], photo([
    "A snapshot from a phone held up high, looking down at an angle at the pale-oak kitchen table. Laid out together on it, the things "
    "she has tried for her knee: a plain grey knit knee sleeve, a bulky black hinged knee brace with metal side hinges, a plain white "
    "tube of gel with no label, and a plain silver blister pack of white tablets. Her hand is just setting the blister pack down beside "
    "the others. Medium shot: the four things and her hand fill the middle of the frame, the edge of the table, the linen runner and the "
    "sage-green units behind.",
    "Her hand: THE SAME WOMAN as in the attached character sheet — slim, pale, faintly freckled older skin, thin skin over the knuckles, "
    "a plain gold wedding ring, the dusty-pink cardigan cuff at the wrist.",
    KITCHEN,
    angle("B09-BR", "the things on the table"),
    focus("everything", deep=True),
    light("KITCH-L", "the table and her hand"), colour("KITCH-AM").replace("a dusty-pink cardigan cuff and a yellowed photo album", "a dusty-pink cardigan cuff, a grey sleeve, a black brace and a white tube").replace("the faded orange of the old photograph", "the black brace")],
    NO_FACE + ", no person beyond her hand, no product anywhere, no knee strap, no strap of any kind, no readable text, no labels, "
    "no brand names, no logos, no pharmacy boxes, no printing on the blister pack, no second hand, no extra fingers"))

# B10a — "A sleeve squeezes the whole knee and leaves that band carrying everything." v2 (user 'GIVE ME DIFFERENT IMAGE HERE'; v1 was
# the overhead lap view, the sleeve sitting like a cap). Low, front-on CU: Maureen standing in her kitchen, the same grey sleeve (as in
# B09-BR) already on, snug round the whole knee; her hands press it flat round the joint. Faceless.
B["B10a"] = (NB2, ["R1", "P4", "K9"], photo([
    "A snapshot from a phone held low, at knee height, straight in front of her as she stands on the kitchen floor. She is wearing a "
    "plain grey knit knee sleeve on her right leg, pulled on fully: it wraps the WHOLE knee as one even tube, from just above the knee "
    "on the lower thigh down over the kneecap to just below it on the upper shin, snug and squeezing evenly all the way round, the knit "
    "stretched smooth over the kneecap. Both her hands rest on it, one each side of the knee, pressing it flat round the joint. Close-up: "
    "the sleeved knee and her hands fill the middle of the frame, the hem of her navy skirt at the top, her bare left knee beside it and "
    "her white canvas plimsolls on the tiles at the bottom, the kitchen table legs and units behind.",
    R1_BODY + " " + R1_LEGS + " Her hands: slim, pale, faintly freckled older skin, a plain gold wedding ring, the dusty-pink cardigan "
    "cuffs at the wrists. The sleeve is the same plain grey knit knee sleeve as on the table in the attached photo.",
    KITCHEN,
    angle("B10a", "her sleeved knee"),
    focus("everything", deep=True),
    light("KITCH-L", "her knee and hands"), colour("KITCH-AM").replace("a dusty-pink cardigan cuff and a yellowed photo album", "a dusty-pink cardigan cuff, a navy skirt, white plimsolls and a grey knit sleeve").replace("the faded orange of the old photograph", "the grey sleeve")],
    NO_FACE + ", no torso above the waist, no product anywhere, no knee strap, no strap of any kind, no brace, no sock, no cap over the "
    "kneecap, no gap in the sleeve, no readable text, no labels, no logos, no second person, no extra hands, no extra fingers, no wrong "
    "number of legs"))

# B10b — "A hinged brace stops the knee going sideways, and it was never going sideways." (user 'GIVE ME BROLLS HERE'). High
# three-quarter CU on the table: her hands try to bend the same black hinged brace (as in B09-BR) sideways at its metal hinge; it will not.
B["B10b"] = (NB2, ["R1", "P4", "K9"], photo([
    "A snapshot from a phone held up high, looking down at an angle at the pale-oak kitchen table. The same bulky black hinged knee "
    "brace as in the attached photo lies on the linen runner, its two metal side hinges showing. Her two hands hold it at either end "
    "of one metal hinge and push to bend it sideways, and it does not give: the metal side bar stays dead straight, her knuckles "
    "whitening slightly with the effort. Close-up: her hands and the brace fill the frame, the table and the jug of flowers soft behind.",
    "Her hands: THE SAME WOMAN as in the attached character sheet — slim, pale, faintly freckled older skin, thin skin over the "
    "knuckles, a plain gold wedding ring, the dusty-pink cardigan cuffs at the wrists.",
    KITCHEN,
    angle("B10b", "her hands and the brace"),
    focus("the metal hinge", deep=False).replace("the room behind", "the table behind"),
    light("KITCH-L", "her hands and the brace"), colour("KITCH-AM").replace("a dusty-pink cardigan cuff and a yellowed photo album", "a dusty-pink cardigan cuff and a black brace").replace("the faded orange of the old photograph", "the brushed metal hinge")],
    NO_FACE + ", no person beyond her hands, no product anywhere, no knee strap, no readable text, no labels, no brand names, no logos, "
    "no second person, no extra hands, no extra fingers, no bent metal"))

# B10a2 — "and leaves that band carrying everything." (user 'BROLLS HERE', second half of the B10a line). ANAT, three-quarter: a
# faint grey knit sleeve squeezing the whole knee evenly, and under it the patellar tendon alone lit and taut — still carrying the load.
B["B10a2"] = (NB2, [], anat(
    "Seen from eye level, three-quarter front, close: the knee under load, wrapped from the lower thigh to the upper shin in a faint, "
    "translucent grey knit sleeve — a soft ghostly compression tube of fine knit texture squeezing the WHOLE joint evenly all the way "
    "round, pressing the same everywhere. Under it, the anatomy stays readable, and one structure alone is lit: the patellar tendon, "
    "running from the lower edge of the kneecap to the top of the shin as one clear pearly band, drawn taut, with its one tight spot "
    "glowing just below the kneecap — still carrying all of the load while the sleeve round everything changes nothing. "
    + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from eye level, three-quarter front, the sleeved knee large in the middle of the frame with the lower thigh above and "
         "the upper shin below", stack="ANAT-B", slots={"[STACK]": "the surrounding soft tissue"})
    .replace("no clothing, ", "no clothing other than the faint grey knit sleeve, no strap, no brace, no product, "))

# B10b2 v2 — "and it was never going sideways." User Fix 'GIVE ME DIFFERENT IMAGE HERE' (v1: Maureen walking towards the lens).
# ANAT-A in profile, low: the knee as a hinge, bent forwards mid-step in one flat plane — the joint only ever bends forwards.
B["B10b2"] = (NB2, [], anat(
    "Seen from the side, in exact profile, from slightly below: the whole knee bent forwards mid-step like a hinge — the thigh angled "
    "down from the upper left to the knee pointing to the right, the shin angled back down to the lower left, the joint between them folding in one flat plane square to the "
    "lens, the femur and tibia meeting at the hinge with the kneecap riding in front of it. Everything in the leg lines up in that one "
    "plane: nothing twists, nothing turns or leans sideways, the foot pointing straight ahead in line with the knee. The quadriceps, "
    "hamstrings and calf in rich detail around the hinge. "
    + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from the side, in exact profile, from slightly below, the bent knee joint large in the middle of the frame with the thigh "
         "above-left, the knee pointing right and the shin below-left"))

# B10c — "Gel sits on the skin." (user 'BROLLS HERE'). Side-on at knee height: seated in her kitchen, Maureen's fingertips smooth clear
# gel over the front of her bare knee — a glossy film lying on the surface of the skin. Plain unlabelled tube on the table edge.
B["B10c"] = (NB2, ["R1", "P4"], photo([
    "A snapshot from a phone held at knee height beside her as she sits on a wooden kitchen chair, side-on. Her right leg is bent with "
    "the bare knee nearest the lens; the fingertips of her right hand are smoothing a thin layer of clear gel over the front of the "
    "knee, the gel lying as a wet, glossy film on the surface of the skin, catching the window light. A plain white tube with no label "
    "lies on the edge of the pale-oak table behind. Close: the frame holds her knee, her hand and the hem of her navy skirt, the kitchen "
    "going soft behind.",
    R1_BODY + " " + R1_LEGS + " Her hand: slim, pale, faintly freckled older skin, a plain gold wedding ring, the dusty-pink cardigan "
    "cuff at the wrist. Wearing a navy skirt ending just above the knee.",
    KITCHEN,
    angle("B10c", "her knee and the gel"),
    focus("the gel on her knee", deep=False).replace("the room behind", "the kitchen behind"),
    light("KITCH-R", "her knee and hand"), colour("KITCH-AM").replace("a dusty-pink cardigan cuff and a yellowed photo album", "a dusty-pink cardigan cuff and a navy skirt").replace("the faded orange of the old photograph", "the glossy clear gel")],
    NO_FACE + ", no torso, no product anywhere, no knee strap, no brace, no sleeve, no label on the tube, no readable text, no logos, "
    "no second person, no extra fingers, no wrong number of legs"))

# B10d — "A painkiller turns the alarm off" (first half of the line; user 'BROLLS HERE'). Low three-quarter CU on the kitchen table:
# her thumb pops one white tablet out of a plain blister pack beside a glass of water.
B["B10d"] = (NB2, ["R1", "P4"], photo([
    "A snapshot from a phone resting low on the pale-oak kitchen table, three-quarter on, looking slightly up. Her two hands hold a plain "
    "silver blister pack of small white tablets, her thumb pressing one tablet out through the foil, the tablet just breaking through. "
    "A plain glass of water stands beside her hands on the table. Close: her hands, the blister pack and the glass fill the frame, the "
    "kitchen units soft behind.",
    "Her hands: THE SAME WOMAN as in the attached character sheet — slim, pale, faintly freckled older skin, thin skin over the knuckles, "
    "a plain gold wedding ring, the dusty-pink cardigan cuffs at the wrists.",
    KITCHEN,
    angle("B10d", "her hands and the tablets").replace("close to the floor", "resting on the table top"),
    focus("the tablet under her thumb", deep=False).replace("the room behind", "the kitchen behind"),
    light("KITCH-L", "her hands and the table"), colour("KITCH-AM").replace("a dusty-pink cardigan cuff and a yellowed photo album", "a dusty-pink cardigan cuff and a silver blister pack").replace("the faded orange of the old photograph", "the white tablets")],
    NO_FACE + ", no person beyond her hands, no product anywhere, no knee strap, no printing on the blister pack, no pharmacy box, "
    "no brand names, no readable text, no logos, no second person, no extra hands, no extra fingers"))

# B11-BR v2 — "None of them are aimed at the spot." User Fix 'fix this, give me different image' (v1: her fingertip on the knee, the
# remedies on the table). ANAT-A front-on: the sleeve, the brace's side bars and the gel film all sit AROUND the knee; the one spot on
# the tendon just below the kneecap glows untouched in the middle.
B["B11-BR"] = (NB2, [], anat(
    "Seen straight from the front at eye level, close: the whole knee in the middle of the frame, and around it, rendered as faint "
    "ghostly overlays, the three things people try: a translucent grey knit sleeve squeezing the whole joint evenly from the lower thigh "
    "to the upper shin; the two black side bars and round hinges of a knee brace, ghosted, running down the OUTER and INNER sides of the "
    "knee; and a thin glossy film of gel lying on the skin's surface over the front. All three sit AROUND the knee and on its surface — "
    "not one of them reaches the patellar tendon just below the kneecap, where the one tight spot glows, untouched, in the middle of "
    "everything. "
    + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed straight from the front at eye level, close, the whole knee in the middle of the frame")
    .replace("no clothing, ", "no clothing other than the faint ghosted sleeve, no strap, "))

# B12 — "What that band actually needs" (first half of the B12 line; user 'BROLLS HERE'). ANAT-A in profile under load, the tendon
# spot glowing hot; pip — knee upper right, lower-left clear for the host.
B["B12"] = (NB2, [], anat(
    "Seen from the side, in profile, at eye level: the knee bent a little under a step's load, the quadriceps above, the kneecap, and the "
    "patellar tendon below it drawn taut as one clear pearly band down to the top of the shin, its one tight spot just below the kneecap "
    "glowing hot red-orange at the core. THE KNEE SITS IN THE UPPER RIGHT OF THE FRAME; the lower-left third of the frame is calm "
    "near-black field with nothing in it (a person will be placed there later). "
    + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from the side, in profile, at eye level, the knee joint in the upper right of the frame, the lower-left third empty field"))

# B12b — "is for less of your weight to land on it." (second half of the B12 line). ANAT-B ECU from above on the patellar tendon:
# the spot below the kneecap cooling from hot red-orange to a soft, calm pearly glow — less load landing on it.
B["B12b"] = (NB2, [], anat(
    "Seen from above, looking down the front of the knee, very close: the lower edge of the kneecap at the top of the frame and the "
    "patellar tendon below it as a broad pearly band filling the frame. On it, just below the kneecap, the one spot is CALMING: its "
    "centre still a soft warm glow, the hot red-orange cooling and fading to a gentle, even pearly light, the tendon relaxed and at "
    "ease, the whole band quiet — less load landing on it.",
    view="viewed from above, very close on the patellar tendon just below the kneecap, the tendon filling the frame", stack="ANAT-B",
    slots={"[STACK]": "the surrounding soft tissue"})
    .replace("mid-intensity and clearly glowing — not at peak, leaving headroom to escalate", "low, soft and calm, cooling")
    .replace("Unmistakably the brightest element in frame.", "Still the brightest element in frame, but quiet."))

# ── 2026-09-30 round: B10d2 Fix + product beats B13–B14c ─────────────────────────────
REFS.update({"PF": ("front.webp — the strap front-on (Image 1)", "20bc8be5-8526-48b6-a6e0-acbcb17b7c56"),
             "PW": ("worn_front.jpg — worn placement", "2290ef3b-75a4-4c39-8ea2-b9c4b60e6637"),
             "PBI": ("back_inner.jpg — the pad flat-on (Image 1)", "a4613068-0891-4e4b-9ad3-cffbd00180d6"),
             "PI": ("inner_face.jpg — the pad in a hand", "7bd450f9-762f-446e-a6fd-f1a9c6980182")})
LIGHT["M-SUN-R"] = ("the glass panel of her front door", "right", "warm afternoon sun, soft and golden — the after state, easy and bright, never harsh")
COLOUR["M-STAIRS-SUN"] = ("warm afternoon sunlight", "pale duck-egg blue walls, oatmeal carpet, white spindles and skirting, honey oak handrail",
                          "a sage-green cardigan, a white T-shirt and a mid-blue denim skirt", "the matte-black strap and its chrome slides", "true to life, warm")
KELVIN["M-STAIRS-SUN"] = 5600
PROD_NEG = ("no neoprene sleeve, no padded brace, no generic knee strap, no flat band with a square buckle, no dog-bone pad, no velcro, "
            "no second strap, no product redesigned, no oversized strap, no shell wider than a hand")

# B10d2 v2 — "and leaves the load exactly where it was." User Fix 'give me different broll here' (v1: Maureen's plimsoll landing on
# her bottom stair). Desmond, low side-on: sitting on his bottom stair, pushing up to stand, both knees bent hard under his whole weight.
B["B10d2"] = (NB2, ["R2", "P2"], photo([
    "A snapshot from a phone held low near the hall floor, side-on to him, about a metre and a half away. He is getting up off his bottom "
    "stair: caught halfway, his seat just lifting off the stair tread, both feet flat on the hall carpet, both knees bent hard and pushed "
    "forward over his toes, his two hands pressed flat on the tops of his thighs just above the knees, pushing down to get himself up — his "
    "knees taking his whole weight. The frame is cropped at his waist: it holds his thighs, knees, shins, trainers, his hands and the bottom "
    "two stairs.",
    R2_LEGS + " Wearing " + WARD["D-D1"] + ".",
    D_STAIRS,
    angle("B10d2", "his legs rising off the stair"),
    focus("his near knee and hands", deep=False).replace("the room behind", "the hall behind"),
    light("D-GREY-L", "his legs and the stairs"), colour("D-STAIRS-AM")],
    NO_FACE + ", no torso above the waist, no product anywhere, no knee strap, no brace, no sleeve, no walking stick, no second person, "
    "no readable text, " + PLAIN_SHOES + ", no wrong number of legs, no extra hands, no extra fingers"))

# B13 v2 — "That is what this does. It is called Stryde." User Fix 'fix the product' (v1: a U-shaped shell, the band standing up as a
# stiff ring). One hand holds it up by the fingertips on the pad behind (HELD_GRIPS 'fingertips behind'), front square to the lens exactly
# as front.webp, the band hanging soft below (FP01, FP05, FP06, FP11, FP12).
B["B13"] = (NBP, ["PF", "R1", "P4"], photo([
    "A snapshot from a phone held at chest height, straight on, in her kitchen. The strap in Image 1, copied exactly — same shell, band, "
    "slides and wordmark, nothing redesigned — held up in ONE hand at chest height above the pale-oak table: her fingertips pressed flat on "
    "the pad behind the shell, her thumb at the shell's lower left corner, the front face of the shell square to the lens exactly as it "
    "faces the camera in Image 1, the wordmark readable, nothing covering the shell, the peaks, the notch or the wordmark. The soft black "
    "knit band hangs down loosely from both slides behind her hand in a slack, drooping loop, bending like fabric. Close-up: the shell fills "
    "about half the frame width, her hand and wrist behind and below it, the kitchen soft behind.",
    "THE SHAPE, exactly as Image 1: a wide, low matte-black shell, about two and a half times as wide as it is tall. Its top edge rises into TWO rounded peaks, one over each end third of the shell, with a deep rounded notch dipping between them in the middle; beyond each peak the top edge drops down to a short straight shoulder where a brushed chrome slide with three small engraved chevrons sits upright at each end. The bottom edge is gently waisted. The black coarse-knit band comes out of each slide. The shell is flat-fronted and wide — never a U, never a cup, never a tall ring, never a curved bow. " + P.WORDMARK_LOCK + " " + P.SIZE_HELD,
    "Her hand: THE SAME WOMAN as in the attached character sheet — slim, pale, faintly freckled older skin, thin skin over the knuckles, "
    "a plain gold wedding ring, the dusty-pink cardigan cuff at the wrist.",
    KITCHEN,
    angle("B13", "the strap in her hand"),
    focus("the product and its wordmark", deep=False).replace("the room behind", "the kitchen behind"),
    light("KITCH-R", "the strap and her hand"), colour("KITCH-AM").replace("a dusty-pink cardigan cuff and a yellowed photo album", "a dusty-pink cardigan cuff").replace("the faded orange of the old photograph", "the brushed chrome slides")],
    NO_FACE + ", no person beyond her hand and wrist, no second hand, " + P.NEG_WORDMARK + ", " + PROD_NEG
    + ", no U-shaped shell, no cup shape, no stiff band, no band standing up in a ring, no band loop above the hand, no curved bow shape, "
    "no peaks at the very ends, no fingers across the wordmark, no fingers on the slides, no hand gripping the band, no strap worn, no packaging, no box"))

# B14a v2 — "It sits two centimetres below the kneecap, on the tendon, and never crosses the joint." User Fix 'fix the woman' (v1: a
# younger, tanned-looking pair of legs and hands, bare feet — not Maureen). Same seat move; Maureen's own legs, hands and plimsolls.
B["B14a"] = (NBP, ["PF", "PW", "R1", "P1"], photo([
    "A snapshot from a phone held up high, looking down at an angle at her right knee as she sits on her bottom stair, the knee bent at a "
    "right angle, the foot flat on the hall floor in a white canvas plimsoll. The strap in Image 1, copied exactly — same shell, band, "
    "slides and wordmark, nothing redesigned — is closed round the top of her right shin, its front face towards the lens: both her hands "
    "hold the shell by its two sides, fingertips flat on the matte shell, sliding the whole strap UP the front of the shin, caught a "
    "finger's width short of its seat — about to stop ON THE PATELLAR TENDON just below the kneecap, where Image 2 shows it worn. The "
    "kneecap above stays bare, its whole outline reading. Close-up: the knee, the strap and her hands fill the frame, the strap about a "
    "third of the frame wide.",
    P.REF_PROD.replace("attached reference image", "Image 1") + " " + P.WORDMARK_LOCK + " " + P.SIZE_WORN,
    "SHE IS MAUREEN, THE SAME WOMAN as in the attached character sheet (Image 3): a SIXTY-NINE-year-old white British woman, short and "
    "slight with a small rounded back. Her legs are thin and VERY PALE, never tanned — milky, faintly freckled older skin with soft creases "
    "over a bony knee, a few thread veins and a faint bluish vein on the shin, slightly loose skin at the knee, real unretouched skin. Her "
    "hands are small, thin-skinned older hands: prominent knuckles and tendons, brown age spots on the backs, short plain unpolished nails, "
    "a plain gold wedding ring. Wearing a sage-green cardigan over a white T-shirt, a mid-blue denim skirt ending just above the knee, and "
    "WHITE CANVAS PLIMSOLLS on both feet.",
    M_STAIRS,
    angle("B14a", "her right knee and the strap"),
    focus("the product and its wordmark", deep=False).replace("the room behind", "the hall behind"),
    light("M-SUN-R", "her knee, the strap and her hands"), colour("M-STAIRS-SUN")],
    NO_FACE + ", no torso above the waist, " + P.NEG_SEAT + ", " + P.NEG_WORDMARK + ", " + PROD_NEG
    + ", no tanned skin, no young skin, no smooth young hands, no manicured nails, no painted nails, no bare feet, no strap on the left leg, "
    "no strap over the kneecap, no strap on the thigh, no fingers across the wordmark, no second person, no extra fingers"))

# B14b v2 — "A silicone pad inside holds pressure on that one band…" User Fix 'too big, fix size' (v1: the strap held upright, longer
# than her whole hand). Held across her fingers exactly like inner_face.jpg, at that photo's size against the hand, framed wider (FP02, FP06).
B["B14b"] = (NBP, ["PBI", "PI", "R1", "P4"], photo([
    "A snapshot from a phone held at eye level, three-quarter on, close, in her kitchen. She holds the strap turned round in ONE hand so "
    "its inside faces the lens, lying ACROSS her fingers sideways exactly as the hand holds it in Image 2 and at the SAME SIZE against the "
    "hand as in Image 2: her fingers under the shell's back, her thumb resting at the pad's lower corner, clear of the raised ridge. It is "
    "a small object: slide to slide it is about 12 cm — SHORTER than her hand from the wrist to the fingertips — and about 5 cm tall, "
    "about as tall as her thumb is long. The pad is Image 1 copied exactly — same outline, same comma-shaped ridge, same fanned grooves, "
    "same chrome slides and black knit band ends, nothing redesigned. Close-up: her whole hand, her wrist and the cardigan cuff in frame, "
    "the strap about two fifths of the frame width, the kitchen table soft behind.",
    P.PAD_BACK_SHOT.replace(" fills the frame", " faces the lens") + " " + P.INNER_PAD + " " + P.SIZE_HELD,
    "Her hand: THE SAME WOMAN as in the attached character sheet — slim, pale, faintly freckled older skin, thin skin over the knuckles, "
    "a plain gold wedding ring, the dusty-pink cardigan cuff at the wrist.",
    KITCHEN,
    angle("B14b", "the inside of the strap in her hand"),
    focus("the pad inside the shell", deep=False).replace("the room behind", "the kitchen behind"),
    light("KITCH-L", "the pad and her hand"), colour("KITCH-AM").replace("a dusty-pink cardigan cuff and a yellowed photo album", "a dusty-pink cardigan cuff").replace("the faded orange of the old photograph", "the grey pad")],
    NO_FACE + ", no person beyond her hand, no second hand, " + P.NEG_INNER_PAD + ", " + PROD_NEG
    + ", no strap longer than her hand, no strap held upright, no strap filling the frame, no wordmark on this side, no thumb over the ridge, "
    "no strap worn, no packaging"))

# B14c v2 — "Your weight gets caught and moved off the worn part before it reaches the joint." User Fix 'fix the product' (v1: an
# invented translucent strap over the joint). ANAT-A front-on at eye level with the REAL strap from front.webp (Image 1), opaque, seated on
# the tendon below the kneecap, wordmark to the lens; the glow at the spot calming around it (FP01, FP03, FP12).
B["B14c"] = (NBP, ["PF"], anat(
    "Seen straight from the front at eye level, close: the knee under a step's load, and worn on it THE STRAP IN IMAGE 1, COPIED EXACTLY — "
    "the same solid, opaque matte-black shell, the same two rounded peaks with the rounded notch between them, the same brushed chrome "
    "slides with engraved chevrons, the same black coarse-knit band and the same grey lowercase stryde wordmark, nothing redesigned, a real "
    "physical object sitting on the translucent model. It sits ON THE PATELLAR TENDON directly below the kneecap: the notch cups the "
    "kneecap's lower border, the peaks either side reach no higher than the base of the kneecap, the shell spans the front of the knee with "
    "a chrome slide at each side, the band running level round the leg behind; the wordmark faces the lens, horizontal and readable. The "
    "kneecap stays fully uncovered above it. Around the shell's edges, on the tendon beneath it, the spot is CALMING: a soft, even pearly "
    "glow seeping out round the shell where the hot red-orange has faded, the tendon relaxed; the load reads as a faint cool glow spread "
    "into the surrounding soft tissue, away from the worn spot. " + P.SIZE_WORN,
    view="viewed straight from the front at eye level, close, the strapped knee large in the middle of the frame")
    .replace("no product,", "no product other than the one strap on the tendon,").replace("no product\n", "no product other than the one strap on the tendon\n")
    .replace("no text overlays, no labels,", "no text overlays, no diagram labels,").replace("no clothing, ", "no clothing, no second strap, no strap over the kneecap, no translucent strap, no ghosted strap, no invented strap shape, no blank shell, "))

# B13 v3 — User Fix 'fix the product stryde' (v2: a plain rounded rectangle, no peaks, no notch). Made as an IMAGE EDIT of v2 (Image 1:
# the confirmed-looking hand, kitchen and hanging band) with front.webp as Image 2: only the object in her hand is replaced, by the
# strap in the product photo copied exactly (FP01, FP12).
REFS["B13V2"] = ("B13 v2 — the scene to edit (Image 1)", "48c97d46-dde1-4c51-a0dd-12179b8c0336")
B["B13"] = (NBP, ["B13V2", "PF"], (
    "Edit Image 1. Keep everything in Image 1 exactly as it is — the same kitchen, the same light, the same hand with the gold ring and "
    "the dusty-pink cuff, the same pose, the same camera and framing, the same soft black knit band hanging down in a loop behind her "
    "hand. Change ONLY the black shell she holds up: replace it with the strap from Image 2, copied exactly — the same matte-black shell "
    "with its top edge rising into TWO rounded peaks with a deep rounded notch dipping between them in the middle, the same short "
    "shoulders dropping to a brushed chrome slide with three engraved chevrons at each end, the same gently waisted bottom edge and the "
    "same grey lowercase stryde wordmark centred on the lower body beneath the notch. Seen straight on, exactly as the front of the strap "
    "faces the camera in Image 2, at the same size in her hand as the shell in Image 1 — about five to six of her thumb-widths across. "
    "Her thumb stays at the lower left corner and her fingertips stay behind it; nothing covers the peaks, the notch or the wordmark. The "
    "band comes out of both chrome slides and hangs soft behind her hand as in Image 1. A real phone photo, unchanged in look.\n\n"
    "AVOID: no rounded rectangle shell, no oval shell, no flat straight top edge, no U-shaped shell, no cup shape, no peaks at the very "
    "ends, no blank shell, no misspelled wordmark, no second strap, no change to the hand, no change to the kitchen, no change to the "
    "light, no extra fingers, no readable text other than the wordmark"))

# B13 v4 — User Fix 'fix the hand holding the stryde' (v3: the strap right at last, but an odd hand — fingers splayed up above the
# shell, two gold rings). Image edit of v3 (Image 1): only the hand changes; the strap stays exactly as it is (front.webp as Image 2).
REFS["B13V3"] = ("B13 v3 — the scene to edit (Image 1)", "5069cf9a-486c-461a-ada2-2380f3ecb70d")
B["B13"] = (NBP, ["B13V3", "PF"], (
    "Edit Image 1. Keep the strap exactly as it is in Image 1 — the same matte-black shell with its two rounded peaks and the notch "
    "between them, the same chrome slides, the same grey stryde wordmark, the same size and position, the soft black band hanging in a "
    "loop below — and keep the kitchen, the light and the framing exactly the same. The strap must still match Image 2. Change ONLY THE "
    "HAND holding it: ONE natural older woman's right hand, relaxed, holding the strap the way you hold up a phone to show someone — her "
    "four fingers curled together BEHIND the shell, hidden by it, only their tips just showing at the shell's lower edge; her thumb "
    "resting lightly on the front at the shell's lower left corner, below the peak and clear of the wordmark. Nothing sticks up above "
    "the shell. Five fingers in total, natural proportions, slim, pale, faintly freckled older skin with thin skin over the knuckles, "
    "ONE plain gold wedding ring on the ring finger only, the dusty-pink cardigan cuff at the wrist. A real phone photo, unchanged in look."
    "\n\nAVOID: no fingers spread above the shell, no fingers splayed, no second ring, no ring on the thumb, no ring on the index finger, "
    "no extra fingers, no missing fingers, no fused fingers, no second hand, no thumb over the wordmark, no fingers on the chrome slides, "
    "no change to the strap, no change to the wordmark, no change to the kitchen, no change to the light"))

# ── 2026-09-30 Fix round 3 — image edits of the last renders (the B13 v3 approach) ─────────────────────────
REFS["B14AV2"] = ("B14a v2 — the scene to edit (Image 1)", "08cf3855-d502-4d9f-8d7c-ef5460eee8fb")
REFS["B14BV2"] = ("B14b v2 — the scene to edit (Image 1)", "ab4a6700-d742-40b1-8b0d-6eb4c68382da")
REFS["B14CV2"] = ("B14c v2 — the scene to edit (Image 1)", "71f98792-0aca-4ad9-ba37-6b168d66454b")

# B14a v3 — video Fix 'FIX THE PLACEMENT, BELOW THE KNEECAP' (video v1 ended with the strap high and turned to the side of the knee — the
# start frame already had it at kneecap height and rotated: fixed at the source, §22X). Edit of v2: the strap moved to its seat — centred
# on the patellar tendon just below the kneecap, front and wordmark to the lens; her hands at the shell's two sides (FP03, PLACE_LOCK_C).
B["B14a"] = (NBP, ["B14AV2", "PF", "PW"], (
    "Edit Image 1. Keep everything in Image 1 exactly as it is — the same woman, her sage-green cardigan, denim skirt, pale legs and white "
    "plimsolls, the same stairs, hall, light and framing. Change ONLY where the strap sits and how her hands hold it: the strap from "
    "Image 2, copied exactly, is worn on her right leg CENTRED ON THE PATELLAR TENDON DIRECTLY BELOW THE KNEECAP, as in Image 3 — the "
    "notch in the shell's top edge cups the lower border of the kneecap, the two peaks either side reach no higher than the base of the "
    "kneecap, the shell spans the front of the upper shin with a chrome slide at each side of the leg, the front of the shell and the "
    "grey stryde wordmark facing the camera, level and readable, the black band running level round the leg behind. The whole kneecap "
    "stays bare above it, its outline reading in full. Both her hands hold the shell lightly by its two outer ends, fingertips on the "
    "chrome-slide ends, nothing covering the wordmark. The strap is at least a quarter of the frame wide.\n\n"
    + P.PLACE_LOCK_C.replace("[SIDE]", "right") + "\n\n"
    "AVOID: no strap over the kneecap, no strap on the side of the knee, no strap turned sideways, no strap at kneecap height, no strap "
    "low on the shin, no strap on the left leg, no strap on the thigh, no wordmark hidden, no second strap, no change to her clothes, no "
    "change to her legs, no change to the stairs, no extra fingers, no extra hands"))

# B14b v3 — image Fix 'FIX THE PRODUCT' (v2: the pad shape and slides drifted from the real inside). Edit of v2: only the strap in her
# hand replaced by the inside of the strap in back_inner.jpg, copied exactly, at the same size (FP04, FP12; never the word 'silicone').
B["B14b"] = (NBP, ["B14BV2", "PBI", "PI"], (
    "Edit Image 1. Keep everything in Image 1 exactly as it is — the same kitchen, the same light, the same hand with its pink cuff and "
    "gold ring, the same pose, the same camera and framing, the same size in the hand. Change ONLY the strap she holds: replace it with "
    "the inside of the strap in Image 2, COPIED EXACTLY — the same smooth matte-black back with its narrow waisted outline, the same "
    "mid-grey pad with the long smooth comma-shaped raised ridge running down its middle and the fine curved grooves fanning out from it "
    "on both sides, the same polished chrome slide at each end with the black knit band looped through it. Held upright in her hand as "
    "in Image 1, its inside to the lens, exactly as Image 3 shows it in a real hand. No wordmark on this side.\n\n"
    + P.INNER_PAD + "\n\n"
    "AVOID: " + P.NEG_INNER_PAD + ", no invented pad shape, no different outline, no second ridge, no wordmark, no second strap, no "
    "change to the hand, no change to the kitchen, no change to the light, no extra fingers, no strap larger than in Image 1"))

# B14c v3 — image Fix 'FIX SIZE BIGGER' (v2: the strap a little narrow for the knee). Edit of v2: the same strap scaled up to true
# worn size — spanning the whole front of the leg, slide to slide at its outer edges, as tall as the kneecap (SIZE_WORN, FP02, FP11).
B["B14c"] = (NBP, ["B14CV2", "PF"], (
    "Edit Image 1. Keep everything in Image 1 exactly as it is — the same anatomical model, the same muscles, bones and kneecap, the "
    "same near-black field, the same light and framing, the same position of the strap just below the kneecap with the wordmark to the "
    "lens. Change ONLY the SIZE of the strap: make it BIGGER — about one and a half times as wide as in Image 1, so the shell spans the "
    "WHOLE FRONT WIDTH OF THE LEG from edge to edge, with a chrome slide right at each outer side of the leg, and the shell about as tall "
    "as the kneecap itself. The notch still cups the kneecap's lower border and the peaks still reach no higher than its base; the "
    "kneecap stays uncovered above it. The strap keeps exactly the shape and details of Image 2 — the two rounded peaks and the notch, "
    "the chevron slides, the grey stryde wordmark — and the black band stays level round the leg. " + P.SIZE_WORN + "\n\n"
    "AVOID: no small strap, no strap narrower than the leg, no strap over the kneecap, no strap lower on the shin, no change to the "
    "anatomy, no change to the light, no second strap, no blank shell, no text other than the wordmark"))

# ── 2026-09-30 Fix round 4 ──────────────────────────────────────────────────────────────────────────────
# B13 v5 — User Fix 'CHANGE THE IMAGE, MAKE SURE THE PRODUCT IS RIGHT AND THE SIZE'. A new image: seen from above, the strap lying
# front-face-up across her ONE open palm like the product photo laid flat (HELD_GRIPS 'open palm'; FP01, FP02, FP05, FP06, FP11, FP12).
B["B13"] = (NBP, ["PF", "R1", "P4"], photo([
    "A snapshot from a phone held above her hand, looking straight down, in her kitchen. The strap in Image 1, COPIED EXACTLY — same "
    "shell, band, slides and wordmark, nothing redesigned — lies front face UP across her ONE open, upturned right palm, seen from above "
    "exactly as Image 1 shows it: the matte-black shell with its two rounded peaks and the deep rounded notch between them, a chrome "
    "slide with three engraved chevrons at each end, the grey lowercase stryde wordmark centred beneath the notch, sharp and readable. "
    "TRUE SIZE: the shell is about 12 cm across and 5 cm tall — it lies across her palm with each chrome slide just past the edges of her "
    "palm, no wider than her hand, about as tall as her thumb is long. Her fingers are relaxed and slightly curled at the shell's lower "
    "edge, her thumb resting beside it; nothing covers the shell, the peaks, the notch or the wordmark. The soft black knit band comes out "
    "of both slides and hangs down over the sides of her hand in one closed, slack loop, bending like fabric. Close-up: the strap about "
    "half the frame width, her palm and wrist around it, the pale-oak table soft below.",
    P.WORDMARK_LOCK + " " + P.SIZE_HELD,
    "Her hand: THE SAME WOMAN as in the attached character sheet — slim, pale, faintly freckled older skin, thin skin over the knuckles, "
    "ONE plain gold wedding ring, the dusty-pink cardigan cuff at the wrist.",
    KITCHEN.replace("THE SAME KITCHEN as the attached location plate", "Below, THE SAME KITCHEN TABLE as the attached location plate"),
    "THE CAMERA ANGLE: a camera held directly above her hand, looking straight down at the strap in her palm. This exact angle.",
    focus("the product and its wordmark", deep=False).replace("the room behind", "the table below"),
    light("KITCH-R", "the strap and her hand"), colour("KITCH-AM").replace("a dusty-pink cardigan cuff and a yellowed photo album", "a dusty-pink cardigan cuff").replace("the faded orange of the old photograph", "the brushed chrome slides")],
    NO_FACE + ", no person beyond her hand and wrist, no second hand, " + P.NEG_WORDMARK + ", " + PROD_NEG
    + ", no rounded rectangle shell, no oval shell, no flat straight top edge, no U-shaped shell, no cup shape, no stiff band, no band cut "
    "off at the slides, no strap bigger than her hand, no strap much smaller than her palm, no second ring, no fingers across the "
    "wordmark, no fingers on the slides, no strap worn, no packaging, no box"))

# B14a v4 — User Fix 'MAKE SURE THE STRAP STAY IN THAT PLACE' (the place = on the tendon just below the kneecap, the earlier Fix; v3's
# edit left it high and turned). A new image, front-on: seated on her bottom stair, the strap ALREADY SEATED below the kneecap, her
# fingertips just leaving its ends; the video then only lifts her hands away — the strap never moves (PLACE_LOCK_C; FP03, FP11).
B["B14a"] = (NBP, ["PF", "PW", "R1", "P1"], photo([
    "A snapshot from a phone held at knee height, straight in front of her, as she sits on her bottom stair with her right knee bent at a "
    "right angle towards the lens and her right foot flat on the hall floor in a white canvas plimsoll. The strap in Image 1, COPIED "
    "EXACTLY — same shell, band, slides and wordmark, nothing redesigned — is worn on her right leg exactly as in Image 2: seated ON THE "
    "PATELLAR TENDON directly below the kneecap, square to the lens, the grey stryde wordmark level and readable. Her two hands rest "
    "lightly at the shell's two outer ends, fingertips on the chrome slides, just about to lift away. The whole kneecap is bare above it. "
    "Close-up: her right knee fills the middle of the frame from mid-thigh to mid-shin, the strap about a third of the frame wide, her "
    "hem and hands in frame, the stairs soft behind.",
    P.PLACE_LOCK_C.replace("[SIDE]", "right") + " " + P.SIZE_WORN,
    "SHE IS MAUREEN, THE SAME WOMAN as in the attached character sheet (Image 3): sixty-nine, short and slight. Her legs are thin and very "
    "pale, never tanned — faintly freckled older skin with soft creases over a bony knee, a few thread veins. Her hands are small, "
    "thin-skinned older hands with age spots and one plain gold wedding ring. Wearing a sage-green cardigan over a white T-shirt, a "
    "mid-blue denim skirt ending just above the knee, white canvas plimsolls.",
    M_STAIRS,
    "THE CAMERA ANGLE: an eye-level camera at the height of her knee, seen from the front of her right knee and the strap. This exact angle.",
    focus("the product and its wordmark", deep=False).replace("the room behind", "the hall behind"),
    light("M-SUN-R", "her knee, the strap and her hands"), colour("M-STAIRS-SUN")],
    NO_FACE + ", no torso above the waist, " + P.NEG_PLACE.replace('[OTHER_SIDE]', 'left') + ", " + P.NEG_WORDMARK + ", " + PROD_NEG
    + ", no strap over the kneecap, no strap at kneecap height, no strap on the side of the knee, no strap turned sideways, no strap low "
    "on the shin, no strap on the left leg, no tanned skin, no bare feet, no second person, no extra fingers"))

# B14b v4 — User Fix 'FIX THE PRODUCT SHOWING THE STRAP' (v3: the pad right, but the band cut off in short stubs at the slides — not a
# whole strap; FP05). Edit of v3: the same inside and pad, and the whole black knit band continuing from both slides as one closed loop.
REFS["B14BV3"] = ("B14b v3 — the scene to edit (Image 1)", "0395fa6e-9c5e-4761-9fec-9fe8a5a48fe3")
B["B14b"] = (NBP, ["B14BV3", "PBI", "PI"], (
    "Edit Image 1. Keep everything in Image 1 exactly as it is — the same kitchen, light, framing and hand, and the same inside of the "
    "shell with its grey grooved pad and smooth comma-shaped ridge, the same chrome slides, the same size in her hand. Change ONLY the "
    "band: show THE WHOLE STRAP. The black coarse-knit elastic band does not stop at the slides — it runs out of the top slide and out of "
    "the bottom slide and joins behind her hand into ONE CLOSED, continuous loop, soft and slack, hanging down past her wrist and bending "
    "like fabric, exactly as the band loops through its slides in Image 2 and hangs from the real strap in Image 3. Two small black "
    "keeper loops sit on the band. The pad stays facing the lens. No wordmark on this side.\n\n"
    "AVOID: no band cut off at the slides, no short band stubs, no open band ends, no stiff band, no band standing up in a ring, no "
    "second strap, no change to the pad, no change to the ridge, no wordmark, no change to the hand, no change to the kitchen, no extra "
    "fingers"))

# ── 2026-09-30 Fix round 5 — size (image edits of the last renders; FP02: every earlier size note on this product was "too big") ──
REFS["B13V5"] = ("B13 v5 — the scene to edit (Image 1)", "3c4796b1-e2d6-457c-9b02-c1aa9fe4105e")
REFS["B14BV4"] = ("B14b v4 — the scene to edit (Image 1)", "cf900e16-d5f8-423a-b72d-6fea1b21f48f")
B["B13"] = (NBP, ["B13V5", "PF"], (
    "Edit Image 1. Keep everything in Image 1 exactly as it is — the same kitchen, light, framing and camera, the same hand and cuff, "
    "the same strap design copied from Image 2 with its two rounded peaks, notch, chevron slides and grey stryde wordmark, lying on her "
    "open palm in the same way. Change ONLY THE SIZE of the strap: make it SMALLER, about two thirds of its size in Image 1 — its true "
    "size, a small shell about 12 cm across and 5 cm tall: from slide to slide it is only a little wider than her palm, about five of "
    "her thumb-widths, and it is about as tall as her thumb is long, so her fingers and the heel of her palm show clearly around it. The "
    "band shrinks with it and still hangs soft behind her hand. The wordmark stays readable.\n\n"
    "AVOID: no strap as wide as the whole hand with fingers spread, no oversized strap, no strap bigger than in the product photo, no "
    "change to the strap's shape, no change to the wordmark, no second strap, no change to the hand, no change to the kitchen, no extra fingers"))
B["B14b"] = (NBP, ["B14BV4", "PBI", "PI"], (
    "Edit Image 1. Keep everything in Image 1 exactly as it is — the same kitchen, light, framing and camera, the same hand and cuff, "
    "the same inside of the strap with its grey grooved pad, smooth comma-shaped ridge, chrome slides and closed black band loop. Change "
    "ONLY THE SIZE of the strap: make it SMALLER, about two thirds of its size in Image 1 — its true size, as in Image 3: from slide to "
    "slide about 12 cm, SHORTER than her hand from the wrist to the fingertips, about as tall as her thumb is long, sitting in her hand "
    "the way the strap sits in the hand in Image 3. The band loop shrinks with it and still hangs soft below. The pad still faces the "
    "lens.\n\n"
    "AVOID: no strap longer than her hand, no oversized strap, no strap bigger than in Image 3, no change to the pad, no change to the "
    "ridge, no change to the strap's shape, no wordmark, no second strap, no change to the hand, no change to the kitchen, no extra fingers"))

# ── 2026-09-30 "BROLLS HERE" B15-BR, B15, B16a, B16b, B16c ──────────────────────────────────────────────
# Learned on B14a (three misses): fresh renders put a worn strap on the side of the knee. Worn shots here are IMAGE EDITS of
# worn_front.jpg (the real strap worn, front-on, correctly placed) — only the leg, clothes and room change (FP03, FP11, FP12).
REFS.update({"PWE": ("worn_front.jpg — the shot to edit (Image 1)", "2290ef3b-75a4-4c39-8ea2-b9c4b60e6637"),
             "S1": ("S1-SURGEON sheet", "7569a690-7398-49cb-ba09-4da6e7efd4ad"),
             "P5": ("P5-CONSULT plate", "833bfccb-a188-46d7-873a-ddc728f658fc"),
             "B13V6": ("B13 v6 — the strap in a hand at true size", "18bd9cdf-0960-44c3-a3c1-ef65855dd429")})
KEEP_STRAP = ("Keep the strap EXACTLY as it is in Image 1 — the same matte-black shell with two rounded peaks and the notch cupping the "
              "lower edge of the kneecap, the same chrome slides at the outer sides of the leg, the same grey stryde wordmark, the same "
              "size, position and angle, seated on the patellar tendon directly below the kneecap, front-on to the camera — and keep the "
              "camera angle and framing the same.")
EDIT_NEG = ("no strap moved, no strap higher, no strap lower, no strap on the side of the knee, no strap over the kneecap, no change to "
            "the strap's shape or size, no wordmark change, no second strap, no hairy legs")

# B15 — "A centimetre too high and it is a sleeve again." ECU front-on, Maureen's right knee, the kneecap's lower edge in the notch.
B["B15"] = (NBP, ["PWE", "R1", "P1"], (
    "Edit Image 1. " + KEEP_STRAP + " Change ONLY the person and the room: the leg is now Maureen's, THE SAME WOMAN as in the character "
    "sheet (Image 2) — a slight white British woman of sixty-nine: a thin, VERY PALE older leg, faintly freckled, soft creases over a "
    "bony kneecap, a few thread veins on the shin, fine pale hair only, real unretouched skin. In place of the dark shorts, the hem of a "
    "mid-blue denim skirt ending just above the knee. Behind her, instead of the window, THE SAME HALL as Image 3 — pale duck-egg blue "
    "walls, white skirting, oatmeal carpet, the foot of the stairs — soft and out of focus, warm afternoon sun from the right. A real "
    "phone photo.\n\nAVOID: " + EDIT_NEG + ", no tanned skin, no young skin, no man's leg, no shorts"))

# B16a — "Thirty four percent less strain. Measured." Front-on CU, Desmond's strapped right knee as he stands on his stair.
B["B16a"] = (NBP, ["PWE", "R2", "P2"], (
    "Edit Image 1. " + KEEP_STRAP + " Change ONLY the person and the room: the leg is now Desmond's, THE SAME MAN as in the character "
    "sheet (Image 2) — a Black British man of sixty-six: a strong, dark brown older leg, a few grey hairs on the shin, an ashy kneecap "
    "with soft creases, real unretouched skin. Instead of the dark shorts, the hem of khaki cotton shorts ending just above the knee. He "
    "stands on a stair of HIS OWN STAIRS as in Image 3: his foot on the charcoal-grey stair carpet with a white stripe at the nosing, "
    "warm mid-grey walls and white spindles behind him, soft and out of focus, warm afternoon sun from the left. A real phone photo."
    "\n\nAVOID: " + EDIT_NEG + ", no pale skin, no white man's leg, no dark shorts"))

# B16c — "Two hundred thousand people wearing one." Ground-level front-on: Desmond's strapped knee and shin walking toward the lens.
B["B16c"] = (NBP, ["PWE", "R2", "P3"], (
    "Edit Image 1. " + KEEP_STRAP + " Change ONLY the person, his step and the place: the leg is now Desmond's, THE SAME MAN as in the "
    "character sheet (Image 2) — a Black British man of sixty-six: a strong, dark brown older leg, a few grey hairs on the shin, an ashy "
    "kneecap, real unretouched skin. Instead of the dark shorts, the hem of khaki cotton shorts ending just above the knee. He is out "
    "walking TOWARDS the camera on THE SAME PAVEMENT as Image 3 — grey paving slabs, a low garden wall and privet hedge, parked cars, "
    "1930s semis going away, soft and out of focus behind — this leg planted mid-stride, the knee slightly bent, a plain white trainer "
    "with navy trim on the slab; the camera low, near knee height. Warm afternoon sun from the left. A real phone photo.\n\n"
    "AVOID: " + EDIT_NEG + ", no pale skin, no dark shorts, no logos on the trainer, no running"))

# B15-BR — "The placement is the whole thing." High three-quarter, her own view: seated on her bottom stair, two fingertips of her left
# hand laid flat on the tendon just below her bare kneecap, the strap resting front face up in her right palm, ready (HELD, FP02, FP06).
B["B15-BR"] = (NBP, ["PF", "B13V6", "R1", "P1"], photo([
    "A snapshot from a phone held up high, looking down at her right knee as she sits on her bottom stair, the knee bent, the foot flat "
    "on the hall floor in a white canvas plimsoll. Two fingertips of her left hand lie flat on the patellar tendon JUST BELOW HER BARE "
    "KNEECAP, marking the spot. Her right hand, beside the knee, holds the strap from Image 1 resting front face up across her open palm "
    "exactly as the hand holds it in Image 2 — copied exactly, the matte-black shell with two rounded peaks and the notch, the chrome "
    "slides, the grey stryde wordmark readable, at its true size: about 12 cm across, a little wider than her palm, the soft band hanging "
    "over the sides of her hand. The kneecap is bare. Close-up: her knee, her two hands and the strap fill the frame.",
    "Her legs and hands: THE SAME WOMAN as in the attached character sheet — thin, very pale, faintly freckled older skin, soft creases "
    "over a bony knee, a few thread veins, one plain gold wedding ring, the sage-green cardigan cuffs at the wrists; a mid-blue denim "
    "skirt ending just above the knee.",
    M_STAIRS,
    angle("B15-BR", "her knee, her hands and the strap"),
    focus("the hands and what they hold", deep=False).replace("the room behind", "the hall behind"),
    light("M-SUN-R", "her knee, hands and the strap"), colour("M-STAIRS-SUN")],
    NO_FACE + ", no torso above the waist, no strap on the leg, no strap worn, " + P.NEG_WORDMARK + ", " + PROD_NEG
    + ", no oversized strap, no strap bigger than her hand, no tanned skin, no bare feet, no second person, no extra fingers, no extra hands"))

# B16b — "Three years with orthopedic surgeons." MCU three-quarter at his desk: S1 in navy scrubs and grey gilet, the knee model on the
# desk, holding the strap up in one hand at chest height, front face to the lens, looking up from it (APPROACH-PRO, HELD).
LIGHT["CONS-L"] = ("the half-lowered white roller blind on the left-hand wall", "left", "soft even daylight — calm and clinical, never cold")
COLOUR["CONS-PM"] = ("soft even daylight, cool-neutral", "off-white walls, a pale wood desk, grey vinyl, a white roller blind",
                     "navy surgical scrubs and a plain grey fleece gilet", "the matte-black strap and its chrome slides", "true to life, calm")
KELVIN["CONS-PM"] = 5600
B["B16b"] = (NBP, ["S1", "P5", "PF", "B13V6"], photo([
    "A snapshot from a phone at eye level, three-quarter on, a medium close-up across his desk in his consulting room. He sits at the "
    "pale wood desk, the life-size anatomical knee model beside him, and holds the strap from Image 3 up in ONE hand at chest height, "
    "its front face and the grey stryde wordmark towards the lens — copied exactly, the matte-black shell with two rounded peaks and the "
    "notch, the chrome slides, at its true size, about 12 cm across, a little wider than his palm, the way the hand holds it in Image 4, "
    "the soft band hanging below his hand. He has just looked up from it towards someone across the desk, calm and kind. The frame holds "
    "him from mid-chest up, the strap and the knee model in the lower part of the frame.",
    "HE IS THE SAME MAN as in the attached character sheet (Image 1): a British man of Pakistani heritage, fifty-eight, medium height and "
    "solid build, short black hair grey at the temples, combed back, kind and attentive, bare face; wearing navy surgical scrubs with a "
    "short-sleeved tunic and a plain grey fleece gilet.",
    "THE SAME CONSULTING ROOM as the attached location plate (Image 2): off-white walls, the half-lowered white roller blind on the "
    "left-hand wall, the pale wood desk, the anatomical knee model, a framed botanical print, the grey couch soft behind.",
    angle("B16b", "him at his desk with the strap"),
    focus("the nearest eye of the surgeon", deep=False).replace("the room behind", "the consulting room behind"),
    light("CONS-L", "his face, hands and the strap"), colour("CONS-PM")],
    "no looking at the camera, no smiling for the camera, no white coat, no stethoscope, no second person, " + P.NEG_WORDMARK + ", "
    + PROD_NEG + ", no oversized strap, no strap worn, no readable text on the monitor, no certificates with text, no extra fingers, no extra hands"))

# ── 2026-09-30 "GIVE ME BROLLS FOR B17A TO B17C" — edits of B16a v1 / B15 v1 (the worn placement that came out right) ──
REFS.update({"B16AV1": ("B16a v1 — the shot to edit (Image 1)", "c47a0262-949a-4916-b2b9-f3a4f299e573"),
             "B15V1": ("B15 v1 — the shot to edit (Image 1)", "7f990a90-9ac1-4b71-ae5d-db3100e64d28")})
KEEP_WORN = ("Keep the strap EXACTLY as it is in Image 1 — the same shell, peaks, notch, chrome slides and grey stryde wordmark, the "
             "same size, the same place seated on the tendon directly below the kneecap, front-on — and keep the leg, the skin and the room.")
TRACKSUIT = ("plain navy tracksuit bottoms, soft brushed cotton, no logo, no stripes, no piping")

# B17a — "Ten seconds to put on." High, his own view down on his strapped right knee on his stairs: the navy tracksuit leg rolled up
# above the knee, both hands just finishing — fingertips at the strap's two chrome-slide ends (FP10: on in one move).
B["B17a"] = (NBP, ["B16AV1", "R2"], (
    "Edit Image 1. " + KEEP_WORN + " Change: instead of the khaki shorts he wears " + TRACKSUIT + ", the right leg rolled up in soft "
    "folds to just above the knee. Add HIS TWO HANDS — THE SAME MAN as in the character sheet (Image 2): strong, dark brown older hands, "
    "thick knuckles — the fingertips of each resting lightly on the strap's two outer chrome-slide ends, just finishing putting it on, "
    "the thumbs clear of the wordmark and the notch. See it a little more from above, as he looks down at his own knee. A real phone "
    "photo.\n\nAVOID: no strap moved, no strap higher, no strap lower, no strap on the side of the knee, no hands covering the wordmark, "
    "no hands on the band, no fastening, no logos on the tracksuit, no stripes, no extra fingers, no extra hands, no second strap"))

# B17b — "No sores, no rolling down," Front-on ECU at knee height, Maureen's strapped knee: one fingertip resting on the smooth,
# unmarked skin just below the strap's lower edge — no red mark, no groove, the band flat.
B["B17b"] = (NBP, ["B15V1", "R1"], (
    "Edit Image 1. " + KEEP_WORN + " Add ONE HAND — THE SAME WOMAN as in the character sheet (Image 2): a slim, pale, faintly freckled "
    "older hand with a plain gold wedding ring and the sage-green cardigan cuff at the wrist — its index fingertip resting on the skin "
    "JUST BELOW THE STRAP'S LOWER EDGE, at the side of the shin. The skin there is smooth and unmarked: no red line, no groove, no "
    "chafing; the band lies flat against the leg. Come a little closer so the strap's lower edge and her fingertip are large in the "
    "frame. A real phone photo.\n\nAVOID: no strap moved, no redness, no marks on the skin, no sores, no groove in the skin, no finger "
    "on the wordmark, no second hand, no extra fingers, no second strap"))

# B17c — "and nobody can see it." Front-on at knee height, Desmond's strapped knee: his hand holds the rolled-up navy tracksuit hem just
# above the knee, about to let it drop over the strap (the drop is the video).
B["B17c"] = (NBP, ["B16AV1", "R2"], (
    "Edit Image 1. " + KEEP_WORN + " Change: instead of the khaki shorts he wears " + TRACKSUIT + ". The right trouser leg is pulled up, "
    "bunched just above the knee, and HIS ONE HAND — THE SAME MAN as in the character sheet (Image 2): a strong, dark brown older hand — "
    "holds the gathered hem there, about to let it fall back down over the strap and the shin. The strap and the kneecap are fully "
    "visible below the bunched fabric. A real phone photo.\n\nAVOID: no strap moved, no strap higher, no strap lower, no fabric covering "
    "the strap yet, no logos on the tracksuit, no stripes, no shorts, no second hand, no extra fingers, no second strap"))

# ── 2026-09-30 "CONFIRM AND FIX THOSE" — B15-BR, B16b, B17a, B17b, B17c ─────────────────────────────────
REFS.update({"B15BRV1": ("B15-BR v1 — the shot to edit (Image 1)", "c77be803-6bed-4724-a149-9c37c6ea9037"),
             "B16BV1": ("B16b v1 — the shot to edit (Image 1)", "a1856804-7303-4094-ad47-a26814674d77"),
             "B17CV1": ("B17c v1 — the shot to edit (Image 1)", "bf16b2d6-7dbb-4787-a3fe-740878153396")})

# B15-BR v2 — Fix 'FIX THE PRODUCT': edit of v1, only the strap in her palm replaced by front.webp copied exactly, at true size.
B["B15-BR"] = (NBP, ["B15BRV1", "PF"], (
    "Edit Image 1. Keep everything in Image 1 exactly as it is — the same woman, stairs, light, camera and framing, the same open palm. "
    "Change ONLY the strap resting in her palm: replace it with the strap in Image 2, COPIED EXACTLY — the matte-black shell with its "
    "two rounded peaks and the deep rounded notch between them, the short shoulders dropping to a brushed chrome slide with three "
    "engraved chevrons at each end, the gently waisted bottom edge, the grey lowercase stryde wordmark centred beneath the notch — lying "
    "front face up across her palm at its true size, about 12 cm across, a little wider than her palm, the soft black knit band hanging "
    "over the sides of her hand in one closed loop.\n\nAVOID: no U-shaped shell, no cup shape, no rounded rectangle, no stiff band, no "
    "band standing up in a ring, no oversized strap, no change to the woman, no change to the stairs, no second strap, no extra fingers"))

# B16b v2 — Fix 'FIX THE SIZE, TOO BIG': edit of v1, only the strap in his hand made smaller (about two thirds).
B["B16b"] = (NBP, ["B16BV1", "PF"], (
    "Edit Image 1. Keep everything in Image 1 exactly as it is — the same surgeon, his face, scrubs and gilet, the desk, the knee model, "
    "the room, light and framing, and the same strap design as Image 2. Change ONLY THE SIZE of the strap in his hand: make it SMALLER, "
    "about two thirds of its size in Image 1 — its true size, a small shell about 12 cm across and 5 cm tall, only a little wider than "
    "his palm, about as tall as his thumb is long, his fingers and hand showing clearly around it, the band shrinking with it. The "
    "wordmark stays readable.\n\nAVOID: no oversized strap, no strap as wide as his hand with fingers spread, no change to the strap's "
    "shape, no change to his face, no change to the room, no second strap, no extra fingers"))

# B17a v2 — Fix 'GIVE ME DIFFERENT IMAGE HERE' (v1: the strap sat over the tracksuit). Edit of B17c v1 (bare knee, hem bunched above):
# both his hands now at the strap's two chrome-slide ends, pressing it into place — on in one move (FP10).
B["B17a"] = (NBP, ["B17CV1", "R2"], (
    "Edit Image 1. Keep the strap EXACTLY as it is in Image 1 — seated on the bare skin of the tendon directly below the kneecap, the "
    "same shell, peaks, notch, chrome slides and grey stryde wordmark, the same size and place — and keep the leg, the stairs, the light "
    "and the framing. The navy tracksuit leg stays bunched up above the bare knee on its own. Change ONLY his hands: his hand lets go of "
    "the fabric, and BOTH HIS HANDS — THE SAME MAN as in the character sheet (Image 2), strong dark-brown older hands with thick knuckles "
    "— now rest with their fingertips on the strap's two outer chrome-slide ends, one each side, pressing it into place, the thumbs clear "
    "of the wordmark and the notch. A real phone photo.\n\nAVOID: no strap over the fabric, no fabric covering the strap, no strap "
    "moved, no hands on the wordmark, no hands on the band, no fastening, no extra fingers, no extra hands, no second strap"))

# B17b v2 — Fix 'GIVE ME DIFFERENT BROLL HERE' (v1: her fingertip at the strap's edge). "No sores, no rolling down": edit of B15 v1 —
# Maureen coming down onto her bottom stair, the strap still exactly in place under the kneecap.
B["B17b"] = (NBP, ["B15V1", "R1", "P1"], (
    "Edit Image 1. Keep the strap EXACTLY as it is in Image 1 — the same shell, peaks, notch, chrome slides and grey stryde wordmark, the "
    "same size, seated on the tendon directly below the kneecap, front-on — and keep her pale older leg and denim skirt hem. Change: she "
    "is coming DOWN HER STAIRS towards the camera, as in Image 3 — this knee a little bent as her weight lands on it, her white canvas "
    "plimsoll on the oatmeal carpet of the bottom stair at the foot of the frame; widen a little so the frame holds from the skirt hem "
    "down to her foot, the stair treads and white spindles soft behind her, warm afternoon sun from the right. The strap has not moved. "
    "A real phone photo.\n\nAVOID: no strap moved, no strap rolled down, no strap slipped, no strap higher, no redness on the skin, no "
    "second strap, no tanned skin, no bare feet, no extra legs"))

# B17c v2 — Fix 'GIVE ME DIFFERENT BROLL HERE' (v1: his hand about to drop the hem). "and nobody can see it.": side-on, waist-down,
# Desmond comes down his stairs in navy tracksuit bottoms, the fabric smooth over both knees — nothing shows. No product in frame.
LIGHT["D-SUN-L"] = ("the glass panel of his front door", "left", "warm afternoon sun, soft and golden — the after state, easy and bright, never harsh")
COLOUR["D-STAIRS-SUN"] = ("warm afternoon sunlight", "warm mid-grey walls, charcoal carpet with white nosing stripes, white spindles and skirting",
                          "navy tracksuit bottoms and white trainers with navy trim", "the white nosing stripes", "true to life, warm")
KELVIN["D-STAIRS-SUN"] = 5600
B["B17c"] = (NB2, ["R2", "P2"], photo([
    "A snapshot from a phone held at hip height beside his stairs, side-on to him. He is coming down his stairs easily, caught mid-step: "
    "one foot planted on a stair taking his weight, the other lowering to the stair below, one hand light on the handrail. The frame is "
    "cropped at his waist: it holds his legs in plain navy tracksuit bottoms from the hip down to his trainers and the stair treads. The "
    "soft trouser fabric falls smooth and loose over both knees — no bulge, no outline, nothing showing underneath.",
    R2_LEGS + " Wearing " + TRACKSUIT + " and plain white trainers with navy trim.",
    D_STAIRS,
    angle("B17c", "his legs on the stairs"),
    focus("his trousered knees", deep=False).replace("the room behind", "the hall behind"),
    light("D-SUN-L", "his legs and the stairs"), colour("D-STAIRS-SUN")],
    NO_FACE + ", no torso above the waist, no product anywhere, no knee strap visible, no bulge under the trousers, no outline of anything "
    "under the fabric, no shorts, no bare legs, no logos on the tracksuit, no stripes, " + PLAIN_SHOES + ", no walking stick, no second "
    "person, no extra legs"))

# B17c v3 — "and nobody can see it." User Fix 'FIX THIS, GIVE ME DIFFERENT BROLL' (v2: Desmond on his stairs in tracksuit bottoms).
# Three-quarter at her kitchen table: Maureen in long navy trousers, legs crossed, a cup of tea in both hands — the fabric smooth over
# both knees, nothing shows. Framed from the chin down. No product in frame.
B["B17c"] = (NB2, ["R1", "P4"], photo([
    "A snapshot from a phone at eye level across her kitchen table, three-quarter on. She sits on a wooden chair turned a little out "
    "from the pale-oak table, her legs crossed at the knee, holding a mug of tea in both hands in her lap, about to lift it. The frame "
    "holds her from just below the chin down to her plimsolls: the cardigan, her hands round the mug, and both legs in long navy "
    "trousers. The soft trouser fabric falls smooth and loose over both knees — no bulge, no outline, nothing showing underneath. An "
    "ordinary, easy afternoon.",
    R1_BODY + " Wearing a sage-green cardigan over a white T-shirt, long navy wide-leg cotton trousers to the ankle and white canvas "
    "plimsolls. Her hands: slim, pale, faintly freckled older skin, a plain gold wedding ring.",
    KITCHEN,
    angle("B17c", "her sitting at the kitchen table"),
    focus("her crossed knees and hands", deep=False).replace("the room behind", "the kitchen behind"),
    light("KITCH-R", "her and the table"), colour("KITCH-AM").replace("a dusty-pink cardigan cuff and a yellowed photo album", "a sage-green cardigan and long navy trousers").replace("the faded orange of the old photograph", "the mug of tea")],
    NO_FACE + ", no product anywhere, no knee strap visible, no bulge under the trousers, no outline of anything under the fabric, no "
    "shorts, no skirt, no bare legs, no readable text on the mug, no logos, no second person, no extra hands, no extra fingers, no extra legs"))

# ── 2026-09-30 "FIX THOSE" — B17b, B17c walking on the pavement ────────────────────────────────────────
REFS["B16CV1"] = ("B16c v1 — the shot to edit (Image 1)", "2b9f648e-cf29-49e9-8c84-49836ab0329d")
# B17b v3 — Fix 'USING OR WALKING': edit of B15 v1 — Maureen out walking towards the lens on the pavement, the strap in use, staying put.
B["B17b"] = (NBP, ["B15V1", "R1", "P3"], (
    "Edit Image 1. " + KEEP_WORN.replace(" and keep the leg, the skin and the room.", " and keep her pale older leg and the denim skirt hem.")
    + " Change ONLY her step and the place: she is out WALKING TOWARDS THE CAMERA on THE SAME PAVEMENT as Image 3 — grey paving slabs, "
    "a low garden wall and privet hedge, parked cars, 1930s semis going away, soft and out of focus behind — this leg planted mid-stride, "
    "the knee slightly bent, a white canvas plimsoll on the slab at the foot of the frame; the camera low, near knee height. Warm "
    "afternoon sun from the right. The strap sits exactly where it was, in use. A real phone photo.\n\nAVOID: no strap moved, no strap "
    "rolled down, no strap slipped, no strap higher, no redness on the skin, no second strap, no tanned skin, no bare feet, no running, "
    "no extra legs"))
# B17c v4 — Fix 'WALKING WEARING PANTS': edit of B16c v1 — the same stride on the same pavement, but in long navy trousers: the fabric
# covers the knee and shin, smooth — nothing shows. No product visible.
B["B17c"] = (NBP, ["B16CV1", "R2"], (
    "Edit Image 1. Keep everything in Image 1 exactly as it is — the same pavement, street, light, low camera and framing, the same "
    "stride, the same plain white trainer on the slab. Change ONLY his clothes: instead of khaki shorts he wears long plain navy cotton "
    "trousers to the ankle, straight-leg, soft and a little loose. The trouser leg covers the whole knee and shin down to the trainer; "
    "the fabric falls smooth over the knee with only the natural creases of walking — no bulge, no outline, nothing showing underneath. "
    "No strap is visible anywhere. A real phone photo.\n\nAVOID: no visible strap, no bulge under the trousers, no outline of a strap "
    "under the fabric, no bare knee, no shorts, no rolled-up trousers, no logos on the trainer, no stripes, no extra legs"))

# ── 2026-09-30 B16c ×3 — "Two hundred thousand people wearing one." User Fix 'GIVE ME 3 BROLLS FOR THIS LINE, WALKING WEARING STRYDE'.
# Three different one-off people out walking with the strap on, each an edit of worn_front.jpg (placement stays right, FP03/FP12). ──
def walker(person, clothes, place, light_side, cam="the camera low, near knee height, straight on", extra=""):
    return ("Edit Image 1. " + KEEP_STRAP + " Change ONLY the person, the step and the place: the leg is now " + person + ". Instead of "
            "the dark shorts, " + clothes + ". They are out WALKING TOWARDS THE CAMERA " + place + ", soft and out of focus behind — "
            "this leg planted mid-stride, the knee slightly bent" + extra + "; " + cam + ". Warm afternoon sun from the " + light_side +
            ". A real phone photo.\n\nAVOID: " + EDIT_NEG.replace(", no hairy legs", "") + ", no logos on the shoes, no swoosh, no "
            "brand marks, no running, no extra legs")
B["B16c"] = (NBP, ["PWE"], walker(
    "a British Indian woman in her sixties — warm brown older skin, a few faint creases over the kneecap, real unretouched skin",
    "the hem of a knee-length navy floral cotton skirt just above the knee",
    "along a tarmac path through a green English park — mown grass, big old trees, a wooden bench",
    "left", extra=", a plain white canvas plimsoll on the path at the foot of the frame"))
B["B16c2"] = (NBP, ["PWE"], walker(
    "a white British man about seventy — pale, weathered older skin, grey hairs on the shin, real unretouched skin",
    "the hem of stone-coloured cotton walking shorts just above the knee",
    "along a seaside promenade — pale paving, blue railings, the grey-blue sea and a pale sky",
    "right", cam="the camera low, near knee height, a little to one side so the leg is seen three-quarter on — the strap's front still "
    "facing the camera enough that the wordmark reads", extra=", a plain grey walking shoe on the paving"))
B["B16c3"] = (NBP, ["PWE"], walker(
    "a Black British woman in her late fifties — deep brown skin, smooth with soft creases at the knee, real unretouched skin",
    "the hem of a knee-length khaki cotton skirt just above the knee, a paper shopping bag swinging lightly at her side",
    "along a busy British high-street pavement — shopfronts with no readable signs, other people blurred far behind",
    "left", cam="the camera at knee height, straight on", extra=", a plain tan leather flat on the paving"))

# ── 2026-09-30 "PROCEED TO B18-BR TO B19BR2" ─────────────────────────────────────────────────────────────
REFS.update({"B16AV1E": ("B16a v1 — the shot to edit (Image 1)", "c47a0262-949a-4916-b2b9-f3a4f299e573"),
             "B17BV2": ("B17b v2 — the shot to edit (Image 1)", "9cd0c861-73b5-4458-b5f3-7605104c44d8"),
             "HK1A": ("HK1-a — the hook shot to edit (Image 1)", "661eba13-ffd8-4a6f-8b1c-2bfca7beddcc")})

# B18-BR — "The thing people write to us about most is not the pain." Overhead on the oak table: a small pile of handwritten cards and
# letters, the writing too soft to read; one hand spreading them out. No product.
B["B18-BR"] = (NB2, ["P4"], photo([
    "A snapshot from a phone held straight above the pale-oak kitchen table, looking down. A small loose pile of handwritten cards and "
    "letters on the linen runner — cream and pale blue notepaper, a few greetings cards, envelopes with stamps — the handwriting soft "
    "and out of focus, never readable. One older woman's hand, slim and pale with a plain gold wedding ring and a sage-green cardigan "
    "cuff, spreads them out across the table with her fingertips. Close: the letters and her hand fill the frame.",
    KITCHEN.replace("THE SAME KITCHEN as the attached location plate", "On the table of THE SAME KITCHEN as the attached location plate"),
    angle("B18-BR", "the letters on the table"),
    focus("the hands and what they hold", deep=False).replace("the room behind", "the table edges"),
    light("KITCH-R", "the letters and her hand"), colour("KITCH-AM").replace("a dusty-pink cardigan cuff and a yellowed photo album", "a sage-green cardigan cuff").replace("the faded orange of the old photograph", "the pale blue notepaper")],
    NO_FACE + ", no readable handwriting, no readable text, no names, no addresses, no logos, no product anywhere, no knee strap, no "
    "second hand, no extra fingers"))

# B18a — "It is that the knee stops feeling like a rusty hinge." Edit of B16a v1 (Desmond's strap placed right): he sits down onto his
# bottom stair — the strapped knee bending smoothly, three-quarter on.
B["B18a"] = (NBP, ["B16AV1E", "R2", "P2"], (
    "Edit Image 1. " + KEEP_WORN.replace(" and keep the leg, the skin and the room.", " and keep his leg, skin, khaki shorts and stairs.")
    + " Change ONLY his pose and the angle a little: he is SITTING DOWN onto his bottom stair, caught just before he lands — his strapped "
    "right knee bending smoothly to about a right angle, his foot flat on the hall floor, seen a little from the side, three-quarter on, "
    "at knee height, the strap's front and wordmark still facing the camera. His hands rest loosely on his thighs. The grey stair "
    "carpet with its white nosing stripe behind and under him, as in Image 3. Warm afternoon sun from the right. A real phone photo.\n\n"
    "AVOID: no strap moved, no strap higher, no strap lower, no strap on the side of the knee, no strap over the kneecap, no change to "
    "the strap's shape or size, no second strap, no face, no extra legs, no extra hands"))

# B18b — "They stop planning the stairs before they get to them." Low WIDE from the foot of her stairs: Maureen at the top starting
# straight down, facing forwards, hand light on the rail, the strap on her right knee. Face allowed (after-state).
B["B18b"] = (NBP, ["PF", "R1", "P1"], photo([
    "A snapshot from a phone held low at the foot of her stairs, looking straight up the flight. Maureen is at the top, starting to come "
    "straight down towards the camera, facing forwards, easy and unhurried — her right foot just stepping onto the first stair down, her "
    "left hand resting lightly on the honey oak handrail, a small relaxed smile. On her right leg, just below the kneecap, the black "
    "strap from Image 1, small in this wide frame but clearly the same shell, its chrome slides catching the light. Wide: the whole "
    "flight and her whole figure in frame, small at the top.",
    R1 + " Wearing " + WARD["M-D2"] + ". " + R1_LEGS,
    M_STAIRS,
    angle("B18b", "her coming down the stairs"),
    focus("everything", deep=True),
    light("M-SUN-R", "her and the stairs").replace("from the right of the frame", "from the right of the frame, the half-landing window glowing behind her"), colour("M-STAIRS-SUN")],
    "no strap on the left leg, no second strap, no brace, no sleeve, no walking stick, no stairlift, no second person, no looking into the "
    "lens, no posing, no readable text, no logos on the plimsolls, no wrong number of legs"))

# B19-BR — "And you do not have to take my word for any of it." From behind at the foot of her stairs: Maureen holds one strap in her
# hand at her side and looks up the flight. The strap as in B13 v6 (true size, held).
B["B19-BR"] = (NBP, ["PF", "B13V6", "R1", "P1"], photo([
    "A snapshot from a phone at eye level in the hall, behind her. Maureen stands at the foot of her stairs, her back to the camera, "
    "looking up the flight. In her right hand, held down at her side and turned a little towards the camera, is the strap from Image 1 "
    "— the matte-black shell with two rounded peaks, the chrome slides, the grey stryde wordmark readable — at its true size, resting "
    "across her fingers the way it rests in the hand in Image 2, the soft black band hanging below. Medium: her from the hair to her "
    "plimsolls, the stairs rising ahead of her.",
    R1 + " Wearing " + WARD["M-D2"] + ". Her face is not seen — only the back of her soft white hair.",
    M_STAIRS,
    angle("B19-BR", "her at the foot of the stairs"),
    focus("everything", deep=True),
    light("M-SUN-R", "her and the stairs"), colour("M-STAIRS-SUN")],
    "no face, no strap worn, no second strap, no oversized strap, " + P.NEG_WORDMARK + ", " + PROD_NEG + ", no second person, no "
    "readable text, no extra hands, no extra fingers"))

# B19a — "Put one on one knee only. Leave the other bare." Edit of B17b v2: she now sits on her bottom stair, both knees side by side
# seen from above — the strap on the right knee, the left knee bare.
B["B19a"] = (NBP, ["B17BV2", "R1", "P1"], (
    "Edit Image 1. " + KEEP_WORN.replace(" and keep the leg, the skin and the room.", " and keep her pale older legs, denim skirt and stairs.")
    + " Change ONLY her pose and the view: she is SITTING on her bottom stair, both knees bent side by side, seen from above as she looks "
    "down at them — the strap on her RIGHT knee exactly as in Image 1, her LEFT knee BARE, nothing on it. Her two hands rest on her "
    "thighs above the knees. Both kneecaps clearly visible. Warm afternoon sun from the right. A real phone photo.\n\nAVOID: no strap on "
    "the left knee, no second strap, no strap moved, no strap over the kneecap, no face, no extra legs, no extra hands"))

# B19b — "Go to your own stairs and come down forwards." Edit of HK1-a (the hook's view through the spindles): the same view, now in the
# after state — denim skirt, warm sun, and the strap from Image 2 on her right knee.
B["B19b"] = (NBP, ["HK1A", "PW", "R1"], (
    "Edit Image 1. Keep the same view as Image 1 — through the white stair spindles, side-on, low, her legs coming down her stairs "
    "forwards, one hand on the oak handrail. Change: she now wears a mid-blue denim skirt ending just above the knee and a sage-green "
    "cardigan; the light is warm afternoon sun; and on her RIGHT knee, on the tendon just below the kneecap, she wears the strap as in "
    "Image 2 — a black shell with two rounded peaks cupping the base of the kneecap and a chrome slide at each side, the black band "
    "running round the leg — seen from the side, slim and flush. She comes down easily. A real phone photo.\n\nAVOID: no strap over the "
    "kneecap, no strap on the left leg, no second strap, no brace, no sleeve, no walking stick, no face, no extra legs"))

# B19-BR2 — "You will know in a minute. …" CU side-on: her hand lets go of the oak handrail mid-step as she comes down steadily.
B["B19-BR2"] = (NB2, ["R1", "P1"], photo([
    "A snapshot from a phone at eye level beside her stairs, side-on, close on the honey oak handrail. Her hand — slim, pale, faintly "
    "freckled, a plain gold wedding ring, a sage-green cardigan cuff — is just lifting off the rail as she comes down, the fingers "
    "opening, a few centimetres of air between palm and wood. Close: her hand and the rail fill the frame, the white spindles and the "
    "hall soft behind.",
    M_STAIRS,
    angle("B19-BR2", "her hand leaving the handrail"),
    focus("the hands and what they hold", deep=False).replace("the room behind", "the hall behind"),
    light("M-SUN-R", "her hand and the rail"), colour("M-STAIRS-SUN")],
    NO_FACE + ", no product anywhere, no knee strap, no second hand, no extra fingers, no gripping the rail tightly, no readable text"))

if __name__ == "__main__":
    out = HERE / "prompts"; out.mkdir(exist_ok=True)
    for b in sys.argv[1:] or B:
        model, refs, p = B[b]
        assert "[" not in p.replace("[slowly]", ""), (b, p[p.index("["):p.index("[") + 80])
        (out / f"{b}.t2i.txt").write_text(p)
        (out / f"{b}.refs.json").write_text(json.dumps(dict(model=model, refs=[REFS[k] for k in refs]), indent=1))
        print(b, model, len(p), "chars", [REFS[k][0] for k in refs])
