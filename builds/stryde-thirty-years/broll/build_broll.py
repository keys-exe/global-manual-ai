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

# ── Fix round 1 (user Fix notes on the board, 2026-09-28 ~17:45) — each replaces its v1 entry ─────────────────
FIX1 = {
 "BR-02": "point under the knee cap", "BR-05a": "make it pov style", "BR-08": "pov style, she's open the drawer",
 "BR-11": "fix the product", "BR-12": "wrong product, wrong position", "MECH-01": "close up the patellar tendon",
 "MECH-02": "remove the patellar tendon show the cartilage", "MECH-06": "create new broll here",
}
POV = ("THIS IS A FIRST-PERSON VIEW: the phone is held at the chest of the person doing it, pointing down and forward the way "
       "their own eyes see, so their own forearms and hands come into frame from the bottom edge; no face of theirs is ever seen.")
B["BR-02"] = (NBP, ["C1", "S1", "P2"], photo([
    "A close snapshot from a phone held a little above her knee. Her right leg is straight out from the stool, the bare knee filling the "
    "middle of the frame from mid-thigh to mid-shin. His right index fingertip presses into the soft hollow directly UNDER her kneecap, "
    "on the tendon just below the kneecap's lower edge, centred on the front of the knee, the skin dimpling under the fingertip; the "
    "kneecap's whole outline sits clear just above his fingertip. Only his hand and rolled cuff come in from the side. " + C1_HANDS +
    " Her knee: " + SKIN_LEG,
    "Her skirt hem and boot: " + WARD["W-D1"] + ".",
    BENCH, angle("BR-02", "her knee"), focus("his fingertip under her kneecap"), light("WS-L", "the knee and his hand"), colour("FIT")],
    "no finger on the side of the knee, no finger on the kneecap itself, no finger on the thigh, no finger on the shin, no strap, "
    "no brace, no sleeve, no second hand, no finger pointing at the lens, " + NEG_HANDS))
B["BR-05a"] = (NBP, ["C1", "P2"], photo([
    POV + " He looks down at the scarred dark beech of his own workbench. His two hands are laying four generic knee supports out in a "
    "row across the wood in front of him, left to right: a plain beige neoprene knee sleeve, a black hinged knee brace with steel side "
    "bars, a grey knee support with a clear gel ring, and a rolled black elastic knee wrap — the first three already down, his right "
    "hand setting the wrap down at the end of the row, caught mid-placement. All four plain and unbranded. The bib of his navy apron "
    "shows at the very bottom edge. " + C1_HANDS,
    BENCH, angle("BR-05a", "the bench"), focus("the hands and what they hold"), light("WS-L", "the bench"), colour("WORKSHOP")],
    "no face, no camera looking down from the ceiling, no third person's view, no strap, no stryde wordmark, no brand names, no labels, "
    "no packaging, " + NEG_HANDS))
B["BR-08"] = (NBP, ["S1", "P1"], photo([
    POV + " She looks down at the dark oak sideboard in front of her. Her own right hand has just pulled its long top drawer open towards "
    "her and is still on the handle, the drawer open and full to the brim with a tangle of worn knee supports: beige and black neoprene "
    "sleeves, a hinged brace with steel bars, elastic wraps, a gel-pad support, all unbranded and a little grubby. Her dusty-pink "
    "polo-neck sleeve runs from the bottom edge to her hand. Real unretouched skin on the back of the hand of a woman of about seventy.",
    LIVING + " The curtains are half drawn.", angle("BR-08", "the drawer"), focus("the foreground", deep=False),
    light("LV-PM", "the drawer"), colour("LIV-PM")],
    "no face, no over-the-shoulder view, no second person, no strap, no stryde wordmark, no brand names, no labels, no packaging, " + NEG_HANDS))
