#!/usr/bin/env python3
"""Step 7 · video Fixes (the user, 2026-09-30 ~12:30 UTC: "fix those and generate the new ones"; board Fix notes). §22X: fault diagnosed, fixed in
the motion, never the same prompt resent.
  PR-12 v3 (gen 2 on its frame) "just let move it infront dont turn it": v2 tipped the strap towards the light → she moves it straight across in front of
    her, from beside her face to in front of her chest, its front face square to the lens the whole time, never turned or tilted.
  BR-22b v2 (gen 2) "dont make the strap jump": v1's band jumped as it slid → nothing moves suddenly; one limp band only sags slowly a little lower
    over the edge; everything else lies still.
Writes acts/video/<beat>.v<n>.call.json."""
import json, pathlib
here = pathlib.Path(__file__).parent
src = (here / "build_act5_videos.py").read_text()
exec(compile(src[:src.index("\nC = {}")].replace("__file__", repr(str(here / "build_act5_videos.py"))), "build_act5_videos", "exec"))
C = {}
C["PR-12"] = (3, 2, ("just let move it infront dont turn it",
  "v2 tipped the strap towards the light and back → a straight sideways move in front of her, the front face square to the lens throughout, no turn, no tilt"),
  broll("PR-12",
  "She moves the strap slowly straight across in front of her, from beside her face down to in front of her chest, over about two seconds, its front "
  "face square to the lens the whole time and the wordmark readable; she holds it still there with a small smile." + PROD,
  fr("PR-12", "MEDIUM, as in the start frame: her from the waist up at the kitchen window, the strap small in her hand."),
  [PNEG, "no turning, no tilting, no rotating, no strap growing, no strap coming towards the lens, no fingers across the wordmark, no speaking"],
  "unhurried", "in_place",
  [{"risk": "the strap turns or tilts (the user's fault)", "prevented_by": "a straight sideways move, front face square to the lens; no turning, no tilting"},
   {"risk": "the strap grows as it moves", "prevented_by": "moves across, never towards the lens; no strap growing"},
   {"risk": "the wordmark smears", "prevented_by": "product-constancy line; product negatives"}]))
C["BR-22b"] = (2, 2, ("dont make the strap jump",
  "v1's band jumped as it slid off the edge → no sudden movement: one limp band only sags slowly a little lower; everything else lies still"),
  broll("BR-22b",
  "Almost still: one limp stretched band hanging over the table edge sags slowly a little lower under its own weight, over about three seconds; nothing "
  "else moves; the copies and the plastic bag lie still on the table.",
  fr("BR-22b", "CLOSE, as in the start frame: the copy straps over the table edge, the bag behind."),
  ["no jumping, no bouncing, no sudden movement, no strap flicking, no strap falling, no swinging, no wordmark, no logo, no text on the copies, no hands"],
  "unhurried", "in_place",
  [{"risk": "a strap jumps (the user's fault)", "prevented_by": "almost still, one slow sag; no jumping, no sudden movement"},
   {"risk": "a wordmark appears on the copies", "prevented_by": "no wordmark, no logo, no text on the copies"},
   {"risk": "the bands stretch in motion", "prevented_by": "sags a little only; NEG-WARP-C"}]))
for b, (v, g, (fault, note), c) in C.items():
    c.update(generation=g, video_version=v, user_fault=fault, fix_note=note)
    (here / "video" / f"{b}.v{v}.call.json").write_text(json.dumps(c, ensure_ascii=False, indent=1)); print(f"{b}.v{v} {len(c['prompt'])} chars {c['duration']}s")
