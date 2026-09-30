#!/usr/bin/env python3
"""Step 7 body B-roll start images for stryde-not-your-cartilage (act map work/actmap.json, STEP4_5.md light plans and wardrobe).
Mode 1 phone seeds: CAM-LOCK -> FRAME-SCALE -> prose -> plate -> product -> angle -> focus -> light -> colour -> CAP-FILE -> negatives.
Product strings from the STRYDE product sheet module; placeholders from Appendix A by ID. Writes body/<BEAT>.t2i.txt + body.json.
Anatomy beats use ANAT-A (full stack) with named fine detail on every beat: the user's HK1-01 Fix "MAKE MORE DETAILS" applied globally (§34)."""
import json, re, sys, pathlib
H = pathlib.Path(__file__).resolve().parent; B = H.parent; ROOT = B.parents[1]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
sys.path.insert(0, str(ROOT / "products/stryde")); import stryde_product_sheet as P  # noqa: E402
REFS = ROOT / "products/stryde"
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S); return m.group(1).strip()
ROWS = {r["beat"]: r for r in json.loads((B / "work/actmap.json").read_text())["rows"]}
HEIGHT = {"overhead": "an overhead camera looking straight down", "high": "a high camera looking down", "eye": "an eye-level camera",
          "low": "a low camera close to the floor looking up", "ground": "a camera at ground level, at knee height"}
SIDE = {"front": "the front", "three-quarter": "three-quarter", "profile": "the side, in profile", "ots": "over the shoulder", "behind": "directly behind"}
def angle(b, subj, fg=""):
    r = ROWS[b]; return (S("ANGLE-LINE").replace("[HEIGHT CLAUSE from §30I]", HEIGHT[r["height"]]).replace("[SIDE]", SIDE[r["side"]])
        .replace("[SUBJECT]", subj).replace("[, looking past FOREGROUND, soft in the near foreground | , seen in REFLECTION]", fg))
def focus(plane, deep=False):
    return (S("FOCUS-LINE").replace("[PLANE — the nearest eye of NAME / the hands and what they hold / the product and its wordmark / the foreground / everything]", plane)
        .replace("[DEPTH — the room behind falls to a soft, recognisable shape | everything from near to far stays sharp]",
                 "everything from near to far stays sharp" if deep else "the room behind falls to a soft, recognisable shape"))
def light(src, subj, side, q, face=True):
    s = (S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", src).replace("[SUBJECT]", subj)
         .replace("[SCREEN SIDE]", side).replace("[TIME-OF-DAY QUALITY and the act's light state]", q).replace("toward [SIDE]", f"toward the {side}"))
    if not face:
        s = s.replace(f"so the face has a lit side toward the {side} and a softer shadow side, with a small catchlight in the eyes", f"so it has a lit side toward the {side} and a softer shadow side")
    return s
def colour(lc, k, sc, who, wc, ac, sat):
    return (S("COLOUR-KEY").replace(", exactly as in the attached master frame", "").replace("[LIGHT COLOUR]", lc).replace("[KELVIN]", str(k))
        .replace("[SET COLOURS]", sc).replace("[WHO]", who).replace("[WARDROBE COLOURS]", wc).replace("[ACCENT]", "the accent is " + ac).replace("[SATURATION AND CONTRAST IN CAMERA]", sat))
NEG_BASE = ("no readable text, no logos other than the stryde wordmark, no AI face, no plastic skin, no waxy skin, no extra fingers, no fused fingers, no polished render, "
            "no advertising image, no studio lighting, no vignette, no glowing skin, no light from nowhere, no shadows falling in two directions, no lens flare")
NEG_HANDS = "no wrong finger count, no malformed hands, no hands merging into objects"
def photo(parts, avoid, scale="about three quarters"):
    return "\n\n".join([S("CAM-LOCK"), S("FRAME-SCALE").replace("[SCALE]", scale)] + [p for p in parts if p] + [P.BODY_WHOLE, S("CAP-FILE"), "AVOID: " + avoid + ", " + NEG_BASE])
