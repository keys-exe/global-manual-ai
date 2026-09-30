#!/usr/bin/env python3
"""Step 7 · image Fix round 11 (the user, 2026-09-30 ~10:45 UTC: "fix those and generate the next videos"; board Fix notes). One render each, to the
board To check; each beat's video waits for the user's Confirm of its image (Manual).
  BR-06 v6   image "fix this distorted image" → side-on from the hall: one plain straight flight, her mid-flight facing the steps, both hands on the rail.
  BR-10b v2  video "this feels lke floating" → the leg was held up in the air; now the heel rests on a low footstool, the leg supported and straight.
  BR-10c v2  video "make this anatomy" → ANAT render: the foot lands a step down, the load runs down the thigh and lands on the patellar tendon.
  BR-14b v3  video "use anatomy here" → ANAT render with the strap on: the load comes down, meets the pad over the tendon and is turned off into the shell.
  BR-16a v4 + BR-16a2 v1  video "this should be 2 brolls make an over all new ones" → "Measured." a gait lab: a volunteer wearing the strap steps down
             onto a force plate · "Three years with orthopedic surgeons." a surgeon fits the strap on a patient's knee on the couch, a second watches.
  BR-16b v2  video "i need new image here" → a walking group coming towards us along a park path, the slim strap on several knees.
  BR-17b v3  video "new image productive broll but with the pants down not showing the strap" → out at the greengrocer's, trouser legs down.
  BR-20 v2 + BR-20b v1 + BR-20c v1  video "i want new images here this should be 3 brolls" → her X-ray with his fingertip on the narrowed joint gap ·
             the two identical films side by side on his desk · ANAT render with the strap: the step lands and the tendon stays cool.
Act map + wardrobe updated first (work/actmap.py, work/wardrobe.py; angles.py PASS). Bases asserted; paragraph swaps."""
import json, pathlib, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here.parent / "work")); from wardrobe import wear
def rep(t, pairs):
    for o, n in pairs:
        assert t.count(o) == 1, o[:80]; t = t.replace(o, n)
    return t
def paras(f):
    P = (here / f).read_text().split("\n\n")
    assert P[0].startswith("Shot on an iPhone") and P[1].startswith("THE CAMERA ANGLE") and P[4].startswith(("A snapshot", "EDIT")) and P[7].startswith("AVOID"), f
    return P
PH0, FILEP = paras("BR-10b.image.r9.prompt.txt")[0], paras("BR-10b.image.r9.prompt.txt")[6]
BASE_AVOID = ("AVOID: no AI face, no plastic skin, no extra fingers, no fused fingers, no melted hands, no CGI look, no fake commercial gloss, no moody dark "
              "grade, no glowing skin, no shadows falling in two directions, no lens flare, ")
TXT = "no readable text, logos, brand names or labels anywhere"
TXT_P = "no readable text, logos, brand names or labels anywhere except the stryde wordmark on the strap"
PNEGI = ("no blank shell, no missing wordmark, no misspelled wordmark, no wordmark on the band, no strap on the kneecap, no strap on the thigh, no sleeves, "
         "no braces, no oversized strap, no chunky strap, no strap taller than the kneecap, ")
PROD = [p for p in (here / "BR-16b.image.prompt.txt").read_text().split("\n\n") if p.startswith("A snapshot")][0]
PROD = PROD[PROD.index("The product exactly as in the attached reference image"):PROD.index("never to one side of the notch —") + len("never to one side of the notch —")]
SLIM = (" On the leg it is a small, slim strap: the shell is only about three centimetres tall — shorter than the kneecap — and hugs the front of the knee "
        "just below it; the band is a narrow strip round the leg. It looks light and discreet, never chunky, never a big block on the knee.")
