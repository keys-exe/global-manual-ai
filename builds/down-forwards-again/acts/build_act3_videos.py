#!/usr/bin/env python3
"""Step 7 · videos (the user, 2026-09-29 ~19:50 UTC: "fix and generate the act 3 videos"). Same stack as acts/build_act1_videos.py.
  Act 3, generation 1: BR-11a, BR-11b, BR-11c, PR-12, BR-13, MECH-14, BR-14b, BR-15 (product beats carry the product-constancy line in motion and the
    product negatives, compressed to the ≤2,500 budget as on HK2-02a).
  Act 1, generation 1 on the newly confirmed images: BR-05, MECH-03a, MECH-03d, MECH-05 (new image and mechanism).
  Video Fixes (§22X):
    BR-06 gen 2 — "she should be halfway down the stairs to show the going backwards": v1 ran her to the foot of the stairs and turned her round → she
      stays in the middle of the flight, facing the steps, going backwards the whole clip; negatives for reaching the bottom / turning round.
    BR-10 gen 2 — "this should be 3 separate brolls": split into BR-10 / BR-10b / BR-10c → this clip covers only "It was never how hard she tried." (3 s).
    MECH-03 gen 3 — "normal walk only": v2 bent the leg into a big loaded step (and a hand strayed into frame) → one ordinary walking step at a normal
      pace; user_go = the user's own "fix and generate the act 3 videos" on the card's Fix note.
Writes acts/video/<beat>.call.json (fixes as <beat>.v<gen>.call.json)."""
import json, pathlib
here = pathlib.Path(__file__).parent
src = (here / "build_act1_videos.py").read_text()
exec(compile(src[:src.index("\nC = {}")].replace("__file__", repr(str(here / "build_act1_videos.py"))), "build_act1_videos", "exec"))
START.update({k: U + v for k, v in {
 "BR-05": "hf_20260929_192316_fc4bf6ac-46f2-40d1-aa38-1da630a2032b.png", "MECH-03a": "hf_20260929_192317_1b75d875-de9f-442e-be09-04da6a7c9a32.png",
 "MECH-03d": "hf_20260929_192316_1e55d687-a0da-4350-90c2-1d86de950baf.png", "MECH-05": "hf_20260929_192316_776ee6ae-4050-456c-a63e-c6cb6b845292.png",
 "BR-06": "hf_20260929_164555_aab0d0bc-3d67-4315-8bce-8594012f2743.png", "BR-10": "hf_20260929_153825_2a91b599-e58c-492c-b503-556383b46131.png",
 "BR-11a": "hf_20260929_153824_de9f1657-c22a-4360-acb0-cec9eabc7fdd.png", "BR-11b": "hf_20260929_153824_fa5442a9-ed51-4c45-9e00-b0da971e9e0e.png",
 "BR-11c": "hf_20260929_164557_c1065494-f438-49eb-bb85-e7ac5b5bf97b.png", "PR-12": "hf_20260929_164556_7dee7043-71f8-4de2-8018-33223fbf2980.png",
 "BR-13": "hf_20260929_154014_c0da3d51-d9f2-46fe-b089-df427456f60f.png", "MECH-14": "hf_20260929_182443_2ede3694-8ad7-494d-af5b-b898d3fd75bc.png",
 "BR-14b": "hf_20260929_180956_a959a453-86d6-4d18-95d4-9fde94fbff07.png", "BR-15": "hf_20260929_153218_8009e376-63ac-4f22-8481-089ad2d0df1f.png"}.items()})
PIP = ""  # the crop sentence is per layout (§35 Layout): pip / split below; cutout and full take none
LAY = {"pip": " Framed for a picture-in-picture crop: one subject, large and centred, readable at a third of the width.",
       "split": " Framed for a split crop: the action sits in the middle band of the frame, nothing that matters in the top or bottom quarter."}
A = {r["beat"]: r for r in json.load(open(here.parent / "work/actmap.json"))}
def fr(beat, s):
    return s + LAY.get(A[beat]["layout"].split()[0], "")
PROD = " The strap keeps its exact shape, size and wordmark in every frame and moves only with the body it sits on."
WORN = " The strap stays on the front of the knee just below the kneecap, never sliding or rotating;" + PROD[len(" The strap"):]
PNEG = "no bending, no curling, no folding, no melting, no flipping of the product, no second strap"
WNEG = "no strap sliding down the leg, no strap rotating round the leg, no strap on the kneecap"
C = {}
# ---- Act 1, newly confirmed images -------------------------------------------------------------------------------------------
C["BR-05"] = broll("BR-05",
  "At the top of the stairs she stays where she is: both hands tighten on the banister, she takes one slow breath in, her shoulders rising a little, "
  "and keeps looking down the flight, over about two seconds; she has not moved her feet on the last frame.",
  fr("BR-05", "WIDE, as in the start frame: her whole body at the top of the flight, the stairs falling away below her."),
  ["no step taken, no walking down, no foot off the top step, no hands leaving the rail, no speaking, no mouth moving"],
  "unhurried", "in_place",
  [{"risk": "she starts walking down (becomes a different beat)", "prevented_by": "she stays; no step taken, no foot off the top step"},
   {"risk": "hands fuse with the rail", "prevented_by": "one tightening of the grip; NEG-WARP-C; HOLD-C"},
   {"risk": "she speaks under the VO", "prevented_by": "no speaking, no mouth moving; the action is one breath"}])
