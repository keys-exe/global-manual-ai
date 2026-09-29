#!/usr/bin/env python3
"""Step 7 · image Fix round 1 (the user's board Fix notes, 2026-09-29). Each fix is made at the source of the fault, one new render per card.
  BR-02  "the xray is floating"            — v1 held the film in the air in front of the blinds → the film hangs on a wall X-ray viewer clip, flat against the glass
  BR-04  "the patellar tendon and not the leg its under the knee cap not above" — v2 pressed the thigh (the knee sat at the frame top, leg straight) →
         knee bent at a right angle, the kneecap in the middle of the frame, fingertip on the tendon below it
  BR-05a "the glasses are at the back and she should show strugging going up" — the cord swung round to her back; she climbed easily →
         glasses on her nose (reading the post), the climb is hard: both hands hauling on the banister, one step at a time, three-quarter back so the strain shows
  BR-06  "distorted location fix this"     — the landing-down view invented a second flight and a gallery → the one straight flight of the plate, seen from the hall
  BR-09b "fix they are so many"            — the FOCUS line ("the woman in the foreground") produced a second woman → exactly one person, focus on the garden
  MECH-03 "it should be the patellar tendon and not the lknee cap" — the glow sat on the patella → the kneecap named and kept unlit, the band placed below it
Base prompts are the current versions (acts/<beat>.image[.v2].prompt.txt); edits are exact replacements, asserted."""
import json, pathlib
here = pathlib.Path(__file__).parent
def edit(src, pairs):
    t = (here / src).read_text()
    for old, new in pairs:
        assert t.count(old) == 1, (src, old[:80]); t = t.replace(old, new)
    return t
F = {}
F["BR-02"] = ("BR-02.image.prompt.txt", 2, [
 ("are caught pressing a grey-and-black knee X-ray film flat against the window glass, the film big in the foreground, its top edge just sliding under a small clip, the daylight coming through it:",
  "are caught pushing the top edge of a grey-and-black knee X-ray film into the steel spring clip of a plain wall-mounted X-ray viewer beside the window — a flat white "
  "light panel screwed to the wall, switched off, lit only by the window. The film lies flat against the panel's frosted face along its whole surface, touching it edge to edge, "
  "held by the clip at the top and his fingertips at the bottom corners, nothing between film and panel; the film big in the foreground:"),
 ("no face, no lightbox, no glowing screen,", "no face, no film in mid-air, no film held away from the panel, no gap behind the film, no floating film, no panel glowing brightly,")])
F["BR-04"] = ("BR-04.image.v2.prompt.txt", 3, [
 ("She sits in the mustard armchair, the hem of her camel corduroy skirt pushed back above her LEFT knee with her left hand, the bare knee filling the middle of the frame: pale skin, a little swollen, "
  "fine creases, a few faint thread veins.",
  "She sits in the mustard armchair with her LEFT knee bent at a right angle, the foot flat on the rug, the hem of her camel corduroy skirt pushed back a hand's width above the knee with her left hand. "
  "The bare knee fills the middle of the frame, seen from above and in front: the rounded kneecap in the centre of the picture, and below it the short stretch of bare skin down to the bump at the top of the shin — "
  "pale skin, a little swollen, fine creases, a few faint thread veins."),
 ("is caught pressing into the soft spot just below her LEFT kneecap, two centimetres under its lower edge, the skin dimpling round the fingertip. The kneecap's outline reads clearly above the finger.",
  "is caught pressing its tip into the soft band of tendon BELOW her LEFT kneecap — two centimetres under the kneecap's lower edge, between the kneecap and the bump of the shin bone, "
  "the skin dimpling round the fingertip. The whole kneecap reads clearly ABOVE the fingertip; the finger is under the kneecap, never on the thigh, never above the knee."),
 ("no finger on the kneecap itself,", "no finger on the kneecap itself, no finger on the thigh, no finger above the kneecap, no straight leg, no thigh filling the frame,")])
F["BR-05a"] = ("BR-05a.image.v2.prompt.txt", 3, [
 ("seen from behind of the woman on the stairs.", "seen from a three-quarter angle from behind of the woman on the stairs."),
 ("seen from behind. She wears", "seen from behind and a little to the side, her face in profile. She wears"),
 ("and reading glasses on a thin beaded cord round her neck.", "and her reading glasses on her nose, their thin beaded cord looping down either side of her face to the front of her collar."),
 ("caught in the middle of one steady step: her right foot planted on the next tread, her left foot just lifting off the one below, her right hand sliding up the banister rail, her body upright and easy.",
  "struggling, one step at a time: both hands clamped on the banister rail, hauling herself up, her body bent forward over the rail, her right foot planted on the next tread "
  "and the LEFT leg dragging behind, stiff, its foot only just leaving the step below; her jaw set, lips pressed, a pause in the middle of the climb."),
 ("no face towards the camera,", "no face towards the camera, no glasses cord down her back, no glasses hanging behind her, no easy stride, no upright easy posture,")])