B["BR-11"] = (NBP, ["front", "back", "C1", "P2"], photo([
    "The strap in this photo is THE EXACT SAME OBJECT as the first attached product photo, the front, and the second, the back — only "
    "the view changes. A snapshot from a phone propped at eye level on the bench. His right hand holds the strap up at chest height over "
    "the bench, front face and wordmark square to the lens: " + dict(P.HELD_GRIPS)["bottom-edge pinch"].split(" (")[0] + ". "
    "Nothing rises above the shell's top edge; both peaks and the notch stand clear. " + C1_HANDS,
    PROD + " " + RIGID + " The shell is a hard, thin, curved plate like the product photos, never a soft rounded pad, never a flat "
    "cushion. " + P.SIZE_HELD,
    BENCH, angle("BR-11", "his hand"), focus("the product and its wordmark"), light("WS-L", "his hand"), colour("WORKSHOP")],
    HELD_NEG + ", no soft pad, no cushion, no rounded blob shell, no thick padded shell, no flat oval, no shell without peaks, "
    "no face, " + NEG_HANDS))
B["BR-12"] = (NBP, ["worn_rear", "front", "back", "S1", "P0"], photo([
    "The strap and its position are EXACTLY as in the first attached photo, the rear-worn reference: keep that strap, that band height "
    "and that view, and change only the person, her clothes and the room. A snapshot from a phone held at knee height directly behind "
    "her. She stands on the bottom stair facing up the flight, her weight on her right leg; the frame runs from mid-thigh to mid-calf, "
    "the back of her right knee in the middle of the frame. The black coarse-knit band crosses the back of the leg JUST BELOW the "
    "crease behind the knee, across the very top of the calf — never low down the calf — with the two black keeper loops together at "
    "the centre, and at each side of the leg the edge of the rigid black shell and a brushed chrome slide stand just proud of the "
    "outline, because the shell sits on the front of the knee. " + SKIN_LEG,
    "Her skirt hem and boots: " + WARD["W-D2"] + ".",
    PROD + " " + REAR, STAIRS, angle("BR-12", "the back of her right knee"),
    focus("the product and its wordmark").replace("the product and its wordmark", "the band and its keeper loops"),
    light("ST-R", "the back of her knee"), colour("STAIRS")],
    "no band low on the calf, no band at the ankle, no band on the thigh, no band without shell edges at the sides, no plain wristband, "
    "no watch strap, no loop of webbing, no shell at the back, no wordmark visible from behind, no strap on the left knee, no face, no hands"))
B["MECH-01"] = (NB2, [], anat("MECH-01",
    "CLOSE UP ON THE PATELLAR TENDON: the frame is tight on the front of the knee, the lower half of the kneecap at the top of the "
    "frame and the patellar tendon filling the middle of the frame as a thick pearly band running down to the top of the shin. The "
    "knee is carrying the body's weight. " + S("ANAT-HOT") + " " + P.ANAT_A_POINT_TIGHT,
    view="framed tight on the front of the knee joint, the lower kneecap and the patellar tendon below it filling the frame"))
B["MECH-02"] = (NB2, [], anat("MECH-02",
    "THE CARTILAGE, NOT THE TENDON: the view looks into the knee joint from the front, the joint slightly opened, the smooth pearly "
    "articular cartilage capping the lower end of the femur and the top of the tibia clearly shown, with the two crescent menisci "
    "between them; the cartilage is the subject, picked out in a soft cool pearly white. No glow anywhere and no tendon shown — the "
    "patellar tendon is left out of the model.",
    extra_neg="no patellar tendon, no tendon in front of the joint, no glow, no hot spot, no kneecap covering the joint", look="B",
    view="framed tight on the front of the knee joint, the kneecap lifted away out of the frame so the joint surfaces show"))
