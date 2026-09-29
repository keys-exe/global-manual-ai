#!/usr/bin/env python3
"""Step 6 hook frames v3 — the user's board Fix notes, 2026-09-29:
  HK1-01a  "SHOULD SHOW HER GOING DOWN THE STAIRS AT THE SUBWAY STATION RUNNING DOWN NOT JUST AT HOME"
           → the after: she runs lightly DOWN the entrance stairs of an Underground station, forwards (P-D2, CONCEALED under trousers)
  HK1-02a  "DONT JUST SHOW 1 BROLL HERE SHOW ALL OF THOSE" → one B-roll per "without" (§30B triplet, one variable escalating):
           HK1-02a the operation (a pre-op marker arrow drawn on her left knee) · HK1-02b the physio (resistance band on the front-room floor)
           · HK1-02c the drawer (the v2 spill render, carried over — no new call)
  HK2-02a  "THE TEN SECONDS IT MEANS TEN SECONDS TO PUT ON THE STRYDE STRAP" → seating beat (§9B, SEAT_LOCK start frame, Product Sheet WEAR_GUIDE)
Helpers and shared strings come from build_hooks.py (v1), read up to its beat table."""
import re, json, pathlib, importlib.util
here = pathlib.Path(__file__).parent
src = (here / "build_hooks.py").read_text()
exec(compile(src[:src.index("\nB = {}")].replace("__file__", repr(str(here / "build_hooks.py"))), "build_hooks.py", "exec"))
spec = importlib.util.spec_from_file_location("ps", ROOT / "products/stryde/stryde_product_sheet.py"); ps = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(ps)
except AssertionError: pass

P_D1 = ("She wears a cream fine-knit roll-neck under an oatmeal cable-knit cardigan buttoned once, a knee-length plum wool skirt with bare legs, "
        "and reading glasses on a cord round her neck.")
P_D2 = ("Today she wears a white cotton shirt with the sleeves turned back, an open coral lightweight cardigan, wide-leg navy linen trousers down to the ankle, "
        "and tan leather flat loafers; small gold hoop earrings.")
B = {}
# HK1-01a v3 — L-TUBE (INCIDENTAL, new): station entrance stairs from the street, the after (P-D2), running lightly down forwards
B["HK1-01a"] = dict(model="nano_banana_2", refs=["P-PATIENT"], body=[S("CAM-LOCK"),
  angle("low", "the front", "the woman coming down the stairs"),
  focus("everything", "everything from near to far stays sharp"),
  "The entrance stairs of a London Underground station on a busy morning: a wide flight of worn concrete steps with steel nosings and a steel handrail down the right-hand wall, "
  "cream-and-maroon glazed tiles on the walls, the street and a strip of pale sky bright at the top of the stairs behind her, a couple of commuters in coats further up, soft and small. "
  "No signs, no logos, no roundels, no readable text anywhere.",
  "A snapshot from a phone held at hip height by someone standing at the bottom of the stairs, not looking at the screen, tilted a touch. " + P_FACE + " " + P_D2 +
  " She is RUNNING DOWN the station stairs FACING FORWARDS, light and quick, a woman in a hurry for her train and loving it: caught mid-stride on the lower third of the flight, "
  "her weight landing on her left foot on one step, her right foot already off the step above and swinging down, her right hand skimming the handrail without gripping it, "
  "her left arm swinging, her handbag bouncing at her hip, a small real smile, eyes on the steps ahead. "
  "The wide trousers swing loose and crease at the knees as linen does, both legs reading as ordinary covered legs. "
  "Her whole body from hair to shoes is in frame, with steps below her to land on.",
  light("The open street entrance at the top of the stairs behind her", "her", "right", "bright morning daylight pouring down the stairs, with the station's overhead strip lights filling the lower steps", "the right"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([S("NEG-CONCEAL"), *NEG_BASE(), "no walking backwards, no clutching the handrail, no stick, no stumbling, no falling, no pain on her face, "
                         "no skirt, no bare knees, no feet cut off, no motion blur smearing her, no crowd blocking her, no Underground roundel, no station name, no signs", NOTEXT])])

# HK1-02a — the operation she did not have: pre-op marker arrow on her LEFT knee (hospital, INCIDENTAL L-HOSP); product absent
B["HK1-02a"] = dict(model="nano_banana_2", refs=["P-PATIENT"], body=[S("CAM-LOCK"),
  angle("high", "a three-quarter angle", "her knee on the hospital bed"),
  focus("the hands and what they hold", "the room behind falls to a soft, recognisable shape"),
  "An NHS pre-operation bay: a hospital trolley bed with a white sheet and a pale blue cellular blanket, a blue disposable curtain drawn round on a ceiling rail, a grey vinyl floor, a wall panel of oxygen outlets soft behind.",
  "A snapshot from a phone held above the bed by someone standing at its side, looking down, not looking at the screen. "
  "The woman of sixty-nine from the attached reference sheet sits on the edge of the bed in a faded blue-patterned hospital gown, a white plastic name band on her wrist, her bare LEFT leg straight out on the bed, "
  "her hands knotted in her lap at the edge of the frame. A nurse's gloved hand in a blue nitrile glove, holding a black surgical skin marker, "
  "is caught in the middle of drawing a thick black ARROW on the skin of her thigh just above her LEFT kneecap, pointing down at the knee, the arrow's shaft drawn and the head half made. "
  "Her knee is the middle of the frame: pale, a little swollen, the skin thin and creased. The rest of her is cut off by the frame above the waist.",
  light("The bay's window on the far wall, past the curtain", "the bed and her knee", "left", "flat grey daylight mixed with the ward's cool ceiling light", "the left", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no blood, no incision, no scalpel, no surgery in progress, no operating theatre, no strap product, no brace, no writing other than the arrow, "
                         "no readable name on the wrist band, no hospital logo, no hand cut off at the frame edge, no bare glove-less hand holding the marker", NOTEXT])])