C["MECH-03a"] = mech("MECH-03a",
  "The virtual camera pushes in toward the knee; as the push arrives, the small red spot a thumb's width below the kneecap pulses brighter once, sharp, "
  "and stays lit; the kneecap and everything around it stay calm and still.",
  fr("MECH-03a", "CLOSE, as in the start frame: the knee from the front, the kneecap and the spot below it."),
  ["no glow on the kneecap, no second spot, no spot moving"],
  [{"risk": "the glow jumps onto the kneecap", "prevented_by": "the spot below the kneecap pulses; no glow on the kneecap"},
   {"risk": "the spot spreads or moves", "prevented_by": "one pulse, stays lit; no second spot, no spot moving"},
   {"risk": "the camera drifts off the knee", "prevented_by": "RIG-RVF push toward the target; NEG-CAM-RV"}])
C["MECH-03d"] = mech("MECH-03d",
  "The whole weight bears down: the bent leg sinks a finger's width lower onto the step, the thigh muscles drawing taut, and the band under the kneecap "
  "blazes brighter to near-white at the peak and holds there; the bones keep their shape.",
  fr("MECH-03d", "MEDIUM, as in the start frame: the whole bent leg on the step, the knee in the middle."),
  ["no leg sliding off the step, no glow on the kneecap"],
  [{"risk": "the leg distorts under the load", "prevented_by": "sinks a finger's width only; HOLD-AC"},
   {"risk": "the glow spreads over the whole knee", "prevented_by": "the band under the kneecap blazes; no glow on the kneecap"},
   {"risk": "the foot slides through the step", "prevented_by": "no leg sliding off the step; NEG-WARP-C"}])
C["MECH-05"] = mech("MECH-05",
  "The foot lands on the step and the knee bends to catch the weight; at the instant of the landing the band under the kneecap flares bright red, "
  "sharp and sudden, and holds hot as the weight settles; the kneecap stays plain ivory.",
  fr("MECH-05", "CLOSE, as in the start frame: the knee, the band under the kneecap and the step below."),
  ["no second step, no foot sliding through the step, no glow on the kneecap"],
  [{"risk": "the flare comes before the landing", "prevented_by": "at the instant of the landing, sharp and sudden"},
   {"risk": "the glow lands on the kneecap", "prevented_by": "the kneecap stays plain ivory; no glow on the kneecap"},
   {"risk": "the foot passes through the step", "prevented_by": "no foot sliding through the step; HOLD-AC"}])
# ---- Act 3 -------------------------------------------------------------------------------------------------------------------
C["BR-11a"] = broll("BR-11a",
  "Her hand squeezes the black knee sleeve flat once, the stretchy fabric crumpling and bunching in her fist over about a second, then loosens a little "
  "and holds it; the sleeve keeps its size.",
  fr("BR-11a", "CLOSE, as in the start frame: her hand and the sleeve, the kitchen soft behind."),
  ["no sleeve changing size, no second sleeve, no logo, no text on the sleeve, no strap"],
  "unhurried", "in_place",
  [{"risk": "the sleeve melts into the hand", "prevented_by": "one squeeze; NEG-WARP-C; HOLD-C"},
   {"risk": "a logo or text appears", "prevented_by": "no logo, no text on the sleeve"},
   {"risk": "the sleeve grows or shrinks", "prevented_by": "the sleeve keeps its size"}])
C["BR-11b"] = broll("BR-11b",
  "Her hand tips the grey hinged brace to one side and back on the table, the metal hinge swinging side to side once, slowly, over about two seconds, "
  "the loose straps swaying; then she lets it rest still on the table.",
  fr("BR-11b", "CLOSE, as in the start frame: her hand and the brace on the kitchen table."),
  ["no brace breaking, no parts coming off, no second brace, no logo, no text on the brace, no strap"],
  "unhurried", "in_place",
  [{"risk": "the brace bends like rubber", "prevented_by": "the hinge swings; rigid parts hold; HOLD-C"},
   {"risk": "parts detach or duplicate", "prevented_by": "no parts coming off, no second brace"},
   {"risk": "text appears on the brace", "prevented_by": "no logo, no text on the brace"}])
