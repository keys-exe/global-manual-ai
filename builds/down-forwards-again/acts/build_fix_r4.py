#!/usr/bin/env python3
"""Step 7 · image Fix round 4 (the user's board Fix notes, 2026-09-29 ~17:50 UTC). One new render per card; fixes at the source.
  BR-04  "she should be pointing at her patellar tendon and not the side of her knee" — two renders drifted to the side of the knee → a tight head-on close-up
         of the bent knee, the finger coming straight down onto the midline under the kneecap; nano_banana_pro for tighter placement
  BR-14b "product is too big" — SIZE_WORN alone let it spread → explicit slim size on the leg
  BR-19b "the knee that the strap is on should not be bent so the product is shown" → the strapped LEFT leg straight and bearing her weight, facing the lens;
         the RIGHT foot is the one stepping down
  BR-22a2 "should be a product broll" → a product close-up of the two straps; the lived-in still life (calendar, mug, book) dropped
  BR-22b "wrong placement and she should be facing in front" → her leg from the front, the copy on the knee where a strap goes, slipped a little, not at mid-shin
  MECH-14 "wrong inside" — the pad shape didn't match the user's photo → the photo described shape by shape (hourglass pad with the notch-side curve, contour
         grooves, bone-shaped central bar), the strap laid flat in her palm, back up, long axis across her hand
Base prompts are the round-3 prompts (acts/<beat>.image.r3.prompt.txt); edits are exact replacements, asserted."""
import json, pathlib, importlib.util
here = pathlib.Path(__file__).parent
ROOT = here.parents[2]
spec = importlib.util.spec_from_file_location("ps", ROOT / "products/stryde/stryde_product_sheet.py"); ps = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(ps)
except AssertionError: pass
SLIM = (" On the leg it is a small, slim strap: the shell is only about three centimetres tall — shorter than the kneecap — and hugs the front of the knee just below "
        "it; the band is a narrow strip round the leg. It looks light and discreet, never chunky, never a big block on the knee.")
def edit(src, pairs):
    t = (here / src).read_text()
    for old, new in pairs:
        assert t.count(old) == 1, (src, old[:90]); t = t.replace(old, new)
    return t
F = {}
F["BR-04"] = ("BR-04.image.r3.prompt.txt", 6, "nano_banana_pro", [
 ("the lens at the height of her knee, level, straight in FRONT of her, looking at the front of her bent knee and her hand.",
  "the lens at the height of her knee, level, straight in FRONT of her knee and square to it, close, so the knee fills the middle of the frame head-on — the kneecap facing the lens, not turned to either side."),
 ("is caught pressing its tip into the soft band of tendon BELOW her LEFT kneecap — in the CENTRE of the knee, on its midline, directly under the lowest point of the kneecap, two centimetres under its lower edge, between the kneecap and the bump of the shin bone, not to either side, the skin dimpling round the fingertip.",
  "comes straight down from above and presses its tip into the patellar tendon — the soft band directly BELOW the middle of her LEFT kneecap, in the dip between the kneecap's lowest point and the bump at the top of the shin bone, exactly on the same vertical line as the centre of the kneecap, the skin dimpling round the fingertip. Seen from the front, the kneecap sits directly above the fingertip like a cap above a stem; the finger is on the front of the knee, never on its side."),
 ("no finger on the inner or outer side of the knee,", "no finger on the inner or outer side of the knee, no finger on the side of the knee, no side view of the knee, no finger pointing sideways,")])
F["BR-14b"] = ("BR-14b.image.r3.prompt.txt", 2, "nano_banana_pro", [
 (" Her RIGHT knee is bare.", SLIM + " Her RIGHT knee is bare."),
 ("no face, no hand on the rail,", "no oversized strap, no chunky strap, no strap taller than the kneecap, no strap covering the whole knee, no face, no hand on the rail,")])
F["BR-19b"] = ("BR-19b.image.r3.prompt.txt", 3, "nano_banana_pro", [
 ("caught in the moment her LEFT foot lands on the first step down with the LEFT knee bending freely under her weight, her right foot still on the landing, the whole flight of stairs between her and the lens.",
  "caught in the moment her RIGHT foot reaches down for the first step while her LEFT leg stands straight on the top step taking her weight — the LEFT knee straight, facing the lens, so the strap on it shows full on; the whole flight of stairs between her and the lens."),
 ("no strap on the right knee,", "no bent left knee, no left knee hidden, no strap on the right knee,")])
F["BR-22b"] = ("BR-22b.image.r3.prompt.txt", 3, "nano_banana_pro", [
 ("seen from the side, in profile of a leg with a cheap copy strap.", "seen from the front of her knee with a cheap copy strap on it."),
 ("A snapshot from a phone held low by someone crouched on the kitchen floor, not looking at the screen. An adult's bare lower leg from the knee down, standing, a grey sock and a trainer. On it:",
  "A snapshot from a phone held low by someone crouched on the kitchen floor in front of her, not looking at the screen. Her bare legs from just above the knees down, standing, facing the lens, the hem of a knee-length skirt at the top of the frame, flat shoes. On her LEFT knee:"),
 ("The copy has stretched and slipped: it has sagged down off the kneecap to the middle of the shin, its band slack and loose round the calf.",
  "It sits on her LEFT knee where a strap goes — just below the kneecap — but it has stretched: it has slipped a finger's width lower than it should, tilted a little, its band slack and loose round the leg, a small gap opening between the shell and the skin at one side."),
 ("no face, no genuine strap,", "no copy at mid-shin, no copy at the ankle, no side view, no profile view, no face, no genuine strap,")])
