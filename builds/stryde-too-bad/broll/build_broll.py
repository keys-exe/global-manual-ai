#!/usr/bin/env python3
"""Step 7 body B-roll start images for stryde-too-bad — Act 1 (act map work/actmap.json; STEP4_5.md light plans, wardrobe ledger).
Mode 1 §22T candid seed: CAM-LOCK → prose → person → scene (plate) → product → ANGLE-LINE → FOCUS-LINE → LIGHT-SHOT → COLOUR-KEY →
CAP-FILE → negatives. Product blocks from the STRYDE product sheet module; anatomy from Appendix A (ANAT-BASE + ANAT-LIGHT + ANAT-FIELD +
ANAT-A/B, the sheet's slots). Pattern from stryde-thirty-years/broll/build_broll.py. Route: realistic → Higgsfield nano_banana_pro
(nano_banana_2 where the act map says NB2 — no readable wordmark); anatomy → nano_banana_2; the offer card → gpt_image_2_5 sunburst.
Writes broll/<BEAT>.t2i.txt and broll/broll.json ({beat: {model, refs, prompt, act, line, chars}}). Usage: build_broll.py [Act 1|Act 2]"""
import json, re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent; BUILD = HERE.parent; ROOT = BUILD.parents[1]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
sys.path.insert(0, str(ROOT / "products/stryde")); import stryde_product_sheet as P  # noqa: E402
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S); return m.group(1).strip()
ROWS = {r["beat"]: r for r in json.loads((BUILD / "work/actmap.json").read_text())["rows"]}
NBP, NB2, GPT = "nano_banana_pro", "nano_banana_2", "gpt_image_2_5"

# ── people (cast/build_sheets.py identity strings, shortened to face + build) ────────────────────────────────────────
DENISE = ("THE SAME WOMAN exactly as in the attached character sheet — a square face with a broad strong jaw and full rounded cheeks, "
          "wide-set warm brown eyes under full straight dark-grey brows, a wide nose with a low bridge, a generous full mouth, a single "
          "short deep dimple in her left cheek; chin-length grey-and-black twist-out curls; an African-American woman of sixty-four, "
          "sturdy and broad-shouldered with strong legs — unchanged in face, age and build.")
ALAN = ("THE SAME MAN exactly as in the attached character sheet — a long thin face with sunken cheeks, small close-set pale blue eyes "
        "under wiry white brows, a large nose with a visible crook to the left, large ears, bald on top with a short white fringe round "
        "the back; a white British man of seventy-two, short and wiry, a slight bow in the legs — unchanged in face, age and build.")
CLIVE = ("THE SAME MAN exactly as in the attached character sheet — a long lean face with high sharp cheekbones, hooded dark brown eyes, "
         "a long straight nose, a neat white moustache, short tightly coiled grey-white hair receding high at both temples, a small "
         "raised scar on his left earlobe; a Black British man of sixty-seven, tall and lean with long thin legs — unchanged in face, age and build.")
FIONA = ("THE SAME WOMAN exactly as in the attached character sheet — a wide oval face with a strong jaw, light hazel eyes, freckles "
         "across the nose and cheeks, a small pale scar on the point of her chin, shoulder-length curly copper-red hair going grey at "
         "the temples; a white British woman of sixty-six, tall, strong-shouldered and long-limbed — unchanged in face, age and build.")
SURGEON = ("An orthopaedic consultant of about fifty-five, a white British man: a broad, lived-in face with a short greying beard, "
           "reading glasses pushed up into thick salt-and-pepper hair, a pale blue shirt with the sleeves rolled to the forearm, no "
           "white coat, no stethoscope. " + S("APPROACH-PRO"))
WARD = {
    "D-D1": "a mustard-yellow short-sleeved linen shirt, olive cotton shorts ending above the knee so both knees are bare, barefoot, small gold hoop earrings",
    "D-D2": "a white T-shirt under an open lavender lightweight zip jacket, navy cotton shorts ending above the knee so both knees are bare, white trainers",
    "A-D1": "a sage-green polo shirt under a navy V-neck cardigan, grey trousers, brown slippers",
    "A-D2": "a pale blue denim shirt with the sleeves rolled, stone cotton trousers, brown garden boots",
    "C-D1": "a grey T-shirt under a dark green shop apron, charcoal work shorts ending above the knee so both knees are bare, black trainers, a pencil behind his ear",
    "F-D1": "a white linen shirt with the sleeves rolled, cropped blue linen trousers rolled up above the knee so both knees are bare, tan leather sandals",
    "F-D2": "a grey T-shirt under an open red waterproof jacket, black walking shorts ending above the knee so both knees are bare, brown leather walking boots, a small rucksack",
}
SKIN = {"f64": P.LEG_SKIN.replace("about sixty", "about sixty-five"), "m70": P.LEG_SKIN.replace("about sixty", "about seventy"),
        "dark": P.LEG_SKIN.replace("an adult leg of about sixty", "a Black adult's leg of about sixty-five, deep brown skin a little darker over the knee")}

# ── places (the plates and the traversed locations) ────────────────────────────────────────────────────────────────
LOUNGE = ("THE SAME LOUNGE exactly as in the attached location plate — the teal velvet sofa with mustard cushions, the low oak coffee "
          "table with its stack of books and bowl of clementines, the red-and-cream kilim rug, the bay window on the south wall, warm-white walls.")
CONSULT = ("THE SAME CONSULTING ROOM exactly as in the attached location plate — the pale grey walls, the light wood desk, the window on "
           "the right-hand wall, the examination couch behind.")
PARK = ("A London park on a bright morning: a grey tarmac path curving across open mown grass, plane trees, a green-painted Victorian "
        "bandstand with a white fretwork canopy beside the path a little behind her, a few far-off figures, soft and small.")