B["MECH-06"] = (NBP, ["S1", "P1"], photo([
    "A snapshot from a phone held low in front of her at knee height. She sits in the bottle-green wing armchair, her right leg forward, "
    "the knee bare between her skirt hem and her slipper; the fingertips of her right hand press and rub the spot just UNDER her right "
    "kneecap, on the tendon, the same spot as always, her mouth tight. A plain beige neoprene knee sleeve lies on the chair arm beside "
    "her, taken off. The frame runs from her lap to her ankle, her face just out of frame at the top. " + SKIN_LEG,
    "She is " + S1 + " Wearing " + WARD["W-D0"] + ".", LIVING + " The curtains are half drawn.",
    angle("MECH-06", "her knee"), focus("her fingertips under her kneecap"), light("LV-PM", "her knee"), colour("LIV-PM")],
    "no strap, no stryde wordmark, no brand name on the sleeve, no sleeve on the knee, no fingers on the kneecap itself, no sunshine, "
    + NEG_HANDS))

# MECH-02 fix: the Appendix A anatomy strings name the tendon — swap them for the cartilage (the note: "remove the patellar tendon")
_m, _r, _p = B["MECH-02"]
B["MECH-02"] = (_m, _r, _p.replace("the patellar tendon crisp", "the cartilage crisp").replace("sheen on the patellar tendon", "sheen on the cartilage")
    .replace("Only femur, patella and tibia and the patellar tendon. Bones in warm ivory-gold with soft low inner luminosity; the patellar tendon in pearly ivory-white, dense, running its full length between its attachments.",
             "Only the femur and tibia, the cartilage capping their ends and the menisci between them. Bones in warm ivory-gold with soft low inner luminosity; the cartilage smooth and pearly.")
    .replace("no glow on the tibial tuberosity, no glow spreading down the shin, ", "").replace(", no product cracking, no product deforming", ""))
FIX1_JOBS = {"BR-02": "bfafd47f-ce72-47c4-bcc6-55be31af8dee", "BR-05a": "852d6116-7aa7-476f-9555-2a1514af77af", "BR-08": "d3d166aa-f7c9-46f8-b42f-17f4c23912a7",
             "BR-11": "b1d142ef-2753-4713-bd86-3f7e7e7a4308", "BR-12": "dc796778-3e19-441e-8616-b7f7f7bd206f", "MECH-01": "6793dce7-0fbe-41cc-8f32-5faa5ba96752",
             "MECH-02": "a31b29af-069e-4085-a830-368e2bb64c4d", "MECH-06": "62022a6c-b2ea-492a-9f9f-79557e9b733e"}

# ── Fix round 2 (user Fix notes, 2026-09-28 ~18:00) ──────────────────────────────────────────────────────────
FIX2 = {"BR-14b": "wtong product", "BR-15a": "fix the product make it small", "BR-18a": "fix the size of product"}
SMALL = ("THE STRAP IS SMALL: the shell is about 12 cm across and 5 cm tall — no wider than his hand across the knuckles, "
         "so his fingers and thumb cover a good part of its lower edge — and the closed band is a small soft loop not much bigger "
         "than his wrist. It is a small, light thing held easily in one hand, never a large mask-sized object.")
NEG_SMALL = ", no oversized strap, no strap wider than his hand, no mask-sized shell, no giant product, no shell bigger than his palm"
B["BR-14b"] = (NBP, ["front", "C1", "P2"], photo([
    "A snapshot from a phone propped at eye level on the bench. His two hands hold one cheap copy strap and pull its band apart: "
    "his left hand holds the copy's shell up at chest height, the shell square to the lens, and his right hand pulls the thin band "
    "away from it, the band stretched out long and thin, pale where it is stretched, a loose thread hanging from its edge. "
    "THE COPY IS SHAPED LIKE THE ATTACHED PRODUCT PHOTO at a glance — the same small shell with two peaks and a notch — but cheap: "
    + P.FAKE_BASE.split(": ", 1)[1] + " The copy's shell is clearly visible and readable as a knock-off of the attached shape. " + C1_HANDS,
    SMALL.replace("The strap", "The copy").replace("THE STRAP", "THE COPY"),
    BENCH, angle("BR-14b", "his hands"), focus("the hands and what they hold"), light("WS-L", "his hands"), colour("WORKSHOP")],
    P.NEG_FAKE_HERO + ", no stryde wordmark on the copy, no chrome on the copy, no matte finish on the copy, no cord, no string, "
    "no shoelace, no thin rope, no missing shell, no face" + NEG_SMALL + ", " + NEG_HANDS))
