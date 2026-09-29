#!/usr/bin/env python3
"""Step 7 · image Fix round 3 + the three new body B-rolls (the user, 2026-09-29 ~17:10 UTC).
Board Fix notes:
  BR-04  "should be at the center not the side, its right under that knee cap"      → fingertip on the knee's midline, directly under the kneecap's lowest point
  BR-16a "still too big the product fix it"                                          → waist-up framing, strap held low by the life-size knee model and sized against it
  BR-19b "she should be from the top going down and her hands will never touch the hand rails" → at the top of the flight stepping down, hands free
  BR-22b "fix the strap so it doesnt look distorted"                                 → one simple flat copy shape; the twist/gap that warped it removed
  BR-23  "she should be from the top of the stairs going down"                       → at the top of the flight stepping down
  MECH-14 "no need an anatomy here you can just show the inside  also this should not be 1 broll that script line is way too long for 1 broll only"
         → MECH-14 = the inside of the pad in her hand (the user's pad photo, described); BR-14b carries the second sentence
Chat: PR-22a's line → three B-rolls: PR-22a (two straps, done) · BR-22a2 "Sixty days, and you keep the straps." · BR-22a3 "From the Stryde site."
Fixes edit the current prompt (exact replacements, asserted); new beats are written from the same shared strings as build_acts2_5.py.
Outputs acts/<beat>.image.r3.prompt.txt, fix_r3.json, fix_r3_batch.json."""
import sys, json, pathlib, importlib.util
here = pathlib.Path(__file__).parent
hk = here.parent / "hooks" / "build_hooks.py"
src = hk.read_text()
exec(compile(src[:src.index("\nB = {}")].replace("__file__", repr(str(hk))), str(hk), "exec"))
spec = importlib.util.spec_from_file_location("ps", ROOT / "products/stryde/stryde_product_sheet.py"); ps = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(ps)
except AssertionError: pass
sys.path.insert(0, str(here.parent / "work")); from wardrobe import wear
WM = NOTEXT.replace("anywhere", "anywhere except the stryde wordmark on the strap")
GRIP = dict(ps.HELD_GRIPS)["open palm"]
SMALL = (" In real life it is a small strap: the shell is about ten centimetres across — about the width of the palm of the hand holding it — and about "
         "three centimetres tall; it looks small and light in the hand, never bigger than the hand.")
# the user's photo of the pad's inside (chat, 2026-09-29), described — overrides the Product Sheet's INNER_PAD for this build
PAD = ("the back of the shell: matte black, with a soft mid-grey silicone pad set into it that follows the shell's outline — wide at both ends, pinched in at the "
       "middle — its whole surface covered in fine raised ridges running in close, parallel curved lines that sweep round the pad like a fingerprint, and down its "
       "centre, along its length, one smooth raised bar, a rounded rib standing proud of the ridges. A brushed chrome slide sits at each end of the shell with the "
       "black coarse-knit band looped through it. No wordmark shows on this side.")
def edit(src, pairs):
    t = (here / src).read_text()
    for old, new in pairs:
        assert t.count(old) == 1, (src, old[:90]); t = t.replace(old, new)
    return t
F, NEW = {}, {}
F["BR-04"] = ("BR-04.image.v4.prompt.txt", 5, [
 ("is caught pressing its tip into the soft band of tendon BELOW her LEFT kneecap — two centimetres under the kneecap's lower edge, between the kneecap and the bump of the shin bone,",
  "is caught pressing its tip into the soft band of tendon BELOW her LEFT kneecap — in the CENTRE of the knee, on its midline, directly under the lowest point of the kneecap, "
  "two centimetres under its lower edge, between the kneecap and the bump of the shin bone, not to either side,"),
 ("no finger on the thigh,", "no finger on the thigh, no finger to the side of the knee, no finger on the inner or outer side of the knee, no finger off-centre,")])
