#!/usr/bin/env python3
"""Step 7 · videos (the user, 2026-09-29 ~20:10 UTC: "fix and generate the act 4 videos"). Same stack as acts/build_act3_videos.py (per-layout crop
sentence, product-constancy line + product negatives, compressed to ≤2,500).
  Act 4, generation 1: BR-16a, BR-16b, BR-17a, BR-17b, BR-19a, BR-19b, BR-20 — lengths from acts/plan/lengths.py after the TH-only-stretch fix
    (BR-17b ends 0.4 s after "see it"; the doctor's "I do not sell these…" stays on the doctor).
  Act 2, generation 1 on the newly confirmed images: BR-10b, BR-10c.
  Video Fix (§22X): BR-14b gen 2 — "dont show any hesitation she should be walking normally no stopiing": v1 stepped once and stopped, feet together →
    three even steps down at a normal pace (one per second), no pause, still walking on the last frame.
Writes acts/video/<beat>.call.json (the fix as BR-14b.v2.call.json)."""
import json, pathlib
here = pathlib.Path(__file__).parent
src = (here / "build_act3_videos.py").read_text()
exec(compile(src[:src.index("\nC = {}")].replace("__file__", repr(str(here / "build_act3_videos.py"))), "build_act3_videos", "exec"))
START.update({k: U + v for k, v in {
 "BR-10b": "hf_20260929_195644_4d18f19b-4ccd-4c26-a66e-1ee65c21ad8c.png", "BR-10c": "hf_20260929_195645_b25959dd-51a5-48fa-9a2a-1c139e496f90.png",
 "BR-16a": "hf_20260929_170655_dcbe34d5-89bf-4289-b539-08e24cf0eb7a.png", "BR-16b": "hf_20260929_153218_805cee27-02de-4469-b8ff-5550762681e1.png",
 "BR-17a": "hf_20260929_164556_dc25c5b4-0b8f-462f-9fd2-be6de4873b39.png", "BR-17b": "hf_20260929_154015_07be18f0-0041-4317-999e-b50a8c8d9adf.png",
 "BR-19a": "hf_20260929_154016_28c09160-2ff3-484b-a487-3cdc3a39ddfc.png", "BR-19b": "hf_20260929_180956_191ad8dc-c682-4e15-9753-1780670c67ed.png",
 "BR-20": "hf_20260929_154135_2b4d5736-a3cb-43fe-9f8d-3ff8d98ec71c.png"}.items()})
C = {}
C["BR-10b"] = broll("BR-10b",
  "Her leg held out straight, she tightens her thigh muscle once, hard, under her flat hand, over about a second — the muscle's firm shape rising under the "
  "grey jogging bottoms and her fingers lifting a little with it — and holds it there, steady, on the last frame.",
  fr("BR-10b", "CLOSE, as in the start frame: her straight leg side-on and her hand on the thigh, the front room behind."),
  ["no leg bending, no kicking, no hand sliding off the thigh, no extra legs, no bare leg, no standing up"],
  "unhurried", "in_place",
  [{"risk": "the leg distorts or duplicates", "prevented_by": "one squeeze, the leg held straight; no extra legs; NEG-WARP-C"},
   {"risk": "she kicks or bends the leg", "prevented_by": "no leg bending, no kicking"},
   {"risk": "the hand melts into the fabric", "prevented_by": "fingers lift a little with the muscle; HOLD-C"}])
C["BR-10c"] = broll("BR-10c",
  "Her left foot comes down flat onto the hall floor off the bottom stair and her left knee bends to take her whole weight, over about a second; her right "
  "foot stays on the stair behind, heel lifting; she stands like that, the weight settled on the left leg, on the last frame.",
  fr("BR-10c", "CLOSE, as in the start frame: her legs from the thigh down at the foot of the stairs, from floor level."),
  ["no second step, no stumbling, no feet sliding over the floor, no third leg, no extra feet"],
  "unhurried", "travels",
  [{"risk": "legs duplicate or cross", "prevented_by": "one step down; no third leg, no extra feet; NEG-WARP-C"},
   {"risk": "the foot slides on landing", "prevented_by": "comes down flat; no feet sliding over the floor"},
   {"risk": "the camera travels", "prevented_by": "RIG-R1C: the phone stays on the floor at the foot of the stairs"}])