B["BR-15a"] = (NBP, ["front", "back", "C1", "P2"], photo([
    "The strap in this photo is THE EXACT SAME OBJECT as the first attached product photo, the front, and the second, the back — "
    "only the view changes. A snapshot from a phone propped at eye level on the bench, a little further back so his chest and "
    "apron fill the frame behind. He holds the strap up towards the lens in his right hand at chest height, front face and wordmark "
    "square to the camera: " + dict(P.HELD_GRIPS)["bottom-edge pinch"].split(" (")[0] + ". Nothing rises above the shell's top edge. "
    "His face is just out of frame at the top. " + C1_HANDS,
    PROD + " " + RIGID + " " + SMALL,
    BENCH, angle("BR-15a", "the strap"), focus("the product and its wordmark"), light("WS-L", "the strap"), colour("WORKSHOP")],
    HELD_NEG + NEG_SMALL + ", " + NEG_HANDS))
B["BR-18a"] = (NBP, ["front", "back", "C1", "P2"], photo([
    "Both straps in this photo are THE EXACT SAME OBJECT as the first attached product photo, the front, and the second, the back — "
    "only the view changes. A snapshot from a phone propped at eye level on the bench, three-quarter to him, a little further back so "
    "his chest and apron fill the frame behind. He holds two identical straps up side by side towards the lens, one in each hand, "
    "each by the bottom-edge pinch: thumb in front on the shell's bottom edge below the wordmark, fingers behind on the pad, the "
    "bands hanging slack round his wrists. Both front faces and wordmarks to the camera, level with each other, a hand's width apart. "
    "Nothing rises above the shells' top edges. " + C1_HANDS,
    PROD + " Two identical units of it, the same size. " + RIGID + " " + SMALL.replace("THE STRAP IS SMALL", "EACH STRAP IS SMALL"),
    BENCH, angle("BR-18a", "the two straps"), focus("the product and its wordmark"), light("WS-L", "the straps"), colour("WORKSHOP")],
    HELD_NEG.replace("no second strap, ", "") + ", no third strap, no straps of different sizes, no face" + NEG_SMALL + ", " + NEG_HANDS))

# ── Fix round 3 (user Fix notes, 2026-09-28 ~18:05) ──────────────────────────────────────────────────────────
FIX3 = {"BR-02": "pointing the patellar tendd under the kneecap", "BR-11": "fix the size of the strap", "BR-13": "change this",
        "BR-15c": "fix the product"}
B["BR-02"] = (NBP, ["C1", "S1", "P2"], photo([
    "A close snapshot from a phone held at knee height directly in front of her knee. Her right leg is straight out from the stool and "
    "the bare knee fills the middle of the frame, from just above the kneecap to mid-shin. ONLY ONE FINGERTIP TOUCHES HER: his right "
    "index finger is extended and its tip rests exactly in the soft hollow just under the lower edge of her kneecap, on the patellar "
    "tendon, dead centre on the front of the knee, pressing a little so the skin dimples; his other three fingers are curled into his "
    "palm and his thumb tucked, the rest of his hand held away from her leg, coming in from the bottom right. The whole kneecap sits "
    "clear and bare just above his fingertip. " + C1_HANDS + " Her knee: " + SKIN_LEG,
    "Her skirt hem at the top of the frame: " + WARD["W-D1"] + ".",
    BENCH, "THE CAMERA ANGLE: a camera at knee height, square to the front of her knee, close. This exact angle.",
    focus("his fingertip under her kneecap"), light("WS-L", "the knee and his hand"), colour("FIT")],
    "no hand gripping the knee, no palm on the knee, no fingers wrapped round the knee, no more than one finger touching her, "
    "no finger on the side of the knee, no finger on the kneecap itself, no finger on the shin, no strap, no brace, no sleeve, "
    "no second hand, " + NEG_HANDS))
