#!/usr/bin/env python3
"""Step 7 · image Fix round 18 (the user, 2026-10-01: "fix those and generate the next videos"; board Fix note on BR-10c v3).
  BR-10c v4 "THIS SHOULD BE THE PATELLAR TENDON" → v3 lit the knee joint and the kneecap's side and back, not the tendon. An edit of v3 (attached
            first): same leg, angle, light and pulses; the red moved to the patellar tendon only — the cord on the FRONT of the knee from the kneecap's
            lower tip down to the bump on the shin bone — the kneecap, the joint and the back of the knee unlit. One render, to the board To check.
Base: acts/BR-10c.image.r12.prompt.txt (exact replacements asserted)."""
import json, pathlib
here = pathlib.Path(__file__).parent
def rep(t, pairs):
    for o, n in pairs:
        assert t.count(o) == 1, o[:80]; t = t.replace(o, n)
    return t
t = (here / "BR-10c.image.r12.prompt.txt").read_text()
P = t.split("\n\n")
P.insert(1, "EDIT THE ATTACHED IMAGE: keep the same anatomical leg, the same camera angle, framing, step, light and the red pulses in the thigh exactly as "
            "they are, and change only WHERE THE RED LANDS: take every bit of red off the kneecap, off the joint and off the back and sides of the knee, "
            "and put it on the patellar tendon only — the short, thumb-wide cord on the FRONT of the knee that runs from the kneecap's lower tip straight "
            "down to the bump at the top of the shin bone. Make that cord clearly visible on the front edge of the leg and make it the one bright red "
            "spot in the frame; the kneecap above it is plain ivory.")
t = "\n\n".join(P)
t = rep(t, [("AVOID: ", "AVOID: no red at the back of the knee, no red on the side of the knee, no red inside the joint, no red on the kneecap, no red ring round the knee, ")])
OUT = {"BR-10c": dict(v=4, refs=["e521c8c1-1999-4962-802c-9193de1d1cd5"], prompt=t)}
for b, o in OUT.items():
    (here / f"{b}.image.r18.prompt.txt").write_text(o["prompt"]); o["model"] = "nano_banana_pro"; print(b, o["v"], len(o["prompt"]))
json.dump(OUT, open(here / "fix_r18.json", "w"), indent=1)