HOUSE = paras("BR-10b.image.r9.prompt.txt")[3].split(" The front room")[0]
PATIENT = ("THE SAME WOMAN exactly as in the attached reference sheet — a white British woman of sixty-nine, short and petite with a slight stoop, a small "
           "fine-boned oval face, pale grey-blue eyes, a small straight nose, a thin upper lip with a small mole above its right corner, chin-length layered "
           "hair dyed chestnut brown with silver roots at the parting, tucked behind the ears — unchanged in face, age and build; only her clothes are different today.")
DOCTOR = [p for p in (here / "BR-20.image.prompt.txt").read_text().split("\n\n") if p.startswith("A snapshot")][0]
DOCTOR = DOCTOR[DOCTOR.index("THE SAME MAN"):DOCTOR.index(" He stands at the window")]
def img(angle, focus, place, snap, light, avoid):
    return "\n\n".join([PH0, "THE CAMERA ANGLE: " + angle + " This exact angle, not a straight-on eye-level view.",
                        "FOCUS: " + focus + " The blur is optical: soft and round, never smeared.", place, snap, "THE LIGHT: " + light +
                        " The shadows fall away from that source, one way only.", FILEP, BASE_AVOID + avoid])
R = dict(P="02333782-0c9a-4696-b3f1-fcc7480fe8db", P0="176c5c39-ac17-46c4-9e9b-2c06735dc0c8", P1="d0eeaf2a-abad-4a79-a9da-624c5eef41a1",
         FRONT="c942d91d-718d-4723-b190-ad85186ac8d9", TQ="4a56cffe-69bc-4f77-ac90-38258b124e65", WORN="793ca329-e4b3-49fd-943c-5e97bae5366d",
         P3="757817ea-6840-487c-879c-1b0310e137b2", D="b17f293d-306f-406c-b145-029402a1c074")
OUT = {}
# ---- BR-06 v6 ---------------------------------------------------------------------------------------------------------------
OUT["BR-06"] = dict(v=6, refs=[R["P0"], R["P"]], prompt=img(
  "the lens at the subject's chest height, level, seen side-on, in profile, of the woman on the stairs, from across the hall.",
  "everything is in sharp focus; everything from near to far stays sharp.",
  HOUSE + " The hall and the ONE straight flight of stairs of the attached property photograph, seen side-on from across the hall: the flight rises as one "
  "plain straight diagonal from the hall floor at the right of the frame up to the landing at the top left, the patterned runner with brass rods on every "
  "tread, the dark turned banister rail running parallel above the treads on the open side nearest the lens, its balusters evenly spaced and straight. Every "
  "tread the same depth, every riser the same height, one straight line of steps — nothing curved, bent or doubled.",
  "A snapshot from a phone held at chest height by someone standing across the hall, not looking at the screen. " + PATIENT + " " + wear("BR-06") +
  " She is HALFWAY up the flight, about eight steps above the hall floor — as many steps below her as above her — coming down BACKWARDS: her body faces the "
  "stairs, her back to the hall below, both hands gripping the banister rail in front of her, her LEFT foot reaching back and down for the tread below, toes "
  "feeling for it, her weight on her arms, her head turned down over her shoulder to watch her feet. We see her whole body side-on, from hair to feet, in "
  "the middle of the flight, the steps above her rising to the landing and the steps below her dropping to the hall floor.",
  "The tall landing window at the top of the stairs lights her from the left of the frame, a grey morning, flat and cool, so she has a lit side toward the "
  "left and a softer shadow side.",
  "no second staircase, no curved stairs, no bent or broken stair geometry, no uneven treads, no floating steps, no stairs melting into the wall, no extra "
  "banisters, no banister passing through her, no woman near the bottom of the stairs, no woman near the top of the stairs, no facing forwards, no face "
  "towards the camera, no smiling, no falling, no stick, no second person, no strap product, no brace, no feet cut off, no extra legs, " + TXT))
