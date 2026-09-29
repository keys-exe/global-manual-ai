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
        "P4": ("P4-KITCHEN plate", "0bedfad5-bf20-4ebd-a862-fed90b55601a")}
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

# B06 v4 — user Fix 'MORE ARROWS, MORE DETAILS' on "Seventeen times your bodyweight is still arriving, every step, in exactly the
# same place." (v3: one pointer arrow). Several force arrows now carry the bodyweight down the thigh and converge on the one tendon spot,
# plus the pointer; more anatomical detail. Still no text. Pip (host cut-out bottom-left): knee upper right.
B["B06"] = (NB2, [], anat(
    "Seen from a low three-quarter angle, CAUGHT MID-STEP: the leg bending under a landing, the foot just striking the ground below the "
    "frame, the thigh muscles visibly tensed and bulging with the load, the knee flexed — the body's weight coming down through it. In "
    "very rich, high anatomical detail: the four heads of the quadriceps each distinct with fine fibre striation and pearly tendon sheaths, "
    "the quadriceps tendon sweeping over the kneecap, the kneecap with its textured bony surface and its smooth cartilage underside, the "
    "patellar tendon as a banded, fibrous ribbon drawn taut with its long fibres visible, the infrapatellar fat pad and the small bursa "
    "behind it, the joint capsule as a thin translucent sleeve, the two crescent menisci, the collateral ligaments at the sides, the "
    "cruciate ligaments crossing deep inside, fine blood vessels threading over the bone, the bone ends with porous trabecular texture — "
    "and the cartilage between the bones visibly THIN and worn. SEVERAL FORCE ARROWS: five or six smooth, slightly glowing white-to-amber "
    "arrows run DOWN the front and sides of the thigh from the top of the frame, following the line of the leg like the body's weight "
    "pouring down, all CONVERGING on the one same spot on the patellar tendon just below the kneecap; plus one larger clean white pointer "
    "arrow outside the leg in the dark field pointing precisely at that spot. The arrows are crisp medical-illustration graphics, no "
    "text, no label, no number on any of them. THE KNEE SITS IN THE UPPER RIGHT OF THE FRAME; the lower-left third of the frame is calm "
    "near-black field with nothing in it (a person will be placed there later). "
    + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from a low three-quarter angle, foreshortened, the knee joint in the upper right of the frame, the lower-left third "
         "empty field")
    .replace("no arrows, no force arrows, ", "no arrows pointing anywhere but the tendon spot, ").replace("no diagram markings, ", "").replace("no annotations, ", "")
    .replace("no individual muscle fibres, ", "").replace("no surface veins, ", "")
    .replace("never fine striation and never individual fibres", "fine striation readable"))

# B06-BR2 — user "The load does not thin with it — BROLL HERE". Desmond on the pavement, knee-height side-on: one heavy step, his
# whole weight landing on the knee. Faceless; plain trainers.
# v2 — user Fix 'FOCUS ON KNEE' (v1: both legs, shorts to trainers, the knee small): a close-up on the landing right knee.
B["B06-BR2"] = (NB2, ["R2", "P3"], photo([
    "A close-up snapshot from a phone held at knee height on the pavement, side-on, close in. He is walking along the pavement from the "
    "left of the frame to the right, caught as his right foot lands and takes his whole weight: THE RIGHT KNEE FILLS THE MIDDLE OF THE "
    "FRAME, bending a little under the load, the kneecap and the band of tendon below it standing out under the skin, the lower thigh "
    "muscle firm above it and the top of the shin below. The frame holds only the knee, from just below the shorts hem to the middle of "
    "the shin — no feet, no trainers, no other leg in focus; the other leg is only a soft dark shape behind. The street behind is a soft "
    "grey blur of paving and hedge.",
    R2_BODY + " Wearing dark grey jogging shorts ending just above the knee.",
    STREET,
    angle("B06-BR2", "his right knee"),
    focus("his right knee and the tendon below the kneecap", deep=False).replace("the room behind", "the street behind"),
    light("STREET-AM-L", "his knee"),
    colour("STREET-AM").replace("navy skirt and white plimsolls", "dark grey jogging shorts")],
    NO_FACE + ", no torso, no hands, no product anywhere, no knee strap, no knee support, no walking stick, no limp, no second person, "
    "no dog, no number plates, no readable signs, no feet in frame, no shoes in frame, no wrong number of legs"))

