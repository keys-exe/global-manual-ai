#!/usr/bin/env python3
"""Step 7 · video Fixes (the user, 2026-09-30 ~12:50 UTC: "fix those and generate the new ones").
  BR-14b v5 "this is not the right image to genrate the video" — MY FAULT: v4 was sent from the old live-action frame (a stale START entry in the
    builder chain), not the confirmed anatomy frame v3. Same motion as v4 (the red turns cool blue at the strap), now from the confirmed frame.
    From here on every call's start_image is read from the board's imageUrl and asserted (START_FROM_BOARD below).
  BR-22b v3 "just showing them no other movement": v2 still let one band sag → nothing in the scene moves; only the phone's slight handheld sway.
Third+ videos of these cards: user_go = the message above."""
import json, pathlib, glob
here = pathlib.Path(__file__).parent
src = (here / "build_act5_videos.py").read_text()
exec(compile(src[:src.index("\nC = {}")].replace("__file__", repr(str(here / "build_act5_videos.py"))), "build_act5_videos", "exec"))
BOARD = "/tmp/claude-0/-home-user-global-manual-ai/33ac0ea1-56e5-53d2-9765-ab6fc866d4ca/scratchpad/g17/generations"
def board(b): return json.load(open(f"{BOARD}/down-forwards-again__{b}.json"))
for b in ["BR-14b", "BR-22b"]:
    d = board(b); assert d["imageStatus"] == "confirmed", b; START[b] = d["imageUrl"]  # START_FROM_BOARD: the confirmed frame, never a stale entry
GO = "the user, 2026-09-30 ~12:50 UTC: 'fix those and generate the new ones' — asked for this card's Fix"
C = {}
C["BR-14b"] = (5, 5, ("this is not the right image to genrate the video",
  "v4 was sent from the old live-action frame by mistake → the same blue-at-the-strap motion from the confirmed anatomy frame (v3)"),
  mech("BR-14b",
  "The foot lands on the step; a stream of red light runs down the thigh and, the moment it meets the strap, turns cool calm blue, spreading softly "
  "blue round the shell and the band, over about two seconds; below the strap the tendon and the joint stay cool pale blue. The strap is solid, keeps "
  "its exact shape, size and wordmark.",
  fr("BR-14b", "CLOSE, as in the start frame: the anatomical knee with the strap, the step below."),
  ["no red below the strap, no red on the tendon, no strap moving, no strap turning translucent, no wordmark changing, no real skin, no live-action leg"],
  [{"risk": "the wrong start frame again (the user's fault)", "prevented_by": "start_image read from the board's confirmed imageUrl and asserted"},
   {"risk": "the red stays red past the strap", "prevented_by": "turns cool blue the moment it meets the strap; no red below the strap"},
   {"risk": "the strap melts into the anatomy", "prevented_by": "the strap is solid, keeps its shape; no strap turning translucent"}]))
C["BR-22b"] = (3, 3, ("just showing them no other movement",
  "v2 still let one band sag → nothing in the scene moves at all; only the phone's slight handheld sway"),
  broll("BR-22b",
  "Nothing in the scene moves: the copy straps, their limp bands and the plastic bag lie exactly as they are on the table for the whole clip; only the "
  "phone's slight natural handheld sway.",
  fr("BR-22b", "CLOSE, as in the start frame: the copy straps over the table edge, the bag behind."),
  ["no strap moving, no band moving, no sagging, no sliding, no swinging, no jumping, no bag moving, no wordmark, no logo, no text on the copies, no hands"],
  "unhurried", "still",
  [{"risk": "a band moves (the user's fault)", "prevented_by": "nothing in the scene moves; no band moving, no sagging"},
   {"risk": "a wordmark appears on the copies", "prevented_by": "no wordmark, no logo, no text on the copies"},
   {"risk": "the camera drifts away", "prevented_by": "RIG-R1C: slight handheld sway only"}]))
for b, (v, g, (fault, note), c) in C.items():
    assert c["start_image"] == board(b)["imageUrl"], b
    c.update(generation=g, video_version=v, user_fault=fault, fix_note=note, user_go=GO)
    (here / "video" / f"{b}.v{v}.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print(f"{b}.v{v} {len(c['prompt'])} chars {c['duration']}s")
