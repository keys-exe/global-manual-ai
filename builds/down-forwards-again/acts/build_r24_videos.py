#!/usr/bin/env python3
"""Step 7 · BR-10c video v4 (the user, 2026-10-01: "generate the video"; image v7 confirmed on the board with its motion plan on the card).
§35A form, Kling connector (kling-video-v3_0, first frame, silent). The image lesson carried over: the target named by what it looks like and
where it is, the kneecap named once only. Taste: HT11, HT12, HT13. Gen 4 of the card's video (v3 was the unused Kling clip on the old frame);
user_go = the message above."""
import json, pathlib
here = pathlib.Path(__file__).parent
d = json.load(open("/tmp/claude-0/-home-user-global-manual-ai/33ac0ea1-56e5-53d2-9765-ab6fc866d4ca/scratchpad/g31/generations/down-forwards-again__BR-10c.json"))
assert d["imageStatus"] == "confirmed"
LINE = "It was where the load was landing."
MOTION = d["motionPlan"]
PROMPT = (f'For the line "{LINE}": {MOTION} '
          "The virtual camera holds steady with a very slow, small drift. "
          "The glowing cord runs from the bottom of the round bone down to the top of the shin bone, in the centre of the frame. "
          "The bones and muscles keep their shape and place. "
          "No zoom, no leg movement, no second leg, no text.")
c = json.load(open(here / "video/BR-10c.v3.call.json"))
c.update(prompt=PROMPT, start_image=d["imageUrl"], script_line=LINE, motion_plan=MOTION, motion_confirmed=True,
         motion_confirmed_by="the user's Confirm of image v7 on the board (motion plan on the card) + 'generate the video'",
         taste=["HT11", "HT12", "HT13"], generation=4, video_version=4, user_fault="IT SHOULD BE THE PATELLAR TENDON NOT THE KNEE CAP (image)",
         fix_note="new confirmed frame v7 (the tendon lit) → the knee stays still, the pulses land on the tendon; kneecap named once only",
         user_go="the user, 2026-10-01: 'generate the video'")
(here / "video/BR-10c.v4.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print("BR-10c.v4", len(PROMPT))