# ---- BR-10b v2 (the heel supported) -----------------------------------------------------------------------------------------
P = paras("BR-10b.image.r9.prompt.txt")
P[1] = "THE CAMERA ANGLE: the lens low, at the height of her seat, looking up at the subject, seen in profile to her straight leg resting on the footstool, close. This exact angle, not a straight-on eye-level view."
P[3] = P[3].replace("the mustard fireside armchair, the patterned rug.", "the mustard fireside armchair, the patterned rug, a low round tapestry footstool in front of the chair.")
P[4] = rep(P[4], [("her LEFT leg held out straight in front of her, level with the seat, the heel of her white trainer off the rug,",
                   "her LEFT leg straight out in front of her, the heel of her white trainer RESTING on a low round tapestry footstool — the leg supported, the "
                   "footstool firmly on the rug and the heel firmly on the footstool,"), ("A strong leg, held steady.", "A strong leg, resting and steady.")])
P[7] = rep(P[7], [("no weights,", "no weights, no leg held up in the air, no heel floating above the footstool, no foot hovering, no leg raised off the footstool,")])
OUT["BR-10b"] = dict(v=2, refs=[R["P1"], R["P"]], prompt="\n\n".join(P))
# ---- anatomy: BR-10c v2, BR-14b v3, BR-20c v1 ------------------------------------------------------------------------------
M = (here / "MECH-05.image.r8.prompt.txt").read_text()
FRAME = [s for s in M.split("\n\n")[0].split(". ") if s.startswith("A stylised anatomical model")][0]
STATE = [p for p in M.split("\n\n") if p.startswith("STATE —")][0]
AV = [p for p in M.split("\n\n") if p.startswith("AVOID")][0]
PROD_ANAT = (" The knee wears the STRYDE strap, the only solid real-world object in the render: " + PROD.replace("The product exactly as in the attached reference image — ", "exactly as in the attached reference image — ")
             + " The strap sits on the patellar tendon directly below the kneecap, the notch cupping the kneecap's lower border, the band round the leg. "
             "Its shell is solid matte black, drawn true to the photograph, not translucent, never merged into the anatomy." + SLIM.replace(" On the leg it is", " It is"))
def anat(frame, state, avoid_swap=(), prod=False):
    t = M.replace(FRAME, frame).replace(STATE, state)
    if prod:  # the strap beats: the load is caught (BR-14b) or absent (BR-20c) — the glow-location paragraph would contradict it
        t = t.replace(state, state + PROD_ANAT); G = [p for p in t.split("\n\n") if p.startswith("WHERE THE GLOW IS")]; assert len(G) == 1
        t = t.replace("\n\n" + G[0], "")
    a = AV
    for o, n in avoid_swap: assert a.count(o) == 1, o; a = a.replace(o, n)
    return t.replace(AV, a)
PROD_AV = [("no rigid brace, no hinges, no sleeve, no second unit, no product half-on,", "no rigid brace, no hinges, no sleeve, no second unit, no product half-on, no translucent strap, no glowing strap, no chunky strap, no strap on the kneecap, no blank shell, no misspelled wordmark,"),
           ("no text overlays,", "no text overlays other than the stryde wordmark on the strap,")]
OUT["BR-10c"] = dict(v=2, refs=[], prompt=anat(
  "A stylised anatomical model of a whole left leg seen from a low three-quarter front angle, from the hip down to the foot, the foot just landing flat on a simple dark floor a step down from a simple dark step behind it, the knee bending to take the weight, the leg dominating the frame",
  "STATE — WHERE THE LOAD LANDS. The foot has just landed and the body's weight is arriving down the leg: a stream of warm red light runs down through the "
  "thigh like a current, from the hip to the knee, and pours into one point — the patellar tendon just below the kneecap — which flares bright red, near-white "
  "at its core, the brightest thing in frame. The stream above it is soft; the landing point is sharp. The shin and foot below stay calm and unlit."))
