#!/usr/bin/env python3
"""Step 7 · videos on the round-11 images the user confirmed (2026-09-30 ~11:45 UTC), under their "fix those and generate the next videos".
Same stack as acts/build_act5_videos.py. One call each, preflight before any credit.
  BR-06 v3   (new frame: side-on, mid-flight, backwards) — third video of the card; user_go = the message above (new start image, the fault fixed at
             the frame: v1/v2 started high and ran her to the bottom).
  BR-10b v2  (new frame: heel on the footstool — the user's "this feels lke floating" fixed at the frame).
  BR-14b v3  (new anatomy frame with the strap — "use anatomy here"); third video of the card, user_go as above.
  BR-16a v2 (gait lab), BR-17b v2 (greengrocer's), BR-20 v2 (finger on the joint gap) — new concepts, first video on each new frame.
  BR-20b v1 (the two films on the desk) — first generation.
Writes acts/video/<beat>[.v<n>].call.json."""
import json, pathlib
here = pathlib.Path(__file__).parent
src = (here / "build_act5_videos.py").read_text()
exec(compile(src[:src.index("\nC = {}")].replace("__file__", repr(str(here / "build_act5_videos.py"))), "build_act5_videos", "exec"))
R11 = json.load(open(here / "fix_r11_renders.json"))
START.update({b: R11[b]["url"] for b in ["BR-06", "BR-10b", "BR-14b", "BR-16a", "BR-17b", "BR-20", "BR-20b"]})
GO = "the user, 2026-09-30 ~10:45 UTC: 'fix those and generate the next videos' — the card's new start image confirmed ~11:45 UTC"
C = {}
C["BR-06"] = (3, 3, broll("BR-06",
  "Holding the banister with both hands, she comes one step further down BACKWARDS: her left foot, reaching back, finds the tread below and takes her "
  "weight, then her right foot follows down onto the same tread, over about three seconds, her hands sliding a little down the rail; she stays in the "
  "middle of the flight, facing the steps, on the last frame.",
  fr("BR-06", "FULL, as in the start frame: her whole body side-on, mid-flight, the stairs above and below her."),
  ["no turning round, no facing forwards, no reaching the bottom, no second step, no feet passing through the treads, no stair geometry changing, "
   "no hands off the rail"],
  "unhurried", "in_place",
  [{"risk": "she runs to the bottom or turns round (v1/v2's fault)", "prevented_by": "one step down only, stays mid-flight facing the steps; no reaching the bottom, no turning round"},
   {"risk": "the stairs warp as she moves (the image fault)", "prevented_by": "no stair geometry changing; locked-off camera; NEG-WARP-C"},
   {"risk": "a foot sinks into a tread", "prevented_by": "the foot finds the tread and takes her weight; no feet passing through the treads"}]))
C["BR-10b"] = (2, 2, broll("BR-10b",
  "With her heel resting on the footstool, she tightens her thigh muscle once, hard, over about a second — the muscle's firm shape rising under the grey "
  "jogging bottoms and her fingers lifting a little with it — and holds it; the heel stays planted on the footstool the whole time.",
  fr("BR-10b", "CLOSE, as in the start frame: her straight leg side-on on the footstool, her hand on the thigh."),
  ["no leg lifting off the footstool, no heel floating, no leg bending, no kicking, no footstool moving, no extra legs"],
  "unhurried", "in_place",
  [{"risk": "the leg floats up (the user's 'feels like floating')", "prevented_by": "the heel stays planted on the footstool; no leg lifting off the footstool"},
   {"risk": "the leg duplicates or bends", "prevented_by": "one squeeze, leg straight; no extra legs, no leg bending; NEG-WARP-C"},
   {"risk": "the hand melts into the fabric", "prevented_by": "fingers lift a little with the muscle; HOLD-C"}]))
C["BR-14b"] = (3, 3, mech("BR-14b",
  "The foot lands on the step; a stream of red light runs down the thigh, meets the strap and fans out sideways inside the shell and round the band, "
  "over about two seconds; below the strap the tendon and the joint stay cool and pale. The strap is solid, keeps its exact shape, size and wordmark.",
  fr("BR-14b", "CLOSE, as in the start frame: the knee with the strap, the step below."),
  ["no red reaching the joint, no glow below the strap, no strap moving, no strap turning translucent, no wordmark changing"],
  [{"risk": "the red runs past the strap into the joint", "prevented_by": "fans out inside the shell; below the strap stays cool; no red reaching the joint"},
   {"risk": "the strap melts into the anatomy", "prevented_by": "the strap is solid, keeps its shape; no strap turning translucent"},
   {"risk": "the camera orbits off the knee", "prevented_by": "RIG-RVF push toward the target; NEG-CAM-RV"}]))
