#!/usr/bin/env python3
"""Step 6 hook frames v5 — the user's board Fix notes, 2026-09-29 ~12:40 UTC (HK1-01a v4 confirmed):
  HK1-02a  "it should not be an operation immediately it should be like the doctor proposing a knee replacement"
           → consultation (L-ORTHO): over the surgeon's shoulder, he holds a knee replacement implant out across the desk to her; her worried face sharp
  HK1-02b  "its too simple and the camera angle i dont like" → a busy NHS physio class, ground level through the parallel bars, she strains through a step
  HK1-02c  "i dont like this create a new one" → keeps the earlier brief (the strap, the braces behind, focus on the strap): the camera down in the drawer
           looking up past the old braces as her hand lifts the STRYDE strap out (HELD_GRIPS bottom-edge pinch)
Helpers and shared strings come from build_hooks.py (v1)."""
import re, json, pathlib, importlib.util
here = pathlib.Path(__file__).parent
src = (here / "build_hooks.py").read_text()
exec(compile(src[:src.index("\nB = {}")].replace("__file__", repr(str(here / "build_hooks.py"))), "build_hooks.py", "exec"))
spec = importlib.util.spec_from_file_location("ps", ROOT / "products/stryde/stryde_product_sheet.py"); ps = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(ps)
except AssertionError: pass
P_D1 = ("She wears a cream fine-knit roll-neck under an oatmeal cable-knit cardigan buttoned once, a knee-length plum wool skirt with bare legs, "
        "and reading glasses on a cord round her neck.")
B = {}
B["HK1-02a"] = dict(model="nano_banana_2", refs=["P-PATIENT"], prompt="\n\n".join([S("CAM-LOCK"),
  "THE CAMERA ANGLE: the lens at the surgeon's shoulder height, looking over his near shoulder across the desk at her. This exact angle, not a straight-on eye-level view.",
  focus("the nearest eye of the woman", "the room behind falls to a soft, recognisable shape"),
  "An NHS orthopaedic outpatient consulting room: a plain desk between them, a computer screen turned away showing nothing readable, a lightbox on the wall behind her with a knee X-ray clipped to it, soft, a pale green wall, a window to the left.",
  "A snapshot from a phone held at shoulder height just behind the surgeon's chair, not looking at the screen. In the near foreground, soft and out of focus, the back of the surgeon's head and his right shoulder in a navy suit jacket, "
  "his forearm reaching across the desk: his hand holds out a TOTAL KNEE REPLACEMENT IMPLANT towards her — a polished chrome-cobalt femoral component curved like a knuckle on a grey-white plastic spacer and a metal tibial tray with a short stem, mirror-bright — "
  "the implant sharp in the middle of the frame. Across the desk, sharp: " + P_FACE + " " + P_D1 +
  " She sits on the patient's chair with her handbag on her lap and both hands clenched on its handle, leaning back slightly away from the implant, looking at it, "
  "her brow drawn together, her lips pressed tight, the worried face of someone being told she needs a new knee, mouth shut.",
  light("The window on the room's left wall", "her face", "left", "flat grey daylight, the problem days", "the left"),
  S("SKIN-T").replace("[AGE-FEATURES]", "fine age spots and faint thread veins"), S("CAP-SHARP"), S("CAP-FILE"),
  "AVOID: " + ", ".join([S("NEG-FILE"), *NEG_BASE(), "no hospital bed, no gown, no surgery, no blood, no scar, no marker arrow, no strap product, no brace, no surgeon's face, "
                         "no second implant, no plastic toy, no readable writing on the screen, the X-ray or the walls, no smiling", NOTEXT])]))