OUT["BR-14b"] = dict(v=3, refs=[R["FRONT"], R["TQ"]], prompt=anat(
  "A stylised anatomical model of a single left knee seen from a three-quarter front angle at eye height, close on the knee: the lower thigh, the kneecap, the patellar tendon under the strap and the top of the shin dominating the frame, the foot just landing on the edge of a simple dark step below, the limb falling away out of frame above",
  "STATE — CAUGHT AND MOVED. The foot has just landed and the load comes down the thigh as a stream of warm red light — and meets the strap: where the pad "
  "inside the strap presses on the patellar tendon, the red stream is caught and turned aside, spreading out sideways along the inside of the shell and "
  "round the band, a soft red glow fanning out left and right under the strap. Below the strap the tendon and the joint stay cool, pale and calm, unlit — "
  "the load never reaches them.", PROD_AV, prod=True))
OUT["BR-20c"] = dict(v=1, refs=[R["FRONT"], R["TQ"]], prompt=anat(
  "A stylised anatomical model of a single left knee in true lateral profile, edge-on, framed from mid-thigh to mid-shin and dominating the frame, the foot below just landing on a simple dark step, the limb falling away out of frame at both ends",
  "STATE — NOT LANDING ANY MORE. A step lands with the strap on: the knee bends a little under the weight, and the patellar tendon under the strap stays "
  "cool and calm — pale, unlit, a quiet ivory-rose, no red anywhere on it. The bones and muscles are calm too. The whole knee reads at rest under a full "
  "step; nothing glows.", PROD_AV + [("no steady unchanging glow,", "no red glow on the tendon, no hot spot,")], prod=True))
# ---- BR-16a v4 (gait lab) + BR-16a2 v1 (surgeons) ---------------------------------------------------------------------------
OUT["BR-16a"] = dict(v=4, refs=[R["FRONT"], R["WORN"]], prompt=img(
  "the lens low, at knee height, level, seen side-on, in profile, of the volunteer's step down onto the force plate.",
  "the knee with the strap on is in sharp focus; the lab behind falls to a soft, recognisable shape.",
  "A university gait lab: a pale grey rubber floor with a square metal force plate set flush in it, a low plain wooden step beside the plate, reflective "
  "markers on stands, a desk with a large monitor behind, tall side windows.",
  "A snapshot from a phone held low by a lab assistant, not looking at the screen. A volunteer — a man of sixty-five, grey hair, a navy t-shirt, grey running "
  "shorts, bare knees, grey trainers, small round reflective markers taped on his leg — steps down off the low wooden step onto the force plate, side-on to us, "
  "caught as his LEFT foot lands flat on the plate and the knee bends a little to take his weight. The knee strap is on his left knee. " + PROD +
  " It sits on the patellar tendon directly below the kneecap, the notch cupping the kneecap's lower border." + SLIM + " Behind him, soft, the monitor shows "
  "a single smooth coloured load curve on a dark background, no numbers readable. His whole body from head to feet is in frame.",
  "The tall side windows light him from the left of the frame, even neutral daylight with soft ceiling panels, so he has a lit side toward the left and a "
  "softer shadow side.",
  PNEGI + "no strap on the right knee, no treadmill, no running, no jumping, no wires, no hospital gown, no second person in front of him, no readable numbers "
  "or text on the monitor, " + TXT_P))