KITCHEN = ("THE SAME KITCHEN exactly as in the attached location plate — the cream shaker units with brushed steel bar handles, the light "
           "oak-effect laminate worktop, the terracotta-effect floor tiles, the pale butter-yellow walls, the window over the sink.")
GARDEN = ("THE SAME BACK GARDEN exactly as in the attached location plate — the lawn, the raised vegetable bed, the wooden bench, the "
          "back of the brick house with its kitchen window and white back door.")
SHOP = ("THE SAME HARDWARE SHOP exactly as in the attached location plate — the long aisle of metal shelving stacked with paint tins, "
        "boxes of screws and tools, the vinyl floor, the shop windows at the far end.")
COAST = ("A clifftop coastal path in Fife on a bright clear day: a narrow worn earth path through short grass and gorse running away "
         "along the cliff top, the sea blue and wide on the LEFT of the frame, a pale sky, a distant headland.")
HALL = ("THE SAME HALL AND STAIRS exactly as in the attached house plate — sage-green plaster walls, the white handrail and square "
        "spindles, the oatmeal wool stair carpet, the straight flight rising along the LEFT-hand wall to a small landing with a window.")

LIGHT = {  # source, screen side, quality — STEP4_5.md light plans
    "LOUNGE": ("the bay window on the lounge's south wall", "right", "bright morning daylight, sun on the rug"),
    "CONSULT": ("the window on the right-hand wall", "right", "soft overcast midday daylight"),
    "PARK": ("the open sky, broken cloud, the sun behind the camera on the left", "left", "bright morning daylight"),
    "GARDEN": ("the late-morning sun from the south over the left-hand fence", "left", "bright raking late-morning sun, the sky cleared"),
    "SHOP": ("the shop windows at the far end and the fluorescent strips above", "right", "even midday working light"),
    "KITCHEN": ("the window over the sink on the kitchen's east wall", "left", "flat grey-white morning daylight"),
    "COAST": ("the high midday sun over the sea on the left", "left", "bright, clean midday light"),
    "HALL": ("the landing window and the front-door glass, both facing south", "right", "bright morning sun falling on the stair carpet"),
}
COLOUR = {  # light colour, kelvin, set colours, wardrobe colours, accent, saturation
    "LOUNGE": ("bright morning daylight", 5600, "warm oak, the red-and-cream kilim, teal velvet, warm-white walls", "mustard yellow and olive", "the teal sofa", "true to life, a touch warm"),
    "CONSULT": ("soft overcast daylight", 6500, "pale grey walls, light wood, white", "pale blue", "the black strap", "true to life, slightly cool"),
    "PARK": ("bright morning daylight", 5600, "green grass, grey tarmac, the green bandstand", "white, lavender and navy", "the lavender jacket", "true to life"),
    "GARDEN": ("bright late-morning sun", 5600, "green lawn, red brick, dark soil in the bed", "pale denim blue and stone", "a green watering can", "true to life, bright"),
    "KITCHEN": ("flat grey-white morning daylight", 5600, "cream units, light oak laminate, terracotta floor, butter-yellow walls", "navy, sage green and grey", "the navy cardigan", "muted, slightly cool"),
    "SHOP": ("even daylight and fluorescent working light", 5000, "grey metal shelving, coloured paint tins, grey vinyl", "grey and dark green with charcoal", "the paint tins", "true to life"),
    "COAST": ("bright clean midday light", 5600, "blue sea, green gorse, a pale earth path", "red, grey and black", "the red waterproof", "clear and fresh"),
    "HALL": ("bright morning sun", 5600, "sage-green walls, white woodwork, oatmeal carpet", "white and blue linen", "the blue trousers", "true to life"),
}
HEIGHT = {"overhead": "an overhead camera looking straight down", "high": "a high camera looking down", "eye": "an eye-level camera",
          "low": "a low camera close to the floor looking up", "ground": "a camera at ground level"}
SIDE = {"front": "the front", "three-quarter": "three-quarter", "profile": "the side, in profile", "three-quarter-back": "three-quarter behind",
        "behind": "directly behind", "ots": "over the shoulder"}
def angle(beat, subj, fg=""):
    r = ROWS[beat]
    return (S("ANGLE-LINE").replace("[HEIGHT CLAUSE from §30I]", HEIGHT[r["height"]]).replace("[SIDE]", SIDE[r["side"]]).replace("[SUBJECT]", subj)
            .replace("[, looking past FOREGROUND, soft in the near foreground | , seen in REFLECTION]", fg))
def focus(plane, deep=False):
    return (S("FOCUS-LINE").replace("[PLANE — the nearest eye of NAME / the hands and what they hold / the product and its wordmark / the foreground / everything]", plane)
            .replace("[DEPTH — the room behind falls to a soft, recognisable shape | everything from near to far stays sharp]",
                     "everything from near to far stays sharp" if deep else "the room behind falls to a soft, recognisable shape"))
def light(key, subj, face=True):
    src, side, q = LIGHT[key]
    t = (S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", src)
         .replace("[SUBJECT]", subj).replace("[SCREEN SIDE]", side).replace("[TIME-OF-DAY QUALITY and the act's light state]", q).replace("[SIDE]", "the " + side))
    return t if face else t.replace("so the face has a lit side toward the %s and a softer shadow side, with a small catchlight in the eyes" % side,
                                    "so it has a lit side toward the %s and a softer shadow side" % side)
def colour(key, who):
    lc, k, sc, wc, ac, sat = COLOUR[key]
    return (S("COLOUR-KEY").replace(", exactly as in the attached master frame", "").replace("[LIGHT COLOUR]", lc).replace("[KELVIN]", str(k))
            .replace("[SET COLOURS]", sc).replace("[WHO]", who).replace("[WARDROBE COLOURS]", wc).replace("[ACCENT]", "the accent is " + ac)
            .replace("[SATURATION AND CONTRAST IN CAMERA]", sat))

