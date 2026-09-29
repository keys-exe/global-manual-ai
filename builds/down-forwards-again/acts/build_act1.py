#!/usr/bin/env python3
"""Step 7 · Act 1 frames (step-1 images) for down-forwards-again, from the act map (work/actmap.json).
Lifestyle BR: the hooks' §22T order (CAM-LOCK → ANGLE-LINE → FOCUS-LINE → PROP-REF/room → prose → LIGHT-SHOT → CAP-FILE → AVOID), start frame caught in the action.
MECH: §12A-1 — ANAT-BASE → density (ANAT-A / ANAT-B) → ANAT-LIGHT → ANAT-FIELD → state (ANAT-HOT / ANAT-REST) → AVOID ANAT-NEG; SITE from the Product Sheet
(the patellar tendon just below the kneecap), ANAT_A_POINT_TIGHT on every ANAT-A beat; ANATOMY_LOOK: conditions = ANAT-B, point = ANAT-A.
Helpers and shared strings come from hooks/build_hooks.py (v1)."""
import re, json, pathlib, importlib.util
here = pathlib.Path(__file__).parent
hk = here.parent / "hooks" / "build_hooks.py"
src = hk.read_text()
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
P_D1 = ("She wears a cream fine-knit roll-neck under an oatmeal cable-knit cardigan buttoned once, a knee-length plum wool skirt with bare legs, "
        "burgundy fleece-lined slippers, and reading glasses on a cord round her neck.")
REF = {"P-PATIENT": "02333782-0c9a-4696-b3f1-fcc7480fe8db", "P0-PROP-P v2": "176c5c39-ac17-46c4-9e9b-2c06735dc0c8",
       "P1-P-FRONTROOM v2": "d0eeaf2a-abad-4a79-a9da-624c5eef41a1", "P2-P-KITCHEN v2": "abc2c220-b0f0-43d2-b583-d22b5696225b",
       "P3-D-CONSULT": "757817ea-6840-487c-879c-1b0310e137b2", "D-VOICE-IMG v2": "b17f293d-306f-406c-b145-029402a1c074"}