C["BR-16a"] = (2, 1, broll("BR-16a",
  "His left foot comes down flat onto the force plate off the low step, the knee bending a little, over about a second; the curve on the "
  "monitor rises once; he stands on the plate." + WORN,
  fr("BR-16a", "MEDIUM, as in the start frame: the volunteer side-on at the plate."),
  [PNEG, WNEG, "no second step, no numbers appearing on the monitor"],
  "unhurried", "in_place",
  [{"risk": "numbers or text appear on the monitor", "prevented_by": "one smooth curve rises; no numbers appearing on the monitor"},
   {"risk": "the strap slides as the foot lands", "prevented_by": "worn-constancy line; no strap sliding down the leg"},
   {"risk": "the legs cross or duplicate", "prevented_by": "one step down; NEG-WARP-C"}]))
C["BR-17b"] = (2, 1, broll("BR-17b",
  "She picks one apple from the crate and drops it into the brown paper bag in her other hand, over about two seconds, with a small contented smile; "
  "the trouser legs hang smooth and straight to her trainers the whole time.",
  fr("BR-17b", "FULL, as in the start frame: her whole body at the greengrocer's display."),
  ["no strap appearing, no strap outline through the trousers, no bulge at the knee, no trouser leg riding up, no apples multiplying, no speaking"],
  "unhurried", "in_place",
  [{"risk": "the strap shows through the trousers (§9D)", "prevented_by": "no strap appearing, no strap outline, no bulge at the knee"},
   {"risk": "the apple or bag morphs in her hand", "prevented_by": "one apple, one drop; no apples multiplying; HOLD-C"},
   {"risk": "she talks under the VO", "prevented_by": "a small smile only; no speaking"}]))
C["BR-20"] = (2, 1, broll("BR-20",
  "His fingertip traces slowly along the narrow joint gap on the film, from the outer side to the inner side, over about two seconds, and rests there; "
  "the film stays flat against the glass and unchanged.",
  fr("BR-20", "CLOSE, as in the start frame: the knee X-ray against the window and his fingertip."),
  ["no film bending, no film changing, no writing appearing on the film, no second film, no finger passing through the film"],
  "unhurried", "in_place",
  [{"risk": "the X-ray image changes as the finger moves", "prevented_by": "the film stays flat and unchanged; no film changing"},
   {"risk": "text appears on the film", "prevented_by": "no writing appearing on the film"},
   {"risk": "the finger sinks into the film", "prevented_by": "traces along the surface; no finger passing through the film"}]))
C["BR-20b"] = (1, 1, broll("BR-20b",
  "His two hands push the two films a finger's width closer together and square them edge to edge, over about two seconds, then lift away out of the "
  "frame; the two films lie side by side, identical and unchanged, on the last frame.",
  fr("BR-20b", "CLOSE, from above as in the start frame: the two X-ray films side by side on the desk."),
  ["no films changing, no third film, no writing appearing on the films, no films sliding apart, no face"],
  "unhurried", "in_place",
  [{"risk": "the two films diverge (they must stay identical)", "prevented_by": "identical and unchanged; no films changing"},
   {"risk": "a third film or text appears", "prevented_by": "no third film, no writing appearing"},
   {"risk": "hands melt into the films", "prevented_by": "a small push, then lift away; HOLD-C"}]))
FIX = {"BR-06": ("fix this distorted image (image) · she should be half way down so we can emphasize the going down backwards",
                 "v1/v2 started high on the flight and the model ran her to the bottom → new side-on frame mid-flight; one backwards step only, she stays mid-flight"),
       "BR-10b": ("this feels lke floating", "v1's leg was held up in the air → new frame with the heel on a footstool; the heel stays planted"),
       "BR-14b": ("use anatomy here", "v1/v2 were live-action steps → new anatomy frame with the strap: the load caught by the pad and turned into the shell")}
(here / "video").mkdir(exist_ok=True)
for b, (v, g, c) in C.items():
    c["generation"] = g; c["video_version"] = v
    if b in FIX: c["user_fault"], c["fix_note"] = FIX[b]
    if g >= 3: c["user_go"] = GO
    name = f"{b}.call.json" if v == 1 else f"{b}.v{v}.call.json"
    (here / "video" / name).write_text(json.dumps(c, ensure_ascii=False, indent=1)); print(f"{name:22s} {len(c['prompt']):5d} chars  {c['duration']}s  span {L[b]['span']}s")