# ── product ─────────────────────────────────────────────────────────────────────────────────────────────────────────
SAME = ("The strap in this photo is THE EXACT SAME OBJECT as the FIRST attached product photo, the front, and the second, the back — "
        "only the view changes.")
PROD = P.REF_PROD.replace("the attached reference image", "the attached product photos, front and back").rstrip(" —") + "."
RIGID = ("It is a RIGID MOULDED shell with a hard edge, never fabric, never neoprene, never a padded pad: a hard, thin, curved plate "
         "shaped like a wide shallow W across its top, never a rectangle, never a box.")
def worn(who):
    return ("The strap sits on %s RIGHT knee on the patellar tendon, directly below the kneecap: the notch cups the kneecap's lower border "
            "with no gap, the two peaks no higher than the base of the kneecap's sides, the kneecap's face bare above, a chrome slide at "
            "each outer side of the leg, the black band round the back of the knee, snug on bare skin, the wordmark horizontal. " % who + P.SIZE_WORN)
WORN_NEG = ("no strap on the left knee, no second strap, no shell over the kneecap, no shell low on the shin, no shell on the thigh, "
            "no uneven peaks, no flat top edge, no rectangular block, no shell narrower than the knee, no slide on the front of the knee, "
            "no shell rotated to the side, no strap over clothing, no loose band tail, no fabric pad, no neoprene pad")
BLOCK_NEG = "no rectangular block, no flat straight top edge, no U-shaped slot notch, no square shell, no box shape, no shell without peaks"
PINCH = dict(P.HELD_GRIPS)["bottom-edge pinch"].split(" (")[0]

# ── tails ───────────────────────────────────────────────────────────────────────────────────────────────────────────
NEG_BASE = ("no readable text, no logos other than the stryde wordmark, no AI face, no plastic skin, no extra fingers, no fused fingers, "
            "no polished render, no advertising image, no studio lighting, no vignette, no glowing skin, no light from nowhere, "
            "no shadows falling in two directions, no lens flare")
NEG_HANDS = "no wrong finger count, no malformed hands, no hands merging into objects"
NEG_SUP = "no hand on the rail, no hand on the wall, no hand on furniture, no hand pressing on the knee, no reaching for support"
NEG_EFF = "no limping, no wincing, no laboured movement, no eyes fixed on the feet, no hesitation"
def photo(parts, avoid):
    return "\n\n".join([S("CAM-LOCK")] + [p for p in parts if p] + [S("CAP-FILE"), "AVOID: " + avoid + ", " + NEG_BASE])

ANAT_SLOTS = {"[REGION]": "knee", "[STACK]": "quadriceps, hamstrings and calf", "[BONES]": "femur, patella and tibia",
              "[TARGET]": "the patellar tendon", "[TARGET JOINT]": "the knee joint", "[SITE]": "the patellar tendon immediately below the kneecap"}
ANAT_NEG = ("no arrows, no force arrows, no motion lines, no diagram markings, no text overlays, no labels, no numbers, no annotations, "
            "no UI, no watermark, no individual muscle fibres, no surface veins, no emission on the bone shafts, no glow on the tibial "
            "tuberosity, no glow spreading down the shin, no second limb, no clothing, no hands, no people, no flat illustration, "
            "no cartoon look, no vignette, no darkened frame corners, no limb falling off into darkness")
def anat(state, extra_neg="", look="A", view=None):
    base = S("ANAT-BASE")
    if view:
        base = base.replace("viewed from a low three-quarter angle, foreshortened, [TARGET JOINT] sitting slightly off-centre and dominating the frame", view)
    t = "\n\n".join([base, S("ANAT-LIGHT"), S("ANAT-FIELD"), S("ANAT-A") if look == "A" else S("ANAT-B"), state,
                     "AVOID: " + ANAT_NEG + (", " + extra_neg if extra_neg else "") + ", " + S("NEG-EXTERNAL")])
    for k, v in ANAT_SLOTS.items():
        t = t.replace(k, v)
    return t
FRONT_VIEW = "viewed from the front, the knee joint in the middle of the frame, the thigh above and the shin below"
TQ_VIEW = "viewed from the front three-quarter, the knee joint in the middle of the frame, the thigh above and the shin below"
PROF_VIEW = "viewed from the side, in profile, the whole knee joint in the middle of the frame with the thigh above and the shin below"
LOW_VIEW = None  # ANAT-BASE's own low three-quarter view
HIGH_VIEW = "viewed from a high three-quarter angle looking down on the knee joint, the thigh above and the shin below"

B = {}   # beat -> (model, refs, prompt); refs are keys of hooks/refs.json + REF_EXTRA
# ── Act 1 ───────────────────────────────────────────────────────────────────────────────────────────────────────────
B["B1-01a"] = (NBP, ["front", "back", "P4-CONSULT"], photo([
    SAME + " A snapshot from a phone held at eye level across the desk, three-quarter to him. The consultant sits at his desk and holds "
    "the strap against the front of the knee of a life-size plastic anatomical knee model standing on the desk — a pale ivory model knee "
    "joint on a small stand, the femur above, the tibia below, the kneecap in place. His right hand has the shell by its two ends, "
    "fingertips on the pad behind it, bringing it in to rest on the model's tendon just below the model's kneecap, caught just before it "
    "touches; the black band hangs loose below. His face is turned to the model, soft, the strap and his hands sharp.",
    SURGEON, CONSULT,
    PROD + " " + RIGID + " " + P.WORDMARK_LOCK + " " + P.SIZE_HELD,
    angle("B1-01a", "his hands and the knee model"), focus("the product and its wordmark"), light("CONSULT", "him"), colour("CONSULT", "he")],
    P.NEG_HELD_P + ", " + P.NEG_WORDMARK + ", " + BLOCK_NEG + ", no white coat, no stethoscope, no patient, no second strap, no skeleton, " + NEG_HANDS))
