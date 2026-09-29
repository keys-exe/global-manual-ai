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
    "COAST": ("the high midday sun over the sea on the left", "left", "bright, clean midday light"),
    "HALL": ("the landing window and the front-door glass, both facing south", "right", "bright morning sun falling on the stair carpet"),
}
COLOUR = {  # light colour, kelvin, set colours, wardrobe colours, accent, saturation
    "LOUNGE": ("bright morning daylight", 5600, "warm oak, the red-and-cream kilim, teal velvet, warm-white walls", "mustard yellow and olive", "the teal sofa", "true to life, a touch warm"),
    "CONSULT": ("soft overcast daylight", 6500, "pale grey walls, light wood, white", "pale blue", "the black strap", "true to life, slightly cool"),
    "PARK": ("bright morning daylight", 5600, "green grass, grey tarmac, the green bandstand", "white, lavender and navy", "the lavender jacket", "true to life"),
    "GARDEN": ("bright late-morning sun", 5600, "green lawn, red brick, dark soil in the bed", "pale denim blue and stone", "a green watering can", "true to life, bright"),
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
B["B1-02"] = (NB2, ["R1-DENISE", "P2-D-LOUNGE"], photo([
    "A snapshot from a phone held high, her own view down at her knee. She sits on the edge of the teal sofa, her right leg straight out "
    "in front, and presses her right forefinger into the soft spot just under her right kneecap, the fingertip whole and resting on the "
    "skin, the skin dimpling a little under it, her other hand on her thigh. The frame is tight on the knee and her hand; her face is out "
    "of frame. " + SKIN["dark"],
    "She is " + DENISE + " Wearing " + WARD["D-D1"] + ".", LOUNGE,
    angle("B1-02", "her right knee"), focus("the hands and what they hold"), light("LOUNGE", "her knee", face=False), colour("LOUNGE", "she")],
    "no strap, no brace, no sleeve on the knee, no second hand on the knee, no fingernail digging in, no face, " + NEG_HANDS))
B["MECH-02"] = (NB2, [], anat(
    "Heel strike: the foot has just landed and the body's weight is coming down the thigh. " + S("ANAT-LOAD") + " " + S("ANAT-HOT") + " "
    + P.ANAT_A_POINT_TIGHT, extra_neg="no glow in the joint space, no glow on the cartilage, no strap, no brace", view=LOW_VIEW))
B["MECH-03"] = (NB2, [], anat(
    "A big generic wraparound knee brace, plain grey, no brand, with two steel hinged side bars and three wide straps, wraps the whole knee "
    "from mid-thigh to mid-shin, drawn as a faint translucent shell squeezing evenly all round; beneath it the single tight red-hot glow "
    "on [SITE] stays exactly as bright as before, untouched. " + P.ANAT_A_POINT_TIGHT,
    extra_neg="no strap, no rigid black shell, no wordmark", view=HIGH_VIEW))
B["B1-04b"] = (NBP, ["front", "back", "R1-DENISE", "P2-D-LOUNGE"], photo([
    SAME + " A snapshot from a phone held at knee height beside the sofa, in profile to her right leg. She sits on the sofa edge, her right "
    "leg out straight, foot on the rug. The strap is already closed round her shin, sitting low at mid-shin, and both her hands have it: "
    "palms and fingertips flat on the two sides of the shell, just beginning to slide it UP her shin towards the knee, caught mid-slide. "
    "The kneecap stands bare above it. Only her hands, forearms and legs are in frame. " + SKIN["dark"],
    "Her hands and legs: " + DENISE.split(" — ")[0] + " — dark brown skin. Wearing " + WARD["D-D1"] + ".", LOUNGE,
    PROD + " " + RIGID + " " + P.WORDMARK_LOCK + " " + P.SIZE_WORN.split(";")[0] + ".",
    angle("B1-04b", "her right leg"), focus("the product and its wordmark"), light("LOUNGE", "her leg", face=False), colour("LOUNGE", "she")],
    "no strap over the kneecap, no strap on the left leg, no second strap, no band open, no velcro, no buckle, no hand gripping the band, "
    + BLOCK_NEG + ", no face, " + NEG_HANDS))
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
    SAME + " A snapshot from a phone at eye level. She holds the strap up at chest height in front of the bay window, front face and "
    "wordmark to the lens: " + PINCH + ". Nothing rises above the shell's top edge; both peaks and the notch stand clear against the "
    "bright window behind, which falls soft. Only her hand and forearm come in from the right. Her hand is a sixty-four-year-old Black "
    "woman's hand: dark brown skin, deeper creases over the knuckles, short unpainted nails, the mustard-yellow sleeve at the elbow.",
    LOUNGE.replace("THE SAME LOUNGE", "THE SAME LOUNGE, the bay window behind her hand,"),
    PROD + " " + RIGID + " " + P.WORDMARK_LOCK + " " + P.SIZE_HELD,
    angle("B1-06", "her hand and the strap"), focus("the product and its wordmark"), light("LOUNGE", "the strap", face=False), colour("LOUNGE", "she")],
    P.NEG_HELD_P + ", " + P.NEG_WORDMARK + ", " + BLOCK_NEG + ", no face, no silhouette, no backlit black shape, " + NEG_HANDS))
