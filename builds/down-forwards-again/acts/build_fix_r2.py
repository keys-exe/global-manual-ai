#!/usr/bin/env python3
"""Step 7 · image Fix round 2 (the user's board Fix notes, 2026-09-29 ~16:40 UTC). Each fix at the source of the fault, one new render per card.
  BR-04  "change the cameerr angle to her front cause the patellar tendon is not on the leg its below the knee" — v3 looked down from above, so the
         shin foreshortened away and the finger read as on the leg → the lens at knee height in FRONT of her, level with the bent knee
  BR-06  "remove the feet at the bottom of the image" — the phone-holder's shoes crept in at hip height → phone at chest height, nothing in the near foreground
  BR-11c "fix where she is sitting its it doesnt look real" — the knee floated with no body attached to the chair → wider, from the side: her whole seated body on the chair
  BR-16a "the product is a bit too big" / PR-12 "the prodtuct is too big" — the strap filled the frame and dwarfed the hand; the sheet's SIZE_HELD alone
         didn't hold it → wider framing (strap small in frame) + its real size in plain terms (about the width of the palm, ~10 cm)
  BR-17a "she sit not sitting on something" — no stair read under her → lower, side-front angle with the tread under her and the flight rising behind
  MECH-14 "i sent the insdie of the silicon pad" (read as: show the inside of the silicone pad) — v1 drew the strap as a plain band → the real strap shape,
         shell cut away in cross-section so its inner pad is seen pressing on the tendon (INNER_PAD from the Product Sheet)
Base prompts are the current versions; edits are exact replacements, asserted."""
import json, pathlib, importlib.util
here = pathlib.Path(__file__).parent
ROOT = here.parents[2]
spec = importlib.util.spec_from_file_location("ps", ROOT / "products/stryde/stryde_product_sheet.py"); ps = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(ps)
except AssertionError: pass
SMALL = (" In real life it is a small strap: the shell is about ten centimetres across — about the width of the palm of the hand holding it — and about "
         "three centimetres tall; it looks small and light in the hand, never bigger than the hand.")
def edit(src, pairs):
    t = (here / src).read_text()
    for old, new in pairs:
        assert t.count(old) == 1, (src, old[:90]); t = t.replace(old, new)
    return t
F = {}
F["BR-04"] = ("BR-04.image.v3.prompt.txt", 4, [
 ("the lens above head height, looking down at the subject, seen from the front of her knee and her hand.",
  "the lens at the height of her knee, level, straight in FRONT of her, looking at the front of her bent knee and her hand."),
 ("A snapshot from a phone held above her lap by someone looking straight down at her knee, not looking at the screen.",
  "A snapshot from a phone held at knee height by someone kneeling on the rug in front of her, facing her, not looking at the screen."),
 ("The bare knee fills the middle of the frame, seen from above and in front: the rounded kneecap in the centre of the picture, and below it the short stretch of bare skin down to the bump at the top of the shin —",
  "The bare knee fills the middle of the frame, seen straight from the front: the rounded kneecap in the upper middle of the picture, and directly below it, facing the lens, the short stretch of bare skin down to the bump at the top of the shin, the shin running straight down to the rug below —"),
 ("The front room of the attached front-room photograph, seen from above: the mustard armchair seat and the patterned rug soft around the knee.",
  "The front room of the attached front-room photograph: the mustard armchair she sits in and the patterned rug, soft behind and around her knee."),
 ("no straight leg, no thigh filling the frame,", "no straight leg, no thigh filling the frame, no view from above, no top-down view,")])
F["BR-06"] = ("BR-06.image.v3.prompt.txt", 4, [
 ("the lens at hip height, looking up at the subject,", "the lens at chest height, looking a little up at the subject,"),
 ("A snapshot from a phone held at hip height by someone standing in the hall at the foot of the stairs, off to the right, not looking at the screen.",
  "A snapshot from a phone held at chest height by someone standing a couple of metres back in the hall, off to the right, not looking at the screen. The bottom edge of the frame is the hall floorboards and the bottom stair — nothing in the near foreground."),
 ("no second staircase,", "no feet or shoes at the bottom of the frame, no photographer's feet, no legs in the foreground, no second staircase,")])