B["MECH-S1"] = (NB2, ["front", "back"], anat(
    "The strap is worn on the model exactly as in the attached product photos, its rigid matte-black shell seated on [SITE], the notch "
    "under the kneecap, the band round the back of the knee. " + S("ANAT-PROD") + " The shell and band glow with a cool electric-blue "
    "light along their edges, and the whole knee beneath reads calm and cool, washed in a faint clear blue; no red anywhere.",
    extra_neg="no strap on the thigh, no strap over the kneecap, no red glow, no hot spot, no sleeve, no brace", view=FRONT_VIEW))
B["MECH-S2"] = (NB2, [], anat(
    "A big generic wraparound knee brace, plain grey, no brand, with two steel hinged side bars and three wide straps, wraps the whole knee "
    "from mid-thigh to mid-shin, drawn as a faint translucent shell so the anatomy shows through it. Under it the knee joint glows hot "
    "red-orange, the heat pooled in the joint and at [SITE]; the brace does nothing to it.",
    extra_neg="no strap, no rigid black shell, no wordmark, no blue glow", view=TQ_VIEW))
# v2 Fix "FIX THIS IMAGE": v1 broke the legs (a third leg raised with the foot at the top of frame, the knee unreadable) and the finger
# pressed the shin, not the spot under the kneecap. Fixed at the prompt: both legs placed and counted, the left out of frame, the right
# heel on the rug, the fingertip on the tendon a thumb's width under the kneecap; extra-limb negatives.
# v3 Fix "CHANGE THIS IMAGE": v2 still put the fingertip halfway down the shin and brought her face in. Fixed: nano_banana_pro, an
# extreme close-up that holds only the one knee (kneecap upper third, fingertip dead centre just under it), no face, no feet.
B["B1-02"] = (NBP, ["R1-DENISE", "P2-D-LOUNGE"], photo([
    "AN EXTREME CLOSE-UP of one knee and nothing else: the frame holds only her bare right knee, from the lower thigh at the top edge to "
    "the upper shin at the bottom edge. The rounded kneecap sits in the upper third of the frame; directly beneath its lower edge, dead "
    "centre, the tip of her right forefinger presses into the soft hollow of the patellar tendon, the skin dimpling a little round it. "
    "No face, no feet, no second leg in the frame; the teal sofa and the kilim rug show only as soft colour at the edges. "
    "A snapshot from a phone held high, her own view down at her right knee. She sits on the edge of the teal sofa. Her RIGHT leg is "
    "straight out in front of her, the heel resting on the rug, the knee and shin running up the frame from the bottom, the whole right "
    "kneecap clearly visible in the middle of the frame; her left leg is bent with its foot flat on the rug, mostly out of frame at the "
    "left edge. Exactly two legs, one right knee in view. Her right forefinger presses into the soft spot on the patellar tendon, about a "
    "thumb's width directly below the lower edge of the kneecap — not on the shin, not on the kneecap — the fingertip whole and resting "
    "on the skin, the skin dimpling a little under it; her left hand rests on her left thigh. The frame is tight on the right knee and "
    "her hand; her face is out of frame. " + SKIN["dark"],
    "She is " + DENISE + " Wearing " + WARD["D-D1"] + ".", LOUNGE,
    angle("B1-02", "her right knee"), focus("the hands and what they hold"), light("LOUNGE", "her knee", face=False), colour("LOUNGE", "she")],
    "no strap, no brace, no sleeve on the knee, no second hand on the knee, no fingernail digging in, no face, no head, no hair, no earring, "
    "no feet, no whole leg, no third leg, no extra limb, no leg raised in the air, no foot above the knee, no crossed legs, no finger on the "
    "shin, no finger low on the leg, no finger on the kneecap, " + NEG_HANDS))
B["MECH-02"] = (NB2, [], anat(
    "Heel strike: the foot has just landed and the body's weight is coming down the thigh. " + S("ANAT-LOAD") + " " + S("ANAT-HOT") + " "
    + P.ANAT_A_POINT_TIGHT, extra_neg="no glow in the joint space, no glow on the cartilage, no strap, no brace", view=LOW_VIEW))
# v2 Fix "CREATE NEW ANATOMY": v1 drew the whole side of the leg up to the hip from a high view, off the confirmed anatomy look.
# New render against the confirmed MECH-S1 as the style and framing reference: the knee from the front filling the frame, muscle over
# bone, the brace translucent, the glow a tight point on the tendon below the kneecap.
B["MECH-03"] = (NB2, ["MECH-S1_v1"], "THE SAME RENDERING STYLE, FRAMING AND SCALE exactly as the attached anatomy image — the same "
    "translucent skin outline, red muscle over ivory bone, the same dark background — with the strap replaced by the brace below.\n\n" + anat(
    "A big generic wraparound knee brace, plain grey, no brand, with two steel hinged side bars and three wide straps, wraps the whole knee "
    "from mid-thigh to mid-shin, drawn as a faint translucent shell squeezing evenly all round; beneath it the single tight red-hot glow "
    "on [SITE] stays exactly as bright as before, untouched. " + P.ANAT_A_POINT_TIGHT,
    extra_neg="no strap, no rigid black shell, no wordmark, no hip, no buttock, no whole leg, no side view", view=FRONT_VIEW))