B["BR-11"] = (NBP, ["front", "back", "C1", "P2"], photo([
    "The strap in this photo is THE EXACT SAME OBJECT as the first attached product photo, the front, and the second, the back — only "
    "the view changes. A snapshot from a phone propped at eye level on the bench, a little further back so his chest and apron fill the "
    "frame behind. His right hand holds the strap up at chest height over the bench, front face and wordmark square to the lens: "
    + dict(P.HELD_GRIPS)["bottom-edge pinch"].split(" (")[0] + ". Nothing rises above the shell's top edge; both peaks and the notch "
    "stand clear. His face is just out of frame at the top. " + C1_HANDS,
    PROD + " " + RIGID + " The shell is a hard, thin, curved plate like the product photos, never a soft rounded pad. " + SMALL,
    BENCH, angle("BR-11", "his hand"), focus("the product and its wordmark"), light("WS-L", "his hand"), colour("WORKSHOP")],
    HELD_NEG + ", no soft pad, no cushion, no rounded blob shell" + NEG_SMALL + ", " + NEG_HANDS))
B["BR-13"] = (NBP, ["worn_bent", "front", "back", "S1", "P0"], photo([
    "The strap and how it sits on the bent knee are EXACTLY as in the first attached photo, the bent-knee worn reference. A snapshot "
    "from a phone held at knee height in the hall, beside the flight, looking through the white spindles at her from the SIDE. The "
    "frame runs from her waist to her boots, her legs in profile across the middle of the frame. She is stepping down one stair "
    "forwards, caught mid-step: her left foot planted on the stair, her right foot reaching down to the step below, the strapped right "
    "knee bent and nearest the camera, the strap on it clear and readable in side view; her hands are out of frame. Two or three white "
    "spindles run soft and out of focus down the near foreground.",
    "Her skirt and boots: " + WARD["W-D2"] + ". " + SKIN_LEG,
    PROD + " " + RIGID + " " + P.PLACE_PROFILE + " " + P.SIZE_WORN, STAIRS,
    "THE CAMERA ANGLE: a camera at knee height, seen from the side, in profile of her legs, looking past the white spindles, soft in the "
    "near foreground. This exact angle, never a view from the front or from the bottom of the stairs.",
    focus("the product and its wordmark"), light("ST-L", "her legs"), colour("STAIRS")],
    WORN_NEG + ", no front view, no full-length figure, no face, no view from the foot of the stairs, " + NEG_SUP + ", " + NEG_EFF))
B["BR-15c"] = (NBP, ["front", "back", "worn_front", "S1", "P0"], photo([
    "The strap in this photo is THE EXACT SAME OBJECT as the first attached product photo, the front — only its place changes. A "
    "snapshot from a phone held low in front of her. She sits on the bottom stair, her right leg straight out in front of her, and the "
    "closed strap sits at mid-shin, well below the knee: the rigid black shell is CENTRED ON THE FRONT OF HER SHIN facing the camera, "
    "its two peaks and notch pointing up the leg towards the kneecap, the grey stryde wordmark horizontal and readable, a chrome slide "
    "at each side of the shin, the black band running round the back of the calf. Both her hands hold the shell by its two sides, palms "
    "and fingertips flat on the matte shell, ready to slide it up; she looks down at it. " + SKIN_LEG,
    S1 + " Wearing " + WARD["W-D2"] + ".",
    PROD + " " + RIGID + " The shell is a hard, thin, curved plate exactly like the product photo, never a soft pad or a floppy band. "
    "Its size never changes: the shell spans the front of her shin from side to side, a chrome slide at each side, about as tall as her "
    "kneecap.", STAIRS,
    "THE CAMERA ANGLE: a low camera in front of her, looking along her straight leg at the front of the shin. This exact angle.",
    focus("the product and its wordmark"), light("ST-L", "her"), colour("STAIRS")],
    P.NEG_SEAT + ", no shell on the side of the shin, no wordmark sideways, no shell facing away, no soft pad, no floppy strap, "
    "no strap on the left leg, " + NEG_HANDS))

