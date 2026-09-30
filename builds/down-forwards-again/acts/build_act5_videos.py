#!/usr/bin/env python3
"""Step 7 · videos (the user, 2026-09-30 ~10:45 UTC: "fix those and generate the next videos"). Same stack as acts/build_act4_videos.py.
  Act 5, generation 1: PR-22a, BR-22a2, BR-22b, BR-23 (BR-22a3 has no card — its line shows the doctor). Lengths from acts/plan/lengths.py A5.
  Newly confirmed images (new shots, generation 1 on the new frame): BR-15 (the fingertip on the notch), PR-12 (waist-up at the kitchen window).
  MECH-03 on its new image (the whole leg, one ordinary walking step) — its fourth video: user_go = this message, the card sat Ready for it.
  Video Fix (§22X): BR-19a gen 2 — "should be going down the stairs no breathing and she should not touch the hand rail": v1 stood at the top and
    breathed → two steps down the flight towards the lens at a normal pace, both hands loose at her sides and away from the banister, no pause.
Videos waiting on new images (not sent here): BR-06, BR-10b, BR-10c, BR-14b, BR-16a, BR-16a2, BR-16b, BR-17b, BR-20, BR-20b, BR-20c.
Writes acts/video/<beat>.call.json (versioned where the card already holds videos)."""
import json, pathlib
here = pathlib.Path(__file__).parent
src = (here / "build_act4_videos.py").read_text()
exec(compile(src[:src.index("\nC = {}")].replace("__file__", repr(str(here / "build_act4_videos.py"))), "build_act4_videos", "exec"))
L.update(json.load(open(here / "plan/lengths.json")))
A = {r["beat"]: r for r in json.load(open(here.parent / "work/actmap.json"))}
START.update({k: U + v for k, v in {
 "BR-15": "hf_20260929_201747_451f9986-635c-4495-81df-8df4606591f7.png", "PR-12": "hf_20260929_201747_0f03d356-3a7e-4d3c-a69c-3d2cdeb9b0c3.png",
 "MECH-03": "hf_20260929_201746_b6704e4c-18a0-4588-a8b3-69a962d8f7e0.png",
 "PR-22a": "hf_20260929_154134_4e7bf83b-5a28-471b-a5af-6ed2e1c720c5.png", "BR-22a2": "hf_20260929_182442_aba229e5-66d6-4822-94fc-90bfa97c5e6b.png",
 "BR-22b": "hf_20260929_182443_27d26b57-43cd-4140-a8f8-5f532d53c908.png", "BR-23": "hf_20260929_170655_75cc01d9-d616-477a-9d0e-51fc89823ad0.png"}.items()})
GO = "the user, 2026-09-30 ~10:45 UTC: 'fix those and generate the next videos' — MECH-03 sat Ready on its new, confirmed image"
C = {}  # beat -> (video version, generation, call)
C["BR-15"] = (2, 1, broll("BR-15",
  "Her forefinger on the strap's notch presses in lightly once, over about a second, lifts a finger's width and settles back on the same spot." + WORN,
  fr("BR-15", "EXTREME CLOSE, as in the start frame: her knee, the strap and her fingertip on the notch."),
  [PNEG, WNEG, "no finger on the kneecap, no hand gripping the strap"],
  "unhurried", "in_place",
  [{"risk": "the finger drifts onto the kneecap", "prevented_by": "settles back on the same spot; no finger sliding onto the kneecap"},
   {"risk": "the press moves or dents the strap", "prevented_by": "the strap does not move; worn-constancy line; product negatives"},
   {"risk": "the fingers fuse with the shell", "prevented_by": "one light press, lifts a finger's width; NEG-WARP-C"}]))
C["PR-12"] = (2, 1, broll("PR-12",
  "Holding the strap up beside her face in the window light, she tips it a few degrees towards the light and back, over about two seconds, its front "
  "face staying square to the lens and the wordmark readable, and gives a small smile; she holds it still on the last frame." + PROD,
  fr("PR-12", "MEDIUM, as in the start frame: her from the waist up at the kitchen window, the strap small beside her face."),
  [PNEG, "no strap turning round, no strap growing, no strap coming towards the lens, no fingers across the wordmark, no speaking, no mouth moving"],
  "unhurried", "in_place",
  [{"risk": "the strap grows as it moves (the user's earlier 'too big')", "prevented_by": "a few degrees' tip only; no strap growing, no strap coming towards the lens"},
   {"risk": "the wordmark smears as the strap tips", "prevented_by": "front face square to the lens; product-constancy line"},
   {"risk": "she speaks under the VO", "prevented_by": "a small smile only; no speaking, no mouth moving"}]))
C["MECH-03"] = (4, 4, mech("MECH-03",
  "One ordinary walking step, about a second: the heel strikes, the weight rolls onto the leg, the knee only slightly bent, and the band under the "
  "kneecap lights red at mid intensity on the landing and stays lit; the bones keep their shape.",
  fr("MECH-03", "FULL, as in the start frame: the whole leg in profile from hip to foot, walking."),
  ["no deep knee bend, no jump, no stomp, no second leg crossing through, no hand entering the frame, no red spreading over the whole knee"],
  [{"risk": "an exaggerated loaded bend (the user's earlier 'normal walk only')", "prevented_by": "one ordinary step, knee only slightly bent; no deep knee bend"},
   {"risk": "the legs cross through each other", "prevented_by": "one step, normal pace; no second leg crossing through; HOLD-AC"},
   {"risk": "the red spreads over the whole knee", "prevented_by": "the band under the kneecap lights; no red spreading"}]))