# v2 Fix "WRONG PRODUCT": v1 drew a neoprene band with a sewn chevron patch and a printed wordmark, not the moulded shell. Fixed as
# HK1-01 v2: the product photo stated as THE EXACT SAME OBJECT, the W outline spelled out, the front worn reference attached, fabric,
# neoprene and chevron-patch negatives.
B["B1-04b"] = (NBP, ["front", "back", "worn_front", "R1-DENISE", "P2-D-LOUNGE"], photo([
    SAME + " The third attached photo shows how it looks closed round a leg. A snapshot from a phone held at knee height beside the sofa, in profile to her right leg. She sits on the sofa edge, her right "
    "leg out straight, foot on the rug. The strap is already closed round her shin, sitting low at mid-shin, and both her hands have it: "
    "palms and fingertips flat on the two sides of the shell, just beginning to slide it UP her shin towards the knee, caught mid-slide. "
    "The kneecap stands bare above it. Only her hands, forearms and legs are in frame. " + SKIN["dark"],
    "Her hands and legs: " + DENISE.split(" — ")[0] + " — dark brown skin. Wearing " + WARD["D-D1"] + ".", LOUNGE,
    PROD + " " + RIGID + " The shell is a hard, thin, curved plate shaped like a wide shallow W across its top — two pointed peaks with "
    "the concave notch between them — exactly the outline of the product photos; the knit band is separate and only runs round the back "
    "of the leg from the chrome slides. " + P.WORDMARK_LOCK + " " + P.SIZE_WORN.split(";")[0] + ".",
    angle("B1-04b", "her right leg"), focus("the product and its wordmark"), light("LOUNGE", "her leg", face=False), colour("LOUNGE", "she")],
    "no strap over the kneecap, no strap on the left leg, no second strap, no band open, no velcro, no buckle, no hand gripping the band, "
    "no neoprene band, no fabric strap with a patch, no sewn chevron patch, no printed wordmark on fabric, no straight-edged band, no "
    "sports tape, " + BLOCK_NEG + ", " + P.NEG_WORDMARK + ", no face, " + NEG_HANDS))
B["MECH-04"] = (NB2, ["front", "back"], anat(
    "The strap is worn on the model exactly as in the attached product photos, its rigid matte-black shell on [SITE]. " + S("ANAT-PROD")
    + " The load arrives down the thigh and the shell takes it: the shell's edges glow a cool electric blue and the spot on [SITE] beneath "
    "it has cooled from red to a calm soft blue, the heat gone out of it; the rest of the knee stays calm.",
    extra_neg=S("NEG-PROT") + ", no strap on the thigh, no strap over the kneecap, no red hot spot", view=PROF_VIEW))
B["B1-05b"] = (NBP, ["front", "back", "R1-DENISE", "P2-D-LOUNGE", "worn_bent"], photo([
    SAME + " A snapshot from a phone held low near the rug, looking up at her three-quarter. She is standing up from the teal sofa in one "
    "easy move, caught mid-rise: her weight already forward over her feet, seat just lifting off the cushion, both knees still bent, her "
    "hands lifting off her knees and free, a small surprised breath out, eyes ahead, the start of a smile. The whole of her is in frame.",
    DENISE + " Wearing " + WARD["D-D1"] + ".", LOUNGE,
    PROD + " " + RIGID + " " + P.PLACE_BENT + " Worn exactly as in the attached bent-knee reference, on her RIGHT knee only.",
    angle("B1-05b", "her"), focus("the nearest eye of Denise"), light("LOUNGE", "her"), colour("LOUNGE", "she")],
    WORN_NEG + ", no hands on the sofa arm, no pushing up, no wincing, " + NEG_EFF))
B["B1-06"] = (NBP, ["front", "back", "R1-DENISE", "P2-D-LOUNGE"], photo([
    # v2 Fix "MAKE IT SMALL": v1 held the strap a hand's length from the lens so it filled half the frame. Fixed at the prompt: held
    # at arm's length, small in the frame (a fifth of its width), the real size in cm, the room large around it.
    SAME + " A snapshot from a phone at eye level, a couple of metres back. She holds the strap up at arm's length at chest height in front "
    "of the bay window, well away from the camera, so the strap is SMALL in the frame — only about a fifth of the frame's width, the "
    "room large around it — front face and wordmark to the lens: " + PINCH + ". Nothing rises above the shell's top edge; both peaks and the notch stand clear against the "
    "bright window behind, which falls soft. Only her hand and forearm come in from the right. Her hand is a sixty-four-year-old Black "
    "woman's hand: dark brown skin, deeper creases over the knuckles, short unpainted nails, the mustard-yellow sleeve at the elbow.",
    LOUNGE.replace("THE SAME LOUNGE", "THE SAME LOUNGE, the bay window behind her hand,"),
    PROD + " " + RIGID + " " + P.WORDMARK_LOCK + " " + P.SIZE_HELD + " " + P.SIZE_OBJECT.replace("Its size never changes: ", "It is "),
    angle("B1-06", "her hand and the strap"), focus("the product and its wordmark"), light("LOUNGE", "the strap", face=False), colour("LOUNGE", "she")],
    P.NEG_HELD_P + ", " + P.NEG_WORDMARK + ", " + BLOCK_NEG + ", no face, no silhouette, no backlit black shape, no strap close to the lens, no strap filling the frame, no oversized strap, no giant product, " + NEG_HANDS))