OUT["BR-16a2"] = dict(v=1, refs=[R["FRONT"], R["WORN"]], prompt=img(
  "the lens at the surgeons' eye height, level, seen from a three-quarter angle of the examination couch, the two surgeons and the knee in one frame.",
  "the strap and the surgeon's hands are in sharp focus; the second surgeon and the clinic behind fall a little soft.",
  "An orthopaedic outpatient clinic room: a pale blue examination couch with paper roll, a spine model and a knee model on a shelf, a sink, a tall window "
  "with a white roller blind half down.",
  "A snapshot from a phone held at eye height by a colleague standing in the doorway, not looking at the screen. A patient — a woman of sixty-two, short grey "
  "hair, a teal blouse, knee-length navy shorts, bare legs — sits on the edge of the couch, her left leg straight out along it. An orthopaedic surgeon — a "
  "friendly white British man of fifty, short dark hair greying at the temples, navy scrubs, a lanyard — leans in and, with both hands flat on the two sides "
  "of the shell, slides the strap up the last finger's width of her shin and seats it on the tendon just below her kneecap, looking at the placement. A second "
  "surgeon — a woman of forty-five, dark hair tied back, navy scrubs, reading glasses pushed up — stands at his shoulder watching, arms folded, one hand at "
  "her chin, nodding. " + PROD + SLIM,
  "The tall window lights them from the right of the frame, soft neutral daylight through the half-drawn blind, so the faces have a lit side toward the "
  "window and a softer shadow side, with a small catchlight in the eyes.",
  PNEGI + "no strap on the right knee, no surgery, no operating theatre, no masks, no scalpels, no blood, no hospital gown, no band being opened, no strap "
  "on the shin, no strap sliding down, " + TXT_P))
# ---- BR-16b v2 (walking group, park) ---------------------------------------------------------------------------------------
OUT["BR-16b"] = dict(v=2, refs=[R["FRONT"], R["WORN"]], prompt=img(
  "the lens low, at knee height, looking a little up at the subject, seen from the front of the walking group coming along the path.",
  "everything is in sharp focus; everything from near to far stays sharp.",
  "A wide park path on a bright spring morning: a pale gravel path, mown grass either side, big old plane trees in fresh leaf, a pond soft far behind.",
  "A snapshot from a phone held low by someone crouched at the edge of the path, a few metres ahead of the group, not looking at the screen. A walking group "
  "of eight older people, in their sixties and seventies, comes along the path towards us, relaxed and chatting, a couple laughing, mid-stride at an easy "
  "pace: men and women, mixed builds, sun hats and caps, light jackets tied round waists, walking shorts or cropped trousers, bare knees, trail shoes and "
  "walking boots, one pair of walking poles. The front walkers are a few metres from the lens, the rest behind them; faces and knees both read. On the knees "
  "of four of them — the two nearest and two further back — the same knee strap. " + PROD + " Each one sits on the patellar tendon directly below the "
  "kneecap, the notch cupping the kneecap's lower border." + SLIM + " The other four wear nothing on their knees.",
  "The open sky lights them from the left of the frame, bright neutral spring daylight through the trees, so they have a lit side toward the left and a "
  "softer shadow side.",
  PNEGI + "no strap on the shin, no two straps on one leg, no faces blurred, no merged people, no extra legs, no running, no crowd of more than eight, no "
  "towpath, no canal, " + TXT_P))
# ---- BR-17b v3 (out at the shops) -------------------------------------------------------------------------------------------
OUT["BR-17b"] = dict(v=3, refs=[R["P"]], prompt=img(
  "the lens at the subject's eye height, level, seen from a three-quarter angle of the woman at the greengrocer's display.",
  "she is in sharp focus from head to shoes; the street behind falls a little soft.",
  "A high-street greengrocer's on a bright morning: wooden crates of apples, oranges and greens on a tilted stand under a green-and-white striped awning, "
  "brown paper bags on a hook, the shop's open front, a pavement of grey flagstones, a street soft behind.",
  "A snapshot from a phone held at eye height by a friend beside her, not looking at the screen. " + PATIENT + " " + wear("BR-17b") + " She stands at the "
  "display, busy with her shopping, reaching into a crate to pick an apple into a brown paper bag in her other hand, weight easy on both legs, a small "
  "contented look. Her whole body from hair to shoes is in frame: the wide-leg mid-blue denim trousers fall straight and loose from her hips all the way down "
  "to her white trainers, the fabric hanging smooth and flat over both knees — nothing shows at the knee, no outline, no bulge, the two legs look exactly alike.",
  "The open sky over the street lights her from the right of the frame, bright morning daylight under the awning, so her face has a lit side toward the "
  "right and a softer shadow side, with a small catchlight in the eyes.",
  "no strap visible, no strap outline through the denim, no bulge at the knee, no rolled trouser leg, no cuff, no shorts, no bare knee, no brace, no stick, "
  "no one else in focus, no shop signs readable, no prices readable, " + TXT))
