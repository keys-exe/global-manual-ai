#!/usr/bin/env python3
"""Step 6 hook frames v4 — the user's board Fix notes, 2026-09-29 ~11:50 UTC:
  HK1-01a  "her hands should never hold the hand rail"          → station stairs as v3, both hands free, nowhere near the rail
  HK1-02a  "the operation is a knee replacement"               → a surgeon holds a total knee replacement implant beside her bare left knee
  HK1-02b  "should be a COURSE not at home"                     → an NHS physiotherapy class in a hospital physio gym, the physio correcting her
  HK1-02c  "holding the stryde strap with her hands and at the back is the braces and the camera focus only of the stryde"
           → held beat (§9A, Product Sheet HELD_GRIPS 'fingertips behind'), the overfull drawer of braces soft behind, focus on the strap
Helpers and shared strings come from build_hooks.py (v1) and build_hooks_v3.py."""
import re, json, pathlib, importlib.util
here = pathlib.Path(__file__).parent
src = (here / "build_hooks.py").read_text()
exec(compile(src[:src.index("\nB = {}")].replace("__file__", repr(str(here / "build_hooks.py"))), "build_hooks.py", "exec"))
spec = importlib.util.spec_from_file_location("ps", ROOT / "products/stryde/stryde_product_sheet.py"); ps = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(ps)
except AssertionError: pass
v3 = json.load(open(here / "hooks_v3.json"))

P_D1 = ("She wears a cream fine-knit roll-neck under an oatmeal cable-knit cardigan buttoned once, a knee-length plum wool skirt with bare legs, "
        "and reading glasses on a cord round her neck.")
B = {}
# HK1-01a v4 — v3 with the hands moved off the rail (the Fix note), everything else kept
p = v3["HK1-01a"]["prompt"]
p = p.replace("her right hand skimming the handrail without gripping it, her left arm swinging, her handbag bouncing at her hip,",
              "BOTH HANDS FREE and nowhere near the handrail — her arms swinging loosely at her sides for balance like anyone taking stairs at a jog, "
              "her handbag strap over her shoulder, the bag bouncing at her hip,")
p = p.replace("a wide flight of worn concrete steps with steel nosings and a steel handrail down the right-hand wall,",
              "a wide flight of worn concrete steps with steel nosings, the steel handrail far over against the right-hand wall, well away from her,")
p = p.replace("no walking backwards, no clutching the handrail,", "no hand on the handrail, no hand touching the rail or the wall, no reaching for the rail, no walking backwards,")
assert "skimming" not in p
B["HK1-01a"] = dict(model="nano_banana_2", refs=["P-PATIENT"], prompt=p)

# HK1-02a v4 — the knee replacement she did not have (L-HOSP, INCIDENTAL)
B["HK1-02a"] = dict(model="nano_banana_2", refs=["P-PATIENT"], prompt="\n\n".join([S("CAM-LOCK"),
  angle("high", "a three-quarter angle", "her knee and the implant"),
  focus("the hands and what they hold", "the room behind falls to a soft, recognisable shape"),
  "An NHS orthopaedic pre-operation bay: a hospital trolley bed with a white sheet and a pale blue cellular blanket, a blue disposable curtain drawn round on a ceiling rail, a grey vinyl floor.",
  "A snapshot from a phone held above the bed by someone standing at its side, looking down, not looking at the screen. "
  "The woman of sixty-nine from the attached reference sheet sits on the edge of the bed in a faded blue-patterned hospital gown, a white plastic name band on her wrist, "
  "her bare LEFT leg straight out on the bed, pale, a little swollen at the knee, a black surgical-marker arrow drawn on her thigh pointing down at the knee. "
  "The orthopaedic surgeon's hand in a blue nitrile glove holds a TOTAL KNEE REPLACEMENT IMPLANT a hand's width above her left knee, showing her what would go in: "
  "a polished chrome-cobalt femoral component curved like a knuckle, sitting on a flat grey-white plastic spacer on a polished metal tibial tray with a short stem, "
  "the real surgical implant, mirror-bright, caught as it is being lowered towards her knee. Her own hands grip the edge of the blanket at the edge of the frame. "
  "Her knee and the implant are the middle of the frame; the rest of her is cut off above the waist.",
  light("The bay's window on the far wall, past the curtain", "the bed, her knee and the implant", "left", "flat grey daylight mixed with the ward's cool ceiling light", "the left", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no blood, no incision, no scalpel, no surgery in progress, no operating theatre, no scar, no strap product, no brace, "
                         "no plastic toy model, no skeleton, no X-ray, no writing other than the arrow, no readable name on the wrist band, no hospital logo, "
                         "no hand cut off at the frame edge, no bare glove-less hand", NOTEXT])]))