# BR-15c: the start frame shows the strap at mid-shin, so the video-only seating negatives about resting low / two actions are dropped
_m, _r, _p = B["BR-15c"]
B["BR-15c"] = (_m, _r, _p.replace("no two separate actions in one clip, no product travelling past the kneecap, ", "")
    .replace("no product coming to rest low on the shin, no product moving downward, no product coming down from above the kneecap, ", ""))
FIX3_JOBS = {"BR-02": "1111ad81-5a82-47d1-9e22-2827d5095616", "BR-11": "56a2c1e9-d175-47eb-b7f0-fdd5325768c0",
             "BR-13": "a938def7-9d7a-4f99-9493-a8797734d25a", "BR-15c": "4ec9787f-9cd4-4f05-8f07-3a043115c5d2"}

# ── Fix round 4 (user Fix note, 2026-09-28 ~18:40) ──────────────────────────────────────────────────────────
# BR-15a still read big after FIX2: the frame was tight on the strap, so the model scaled it up to fill it, and the closed band
# hung as a large loop. Fixed at the source: a wider frame (waist up, the strap a small thing in it), the band folded away in his
# palm, the shell compared to his own hand, and the worn-on-the-knee photo attached as the size anchor.
FIX4 = {"BR-15a": "make it small the product / fix the size"}
B["BR-15a"] = (NBP, ["front", "back", "worn_front", "C1", "P2"], photo([
    "The strap in this photo is THE EXACT SAME OBJECT as the first attached product photo, the front, and the second, the back — "
    "only the view changes. The third attached photo shows it worn on a knee: THAT IS ITS TRUE SIZE, about as wide as a kneecap. "
    "A snapshot from a phone propped at eye level on the bench, well back from him: the frame runs from his collar to his belt, his "
    "chest and apron filling it, his face just out of frame at the top. He holds the strap up in front of his chest in his right hand, "
    "front face and wordmark square to the camera: " + dict(P.HELD_GRIPS)["bottom-edge pinch"].split(" (")[0] + ". The black band is "
    "folded up and tucked into his palm behind the shell, out of sight — no loop hangs down. Nothing rises above the shell's top edge. "
    + C1_HANDS,
    PROD + " " + RIGID + " " + SMALL + " In the frame the shell takes up only about a fifth of the frame's width, clearly narrower "
    "than his hand across the knuckles and much smaller than his chest; his big workman's hand dwarfs it.",
    BENCH, angle("BR-15a", "the strap"), focus("the product and its wordmark"), light("WS-L", "the strap"), colour("WORKSHOP")],
    HELD_NEG + NEG_SMALL + ", no hanging loop, no band dangling, no close-up of the strap, no strap filling the frame, "
    "no strap as wide as his chest, " + NEG_HANDS))

_m, _r, _p = B["BR-15a"]
B["BR-15a"] = (_m, _r, _p.replace(" spanning the whole front of the knee", "").replace(", band slack round the wrist", "")
    .replace(" — and the closed band is a small soft loop not much bigger than his wrist", ""))