# B08-BR — first sentence of B08-TH: "Nothing about the way you walk changed, so you assume nothing changed." (user Fix: B-roll here).
# Maureen from behind, walking down her hall towards the front door, ordinary and unhurried.
B["B08-BR"] = (NB2, ["R1", "P1"], photo([
    "A snapshot from a phone at eye height at the foot of her stairs, looking down her hall towards the front door. She is walking away "
    "from the lens down the hall at an ordinary, unhurried pace, caught mid-stride: her right foot planted, her left heel lifting behind. "
    "Medium shot from behind, her whole figure small in the frame, the front door with its glass panel at the end of the hall, the half-moon "
    "hall table beside it. Her face is not visible — only the back of her head and her soft white hair.",
    R1_BODY + " " + R1_LEGS + " Wearing " + WARD["M-D1"] + ".",
    M_STAIRS + " The half-moon hall table with a key bowl and a blue-and-white vase of dried lavender stands just inside the front door.",
    angle("B08-BR", "her walking down the hall"),
    focus("everything"),
    light("M-GREY-R", "her and the hall"), colour("M-STAIRS-AM")],
    "no face visible, no turning round, no looking back, no limp, no walking stick, no product anywhere, no knee strap, no second person, "
    "no readable text, no wrong number of legs"))

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

# B08a — "Some of the people it happens to have never run a mile in their life." Maureen picks up her keys. Face in frame.
B["B08a"] = (NB2, ["R1", "P1"], photo([
    "A snapshot from a phone at eye height in her hall, three-quarter on. She stands at the small half-moon hall table by the front door and "
    "lifts her keys out of the blue-and-white china bowl on it, about to go out, a straw sunhat and a navy raincoat on the coat stand "
    "behind. Medium shot from the knees up, her face three-quarter to the camera, looking down at the keys.",
    R1 + " Wearing " + WARD["M-D1"] + ".",
    M_STAIRS + " The half-moon hall table with a key bowl and a blue-and-white vase of dried lavender stands just inside the front door.",
    angle("B08a", "her at the hall table"),
    focus("her nearest eye", deep=False).replace("the room behind", "the hall behind"),
    light("M-GREY-L", "her face and hands"), colour("M-STAIRS-AM")],
    "no product anywhere, no knee strap, no running gear, no second person, no looking at the camera, no readable text"))

# B08b — "Others played sport for thirty years." Over Desmond's shoulder: he straightens a team photo. Back of head only.
B["B08b"] = (NB2, ["R2", "P2"], photo([
    "A snapshot from a phone just behind his right shoulder, at eye height. He is on the lower stairs straightening one of the black-framed "
    "football team photographs on the stair wall, the fingertips of his right hand levelling its bottom corner. Close: the soft edge of "
    "his shoulder and the back of his close-cropped grey-white head in the near foreground, his hand and the frame sharp beyond. In the "
    "photograph, a young amateur team in two rows — the players too small and soft to make out, no readable writing.",
    "THE SAME MAN as in the attached character sheet of him, seen only from behind: close-cropped grey-white hair, dark brown skin, the "
    "navy zip-neck sports top. His hand: dark brown older skin, thick knuckles, real unretouched skin.",
    D_STAIRS,
    angle("B08b", "his hand on the team photo", ", looking past his shoulder, soft in the near foreground"),
    focus("his hand and the frame", deep=False).replace("the room behind", "the wall around it"),
    light("D-GREY-R", "his hand and the photo"), colour("D-STAIRS-AM")],
    "no face, no profile of the face, no product anywhere, no readable text, no names, no trophies, no second person, no extra fingers"))

# B08c — "It is coming from standing up and walking." Desmond seated on the bottom stair, rising. Face in frame.
B["B08c"] = (NB2, ["R2", "P2"], photo([
    "A snapshot from a phone held low in the hall, three-quarter on. He is getting up off the bottom stair where he has just tied his "
    "trainers, caught just as he starts to rise: his weight coming forward over his feet, both hands pushing off his knees, his bare knees "
    "bent and starting to straighten, his face three-quarter to the camera, looking ahead, matter-of-fact. Medium shot, the whole of him "
    "from head to trainers.",
    R2 + " Wearing " + WARD["D-D1"] + ".",
    D_STAIRS,
    angle("B08c", "him rising off the bottom stair"),
    focus("everything", deep=True),
    light("D-GREY-L", "him and the stairs"), colour("D-STAIRS-AM")],
    "no wincing, no pain face, no product anywhere, no knee strap, no second person, " + PLAIN_SHOES + ", no looking at the camera"))

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

if __name__ == "__main__":
    out = HERE / "prompts"; out.mkdir(exist_ok=True)
    for b in sys.argv[1:] or B:
        model, refs, p = B[b]
        assert "[" not in p.replace("[slowly]", ""), (b, p[p.index("["):p.index("[") + 80])
        (out / f"{b}.t2i.txt").write_text(p)
        (out / f"{b}.refs.json").write_text(json.dumps(dict(model=model, refs=[REFS[k] for k in refs]), indent=1))
        print(b, model, len(p), "chars", [REFS[k][0] for k in refs])