F["BR-11c"] = ("BR-11c.image.v2.prompt.txt", 3, [
 ("the lens above head height, looking down at the subject, seen from a three-quarter angle of her knee and her hand.",
  "the lens at the subject's eye height, level, seen from the side, in profile of the woman sitting at the table."),
 ("A snapshot from a phone held above her lap by someone looking down, not looking at the screen. She sits on a spindle-back kitchen chair,",
  "A snapshot from a phone held at eye height by someone standing a couple of metres away in the kitchen, not looking at the screen. Her whole seated body is in frame, side-on: "
  "she sits back on a spindle-back kitchen chair pulled out from the pine table, her bottom on the seat, her back against the spindles, her LEFT foot flat on the tiled floor and the left knee bent at a right angle over the edge of the seat — hip, thigh, knee, shin and foot one continuous leg. She wears a cornflower-blue linen shirt with the sleeves rolled, and"),
 ("her wide-leg cream cotton trouser leg rolled up above her LEFT knee, the bare knee in the middle of the frame:", "her wide-leg cream cotton trouser leg rolled up above her LEFT knee, the bare knee clear:"),
 ("A small plain white tube with no label lies on the table edge beside her, its cap off.", "A small plain white tube with no label lies on the table beside her, its cap off. Her face is turned down to the knee, soft, calm, mouth shut."),
 ("no face, no strap product,", "no floating knee, no leg detached from her body, no knee without a body, no impossible pose, no strap product,")])
F["BR-16a"] = ("BR-16a.image.prompt.txt", 2, [
 ("the lens at the subject's eye height, level, seen from a three-quarter angle of the surgeon.", "the lens at the subject's eye height, level, seen from a three-quarter angle of the surgeon at his desk."),
 ("holds a knee strap up at chest height between them, looking at it with a small approving nod, mouth closed.",
  "holds a knee strap up at chest height between them, looking at it with a small approving nod, mouth closed. His head, chest and both hands are in frame; the strap is a small object in his hand, not the subject of the frame."),
 ("the band is a little wider than the thumb.", "the band is a little wider than the thumb." + SMALL),
 ("no strap on a leg,", "no oversized strap, no strap bigger than his hand, no strap filling the frame, no strap on a leg,")])
F["PR-12"] = ("PR-12.image.v2.prompt.txt", 3, [
 ("holds her knee strap up into the window light, sharp and filling the middle of the frame, its front face square to the lens.",
  "holds her knee strap up into the window light at arm's length, its front face square to the lens; her hand, wrist and forearm and the kitchen around them are in frame, the strap a small object in the middle of the picture, taking up about a quarter of the frame's width."),
 ("the band is a little wider than the thumb.", "the band is a little wider than the thumb." + SMALL),
 ("no strap on a leg,", "no oversized strap, no strap bigger than her hand, no strap filling the frame, no close-up macro, no strap on a leg,")])
F["BR-17a"] = ("BR-17a.image.v2.prompt.txt", 3, [
 ("the lens above head height, looking down at the subject, seen from a three-quarter angle of her left leg and the strap.",
  "the lens at hip height, looking up at the subject, seen from a three-quarter angle from the front of the woman sitting on the bottom stair."),
 ("A snapshot from a phone held above her by someone standing in the hall, looking down, not looking at the screen. The woman of sixty-nine from the attached reference sheet sits on the bottom stair,",
  "A snapshot from a phone held at hip height by someone crouched in the hall in front of her, off to one side, not looking at the screen. The woman of sixty-nine from the attached reference sheet sits on the second tread of her staircase — her bottom on the carpeted tread with its patterned runner and brass rod, the next steps and the dark turned banister rising behind her, her right hand free — "),
 ("no skirt,", "no floating seat, no chair, no sitting on nothing, no stairs missing under her, no skirt,")])