# ── Fix round 5 (user Fix notes, 2026-09-28 ~18:50) ──────────────────────────────────────────────────────────
# BR-15c "wrong product": the frame was her whole seated figure, so the strap was a few dozen pixels and came out as a thin band.
#   Fixed at the source: a close frame on her right shin and knee and her hands, so the shell renders large enough to be the product.
# BR-18a "remove the bracelet": the slack bands round his wrists read as bracelets. An edit of the confirmed-look v2 render
#   (job ref first) that only tucks the bands into his palms; everything else unchanged.
FIX5 = {"BR-15c": "wrong product", "BR-18a": "remove the bracelet"}
FIX5_EDIT_REF = {"BR-18a": "98cbf149-c29e-410c-a7cb-05cefbbfd7f5"}
B["BR-15c"] = (NBP, ["front", "worn_front", "back", "S1", "P0"], photo([
    "The strap in this photo is THE EXACT SAME OBJECT as the first attached product photo, the front; the second attached photo shows "
    "how it looks on a leg. A close snapshot from a phone held low in front of her as she sits on the bottom stair: the frame runs from "
    "just above her right knee down to her ankle, her right leg straight out towards the camera and filling the frame, her two hands "
    "on the strap. The closed strap sits at mid-shin, a hand's width below the kneecap: the rigid matte-black shell is CENTRED ON THE "
    "FRONT OF HER SHIN facing the camera, its two matching peaks and the notch between them pointing up the leg towards the kneecap, "
    "the grey stryde wordmark horizontal and readable under the notch, a brushed chrome slide at each end of the shell, the black "
    "band running round the back of the calf. Her thumbs and fingertips hold the two ends of the shell, flat on the matte shell, ready "
    "to slide it up. " + SKIN_LEG,
    "Her skirt hem at the top edge and her tan boots at the bottom: " + WARD["W-D2"] + ".",
    PROD + " " + RIGID + " The shell is as wide as the front of her shin and about as tall as her kneecap, large and clear in this "
    "close frame.", STAIRS,
    "THE CAMERA ANGLE: a low camera close in front of her, looking along her straight right leg at the front of the shin. This exact angle.",
    focus("the product and its wordmark"), light("ST-L", "her shin"), colour("STAIRS")],
    P.NEG_SEAT + ", no thin band without a shell, no plain black strap, no shell on the side of the shin, no wordmark sideways, "
    "no shell facing away, no soft pad, no floppy strap, no strap on the left leg, no face, no whole figure, " + NEG_HANDS))
B["BR-18a"] = (NBP, ["front", "C1"], photo([
    "EDIT OF THE FIRST ATTACHED IMAGE. Keep everything in it exactly as it is — the man, his face, his pose, his hands, the two straps, "
    "their size and position, the bench, the vice, the workshop and the light — and change only this: there is NOTHING ON HIS WRISTS. "
    "The two straps' black bands are folded and tucked into his palms behind the shells, out of sight, so no band loops round either "
    "wrist and no bracelet, watch or band of any kind is on his wrists or forearms; his bare wrists and the rolled cuffs of his check "
    "shirt show."],
    "no bracelet, no wristband, no watch, no band round the wrist, no loop hanging from his hands, no other change to the image, "
    "no third strap, " + NEG_HANDS))

_m, _r, _p = B["BR-15c"]
B["BR-15c"] = (_m, _r, _p.replace("no two separate actions in one clip, no product travelling past the kneecap, ", "")
    .replace("no product coming to rest low on the shin, no product moving downward, no product coming down from above the kneecap, ", "")
    .replace(" spanning the whole front of the knee", ""))

# ── Pinned end frame for BR-11 (§27G: the strap turns over, so the video runs to an approved end frame) ─────────────
END = {"BR-11-END": (NBP, ["56a2c1e9-d175-47eb-b7f0-fdd5325768c0", "back", "front"], photo([
    "EDIT OF THE FIRST ATTACHED IMAGE: the same photo a moment later. Keep the man, his hands, the bench, the workshop, the camera "
    "position and the light exactly as they are. The only change: his hand has turned the strap over, so it now shows its BACK to "
    "the lens exactly as in the second attached product photo, the back — the soft pad side of the shell facing the camera, the "
    "wordmark now facing away from the camera, the shell the same small size, held the same way at chest height."],
    "no wordmark visible, no second strap, no size change, no other change to the image, " + NEG_HANDS))}

