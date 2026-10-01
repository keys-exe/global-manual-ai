#!/usr/bin/env python3
"""Step 7 · videos on the images the user confirmed on the board (2026-10-01: "fix those and generate the next ones"). Start images read from the
board's confirmed imageUrl and asserted. Same stack as acts/build_act5_videos.py; preflight before any credit.
  BR-16a2 v1 (the surgeon fits the strap, a colleague watches) — first video.
  BR-16b  v2 (four walkers on the park path) — new frame (v1's video was on the old towpath frame); generation 2.
  BR-20c  v1 (anatomy, one leg, the strap on) — first video. RIG-RVD lateral drift, not RIG-RVF: BR-14b v5 showed a fast push makes the model redraw
             the strap as it grows in frame (the user's "dont change the product"); light carries this claim, so the §12A drift option.
Writes acts/video/<beat>[.v<n>].call.json."""
import json, pathlib
here = pathlib.Path(__file__).parent
src = (here / "build_act5_videos.py").read_text()
exec(compile(src[:src.index("\nC = {}")].replace("__file__", repr(str(here / "build_act5_videos.py"))), "build_act5_videos", "exec"))
BOARD = "/tmp/claude-0/-home-user-global-manual-ai/33ac0ea1-56e5-53d2-9765-ab6fc866d4ca/scratchpad/g22/generations"
def board(b): return json.load(open(f"{BOARD}/down-forwards-again__{b}.json"))
for b in ["BR-16a2", "BR-16b", "BR-20c"]:
    d = board(b); assert d["imageStatus"] == "confirmed", b; START[b] = d["imageUrl"]
LOCK = " The strap is locked: small black shell below the kneecap, thin band, same size and wordmark as the start frame throughout."
C = {}
C["BR-16a2"] = (1, 1, broll("BR-16a2",
  "The surgeon's two hands, flat on either side of the strap's shell, press it gently into place on the tendon just below the patient's kneecap and "
  "lift away a finger's width, over about two seconds; the second surgeon gives one small nod." + LOCK,
  fr("BR-16a2", "MEDIUM, as in the start frame: the patient on the couch, the surgeon at her knee, the second surgeon behind."),
  [PNEG, WNEG, "no strap growing, no padding, no brace, no hands through the strap, no speaking"],
  "unhurried", "in_place",
  [{"risk": "the strap turns into a padded brace (the image's earlier fault)", "prevented_by": "the strap is locked line; no padding, no brace, no strap growing"},
   {"risk": "the hands melt into the shell", "prevented_by": "hands flat either side, press and lift a finger's width; HOLD-C"},
   {"risk": "they talk under the VO", "prevented_by": "a small nod only; no speaking, no mouth moving"}]))
C["BR-16b"] = (2, 2, broll("BR-16b",
  "The four walkers take one easy step further along the path towards us at a normal pace, over about a second and a half, with small smiles; "
  "still walking on the last frame, a couple of metres from the lens." + LOCK.replace("The strap is locked", "The strap on each of the two near knees is locked"),
  fr("BR-16b", "FULL, as in the start frame: the four walkers on the park path, the trees and the pond behind."),
  [PNEG, WNEG, "no legs merging, no extra legs, no walkers appearing or vanishing, no walker reaching the lens, "
   "no strap on the bare knees, no padding, no brace"],
  "unhurried", "travels",
  [{"risk": "legs merge or multiply", "prevented_by": "one step each; no legs merging, no extra legs; NEG-WARP-C"},
   {"risk": "the straps turn into braces or spread to other knees", "prevented_by": "the strap is locked line; no padding, no brace, no strap appearing on the bare knees"},
   {"risk": "the camera walks back with them", "prevented_by": "RIG-R1C: the phone stays on the path, sways but never travels"}]))
c = mech("BR-20c",
  "The foot takes a step's weight on the step below, the knee bending a little, over about two seconds; a stream of red light runs down the thigh to the "
  "strap and stops dead at its top edge; below the strap the tendon stays cool, pale and unlit the whole time." + LOCK,
  fr("BR-20c", "CLOSE, held at the start frame's size: the one anatomical leg with the strap, the step below."),
  ["no push, no zoom, no red below the strap, no red on the tendon, no strap growing, no metal clips, no strap glowing, no strap moving, no second leg, no real skin"],
  [{"risk": "the strap is redrawn as the camera closes in (BR-14b v5's fault)", "prevented_by": "RIG-RVD lateral drift, no push, no zoom; the strap is locked line"},
   {"risk": "the red runs on into the tendon", "prevented_by": "stops dead at the strap's top edge; no red below the strap"},
   {"risk": "a second leg appears (the image's earlier fault)", "prevented_by": "no second leg; HOLD-AC"}])
j = json.loads(c["prompt"]); j["camera"]["movement"] = S("RIG-RVD")
for x in ["no static camera, ", "no tripod, ", "no whip pan, ", "no orbit completing a full revolution, ", "no camera crossing behind the target, ",
          "no arrows, ", "no motion lines, ", "no labels, ", "no numbers, ", "no individual muscle fibres, ", "no flat illustration, ",
          "no cartoon look, ", "no vignette, ", "no people, ", "no breath sway, ", "no focus hunt, "]:
    assert x in j["negatives"], x; j["negatives"] = j["negatives"].replace(x, "")
c["prompt"] = json.dumps(j, ensure_ascii=False, separators=(",", ":"))
C["BR-20c"] = (1, 1, c)
for b, (v, g, c) in C.items():
    assert c["start_image"] == board(b)["imageUrl"], b
    c["generation"] = g; c["video_version"] = v
    if g == 2: c["fix_note"] = "v1 ran on the old towpath frame → the new confirmed park frame (four walkers, the strap on the two near knees)"
    name = f"{b}.call.json" if v == 1 else f"{b}.v{v}.call.json"
    (here / "video" / name).write_text(json.dumps(c, ensure_ascii=False, indent=1)); print(f"{name:22s} {len(c['prompt']):5d} chars  {c['duration']}s")