# The user sent the real inside of the pad (chat, 2026-09-29 ~16:50 UTC: "this ist he back of the silicon pad the inside"); it overrides the Product Sheet's
# INNER_PAD (plain smooth black). Described from that photo:
PAD = ("A soft mid-grey silicone pad set into the black back of the shell and following its outline — wide at both ends, pinched in at the middle — its whole surface "
       "covered in fine raised ridges running in close, parallel curved lines that sweep round the pad like a fingerprint, and down its centre, along its length, one "
       "smooth raised bar, a rounded rib standing proud of the ridges — the part that presses on the tendon. A brushed chrome slide sits at each end of the shell, the black knit band looped through.")
F["MECH-14"] = ("MECH-14.image.prompt.txt", 2, [
 ("Around the leg, directly below the kneecap, sits a slim matte-black strap drawn as a smooth dark translucent band, its inner silicone pad pressing on the patellar tendon only — one band as wide as a thumb, just under the kneecap, never crossing the joint.",
  "Around the leg, directly below the kneecap, sits the knee strap in its real shape — a matte-black shell across the front of the knee, its top edge rising into two pointed peaks either side of a notch that cups the underside of the kneecap, a brushed chrome slide at each side, the black knit band running round behind the leg — "
  "drawn as a CUTAWAY: the front of the shell is sliced open like a cross-section, so the viewer sees inside it. Inside the shell, the SILICONE PAD: " + PAD[0].lower() + PAD[1:] +
  " Its smooth central bar presses into the patellar tendon just under the kneecap, the tendon dimpled a little under it. The pad presses on that one band only — about as wide as a thumb — and never crosses the joint."),
 ("no brace covering the joint,", "no plain band, no strap drawn as a simple ring, no pad hidden inside a closed shell, no black pad, no smooth featureless pad, no text on the pad, no brace covering the joint,")])
REF = {"BR-04": ["d0eeaf2a-abad-4a79-a9da-624c5eef41a1", "02333782-0c9a-4696-b3f1-fcc7480fe8db"],
       "BR-06": ["176c5c39-ac17-46c4-9e9b-2c06735dc0c8", "02333782-0c9a-4696-b3f1-fcc7480fe8db"],
       "BR-11c": ["abc2c220-b0f0-43d2-b583-d22b5696225b", "02333782-0c9a-4696-b3f1-fcc7480fe8db"],
       "BR-16a": ["c942d91d-718d-4723-b190-ad85186ac8d9", "4a56cffe-69bc-4f77-ac90-38258b124e65"],
       "PR-12": ["c942d91d-718d-4723-b190-ad85186ac8d9", "4a56cffe-69bc-4f77-ac90-38258b124e65", "abc2c220-b0f0-43d2-b583-d22b5696225b"],
       "BR-17a": ["c942d91d-718d-4723-b190-ad85186ac8d9", "793ca329-e4b3-49fd-943c-5e97bae5366d", "02333782-0c9a-4696-b3f1-fcc7480fe8db", "176c5c39-ac17-46c4-9e9b-2c06735dc0c8"],
       "MECH-14": ["c942d91d-718d-4723-b190-ad85186ac8d9"]}
MODEL = {"BR-16a": "nano_banana_pro", "PR-12": "nano_banana_pro", "BR-17a": "nano_banana_pro"}
out = {}
for b, (src, v, pairs) in F.items():
    txt = edit(src, pairs); (here / f"{b}.image.v{v}.prompt.txt").write_text(txt)
    out[b] = dict(v=v, src=src, model=MODEL.get(b, "nano_banana_2"), ref_jobs=REF[b], chars=len(txt), prompt=txt)
    print(f"{b:8s} v{v} {len(txt):5d} {out[b]['model']}")
json.dump(out, open(here / "fix_r2.json", "w"), indent=1)
json.dump([{"index": 300 + i, "params": {"model": o["model"], "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in o["ref_jobs"]], "prompt": o["prompt"]}} for i, o in enumerate(out.values())],
          open(here / "fix_r2_batch.json", "w"), ensure_ascii=False)