C["BR-11c"] = broll("BR-11c",
  "She rubs the white gel slowly into the skin of her knee with two fingers, one circular rub over about two seconds, the gel thinning to a sheen; her "
  "eyes stay on her knee; still, fingers resting on the knee, on the last frame.",
  fr("BR-11c", "MEDIUM, as in the start frame: her seated at the kitchen table, the trouser leg rolled, her knee and hand."),
  ["no tube moving by itself, no text on the tube, no strap, no brace, no standing up, no speaking"],
  "unhurried", "in_place",
  [{"risk": "fingers fuse into the knee", "prevented_by": "one circular rub; NEG-WARP-C; HOLD-C"},
   {"risk": "text appears on the tube", "prevented_by": "no text on the tube, no text appearing"},
   {"risk": "the rub repeats as a loop", "prevented_by": "one circular rub over two seconds, then still"}])
C["PR-12"] = broll("PR-12",
  "Her hand turns the strap a slow quarter turn towards the window light over about two seconds, pinched at the shell's bottom edge, the light sliding "
  "across the matte shell and catching the chrome slides; she holds it still facing the lens, the wordmark readable." + PROD,
  fr("PR-12", "CLOSE, as in the start frame: her hand holding the strap up in the kitchen window light."),
  [PNEG, "no band opening, no fingers across the wordmark, no fingers on the chrome slides"],
  "unhurried", "in_place",
  [{"risk": "the shell bends or the wordmark smears as it turns", "prevented_by": "a quarter turn only; product-constancy line; product negatives"},
   {"risk": "fingers cover the wordmark", "prevented_by": "pinched at the bottom edge; no fingers across the wordmark"},
   {"risk": "the band opens or dangles oddly", "prevented_by": "no band opening; HOLD-C"}])
C["BR-13"] = broll("BR-13",
  "She sits still on the edge of the armchair, her left leg straight, and takes one slow breath, her hands resting on her thighs; nothing "
  "else moves." + WORN,
  fr("BR-13", "CLOSE, as in the start frame: her legs and the strap on the left knee, the front room behind."),
  [PNEG, WNEG, "no standing up, no hands touching the strap"],
  "unhurried", "still",
  [{"risk": "the strap slides or rotates", "prevented_by": "worn-constancy line; no strap sliding or rotating"},
   {"risk": "the wordmark smears", "prevented_by": "keeps its exact wordmark every frame; no wordmark smearing"},
   {"risk": "a hand goes to the strap", "prevented_by": "hands resting on her thighs; no hands touching the strap"}])
C["MECH-14"] = broll("MECH-14",
  "Her hand tilts the upturned strap slowly towards the window light over about two seconds, a small tilt, the light raking across the grey silicone pad, "
  "its grooves and its smooth central bar; she holds it still. The strap keeps its exact shape, size and pad pattern in every frame and moves only with her hand.",
  fr("MECH-14", "CLOSE, as in the start frame: her open hand from above, the strap back-up on her palm."),
  ["no bending, no curling, no folding, no melting, no flipping of the product", "no strap turning over, no pad changing shape, no grooves moving, "
   "no wordmark appearing, no second strap, no fingers closing over the pad"],
  "unhurried", "in_place",
  [{"risk": "the pad pattern crawls or changes", "prevented_by": "keeps its exact pad pattern; no grooves moving, no pad changing shape"},
   {"risk": "the strap flips to its front", "prevented_by": "a small tilt only; no strap turning over"},
   {"risk": "fingers close over the pad", "prevented_by": "open hand; no fingers closing over the pad"}])
C["BR-14b"] = broll("BR-14b",
  "She steps down one stair: her left foot, the strap on its knee, lands on the tread below and the left knee bends easily under her weight, over "
  "about a second and a half; her right foot follows onto the same tread; she stands there, hands free, on the last frame." + WORN,
  fr("BR-14b", "CLOSE, as in the start frame: her legs on the stairs, the strapped left knee in the middle."),
  [PNEG, WNEG, "no hand on the rail, no second step, no feet sliding over the steps"],
  "unhurried", "travels",
  [{"risk": "the strap slides as the knee bends", "prevented_by": "worn-constancy line; no strap sliding down the leg"},
   {"risk": "a foot melts into the tread", "prevented_by": "one step at a countable pace; NEG-WARP-C"},
   {"risk": "the camera follows her down", "prevented_by": "RIG-R1C: the phone stays at the foot of the stairs"}])
C["BR-15"] = broll("BR-15",
  "His fingertip sets down on the tendon just under the kneecap of the knee model on the desk, holds a beat, then lifts a centimetre and hovers, over "
  "about two seconds; the model stays still on its stand.",
  fr("BR-15", "CLOSE, as in the start frame: his hand and the knee model on the desk."),
  ["no model moving, no model parts coming off, no second hand, no text appearing, no face"],
  "unhurried", "in_place",
  [{"risk": "the model wobbles or morphs", "prevented_by": "the model stays still on its stand; HOLD-C"},
   {"risk": "the finger passes into the model", "prevented_by": "sets down, lifts a centimetre; NEG-WARP-C"},
   {"risk": "a second hand appears", "prevented_by": "no second hand"}])
