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

# B04a — "Going up the stairs, your muscles lift you." Desmond from behind and below, climbing.
B["B04a"] = (NB2, ["R2", "P2"], photo([
    "A snapshot from a phone held low at the foot of the stairs, looking up the flight from behind him. He is climbing his stairs, caught "
    "mid-step: his right foot planted two treads up and his right thigh driving him upwards, the back of the thigh and calf working, "
    "his left heel lifting off the tread below, his right hand on the dark handrail. The frame is cropped at his waist — his back, "
    "shoulders and head are above the frame.",
    R2_BODY + " Wearing " + WARD["D-D1"] + ".",
    D_STAIRS,
    angle("B04a", "his legs climbing the stairs"),
    focus("everything", deep=True),
    light("D-GREY-R", "his legs and the flight"), colour("D-STAIRS-AM")],
    NO_FACE + ", no torso above the waist, no product anywhere, no knee strap, no second person, " + PLAIN_SHOES + ", no going down the stairs, no wrong number of legs"))

# B04b — "Going down, nothing lifts you. You are catching yourself on every step," Desmond side-on through the spindles, stepping down.
B["B04b"] = (NB2, ["R2", "P2"], photo([
    "A snapshot from a phone held at hip height beside the stairs, looking side-on at the flight through the white spindles. He is coming "
    "DOWN, caught at the landing of a step: his right foot just landed on the tread below, the right knee bending deeply to catch his "
    "weight, his left leg still on the tread above, his left hand sliding on the dark handrail. The frame is cropped at his waist.",
    R2_BODY + " Wearing " + WARD["D-D1"] + ".",
    D_STAIRS,
    angle("B04b", "his legs coming down the stairs", ", looking past the white spindles, soft in the near foreground"),
    focus("everything", deep=True),
    light("D-GREY-L", "his legs and the stairs"), colour("D-STAIRS-AM")],
    NO_FACE + ", no torso above the waist, no product anywhere, no knee strap, no second person, " + PLAIN_SHOES + ", no going up the stairs, no wrong number of legs"))

# B04c — "so coming down puts more through that band than going up does." ANAT-C silhouette, only the tendon legible.
B["B04c"] = (NB2, [], anat(
    "Seen from a high three-quarter angle: the knee bent under a downward step, the foot just landing on a step below, the whole leg a dark "
    "translucent silhouette with only the patellar tendon legible inside it, glowing where the landing loads it. "
    + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from a high three-quarter angle, the bent knee in the middle of the frame, the shin angled down to the landing foot on "
         "a faint step below", stack="ANAT-C", slots={"[STACK]": "the surrounding soft tissue"}))

# B05 — cartilage thins. ANAT-B ghost limb, the joint cut away, target = the cartilage. No glow — a condition beat.
B["B05"] = (NB2, [], anat(
    "Seen from the side, in profile, the joint opened in a clean cutaway: the rounded end of the femur above, the flat top of the tibia "
    "below, and between them the smooth pale cartilage layer lining both bone ends — pearly, slightly translucent, visibly thinner at the "
    "front of the joint where the load lands than at the back. Calm, no glow, no emission; the thinning reads by thickness alone.",
    view="viewed from the side, in profile, the knee joint large in the middle of the frame, cut away cleanly so the inside of the joint "
         "is visible", stack="ANAT-B",
    slots={"[TARGET]": "the cartilage lining the joint surfaces"}).replace("the patellar tendon crisp", "the cartilage crisp"))

# B06 — pip (host cut-out bottom-left): the thinner joint, load still arriving at the same spot. Knee upper right.
B["B06"] = (NB2, [], anat(
    "Seen from a low three-quarter angle: the knee under load, the cartilage between the bones visibly thin, the load still arriving at "
    "the same spot below the kneecap. THE KNEE SITS IN THE UPPER RIGHT OF THE FRAME; the lower-left third of the frame is calm near-black "
    "field with nothing in it (a person will be placed there later). " + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from a low three-quarter angle, foreshortened, the knee joint in the upper right of the frame, the lower-left third "
         "empty field"))

# B07 — "That is why it feels like it arrived overnight." Maureen at the top of her stairs, looks down and stops. Face in frame.
B["B07"] = (NB2, ["R1", "P1"], photo([
    "A snapshot from a phone held a little above her, on the landing, three-quarter on. She stands at the top of her stairs, her left hand "
    "on the oak handrail, about to go down, and has stopped: she looks down the flight, her mouth closed, a small hesitation — not "
    "pain, just pausing to think about the first step. Medium close-up: head, shoulders and hands, the top of the flight falling away "
    "below her.",
    R1 + " Wearing " + WARD["M-D1"] + ".",
    M_STAIRS,
    angle("B07", "her at the top of the stairs"),
    focus("her nearest eye", deep=False).replace("the room behind", "the stairs below"),
    light("M-GREY-R", "her face and hands"), colour("M-STAIRS-AM")],
    "no crying, no wincing, no hand on her knee, no product anywhere, no knee strap, no walking stick, no stairlift, no second person, "
    "no looking at the camera"))

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
B["B03-BR"] = (NB2, ["R1", "P4"], photo([
    "A snapshot from a phone held straight above the kitchen table, looking down. A family photo album lies open on the pale-oak table, "
    "its thick card pages yellowed, a few old colour photographs held in by corner mounts. The main photograph, faded to warm oranges and "
    "soft blues the way 1970s prints fade: a teenage girl of about fifteen with white-blonde hair mid-stride along a seaside promenade in "
    "summer, laughing, bare legs, sandals, the sea wall and railings behind her. An older woman's hand rests on the edge of the page, "
    "about to turn it. Close: the frame holds the open album, the photographs and her hand — nothing else of her.",
    "Her hand: THE SAME WOMAN as in the attached character sheet — slim, pale, faintly freckled older skin, thin skin over the knuckles, a "
    "plain gold wedding ring, the dusty-pink cardigan cuff at the wrist.",
    KITCHEN,
    angle("B03-BR", "the open album"),
    focus("the teenage girl's photograph", deep=False).replace("the room behind", "the table around it"),
    light("KITCH-L", "the album and her hand"), colour("KITCH-AM")],
    "no thumb held against anything, no measuring, no readable text, no handwriting, no captions, no dates, no names, no logos, no face of "
    "the older woman, no second hand, no extra fingers, no product anywhere, no knee strap"))

if __name__ == "__main__":
    out = HERE / "prompts"; out.mkdir(exist_ok=True)
    for b in sys.argv[1:] or B:
        model, refs, p = B[b]
        assert "[" not in p.replace("[slowly]", ""), (b, p[p.index("["):p.index("[") + 80])
        (out / f"{b}.t2i.txt").write_text(p)
        (out / f"{b}.refs.json").write_text(json.dumps(dict(model=model, refs=[REFS[k] for k in refs]), indent=1))
        print(b, model, len(p), "chars", [REFS[k][0] for k in refs])