B["MECH-05"] = (NB2, [], anat(
    "CONDITIONS: the cartilage lining the joint surfaces is worn thin and patchy, the femur and tibia sitting close, bone nearly on bone, "
    "and the edge of the meniscus between them is torn and frayed; a dull red glow sits in the narrowed joint space and along the torn "
    "meniscus edge, the rest calm.", look="B", extra_neg="no strap, no brace, no glow on the tendon", view=TQ_VIEW))
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
B["CARD-12b"] = (GPT, ["front", "back"], "\n\n".join([
    "A clean product still on a plain background, vertical 9:16. Two identical straps float side by side in the middle of the frame, a "
    "little apart, both front face and wordmark to the camera, level, against a smooth dark navy-black background with a soft light from "
    "above that falls off gently towards the bottom of the frame and a faint soft shadow under each.",
    "Each strap is THE EXACT SAME OBJECT as the first attached product photo — " + PROD.split(" — ", 1)[-1] + " " + RIGID + " "
    + P.WORDMARK_LOCK + " The black band of each is a closed loop behind its shell, joined at both chrome slides.",
    "Leave the top third and the bottom fifth of the frame clear, plain background only (text is added in the edit).",
    "AVOID: no text, no offer text, no price, no badge, no numbers, no logos other than the stryde wordmark, no box, no third strap, "
    "no hands, no people, no props, no reflections on a floor, no gradient bands, " + BLOCK_NEG]))
B["B1-13a"] = (NBP, ["front", "back", "R4-FIONA", "P5-PROP-F", "worn_front"], photo([
    SAME + " A snapshot from a phone held high at the top of the stairs in front of her, looking down at her and the flight "
    "falling away below. " + S("STAIR-DOWN") + " She stands on the small landing at the top, looking down the flight, one easy breath, relaxed, the strap on her bare right knee, the trouser "
    "legs rolled above both knees. The whole of her is in frame.",
    FIONA + " Wearing " + WARD["F-D1"] + ".", HALL,
    PROD + " " + RIGID + " " + worn("her") + " Seated exactly as in the attached front worn reference.",
    angle("B1-13a", "her"), focus("the nearest eye of Fiona"), light("HALL", "her"), colour("HALL", "she")],
    WORN_NEG + ", " + NEG_SUP + ", no worried face, no hand on the banister"))
B["B1-13b"] = (NBP, ["front", "back", "R4-FIONA", "P5-PROP-F", "worn_bent"], photo([
    SAME + " A snapshot from a phone held low at the foot of the stairs, three-quarter to her, tilted up the flight. She is coming DOWN "
    "the stairs forwards towards the camera, caught mid-step: her left foot planted on the fourth stair from the bottom, the strapped "
    "right foot reaching down to the next step, her hands free at her sides and off the rail, eyes ahead. The whole of her is in frame "
    "from her hair to her sandals. " + S("AFTER-EASE"),
    FIONA + " Wearing " + WARD["F-D1"] + ".", HALL,
    PROD + " " + RIGID + " " + P.PLACE_BENT + " Worn exactly as in the attached bent-knee reference, on her RIGHT knee only.",
    angle("B1-13b", "her"), focus("the whole figure", deep=True), light("HALL", "her"), colour("HALL", "she")],
    WORN_NEG + ", " + NEG_SUP + ", " + NEG_EFF))

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
    assert set(out) == want, sorted(want ^ set(out))
    (HERE / "broll.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