C["BR-16a"] = broll("BR-16a",
  "He turns the strap a slow quarter turn in his hand beside the knee model, over about two seconds, looking at it, then holds it still with its front "
  "face to the lens, the wordmark readable; the knee model stays still on the desk." + PROD,
  fr("BR-16a", "MEDIUM-CLOSE, as in the start frame: the surgeon at his desk, the strap in his hand, the knee model beside it."),
  [PNEG, "no fingers across the wordmark, no band opening, no model moving, no speaking, no mouth moving"],
  "unhurried", "in_place",
  [{"risk": "the shell bends or the wordmark smears as it turns", "prevented_by": "a quarter turn only; product-constancy line; product negatives"},
   {"risk": "he speaks under the VO", "prevented_by": "no speaking, no mouth moving"},
   {"risk": "the knee model moves", "prevented_by": "the knee model stays still; no model moving"}])
C["BR-16b"] = broll("BR-16b",
  "The walkers set off along the towpath together: each takes one easy step forward at a normal walking pace, over about a second and a half, the nearest "
  "legs swinging past the lens, walking poles planting on the gravel; they are still walking on the last frame. The strap on each near knee stays on the "
  "front of the knee just below the kneecap, never sliding, and keeps its shape, size and wordmark.",
  fr("BR-16b", "MEDIUM, as in the start frame: the walkers' legs from the shorts down on the towpath, the canal soft behind."),
  [PNEG, WNEG, "no legs merging, no extra legs, no walkers appearing or vanishing, no feet sliding on the gravel"],
  "brisk", "travels",
  [{"risk": "legs merge or multiply", "prevented_by": "one step each; no legs merging, no extra legs; NEG-WARP-C"},
   {"risk": "straps slide or change", "prevented_by": "worn-constancy wording; product negatives"},
   {"risk": "the camera tracks the walkers", "prevented_by": "RIG-R1C: the phone stays put, sways but never travels"}])
C["BR-17a"] = broll("BR-17a",
  "Both hands, flat on the two sides of the shell, slide the closed strap up the last finger's width of her shin and seat it on the tendon just below "
  "the kneecap, over about two seconds: the notch cups the kneecap's lower border and stops; her fingers "
  "lift away. The band stays closed and is never pulled; the strap keeps its exact shape, size and wordmark in every frame.",
  fr("BR-17a", "CLOSE, as in the start frame: her sitting on the bottom stair, her left leg and the strap."),
  [PNEG, "no band being opened, no strap travelling past or onto the kneecap, no strap moving downward"],
  "unhurried", "in_place",
  [{"risk": "the strap climbs onto the kneecap or stops low", "prevented_by": "seat point named; no strap travelling past or onto the kneecap"},
   {"risk": "the band opens or is tugged", "prevented_by": "the band stays closed and is never pulled; product negatives"},
   {"risk": "hands pass through the strap", "prevented_by": "hands flat on the shell's sides; no hands passing through the strap"}])
C["BR-17b"] = broll("BR-17b",
  "Standing, she tugs the rolled cuff of her left trouser leg loose and lets it drop: the denim unrolls and falls straight down over the knee and the strap, "
  "over about a second and a half, and settles; on the last frame the trouser leg hangs smooth and flat over the knee. The strap does not move under it.",
  fr("BR-17b", "CLOSE, as in the start frame: her left leg from the thigh down, standing in the hall."),
  ["no strap moving, no strap sliding down the leg, no strap outline printing through the denim, no bulge at the knee, no second strap, "
   "no bending, no melting, no flipping of the product, no hand reaching under the trouser leg"],
  "unhurried", "in_place",
  [{"risk": "the strap shows through the fabric (§9D)", "prevented_by": "no strap outline printing through the denim, no bulge at the knee"},
   {"risk": "the denim morphs as it falls", "prevented_by": "one drop, settles; NEG-WARP-C; PHYS-MOTION-C"},
   {"risk": "the strap slips as the cuff drops", "prevented_by": "the strap does not move under it; no strap sliding down the leg"}])