F["MECH-14"] = ("MECH-14.image.r3.prompt.txt", 4, "nano_banana_pro", [
 ("holds her knee strap turned over, resting across her open upturned palm with the front face down on her palm and the inside facing up to the lens, fingers loosely curled at the shell's lower edge, the band draped over her hand, caught in the middle of one slow half turn.",
  "holds her knee strap turned over and laid flat across her open upturned palm, its long axis running across her hand from side to side, the front face down on her palm and the inside facing straight up to the lens, fingers loosely curled at one end."),
 ("the back of the shell: matte black, with a soft mid-grey silicone pad set into it that follows the shell's outline — wide at both ends, pinched in at the middle — its whole surface covered in fine raised ridges running in close, parallel curved lines that sweep round the pad like a fingerprint, and down its centre, along its length, one smooth raised bar, a rounded rib standing proud of the ridges. A brushed chrome slide sits at each end of the shell with the black coarse-knit band looped through it. No wordmark shows on this side.",
  "the inside face of the shell. At each end of the long black shell sits a rectangular brushed chrome slide, the black coarse-knit band looped through it. Between the slides, the shell's back is smooth matte black, and set into it, filling most of it, a large soft mid-grey silicone pad with a thin black rim showing round it. The pad's outline: two broad rounded lobes, one at each end, joined by a narrower middle, and along ONE long side a deep smooth inward curve (behind the shell's notch), so the pad looks like a curved hourglass or a kidney-shaped peanut. Its whole surface is covered in fine raised grooves running in tight parallel curves that follow the pad's outline like contour lines on a map. Down the middle of the pad, lengthwise from one lobe to the other, runs one smooth raised rib with no grooves on it — a long rounded bar, thicker at both ends and slimmer in the middle, like a dog-bone. No wordmark shows on this side."),
 ("no black pad, no smooth featureless pad,", "no black pad, no smooth featureless pad, no rectangular pad, no straight-sided pad, no ridges running straight across, no rib missing,")])
BR22A2 = (here / "BR-22a2.image.r3.prompt.txt").read_text()
F["BR-22a2"] = ("BR-22a2.image.r3.prompt.txt", 2, "nano_banana_pro", [
 ("the lens at the subject's eye height, level, seen from a three-quarter angle of the side table by the armchair.", "the lens at the subject's eye height, level, seen from a three-quarter angle of the two straps on the side table."),
 ("On the side table, weeks after they arrived, lie her two knee straps, side by side, front faces up, their bands in loose closed loops behind them — kept and lived with, the bands a little softened and creased from wear, the shells unmarked.",
  "A product close-up: on the bare dark-wood side table, her two knee straps lie side by side, front faces up and angled a little towards the lens, their bands in neat closed loops behind them, the two wordmarks readable — the straps are the whole subject, sharp in the middle of the frame, the table edge and the room soft around them."),
 (" Beside them: her reading glasses on their beaded cord, a half-drunk mug of tea and a paperback face down. Behind, soft on the wall: a plain paper wall calendar with most of the month's days crossed off in pen, its numbers too soft to read.", " Nothing else on the table."),
 ("each no bigger than the mug is wide.", "each about the width of a hand."),
 ("no box, no packaging,", "no calendar, no mug, no glasses, no book, no clutter, no box, no packaging,")])
REFS = {"BR-04": ["d0eeaf2a-abad-4a79-a9da-624c5eef41a1", "02333782-0c9a-4696-b3f1-fcc7480fe8db"],
        "BR-14b": ["c942d91d-718d-4723-b190-ad85186ac8d9", "2730a819-cf08-49a6-b5cd-01a086777dad", "176c5c39-ac17-46c4-9e9b-2c06735dc0c8"],
        "BR-19b": ["c942d91d-718d-4723-b190-ad85186ac8d9", "793ca329-e4b3-49fd-943c-5e97bae5366d", "02333782-0c9a-4696-b3f1-fcc7480fe8db", "176c5c39-ac17-46c4-9e9b-2c06735dc0c8"],
        "BR-22b": ["abc2c220-b0f0-43d2-b583-d22b5696225b"],
        "MECH-14": ["c942d91d-718d-4723-b190-ad85186ac8d9", "d0eeaf2a-abad-4a79-a9da-624c5eef41a1"],
        "BR-22a2": ["c942d91d-718d-4723-b190-ad85186ac8d9", "d0eeaf2a-abad-4a79-a9da-624c5eef41a1"]}
out = {}
for b, (src_, v, model, pairs) in F.items():
    txt = edit(src_, pairs); (here / f"{b}.image.r4.prompt.txt").write_text(txt)
    out[b] = dict(v=v, src=src_, model=model, ref_jobs=REFS[b], chars=len(txt), prompt=txt); print(f"{b:8s} v{v} {len(txt):5d} {model}")
json.dump(out, open(here / "fix_r4.json", "w"), indent=1)
json.dump([{"index": 500 + i, "params": {"model": o["model"], "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in o["ref_jobs"]], "prompt": o["prompt"]}} for i, o in enumerate(out.values())],
          open(here / "fix_r4_batch.json", "w"), ensure_ascii=False)
