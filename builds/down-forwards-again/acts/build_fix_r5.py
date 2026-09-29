#!/usr/bin/env python3
"""Step 7 · image Fix round 5 (2026-09-29 ~18:20 UTC). One new render per card; fixes at the source.
  MECH-14 the user sent the photo of the pad's inside (products/stryde/stryde_refs/inner_pad_user.png, Higgsfield media dca6d9b5…) → attached as the
          reference; the pad re-described from it (curved-hourglass pad, grooves fanning across it to its edges, dog-bone rib, polished slides)
  BR-04   the user sent the point (builds/down-forwards-again/refs/BR-04_point_ref.png, media 6a2715d9…): the finger points UP from below into the dip
          just under the kneecap, camera a little above the knee in front → attached as a pose/spot reference only (never the man in it)
  BR-22a2 "brolls of showing the results of using the strap" → the result: her, weeks on, stepping down her front step to go out, strapped leg straight
          (own story day P-A5b in work/wardrobe.py; act-map row now BR · L-P-DOOR · hip/three-quarter)
  BR-22b  "show the cheap COPIES" → the copies themselves: three near-copies tipped out on the kitchen table, bands stretched long and limp
Base prompts are the round-4 prompts (acts/<beat>.image.r4.prompt.txt); edits are exact replacements, asserted."""
import json, pathlib, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here.parent / "work"))
from wardrobe import wear
PAD_REF, POINT_REF = "dca6d9b5-4931-4114-b093-f6fd7f8930c8", "6a2715d9-de51-420d-844b-99abba716adb"
def edit(src, pairs):
    t = (here / src).read_text()
    for old, new in pairs:
        assert t.count(old) == 1, (src, old[:90]); t = t.replace(old, new)
    return t
F = {}
F["BR-04"] = ("BR-04.image.r4.prompt.txt", 7, [
 ("the lens at the height of her knee, level, straight in FRONT of her knee and square to it, close, so the knee fills the middle of the frame head-on — the kneecap facing the lens, not turned to either side.",
  "the lens a little above her knee, in FRONT of her, looking down along her bent leg at the front of the knee and the shin — the kneecap facing the lens, not turned to either side — exactly the camera angle of the attached pointing reference photograph."),
 ("A snapshot from a phone held at knee height by someone kneeling on the rug in front of her, facing her, not looking at the screen.",
  "A snapshot from a phone held a little above her knee by someone standing in front of her, facing her, not looking at the screen. The attached pointing reference photograph shows the exact pose and the exact spot: copy only where the fingertip presses and the camera angle — the woman, her clothes, her hands and her room stay as described here, never the man in that photograph."),
 ("comes straight down from above and presses its tip into the patellar tendon",
  "reaches in low beside her shin and points UP, its tip pressing into the patellar tendon"),
 ("no view from above, no top-down view,", "no view from directly overhead, no finger coming down from above, no man, no shorts,")])
F["MECH-14"] = ("MECH-14.image.r4.prompt.txt", 5, [
 ("The strap is the product of the attached reference image, seen from behind: the inside face of the shell. At each end of the long black shell sits a rectangular brushed chrome slide, the black coarse-knit band looped through it. Between the slides, the shell's back is smooth matte black, and set into it, filling most of it, a large soft mid-grey silicone pad with a thin black rim showing round it. The pad's outline: two broad rounded lobes, one at each end, joined by a narrower middle, and along ONE long side a deep smooth inward curve (behind the shell's notch), so the pad looks like a curved hourglass or a kidney-shaped peanut. Its whole surface is covered in fine raised grooves running in tight parallel curves that follow the pad's outline like contour lines on a map. Down the middle of the pad, lengthwise from one lobe to the other, runs one smooth raised rib with no grooves on it — a long rounded bar, thicker at both ends and slimmer in the middle, like a dog-bone. No wordmark shows on this side.",
  "The strap is seen from behind, its inside face exactly as in the attached inside-of-the-pad reference photograph: the matte black shell with a rectangular polished chrome slide at each end and the black coarse-knit band looped through each; the shell's outline pinched in at the middle, with a deep smooth inward curve along one long side; set into it, filling most of it, a soft mid-grey silicone pad in the same curved-hourglass shape — two broad rounded lobes joined by a narrower waist, the deep curve on one side — with a thin black rim showing round it. The pad's surface is covered in fine parallel grooves that fan round the pad, running across it out to its edges. Down its middle, lengthwise from one lobe to the other, runs one smooth raised rib with no grooves on it, shaped like a long dog-bone — rounded and thicker at both ends, slimmer in the middle. No wordmark shows on this side."),
 ("no ridges running straight across,", "no grooves on the central rib, no pad shape other than the reference photograph's,")])
