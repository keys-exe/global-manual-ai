#!/usr/bin/env python3
"""Step 7 · BR-10c video Fix (the user, 2026-10-01: "FIX THOSE"; board Fix note on v2 "I NEED A NEW MOVEMENT BASE ON THE IMAGE").
Written in the §35A form (V7.71.0, merged into this branch 2026-10-01: a video Fix rewrites the prompt in that form): the line, the action from
this frame, the camera in one clause, 2–3 shot facts, ≤ 5 negatives, ≤ 1,000 characters.
  Diagnosis (§22X, motion): v2 asked "the foot lands… the knee bends" on a frame whose foot is already planted, so the model invented a step-up —
  the rest of the body and both hands came into frame, a second leg appeared, the knee bent into a squat. The new movement is read off the frame:
  the foot stays planted, the knee settles a few degrees, the pulses land on the patellar tendon. Nothing enters the frame.
  MOTION is the "Video will show" line; it goes on the card for the user's confirm (§22X) — motion_confirmed is set only from that confirm.
Gen 3 of the card: user_go = the message above. Taste: HT11 (the named structure exactly), HT12 (whole bodies, no extra limbs), HT13 (real motion)."""
import json, pathlib, sys
here = pathlib.Path(__file__).parent
d = json.load(open("/tmp/claude-0/-home-user-global-manual-ai/33ac0ea1-56e5-53d2-9765-ab6fc866d4ca/scratchpad/g27/generations/down-forwards-again__BR-10c.json"))
assert d["imageStatus"] == "confirmed"
LINE = "It was where the load was landing."
MOTION = ("The leg stays planted on the step as it is; the knee settles a few degrees as the weight arrives, over about a second, and three red "
          "pulses run down the thigh one after another and land on the patellar tendon below the kneecap, which flares bright red; it ends on "
          "the tendon glowing red and the kneecap plain ivory.")
PROMPT = (f'For the line "{LINE}": {MOTION} '
          "The virtual camera drifts slowly sideways at a steady distance, a small move. "
          "One leg only, from mid-thigh to the foot, the foot flat on the step the whole time. "
          "The glow sits only on the cord below the kneecap; the kneecap and the joint stay calm. "
          "The bones and muscles keep their shape and place. "
          "No second leg, no hands or body entering the frame, no stepping, no red on the kneecap, no zoom.")
c = json.load(open(here / "video/BR-10c.v2.call.json"))
c.update(prompt=PROMPT, start_image=d["imageUrl"], script_line=LINE, motion_plan=MOTION, motion_confirmed="--confirmed" in sys.argv,
         taste=["HT11", "HT12", "HT13"], risk_class=None, pilot=None, pin_waived=None, generation=3, video_version=3, prefer_multi_shots="false",
         user_fault="I NEED A NEW MOVEMENT BASE ON THE IMAGE",
         fix_note="v2's 'the foot lands, the knee bends' on a planted frame invented a step-up (body, hands and a second leg came into frame, a squat) → the foot stays planted, a slight settle only, the pulses land on the tendon; §35A form",
         user_go="the user, 2026-10-01: 'FIX THOSE' — the card's Fix note on v2")
c.pop("rack", None)
if c["motion_confirmed"]:
    c["motion_confirmed_by"] = "the user, 2026-10-01: 'ITS TAKING TOO LONG ON THE FIXING USE KLING CONNECTOR' — the reply to the proposed 'Video will show' line"
c.update(route="kling", kling_model="kling-video-v3_0", route_note="user 2026-10-01: 'USE KLING CONNECTOR' (Kling credits back: 45,091) — off Kie")
for k in ("kie_model",): c.pop(k, None)
(here / "video/BR-10c.v3.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print("BR-10c.v3", len(PROMPT), "chars;", "motion_confirmed", c["motion_confirmed"])