# HK1-02b — another course of physio: resistance band on the front-room floor (L-P-FRONT, P-D1); overhead; product absent
B["HK1-02b"] = dict(model="nano_banana_2", refs=["P1-P-FRONTROOM v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  "THE CAMERA ANGLE: the lens directly above her, looking straight down at the floor, seen from above her head. This exact angle, not a straight-on eye-level view.",
  focus("the nearest eye of the woman", "everything from near to far stays sharp"),
  PROPREF + " The front room of the attached front-room photograph, seen from above: the patterned rug over the floorboards, the foot of the mustard armchair at one edge.",
  "A snapshot from a phone held straight out above her by someone standing over her, not looking at the screen. " + P_FACE + " " + P_D1 +
  " She lies on her back on a thin blue exercise mat on the rug, her LEFT leg raised straight in the air with a green rubber physio resistance band looped round the sole of her slipper, "
  "both hands gripping the two ends of the band against her chest, caught mid-pull, the band stretched tight, her jaw set and her brow creased with the effort, eyes on the ceiling, mouth shut. "
  "Beside her on the rug: a printed sheet of exercise drawings with stick figures and no readable words, a second yellow band and a small foam roller.",
  light("The bay window on the room's east wall", "her", "left", "grey even daylight through the net curtains, the problem days", "the left"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no gym, no physiotherapist in frame, no second person, no smiling, no strap product, no brace, no readable words on the sheet, "
                         "no band snapping, no feet cut off", NOTEXT])])

# HK2-02a — seating beat (NEG_SEAT goes on the clip, not this start frame: it bans the mid-shin rest the frame needs)
# HK2-02a — seating beat (§9B): ten seconds to put it on. SEAT_LOCK start frame, VISIBLE (bare legs under a knee-length skirt, seated)
REFP = ps.REF_PROD
B["HK2-02a"] = dict(model="nano_banana_pro", refs=["front.webp", "W-L-FRONT", "P-PATIENT", "P1-P-FRONTROOM v2"], body=[S("CAM-LOCK"),
  angle("low", "a three-quarter angle", "her left leg and the strap"),
  focus("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The front room of the attached front-room photograph, the mustard fireside armchair by the bay window.",
  "A snapshot from a phone held low by someone crouched in front of her, not looking at the screen. "
  "The woman of sixty-nine from the attached reference sheet sits forward on the edge of the mustard armchair, " + P_D1.replace("She wears", "wearing") +
  " Her knee-length skirt has ridden up above her knees as she sits, her LEFT leg out straight in front of her, heel on the rug, the bare shin and knee clear. "
  "She is putting her knee strap on. " + REFP + " " + ". ".join(ps.fill(ps.SEAT_LOCK, "left").split(". ")[:2]).split(" and slide the whole strap")[0].rstrip(", ") + ". "
  "This is the first moment, before it moves: the strap still sits at mid-shin, well below the knee, both hands flat on its two sides, "
  "the kneecap bare above it, the notch pointing up at the kneecap, the wordmark upright and readable to the camera." +
  " Her face at the top of the frame looks down at her knee, calm, mouth shut. Her RIGHT leg is bare with nothing on it.",
  light("The bay window on the room's east wall", "her leg and the strap", "right", "bright morning sun through the net curtains, the after", "the right"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([ps.NEG_ADJUST, *NEG_BASE(), "no strap already under the kneecap, no strap seated yet, no strap on the right leg, no two straps, no strap on the kneecap, no strap on the thigh, no trousers, no tights", NOTEXT.replace("anywhere", "anywhere except the stryde wordmark on the strap")])])

REF = {"P-PATIENT": "02333782-0c9a-4696-b3f1-fcc7480fe8db", "P1-P-FRONTROOM v2": "d0eeaf2a-abad-4a79-a9da-624c5eef41a1",
       "front.webp": "c942d91d-718d-4723-b190-ad85186ac8d9", "W-L-FRONT": "793ca329-e4b3-49fd-943c-5e97bae5366d"}
out = {}
for k, b in B.items():
    txt = "\n\n".join(b["body"]); assert "[" not in txt, (k, txt[txt.index("["):txt.index("[")+80])
    out[k] = dict(model=b["model"], refs=b["refs"], ref_jobs=[REF[r] for r in b["refs"]], chars=len(txt), prompt=txt)
    (here / f"{k}.image.v3.prompt.txt").write_text(txt); print(f"{k:8s} {len(txt):5d}  {b['model']:15s} refs: {', '.join(b['refs'])}")
json.dump(out, open(here / "hooks_v3.json", "w"), indent=1)