C["BR-19a"] = (2, 2, broll("BR-19a",
  "She sets off down the stairs forwards at a normal pace at once: two steps, one per second, the strapped left knee bending easily, both hands "
  "loose at her sides, away from the banister; still walking down on the last frame." + WORN,
  fr("BR-19a", "MEDIUM, as in the start frame: her whole body on the flight, the strap on the left knee, the right knee bare."),
  [PNEG, WNEG, "no standing still, no deep breath, no hand on the rail, no strap on the right knee"],
  "unhurried", "travels",
  [{"risk": "she stands and breathes again (the user's fault)", "prevented_by": "sets off at once, two steps, no pause; no standing still, no deep breath"},
   {"risk": "a hand goes to the rail (the user's fault)", "prevented_by": "hands loose and well away from the banister; no hand on the rail"},
   {"risk": "the camera travels with her", "prevented_by": "RIG-R1C: the phone stays on the flight below her, sways but never travels"}]))
C["PR-22a"] = (1, 1, broll("PR-22a",
  "Her hand slides the box lid a few centimetres aside along the table and lets go, over about a second and a half; the two straps lie still in the "
  "open insert, side by side, their wordmarks readable; nothing else moves." + PROD.replace("The strap keeps its", "Each strap keeps its").replace("the body it sits on", "the box it sits in"),
  fr("PR-22a", "CLOSE, from above as in the start frame: the open box with the two straps and the lid beside it."),
  [PNEG.replace("no second strap", "no third strap"), "no straps moving, no straps lifting out, no lid flipping, no wordmark changing, no fingers into the insert"],
  "unhurried", "in_place",
  [{"risk": "a strap moves or a third appears", "prevented_by": "the two straps lie still; no straps moving, no third strap"},
   {"risk": "the lid morphs as it slides", "prevented_by": "slides a few centimetres and lets go; no lid flipping; HOLD-C"},
   {"risk": "the wordmarks smear", "prevented_by": "each strap keeps its exact shape, size and wordmark; product negatives"}]))
C["BR-22a2"] = (1, 1, broll("BR-22a2",
  "She steps down off her front step onto the path, one easy step over about a second, the strapped left leg taking her weight, her bag "
  "steady on her arm; still walking on the last frame." + WORN,
  fr("BR-22a2", "FULL, as in the start frame: her at the front door."),
  [PNEG, WNEG, "no hand on the door frame or wall, no stumbling, no feet sliding"],
  "unhurried", "travels",
  [{"risk": "she steadies herself on the door or the wall", "prevented_by": "hands free; no hand on the door frame, no hand on the wall"},
   {"risk": "the strap slides as she lands", "prevented_by": "worn-constancy line; no strap sliding down the leg"},
   {"risk": "the camera walks back with her", "prevented_by": "RIG-R1C: the phone stays on the path, sways but never travels"}]))
C["BR-22b"] = (1, 1, broll("BR-22b",
  "One of the limp stretched copy straps hanging over the table edge slips a little further off, slowly, over about two seconds, and dangles, "
  "swinging gently once and settling; the others lie still; the plastic bag stays where it is.",
  fr("BR-22b", "CLOSE, as in the start frame: the copy straps over the table edge, the bag behind."),
  ["no wordmark, no logo, no text appearing on the copies, no stryde strap, no strap falling to the floor, no bands stretching longer, no hands"],
  "unhurried", "in_place",
  [{"risk": "a wordmark appears on the copies (they are blank near-copies)", "prevented_by": "no wordmark, no logo, no text appearing on the copies"},
   {"risk": "all the straps slide off together", "prevented_by": "one slips a little further; the others lie still"},
   {"risk": "the bands grow like elastic in motion", "prevented_by": "no bands stretching longer; NEG-WARP-C"}]))
C["BR-23"] = (1, 1, broll("BR-23",
  "She comes down her stairs forwards at a normal pace, two steps, one per second, the strapped left knee bending easily, both hands free at her "
  "sides and never touching the banister, a small smile; still coming down on the last frame." + WORN,
  fr("BR-23", "FULL, as in the start frame: her whole body on the stairs, the front door's stained glass behind."),
  [PNEG, WNEG, "no hand on the rail, no hesitation, no feet sliding, no speaking"],
  "unhurried", "travels",
  [{"risk": "a hand goes to the rail", "prevented_by": "both hands free, never touching the banister; no hand on the rail"},
   {"risk": "the strap slides as the knee bends", "prevented_by": "worn-constancy line; no strap sliding down the leg"},
   {"risk": "the dress morphs over the knee", "prevented_by": "two steps at a countable pace; NEG-WARP-C; PHYS-MOTION-C"}]))
FIX = {"BR-19a": ("should be going down the stairs no breathing and she should not touch the hand rail",
                  "v1 stood still at the top and took a breath → she sets off down the flight at once, two steps at a normal pace, hands loose and away from the banister")}
(here / "video").mkdir(exist_ok=True)
for b, (v, g, c) in C.items():
    c["generation"] = g; c["video_version"] = v
    if b in FIX: c["user_fault"], c["fix_note"] = FIX[b]
    if g >= 3: c["user_go"] = GO; c["fix_note"] = "v3 came from the old image; the user asked 'make a new image' → new start image: the whole leg, one ordinary walking step, mid-intensity glow"
    name = f"{b}.call.json" if v == 1 else f"{b}.v{v}.call.json"
    (here / "video" / name).write_text(json.dumps(c, ensure_ascii=False, indent=1)); print(f"{name:22s} {len(c['prompt']):5d} chars  {c['duration']}s  span {L[b]['span']}s")
