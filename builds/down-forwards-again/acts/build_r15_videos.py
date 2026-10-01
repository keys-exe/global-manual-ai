#!/usr/bin/env python3
"""Step 7 · video Fix (the user, 2026-10-01: "fix those and generate the next ones").
  BR-14b v6 "dont change the product" — diagnosis (§22X, motion): v5's RIG-RVF fast push ran from the whole leg to a tight close-up, and as the strap
    grew in frame the model redrew it — a taller, wider shell, metal side clips, a thicker band. Fix at the source: RIG-RVD (light carries the
    claim, §12A option) — a small lateral drift, no push, so the strap stays the size it is in the confirmed frame; the strap described as it is
    there and locked (matte black, thin band, no metal parts); the blue light glows round it, never on it. Start image read from the board.
Sixth video of the card: user_go = the message above."""
import json, pathlib
here = pathlib.Path(__file__).parent
src = (here / "build_act5_videos.py").read_text()
exec(compile(src[:src.index("\nC = {}")].replace("__file__", repr(str(here / "build_act5_videos.py"))), "build_act5_videos", "exec"))
BOARD = "/tmp/claude-0/-home-user-global-manual-ai/33ac0ea1-56e5-53d2-9765-ab6fc866d4ca/scratchpad/g20/generations"
def board(b): return json.load(open(f"{BOARD}/down-forwards-again__{b}.json"))
d = board("BR-14b"); assert d["imageStatus"] == "confirmed"; START["BR-14b"] = d["imageUrl"]
GO = "the user, 2026-10-01: 'fix those and generate the next ones' — asked for this card's Fix"
c = mech("BR-14b",
  "The foot lands on the step; red light runs down the thigh and, reaching the strap, turns cool blue, a soft glow round the knee, over about "
  "two seconds; the tendon below stays pale blue. THE STRAP IS LOCKED: exactly as in the start frame — small matte-black shell, thin black band, "
  "white 'stryde' wordmark, same size on screen throughout; it never grows or gains parts; the light glows round it, never on it.",
  fr("BR-14b", "CLOSE, as in the start frame and held at that size: the anatomical knee with the strap, the step below; the strap stays as large as it is in the start frame."),
  ["no push, no zoom, no strap growing, no wider band, no taller shell, no metal clips, no buckle, no side plates, "
   "no strap glowing, no strap changing colour, no wordmark changing, no red below the strap, no real skin"],
  [{"risk": "the strap is redrawn as the camera closes in (v5's fault)", "prevented_by": "RIG-RVD lateral drift, no push, no zoom; the strap keeps its on-screen size"},
   {"risk": "the strap gains parts (metal clips, a wider shell)", "prevented_by": "THE STRAP IS LOCKED line; no metal clips, no buckle, no side plates, no taller shell"},
   {"risk": "the blue light recolours the strap", "prevented_by": "the light glows round it, never on it; no strap glowing, no strap changing colour"}])
j = json.loads(c["prompt"]); j["camera"]["movement"] = S("RIG-RVD")
j["camera"]["framing"] = "CLOSE, held at the start frame's size: the anatomical knee with the strap, the step below."
for x in ["no static camera, ", "no tripod, ", "no whip pan, ", "no orbit completing a full revolution, ", "no camera crossing behind the target, ",
          "no arrows, ", "no motion lines, ", "no labels, ", "no numbers, ", "no individual muscle fibres, ", "no flat illustration, ",
          "no cartoon look, ", "no vignette, ", "no second limb, ", "no people, ", "no breath sway, ", "no focus hunt, "]:
    assert x in j["negatives"], x; j["negatives"] = j["negatives"].replace(x, "")
c["prompt"] = json.dumps(j, ensure_ascii=False, separators=(",", ":"))
assert c["start_image"] == d["imageUrl"]
c.update(generation=6, video_version=6, user_fault="dont change the product",
         fix_note="v5's fast push enlarged the strap and the model redrew it (wider shell, metal clips) → RIG-RVD lateral drift, no push; the strap locked at its start-frame size and look; light round it, never on it",
         user_go=GO)
(here / "video" / "BR-14b.v6.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print("BR-14b.v6", len(c["prompt"]), "chars", c["duration"], "s")
print(j["negatives"][:600])