F["BR-16a"] = ("BR-16a.image.v2.prompt.txt", 3, [
 ("the lens at the subject's eye height, level, seen from a three-quarter angle of the surgeon at his desk.",
  "the lens at the subject's eye height, level, seen from a three-quarter angle of the surgeon at his desk, from a little further back."),
 ("sits at the desk beside the knee model and holds a knee strap up at chest height between them, looking at it with a small approving nod, mouth closed. His head, chest and both hands are in frame; the strap is a small object in his hand, not the subject of the frame.",
  "sits at the desk beside the life-size anatomical knee model and holds a knee strap low in front of him at desk height, right next to the model's knee, looking at it with a small approving nod, mouth closed. "
  "He is framed from the waist up with the desk, the knee model and the window around him; the strap is a small object in his hand, the same width as the model's knee — never wider than his four fingers held together."),
 ("no oversized strap,", "no strap held up to the camera, no strap at chest height, no strap in the foreground, no strap wider than the knee model's knee, no oversized strap,")])
F["BR-19b"] = ("BR-19b.image.v2.prompt.txt", 2, [
 ("A snapshot from a phone held at hip height by someone standing at the foot of the stairs, not looking at the screen.",
  "A snapshot from a phone held at hip height by someone standing at the foot of the stairs, looking up the whole flight, not looking at the screen."),
 ("She is coming DOWN her stairs facing forwards, five steps from the bottom, easy and steady, one hand resting light on the banister, caught in the moment her LEFT foot lands on the tread below with the LEFT knee bending freely under her weight, her right foot still on the step above.",
  "She is at the very TOP of the flight, just stepping off the landing to come DOWN her stairs facing forwards, easy and steady, both hands free at her sides and never touching the banister or the wall, "
  "caught in the moment her LEFT foot lands on the first step down with the LEFT knee bending freely under her weight, her right foot still on the landing, the whole flight of stairs between her and the lens."),
 ("no gripping the rail,", "no gripping the rail, no hand on the banister, no hand on the rail, no hand touching the wall, no bottom of the stairs, no woman near the hall floor,")])
F["BR-22b"] = ("BR-22b.image.prompt.txt", 2, [
 ("The copy has stretched and slipped: it has sagged down off the kneecap to the middle of the shin, the band loose and baggy round the calf, one end twisted, gapping away from the skin.",
  "The copy has stretched and slipped: it has sagged down off the kneecap to the middle of the shin, its band slack and loose round the calf. It is one simple clean shape — one flat shell, one band, "
  "two small plastic buckles — lying naturally on the leg, every part of it in proportion, nothing bent out of shape."),
 ("no face, no genuine strap,", "no warped shell, no melted plastic, no distorted strap, no twisted band, no strap folding in on itself, no extra buckles, no face, no genuine strap,")])
F["BR-23"] = ("BR-23.image.v2.prompt.txt", 2, [
 ("A snapshot from a phone held at hip height by someone standing at the foot of the stairs, off to one side, not looking at the screen.",
  "A snapshot from a phone held at hip height by someone standing at the foot of the stairs, off to one side, looking up the whole flight, not looking at the screen."),
 ("She is coming DOWN her stairs facing forwards, four steps from the bottom, light and easy,",
  "She is at the very TOP of the flight, just stepping off the landing to come DOWN her stairs facing forwards, light and easy, the whole flight of stairs between her and the lens,"),
 ("caught in the moment her LEFT foot lands on the tread below with the LEFT knee bending freely,", "caught in the moment her LEFT foot lands on the first step down with the LEFT knee bending freely,"),
 ("no hand on the rail,", "no hand on the rail, no bottom of the stairs, no woman near the hall floor,")])
