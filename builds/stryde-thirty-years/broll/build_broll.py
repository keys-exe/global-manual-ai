#!/usr/bin/env python3
"""Step 7 body B-roll start images for stryde-thirty-years (act map work/actmap.json, E6 lengths work/broll/lengths_HK1.json).

Mode 1 lifestyle beats: §22T short candid seed (CAM-LOCK → prose → REF-PROD → light → CAP-FILE → negatives) plus the
§30I–§30L lines (ANGLE-LINE, FOCUS-LINE, LIGHT-SHOT, COLOUR-KEY). Product blocks from the STRYDE product sheet module,
anatomy from Appendix A (ANAT-BASE + ANAT-LIGHT + ANAT-FIELD + ANAT-A/B, the sheet's slots, ANAT_A_POINT_TIGHT).
Route (user, stryde builds 2026-09-28): realistic B-roll → Higgsfield nano_banana_pro; anatomy → Higgsfield nano_banana_2.
Writes broll/<BEAT>.t2i.txt and broll/broll_v1.json ({beat: {model, refs, prompt, act, line, call_s}}).
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
    return m.group(1).strip()


ROWS = {r["beat"]: r for r in json.loads((BUILD / "work/actmap.json").read_text())}
LEN = {r["beat"]: r for r in json.loads((BUILD / "work/broll/lengths_HK1.json").read_text())["lengths"]}

# ── people ──────────────────────────────────────────────────────────────────────
S1_FACE = ("a long, angular face with a strong straight nose, high flat cheekbones, wide-set blue eyes and a thin wide mouth; "
           "large ears that stand well out from the head, clearly visible with the hair tucked behind them; the right eyebrow a little "
           "higher than the left; chin-length straight hair dyed dark brown and grown out, two inches of silver roots at the parting, "
           "tucked behind the ears. A white British woman of sixty-nine, tall and lean, long legs, a slight forward stoop at the shoulders")
S1 = "THE SAME WOMAN exactly as in the attached character sheet of her — " + S1_FACE + " — unchanged in face, age and build."
C1_FACE = ("a narrow, hollow-cheeked face with a long jaw, deep-set pale grey eyes under a low brow, a neat grey moustache, no beard; "
           "a hooked nose broken once and set crooked, the tip bent clearly to his left; the left side of the mouth a little higher than "
           "the right; thin grey hair combed straight back. A white British man of sixty-two, short and wiry, sinewy forearms")
C1 = "THE SAME MAN exactly as in the attached character sheet and talking-head photo of him — " + C1_FACE + " — unchanged in face, age and build."
C1_HANDS = ("His hands, the same sixty-two-year-old maker's hands as the attached references: big-knuckled, sinewy, weathered, sun spots "
            "on the backs, nails short with dried glue under them, the rolled cuffs of a green-and-brown check flannel shirt at the "
            "forearms and the faded navy canvas apron behind.")
WARD = {
    "M-D1": "his green-and-brown check flannel shirt with the sleeves rolled, the faded navy canvas work apron, grey work trousers, brown leather work boots",
    "W-D0": "a dusty-pink polo-neck jumper, a heather-grey wool skirt ending a hand above the knee so both knees are bare, sheepskin slippers",
    "W-D1": "a white cotton blouse under a cornflower-blue cardigan, a dark green corduroy skirt ending a hand above the knee so both knees are bare, tan leather ankle boots",
    "W-D2": "a mustard lambswool crew-neck jumper, a navy corduroy A-line skirt ending a hand above the knee so both knees are bare, tan leather ankle boots",
    "W-D3": "a chambray shirt under the green waxed jacket from her hall hook, stone walking shorts ending just above the knee, tan leather ankle boots",
}
SKIN_LEG = P.LEG_SKIN.replace("about sixty", "about seventy")

# ── places, light and colour (STEP4_5.md light plans and COLOUR-KEYs) ────────────
BENCH = ("THE SAME WORKSHOP as the attached location plate: the long scarred dark-beech workbench, the blue cast-iron vice at its end, "
         "the pegboard of shears, punches and rivet setters on the whitewashed brick, the tall iron-framed east factory windows along the bench wall.")
RAIL = ("THE SAME WORKSHOP as the attached location plate, the rail aisle: the long steel rail of finished knee braces on hangers down one "
        "side, the concrete floor, the timber trusses above, the bench and its tall windows across the room.")
STAIRS = ("THE SAME HALL AND STAIRS as the attached house plate: cream plaster walls scuffed along the stairs, orange-varnished pine handrail "
          "and white spindles, pale fawn twist-pile carpet, plain pine skirting; the straight flight rises on the LEFT as you face in from the front door.")
LIVING = ("THE SAME LIVING ROOM as the attached room plate: cream walls, pale fawn carpet, the bottle-green wing armchair, the dark oak "
          "sideboard, the south patio doors on the far wall.")
LANE = ("A narrow English village lane near her house: grey tarmac with a grass strip down the middle, tall green hedges either side, a grey "
        "five-bar field gate set into the hedge ahead.")

LIGHT = {  # source, screen side, quality
    "WS-L": ("the low morning sun through the tall east factory windows along the bench wall", "left", "pale, clean early-morning light"),
    "WS-R": ("the low morning sun through the tall east factory windows across the room", "right", "pale, clean early-morning light"),
    "ST-L": ("the landing window at the top of the flight and the frosted front-door glass", "left", "soft, cool-neutral north light, no direct sun"),
    "ST-R": ("the landing window at the top of the flight and the frosted front-door glass", "right", "soft, cool-neutral north light, no direct sun"),
    "LV-AM": ("the mid-morning sun low through the south patio doors", "right", "warm mid-morning sun with a sun patch on the carpet"),
    "LV-PM": ("the flat grey sky through the south patio doors, the curtains half drawn", "right", "flat, grey, cooler afternoon light"),
    "LANE": ("the bright overcast sky", "front", "bright, even overcast morning light"),
}
COLOUR = {
    "WORKSHOP": ("pale east morning daylight, clean and slightly cool", "whitewashed grey-white brick, grey concrete, dark oiled beech, the blue cast-iron vice, black neoprene",
                 "a green-and-brown check shirt and a faded navy apron", "the blue vice and the black strap", "slightly muted"),
    "FIT": ("pale east morning daylight, clean and slightly cool", "whitewashed grey-white brick, grey concrete, dark oiled beech, the blue cast-iron vice",
            "white and cornflower blue with a bottle-green skirt on her, a green-and-brown check shirt and a navy apron on him", "the black strap", "slightly muted"),
    "STAIRS": ("soft cool-neutral north light", "cream walls, pale fawn carpet, orange pine handrail, white spindles", "mustard yellow, navy cord and tan boots",
               "the mustard jumper and the black strap", "true to life"),
    "LIV-AM": ("warm mid-morning sun from the south", "cream walls, fawn carpet, bottle-green velour armchair, dark oak", "mustard, navy and tan",
               "the green armchair", "a touch warm"),
    "LIV-PM": ("flat grey afternoon, cooler, curtains half drawn", "cream walls, fawn carpet, bottle-green velour armchair, dark oak", "dusty pink, heather grey and sheepskin",
               "the beige sleeve", "muted"),
    "LANE": ("bright overcast morning", "grey tarmac, green hedges, a grey five-bar gate", "chambray blue, a green waxed jacket, stone shorts and tan boots, with a wheaten border terrier on a red lead",
             "the red dog lead", "true to life"),
}


def light(key, subj):
    src, side, q = LIGHT[key]
    if side == "front":
        return f"THE LIGHT: {src} lights {subj} evenly from in front and above, {q}; soft shadows under the chin and the hedges, one way only."
    return (S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", src)
            .replace("[SUBJECT]", subj).replace("[SCREEN SIDE]", side).replace("[TIME-OF-DAY QUALITY and the act's light state]", q)
            .replace("[SIDE]", "the " + side)).replace(
            "" if subj in ("her", "him") else "so the face has a lit side toward the " + side + " and a softer shadow side, with a small catchlight in the eyes",
            "" if subj in ("her", "him") else "so it has a lit side toward the " + side + " and a softer shadow side")


def colour(key):
    lc, sc, wc, ac, sat = COLOUR[key]
    return (S("COLOUR-KEY").replace("[LIGHT COLOUR]", lc).replace("[SET COLOURS]", sc).replace("[WHO] wears [WARDROBE COLOURS]", "the wardrobe is " + wc)
            .replace("[ACCENT]", "the accent is " + ac).replace("[SATURATION AND CONTRAST IN CAMERA]", sat)
            .replace(", exactly as in the attached master frame", ""))


HEIGHT = {"overhead": "an overhead camera looking straight down", "high": "a high camera looking down", "eye": "an eye-level camera",
          "low": "a low camera close to the floor looking up", "ground": "a camera at ground level"}
SIDE = {"front": "the front", "three-quarter": "three-quarter", "profile": "the side, in profile", "three-quarter-back": "three-quarter behind",
        "behind": "directly behind", "ots": "over the shoulder"}


def angle(beat, subj, fg=""):
    r = ROWS[beat]
    return (S("ANGLE-LINE").replace("[HEIGHT CLAUSE from §30I]", HEIGHT[r["height"]]).replace("[SIDE]", SIDE[r["side"]]).replace("[SUBJECT]", subj)
            .replace("[, looking past FOREGROUND, soft in the near foreground | , seen in REFLECTION]", fg))


def focus(plane, deep=True):
    return (S("FOCUS-LINE").replace("[PLANE — the nearest eye of NAME / the hands and what they hold / the product and its wordmark / the foreground / everything]", plane)
            .replace("[DEPTH — the room behind falls to a soft, recognisable shape | everything from near to far stays sharp]",
                     "everything from near to far stays sharp" if deep else "the room behind falls to a soft, recognisable shape"))


# ── product ─────────────────────────────────────────────────────────────────────
PROD = P.REF_PROD.replace("the attached reference image", "the attached product photos, front and back").rstrip(" —") + "."
RIGID = "It is a RIGID MOULDED shell with a hard edge, never fabric, never neoprene, never a padded pad."
WORN = P.PLACE_LOCK.replace("[SIDE]", "RIGHT") + " " + P.FIT_SNUG + " " + P.SIZE_WORN
WORN_SHORT = ("The strap sits on her RIGHT knee on the patellar tendon, directly below the kneecap: the notch cups the kneecap's lower "
              "border with no gap, the two peaks no higher than the base of the kneecap's sides, the kneecap's face bare above, a chrome "
              "slide at each outer side of the leg, the black band round the back of the knee, snug on bare skin, the wordmark horizontal. " + P.SIZE_WORN)
WORN_NEG = ("no strap on the left knee, no second strap, no shell over the kneecap, no shell low on the shin, no shell on the thigh, "
            "no uneven peaks, no flat top edge, no shell narrower than the knee, no slide on the front of the knee, no shell rotated to the side, "
            "no strap over clothing, no loose band tail, no fabric pad, no neoprene pad")
REAR = P.ORIENT_LOCK
HELD_NEG = P.NEG_HELD_P + ", no band being pulled tight, no velcro, no buckle"

# ── common tails ────────────────────────────────────────────────────────────────
NEG_BASE = ("no readable text, no logos other than the stryde wordmark, no AI face, no plastic skin, no extra fingers, no fused fingers, "
            "no polished render, no advertising image, no studio lighting, no vignette, no glowing skin, no light from nowhere, "
            "no shadows falling in two directions, no lens flare")
NEG_HANDS = "no wrong finger count, no malformed hands, no hands merging into objects"
NEG_SUP = "no hand on the rail, no hand on the wall, no hand on furniture, no hand pressing on the knee, no reaching for support"
NEG_EFF = "no limping, no wincing, no laboured movement, no eyes fixed on the feet, no hesitation"


def photo(parts, avoid):
    body = [S("CAM-LOCK")] + [p for p in parts if p] + [S("CAP-FILE")]
    return "\n\n".join(body + ["AVOID: " + avoid + ", " + NEG_BASE])


ANAT_SLOTS = {"[REGION]": "knee", "[STACK]": "quadriceps, hamstrings and calf", "[BONES]": "femur, patella and tibia",
              "[TARGET]": "the patellar tendon", "[TARGET JOINT]": "the knee joint", "[SITE]": "the patellar tendon immediately below the kneecap"}
ANAT_NEG_T2I = ("no arrows, no force arrows, no motion lines, no diagram markings, no text overlays, no labels, no numbers, no annotations, "
                "no UI, no watermark, no individual muscle fibres, no surface veins, no emission on the bone shafts, no glow on the tibial "
                "tuberosity, no glow spreading down the shin, no second limb, no clothing, no hands, no people, no x-ray look, no flat "
                "illustration, no cartoon look, no vignette, no darkened frame corners, no limb falling off into darkness, "
                "no hinged brace, no second unit")


def anat(beat, state, extra_neg="", look="A", view=None):
    base = S("ANAT-BASE")
    if view:
        base = base.replace("viewed from a low three-quarter angle, foreshortened, [TARGET JOINT] sitting slightly off-centre and dominating the frame", view)
    t = "\n\n".join([base, S("ANAT-LIGHT"), S("ANAT-FIELD"), S("ANAT-A") if look == "A" else S("ANAT-B"), state,
                     "AVOID: " + ANAT_NEG_T2I + (", " + extra_neg if extra_neg else "") + ", " + S("NEG-EXTERNAL")])
    for k, v in ANAT_SLOTS.items():
        t = t.replace(k, v)
    return t


B = {}   # beat -> (model, refs, prompt)
NBP, NB2 = "nano_banana_pro", "nano_banana_2"

# ── Act 1 ───────────────────────────────────────────────────────────────────────
B["MECH-01"] = (NB2, [], anat("MECH-01",
    "Seen from the side, in profile, the knee mid-stride with the foot planted and the limb carrying the body's weight. "
    + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="viewed from the side, in profile, the whole knee joint in the middle of the frame with the thigh above and the shin below"))
B["BR-02"] = (NBP, ["C1", "TH", "S1", "P2"], photo([
    "A snapshot from a phone held high by somebody standing beside the bench, looking down at a fitting. She sits on the tall stool at the "
    "workbench, her right leg straight out, the knee bare between her skirt hem and her boot; his right index fingertip presses into the "
    "tendon just below her right kneecap, the fingertip whole and resting on the skin, the skin dimpling a little under it. Only his hand, "
    "wrist and rolled cuff come in from the left; her hands rest on her thighs. " + C1_HANDS + " Her knee: " + SKIN_LEG,
    "She is " + S1 + " Wearing " + WARD["W-D1"] + ". Her face is out of frame above; only her hands, skirt and legs show.",
    BENCH, angle("BR-02", "her knee"), focus("his fingertip on her knee"), light("WS-L", "the knee and his hand"), colour("FIT")],
    "no strap, no brace, no sleeve on the knee, no second hand, no fingernail digging in, no finger pointing at the lens, " + NEG_HANDS))
B["MECH-02"] = (NB2, [], anat("MECH-02",
    "STATE — ONE SMALL SPOT. The glow sits on [SITE] only, a single tight near-white point on the tendon just below the kneecap; the "
    "cartilage lining the joint and the joint space above it stay dark and calm. " + P.ANAT_A_POINT_TIGHT,
    extra_neg="no glow in the joint space, no glow on the cartilage", look="B",
    view="framed tight on the front of [TARGET JOINT], the kneecap and the tendon below it filling the middle of the frame"))
B["BR-03a"] = (NBP, ["S1", "P0", "front", "back", "worn_front"], photo([
    "A snapshot from a phone held low at the foot of the stairs, tilted up the flight. She is coming DOWN the stairs forwards towards the "
    "camera, caught mid-step: her left foot planted on the third stair from the bottom, the right foot lifting off the step above, her "
    "right hand lifted clear of the handrail and not touching it, eyes ahead down the stairs, mouth shut. The whole of her is in frame "
    "from her hair to her boots. " + S("AFTER-EASE"),
    S1 + " Wearing " + WARD["W-D2"] + ".", STAIRS,
    PROD + " " + RIGID + " " + WORN_SHORT, angle("BR-03a", "her"), focus("the whole figure"), light("ST-L", "her"), colour("STAIRS")],
    WORN_NEG + ", " + NEG_SUP + ", no limping, no wincing, no looking at her feet"))
B["BR-03b"] = (NBP, ["S1", "P1", "front", "back", "worn_bent"], photo([
    "A snapshot from a phone at eye level across the living room. She is standing up from the bottle-green wing armchair in one go, caught "
    "mid-rise: her weight already forward over her feet, her seat just lifting off the cushion, both knees still bent, her hands free at "
    "her sides and not touching the chair arms, eyes ahead, mouth shut. The whole of her is in frame.",
    S1 + " Wearing " + WARD["W-D2"] + ".", LIVING,
    PROD + " " + RIGID + " " + P.PLACE_BENT + " Worn exactly as in the attached bent-knee reference, on her RIGHT knee only.",
    angle("BR-03b", "her"), focus("the whole figure"), light("LV-AM", "her"), colour("LIV-AM")],
    WORN_NEG + ", no hands on the chair arms, no pushing up, no wincing, " + NEG_EFF))
B["BR-03c"] = (NBP, ["S1", "worn_rear", "front", "back"], photo([
    "A snapshot from a phone held at eye level by somebody standing a few steps behind her in the lane. She walks away down the lane, "
    "three-quarter from behind, caught mid-stride, the wheaten border terrier trotting ahead of her on a red lead held loosely in her "
    "left hand; the lane runs away ahead of her to the grey five-bar gate. The whole of her is in frame, small in the lane.",
    S1 + " Wearing " + WARD["W-D3"] + ".", LANE,
    PROD + " Seen from three-quarter behind: only the black band crosses the back of her RIGHT knee, below the hollow, with the edge of "
    "one chrome slide catching the light at the side of the leg, exactly as in the attached rear-worn reference. " + P.SIZE_WORN,
    angle("BR-03c", "her"), focus("the whole figure"), light("LANE", "her"), colour("LANE")],
    "no strap on the left knee, no second strap, no shell on the back of the knee, no wordmark visible from behind, no dog off the lead, "
    "no second dog, no other people, " + NEG_EFF))

# ── Act 2 ───────────────────────────────────────────────────────────────────────
B["BR-05a"] = (NBP, ["C1", "P2"], photo([
    "A snapshot from a phone held flat above the workbench, looking straight down at the scarred dark beech. His two hands are laying "
    "four generic knee supports out in a row across the wood, left to right: a plain beige neoprene knee sleeve, a black hinged knee brace "
    "with steel side bars, a grey knee support with a clear gel ring, and a rolled black elastic knee wrap — the first three already down, "
    "his right hand setting the wrap down at the end of the row, caught mid-placement. All four plain and unbranded. " + C1_HANDS,
    BENCH.replace("the long scarred", "seen from above: the long scarred"), angle("BR-05a", "the bench"), focus("the hands and what they hold"),
    light("WS-L", "the bench"), colour("WORKSHOP")],
    "no strap, no stryde wordmark, no brand names, no labels, no price tags, no packaging, no face, " + NEG_HANDS))
B["BR-05b"] = (NBP, ["C1", "P3"], photo([
    "A snapshot from a phone at eye level in the rail aisle, looking along the rail through the hanging braces. His right hand runs along "
    "the hangers, fingers trailing across them, the nearest braces swinging a little as his hand passes; the hangers hold generic "
    "unbranded knee supports — black and beige neoprene sleeves, hinged braces with steel bars, elastic wraps. " + C1_HANDS +
    " His face is out of frame; his forearm and hand are the subject.",
    RAIL, angle("BR-05b", "his hand", ", looking past the nearest hanging braces, soft in the near foreground"),
    focus("the foreground", deep=False), light("WS-R", "his hand"), colour("WORKSHOP")],
    "no strap, no stryde wordmark, no brand names, no labels, no price tags, no shop, no customers, " + NEG_HANDS))
B["MECH-06"] = (NB2, [], anat("MECH-06",
    "A plain faint translucent sleeve outline wraps the whole knee from mid-thigh to mid-shin, squeezing evenly all round it; beneath it "
    "the single tight near-white glow on [SITE] stays exactly as bright as before, untouched. " + P.ANAT_A_POINT_TIGHT,
    extra_neg="no strap, no rigid shell, no wordmark",
    view="viewed from the front three-quarter, the knee joint in the middle of the frame, the thigh above and the shin below"))
B["BR-07a"] = (NBP, ["S1", "P1"], photo([
    "A snapshot from a phone held high above her, looking down. She sits in the bottle-green wing armchair, her right leg forward, tugging "
    "a plain beige neoprene knee sleeve up over her right knee with both hands, caught mid-tug, the sleeve half over the kneecap, her "
    "shoulders a little rounded, eyes down on the knee, mouth shut. Her face and hands read small and tired. " + SKIN_LEG,
    S1 + " Wearing " + WARD["W-D0"] + ".", LIVING + " The curtains are half drawn.",
    angle("BR-07a", "her"), focus("the hands and what they hold"), light("LV-PM", "her"), colour("LIV-PM")],
    "no strap, no stryde wordmark, no brand name on the sleeve, no sunshine, no smiling, " + NEG_HANDS))
B["BR-07b"] = (NBP, ["C1", "P2"], photo([
    "A snapshot from a phone propped at eye level on the bench. His two hands hold a generic black hinged knee brace with steel side bars "
    "upright on the bench, one hand at each end, pushing the top sideways against the bottom; the steel side bars do not give and the "
    "brace stays straight. " + C1_HANDS,
    BENCH, angle("BR-07b", "his hands"), focus("the hands and what they hold"), light("WS-L", "his hands"), colour("WORKSHOP")],
    "no brace bending, no brace breaking, no strap, no stryde wordmark, no brand names, no face, " + NEG_HANDS))
B["BR-08"] = (NBP, ["S1", "P1"], photo([
    "A snapshot from a phone held high over her right shoulder. She has just pulled the long top drawer of the dark oak sideboard open, "
    "her right hand still on its handle, and the drawer is full to the brim with a tangle of worn knee supports: beige and black neoprene "
    "sleeves, a hinged brace with steel bars, elastic wraps, a gel-pad support, all unbranded and a little grubby. Her shoulder and the "
    "side of her head are soft in the near foreground.",
    S1 + " Wearing " + WARD["W-D0"] + ".", LIVING + " The curtains are half drawn.",
    angle("BR-08", "the drawer", ", looking past her shoulder, soft in the near foreground"), focus("the foreground", deep=False),
    light("LV-PM", "the drawer"), colour("LIV-PM")],
    "no strap, no stryde wordmark, no brand names, no labels, no packaging, " + NEG_HANDS))

# ── Act 3 ───────────────────────────────────────────────────────────────────────
B["BR-10a"] = (NBP, ["C1", "S1", "P2", "front", "back", "worn_front"], photo([
    "A snapshot from a phone held high over the bench, looking down at her knee as he does at a fitting. She sits on the tall stool, her "
    "right leg straight, the strap seated on it; his right index fingertip rests on the skin at the line where her kneecap's lower border "
    "sits in the notch, tracing along it, the fingertip whole and resting lightly. Only his hand and rolled cuff come in from the side. "
    + C1_HANDS + " Her knee: " + SKIN_LEG,
    "Her legs and skirt: " + WARD["W-D1"] + ".",
    PROD + " " + RIGID + " " + WORN_SHORT + " Seated exactly as in the attached front worn reference.",
    BENCH, angle("BR-10a", "her knee"), focus("the product and its wordmark"), light("WS-L", "her knee"), colour("FIT")],
    WORN_NEG + ", no finger covering the wordmark, no finger on the chrome slides, no hand pulling the band, " + NEG_HANDS))
B["BR-10b"] = (NBP, ["S1", "P2", "front", "back", "worn_front"], photo([
    "A snapshot from a phone held at knee height beside her. She stands on the workshop floor by the bench, her right leg straight and "
    "nearest the camera, seen from the side and turned a little towards the lens so the shell's face and wordmark still read; the frame "
    "runs from mid-thigh to mid-shin, the skirt hem at the top. The kneecap's outline stands clear above the shell; the band runs back "
    "round the calf. " + SKIN_LEG,
    "Her skirt and boots: " + WARD["W-D1"] + ".",
    PROD + " " + RIGID + " " + WORN_SHORT + " " + P.PLACE_PROFILE.replace("with the knee bent, ", "with the knee straight, "),
    BENCH, angle("BR-10b", "her right knee"), focus("the product and its wordmark"), light("WS-L", "her knee"), colour("FIT")],
    WORN_NEG + ", no hands in frame, no face"))
B["BR-11"] = (NBP, ["C1", "P2", "front", "back"], photo([
    "A snapshot from a phone propped at eye level on the bench, three-quarter to him. His two hands hold the strap up at chest height "
    "over the bench, front face to the lens, beginning to turn it over: " + dict(P.HELD_GRIPS)["two-hand presentation"].split(" -- ")[0] + ". "
    "The strap is tipped a few degrees in the turn, the wordmark still readable. Nothing rises above the shell's top edge. " + C1_HANDS,
    PROD + " " + RIGID + " " + P.SIZE_HELD + " The band hangs slack below his hands.",
    BENCH, angle("BR-11", "his hands"), focus("the product and its wordmark"), light("WS-L", "his hands"), colour("WORKSHOP")],
    HELD_NEG + ", no face, " + NEG_HANDS))
B["MECH-11"] = (NB2, ["front", "back"], anat("MECH-11",
    "PROTECTION — PRESSURE ON ONE SPOT. The strap is worn on the model exactly as in the attached product photos, its rigid matte-black "
    "shell on [SITE], the notch under the kneecap, the band round the back of the knee. " + S("ANAT-PROD") +
    " Under the pad, the one tight glow on [SITE] is easing, cooling from near-white towards a soft calm amber as the pressure lands on "
    "that single point; the rest of the knee stays calm.", extra_neg="no strap on the thigh, no strap over the kneecap, no sleeve",
    view="viewed from the front three-quarter, the knee joint in the middle of the frame, the thigh above and the shin below"))
B["BR-12"] = (NBP, ["S1", "P0", "front", "back", "worn_rear"], photo([
    "A snapshot from a phone held down at floor level behind her. She stands on the bottom stair facing up the flight, her weight shifting "
    "onto her right leg; the frame is tight on the back of her right knee and calf, from the skirt hem to the top of her boot, the hall "
    "carpet soft below. " + SKIN_LEG,
    "Her skirt and boots: " + WARD["W-D2"] + ".",
    PROD + " Seen from directly behind, exactly as in the attached rear-worn reference: " + REAR,
    STAIRS, angle("BR-12", "the back of her right knee"), focus("the product and its wordmark").replace("the product and its wordmark", "the band and its keeper loops"),
    light("ST-R", "the back of her knee"), colour("STAIRS")],
    P.NEG_ORIENT + ", no strap on the left knee, no face, no hands"))
B["MECH-12"] = (NB2, ["front", "back"], anat("MECH-12",
    "PROTECTION — THE PAD CATCHES THE WEIGHT. Seen from the side, the knee bending as the foot lands on a step below, the body's weight "
    "coming down the thigh. The strap is worn on the model exactly as in the attached product photos, its rigid matte-black shell on "
    "[SITE]. " + S("ANAT-LOAD") + " " + S("ANAT-PROD") + " The load arriving from above lights the pad with a soft cool-white glow that "
    "spreads outward across the width of the shell and away to its two ends, carried off the tendon; [SITE] beneath it and the joint stay "
    "calm and dark.", extra_neg=S("NEG-PROT") + ", no strap on the thigh",
    view="viewed from the side, in profile, the whole knee joint in the middle of the frame with the thigh above and the shin below"))
B["BR-13"] = (NBP, ["S1", "P0", "front", "back", "worn_bent"], photo([
    "A snapshot from a phone at eye level in the hall, looking through the white spindles at the side of the flight. She steps down one "
    "stair forwards, caught mid-step: the right foot reaching down to the next step, the strapped right knee bending, her left leg taking "
    "her weight, her hands free and off the rail, eyes ahead. From her waist to her boots, the spindles soft in the near foreground.",
    S1 + " Wearing " + WARD["W-D2"] + ".", STAIRS,
    PROD + " " + RIGID + " " + P.PLACE_PROFILE + " Worn exactly as in the attached bent-knee reference, on her RIGHT knee only.",
    angle("BR-13", "her", ", looking past the white spindles, soft in the near foreground"), focus("the whole figure"), light("ST-L", "her"), colour("STAIRS")],
    WORN_NEG + ", " + NEG_SUP + ", " + NEG_EFF))
B["BR-14a"] = (NBP, ["C1", "P2", "front", "back"], photo([
    "A snapshot from a phone held above the bench at a slight angle, looking down. His right hand tips a crumpled clear plastic bag and "
    "five cheap copy straps have slid out in a loose heap on the dark beech, one still half in the bag. " + P.FAKE_BASE +
    " These copies have a thin shiny stretchy elastic band and a thin grey foam pad showing at the inside edge of the shell. "
    "Next to the heap, apart from it, lies the real strap for comparison: " + PROD + " " + C1_HANDS,
    BENCH, angle("BR-14a", "the bench"), focus("the foreground"), light("WS-L", "the bench"), colour("WORKSHOP")],
    P.NEG_FAKE_HERO + ", no wordmark on any copy, no labels, no price tags, no face, " + NEG_HANDS))
B["BR-14b"] = (NBP, ["C1", "P2"], photo([
    "A snapshot from a phone propped at eye level on the bench. His two hands hold one cheap copy strap by its two ends and pull the band "
    "apart; the thin shiny elastic band has stretched out long and thin, pale where it is stretched, a loose thread hanging from its edge. "
    + P.FAKE_BASE + " " + C1_HANDS,
    BENCH, angle("BR-14b", "his hands"), focus("the hands and what they hold"), light("WS-L", "his hands"), colour("WORKSHOP")],
    P.NEG_FAKE_HERO + ", no stryde wordmark, no chrome, no labels, no face, " + NEG_HANDS))

# ── Act 4 ───────────────────────────────────────────────────────────────────────
B["BR-15a"] = (NBP, ["C1", "TH", "P2", "front", "back"], photo([
    "A snapshot from a phone propped at eye level on the bench. He holds the strap up towards the lens in his right hand, front face and "
    "wordmark square to the camera: " + dict(P.HELD_GRIPS)["bottom-edge pinch"].split(" (")[0] + ". Nothing rises above the shell's top edge. Behind "
    "the strap his check shirt and navy apron are soft; his face is just out of frame at the top.",
    C1_HANDS, PROD + " " + RIGID + " " + P.SIZE_HELD,
    BENCH, angle("BR-15a", "the strap"), focus("the product and its wordmark"), light("WS-L", "the strap"), colour("WORKSHOP")],
    HELD_NEG + ", " + NEG_HANDS))
B["BR-15b"] = (NBP, ["C1", "TH", "S1", "P2", "front", "back"], photo([
    "A snapshot from a phone held over her shoulder as she sits at the workbench. Across the bench he hands her the strap: his right hand "
    "holds it by the shell's bottom edge, front face and wordmark up, and her right hand comes up from below with the palm open, her "
    "fingertips just touching the pad, caught mid-hand-over. His face is in frame across the bench, looking at the strap, calm; her "
    "shoulder and cardigan sleeve are soft in the near foreground.",
    C1 + " Wearing " + WARD["M-D1"] + ". She is " + S1.replace("THE SAME WOMAN", "the same woman") + " Wearing " + WARD["W-D1"] + ".",
    PROD + " " + RIGID + " " + P.SIZE_HELD,
    BENCH, angle("BR-15b", "him", ", looking past her shoulder, soft in the near foreground"), focus("the hands and what they hold", deep=False),
    light("WS-L", "him"), colour("FIT")],
    HELD_NEG.replace("no product changing hands, ", "") + ", no straightened nose, no symmetrical mouth, " + NEG_HANDS))
B["BR-15c"] = (NBP, ["S1", "P0", "front", "back", "worn_front"], photo([
    "A snapshot from a phone held low beside her. She sits on the bottom stair, her right leg straight out in front on the hall carpet, "
    "bending forward with both hands on the strap on her shin. " + P.SEAT_LOCK.split(" Both hands")[0] + " Both hands hold the shell by "
    "its two sides, palms and fingertips flat on the matte shell, ready to slide it up. " + SKIN_LEG,
    S1 + " Wearing " + WARD["W-D2"] + ". Her face is soft at the top of the frame, eyes on the strap.",
    PROD + " " + RIGID, STAIRS, angle("BR-15c", "her right knee"), focus("the product and its wordmark"), light("ST-L", "her"), colour("STAIRS")],
    P.NEG_SEAT + ", no strap on the left leg, " + NEG_HANDS))
B["BR-16"] = (NBP, ["S1", "P0", "worn_rear", "front", "back"], photo([
    "A snapshot from a phone held high on the landing, looking down the whole flight. She has just started down the stairs forwards, away "
    "from the camera, caught mid-step on the second stair, her hands free and off the rail, the hall far below. One knee strapped, the other "
    "bare: from behind, the black band crosses the back of her RIGHT knee below the hollow; her left knee is bare.",
    S1 + " Wearing " + WARD["W-D2"] + ".", STAIRS.replace("rises on the LEFT as you face in from the front door", "falls away below the landing"),
    PROD + " Seen from behind, exactly as in the attached rear-worn reference: only the band crosses the back of the knee, the edge of one "
    "chrome slide catching the light at the side of the leg. " + P.SIZE_WORN,
    angle("BR-16", "her"), focus("the whole figure"), light("ST-R", "her"), colour("STAIRS")],
    "no strap on the left knee, no second strap, no shell at the back of the knee, " + NEG_SUP + ", " + NEG_EFF))
B["BR-18a"] = (NBP, ["C1", "P2", "front", "back"], photo([
    "A snapshot from a phone propped at eye level on the bench, three-quarter to him. He holds two identical straps up side by side "
    "towards the lens, one in each hand, each by the bottom-edge pinch: thumb in front on the shell's bottom edge below the wordmark, "
    "fingers behind on the pad, the bands hanging slack round his wrists. Both front faces and wordmarks to the camera, level with each "
    "other. Nothing rises above the shells' top edges. " + C1_HANDS,
    PROD + " Two identical units of it, the same size. " + RIGID + " " + P.SIZE_HELD,
    BENCH, angle("BR-18a", "the two straps"), focus("the product and its wordmark"), light("WS-L", "the straps"), colour("WORKSHOP")],
    HELD_NEG.replace("no second strap, ", "") + ", no third strap, no straps of different sizes, no face, " + NEG_HANDS))
B["BR-18b"] = (NBP, ["C1", "P2", "package_open", "front"], photo([
    "A snapshot from a phone held straight above the bench, looking down. His two hands lift the matte-black lid off the box, the lid "
    "tilted up and away at the far edge, caught mid-lift, the inside already showing: " + P.PACKAGE_LOCK + " The box exactly as in the "
    "attached open-box reference. " + C1_HANDS,
    BENCH.replace("the long scarred", "seen from above: the long scarred"), angle("BR-18b", "the box"), focus("the product and its wordmark"),
    light("WS-L", "the box"), colour("WORKSHOP")],
    P.NEG_PACKAGE + ", no face, " + NEG_HANDS))

if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in B.items():
        (HERE / f"{beat}.t2i.txt").write_text(prompt + "\n")
        r = ROWS[beat]
        out[beat] = {"model": model, "refs": refs, "prompt": prompt, "act": r["act"], "phrase": r["phrase"],
                     "call_s": LEN[beat]["call_s"], "chars": len(prompt)}
    (HERE / "broll_v1.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    for b, v in out.items():
        print(b.ljust(8), v["model"].ljust(16), str(v["chars"]).rjust(5), ",".join(v["refs"]))
    assert set(out) == {b for b, r in ROWS.items() if r["type"] in ("BR", "MECH") and not r["act"].startswith("Hook")}, "beat set != act map"
    assert not any("[" in v["prompt"] for v in out.values()), [b for b, v in out.items() if "[" in v["prompt"]]
