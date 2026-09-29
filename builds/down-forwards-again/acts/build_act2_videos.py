#!/usr/bin/env python3
"""Step 7 · Act 2 body videos (the user, 2026-09-29: "generate the act 2 videos") — same stack as acts/build_act1_videos.py (§35 JSON, RIG-R1C, HOLD-C,
PHYS-MOTION-C, INHERIT-CAP/ENV, PiP/cutout framing), start frames = the user-confirmed Act 2 images, lengths from acts/plan/lengths.json (TH-A2).
Also the two Act 1 regenerations that keep their confirmed images after the user's splits (generation 2, §22X): BR-05a and MECH-03 now cover only
their own new spans. Writes acts/video/<beat>.call.json (BR-05a / MECH-03 as <beat>.v2.call.json)."""
import json, pathlib
here = pathlib.Path(__file__).parent
src = (here / "build_act1_videos.py").read_text()
exec(compile(src[:src.index("\nC = {}")].replace("__file__", repr(str(here / "build_act1_videos.py"))), "build_act1_videos", "exec"))
START.update({
 "BR-06": U + "hf_20260929_164555_aab0d0bc-3d67-4315-8bce-8594012f2743.png", "BR-07": U + "hf_20260929_154310_57eb9215-bf07-4fbc-9eb9-e146822b8f87.png",
 "BR-08": U + "hf_20260929_153824_91b4be51-404d-4166-bf3c-baba44a8b898.png", "BR-09a": U + "hf_20260929_152945_df1513d5-a1da-4be6-aca7-6ce9313b6246.png",
 "BR-09b": U + "hf_20260929_160352_cb3f953f-4a00-4ab6-92f3-e8ff8b336f3a.png", "BR-09c": U + "hf_20260929_153824_e2210b25-383c-4ec3-b7d3-0fa665b34923.png",
 "BR-10": U + "hf_20260929_153825_2a91b599-e58c-492c-b503-556383b46131.png"})
PIP = "Framed for its crop: one subject, large and centred, readable at a third of the width."
C = {}
C["BR-06"] = broll("BR-06",
  "Facing the stairs, she comes down one more step backwards: her left foot reaches back and down, feeling for the tread with her toe, slowly, over about "
  "two seconds, both hands gripping the rail; her weight follows onto it and she stops there, still gripping, looking down over her shoulder at the next step.",
  "WIDE, as in the start frame: the hall and the whole flight, her whole body on the stairs, facing the steps.",
  ["no turning round, no walking forwards, no second step, no stumbling, no falling, no feet sliding over the steps, no extra steps appearing, no hands leaving the rail"],
  "unhurried", "travels",
  [{"risk": "she turns and walks down forwards", "prevented_by": "facing the stairs, one step backwards; no turning round, no walking forwards"},
   {"risk": "a foot melts into the step", "prevented_by": "one step at a slow countable pace; NEG-WARP-C; no feet sliding"},
   {"risk": "the camera climbs the stairs", "prevented_by": "RIG-R1C: the phone stays at the foot, sways but never travels"}])
C["BR-07"] = broll("BR-07",
  "She pushes down on the chair arm and rises a hand's width more, her knees trembling, then her strength gives and she sinks back onto the edge of the "
  "seat, over about two seconds; she stays there, breathing out, her hand still on the arm, on the last frame.",
  "MEDIUM, as in the start frame: her side-on at the armchair, head to feet.",
  ["no standing fully up, no falling, no chair moving, no speaking, no mouth moving, no smiling"],
  "unhurried", "in_place",
  [{"risk": "she stands up easily (reads as recovery)", "prevented_by": "rises a hand's width, then sinks back; no standing fully up"},
   {"risk": "hand and chair arm fuse", "prevented_by": "one push and sink; NEG-WARP-C; HOLD-C"},
   {"risk": "the chair slides", "prevented_by": "no chair moving"}])
C["BR-08"] = broll("BR-08",
  "Her weight shifts onto her right foot on the bottom stair and she pushes up; her left foot lifts off the floor and swings up stiffly to join it on the "
  "same stair, the left knee barely bending — one step at a slow careful pace, over about two seconds; both feet end side by side on the bottom stair and stay there.",
  "CLOSE, as in the start frame: her legs from the skirt hem down, the bottom stair and the hall floor.",
  ["no second step, no feet sliding over the steps, no extra steps appearing, no extra legs, no hands in frame, no stumbling"],
  "unhurried", "travels",
  [{"risk": "legs cross or duplicate", "prevented_by": "one step, the left foot joins the right; no extra legs; NEG-WARP-C"},
   {"risk": "she climbs further and leaves frame", "prevented_by": "both feet end side by side on the bottom stair and stay"},
   {"risk": "the left knee bends normally (loses the point)", "prevented_by": "swings up stiffly, the left knee barely bending"}])
C["BR-09a"] = broll("BR-09a",
  "The boots stay exactly where they are on the newspaper. A patch of grey daylight drifts slowly across them and the paper as a cloud passes, over the "
  "whole clip; one small dry fleck of mud drops from a boot's edge onto the newspaper and lies still. Nothing else moves.",
  "CLOSE, as in the start frame: the pair of walking boots on the newspaper by the door, the hall soft behind.",
  ["no boots moving, no laces moving by themselves, no feet, no person, no text appearing on the newspaper, no readable newsprint"],
  "unhurried", "still",
  [{"risk": "the boots shift or morph", "prevented_by": "the boots stay exactly where they are; HOLD-C; no boots moving"},
   {"risk": "the newsprint becomes readable text", "prevented_by": "no text appearing on the newspaper, no readable newsprint"},
   {"risk": "a clip with nothing happening", "prevented_by": "the light drifts across and one fleck of mud falls"}])
