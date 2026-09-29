#!/usr/bin/env python3
"""Step 7 · Acts 2–5 frames (step-1 images) for down-forwards-again, from the act map (work/actmap.json) — the user, 2026-09-29:
"generate all the images so i can check all of them". Same rules as build_act1.py:
Lifestyle BR: §22T order (CAM-LOCK → ANGLE-LINE → FOCUS-LINE → PROP-REF/room → prose → LIGHT-SHOT → (SKIN-T → CAP-SHARP on MCU faces) → CAP-FILE → AVOID),
start frame caught in the action. Product beats: the Product Sheet strings (REF_PROD, PLACE_LOCK, SEAT_LOCK start, HELD_GRIPS, PACKAGE_LOCK, FAKE_BASE)
never retyped. MECH-14: §12A-1 ANAT-A, relief state. P-D1 = the problem days (Acts 1–2), P-D2 = the after (Act 3 on)."""
import re, json, pathlib, importlib.util
here = pathlib.Path(__file__).parent
hk = here.parent / "hooks" / "build_hooks.py"
src = hk.read_text()
import sys; sys.path.insert(0, str(here.parent / "work")); from wardrobe import wear, DAY  # wardrobe v2 (the user, 2026-09-29)
exec(compile(src[:src.index("\nB = {}")].replace("__file__", repr(str(hk))), str(hk), "exec"))
spec = importlib.util.spec_from_file_location("ps", ROOT / "products/stryde/stryde_product_sheet.py"); ps = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(ps)
except AssertionError: pass
def anat(i, drop=()):
    s = ps.fill(S(i), "left").replace("[TARGET JOINT]", "the knee joint")
    for k, v in {"[REGION]": "left knee", "[STACK]": ps.SLOTS["STACK"], "[BONES]": ps.SLOTS["BONES"], "[TARGET]": ps.SLOTS["TARGET"], "[SITE]": ps.SLOTS["SITE"]}.items():
        s = s.replace(k, v)
    for d in drop: s = s.replace(d, "").replace(", ,", ",")
    assert "[" not in s, (i, s[s.index("["):s.index("[") + 60]); return s
NEG_ANAT = lambda drop=(): ", ".join(c for c in (x.strip() for x in S("ANAT-NEG").split(",")) if c not in drop)
P_D1 = ("She wears a cream fine-knit roll-neck under an oatmeal cable-knit cardigan buttoned once, a knee-length plum wool skirt with bare legs, "
        "burgundy fleece-lined slippers, and reading glasses on a cord round her neck.")
P_D2 = ("Today she wears a white cotton shirt with the sleeves turned back, an open coral lightweight cardigan, wide-leg navy linen trousers, "
        "tan leather flat loafers and small gold hoop earrings.")
P_D2_ROLLED = P_D2.replace("wide-leg navy linen trousers", "wide-leg navy linen trousers rolled up in soft wide cuffs well above both knees")
SKIN = lambda f: [S("SKIN-T").replace("[AGE-FEATURES]", f), S("CAP-SHARP")]
WM = NOTEXT.replace("anywhere", "anywhere except the stryde wordmark on the strap")
PLACE = ps.fill(ps.PLACE_LOCK, "left"); PLACE_C = ps.fill(ps.PLACE_LOCK_C, "left"); NEG_PL = ps.fill(ps.NEG_PLACE, "left")
SIZE_W = ps.SIZE_WORN; FIT = ps.FIT_SNUG
GRIP = dict(ps.HELD_GRIPS)["bottom-edge pinch"].replace(" (HELD_EXAMPLE shows this one)", "")
PROD_NEG = ", ".join([ps.NEG_WORDMARK, "no second strap, no strap on the right knee"])
REF = {"P-PATIENT": "02333782-0c9a-4696-b3f1-fcc7480fe8db", "P0-PROP-P v2": "176c5c39-ac17-46c4-9e9b-2c06735dc0c8",
       "P1-P-FRONTROOM v2": "d0eeaf2a-abad-4a79-a9da-624c5eef41a1", "P2-P-KITCHEN v2": "abc2c220-b0f0-43d2-b583-d22b5696225b",
       "P3-D-CONSULT": "757817ea-6840-487c-879c-1b0310e137b2", "D-VOICE-IMG v2": "b17f293d-306f-406c-b145-029402a1c074",
       "front.webp": "c942d91d-718d-4723-b190-ad85186ac8d9", "product_tq_left.jpg": "4a56cffe-69bc-4f77-ac90-38258b124e65",
       "W-L-FRONT": "793ca329-e4b3-49fd-943c-5e97bae5366d", "W-L-BENT": "2730a819-cf08-49a6-b5cd-01a086777dad",
       "package_open": "a9409405-2d78-4802-bdf0-01c7266b18a1"}