F["BR-22a2"] = ("BR-19b.image.r4.prompt.txt", 3, [
 ("seen from the front of the woman coming down the stairs.", "seen from a three-quarter angle of the woman stepping down her front step."),
 ("FOCUS: everything is in sharp focus; everything from near to far stays sharp.",
  "FOCUS: she and the strap on her knee are in sharp focus; the street behind falls to a soft, recognisable shape."),
 ("The hall and the wide straight staircase of the attached property photograph, the dark turned banister on the open right side, the patterned runner with brass rods.",
  "Outside it now: the red-brick front of the house, her front door open behind her with the stained-glass panel and the hall's patterned runner glimpsed inside, one wide red-brick front step down to a short black-and-white tiled path, a low brick wall and a clipped privet hedge, a quiet street beyond."),
 ("A snapshot from a phone held at hip height by someone standing at the foot of the stairs, looking up the whole flight, not looking at the screen.",
  "A snapshot from a phone held at hip height by someone standing on the front path a few steps away, off to one side, not looking at the screen."),
 ("She wears a white cotton crew-neck t-shirt under an open light denim overshirt, a knee-length mustard-yellow A-line skirt with bare legs, navy canvas plimsolls, and reading glasses on a thin beaded cord round her neck.",
  wear("BR-22a2")),
 ("She is at the very TOP of the flight, just stepping off the landing to come DOWN her stairs facing forwards, easy and steady, both hands free at her sides and never touching the banister or the wall, caught in the moment her RIGHT foot reaches down for the first step while her LEFT leg stands straight on the top step taking her weight — the LEFT knee straight, facing the lens, so the strap on it shows full on; the whole flight of stairs between her and the lens.",
  "Weeks on, she is going out again: she has stepped out of her front door and is stepping down the front step onto the path, easy and steady, a cloth shopping bag over her right forearm, her left hand free at her side, nothing to hold and no need of it, caught in the moment her RIGHT foot reaches down onto the path while her LEFT leg stands straight on the step taking her weight — the LEFT knee straight, facing the lens, so the strap on it shows full on."),
 ("Her face is open and quietly surprised, eyes on the stairs ahead, mouth shut.", "Her face is easy and content, a small closed-mouth smile, eyes on the path ahead."),
 ("Her whole body from hair to plimsolls is in frame.", "Her whole body from hair to shoes is in frame."),
 ("The stained-glass panel in the front door, behind the phone lights her from the right of the frame, morning sun, a warm patch on the stairs, the after, so the face has a lit side toward the right",
  "Open late-spring sky over the street lights her from the left of the frame, bright morning sun, the after, so the face has a lit side toward the left"),
 ("no walking backwards, no gripping the rail, no hand on the banister, no hand on the rail, no hand touching the wall, no bottom of the stairs, no woman near the hall floor,",
  "no handrail, no hand on the door frame, no hand touching the wall, no indoor stairs, no hall interior around her,")])
F["BR-22b"] = ("BR-22b.image.r4.prompt.txt", 4, [
 ("the lens at hip height, looking up at the subject, seen from the front of her knee with a cheap copy strap on it.",
  "the lens above the table, looking down at the subject, seen from a three-quarter angle of the cheap copy straps on the kitchen table."),
 ("FOCUS: the foreground is in sharp focus;", "FOCUS: the copies are in sharp focus;"),
 ("The kitchen of the attached kitchen photograph, the terracotta-and-black tiled floor and the table legs soft behind.",
  "The kitchen of the attached kitchen photograph: the bare wooden kitchen table, the terracotta-and-black tiled floor soft below."),
 ("A snapshot from a phone held low by someone crouched on the kitchen floor in front of her, not looking at the screen. Her bare legs from just above the knees down, standing, facing the lens, the hem of a knee-length skirt at the top of the frame, flat shoes. On her LEFT knee: A cheap copy of the strap:",
  "A snapshot from a phone held above the table by someone standing beside it, not looking at the screen. Tipped out on the bare wooden kitchen table from a crumpled clear plastic bag: three cheap copy straps she bought and gave up on, lying in a loose heap. Each is a cheap copy of the strap:"),
 ("It sits on her LEFT knee where a strap goes — just below the kneecap — but it has stretched: it has slipped a finger's width lower than it should, tilted a little, its band slack and loose round the leg, a small gap opening between the shell and the skin at one side. It is one simple clean shape — one flat shell, one band, two small plastic buckles — lying naturally on the leg, every part of it in proportion, nothing bent out of shape.",
  "Their bands have stretched out of shape: long, limp and wavy, far longer than they should be, lying slack across the table like worn-out elastic, one band pulled so thin that the weave shows through, one hanging limp over the table edge. Each copy is one simple clean shape — one flat shell, one band, two small plastic buckles — every part of it in proportion, nothing bent out of shape."),
 ("lights the leg from the right of the frame", "lights the table and the copies from the right of the frame"),
 ("no copy at mid-shin, no copy at the ankle, no side view, no profile view, no face,", "no leg, no person, no hand, no face, no more than three copies,")])
REFS = {"BR-04": [POINT_REF, "d0eeaf2a-abad-4a79-a9da-624c5eef41a1", "02333782-0c9a-4696-b3f1-fcc7480fe8db"],
        "MECH-14": [PAD_REF, "d0eeaf2a-abad-4a79-a9da-624c5eef41a1"],
        "BR-22a2": ["c942d91d-718d-4723-b190-ad85186ac8d9", "793ca329-e4b3-49fd-943c-5e97bae5366d", "02333782-0c9a-4696-b3f1-fcc7480fe8db", "176c5c39-ac17-46c4-9e9b-2c06735dc0c8"],
        "BR-22b": ["abc2c220-b0f0-43d2-b583-d22b5696225b"]}
out = {}
for b, (src_, v, pairs) in F.items():
    txt = edit(src_, pairs); (here / f"{b}.image.r5.prompt.txt").write_text(txt)
    out[b] = dict(v=v, src=src_, model="nano_banana_pro", ref_jobs=REFS[b], chars=len(txt), prompt=txt); print(f"{b:8s} v{v} {len(txt):5d}")
json.dump(out, open(here / "fix_r5.json", "w"), indent=1)
json.dump([{"index": 600 + i, "params": {"model": o["model"], "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in o["ref_jobs"]], "prompt": o["prompt"]}} for i, o in enumerate(out.values())],
          open(here / "fix_r5_batch.json", "w"), ensure_ascii=False)