B["HK1-02b"] = dict(model="nano_banana_2", refs=["P-PATIENT"], prompt="\n\n".join([S("CAM-LOCK"),
  "THE CAMERA ANGLE: the lens a few centimetres off the floor, looking along it and slightly up, seen from a three-quarter angle of her between the parallel bars, "
  "looking past the upright of the near parallel bar, soft in the near foreground. This exact angle, not a straight-on eye-level view.",
  focus("the nearest eye of the woman", "the room behind falls to a soft, recognisable shape"),
  "A busy NHS hospital physiotherapy gym mid-morning, a knee class in full swing: a sprung blue floor, two long wooden parallel bars running away from the camera, wall bars, a rack of coloured resistance bands, "
  "exercise balls and low steps, and behind her a row of five or six other older patients in their own clothes all doing the same step-up at their own steps, a physio at the front of the class calling the count with one hand raised, soft. "
  "No posters with readable words, no logos.",
  "A snapshot from a phone held down on the floor by someone kneeling at the end of the parallel bars, not looking at the screen. " + P_FACE + " " + P_D1 +
  " She stands between the parallel bars gripping both bars hard, knuckles white, caught in the middle of stepping up onto a low grey step with her LEFT foot, "
  "the left knee bent and shaking under the load, her whole weight hanging on her arms, her face screwed up with the effort, a sheen of sweat on her forehead, eyes on her knee, mouth shut. "
  "A physiotherapist in a navy tunic crouches at her side with both hands hovering either side of her left knee, spotting it. Her feet, the step and the floor are big and close in the lower frame.",
  light("The tall windows along the gym's far wall", "her", "left", "grey daylight with the gym's ceiling panels on, the problem days", "the left"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no home, no living room, no smiling, no strap product, no brace, no readable words anywhere, no NHS logo, no gym brand, "
                         "no crowd blocking her, no eye-level camera", NOTEXT])]))

grip = dict(ps.HELD_GRIPS)["bottom-edge pinch"].replace(" (HELD_EXAMPLE shows this one)", "")
B["HK1-02c"] = dict(model="nano_banana_pro", refs=["front.webp", "product_tq_left.jpg", "P2-P-KITCHEN v2"], prompt="\n\n".join([S("CAM-LOCK"),
  "THE CAMERA ANGLE: the lens down inside the open drawer, among the old knee supports, looking up and out of the drawer at her hand and the kitchen ceiling beyond. This exact angle, not a straight-on eye-level view.",
  focus("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The kitchen of the attached kitchen photograph, seen from inside the old pine Welsh dresser's top drawer: the drawer's pine sides rising at the edges of the frame, the kitchen ceiling and pendant light above, soft.",
  "A snapshot from a phone lying in the drawer, face up, among the clutter. In the near foreground, filling the bottom third of the frame and softly out of focus: a heap of old knee supports — "
  "black stretchy sleeves, beige wraps with loose velcro tabs, a grey hinged brace with metal side bars — all worn, blank and plain. "
  "Above them, sharp and in the middle of the frame, a woman's hand — sixty-nine, thin skin, a plain gold wedding band, the cuff of an oatmeal cable-knit cardigan — is caught lifting her knee strap up out of the drawer. "
  + ps.REF_PROD + " held by the " + grip + ", its front face turned down towards the lens, the wordmark readable. "
  "The strap is the only sharp thing in the picture; the old braces below and the kitchen above are soft.",
  light("The window over the sink on the room's west wall", "the strap and her hand", "right", "flat overcast daylight falling into the drawer", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([ps.NEG_HELD_P, *NEG_BASE(), "no face in frame, no second hand, no strap worn on a leg, no brace in her hand, no sharp braces, no packaging", NOTEXT.replace("anywhere", "anywhere except the stryde wordmark on the strap")])]))

REF = {"P-PATIENT": "02333782-0c9a-4696-b3f1-fcc7480fe8db", "P2-P-KITCHEN v2": "abc2c220-b0f0-43d2-b583-d22b5696225b",
       "front.webp": "c942d91d-718d-4723-b190-ad85186ac8d9", "product_tq_left.jpg": "4a56cffe-69bc-4f77-ac90-38258b124e65"}
out = {}
for k, b in B.items():
    txt = b["prompt"]; assert "[" not in txt, (k, txt[txt.index("["):txt.index("[")+80])
    out[k] = dict(model=b["model"], refs=b["refs"], ref_jobs=[REF[r] for r in b["refs"]], chars=len(txt), prompt=txt)
    (here / f"{k}.image.v5.prompt.txt").write_text(txt); print(f"{k:8s} {len(txt):5d}  {b['model']:15s} refs: {', '.join(b['refs'])}")
json.dump(out, open(here / "hooks_v5.json", "w"), indent=1)