NB2, NBP = "nano_banana_2", "nano_banana_pro"
B = {}
# ───────────── Act 2 · P-D1 (the problem days) ─────────────
B["BR-06"] = dict(model=NB2, refs=["P0-PROP-P v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  angle("high", "a three-quarter angle from behind", "the woman on the stairs"),
  focus("everything", "everything from near to far stays sharp"),
  PROPREF + " The hall and the wide straight staircase of the attached property photograph, seen from the landing looking down: the stairs fall away along the left-hand wall, the dark turned banister on the open right side, the patterned runner with brass rods, the hall floor far below.",
  "A snapshot from a phone held by someone standing on the landing at the top of the stairs, looking down, not looking at the screen. "
  "The woman of sixty-nine from the attached reference sheet — chestnut-dyed chin-length hair with silver roots — " + wear("BR-06", "wearing ").rstrip(".") +
  ". She is coming DOWN her stairs BACKWARDS, facing the steps, three steps below the landing, both hands gripping the banister rail, "
  "caught in the moment her LEFT foot reaches back and down for the tread below, toes feeling for it, her weight hanging on her arms, head bowed to watch her feet. "
  "We see her back and the side of her face, turned down to the steps. Her whole body from hair to feet is in frame, the rest of the stairs dropping away below her.",
  light("The tall landing window beside the phone", "her", "right", "a grey morning, the problem days, flat and cool", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no facing forwards, no face towards the camera, no smiling, no falling, no stick, no second person, no strap product, no brace, no feet cut off", NOTEXT])])
B["BR-07"] = dict(model=NB2, refs=["P1-P-FRONTROOM v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  angle("eye", "the side, in profile", "the woman in the armchair"),
  focus("the nearest eye of the woman", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The front room of the attached front-room photograph: the low mustard fireside armchair with dark wooden arms, the bay window with net curtains behind.",
  "A snapshot from a phone held at eye height by someone sitting on the sofa beside her, not looking at the screen. " + P_FACE + " " + wear("BR-07") +
  " She sits deep in the low mustard armchair and is trying to stand: both hands pushing down on the chair's wooden arms, elbows locked, her body rocked forward "
  "over her knees, her bottom just lifted a finger's width off the seat cushion, caught at the top of the first try before she sinks back — jaw set, lips pressed, "
  "breath held, eyes on the floor ahead of her. Her whole body from head to feet is in frame, side-on.",
  light("The bay window on the room's east wall", "her", "left", "grey even daylight through the net curtains, the problem days", "the left"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no standing up already, no smiling, no second person helping, no stick, no strap product, no brace, no feet cut off", NOTEXT])])
B["BR-08"] = dict(model=NB2, refs=["P0-PROP-P v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  angle("low", "a three-quarter angle", "her legs at the bottom stair").replace("the lens at hip height, looking up at the subject", "the lens a hand's width off the floor, looking along the bottom stair"),
  focus("everything", "everything from near to far stays sharp"),
  PROPREF + " The foot of the wide staircase in the attached property photograph: the bottom tread with its patterned runner and brass rod, the hall floorboards, the newel post.",
  "A snapshot from a phone resting on the hall floor at the foot of the stairs, not looking at the screen. Only her legs from the knees down: an older woman's bare legs "
  "below the hem of a knee-length faded denim skirt, red tartan slippers. She is stepping up onto the bottom stair, caught mid-step: her RIGHT foot planted flat on the "
  "bottom tread taking the weight, the RIGHT knee bent and working, her LEFT foot still on the hall floor behind, heel lifted, the LEFT leg trailing straight and careful. "
  "Pale skin, faint thread veins, a little swelling round the left knee.",
  light("The stained-glass panel in the front door, behind the phone", "her legs", "right", "a grey morning, a pale wash along the runner", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face, no left foot leading, no stick, no strap product, no brace, no second person, no feet cut off", NOTEXT])])
B["BR-09a"] = dict(model=NB2, refs=["P0-PROP-P v2"], body=[S("CAM-LOCK"),
  angle("low", "the front", "the walking boots by the door"),
  focus("the foreground", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The hall of the attached property photograph, by the front door, the burgundy-and-cream runner and the skirting soft behind.",
  "A snapshot from a phone held low by someone crouching in the hall, not looking at the screen. On a folded sheet of old newspaper on the hall floorboards beside the "
  "front door: a pair of women's brown leather walking boots, laces loose and dusty, dried pale mud on the soles and a little flaked off onto the paper, the leather creased "
  "and dulled, a fine film of dust on the toe caps — boots that have waited a long time. A wooden walking pole leans in the corner behind them, soft.",
  light("The stained-glass panel in the front door", "the boots", "left", "a grey morning, the problem days", "the left", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no person, no feet in the boots, no new shiny boots, no readable headlines on the newspaper", NOTEXT])])
B["BR-09b"] = dict(model=NB2, refs=["P2-P-KITCHEN v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  angle("eye", "a three-quarter angle from behind", "the woman at the sink"),
  focus("the garden beyond the window", "the woman in the foreground stays readable, a touch soft"),
  PROPREF + " The kitchen of the attached kitchen photograph: the window over the sink on the west wall, looking out on the back garden.",
  "A snapshot from a phone held at eye height by someone standing in the kitchen behind her, not looking at the screen. The woman of sixty-nine from the attached reference "
  "sheet — chestnut-dyed chin-length hair with silver roots — " + wear("BR-09b", "wearing ").rstrip(".") +
  ", stands at the sink with a mug of tea in her hand, seen from behind and a little to one side, her head just lifting to look out of the window. "
  "Through the glass, sharp: an overgrown back garden — long uncut grass, a rose bed choked with weeds, an empty bird table, a wooden bench gone green, "
  "a garden fork left leaning against the fence.",
  light("The window over the sink on the room's west wall", "her", "back", "flat overcast daylight, the problem days", "the window", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face towards the camera, no smiling, no sunny garden, no neat garden, no second person, no strap product, no brace", NOTEXT])])
B["BR-09c"] = dict(model=NB2, refs=["P0-PROP-P v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  angle("eye", "over her shoulder", "the family on the doorstep", ", looking past her shoulder, soft in the near foreground"),
  focus("the daughter's nearest eye", "the street behind falls to a soft, recognisable shape"),
  PROPREF + " The hall of the attached property photograph at the open front door, the stained-glass panel in the door, a red-brick front path and a grey street beyond.",
  "A snapshot from a phone held at eye height by someone standing in the hall just behind her, not looking at the screen. In the near foreground, soft: the back of "
  "the woman of sixty-nine from the attached reference sheet, chestnut-dyed hair with silver roots, a bottle-green roll-neck collar under a long charcoal draped cardigan, one hand on the edge of the front "
  "door she has just pulled open. On the doorstep, sharp: her daughter, a white British woman in her forties with shoulder-length light brown hair, in a navy rain jacket, "
  "holding a supermarket bag of shopping, a warm tired smile; beside her, her son of eight in a maroon school jumper, looking up at his grandmother. "
  "They have come to her. Nobody steps over the threshold.",
  light("The open front door, the grey street beyond", "the family", "left", "a grey morning, soft light on their faces", "the left"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no hugging, no stepping inside, no third visitor, no dog, no strap product, no brace", NOTEXT])])
B["BR-10"] = dict(model=NB2, refs=["P1-P-FRONTROOM v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  angle("high", "a three-quarter angle", "the woman in the armchair"),
  focus("the hands and what they hold", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The front room of the attached front-room photograph: the mustard fireside armchair, the patterned rug.",
  "A snapshot from a phone held above her by someone standing beside the armchair, looking down, not looking at the screen. The woman of sixty-nine from the attached "
  "reference sheet sits in the mustard armchair, " + wear("BR-10", "wearing ").rstrip(".") +
  ", her LEFT leg lifted out straight in front of her, a plain green rubber physio resistance band looped round the sole of her trainer, both hands pulling "
  "its two ends back towards her chest, caught mid-pull, the band stretched taut, her knuckles pale with effort. Her face is at the top edge of the frame, "
  "turned down, soft. A printed exercise sheet with small stick-figure drawings and no readable words lies on the arm of the chair.",
  light("The bay window on the room's east wall", "her hands and the band", "left", "grey even daylight through the net curtains, the problem days", "the left", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no gym, no physiotherapist, no second person, no smiling, no strap product, no brace, no band snapping, no logo on the band", NOTEXT])])
# ───────────── Act 3 · P-D2 (the after) ─────────────
B["BR-11a"] = dict(model=NB2, refs=["P2-P-KITCHEN v2"], body=[S("CAM-LOCK"),
  angle("eye", "the front", "the knee sleeve in a hand"),
  focus("the hands and what they hold", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The kitchen of the attached kitchen photograph, the pine table and the dresser soft behind, brighter today.",
  "A snapshot from a phone held at eye height by someone across the table, not looking at the screen. An older woman's hand — thin skin, a plain gold wedding band, "
  "the rolled cuff of a cornflower-blue linen shirt — holds up a plain black stretchy knee sleeve, a tube of thick neoprene knit with an open hole at the kneecap, "
  "caught in the middle of one squeeze: her fingers crushing it flat so it bunches and folds in her fist. No brand, no writing, no logo on it.",
  light("The window over the sink on the room's west wall", "the hand and the sleeve", "right", "brighter daylight, still indirect, the after", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face, no strap product, no hinged brace, no logo or label on the sleeve", NOTEXT])])
B["BR-11b"] = dict(model=NB2, refs=["P2-P-KITCHEN v2"], body=[S("CAM-LOCK"),
  angle("low", "the side, in profile", "the hinged brace on the table"),
  focus("the foreground", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The kitchen of the attached kitchen photograph: the bare pine table top, the dresser soft behind.",
  "A snapshot from a phone resting low on the edge of the pine table, not looking at the screen. Lying on the table: a bulky grey hinged knee brace — grey foam-lined "
  "fabric cuffs above and below, two metal side bars with a round metal hinge at the knee on each side, black velcro straps hanging loose. An older woman's hand "
  "— a plain gold wedding band, the rolled cuff of a cornflower-blue linen shirt — holds the upper cuff, caught tilting the lower half sideways so the hinge swings open at an angle. "
  "No brand, no writing, no logo anywhere on it.",
  light("The window over the sink on the room's west wall", "the brace", "right", "brighter daylight, still indirect, the after", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face, no leg in the brace, no strap product, no logo or label on the brace", NOTEXT])])
B["BR-11c"] = dict(model=NB2, refs=["P2-P-KITCHEN v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  angle("high", "a three-quarter angle", "her knee and her hand"),
  focus("the hands and what they hold", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The kitchen of the attached kitchen photograph, the terracotta-and-black tiled floor soft below.",
  "A snapshot from a phone held above her lap by someone looking down, not looking at the screen. She sits on a spindle-back kitchen chair, her wide-leg cream cotton "
  "trouser leg rolled up above her LEFT knee, the bare knee in the middle of the frame: pale skin, fine creases, faint thread veins. Her right hand — a plain gold "
  "wedding band, the rolled cuff of a cornflower-blue linen shirt — is caught in the middle of one slow rub, spreading a smear of white gel across the front of the knee, "
  "the gel glistening on the skin. A small plain white tube with no label lies on the table edge beside her, its cap off.",
  light("The window over the sink on the room's west wall", "her knee and hand", "right", "brighter daylight, still indirect, the after", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face, no strap product, no brace, no label or brand on the tube", NOTEXT])])
B["PR-12"] = dict(model=NBP, refs=["front.webp", "product_tq_left.jpg", "P2-P-KITCHEN v2"], body=[S("CAM-LOCK"),
  angle("eye", "the front", "the strap held up in her hand"),
  focus("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The kitchen of the attached kitchen photograph, the window over the sink bright behind, the pine dresser soft.",
  "A snapshot from a phone held at eye height by someone standing across from her, not looking at the screen. An older woman's hand — thin skin, a plain gold wedding "
  "band, the rolled cuff of a cornflower-blue linen shirt — holds her knee strap up into the window light, sharp and filling the middle of the "
  "frame, its front face square to the lens. " + ps.REF_PROD + " held by the " + GRIP + ". " + ps.SIZE_HELD,
  light("The window over the sink on the room's west wall", "the strap and her hand", "right", "brighter daylight, the after, the chrome slides catching it", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([ps.NEG_HELD_P, PROD_NEG, *NEG_BASE(), "no face, no packaging, no strap on a leg", WM])])
B["BR-13"] = dict(model=NBP, refs=["front.webp", "W-L-FRONT", "P-PATIENT", "P1-P-FRONTROOM v2"], body=[S("CAM-LOCK"),
  angle("eye", "a three-quarter angle", "her left knee"),
  focus("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The front room of the attached front-room photograph, the mustard armchair and the bay window soft behind, sun through the nets.",
  "A snapshot from a phone held at knee height by someone crouched beside her, not looking at the screen. The woman of sixty-nine from the attached reference sheet "
  "sits on the front edge of the mustard armchair, " + wear("BR-13", "wearing ").rstrip(".") +
  ", the skirt resting just above her knees as she sits, her LEFT leg out straight in front of her, heel on the rug, the bare knee filling the middle of the frame, still, resting. " + ps.REF_PROD + " " + PLACE + " " +
  SIZE_W + " " + FIT + " " + ps.LEG_SKIN + " Her hands rest on her thigh above the knee, not touching the strap. Her RIGHT leg is bare with nothing on it.",
  light("The bay window on the room's east wall", "her knee and the strap", "left", "bright morning sun through the net curtains, the after", "the left", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([NEG_PL, ps.NEG_WORDMARK, *NEG_BASE(), "no hands on the strap, no face, no trousers, no tights", WM])])
B["MECH-14"] = dict(model=NB2, refs=[], body=[anat("ANAT-BASE").replace("A stylised anatomical model of a single knee", "A stylised anatomical model of a single left knee mid-step, bent and taking the weight,"),
  anat("ANAT-A"), anat("ANAT-LIGHT"), anat("ANAT-FIELD"),
  "Around the leg, directly below the kneecap, sits a slim matte-black strap drawn as a smooth dark translucent band, its inner silicone pad pressing on the patellar "
  "tendon only — one band as wide as a thumb, just under the kneecap, never crossing the joint. STATE — RELIEF: under the pad the tendon glows a calm cool blue, "
  "the last trace of red fading at its edges, the load visibly caught and carried round the joint; the joint itself stays calm and uncoloured.",
  "AVOID: " + NEG_ANAT(("no arrows", "no force arrows", "no motion lines", "no vector lines", "no highlighted hotspots", "no rigid brace", "no sleeve", "no second unit"))
  + ", no brace covering the joint, no sleeve over the whole knee, no second strap, no strap above the kneecap"])
B["BR-15"] = dict(model=NB2, refs=["P3-D-CONSULT", "D-VOICE-IMG v2"], body=[S("CAM-LOCK"),
  angle("high", "a three-quarter angle", "his hand on the knee model"),
  focus("the hands and what they hold", "the room behind falls to a soft, recognisable shape"),
  "IN THE SAME ROOM as the attached consulting-room photograph, on his desk, the window soft behind.",
  "A snapshot from a phone held above the desk by someone standing beside him, looking down, not looking at the screen. On the desk stands a plain anatomical knee "
  "model on a small stand — ivory plastic femur, kneecap and shin bone, with a pale tendon strap running from the lower edge of the kneecap to the top of the shin. "
  "The doctor's hand — a stocky man's hand of fifty-four, fair freckled skin, a plain steel watch, the white cuff of his doctor's coat over a pale blue shirt cuff — "
  "is caught with his forefinger set on that tendon just under the kneecap, pointing at the one spot. His face is out of frame.",
  light("The consulting-room window, camera-left", "his hand and the model", "left", "steady overcast daylight", "the left", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face, no finger on the kneecap itself, no strap product, no labels or numbers on the model", NOTEXT])])
# ───────────── Act 4 ─────────────
B["BR-16a"] = dict(model=NBP, refs=["front.webp", "product_tq_left.jpg"], body=[S("CAM-LOCK"),
  angle("eye", "a three-quarter angle", "the surgeon"),
  focus("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
  "An orthopaedic clinic room: pale walls, a side window, an anatomical knee model on a small stand on the desk, a framed certificate soft on the wall.",
  "A snapshot from a phone held at eye height by a colleague across the desk, not looking at the screen. An orthopaedic surgeon, a friendly white British man of about "
  "sixty with short grey hair and rimless glasses, in navy scrubs, sits at the desk beside the knee model and holds a knee strap up at chest height between them, looking at "
  "it with a small approving nod, mouth closed. " + ps.REF_PROD + " held by the " + GRIP + ". " + ps.SIZE_HELD,
  light("The side window of the clinic room", "him and the strap", "right", "neutral daylight", "the right"),
  *SKIN("sun spots and faint crow's feet"), S("CAP-FILE"),
  "AVOID: " + ", ".join([ps.NEG_HELD_P, PROD_NEG, *NEG_BASE(), "no strap on a leg, no packaging, no speaking, no white coat", WM])])
B["BR-16b"] = dict(model=NBP, refs=["front.webp", "W-L-FRONT"], body=[S("CAM-LOCK"),
  angle("low", "the side, in profile", "the walkers' legs").replace("the lens at hip height, looking up at the subject", "the lens a hand's width off the path, looking along it"),
  focus("everything", "everything from near to far stays sharp"),
  "A canal towpath on a bright morning: packed gravel path, a low brick edge, the still green water of the canal and a moored narrowboat soft beyond.",
  "A snapshot from a phone resting on the ground at the edge of the towpath, not looking at the screen. Across the frame from left to right, a line of four older walkers' "
  "legs from the thighs down, mid-stride, in outdoor shorts with bare knees, walking boots and trail shoes, one pair of walking poles. On the nearer knee of each walker, "
  "sitting on the patellar tendon directly below the kneecap: the same knee strap. " + ps.REF_PROD + " Each one sits under its kneecap with the notch cupping the kneecap's "
  "lower border and the shell spanning the front of the knee, the band running round behind the leg. Varied legs: tanned, pale, hairy, freckled.",
  light("The open sky", "the legs", "left", "bright neutral daylight", "the left", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([ps.NEG_WORDMARK, *NEG_BASE(), "no faces, no strap on the kneecap, no strap on the thigh, no sleeves, no braces, no crowd, no running", WM])])
SEAT_START = ". ".join(ps.fill(ps.SEAT_LOCK, "left").split(". ")[:2]).split(" and slide the whole strap")[0].rstrip(", ") + ". "
B["BR-17a"] = dict(model=NBP, refs=["front.webp", "W-L-FRONT", "P-PATIENT", "P0-PROP-P v2"], body=[S("CAM-LOCK"),
  angle("high", "a three-quarter angle", "her left leg and the strap"),
  focus("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The foot of the wide staircase in the attached property photograph, sun through the front-door glass laying a warm patch on the runner.",
  "A snapshot from a phone held above her by someone standing in the hall, looking down, not looking at the screen. The woman of sixty-nine from the attached reference "
  "sheet sits on the bottom stair, " + wear("BR-17a", "wearing ").rstrip(".") +
  ", the LEFT trouser leg rolled up in a wide cuff above the knee, her LEFT leg stretched out in front of her, heel on the hall floor, the bare shin and knee clear. She is putting her knee strap on. " + ps.REF_PROD + " " + SEAT_START +
  "This is the first moment, before it moves: the strap still sits at mid-shin, well below the knee, both hands flat on its two sides, the kneecap bare above it, "
  "the notch pointing up at the kneecap, the wordmark upright and readable to the camera. Her face at the top of the frame looks down at her knee, calm, mouth shut. "
  "Her RIGHT leg stays covered by its denim trouser leg, nothing on it.",
  light("The stained-glass panel in the front door", "her leg and the strap", "right", "morning sun through the door glass, the after", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([ps.NEG_ADJUST, *NEG_BASE(), "no strap already under the kneecap, no strap on the right leg, no two straps, no strap on the kneecap, no strap on the thigh, no skirt", WM])])
B["BR-17b"] = dict(model=NBP, refs=["front.webp", "W-L-FRONT", "P0-PROP-P v2"], body=[S("CAM-LOCK"),
  angle("low", "a three-quarter angle", "her left knee"),
  focus("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The hall of the attached property photograph at the foot of the stairs, the runner and the skirting soft behind, morning sun on the floorboards.",
  "A snapshot from a phone held low by someone crouched in the hall, not looking at the screen. Her legs from the hips down: she has just stood up from the bottom stair, "
  "white leather trainers on the floorboards. The wide-leg mid-blue denim trouser on her LEFT leg is still rolled up in a soft wide cuff above the knee, and her left hand is "
  "caught at the cuff, fingers on the fabric, just about to let it fall. Below the cuff the knee strap is on. " + ps.REF_PROD + " " + PLACE + " " + SIZE_W + " " + ps.LEG_SKIN +
  " Her RIGHT trouser leg already hangs straight to the ankle.",
  light("The stained-glass panel in the front door", "her knee and the strap", "right", "morning sun through the door glass, the after", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([NEG_PL, ps.NEG_WORDMARK, *NEG_BASE(), "no face, no hand touching the strap, no skirt", WM])])
B["BR-19a"] = dict(model=NBP, refs=["front.webp", "W-L-FRONT", "P-PATIENT", "P0-PROP-P v2"], body=[S("CAM-LOCK"),
  angle("high", "the front", "the woman on the landing"),
  focus("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The top of the wide staircase in the attached property photograph: the landing, the tall landing window, the banister turning at the top.",
  "A snapshot from a phone held above her by someone standing a few steps up the next flight, looking down, not looking at the screen. " + P_FACE + " " + wear("BR-19a") +
  " She stands still on the landing at the top of the stairs, facing the camera, both feet flat, one hand resting lightly on the banister post, the stairs dropping "
  "away below and behind her. Her face is calm and ready, a breath before she goes. On her LEFT knee: " + ps.REF_PROD + " " + PLACE + " " + SIZE_W +
  " Her RIGHT knee is bare, nothing on it — one knee only. Her whole body from hair to plimsolls is in frame.",
  light("The tall landing window", "her", "right", "morning sun, the after", "the right"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([NEG_PL, ps.NEG_WORDMARK, *NEG_BASE(), "no strap on the right knee, no two straps, no trousers, no stepping, no feet cut off", WM])])
B["BR-19b"] = dict(model=NBP, refs=["front.webp", "W-L-FRONT", "P-PATIENT", "P0-PROP-P v2"], body=[S("CAM-LOCK"),
  angle("low", "the front", "the woman coming down the stairs"),
  focus("everything", "everything from near to far stays sharp"),
  PROPREF + " The hall and the wide straight staircase of the attached property photograph, the dark turned banister on the open right side, the patterned runner with brass rods.",
  "A snapshot from a phone held at hip height by someone standing at the foot of the stairs, not looking at the screen. " + P_FACE + " " + wear("BR-19b") +
  " She is coming DOWN her stairs facing forwards, five steps from the bottom, easy and steady, one hand resting light on the banister, caught in the moment her LEFT "
  "foot lands on the tread below with the LEFT knee bending freely under her weight, her right foot still on the step above. Her face is open and quietly surprised, "
  "eyes on the stairs ahead, mouth shut. On her LEFT knee the strap sits under the kneecap: " + ps.REF_PROD + " " + PLACE_C + " Her RIGHT knee is bare. "
  "Her whole body from hair to plimsolls is in frame.",
  light("The stained-glass panel in the front door, behind the phone", "her", "right", "morning sun, a warm patch on the stairs, the after", "the right"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([NEG_PL, ps.NEG_WORDMARK, *NEG_BASE(), "no walking backwards, no gripping the rail, no strap on the right knee, no trousers, no fall, no second person, no feet cut off", WM])])
B["BR-20"] = dict(model=NB2, refs=["P3-D-CONSULT", "D-VOICE-IMG v2"], body=[S("CAM-LOCK"),
  angle("eye", "a three-quarter angle from behind", "the doctor at the window", ", looking past his shoulder, soft in the near foreground"),
  focus("the two X-ray films", "the room behind falls to a soft, recognisable shape"),
  "IN THE SAME ROOM as the attached consulting-room photograph, at its tall window, white vertical blinds open, grey daylight outside.",
  "A snapshot from a phone held at eye height by someone standing just behind him, not looking at the screen. " + D_FACE + " " + D_WARD +
  " He stands at the window seen from behind his right shoulder, the side of his face just in view, and holds up two grey-and-black knee X-ray films side by side against "
  "the glass, one in each hand, the daylight coming through them: the same left knee twice, the same narrowed joint gap on the inner side, identical. "
  "He looks from one to the other, still, mouth shut.",
  light("The consulting-room window, behind the films", "the films and him", "back", "steady overcast daylight coming through the films", "the window"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no lightbox, no glowing screen, no different scans, no X-ray of a hand or chest, no writing, names, dates or labels on the films", NOTEXT])])
# ───────────── Act 5 ─────────────
B["PR-22a"] = dict(model="gpt_image_2_5", refs=["package_open", "front.webp", "P2-P-KITCHEN v2"], body=[S("CAM-LOCK"),
  angle("high", "straight overhead", "the open box on the table").replace("the lens above head height, looking down at the subject", "the lens straight above the table, looking down"),
  focus("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The pine farmhouse table of the attached kitchen photograph, seen from straight above.",
  "A snapshot from a phone held flat above the kitchen table, not looking at the screen. On the bare pine table top: the open box, its lid set down beside it, "
  "wordmark up. " + ps.PACKAGE_LOCK + " An older woman's hand — a plain gold wedding band, the cuff of a lilac cotton shirt — rests at the edge of the frame on the lid.",
  light("The window over the sink on the room's west wall", "the box", "right", "brighter daylight, still indirect, the after", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([ps.NEG_PACKAGE, ps.NEG_WORDMARK, *NEG_BASE(), "no face, " + ps.NEG_RING])])
B["BR-22b"] = dict(model=NBP, refs=["P2-P-KITCHEN v2"], body=[S("CAM-LOCK"),
  angle("low", "the side, in profile", "a leg with a cheap copy strap"),
  focus("the foreground", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The kitchen of the attached kitchen photograph, the terracotta-and-black tiled floor and the table legs soft behind.",
  "A snapshot from a phone held low by someone crouched on the kitchen floor, not looking at the screen. An adult's bare lower leg from the knee down, standing, a grey "
  "sock and a trainer. On it: " + ps.FAKE_BASE + " The copy has stretched and slipped: it has sagged down off the kneecap to the middle of the shin, the band loose and "
  "baggy round the calf, one end twisted, gapping away from the skin.",
  light("The window over the sink on the room's west wall", "the leg", "right", "brighter daylight, still indirect", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([ps.NEG_FAKE_HERO, *NEG_BASE(), "no face, no genuine strap, no chrome, no wordmark, no logo anywhere", NOTEXT])])
B["BR-23"] = dict(model=NBP, refs=["front.webp", "W-L-FRONT", "P-PATIENT", "P0-PROP-P v2"], body=[S("CAM-LOCK"),
  angle("low", "a three-quarter angle", "the woman coming down the stairs"),
  focus("everything", "everything from near to far stays sharp"),
  PROPREF + " The hall and the wide straight staircase of the attached property photograph, the dark turned banister on the open right side, the patterned runner with brass rods.",
  "A snapshot from a phone held at hip height by someone standing at the foot of the stairs, off to one side, not looking at the screen. " + P_FACE + " " + wear("BR-23") +
  " She is coming DOWN her stairs facing forwards, four steps from the bottom, light and easy, both hands free at her sides and not holding the rail, her hand near "
  "the banister but not on it, caught in the moment her LEFT foot lands on the tread below with the LEFT knee bending freely, a small private smile. On her LEFT knee: "
  + ps.REF_PROD + " " + PLACE_C + " Her RIGHT knee is bare. Her whole body from hair to sandals is in frame.",
  light("The stained-glass panel in the front door, behind the phone", "her", "right", "morning sun, a warm patch on the stairs, the after", "the right"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([NEG_PL, ps.NEG_WORDMARK, *NEG_BASE(), "no hand on the rail, no walking backwards, no strap on the right knee, no trousers, no fall, no second person, no feet cut off", WM])])
out = {}
for k, b in B.items():
    txt = "\n\n".join(b["body"]); assert "[" not in txt, (k, txt[txt.index("["):txt.index("[") + 80])
    out[k] = dict(model=b["model"], refs=b["refs"], ref_jobs=[REF[r] for r in b["refs"]], chars=len(txt), prompt=txt)
    (here / (f"{k}.image.v2.prompt.txt" if k in DAY else f"{k}.image.prompt.txt")).write_text(txt); print(f"{k:8s} {len(txt):5d}  {b['model']:15s} refs: {', '.join(b['refs']) or '—'}")
json.dump(out, open(here / "acts2_5_v2.json", "w"), indent=1)
def params(v):
    p = {"model": v["model"], "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
         "medias": [{"role": "image_references", "value": j} for j in v["ref_jobs"]], "prompt": v["prompt"]}
    if v["model"] == "gpt_image_2_5": p.update(variant="sunburst", quality="high")
    return p
json.dump([{"index": i, "beat": k, "params": params(v)} for i, (k, v) in enumerate(out.items())], open(here / "acts2_5_v2_batch.json", "w"), indent=1)