C["BR-09b"] = broll("BR-09b",
  "She lifts her head and looks out of the window at the overgrown garden, one slow turn of the head over about a second, and keeps looking; the mug stays "
  "still in her hands; her shoulders drop a little with a slow breath out; still looking out on the last frame.",
  "MEDIUM, as in the start frame: the kitchen, her at the sink by the window, the garden through the glass.",
  ["no walking, no drinking, no mug moving by itself, no speaking, no smiling, no people in the garden"],
  "unhurried", "in_place",
  [{"risk": "the mug slides or melts", "prevented_by": "the mug stays still in her hands; HOLD-C"},
   {"risk": "she walks off", "prevented_by": "one turn of the head, then keeps looking; no walking"},
   {"risk": "figures appear in the garden", "prevented_by": "no people in the garden"}])
C["BR-09c"] = broll("BR-09c",
  "She pulls the front door the last few inches open, her hand on its edge, over about a second; on the step her daughter gives a small tired smile and "
  "lifts the shopping bag a little, and the boy looks up at his grandmother; nobody steps over the threshold; they stay like that on the last frame.",
  "MEDIUM, as in the start frame: over her shoulder in the hall, the open door, her daughter and grandson on the step.",
  ["no hugging, no stepping inside, no speaking, no mouth moving, no third visitor, no dog, no door closing"],
  "unhurried", "in_place",
  [{"risk": "the family walks in (changes the beat)", "prevented_by": "nobody steps over the threshold; no stepping inside"},
   {"risk": "faces change or duplicate", "prevented_by": "small actions only; HOLD-C; no third visitor"},
   {"risk": "they talk under the VO", "prevented_by": "no speaking, no mouth moving"}])
C["BR-10"] = broll("BR-10",
  "Seated in the armchair, she draws the green exercise band back towards her chest with both hands, slowly, over about two seconds, her foot pressing "
  "into the loop and her leg straightening as the band stretches; she holds it there, straining a little, eyes down on her foot, on the last frame.",
  "MEDIUM, as in the start frame: her in the armchair, the band from her hands to her foot.",
  ["no band snapping, no band passing through her hand or foot, no second band, no standing up, no text on the exercise sheet, no speaking"],
  "unhurried", "in_place",
  [{"risk": "the band passes through her hand or foot", "prevented_by": "one pull; no band passing through; NEG-WARP-C"},
   {"risk": "the band snaps or duplicates", "prevented_by": "no band snapping, no second band; HOLD-C"},
   {"risk": "text appears on the exercise sheet", "prevented_by": "no text on the exercise sheet, no text appearing"}])
# ---- Act 1 regenerations after the splits (generation 2) --------------------------------------------------------------------
R2 = {}
R2["BR-05a"] = broll("BR-05a",
  "She pulls herself up onto the next stair: both hands tighten on the newel post, her left foot lifts slowly onto the tread above and her weight "
  "follows it, over about two seconds, her back bent with the effort; she stops there, gripping the post, on the last frame.",
  "WIDE, as in the start frame: the hall and the foot of the stairs, her whole body side-on on the bottom steps.",
  ["no second step, no stumbling, no falling, no feet sliding over the steps, no extra steps appearing, no hand leaving the post"],
  "unhurried", "travels",
  [{"risk": "a foot melts into or misses the tread", "prevented_by": "one step up at a slow countable pace; NEG-WARP-C; no feet sliding"},
   {"risk": "she climbs several steps and leaves frame", "prevented_by": "one step, then she stops; no second step"},
   {"risk": "the camera travels with her", "prevented_by": "RIG-R1C: the phone stays in the hall, sways but never travels"}])
R2["MECH-03"] = mech("MECH-03",
  "The leg takes one step's load: the thigh muscle tightens and the knee gives a little, and at that moment the band of tendon under the kneecap "
  "flashes bright red along its whole length, as one band; the red holds hot while the load stays on; the kneecap and shin bone keep their places.",
  "CLOSE, as in the start frame: the knee, the kneecap and the band of tendon below it.",
  ["no red spreading over the whole knee, no second band"],
  [{"risk": "the red spreads over the whole knee", "prevented_by": "the band of tendon under the kneecap flashes as one band; no red spreading"},
   {"risk": "the leg bends too far and the anatomy breaks", "prevented_by": "the knee gives a little; HOLD-AC"},
   {"risk": "the glow fades in gently", "prevented_by": "flashes at the moment of load; no gradual onset"}])
FIX = {"BR-05a": ("this should be 2 brolls", "the line was split: BR-05 now carries 'Coming down is worse than going up.' → this clip covers only "
                  "'Going up, your muscles lift you.' (span 2.02 s → 3 s instead of 5 s); same confirmed image and action"),
       "MECH-03": ("this should be cut into 4 brolls", "B-03 was split into MECH-03a, BR-03b, MECH-03, MECH-03d → this clip covers only 'Every step "
                   "you take lands on it.' (span 2.38 s → 3 s instead of 10 s); same confirmed image and action")}
for b, c in R2.items():
    c["generation"] = 2; c["fix_note"] = FIX[b][1]; c["user_fault"] = FIX[b][0]
(here / "video").mkdir(exist_ok=True)
for b, c in C.items():
    (here / "video" / f"{b}.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print(f"{b:8s} {len(c['prompt']):5d} chars  {c['duration']}s  span {L[b]['span']}s")
for b, c in R2.items():
    (here / "video" / f"{b}.v2.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print(f"{b:8s} v2 {len(c['prompt']):5d} chars  {c['duration']}s  span {L[b]['span']}s")