F["BR-06"] = ("BR-06.image.v2.prompt.txt", 3, [
 ("the lens above head height, looking down at the subject, seen from a three-quarter angle from behind of the woman on the stairs.",
  "the lens at hip height, looking up at the subject, seen from a three-quarter angle from behind of the woman on the stairs."),
 ("The hall and the wide straight staircase of the attached property photograph, seen from the landing looking down: the stairs fall away along the left-hand wall, the dark turned banister on the open right side, the patterned runner with brass rods, the hall floor far below.",
  "The hall and the wide straight staircase of the attached property photograph, exactly as it stands there: ONE straight flight rising along the left-hand wall, the dark turned banister on the open right side, "
  "the patterned runner with brass rods, the landing window at the top. Nothing else: no second flight, no gallery, no second banister."),
 ("A snapshot from a phone held by someone standing on the landing at the top of the stairs, looking down, not looking at the screen.",
  "A snapshot from a phone held at hip height by someone standing in the hall at the foot of the stairs, off to the right, not looking at the screen."),
 ("three steps below the landing,", "four steps above the hall floor,"),
 ("The tall landing window beside the phone lights her", "The tall landing window at the top of the stairs lights her"),
 ("the rest of the stairs dropping away below her.", "the flight rising behind her to the landing."),
 ("no facing forwards,", "no second staircase, no gallery landing, no extra banisters, no bent or broken stair geometry, no facing forwards,")])
F["BR-09b"] = ("BR-09b.image.v2.prompt.txt", 3, [
 ("the woman in the foreground stays readable, a touch soft.", "she stays readable in the middle of the room, a touch soft."),
 ("A snapshot from a phone held at eye height by someone standing in the kitchen behind her,", "A snapshot from a phone held at eye height by someone standing well back in the kitchen doorway behind her,"),
 ("Through the glass, sharp:", "She is the only person in the kitchen — one woman, once. Through the glass, sharp:"),
 ("no second person,", "no second person, no second woman, no duplicate of her, no one in the foreground, no people in the garden,")])
F["MECH-03"] = ("MECH-03.image.prompt.txt", 2, [
 ("The glow is one tight, bright spot on the patellar tendon just below the kneecap,",
  "WHERE THE GLOW IS: the kneecap is the small rounded bone at the front of the knee — it stays plain unlit ivory like the other bones. The glow starts a thumb's width BELOW the kneecap's lower tip "
  "and sits on the short cord that runs from there down to the bump at the top of the shin bone — that cord, the patellar tendon, is the only thing that glows. The glow is one tight, bright spot on that tendon,"),
 ("no leader lines,", "no glow on the kneecap, no red on the patella, no glow behind or above the kneecap, no glow at the joint line, no leader lines,")])
out = {}
REF = {"BR-02": ["757817ea-6840-487c-879c-1b0310e137b2", "b17f293d-306f-406c-b145-029402a1c074"],
       "BR-04": ["d0eeaf2a-abad-4a79-a9da-624c5eef41a1", "02333782-0c9a-4696-b3f1-fcc7480fe8db"],
       "BR-05a": ["176c5c39-ac17-46c4-9e9b-2c06735dc0c8", "02333782-0c9a-4696-b3f1-fcc7480fe8db"],
       "BR-06": ["176c5c39-ac17-46c4-9e9b-2c06735dc0c8", "02333782-0c9a-4696-b3f1-fcc7480fe8db"],
       "BR-09b": ["abc2c220-b0f0-43d2-b583-d22b5696225b", "02333782-0c9a-4696-b3f1-fcc7480fe8db"], "MECH-03": []}
for b, (src, v, pairs) in F.items():
    txt = edit(src, pairs); (here / f"{b}.image.v{v}.prompt.txt").write_text(txt)
    out[b] = dict(v=v, src=src, model="nano_banana_2", ref_jobs=REF[b], chars=len(txt), prompt=txt)
    print(f"{b:8s} v{v} {len(txt):5d}")
json.dump(out, open(here / "fix_r1.json", "w"), indent=1)
json.dump([{"index": 200 + i, "params": {"model": "nano_banana_2", "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in o["ref_jobs"]], "prompt": o["prompt"]}} for i, o in enumerate(out.values())],
          open(here / "fix_r1_batch.json", "w"), ensure_ascii=False)