# ---- video Fixes -------------------------------------------------------------------------------------------------------------
F = {}
F["BR-06"] = (2, "she should be halfway down the stairs tos how the going backwards", "v1 ran her all the way to the foot of the stairs and turned her to face the hall → she stays in the middle of the flight, facing the steps, going down backwards for the whole clip; negatives for reaching the bottom and turning round", broll("BR-06",
  "Halfway down the flight and facing the stairs, she keeps coming down backwards: her left foot reaches back and down for the next tread and her weight "
  "follows, then her right foot joins it, slowly, over about two and a half seconds; she reaches back with her left foot again for the next one; still "
  "facing the stairs, still in the middle of the flight, both hands on the rail, on the last frame.",
  fr("BR-06", "WIDE, as in the start frame: the hall and the whole flight, her whole body on the stairs, facing the steps."),
  ["no reaching the bottom of the stairs, no stepping off onto the hall floor, no turning round, no turning to face the hall, no walking forwards, "
   "no stumbling, no falling, no feet sliding over the steps, no extra steps appearing, no hands leaving the rail"],
  "unhurried", "travels",
  [{"risk": "she reaches the bottom and turns (the user's fault)", "prevented_by": "still in the middle of the flight on the last frame; no reaching the bottom, no turning round"},
   {"risk": "a foot melts into the step", "prevented_by": "one step at a slow countable pace; NEG-WARP-C"},
   {"risk": "the camera climbs the stairs", "prevented_by": "RIG-R1C: the phone stays at the foot"}]))
F["BR-10"] = (2, "this should be 3 separate brolls", "B-10 split into BR-10 / BR-10b / BR-10c → this clip covers only 'It was never how hard she tried.' (span 2.04 s → 3 s instead of 6 s); same confirmed image and action", broll("BR-10",
  "Seated in the armchair, she draws the green exercise band back towards her chest with both hands, slowly, over about two seconds, her foot pressing "
  "into the loop and her leg straightening as the band stretches; she holds it there, straining a little, eyes down on her foot, on the last frame.",
  fr("BR-10", "MEDIUM, as in the start frame: her in the armchair, the band from her hands to her foot."),
  ["no band snapping, no band passing through her hand or foot, no second band, no standing up, no text on the exercise sheet, no speaking"],
  "unhurried", "in_place",
  [{"risk": "the band passes through her hand or foot", "prevented_by": "one pull; no band passing through; NEG-WARP-C"},
   {"risk": "the band snaps or duplicates", "prevented_by": "no band snapping, no second band; HOLD-C"},
   {"risk": "text appears on the exercise sheet", "prevented_by": "no text on the exercise sheet, no text appearing"}]))
F["MECH-03"] = (3, "normal walk only", "v2 bent the leg into a big loaded step and a hand strayed into the top of the frame → one ordinary walking step at a normal pace (one step per second), a slight knee flex only; no hand entering the frame", mech("MECH-03",
  "The leg takes one ordinary walking step at a normal walking pace, one step per second: the foot lands, the knee flexes only slightly as the weight "
  "comes onto it, and in that moment the band of tendon under the kneecap lights red along its length, then eases as the leg rolls on.",
  fr("MECH-03", "CLOSE, as in the start frame: the knee, the kneecap and the band of tendon below it."),
  ["no deep knee bend, no jump, no stomp, no hand entering the frame, no red spreading over the whole knee"],
  [{"risk": "an exaggerated loaded bend again (the user's fault)", "prevented_by": "one ordinary walking step, slight flex only; no deep knee bend"},
   {"risk": "a hand enters the frame (v2)", "prevented_by": "no hand entering the frame, no hands"},
   {"risk": "the red spreads over the whole knee", "prevented_by": "the band under the kneecap lights; no red spreading"}]))
GO = "the user, 2026-09-29 ~19:50 UTC: 'fix and generate the act 3 videos' — asked for this card's Fix ('normal walk only')"
(here / "video").mkdir(exist_ok=True)
for b, c in C.items():
    (here / "video" / f"{b}.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print(f"{b:8s} {len(c['prompt']):5d} chars  {c['duration']}s  span {L[b]['span']}s")
for b, (g, fault, note, c) in F.items():
    c["generation"] = g; c["fix_note"] = note; c["user_fault"] = fault
    if g >= 3: c["user_go"] = GO
    (here / "video" / f"{b}.v{g}.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print(f"{b:8s} v{g} {len(c['prompt']):5d} chars  {c['duration']}s  span {L[b]['span']}s")