C["BR-19a"] = broll("BR-19a",
  "She stands still at the top of the stairs and takes one slow breath, her hands loose at her sides, her eyes going down the flight in front of her; she has "
  "not stepped on the last frame." + WORN,
  fr("BR-19a", "MEDIUM, as in the start frame: her whole body at the top of the stairs, the strap on the left knee, the right knee bare."),
  [PNEG, WNEG, "no step taken, no strap on the right knee, no hands touching the strap, no speaking"],
  "unhurried", "still",
  [{"risk": "a strap appears on the right knee", "prevented_by": "no strap on the right knee; no second strap"},
   {"risk": "she starts walking down", "prevented_by": "no step taken"},
   {"risk": "the strap slides", "prevented_by": "worn-constancy line; no strap sliding down the leg"}])
C["BR-19b"] = broll("BR-19b",
  "She comes down the stairs forwards at a normal pace, two steps, one step per second, the strapped left knee bending easily each time, both hands "
  "free at her sides and never touching the banister; still coming down on the last frame." + WORN,
  fr("BR-19b", "WIDE, as in the start frame: her whole body on the stairs, the flight between her and the lens."),
  [PNEG, WNEG, "no hand on the banister, no hand on the rail, no hesitation, no feet sliding over the steps"],
  "unhurried", "travels",
  [{"risk": "a hand goes to the rail (the user's earlier fix)", "prevented_by": "both hands free, never touching the banister; no hand on the rail"},
   {"risk": "the strap slides as the knee bends", "prevented_by": "worn-constancy line; no strap sliding down the leg"},
   {"risk": "the camera climbs towards her", "prevented_by": "RIG-R1C: the phone stays at the foot of the stairs"}])
C["BR-20"] = broll("BR-20",
  "He holds the two knee X-rays up side by side against the window, still, his eyes moving slowly from one film to the other and back, over about four "
  "seconds; the two films stay side by side and unchanged; he lowers them a finger's width at the end.",
  fr("BR-20", "MEDIUM-CLOSE, as in the start frame: the doctor at the window holding up the two X-rays."),
  ["no films changing, no third film, no writing appearing on the films, no films bending, no speaking, no mouth moving"],
  "unhurried", "in_place",
  [{"risk": "the two films diverge or change", "prevented_by": "the two films stay side by side and unchanged; HOLD-C"},
   {"risk": "text appears on the films", "prevented_by": "no writing appearing on the films, no text appearing"},
   {"risk": "he talks under the VO", "prevented_by": "no speaking, no mouth moving"}])
F = {"BR-14b": (2, "dont show any hesitation she should be walking normally no stopiing",
  "v1 took one step down and stopped with both feet on one tread → three even steps down at a normal walking pace, one step per second, no pause, still walking on the last frame",
  broll("BR-14b",
  "She walks down the stairs at a normal pace without stopping: three even steps, one per second — her left foot with the strap lands on the tread "
  "below and the knee bends easily, then the right foot goes on down past it, then the left again — no pause between steps; still walking "
  "on the last frame." + WORN,
  fr("BR-14b", "CLOSE, as in the start frame: the strapped left knee in the middle."),
  [PNEG, WNEG, "no stopping, no pausing, no feet together on one tread"],
  "brisk", "travels",
  [{"risk": "she stops or brings her feet together (the user's fault)", "prevented_by": "three even steps, no pause; no stopping, no feet together on one tread"},
   {"risk": "the strap slides as the knee bends", "prevented_by": "worn-constancy line; no strap sliding down the leg"},
   {"risk": "a foot melts into a tread", "prevented_by": "one step per second, countable; NEG-WARP-C"}]))}
(here / "video").mkdir(exist_ok=True)
for b, c in C.items():
    (here / "video" / f"{b}.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print(f"{b:8s} {len(c['prompt']):5d} chars  {c['duration']}s  span {L[b]['span']}s")
for b, (g, fault, note, c) in F.items():
    c["generation"] = g; c["fix_note"] = note; c["user_fault"] = fault
    (here / "video" / f"{b}.v{g}.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print(f"{b:8s} v{g} {len(c['prompt']):5d} chars  {c['duration']}s  span {L[b]['span']}s")