B = {}
B["BR-01"] = dict(refs=["P2-P-KITCHEN v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  angle("eye", "a three-quarter angle", "the woman at the table"),
  focus("the nearest eye of the woman", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The kitchen of the attached kitchen photograph: the pine farmhouse table, the spindle-back chairs, the dresser soft behind.",
  "A snapshot from a phone held at eye height by someone sitting across the corner of the table, not looking at the screen. " + P_FACE + " " + P_D1 +
  " She sits at the pine table, both hands round a mug of tea, a morning newspaper folded by her elbow, and her left hand has just left the mug and come down "
  "onto her LEFT knee under the table edge, caught in the middle of one slow rub across the knee through the skirt, her face tight with the familiar ache, "
  "eyes down, mouth shut. Head, shoulders, both hands and the left knee are in frame.",
  light("The window over the sink on the room's west wall", "her", "right", "flat overcast daylight, the grey problem days", "the right"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no smiling, no second person, no strap product, no brace on the knee, no bare knee showing a product", NOTEXT])])
B["BR-02"] = dict(refs=["P3-D-CONSULT", "D-VOICE-IMG v2"], body=[S("CAM-LOCK"),
  angle("low", "a three-quarter angle", "his hands at the window"),
  focus("the foreground", "the room behind falls to a soft, recognisable shape"),
  "IN THE SAME ROOM as the attached consulting-room photograph, at its tall window on the left, white vertical blinds open, grey daylight outside.",
  "A snapshot from a phone held low by someone standing beside him, looking up at the window, not looking at the screen. "
  "The doctor's two hands — a stocky man's hands of fifty-four, fair freckled skin, a plain steel watch, the white cuffs of his doctor's coat over pale blue shirt cuffs — "
  "are caught pressing a grey-and-black knee X-ray film flat against the window glass, the film big in the foreground, its top edge just sliding under a small clip, "
  "the daylight coming through it: the pale bones of one knee, the joint gap narrowed almost to nothing on one side. His face is out of frame above.",
  light("The consulting-room window, behind the film", "the film and his hands", "back", "steady overcast daylight coming through the film", "the window", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face, no lightbox, no glowing screen, no X-ray of a hand or chest, no writing, names or labels on the film, no coat missing", NOTEXT])])
B["BR-04"] = dict(refs=["P1-P-FRONTROOM v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  angle("high", "the front", "her knee and her hand"),
  focus("the hands and what they hold", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The front room of the attached front-room photograph, seen from above: the mustard armchair seat and the patterned rug soft around the knee.",
  "A snapshot from a phone held above her lap by someone looking straight down at her knee, not looking at the screen. She sits in the mustard armchair, "
  "the hem of her plum wool skirt pushed back above her LEFT knee with her left hand, the bare knee filling the middle of the frame: pale skin, a little swollen, "
  "fine creases, a few faint thread veins. Her right forefinger — a woman of sixty-nine, thin skin, a plain gold wedding band, the cuff of an oatmeal cardigan — "
  "is caught pressing into the soft spot just below her LEFT kneecap, two centimetres under its lower edge, the skin dimpling round the fingertip. "
  "The kneecap's outline reads clearly above the finger.",
  light("The bay window on the room's east wall", "her knee and hand", "left", "grey even daylight through the net curtains", "the left", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face, no strap product, no brace, no plaster, no bruise, no finger on the kneecap itself, no second hand pressing, no right knee in focus", NOTEXT])])
B["BR-05a"] = dict(refs=["P0-PROP-P v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  angle("eye", "behind", "the woman on the stairs"),
  focus("everything", "everything from near to far stays sharp"),
  PROPREF + " The hall and the wide straight staircase of the attached property photograph: the stairs rise away along the left-hand wall, the dark turned banister on the open right side, the patterned runner with brass rods on every tread.",
  "A snapshot from a phone held at eye height by someone standing in the hall at the foot of the stairs, behind her, not looking at the screen. "
  "The woman of sixty-nine from the attached reference sheet — chestnut-dyed chin-length hair with silver roots — seen from behind. " + P_D1 +
  " She is going UP her stairs away from the camera, two steps from the bottom, caught in the middle of one steady step: her right foot planted on the next tread, "
  "her left foot just lifting off the one below, her right hand sliding up the banister rail, her body upright and easy. Her whole body from hair to slippers is in frame, stairs above her.",
  light("The tall landing window at the top of the stairs", "her", "right", "a grey morning, the landing window a soft bright source, the hall a stop darker", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face towards the camera, no walking backwards, no coming down, no stick, no second person, no strap product, no brace, no feet cut off", NOTEXT])])
B["BR-05b"] = dict(refs=["P0-PROP-P v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  angle("low", "a three-quarter angle", "the woman coming down the stairs"),
  focus("everything", "everything from near to far stays sharp"),
  PROPREF + " The hall and the wide straight staircase of the attached property photograph, the dark turned banister on the open right side, the patterned runner with brass rods.",
  "A snapshot from a phone held at hip height by someone standing at the foot of the stairs, off to one side, not looking at the screen. " + P_FACE + " " + P_D1 +
  " She is coming DOWN her stairs facing forwards, four steps from the bottom, slowly and carefully, both hands gripping the banister rail, "
  "caught in the moment her LEFT foot lands on the tread below: the LEFT knee bent and braced as it takes her weight, her right foot still on the step above, "
  "her body leaning back a little towards the rail, her face tight and wary, eyes on the tread, mouth shut. Her whole body from hair to slippers is in frame.",
  light("The stained-glass panel in the front door, behind the phone", "her", "right", "a grey morning, a pale wash down the runner", "the right"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no walking backwards, no smiling, no stick, no fall, no second person, no strap product, no brace, no feet cut off", NOTEXT])])
NEG_ANAT = lambda drop=(): ", ".join(c for c in (x.strip() for x in S("ANAT-NEG").split(",")) if c not in drop)
B["MECH-01"] = dict(refs=[], body=[anat("ANAT-BASE").replace("A stylised anatomical model of a single knee", "A stylised anatomical model of both knees of one older woman, the LEFT knee in front,"),
  anat("ANAT-B"),
  "THE CONDITION: in the LEFT knee the joint space between femur and tibia has narrowed almost to nothing on the inner side, the thin cartilage worn away so the "
  "two bone ends nearly touch, their facing surfaces roughened and flattened, a faint warm orange-red glow where bone meets bone. Behind it, softer, the RIGHT knee "
  "shows the same joint beginning to narrow, a first faint warm redness starting at its inner side — the second knee following the first.",
  anat("ANAT-LIGHT"), anat("ANAT-FIELD"),
  "AVOID: " + NEG_ANAT(("no second limb", "no highlighted hotspots"))])
B["MECH-03"] = dict(refs=[], body=[anat("ANAT-BASE").replace("viewed from a low three-quarter angle, foreshortened, the knee joint sitting slightly off-centre",
  "in true lateral profile, edge-on, the limb running vertically, framed from mid-thigh to mid-shin"),
  anat("ANAT-A"), anat("ANAT-LIGHT"), anat("ANAT-FIELD"),
  anat("ANAT-HOT").replace("The emission", "The emission, a deep glowing red,"),
  ps.ANAT_A_POINT_TIGHT + " The lit band is the patellar tendon, about as wide as a thumb, running from the lower edge of the kneecap down to the top of the shin.",
  "AVOID: " + NEG_ANAT(("no highlighted hotspots", "no arrows", "no force arrows", "no motion lines", "no vector lines"))])
B["MECH-05"] = dict(refs=[], body=[anat("ANAT-BASE").replace("A stylised anatomical model of a single knee", "A stylised anatomical model of a single left leg stepping down, the knee bending to take the weight,"),
  anat("ANAT-A"), anat("ANAT-LIGHT"), anat("ANAT-FIELD"),
  "The leg is caught partway through stepping down onto a lower step: the knee bent, the thigh muscles lengthening under tension to control the descent, "
  "the foot just meeting the step below. " + anat("ANAT-REST"),
  "AVOID: " + NEG_ANAT(("no arrows", "no force arrows", "no motion lines", "no vector lines"))])
out = {}
for k, b in B.items():
    txt = "\n\n".join(b["body"]); assert "[" not in txt, (k, txt[txt.index("["):txt.index("[") + 80])
    out[k] = dict(model="nano_banana_2", refs=b["refs"], ref_jobs=[REF[r] for r in b["refs"]], chars=len(txt), prompt=txt)
    (here / f"{k}.image.prompt.txt").write_text(txt); print(f"{k:8s} {len(txt):5d}  refs: {', '.join(b['refs']) or '—'}")
json.dump(out, open(here / "act1.json", "w"), indent=1)
json.dump([{"index": i, "params": {"model": v["model"], "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in v["ref_jobs"]], "prompt": v["prompt"]}} for i, v in enumerate(out.values())],
          open(here / "act1_batch.json", "w"), indent=1)
