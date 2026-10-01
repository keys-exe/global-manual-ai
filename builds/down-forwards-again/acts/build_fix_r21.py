#!/usr/bin/env python3
"""Step 7 · BR-10c image v5 (the user, 2026-10-01, board Fix note: "USE NEW IMAGE HERE ALSO USE KLING FOR VIDEO"). A new image, not an edit:
the camera moves to the FRONT of the knee (front three-quarter, close), so the patellar tendon — the cord from the kneecap's lower tip to the
bump on the shin bone — faces the lens and the red lands on it unmistakably (HT11: the named structure exactly; HT21: the subject fills the
frame; HT12: one whole leg). The leg stands planted on the step (no step-up for the video to invent, v2's fault). Model per the build's lock
(nano_banana_pro, anatomy). Its video goes through the Kling connector after the user's confirm.
Base: acts/BR-10c.image.r18.prompt.txt with the edit paragraph dropped and the framing replaced (exact replacements asserted)."""
import json, pathlib
here = pathlib.Path(__file__).parent
def rep(t, pairs):
    for o, n in pairs:
        assert t.count(o) == 1, o[:80]; t = t.replace(o, n)
    return t
P = (here / "BR-10c.image.r18.prompt.txt").read_text().split("\n\n")
assert P[1].startswith("EDIT THE ATTACHED IMAGE"); del P[1]
t = "\n\n".join(P)
t = rep(t, [("A stylised anatomical model of ONE left leg seen close from a low three-quarter front angle, framed from mid-thigh down to the foot, the foot just landing flat on the edge of a simple dark step, the knee bending a little to take the weight, the knee large in the middle of the frame, the other leg entirely out of frame.",
             "A stylised anatomical model of ONE left leg seen from the FRONT, a slight three-quarter turn, the camera at knee height, close: framed from mid-thigh down to the foot, the foot standing planted flat on a simple dark step, the knee straight with a soft bend, the knee and the patellar tendon large in the middle of the frame and facing the lens, the other leg entirely out of frame."),
            ("STATE — WHERE THE LOAD LANDS. The foot has just landed and the body's weight is arriving down the leg:",
             "STATE — WHERE THE LOAD LANDS. The foot stands planted and the body's weight is arriving down the leg:"),
            ("AVOID: ", "AVOID: no side view, no profile, no back of the knee, ")])
OUT = {"BR-10c": dict(v=5, refs=[], prompt=t)}
(here / "BR-10c.image.r21.prompt.txt").write_text(t); OUT["BR-10c"]["model"] = "nano_banana_pro"; print("BR-10c v5", len(t))
json.dump(OUT, open(here / "fix_r21.json", "w"), indent=1)
