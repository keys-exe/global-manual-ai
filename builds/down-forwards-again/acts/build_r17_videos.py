#!/usr/bin/env python3
"""Step 7 · video Fix (the user, 2026-10-01: "fix those and generate the next videos ones"; board Fix note).
  BR-20c v2 "dont show that red line i want blue glow on the stryde" — diagnosis (§22X, prompt): v1 asked for a red stream down the thigh that stops at
    the strap. Now no red anywhere: as the step lands, the strap itself lights up with a soft cool blue glow (shell and band edges), the tendon below
    calm. Same confirmed frame, same RIG-RVD drift (no push — the strap must not be redrawn); the strap's shape, size and wordmark locked.
Generation 2 of the card."""
import json, pathlib
here = pathlib.Path(__file__).parent
src = (here / "build_act5_videos.py").read_text()
exec(compile(src[:src.index("\nC = {}")].replace("__file__", repr(str(here / "build_act5_videos.py"))), "build_act5_videos", "exec"))
BOARD = "/tmp/claude-0/-home-user-global-manual-ai/33ac0ea1-56e5-53d2-9765-ab6fc866d4ca/scratchpad/g23/generations"
def board(b): return json.load(open(f"{BOARD}/down-forwards-again__{b}.json"))
d = board("BR-20c"); assert d["imageStatus"] == "confirmed"; START["BR-20c"] = d["imageUrl"]
LOCK = " The strap is locked: small black shell below the kneecap, thin band, same size and wordmark as the start frame throughout."
c = mech("BR-20c",
  "The foot takes a step's weight on the step below, the knee bending a little, over about two seconds; as the weight lands, the strap lights up "
  "with a soft cool blue glow along its shell and band, and the glow holds; the tendon below stays calm and pale. No red anywhere." + LOCK,
  fr("BR-20c", "CLOSE, held at the start frame's size: the one anatomical leg with the strap, the step below."),
  ["no red light, no red line, no red glow anywhere, no push, no zoom, no strap growing, no metal clips, no strap moving, no second leg, no real skin"],
  [{"risk": "the strap is redrawn as the camera closes in (BR-14b v5's fault)", "prevented_by": "RIG-RVD lateral drift, no push, no zoom; the strap is locked line"},
   {"risk": "a red line appears (the user's fault)", "prevented_by": "no red anywhere; the glow is cool blue on the strap; no red light, no red line"},
   {"risk": "a second leg appears (the image's earlier fault)", "prevented_by": "no second leg; HOLD-AC"}])
j = json.loads(c["prompt"]); j["camera"]["movement"] = S("RIG-RVD")
for x in ["no static camera, ", "no tripod, ", "no whip pan, ", "no orbit completing a full revolution, ", "no camera crossing behind the target, ",
          "no arrows, ", "no motion lines, ", "no labels, ", "no numbers, ", "no individual muscle fibres, ", "no flat illustration, ",
          "no cartoon look, ", "no vignette, ", "no people, ", "no breath sway, ", "no focus hunt, "]:
    assert x in j["negatives"], x; j["negatives"] = j["negatives"].replace(x, "")
c["prompt"] = json.dumps(j, ensure_ascii=False, separators=(",", ":"))
assert c["start_image"] == d["imageUrl"]
c.update(generation=2, video_version=2, user_fault="dont show that red line i want blue glow on the stryde",
         fix_note="v1 ran a red stream down the thigh to the strap → no red at all; the strap itself glows soft cool blue as the step lands")
(here / "video" / "BR-20c.v2.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print("BR-20c.v2", len(c["prompt"]), "chars", c["duration"], "s")