def plate(name, anchors, prop=None):
    s = (S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", prop) + " ") if prop else ""
    return s + f"THE SAME PLACE exactly as in the attached location plate — {anchors}."
PROD = P.REF_PROD.replace("the attached reference image", "the attached product photos").rstrip(" —") + "."
RIGID = "It is a RIGID MOULDED shell with a hard edge, never fabric, never neoprene."
WORN = " ".join([PROD, RIGID, P.fill(P.PLACE_LOCK, "right"), P.FIT_SNUG, P.SIZE_WORN, P.WORDMARK_LOCK, P.LEG_SKIN])
WORN_BENT = " ".join([PROD, RIGID, P.fill(P.PLACE_BENT, "right"), P.FIT_SNUG, P.SIZE_WORN, P.WORDMARK_LOCK, P.LEG_SKIN])
NEG_WORN = P.fill(", ".join([P.NEG_PLACE, P.NEG_ORIENT, P.NEG_WORDMARK, P.NEG_OBSERVED, "no strap on the left knee, no strap on both knees, no strap over clothing"]), "right")
HELD = lambda grip: " ".join([PROD, RIGID, "Held: " + dict(P.HELD_GRIPS)[grip] + ".", P.WORDMARK_LOCK, P.SIZE_HELD])
NEG_HELD = ", ".join([P.NEG_HELD_P, P.NEG_WORDMARK, P.NEG_OBSERVED, NEG_HANDS])
# people (identity read off the confirmed sheets; wardrobe per the STEP4_5 ledger)
FOLAKE = ("the woman in the attached character sheet — a Black British woman of Nigerian heritage, sixty-six: wide face, very high prominent cheekbones, narrow pointed chin, "
          "narrow deep-set dark eyes, broad flat nose, wide mouth with a full lower lip, the small keloid bump on the top rim of her right ear, long thin grey-and-black box braids "
          "tied back in a low ponytail, slim and wiry — her real age showing, bare face")
DEREK = ("the man in the attached character sheet — a white British man of seventy-four from the north-east: broad square face, heavy-lidded pale grey eyes, bushy white brows, "
         "a wide flattened nose, a short clipped white beard, thick wavy white hair combed back, big-framed with a round belly, the top joint of his left index finger missing — his real age showing")
HASSAN = ("the man in the attached character sheet — a Black British man of Sudanese heritage, seventy-two, very dark skin: a long face with a heavy square jaw and hollow cheeks, "
          "deep-set eyes under a heavy brow ridge, a long nose broad at the tip, clean-shaven with grey stubble, a short rounded grey afro thinning at the crown, the thin pale scar along "
          "his right jawline, very tall and thin with a slight stoop — his real age showing")
ELAINE = ("the woman in the attached character sheet — a white British woman of Welsh heritage, sixty-three: narrow heart-shaped face, pointed chin, wide-set bright blue eyes, "
          "a long thin nose with a slight bump, thin lips, three small pale moles under her left eye, an ash-grey blonde pixie cut, petite and slim — her real age showing, bare face")
WARD = {
 "F-D1": "a long burnt-orange knitted cardigan over a black long-sleeved jersey top, charcoal jersey trousers and maroon slippers",
 "F-D2": "a yellow-and-green wax-print short-sleeved blouse, a navy cotton skirt ending just above the knee so the right knee is bare, tan leather flat sandals",
 "D-D1": "a checked flannel shirt under an olive waxed jacket zipped up, dark jeans, brown walking boots and a tweed flat cap",
 "D-D2": "a grey T-shirt under an open navy fleece, khaki walking shorts ending above the knee so both knees are bare, black trail shoes with grey socks",
 "D-D3": "a blue-and-white striped shirt with the sleeves rolled, stone chino shorts ending above the knee so both knees are bare, brown lace-up shoes",
 "H-D1": "a white shirt under a navy V-neck cardigan, grey wool trousers and black leather shoes",
 "H-D2": "a maroon polo shirt, charcoal cotton shorts ending above the knee so both knees are bare, brown leather slippers",
 "E-D3": "a navy-and-white striped long-sleeved top, olive cotton shorts ending mid-thigh so both knees and shins are bare, barefoot",
  "E-D1": "a navy-and-white striped long-sleeved top, olive cropped cotton trousers rolled up above the right knee so the knee is bare, white canvas trainers",
}
CS01 = "the consultant — a white British woman of about fifty with a short dark bob, in a navy knee-length dress with a blank lanyard, no white coat"
SG01 = "the surgeon — a Black British man of about fifty-five with a close grey beard and short greying hair, in a pale blue shirt with the sleeves rolled, no white coat, approachable"
# locations: plate anchors + light plan
LOC = {
 "P1": ("plates/P1-F-LOUNGE_v1.jpg", "Folake's front lounge: the burgundy armchair with its crocheted cream cushion, the glass-topped coffee table on the cream rug, the wide east window with net curtains and gold curtains tied back, the brass standard lamp, the rubber plant", "the magnolia woodchip walls, plain white woodwork and the mid-oak laminate"),
 "P0": ("plates/P0-PROP-FO_v1.jpg", "Folake's hall: the straight staircase rising along the right-hand wall with the white handrail and square spindles and the deep red stair carpet, the telephone table at the foot of the stairs, the coat rack by the door", "the magnolia woodchip walls, plain white woodwork and the mid-oak laminate"),
 "P2": ("plates/P2-D-TOWPATH_v1.jpg", "the canal towpath: the gravel path, the still canal on the left with its stone edge, the humped stone bridge in the middle distance, the moored narrowboats, the wooden bench in the hedgerow on the right", None),
 "P3": ("plates/P3-PROP-H_v1.jpg", "Hassan's hall: the steep straight staircase rising along the left-hand wall with the dark-stained handrail on turned white spindles and the brown-and-gold patterned carpet up every stair, the shoe rack by the door, the woven wall hanging", "the pale sage walls, tall white moulded skirting, dark-stained panel doors and the brown-and-gold patterned carpet"),
 "P4": ("plates/P4-H-KITCHEN_v1.jpg", "Hassan's galley kitchen: cream units with wooden trim, the dark speckled worktop, the window over the stainless-steel sink on the far wall, the white electric kettle, the round tin tea caddy, the chequered vinyl floor", "the pale sage walls, tall white moulded skirting, dark-stained panel doors and the brown-and-gold patterned carpet"),
 "P5": ("plates/P5-E-BEDROOM_v1.jpg", "Elaine's bedroom: the double bed with the white-and-grey striped duvet, the south sash window on the right, the white wardrobe, the cane-seated chair by the window, the stripped pine floorboards", None),
 "P6": ("plates/P6-CONSULT_v1.jpg", "the consultant's room: the X-ray light box on the far wall, the blue examination couch with its paper roll and two-step footstool, the desk under the left-hand window, the pale grey-blue walls", None),
}
SHEET = {"R1": "cast/R1-FOLAKE_v1.jpg", "R2": "cast/R2-DEREK_v1.jpg", "R3": "cast/R3-HASSAN_v1.jpg", "R4": "cast/R4-ELAINE_v1.jpg"}
PR = lambda *k: [str(REFS / f) for f in k]
FRONT, BACK = "stryde_refs/front.webp", "stryde_refs/back.webp"
# anatomy (ANAT-A everywhere + fine detail, §34 global from HK1-01's Fix)
SL = P.SLOTS
def fillx(s, **kw):
    for k, v in kw.items(): s = s.replace(f"[{k.replace('_',' ')}]", v)
    return s
DETAIL = ("FINE DETAIL, rendered with the density of a high-end medical-atlas CGI: the patellar tendon a thick pearly band from the lower edge of the kneecap down to the shin, "
          "its fine lengthwise fibre sheen visible; the quadriceps tendon above the kneecap; the collateral ligaments on both sides of the joint as pale silvery straps; the crescent-shaped "
          "menisci as pale translucent wedges between the bones; the bone surfaces with fine grain and small pores; the translucent outer contour with a faint glassy sheen.")
MODULATION = ("no crossfade, no glow fading in place, no gradual onset, no delay before the modulation starts, no build-up, no ignition, no steady unchanging glow, no emission settling or resolving, ")
def anat(scene, prod=False, neg_extra="", modulating=True, view=None):
    base = fillx(S("ANAT-BASE"), REGION=SL["REGION"], TARGET_JOINT=SL["TARGET_JOINT"])
    if view: base = base.replace("viewed from a low three-quarter angle", view)
    neg = S("ANAT-NEG").replace("no individual muscle fibres, ", "")
    if not modulating: neg = neg.replace(MODULATION, "")
    if prod: neg = neg.replace("no rigid brace, no hinges, no sleeve, no second unit, no product half-on, ", "no second unit, no product half-on, ")
    parts = [base, fillx(S("ANAT-A"), STACK=SL["STACK"], BONES=SL["BONES"]), DETAIL, scene]
    if prod: parts.append(PROD + " " + RIGID + " " + P.fill(P.PLACE_LOCK, "right") + " " + P.WORDMARK_LOCK + " " + S("ANAT-PROD"))
    parts += [fillx(S("ANAT-LIGHT"), TARGET=SL["TARGET"]), S("ANAT-FIELD"), "AVOID: " + neg + ", no sparse empty interior, no low detail" + neg_extra]
    return "\n\n".join(parts)
BEATS = {}
def add(beat, model, refs, prompt): BEATS[beat] = (model, refs, prompt)
# ---- Act 1 ----
add("B-01a", "nano-banana-pro", PR(FRONT, "stryde_refs/package_open.jpg") + [SHEET["R2"], LOC["P2"][0]], photo([
  "A snapshot from a phone held high over his lap, looking down. He sits on the wooden bench on the towpath and his hands have just lifted the lid off the box resting on his knees: " + P.PACKAGE_LOCK +
  " The lid is in his left hand, tilted up at the top of the frame; his right hand steadies the box. His hands are " + DEREK + "'s hands: big, weathered, sun-mottled, the top joint of the left index finger missing. "
  "He wears " + WARD["D-D2"] + "; his knees and the khaki shorts are soft at the bottom of the frame.",
  plate("P2", LOC["P2"][1]), angle("B-01a", "the open box"), focus("the two straps in the box and their wordmarks"),
  light("open sky, the cloud broken, sun high on the left", "the box and his hands", "left", "late-morning daylight", face=False),
  colour("clear daylight", 5600, "the grey-green towpath, the weathered bench", "he", "navy and khaki", "the matte-black box", "natural, true to life")],
  P.NEG_PACKAGE + ", " + P.NEG_WORDMARK + ", no strap worn, no face, " + NEG_HANDS, scale="about three quarters"))
add("MECH-S1", "nano-banana-2", PR(FRONT, BACK), anat(
  "THE STATE: the strap is seated on the patellar tendon just below the kneecap and glows a clean electric blue along its edges; the tendon beneath it is calm and blue-white, no red anywhere. Protected, calm.", prod=True, neg_extra=", no red glow, no orange glow"))
add("MECH-S2", "nano-banana-2", [], anat(
  "THE STATE: the knee is wrapped in a big bulky blank wraparound brace — a thick fabric sleeve with two steel hinge bars down its sides and three wide straps, no brand — rendered solid over the translucent limb, "
  "and under it the joint glows hot red-orange, the heat spreading through the whole joint the brace wraps. " +
  fillx(S("ANAT-HOT"), REGION=SL["REGION"], TARGET=SL["TARGET"], SITE="the whole knee joint under the brace", BONES=SL["BONES"], STACK=SL["STACK"]),
  view="viewed three-quarter from the front").replace("no rigid brace, no hinges, no sleeve, ", "") + ", no strap, no stryde wordmark, no brand on the brace")
add("MECH-01", "nano-banana-2", [], anat(
  "THE STATE — BONE ON BONE: the cartilage capping the femur and the tibia is worn away on the inner side, the joint space closed so bone meets bone, rough and pitted where they touch, "
  "and exactly there the joint glows hot red-orange, near-white at the core where bone grinds on bone. " +
  fillx(S("ANAT-HOT"), REGION=SL["REGION"], TARGET="the worn joint surfaces", SITE="the inner side of the knee joint where bone meets bone", BONES=SL["BONES"], STACK=SL["STACK"]),
  view="viewed low and from the side, in profile", neg_extra=", no strap, no product"))
add("B-02b", "nano-banana-2", [SHEET["R3"], LOC["P6"][0]], photo([
  "A snapshot across the consultant's desk. He sits in the visitor's chair facing the camera, hands on his knees, looking down at the plastic knee model the consultant has just turned towards him on the desk, "
  "listening, quiet, worried. " + HASSAN[0].upper() + HASSAN[1:] + ". He wears " + WARD["H-D1"] + ". In the near foreground at the left, out of focus, the back of the head and navy shoulder of " + CS01 + "; her face is not seen.",
  plate("P6", LOC["P6"][1]), angle("B-02b", "the consultant, towards him", ", looking past her navy shoulder, soft in the near foreground"), focus("the nearest eye of Hassan"),
  light("the window on the consulting room's left-hand wall", "him", "left", "overcast morning daylight"),
  colour("overcast morning daylight", 6500, "pale grey-blue walls, the light wood desk", "he", "white and navy", "the red ligaments of the knee model", "cool, true to life"), S("SKIN-B1")],
  "no knee strap, no brace, no X-ray numbers, no text on screens, no smile, no looking at the camera, " + NEG_HANDS))
add("B-03a", "nano-banana-2", [SHEET["R2"], LOC["P2"][0]], photo([
  "A snapshot on the towpath, caught mid-moment: walking along the path he has just stopped, weight on his left leg, his right hand pressed onto his right knee through his jeans, leaning a little, "
  "a wince on his face. " + DEREK[0].upper() + DEREK[1:] + ". He wears " + WARD["D-D1"] + ". No strap, no brace.",
  plate("P2", LOC["P2"][1]), angle("B-03a", "him"), focus("everything", deep=True),
  light("open sky under high thin cloud, the sun a pale disc high on the left", "him", "left", "flat bright overcast"),
  colour("flat bright overcast", 6500, "grey-green towpath, brown-green canal, the stone bridge", "he", "olive and denim", "the tweed cap", "muted, slightly cool"), S("SKIN-B1")],
  "no knee strap, no brace, no walking stick, no second person, no smile"))
add("B-03b", "nano-banana-2", [SHEET["R3"], LOC["P3"][0]], photo([
  "A snapshot from the foot of the stairs looking up the whole flight: he stands IN THE MIDDLE OF THE STAIRCASE, on the seventh step of fourteen, with about six carpeted steps "
  "visible below his feet running down to the camera and about six more rising above his head to the landing, so he is clearly halfway up, never at the bottom and never at the top. "
  "Both feet on that one step, his right hand gripping the dark handrail hard, pausing with a wince, breathing out. " + HASSAN[0].upper() + HASSAN[1:] + ". He wears " + WARD["H-D1"] + ". No strap, no brace.",
  plate("P3", LOC["P3"][1], LOC["P3"][2]), angle("B-03b", "him on the stairs"), focus("the nearest eye of Hassan"),
  light("the front door's coloured-glass panel behind the camera and the half-landing window above", "him", "right", "warm morning daylight"),
  colour("warm morning daylight", 5600, "pale sage walls, the brown-and-gold patterned stair carpet, the dark handrail", "he", "white and navy", "the woven wall hanging", "natural"), S("SKIN-B1")],
  "no knee strap, no brace, no walking stick, no stairlift, no smile, no looking at the camera, no man on the bottom steps, no man at the foot of the stairs, no man at the top of the stairs, " + NEG_HANDS))
add("B-03c", "nano-banana-2", [SHEET["R1"], LOC["P1"][0]], photo([
  "A snapshot caught mid-action from a phone held a little above her: she is half-way up out of the burgundy armchair, both hands pushing down on its wooden arms, her body leaning forward over her knees, "
  "a wince on her face. " + FOLAKE[0].upper() + FOLAKE[1:] + ". She wears " + WARD["F-D1"] + ". No strap, no brace.",
  plate("P1", LOC["P1"][1], LOC["P1"][2]), angle("B-03c", "her"), focus("the nearest eye of Folake"),
  light("the wide window on the lounge's east wall", "her", "left", "bright morning daylight through the nets"),
  colour("soft bright morning daylight through net curtains", 5600, "magnolia walls, the burgundy armchair, the cream rug", "she", "burnt orange and black", "her maroon slippers", "natural, a little flat"), S("SKIN-B1")],
  "no knee strap, no brace, no walking stick, no smile, no looking at the camera, no mug, " + NEG_HANDS))
# ---- Act 2 ----
# v2 (Fix "wrong product, use the reference product"): v1 drew a small dog-bone shell with a loose strap -> the strap large in frame as the closed ring of the front photo
REF_EXACT = ("EXACTLY THE PRODUCT IN THE ATTACHED FRONT PHOTO, copied shape for shape: the band is a CLOSED RING of black knit elastic, the wide shell set into the front of the ring, "
             "its top edge rising into two rounded pointed peaks either side of a wide shallow notch, a brushed chrome slide at each end where the band enters the shell, the grey stryde wordmark "
             "on the shell's lower body. Never a loose flat strap, never a dog-bone or bow-tie shape, never a small shell.")
add("B-04", "nano-banana-pro", PR(FRONT, "stryde_refs/product_tq_left.jpg", BACK) + [SHEET["R2"], LOC["P2"][0]], photo([
  "A close snapshot on the towpath: his hand held out at chest height, the strap standing in his open palm as a closed ring, the front of the shell and its wordmark square to the phone, "
  "the strap large, filling about half the width of the frame. " + REF_EXACT + " " + HELD("open palm") +
  " His hand is " + DEREK + "'s hand: big, weathered, sun-mottled. The canal and the stone bridge soft behind.",
  plate("P2", LOC["P2"][1]), angle("B-04", "the strap in his palm"), focus("the strap and its wordmark"),
  light("open sky, the cloud broken, sun high on the left", "the strap and his hand", "left", "late-morning daylight", face=False),
  colour("clear daylight", 5600, "the canal's brown-green, the grey stone bridge", "he", "a navy fleece cuff", "the matte-black strap and its grey wordmark", "natural")],
  NEG_HELD + ", no face, no strap worn, no dog-bone shell, no bow-tie shell, no loose open strap, no small shell, no band hanging loose off the hand", scale="about half"))
add("MECH-02", "nano-banana-2", PR(FRONT, BACK), anat(
  "THE STATE: one tight hot red point glows on the patellar tendon just below the kneecap — " + P.ANAT_A_POINT_TIGHT + " The strap sits just below it on the shin, about to seat, not yet on the point.",
  prod=True, neg_extra=", no glow spreading onto the shin, no glow on the kneecap"))
add("B-06", "nano-banana-pro", PR(FRONT, "stryde_refs/worn_front.jpg") + [SHEET["R3"], LOC["P3"][0]], photo([
  "A snapshot from knee height at the foot of the stairs: he sits on the bottom stair, his right leg stretched out straight in front of him, the strap on his right knee, his face easing, a small relieved breath. " +
  HASSAN[0].upper() + HASSAN[1:] + ". He wears " + WARD["H-D2"] + ". " + WORN,
  plate("P3", LOC["P3"][1], LOC["P3"][2]), angle("B-06", "him on the bottom stair"), focus("the nearest eye of Hassan"),
  light("the front door's coloured-glass panel", "him", "right", "warm morning daylight, the after"),
  colour("warm morning daylight", 5600, "pale sage walls, the patterned stair carpet", "he", "maroon and charcoal", "the black strap on his knee", "natural, warm"), S("SKIN-B1")],
  NEG_WORN + ", no looking at the camera, " + NEG_HANDS))
add("B-07", "nano-banana-pro", PR(FRONT, "stryde_refs/worn_front.jpg") + [SHEET["R1"], LOC["P0"][0]], photo([
  "A snapshot from the foot of the stairs, caught mid-step: she is coming down her staircase forwards, her left foot on the step below, her right foot on the step above, a hand light on the white handrail, "
  "the strap on her right knee, easy. " + FOLAKE[0].upper() + FOLAKE[1:] + ". She wears " + WARD["F-D2"] + ". " + WORN,
  plate("P0", LOC["P0"][1], LOC["P0"][2]), angle("B-07", "her coming down the stairs"), focus("everything", deep=True),
  light("the front-door glass behind the camera and the landing window above", "her", "right", "soft bright morning daylight, the after"),
  colour("soft bright morning daylight", 5600, "magnolia walls, the deep red stair carpet, the white handrail", "she", "yellow, green and navy", "the black strap on her knee", "natural, warm"), S("SKIN-B1")],
  NEG_WORN + ", no walking stick, no looking at the camera, " + NEG_HANDS, scale="about three quarters"))
# v3 (Fix x2 "change/CHANG THE PRODUCT"): v1 profile and v2 full-length both kept the strap small, so the model drew a generic narrow band -> low and close, knees to chest, the shell large
NOT_BAND = ("It is NOT a narrow patella band, NOT a thin tube strap, NOT a sports strap: the shell is a WIDE moulded panel that covers the whole front of the knee from side to side, "
            "about as tall as the kneecap, its top edge rising into two pointed peaks either side of a notch that cups the kneecap, a chrome slide at each end, exactly like the attached worn photo.")
NEG_BAND = "no narrow knee band, no thin tube strap, no patella strap band, no strap narrower than the kneecap, no plain black band with a logo, no fabric knee wrap, no sleeve, no generic brace, no wordmark on the side of the leg"
add("B-08", "nano-banana-pro", PR("stryde_refs/worn_front.jpg", FRONT, "stryde_refs/product_tq_left.jpg") + [SHEET["R3"], LOC["P4"][0]], photo([
  "A close snapshot from a phone held low, at his knee height, a little in front of him and to one side: he stands at the kitchen sink filling the white kettle, framed from his knees up to his chest, "
  "the kettle and his hands at the tap at the top of the frame, his bare right knee large in the lower half of the frame with the strap on it, the front of its shell, its two peaks and notch "
  "and its grey wordmark facing the phone. " + HASSAN[0].upper() + HASSAN[1:] + ". He wears " + WARD["H-D2"] + ". " + WORN + " " + NOT_BAND,
  plate("P4", LOC["P4"][1], LOC["P4"][2]), angle("B-08", "him at the sink"), focus("the strap on his knee and its wordmark"),
  light("the window over the sink on the kitchen's far wall", "him", "left", "bright morning sun along the worktop"),
  colour("bright morning sun", 5600, "cream units, the dark speckled worktop, white tiles", "he", "maroon and charcoal", "the white kettle", "natural, warm")],
  NEG_WORN + ", " + NEG_BAND + ", no looking at the camera, no water splashing everywhere, " + NEG_HANDS, scale="about half"))
# v2 (Fix "make this woman using short, wrong wear of product"): v1 in trousers, seen in profile, drew the band being fastened -> shorts, three-quarter front, the strap a closed ring on the shin
add("B-09a", "nano-banana-pro", PR("stryde_refs/worn_front.jpg", FRONT) + [SHEET["R4"], LOC["P5"][0]], photo([
  "A close snapshot from knee height, a little to her right: she sits on the edge of her bed in shorts, her bare right leg straight out towards the phone, the knee large in frame. "
  "The strap is already on and closed — a CLOSED RING around her upper shin, a hand's width below the kneecap, the front of its shell, its peaks, notch and grey wordmark facing the phone, "
  "exactly like the attached worn photo but sitting lower on the shin — and both her hands rest flat on the two sides of the shell, about to slide it up to the kneecap. Nothing is being fastened. "
  + ELAINE[0].upper() + ELAINE[1:] + " — only her hands, forearms and legs in frame. She wears " + WARD["E-D3"] + ". " +
  PROD + " " + RIGID + " " + P.WORDMARK_LOCK + " " + P.LEG_SKIN + " " + NOT_BAND,
  plate("P5", LOC["P5"][1]), angle("B-09a", "her leg and hands"), focus("the strap and her hands"),
  light("the sash window on the bedroom's south wall", "her leg", "right", "bright morning daylight", face=False),
  colour("bright morning daylight", 5600, "dove-grey walls, the striped duvet, pine floorboards", "she", "navy-and-white stripes and olive shorts", "the black strap", "natural")],
  P.fill(P.NEG_SEAT, "right") + ", " + P.NEG_WORDMARK + ", " + P.NEG_OBSERVED + ", " + NEG_BAND + ", no trousers, no rolled trouser leg, no open band, no band ends in her hands, no strap on the knee yet, no face, " + NEG_HANDS, scale="about half"))
# v2 (Fix "wrong product"): v1 drew a dog-bone pad with no peaks -> the inside photo attached first and copied, the strap large and square to the phone
add("B-09b", "nano-banana-pro", PR("stryde_refs/back_inner.jpg", FRONT, BACK) + [SHEET["R4"], LOC["P5"][0]], photo([
  "A close snapshot looking down: sitting on the bed she holds the second strap up in both hands and has turned it round so the inside of the shell faces the phone square-on, the strap large in frame. "
  "The inside of the shell is EXACTLY as in the attached photo of the inside, copied shape for shape: the same outline as the front of the shell — two rounded pointed peaks either side of a wide shallow notch "
  "along the top edge, a chrome slide at each end — never a dog-bone or bow-tie outline; the band is a closed ring of black knit elastic looping away behind it. " + P.PAD_BACK_SHOT + " " + P.INNER_PAD +
  " Her hands are " + ELAINE + "'s hands: small, slim, fine-skinned, the striped cuffs at the wrists.",
  plate("P5", LOC["P5"][1]), angle("B-09b", "the strap in her hands"), focus("the pad inside the shell"),
  light("the sash window on the bedroom's south wall", "the strap and her hands", "right", "bright morning daylight", face=False),
  colour("bright morning daylight", 5600, "the striped duvet below", "she", "navy-and-white stripes", "the mid-grey pad", "natural")],
  P.NEG_INNER_PAD + ", " + P.NEG_HELD_P + ", no dog-bone outline, no bow-tie outline, no shell without peaks, no loose open strap, no face, " + NEG_HANDS, scale="about half"))
add("B-10", "nano-banana-pro", PR(FRONT, "stryde_refs/worn_bent.jpg") + [SHEET["R3"], LOC["P4"][0]], photo([
  "A snapshot caught mid-action from low down: he is crouched at the bottom kitchen cupboard, one hand on the open cupboard door, the other reaching in for a saucepan, his right knee deeply bent, "
  "the strap on it staying put, easy. " + HASSAN[0].upper() + HASSAN[1:] + ". He wears " + WARD["H-D2"] + ". " + WORN_BENT,
  plate("P4", LOC["P4"][1], LOC["P4"][2]), angle("B-10", "him crouching"), focus("everything", deep=True),
  light("the window over the sink on the kitchen's far wall", "him", "left", "bright morning sun along the worktop"),
  colour("bright morning sun", 5600, "cream units, chequered floor", "he", "maroon and charcoal", "the black strap on his knee", "natural, warm"), S("SKIN-B1")],
  P.fill(P.NEG_BENT, "right") + ", " + NEG_WORN + ", " + NEG_HANDS))
add("B-11a", "nano-banana-pro", PR(FRONT, "stryde_refs/worn_front.jpg") + [SHEET["R4"], LOC["P5"][0]], photo([
  "A close snapshot from low down beside the bed: she stands by the bed, the olive trouser still rolled above her right knee showing the strap worn on it, her fingers at the rolled cuff just letting it go. "
  "Only her leg from the thigh down, her hand and the edge of the bed in frame. " + WORN,
  plate("P5", LOC["P5"][1]), angle("B-11a", "her right leg"), focus("the strap and its wordmark"),
  light("the sash window on the bedroom's south wall", "her leg", "right", "bright morning daylight", face=False),
  colour("bright morning daylight", 5600, "dove-grey walls, pine floorboards", "she", "olive and white", "the black strap", "natural")],
  NEG_WORN + ", no face, " + NEG_HANDS, scale="about half"))
add("B-11b", "nano-banana-2", [SHEET["R4"]], photo([
  "A snapshot at a street-market fruit stall in Cardiff under a green-and-white striped awning, late morning: she stands at the stall choosing apples into a paper bag, weight easy on both legs, relaxed, "
  "not thinking about her knee. " + ELAINE[0].upper() + ELAINE[1:] + ". She wears " + WARD["E-D1"].replace(" rolled up above the right knee so the knee is bare", " rolled down to the ankle") +
  " and a yellow raincoat, open. In the near foreground, soft and out of focus, a crate of red apples.",
  angle("B-11b", "her", ", looking past a crate of apples, soft in the near foreground"), focus("the nearest eye of Elaine"),
  light("open sky over the market, the sun behind the camera's right", "her", "right", "bright late-morning daylight"),
  colour("bright daylight", 5600, "the green-and-white awning, crates of fruit", "she", "navy stripes, olive and yellow", "the red apples", "natural, lively"), S("SKIN-B1")],
  "no strap visible, no knee visible, no brace, no readable signs, no prices, no shop names, no looking at the camera, " + NEG_HANDS))
# v2 (Fix "FIX THE PRODUCT"): v1 medium shot kept the strap small -> generic narrow band; now tight on the knee, the shell large
add("B-12", "nano-banana-pro", PR("stryde_refs/worn_front.jpg", FRONT, "stryde_refs/product_tq_left.jpg") + [SHEET["R2"], LOC["P6"][0]], photo([
  "A close snapshot over the surgeon's shoulder, tight on the knee: Derek sits on the edge of the blue examination couch and his bare right knee fills the middle of the frame with the strap on it, "
  "the front of its shell, its two peaks and notch and its grey wordmark facing the phone; " + SG01 + " crouches in front of him, the side of his head and his shoulder soft in the near foreground at the left, "
  "and his two fingers tap the top edge of the shell. Derek's face is at the top of the frame, looking down, pleased. " + DEREK[0].upper() + DEREK[1:] + ". He wears " + WARD["D-D3"] + ". " + WORN + " " + NOT_BAND,
  plate("P6", LOC["P6"][1]), angle("B-12", "the surgeon, towards Derek's knee", ", looking past the surgeon's shoulder, soft in the near foreground"), focus("the strap on his knee and its wordmark"),
  light("the window on the consulting room's left-hand wall", "Derek", "left", "overcast morning daylight"),
  colour("overcast morning daylight", 6500, "pale grey-blue walls, the blue couch", "he", "blue-and-white stripes and stone", "the black strap", "cool, true to life")],
  NEG_WORN + ", " + NEG_BAND + ", no white coat, no stethoscope, no text, no chest X-ray, " + NEG_HANDS, scale="about half"))
add("B-13a", "nano-banana-pro", PR(FRONT, "stryde_refs/package_open.jpg") + [LOC["P1"][0]], photo([
  "A snapshot from directly above the glass-topped coffee table in Folake's lounge: the open box lies on the glass, " + P.PACKAGE_LOCK + " A hand — a Black woman's hand, slim, dark brown skin, "
  "short unpainted nails, a wax-print cuff at the wrist — settles the lid on the table beside it.",
  plate("P1", LOC["P1"][1], LOC["P1"][2]), angle("B-13a", "the open box"), focus("the two straps and their wordmarks"),
  light("the wide window on the lounge's east wall", "the box", "left", "bright morning daylight", face=False),
  colour("bright morning daylight", 5600, "the glass table on the cream rug", "she", "a yellow-and-green wax-print cuff", "the matte-black box", "natural, warm")],
  P.NEG_PACKAGE + ", " + P.NEG_WORDMARK + ", no face, " + NEG_HANDS, scale="about half"))
add("CARD-13b", "gpt-image-2-5-sunburst-image-to-image", PR(FRONT, "stryde_refs/product_tq_left.jpg"), "\n\n".join([
  "Product photograph, vertical 9:16. Two identical straps float side by side, slightly overlapping and angled towards each other, against a deep navy-black background with a soft top light and a faint "
  "cool rim on their edges, the lower third of the frame and the top quarter empty dark space for text added later.",
  PROD, RIGID, P.WORDMARK_LOCK, P.SIZE_OBJECT,
  "AVOID: " + ", ".join([P.NEG_WORDMARK, P.NEG_OBSERVED, "no text, no offer text, no price, no URL, no badge, no third strap, no single strap, no box, no hands, no people, no props, no reflections of text"])]))
add("B-14", "nano-banana-pro", PR(FRONT, "stryde_refs/worn_front.jpg") + [SHEET["R2"], LOC["P2"][0]], photo([
  "A snapshot from low down on the towpath, caught mid-stride: he walks towards the camera along the path, the stone bridge behind him, his left foot forward, arms swinging easy, the strap on his right knee, "
  "a small contented smile. " + DEREK[0].upper() + DEREK[1:] + ". He wears " + WARD["D-D2"] + ". " + WORN,
  plate("P2", LOC["P2"][1]), angle("B-14", "him walking"), focus("everything", deep=True),
  light("open sky, the cloud broken, sun high on the left", "him", "left", "bright late-morning sun, the after"),
  colour("clear daylight", 5600, "the green hedgerow, the canal, the stone bridge", "he", "navy and khaki", "the black strap on his knee", "natural, warm"), S("SKIN-B1")],
  NEG_WORN + ", no walking stick, no second person, no looking at the camera, " + NEG_HANDS, scale="about two thirds"))
if __name__ == "__main__":
    out = {}
    for beat, (model, refs, prompt) in BEATS.items():
        assert "[" not in prompt, (beat, prompt[prompt.index("["):][:100])
        (H / f"{beat}.t2i.txt").write_text(prompt + "\n")
        out[beat] = {"model": model, "refs": [str(pathlib.Path(r)) for r in refs], "chars": len(prompt), "line": ROWS[beat]["phrase"]}
        print(f"{beat:9s} {model:38s} {len(prompt):5d} refs {len(refs)}")
    (H / "body.json").write_text(json.dumps(out, indent=1))
    missing = [r for b in out.values() for r in b["refs"] if not (B / r).exists() and not pathlib.Path(r).exists()]
    print("missing refs:", missing)
