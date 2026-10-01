#!/usr/bin/env python3
"""Step 7 · BR-10c image v6 (hourly Fix check 2026-10-01 11:41 UTC; board Fix note on v5: "MAKE THIS A CLOSE UP SHOT AND PATELLAR TENDON").
v5 framed the whole leg and the brightest spot sat on the kneecap. v6: an image edit of v5 (attached), the camera moved in to a close-up of
the knee only — from just above the kneecap to the top of the shin, front-on — so the patellar tendon is large in the frame, and the red
taken off the kneecap and put on the tendon (HT11, HT21). Model per the build's lock: nano_banana_pro. Its video (Kling) follows the Confirm."""
import json, pathlib
here = pathlib.Path(__file__).parent
EDIT = ("EDIT THE ATTACHED IMAGE: keep the same anatomical style, colours, light and dark background, and move the camera in to a CLOSE-UP of the "
        "knee only, seen from the front: the frame runs from a hand's width above the kneecap down to the top of the shin, the knee filling the "
        "frame. In the middle of the frame, the patellar tendon — the short, thumb-wide cord from the kneecap's lower tip down to the bump at the "
        "top of the shin bone — is large and clear, and it is the one bright red spot in the frame, near-white at its core. The kneecap above it is "
        "plain ivory with no glow on it; the red light comes down the thigh muscle above as a soft stream and lands on the tendon.")
P = (here / "BR-10c.image.r21.prompt.txt").read_text().split("\n\n")
P[0] = ("Premium 3D anatomical visualisation for medical education, broadcast-quality CGI render, clean. Vertical composition. A close-up of a "
        "stylised anatomical model of ONE left knee, seen from the front, filling the frame. Deep near-black background with a faint cool blue tint. "
        "The outer body contour is a very faint translucent glass-like shell.")
P.insert(1, EDIT)
t = "\n\n".join(P)
for o, n in [("The shin and foot below stay calm and unlit.", "The shin below stays calm and unlit."),
             ("The foot stands planted and the body's weight is arriving down the leg:", "The body's weight is arriving down the leg:"),
             ("AVOID: no side view,", "AVOID: no foot, no whole leg, no step, no wide shot, no glow on the kneecap's face, no side view,")]:
    assert t.count(o) == 1, o; t = t.replace(o, n)
OUT = {"BR-10c": dict(v=6, refs=["538cbd5a-94cb-441b-82e2-62e6441edf3f"], prompt=t, model="nano_banana_pro")}
(here / "BR-10c.image.r22.prompt.txt").write_text(t); json.dump(OUT, open(here / "fix_r22.json", "w"), indent=1); print("BR-10c v6", len(t))
