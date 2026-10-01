#!/usr/bin/env python3
"""Step 7 · videos on the images the user confirmed on the board (2026-10-01: "fix those and generate the next videos"): BR-16a v6 and BR-23 v4.
Start images read from the board's confirmed imageUrl and asserted. Same stack as acts/build_act5_videos.py; preflight before any credit.
  BR-16a v3 (gen 3, new treadmill frame; user_go = the message above): he walks steadily on the treadmill, the curve rises on the monitor.
  BR-23  v2 (gen 2, new frame going up): one easy step up towards the landing, hands free, a small smile; the camera stays on the landing.
Writes acts/video/<beat>.v<n>.call.json."""
import json, pathlib
here = pathlib.Path(__file__).parent
src = (here / "build_act5_videos.py").read_text()
exec(compile(src[:src.index("\nC = {}")].replace("__file__", repr(str(here / "build_act5_videos.py"))), "build_act5_videos", "exec"))
BOARD = "/tmp/claude-0/-home-user-global-manual-ai/33ac0ea1-56e5-53d2-9765-ab6fc866d4ca/scratchpad/g25/generations"
def board(b): return json.load(open(f"{BOARD}/down-forwards-again__{b}.json"))
for b in ["BR-16a", "BR-23"]:
    d = board(b); assert d["imageStatus"] == "confirmed", b; START[b] = d["imageUrl"]
GO = "the user, 2026-10-01: 'fix those and generate the next videos' — the card's new image confirmed on the board"
LOCK = " The strap is locked: small black shell below the kneecap, thin band, same size and wordmark as the start frame throughout."
C = {}
C["BR-16a"] = (3, 3, "v1/v2 were the step-and-force-plate scene → the new confirmed treadmill frame (the user's 'show it in a like treadmill')", broll("BR-16a",
  "He walks steadily on the moving treadmill belt at an easy pace, two even strides over about three seconds, arms swinging loosely, staying in "
  "place; the curve on the monitor rises once." + LOCK,
  fr("BR-16a", "FULL, as in the start frame: him side-on on the treadmill."),
  [PNEG, WNEG, "no silver dots on his body, no hands on the handrails, no stepping off, no running, no numbers on the monitor, no strap growing, no brace"],
  "unhurried", "in_place",
  [{"risk": "the silver markers come back (the user's image fault)", "prevented_by": "no reflective markers, no silver dots on his body"},
   {"risk": "he walks off the treadmill or the camera follows", "prevented_by": "staying in the same place on the treadmill; RIG-R1C sways but never travels"},
   {"risk": "the legs cross or the strap slides", "prevented_by": "two even strides; worn-constancy line; NEG-WARP-C"}]))
C["BR-23"] = (2, 2, "v1 had her coming down → the new confirmed frame going up (the user's 'she should be going up normally she is not touching the hand rail')", broll("BR-23",
  "She takes one more easy step UP the stairs towards the landing at a normal pace, over about a second and a half, both hands swinging free "
  "away from the banister, a small smile; still mid-flight on the last frame." + LOCK,
  fr("BR-23", "FULL, as in the start frame: her whole body on the stairs, seen from the landing above."),
  [PNEG, WNEG, "no hand on the rail, no coming down, no turning round, no reaching the landing, no feet through the treads, no strap growing, no brace"],
  "unhurried", "travels",
  [{"risk": "she touches the rail (the user's fault)", "prevented_by": "both hands swinging free, away from the banister; no hand on the rail"},
   {"risk": "she reaches the camera or the camera backs away", "prevented_by": "one step only, still mid-flight; RIG-R1C: the phone stays on the landing"},
   {"risk": "the strap turns into a block (the image fault)", "prevented_by": "the strap is locked line; no strap growing, no padding, no brace"}]))
for b, (v, g, note, c) in C.items():
    assert c["start_image"] == board(b)["imageUrl"], b
    c.update(generation=g, video_version=v, fix_note=note)
    if g >= 3: c["user_go"] = GO
    (here / "video" / f"{b}.v{v}.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print(f"{b}.v{v} {len(c['prompt'])} chars {c['duration']}s")