# ── Fix round 6 (user Fix notes, 2026-09-28 ~19:00) ──────────────────────────────────────────────────────────
# BR-11-END "wrong product": v1 kept the front's geometry and only erased the wordmark. Fixed at the source: the back product photo
#   is the FIRST reference and P.PAD_BACK_SHOT describes the pad side; the confirmed BR-11 frame is only the scene reference.
# BR-18a "fix the holding": v3's grips were awkward pinches. Fixed with the grip from the confirmed BR-15a v3 (job ref) named for
#   both hands: thumb in front on the shell's bottom edge, fingers behind, band tucked in the palm.
FIX6 = {"BR-11-END": "wrong product", "BR-18a": "fix the holding"}
END["BR-11-END"] = (NBP, ["back", "56a2c1e9-d175-47eb-b7f0-fdd5325768c0", "front"], photo([
    "The strap in this photo is THE EXACT SAME OBJECT as the FIRST attached product photo, the back of the strap, seen from that same "
    "side. The SECOND attached image is the scene: keep the man, his apron, the bench, the vice, the workshop, the camera position and "
    "the light exactly as in it. The only change from the second image: his hands have turned the strap round so its BACK faces the "
    "lens, held at chest height the same way. " + P.PAD_BACK_SHOT.replace(", fills the frame", "") + " The two peaks and the notch between them are along the TOP edge, "
    "exactly as in the first attached photo; the shell the same small size as in the second image."],
    "no wordmark, no front face, no peaks along the bottom edge, no upside-down shell, no second strap, no size change, "
    "no other change to the scene, " + NEG_HANDS))
B["BR-18a"] = (NBP, ["73cd4b03-518b-4f38-83b4-e65334a19fee", "90168a20-dade-40fe-96db-2ffae7f4f02b", "front"], photo([
    "EDIT OF THE FIRST ATTACHED IMAGE. Keep everything in it exactly as it is — the man, his face, his pose, the two straps, their size "
    "and position side by side, nothing on his wrists, the bench, the vice, the workshop and the light — and change only HOW HE HOLDS "
    "THEM: each hand holds its strap exactly the way he holds the strap in the SECOND attached image — thumb in front on the shell's "
    "bottom edge below the wordmark, the fingers behind the shell, the band folded and tucked into the palm out of sight. A relaxed, "
    "natural grip, the hands low on the shells so both wordmarks, both peaks and both notches stand clear."],
    "no pinching fingertips, no fingers across the wordmark, no fingers over the peaks, no bracelet, no band round the wrist, "
    "no other change to the image, no third strap, " + NEG_HANDS))

if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in B.items():
        (HERE / f"{beat}.t2i.txt").write_text(prompt + "\n")
        r = ROWS[beat]
        out[beat] = {"model": model, "refs": refs, "prompt": prompt, "act": r["act"], "phrase": r["phrase"],
                     "call_s": LEN[beat]["call_s"], "chars": len(prompt)}
    for beat, (model, refs, prompt) in END.items():
        (HERE / f"{beat}.t2i.txt").write_text(prompt + "\n")
    (HERE / "broll_v1.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    for b, v in out.items():
        print(b.ljust(8), v["model"].ljust(16), str(v["chars"]).rjust(5), ",".join(v["refs"]))
    assert set(out) == {b for b, r in ROWS.items() if r["type"] in ("BR", "MECH") and not r["act"].startswith("Hook")}, "beat set != act map"
    assert not any("[" in v["prompt"] for v in out.values()), [b for b, v in out.items() if "[" in v["prompt"]]