# ---- BR-20 v2, BR-20b v1 (the doctor's hands, the scans) --------------------------------------------------------------------
OUT["BR-20"] = dict(v=2, refs=[R["P3"], R["D"]], prompt=img(
  "the lens at the subject's eye height, level, seen from the front of the knee X-ray held against the window, close.",
  "the X-ray and his fingertip on it are in sharp focus; the window frame behind falls soft.",
  "IN THE SAME ROOM as the attached consulting-room photograph, at its tall window, white vertical blinds open, grey daylight outside.",
  "A snapshot from a phone held at eye height by someone standing beside him, not looking at the screen. One knee X-ray film held flat against the window "
  "glass by the doctor's left hand at its top corner — the hand of the man in the attached reference sheet, the cuff of a crisp white doctor's coat over a pale "
  "blue shirt cuff, a plain steel watch — the daylight coming through it: a grey-and-black front view of one left knee, the thigh bone above, the shin bone "
  "below, the joint gap between them clearly narrowed on the inner side, the bone edges there rough and close together. His right forefinger rests on the film "
  "exactly on that narrow inner joint gap, tracing along it. The film fills most of the frame; only his hands and cuffs show.",
  "The consulting-room window behind the film lights it from the back of the frame, steady overcast daylight coming through the film, so the hands have a "
  "lit edge and a softer shadow side.",
  "no face, no lightbox, no glowing screen, no two films, no X-ray of a hand or chest, no writing, names, dates or labels on the film, no fingers passing "
  "through the film, " + TXT))
OUT["BR-20b"] = dict(v=1, refs=[R["P3"], R["D"]], prompt=img(
  "the lens above the desk, looking straight down at the subject, overhead, onto the two X-ray films side by side.",
  "the two films are in sharp focus; the desk edges fall a little soft.",
  "IN THE SAME ROOM as the attached consulting-room photograph, on his wooden desk top, a closed notebook and a pen at the edge.",
  "A snapshot from a phone held over the desk by someone standing at it, not looking at the screen. Two knee X-ray films lie side by side on the desk, edge "
  "to edge, square to each other: two grey-and-black front views of the same left knee, identical — the same bones, the same narrowed joint gap on the inner "
  "side, the same shape, nothing different between them. His two hands — the hands of the man in the attached reference sheet, white coat cuffs over pale "
  "blue shirt cuffs, a plain steel watch — rest at the outer edges of the two films, squaring them up, fingertips flat on the corners.",
  "The consulting-room window at the left lights the desk from the left of the frame, steady overcast north daylight, so the films and hands have a lit "
  "side toward the left and a softer shadow side.",
  "no face, no lightbox, no glowing screen, no third film, no different scans, no X-ray of a hand or chest, no writing, names, dates or labels on the films, "
  "no fingers across the knee images, " + TXT))
for b, o in OUT.items():
    assert "[" not in o["prompt"], b
    (here / f"{b}.image.r11.prompt.txt").write_text(o["prompt"]); o["model"] = "nano_banana_pro"; print(f"{b:8s} v{o['v']} {len(o['prompt']):5d}")
json.dump(OUT, open(here / "fix_r11.json", "w"), indent=1)
json.dump([{"index": 1200 + i, "params": {"model": "nano_banana_pro", "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in o["refs"]], "prompt": o["prompt"]}} for i, o in enumerate(OUT.values())],
          open(here / "fix_r11_batch.json", "w"), ensure_ascii=False)