# v2 Fix "ADD A MUSCLE": v1 was the ANAT-B bone-only ghost limb. Now look A (muscle over bone) against the confirmed MECH-04 as the
# style reference: the quadriceps, hamstrings and calf muscles drawn round the joint, parted just enough to show the worn surfaces.
B["MECH-05"] = (NB2, ["MECH-04_v1"], "THE SAME RENDERING STYLE, FRAMING AND SCALE exactly as the attached anatomy image — the same "
    "translucent skin outline, red muscle over ivory bone, the same dark background — without the strap.\n\n" + anat(
    "The muscles are all there: the quadriceps above the knee, the hamstrings behind it and the calf below, red and fibrous, wrapping "
    "the joint, parted just enough at the front of the joint to show the bone surfaces inside. CONDITIONS: the cartilage lining the joint surfaces is worn thin and patchy, the femur and tibia sitting close, bone nearly on bone, "
    "and the edge of the meniscus between them is torn and frayed; a dull red glow sits in the narrowed joint space and along the torn "
    "meniscus edge, the rest calm.", look="A", extra_neg="no strap, no brace, no glow on the tendon, no bone-only leg, no missing muscles", view=TQ_VIEW))
B["B1-08"] = (NBP, ["front", "back", "R1-DENISE", "worn_front"], photo([
    SAME + " A snapshot from a phone held at waist height on the path, looking a little up. She walks along the park path towards the "
    "camera, caught mid-stride: her left foot planted, the right foot swinging forward, arms swinging easily, eyes ahead, the green "
    "bandstand behind her. The whole of her is in frame from her hair to her trainers. " + S("AFTER-EASE"),
    DENISE + " Wearing " + WARD["D-D2"] + ".", PARK,
    PROD + " " + RIGID + " " + worn("her") + " Seated exactly as in the attached front worn reference.",
    angle("B1-08", "her"), focus("the whole figure", deep=True), light("PARK", "her"), colour("PARK", "she")],
    WORN_NEG + ", no other people close, no dog, " + NEG_EFF))
B["B1-09a"] = (NBP, ["front", "back", "R2-ALAN", "P1-A-GARDEN", "worn_front"], photo([
    SAME + " A snapshot from a phone held low on the lawn, three-quarter to his right leg. He stands on the grass, his right stone trouser "
    "leg rolled up above the knee in a thick roll, the strap on his bare right knee; his right hand has just let go of the roll, fingers "
    "opening beside it, the roll just starting to drop. The frame runs from his hand at mid-thigh down to his boots. " + SKIN["m70"],
    "His hand and legs: " + ALAN.split(" — ")[0] + ". Wearing " + WARD["A-D2"] + ", the right leg rolled up above the knee.", GARDEN,
    PROD + " " + RIGID + " " + worn("his") + " Seated exactly as in the attached front worn reference.",
    angle("B1-09a", "his right knee"), focus("the product and its wordmark"), light("GARDEN", "his knee", face=False), colour("GARDEN", "he")],
    WORN_NEG + ", no left trouser leg rolled, no face, " + NEG_HANDS))
B["B1-09b"] = (NB2, ["R2-ALAN", "P1-A-GARDEN"], photo([
    "A snapshot from a phone at eye level across the lawn, in profile. He walks across the lawn from left to right towards the raised "
    "vegetable bed carrying a green plastic watering can in his right hand, caught mid-stride, eyes ahead, relaxed, not thinking about "
    "his knee. The whole of him is in frame. " + S("AFTER-EASE") + " " + P.WEAR_CONCEAL.replace("[GARMENT]", "stone cotton trousers"),
    ALAN + " Wearing " + WARD["A-D2"] + ", both trouser legs down to the boots.", GARDEN,
    angle("B1-09b", "him"), focus("the whole figure", deep=True), light("GARDEN", "him"), colour("GARDEN", "he")],
    P.NEG_CONCEAL + ", no shorts, no bare knees, " + NEG_EFF))
B["B1-10"] = (NBP, ["front", "back", "R3-CLIVE", "P3-C-SHOP", "worn_front"], photo([
    SAME + " A snapshot from a phone set on the shop floor, three-quarter to him, looking up. He walks along the aisle towards the lens "
    "carrying a cardboard box of stock in both hands at his waist, caught mid-stride: the right foot forward and planted, the strapped "
    "right knee near the lens, eyes ahead. The frame runs from his chest down to the floor. " + S("AFTER-EASE") + " " + SKIN["dark"].replace("sixty-five", "sixty-seven"),
    CLIVE + " Wearing " + WARD["C-D1"] + ".", SHOP,
    PROD + " " + RIGID + " " + worn("his") + " Seated exactly as in the attached front worn reference.",
    angle("B1-10", "him"), focus("the whole figure", deep=True), light("SHOP", "him"), colour("SHOP", "he")],
    WORN_NEG + ", no readable text on the box, no brand on the tins, " + NEG_EFF))
B["B1-11"] = (NBP, ["front", "back", "R4-FIONA", "worn_rear"], photo([
    "A snapshot from a phone held at eye level a few steps behind her on the path. She walks away along the clifftop path, seen from "
    "directly behind, caught mid-stride, the sea wide on the left, the path running on ahead of her. The whole of her is in frame, not "
    "small. " + S("AFTER-EASE"),
    FIONA + " Wearing " + WARD["F-D2"] + ".", COAST,
    PROD + " Seen from directly behind, exactly as in the attached rear-worn reference: " + P.ORIENT_LOCK,
    angle("B1-11", "her"), focus("the whole figure", deep=True), light("COAST", "her"), colour("COAST", "she")],
    P.NEG_ORIENT + ", no strap on the left knee, no second strap, no wordmark visible from behind, no other people, " + NEG_EFF))