# HK1-02b v4 — another COURSE of physio: an NHS physiotherapy class (L-PHYSIO, INCIDENTAL), P-D1
B["HK1-02b"] = dict(model="nano_banana_2", refs=["P-PATIENT"], prompt="\n\n".join([S("CAM-LOCK"),
  angle("eye", "a three-quarter angle", "her on the exercise step"),
  focus("the nearest eye of the woman", "the room behind falls to a soft, recognisable shape"),
  "An NHS hospital physiotherapy gym on a weekday morning, a knee class in progress: a long room with a sprung blue floor, parallel bars along one wall, "
  "wall bars and a rack of coloured resistance bands, a row of plastic chairs, and three or four other older patients in their own clothes doing the same exercise on their own low steps behind her, soft. "
  "No posters with readable words, no logos.",
  "A snapshot from a phone held at eye height by someone standing across the room, not looking at the screen. " + P_FACE + " " + P_D1 +
  " She is doing a step-down exercise on a low grey aerobic step, one hand on the parallel bar beside her for balance, caught mid-movement: her weight on her right leg on the step, "
  "her LEFT foot lowering slowly towards the floor, her left knee trembling, her jaw set, her brow creased with the effort, eyes on her foot, mouth shut. "
  "A physiotherapist in a navy NHS-style tunic and trousers crouches beside her with one hand hovering near her left knee, watching it, a clipboard tucked under her arm with no readable writing.",
  light("The tall windows along the gym's far wall", "her", "left", "grey even daylight, the problem days, with the gym's ceiling panels on", "the left"),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no home, no living room, no front room, no smiling, no strap product, no brace, no readable words anywhere, "
                         "no NHS logo, no gym brand, no feet cut off, no crowd blocking her", NOTEXT])]))

# HK1-02c v4 — held beat (§9A): the strap held up in the kitchen, the overfull brace drawer soft behind; focus only on the strap
grip = dict(ps.HELD_GRIPS)["fingertips behind"]
B["HK1-02c"] = dict(model="nano_banana_pro", refs=["front.webp", "product_tq_left.jpg", "P2-P-KITCHEN v2", "P-PATIENT"], prompt="\n\n".join([S("CAM-LOCK"),
  angle("eye", "the front", "the strap in her hands"),
  focus("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The kitchen of the attached kitchen photograph: behind her hands, soft and out of focus, the old pine Welsh dresser with its top drawer hanging open and overflowing with old knee supports — "
  "black sleeves, beige wraps, a grey hinged brace with metal side bars — spilling over the drawer front, all blank and plain, blurred into soft shapes.",
  "A snapshot from a phone held at chest height close in front of her hands, not looking at the screen. "
  "Her two hands — a woman of sixty-nine, thin skin, soft lines across the knuckles, a plain gold wedding band, the cuffs of an oatmeal cable-knit cardigan over a cream roll-neck — "
  "hold her knee strap up towards the camera at chest height, square to the lens, filling the middle of the frame. " + ps.REF_PROD +
  " " + grip + ", both hands the same way, one near each end of the shell, never on the band, never on the chrome slides, never across the wordmark, the peaks and the notch fully visible. "
  "The strap is the only sharp thing in the picture: every weave of the band, the chevrons on the slides and the grey wordmark crisp, and everything behind it — the dresser, the drawer, "
  "the heap of old braces — falls away to soft, round blur.",
  light("The window over the sink on the room's west wall", "the strap and her hands", "right", "flat overcast daylight", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([ps.NEG_HELD_P, *NEG_BASE(), "no face in frame, no strap worn on a leg, no brace in her hands, no sharp background, no drawer in focus, "
                         "no deep focus, no packaging", NOTEXT.replace("anywhere", "anywhere except the stryde wordmark on the strap")])]))

REF = {"P-PATIENT": "02333782-0c9a-4696-b3f1-fcc7480fe8db", "P2-P-KITCHEN v2": "abc2c220-b0f0-43d2-b583-d22b5696225b",
       "front.webp": "c942d91d-718d-4723-b190-ad85186ac8d9", "product_tq_left.jpg": "4a56cffe-69bc-4f77-ac90-38258b124e65"}
out = {}
for k, b in B.items():
    txt = b["prompt"]; assert "[" not in txt, (k, txt[txt.index("["):txt.index("[")+80])
    out[k] = dict(model=b["model"], refs=b["refs"], ref_jobs=[REF[r] for r in b["refs"]], chars=len(txt), prompt=txt)
    (here / f"{k}.image.v4.prompt.txt").write_text(txt); print(f"{k:8s} {len(txt):5d}  {b['model']:15s} refs: {', '.join(b['refs'])}")
json.dump(out, open(here / "hooks_v4.json", "w"), indent=1)
json.dump([{"index": i, "params": {"model": v["model"], "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in v["ref_jobs"]], "prompt": v["prompt"]}} for i, v in enumerate(out.values())],
          open(here / "batch_v4.json", "w"), indent=1)
