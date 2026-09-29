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

LIGHT = {  # source, screen side, quality
    "M-GREY-L": ("the half-landing window at the top of the flight", "left", "grey morning light, soft and indirect from above — the problem state, flat and cool, never moody"),
    "STREET-AM-L": ("the broad overcast morning sky", "left", "flat, grey, cool morning light"),
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
KELVIN = {"M-STAIRS-AM": 6500, "STREET-AM": 6500, "D-STAIRS-AM": 6500}


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
            .replace("[, looking past FOREGROUND, soft in the near foreground | , seen in REFLECTION]", fg))


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


def anat(state, view=None):
    base = S("ANAT-BASE")
    if view:
        base = base.replace("viewed from a low three-quarter angle, foreshortened, [TARGET JOINT] sitting slightly off-centre and dominating the frame", view)
    t = "\n\n".join([base, S("ANAT-LIGHT"), S("ANAT-FIELD"), S("ANAT-A"), state, "AVOID: " + ANAT_NEG_T2I + ", " + S("NEG-EXTERNAL")])
    for k, v in ANAT_SLOTS.items():
        t = t.replace(k, v)
    return t


NBP, NB2 = "nano_banana_pro", "nano_banana_2"
REFS = {"R1": ("R1-MAUREEN sheet", "fd75b478-6a1b-4a8f-ba80-d20f272f65b0"), "R2": ("R2-DESMOND sheet", "9f0903d2-b148-4273-93b6-e4227a87d9f6"),
        "P1": ("P1-PROP-M plate", "520de2e7-e577-4afe-b18c-b79dbed0acf0"), "P2": ("P2-PROP-D plate", "68ddef76-e5b0-4947-966f-cda7e00335c2"),
        "P3": ("P3-STREET plate", "c19e14a9-5146-4444-8b83-e765dfdc3f8f")}
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
B["HK2-a"] = (NB2, [], anat(
    "Seen from the front, the knee straight and standing, the kneecap in the upper middle of the frame and the patellar tendon running down "
    "from its lower edge to the top of the shin. Only the tendon glows; the rest of the joint stays calm, lit but not glowing. No thumb, no hand, "
    "no ruler, nothing held against it for scale. " + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from the front from a slightly low camera looking up, the kneecap and the tendon below it filling the middle of the frame, "
         "the lower thigh above and the upper shin below"))

B["HK2-b"] = (NB2, ["R2", "P2"], photo([
    "A snapshot from a phone held low near the hall floor at the foot of the stairs, three-quarter on to the bottom stair. He is starting UP "
    "his stairs, caught mid-step: his right foot has just planted flat on the bottom stair and his bare right knee is bending as it takes "
    "his weight, his left foot still on the hall floor behind, heel lifting. The frame is cropped at mid-thigh — his face and body are not "
    "in the frame; it holds his shorts hem, his bare right knee and shin, both trainers, the bottom stairs and the hall floor.",
    R2 + " Wearing " + WARD["D-D1"] + ". His legs: dark brown older skin, strong calves, a few grey hairs on the shins, ashy knees with soft "
    "creases, real unretouched skin.",
    D_STAIRS,
    angle("HK2-b", "his right knee and shin on the bottom stair"),
    focus("his right knee", deep=False),
    light("D-GREY-L", "his legs and the bottom stairs"), colour("D-STAIRS-AM")],
    "no face in frame, no product anywhere, no knee strap, no knee support, no walking stick, no handrail grab, no second person, "
    "no person coming down the stairs, no wrong number of legs"))

if __name__ == "__main__":
    out = HERE / "prompts"; out.mkdir(exist_ok=True)
    for b in sys.argv[1:] or B:
        model, refs, p = B[b]
        assert "[" not in p.replace("[slowly]", ""), (b, p[p.index("["):p.index("[") + 80])
        (out / f"{b}.t2i.txt").write_text(p)
        (out / f"{b}.refs.json").write_text(json.dumps(dict(model=model, refs=[REFS[k] for k in refs]), indent=1))
        print(b, model, len(p), "chars", [REFS[k][0] for k in refs])