B["B1-12a"] = (NBP, ["package_open", "front", "R1-DENISE", "P2-D-LOUNGE"], photo([
    "The box in this photo is THE EXACT SAME BOX as the FIRST attached photo, open. A snapshot from a phone held straight above the "
    "coffee table, looking down. The open box sits on the low oak table, the two straps side by side in the insert; her right hand has "
    "just laid the lid down flat beside the box and is lifting away from it, fingers still near its edge. Only her hand and wrist come in "
    "from the right: a sixty-four-year-old Black woman's hand, dark brown skin, short unpainted nails, the mustard-yellow cuff.",
    P.PACKAGE_LOCK + " Each strap is THE EXACT SAME OBJECT as the second attached product photo. " + P.WORDMARK_LOCK,
    LOUNGE.replace("THE SAME LOUNGE", "THE SAME LOUNGE, seen from directly above the coffee table,"),
    angle("B1-12a", "the open box"), focus("the product and its wordmark"), light("LOUNGE", "the box", face=False), colour("LOUNGE", "she")],
    P.NEG_PACKAGE + ", " + BLOCK_NEG + ", no face, " + NEG_HANDS))
# v2 Fix "Show two straps placed on the table": v1 floated them on a dark card. Now the two straps lie side by side on the lounge's
# oak coffee table (the confirmed lounge plate), a phone snapshot from above; the clear bands for the edit's offer text stay.
B["CARD-12b"] = (GPT, ["front", "back", "P2-D-LOUNGE"], "\n\n".join([
    "A phone snapshot looking down at a low angle onto the low oak coffee table in THE SAME LOUNGE exactly as in the third attached "
    "location plate, vertical 9:16. Two identical straps lie flat side by side on the bare oak tabletop in the middle band of the frame, "
    "a hand's width apart, shells face up, both front faces and wordmarks to the camera, the knit bands resting in closed loops behind "
    "them on the wood, each casting a soft natural shadow. Morning daylight from the bay window; the kilim rug and the teal sofa soft "
    "and out of focus beyond the table's edge.",
    "Each strap is THE EXACT SAME OBJECT as the first attached product photo — " + PROD.split(" — ", 1)[-1] + " " + RIGID + " "
    + P.WORDMARK_LOCK + " The black band of each is a closed loop behind its shell, joined at both chrome slides.",
    "Leave the top third and the bottom fifth of the frame clear — plain tabletop and soft room only (text is added in the edit).",
    "AVOID: no text, no offer text, no price, no badge, no numbers, no logos other than the stryde wordmark, no box, no third strap, "
    "no hands, no people, no other objects on the table, no floating straps, no dark studio background, no packshot, " + BLOCK_NEG]))
# v2 Fix "CHANGE THIS": the user took the strap off B1-13b, the next shot; v1 still wore it, so the two stair shots broke continuity.
# Fixed as B1-13b v2: no strap, bare knees, product blocks and refs out.
B["B1-13a"] = (NBP, ["R4-FIONA", "P5-PROP-F"], photo([
    "A snapshot from a phone held high at the top of the stairs in front of her, looking down at her and the flight "
    "falling away below. " + S("STAIR-DOWN") + " She stands on the small landing at the top, looking down the flight, one easy breath, relaxed, the trouser "
    "legs rolled above both knees, both knees bare with nothing on them. The whole of her is in frame.",
    FIONA + " Wearing " + WARD["F-D1"] + ".", HALL,
    angle("B1-13a", "her"), focus("the nearest eye of Fiona"), light("HALL", "her"), colour("HALL", "she")],
    "no strap, no knee strap, no brace, no sleeve, no support on either knee, no black band on the leg, no stryde wordmark, " + NEG_SUP
    + ", no worried face, no hand on the banister"))
# v2 Fix "REMOVE THE STRAP": the user's call — the shot carries no strap. The product blocks and refs come out, the knees stay bare.
B["B1-13b"] = (NBP, ["R4-FIONA", "P5-PROP-F"], photo([
    SAME + " A snapshot from a phone held low at the foot of the stairs, three-quarter to her, tilted up the flight. She is coming DOWN "
    "the stairs forwards towards the camera, caught mid-step: her left foot planted on the fourth stair from the bottom, the strapped "
    "right foot reaching down to the next step, her hands free at her sides and off the rail, eyes ahead. The whole of her is in frame "
    "from her hair to her sandals. " + S("AFTER-EASE"),
    FIONA + " Wearing " + WARD["F-D1"] + ".", HALL,
    "Both knees are bare below the rolled trouser legs — nothing on either knee.",
    angle("B1-13b", "her"), focus("the whole figure", deep=True), light("HALL", "her"), colour("HALL", "she")],
    "no strap, no knee strap, no brace, no sleeve, no support on either knee, no black band on the leg, no stryde wordmark, no trousers "
    "rolled down over the knees, " + NEG_SUP + ", " + NEG_EFF))

# ── Body 1: a live-action B-roll for every line (user, 2026-09-29 — "Create a B-roll for every line") ──────────────────
# B1-02a on "They're small on purpose", B1-03a on "Seventeen times your bodyweight…", B1-07a on "Perfect for bone on bone, arthritis…";
# the anatomy renders keep the second half of B1-03 and B1-07.
# v2 Fix "CHANG THIS": v1 read as the strap being put on low on the shin (the band round the leg, side-on) — B1-04b again — and the
# room drifted off the plate. Fixed: three-quarter front, the strap held up IN FRONT of the bare knee, a hand's width towards the lens,
# front face to camera, so its small size reads against the knee behind it; never touching the leg; the plate restated.
B["B1-02a"] = (NBP, ["front", "back", "R1-DENISE", "P2-D-LOUNGE"], photo([
    SAME + " A snapshot from a phone at knee height, three-quarter in front of her. She sits on the edge of the teal velvet sofa, her bare "
    "right knee bent at an easy angle, foot flat on the kilim rug, and holds the strap up IN FRONT of the knee — a hand's width towards the "
    "camera, NOT touching the leg — level with the soft spot just under her kneecap, the whole front face and the wordmark square to the "
    "lens: " + PINCH + ". The band hangs slack below her fingers, not round the leg. Seen like this the shell is only as wide as the knee "
    "behind it: small on purpose. Her knee is soft behind the sharp strap. Only her hand, forearm and knees are in frame. " + SKIN["dark"],
    "Her hand and legs: " + DENISE.split(" — ")[0] + " — dark brown skin. Wearing " + WARD["D-D1"] + ".", LOUNGE,
    PROD + " " + RIGID + " " + P.WORDMARK_LOCK + " " + P.SIZE_HELD,
    angle("B1-02a", "her hand and her right knee"), focus("the product and its wordmark"), light("LOUNGE", "her knee", face=False), colour("LOUNGE", "she")],
    P.NEG_HELD_P + ", " + P.NEG_WORDMARK + ", " + BLOCK_NEG + ", no strap worn, no strap touching the knee, no strap on the shin, no band round the leg, no strap being put on, "
    "no side-on strap, no second strap, no face, no fireplace, no white room, no third leg, no extra limb, " + NEG_HANDS))