# ── MECH-14 (new brief) — the inside of the pad, in her hand. P-A2 (jade short-sleeved blouse), front room.
NEW["MECH-14"] = dict(v=3, model="nano_banana_pro", refs=["c942d91d-718d-4723-b190-ad85186ac8d9", "d0eeaf2a-abad-4a79-a9da-624c5eef41a1"], body=[S("CAM-LOCK"),
  angle("high", "a three-quarter angle", "the strap turned over in her hand"),
  focus("the product", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The front room of the attached front-room photograph, the mustard armchair and the patterned rug soft below.",
  "A snapshot from a phone held above her hand by someone standing beside her, looking down, not looking at the screen. An older woman's hand — thin skin, a plain gold wedding band, "
  "the short jade-green sleeve of her blouse at the top of the frame — holds her knee strap turned over, resting across her open upturned palm with the front face down on her palm and the inside facing up to the lens, fingers loosely curled at the shell's lower edge, the band draped over her hand, caught in the middle of one slow half turn. The strap is the product of the attached reference image, seen from behind: " + PAD + SMALL +
  " The grey pad and its smooth central bar are the sharpest thing in the frame.",
  light("The bay window on the room's east wall", "her hand and the strap", "left", "bright morning sun through the net curtains, the after", "the left", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join(["no anatomy, no x-ray, no bones, no black pad, no smooth featureless pad, no text on the pad, no wordmark on the back, no oversized strap, no strap bigger than her hand",
                         "no second strap, no strap on a leg, no packaging", *NEG_BASE(), "no face", NOTEXT])])
# ── BR-14b — "The weight gets caught and moved off the worn part before it reaches the joint." P-A2, the hall stairs, strap VISIBLE, hands free.
NEW["BR-14b"] = dict(v=1, model="nano_banana_pro", refs=["c942d91d-718d-4723-b190-ad85186ac8d9", "2730a819-cf08-49a6-b5cd-01a086777dad", "176c5c39-ac17-46c4-9e9b-2c06735dc0c8"], body=[S("CAM-LOCK"),
  angle("low", "a three-quarter angle", "her left leg stepping down the stairs"),
  focus("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The hall and the wide straight staircase of the attached property photograph, the patterned runner with brass rods, morning sun through the front-door glass.",
  "A snapshot from a phone held low by someone crouched at the foot of the stairs, off to one side, not looking at the screen. Only her legs from the hem of her knee-length "
  "stone-coloured cotton skirt down, bare legs, white canvas plimsolls: she is coming DOWN her stairs facing forwards, caught in the moment her LEFT foot lands flat on the tread below "
  "and the LEFT knee bends easily under her weight, her right foot still on the step above; her hands are out of frame, nowhere near the banister. On her LEFT knee: " + ps.REF_PROD + " " +
  ps.fill(ps.PLACE_LOCK_C, "left") + " " + ps.PLACE_PROFILE + " " + ps.SIZE_WORN + " " + ps.LEG_SKIN + " Her RIGHT knee is bare.",
  light("The stained-glass panel in the front door", "her legs and the strap", "right", "morning sun through the door glass, the after", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([ps.fill(ps.NEG_PLACE, "left"), ps.NEG_WORDMARK, *NEG_BASE(), "no face, no hand on the rail, no trousers, no strap on the right knee, no feet cut off, no anatomy", WM])])
# ── BR-22a2 — "Sixty days, and you keep the straps." Still life, weeks later: the two straps kept by her armchair; 60-day seal added in the edit (EG06).
NEW["BR-22a2"] = dict(v=1, model="nano_banana_pro", refs=["c942d91d-718d-4723-b190-ad85186ac8d9", "d0eeaf2a-abad-4a79-a9da-624c5eef41a1"], body=[S("CAM-LOCK"),
  angle("eye", "a three-quarter angle", "the side table by the armchair"),
  focus("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The front room of the attached front-room photograph: the small dark-wood side table beside the mustard armchair, the bay window behind.",
  "A snapshot from a phone held at table height by someone sitting in the armchair, not looking at the screen. On the side table, weeks after they arrived, lie her two knee straps, "
  "side by side, front faces up, their bands in loose closed loops behind them — kept and lived with, the bands a little softened and creased from wear, the shells unmarked. "
  "Each is the product exactly as in the attached reference image — " + ps.REF_PROD.split("— ", 1)[1] + " Beside them: her reading glasses on their beaded cord, a half-drunk mug of tea "
  "and a paperback face down. Behind, soft on the wall: a plain paper wall calendar with most of the month's days crossed off in pen, its numbers too soft to read." + SMALL.replace("in the hand, never bigger than the hand", "on the table, each no bigger than the mug is wide"),
  light("The bay window on the room's east wall", "the table and the straps", "left", "bright morning sun through the net curtains, the after", "the left", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join(["no box, no packaging, no third strap, no single strap, no person, no readable dates or numbers on the calendar, no oversized straps", ps.NEG_WORDMARK, *NEG_BASE(), WM])])
# ── BR-22a3 — "From the Stryde site." Her phone on the Stryde site; the real site screen is laid over in the edit, so the screen stays soft and wordless here.
NEW["BR-22a3"] = dict(v=1, model="nano_banana_pro", refs=["c942d91d-718d-4723-b190-ad85186ac8d9", "abc2c220-b0f0-43d2-b583-d22b5696225b"], body=[S("CAM-LOCK"),
  angle("high", "a three-quarter angle", "her hand and phone", ", looking past her shoulder, soft in the near foreground"),
  focus("the hands and what they hold", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The kitchen of the attached kitchen photograph, the pine table below her hand.",
  "A snapshot from a phone held over her shoulder by someone standing behind her chair, not looking at the screen. She sits at the pine kitchen table; her right hand — thin skin, "
  "a plain gold wedding band, the cuff of a lilac cotton shirt — holds her own phone in portrait, thumb on the glass mid-scroll. On its bright screen: a clean white shop page with a large "
  "photograph of one black knee strap — the product of the attached reference image, front face on — above soft grey blocks where the words and buttons would be, nothing on the screen readable. "
  "A mug of tea on the table beside the phone.",
  light("The window over the sink on the room's west wall", "her hand and the phone", "right", "brighter daylight, still indirect, the after", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join(["no readable text on the screen, no logos on the screen, no prices, no buttons with words, no second phone, no laptop, no face", *NEG_BASE(), NOTEXT])])
REFS = {"BR-04": ["d0eeaf2a-abad-4a79-a9da-624c5eef41a1", "02333782-0c9a-4696-b3f1-fcc7480fe8db"],
        "BR-16a": ["c942d91d-718d-4723-b190-ad85186ac8d9", "4a56cffe-69bc-4f77-ac90-38258b124e65"],
        "BR-19b": ["c942d91d-718d-4723-b190-ad85186ac8d9", "793ca329-e4b3-49fd-943c-5e97bae5366d", "02333782-0c9a-4696-b3f1-fcc7480fe8db", "176c5c39-ac17-46c4-9e9b-2c06735dc0c8"],
        "BR-22b": ["abc2c220-b0f0-43d2-b583-d22b5696225b"],
        "BR-23": ["c942d91d-718d-4723-b190-ad85186ac8d9", "793ca329-e4b3-49fd-943c-5e97bae5366d", "02333782-0c9a-4696-b3f1-fcc7480fe8db", "176c5c39-ac17-46c4-9e9b-2c06735dc0c8"]}
MODEL = {"BR-04": "nano_banana_2", "BR-16a": "nano_banana_pro", "BR-19b": "nano_banana_pro", "BR-22b": "nano_banana_pro", "BR-23": "nano_banana_pro"}
out = {}
for b, (src_, v, pairs) in F.items():
    txt = edit(src_, pairs); out[b] = dict(v=v, src=src_, model=MODEL[b], ref_jobs=REFS[b], prompt=txt)
for b, n in NEW.items():
    txt = "\n\n".join(n["body"]); assert "[" not in txt, (b, txt[txt.index("["):txt.index("[") + 80])
    out[b] = dict(v=n["v"], src="new", model=n["model"], ref_jobs=n["refs"], prompt=txt)
for b, o in out.items():
    o["chars"] = len(o["prompt"]); (here / f"{b}.image.r3.prompt.txt").write_text(o["prompt"]); print(f"{b:8s} v{o['v']} {o['chars']:5d} {o['model']}")
json.dump(out, open(here / "fix_r3.json", "w"), indent=1)
json.dump([{"index": 400 + i, "params": {"model": o["model"], "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in o["ref_jobs"]], "prompt": o["prompt"]}} for i, o in enumerate(out.values())],
          open(here / "fix_r3_batch.json", "w"), ensure_ascii=False)
