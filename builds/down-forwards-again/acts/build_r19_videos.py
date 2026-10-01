#!/usr/bin/env python3
"""Step 7 · BR-10c video (the user, 2026-10-01: "GENERATE THE VIDEO" — BR-10c v4 confirmed on the board).
  BR-10c v2 (gen 2, new frame v4): the foot lands, red pulses run down the thigh and land on the patellar tendon, which flares; the kneecap and joint
  stay unlit. No product. RIG-RVD drift, not the fast push (a push redraws what grows in frame — the glow could slide back onto the kneecap).
Start image read from the board's confirmed imageUrl and asserted."""
import json, pathlib
here = pathlib.Path(__file__).parent
src = (here / "build_act5_videos.py").read_text()
exec(compile(src[:src.index("\nC = {}")].replace("__file__", repr(str(here / "build_act5_videos.py"))), "build_act5_videos", "exec"))
d = json.load(open("/tmp/claude-0/-home-user-global-manual-ai/33ac0ea1-56e5-53d2-9765-ab6fc866d4ca/scratchpad/g26/generations/down-forwards-again__BR-10c.json"))
assert d["imageStatus"] == "confirmed"; START["BR-10c"] = d["imageUrl"]
c = mech("BR-10c",
  "The foot lands flat on the step and the knee bends a little to take the weight; at that moment three red pulses run down the thigh one after another "
  "and land on the patellar tendon, the cord on the front of the knee below the kneecap, which flares bright red and stays hot; the kneecap and the "
  "joint stay plain ivory; the bones keep their places.",
  fr("BR-10c", "CLOSE, held at the start frame's size: the one anatomical leg from mid-thigh to the foot on the step."),
  ["no push, no zoom, no red on the kneecap, no red at the back of the knee, no red in the joint, no second leg, no real skin"],
  [{"risk": "the red lands on the kneecap or joint (the user's image fault)", "prevented_by": "lands on the patellar tendon below the kneecap; no red on the kneecap, no red in the joint"},
   {"risk": "a second leg appears", "prevented_by": "no second leg; HOLD-AC"},
   {"risk": "the glow fades in slowly and reads as ambient", "prevented_by": "flares at the landing; no gradual onset, no crossfade"}])
j = json.loads(c["prompt"]); j["camera"]["movement"] = S("RIG-RVD")
for x in ["no static camera, ", "no tripod, ", "no whip pan, ", "no orbit completing a full revolution, ", "no camera crossing behind the target, ",
          "no arrows, ", "no motion lines, ", "no labels, ", "no numbers, ", "no individual muscle fibres, ", "no flat illustration, ",
          "no cartoon look, ", "no vignette, ", "no people, ", "no breath sway, ", "no focus hunt, "]:
    assert x in j["negatives"], x; j["negatives"] = j["negatives"].replace(x, "")
c["prompt"] = json.dumps(j, ensure_ascii=False, separators=(",", ":"))
assert c["start_image"] == d["imageUrl"]
c.update(generation=2, video_version=2, fix_note="v1 ran on the old whole-leg frame → the new confirmed frame v4, the red on the patellar tendon")
(here / "video" / "BR-10c.v2.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print("BR-10c.v2", len(c["prompt"]), "chars", c["duration"], "s")