B["B1-03a"] = (NBP, ["R2-ALAN", "P0-A-KITCHEN"], photo([
    "A snapshot from a phone held low near the kitchen floor, three-quarter to him. He steps down the single low step from the hall doorway "
    "onto the kitchen floor, caught mid-step: his left foot still on the step, his right foot just landing flat on the floor tiles, his "
    "right knee bending as it takes his whole weight, his hands free at his sides. The whole of him is in frame, from his hair to his slippers, "
    "his face calm and ordinary, a little careful.",
    "He is " + ALAN + " Wearing " + WARD["A-D1"] + ".", KITCHEN + " The hall doorway with its one low step is on the right of the room.",
    angle("B1-03a", "him"), focus("the whole figure", deep=True), light("KITCHEN", "him"), colour("KITCHEN", "he")],
    "no strap, no brace, no sleeve, no support on either knee, no stryde wordmark, no stairs, no second step, no hand on the wall, no hand "
    "on the door frame, no hand on the worktop, no falling, no stumble, no wincing, no grimace"))
B["B1-07a"] = (NB2, ["R2-ALAN", "P0-A-KITCHEN"], photo([
    "A snapshot from a phone held high, looking down at him. He sits on a wooden chair at the kitchen table, turned a little away from it, "
    "and slowly rubs the inside and outside of his right knee through his grey trousers with both hands, fingers spread round the joint, "
    "his head bowed a little towards it, a tired, patient look. Framed from his shoulders to his feet, his face partly visible from above.",
    "He is " + ALAN + " Wearing " + WARD["A-D1"] + ".", KITCHEN,
    angle("B1-07a", "him"), focus("the hands and what they hold"), light("KITCHEN", "him"), colour("KITCHEN", "he")],
    "no strap, no brace, no sleeve, no support on either knee, no stryde wordmark, no trousers rolled up, no wincing, no grimace, no "
    "crying, " + NEG_HANDS))

# ── pinned end frames (act map pin_end, §27G rule 5; E7 first-and-last-frame call) ─────────────────────────────────────
# B1-01a-END — "yes — product placed": the confirmed v1 start frame a second later, the shell now seated on the model's tendon.
END = {}
END["B1-01a-END"] = (NBP, ["B1-01a_v1", "front", "back"], photo([
    "This photo is THE SAME MOMENT AND THE SAME SCENE as the FIRST attached image, a second later — keep the consultant, his face, his "
    "clothes, the desk, the ivory anatomical knee model on its stand, the room behind, the camera position and the light exactly as in it. "
    "The strap is THE EXACT SAME OBJECT as the second attached product photo, the front. The only change: his hands have brought the strap "
    "the last few centimetres in and the shell now rests seated on the model's patellar tendon, directly below the model's kneecap — the "
    "notch cups the kneecap's lower border with no gap, the two peaks no higher than the base of the kneecap's sides, the kneecap's face "
    "bare above, the wordmark horizontal and facing the camera. His right hand holds it there by its two ends, fingertips on the pad behind, "
    "one small press; the black band still hangs loose below, not yet fastened.",
    RIGID + " " + P.WORDMARK_LOCK],
    "no other change to the scene, no size change, no shell over the kneecap, no shell low on the shin, no shell on the thigh, no shell "
    "turned side-on, no pad side showing, no band fastened round the model, no second strap, no strap on a person, no white coat, "
    + BLOCK_NEG + ", " + P.NEG_WORDMARK + ", " + NEG_HANDS))

if __name__ == "__main__":
    act = sys.argv[1] if len(sys.argv) > 1 else "Act 1"
    out = {}
    for beat, (model, refs, prompt) in B.items():
        r = ROWS[beat]
        if r["act"] != act:
            continue
        assert "[" not in prompt, (beat, prompt[prompt.index("["):][:80])
        (HERE / f"{beat}.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt, "act": r["act"], "line": r["phrase"], "chars": len(prompt)}
        print(beat.ljust(9), model.ljust(16), str(len(prompt)).rjust(5), ",".join(refs))
    want = {b for b, r in ROWS.items() if r["act"] == act}
    assert {b for b in out if not b.endswith("-END")} == want, sorted(want ^ set(out))
    for beat, (model, refs, prompt) in END.items():
        if ROWS[beat[:-4]]["act"] != act:
            continue
        assert "[" not in prompt, beat
        (HERE / f"{beat}.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": refs, "prompt": prompt, "act": act, "line": ROWS[beat[:-4]]["phrase"], "chars": len(prompt)}
        print(beat.ljust(9), model.ljust(16), str(len(prompt)).rjust(5), ",".join(refs))
    (HERE / "broll.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
