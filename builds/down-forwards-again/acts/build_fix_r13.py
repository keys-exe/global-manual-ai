#!/usr/bin/env python3
"""Step 7 · image Fix round 13 (the user, 2026-09-30 ~12:30 UTC: "fix those and generate the new ones").
  BR-16a v5  video Fix on v2 "show it in a like treadmill" → the scene becomes a treadmill walk. The frame is the source (§22X), so a new image first:
             an edit of the confirmed v4 (job b990bcc9, attached first) — the same volunteer, strap, lab and light — with the step and force plate
             replaced by a lab treadmill he walks on, caught mid-stride, the load curve on the monitor beside him. Its video waits for the Confirm.
Base: acts/BR-16a.image.r11.prompt.txt (paragraph swaps, asserted)."""
import json, pathlib
here = pathlib.Path(__file__).parent
P = (here / "BR-16a.image.r11.prompt.txt").read_text().split("\n\n"); assert P[3].startswith("A university gait lab") and P[4].startswith("A snapshot") and P[7].startswith("AVOID")
P[1] = "THE CAMERA ANGLE: the lens low, at knee height, level, seen side-on, in profile, of the volunteer walking on the treadmill. This exact angle, not a straight-on eye-level view."
P[3] = ("EDIT THE FIRST ATTACHED PHOTOGRAPH: keep the same gait lab, the same volunteer, his clothes, the strap on his left knee, the light and the camera "
        "height exactly as they are, and change only the equipment and his action. A university gait lab: a pale grey rubber floor, a low grey lab treadmill "
        "with a black belt and handrails at waist height running side-on across the frame, reflective markers on stands, a large monitor on a stand beside the "
        "treadmill, tall side windows.")
P[4] = P[4].replace("steps down off the low wooden step onto the force plate, side-on to us, caught as his LEFT foot lands flat on the plate and the knee bends a little to take his weight.",
                    "walks steadily on the treadmill at an easy pace, side-on to us, caught mid-stride as his LEFT foot lands on the moving belt and the knee takes his weight, "
                    "his hands swinging free by his sides, not holding the rails.")
assert "walks steadily on the treadmill" in P[4]
P[4] = P[4].replace("Behind him, soft, the monitor shows", "Beside him, soft, the monitor shows")
P[7] = P[7].replace("no treadmill, no running,", "no running, no hands on the handrails, no force plate, no wooden step,")
assert "no hands on the handrails" in P[7]
OUT = {"BR-16a": dict(v=5, refs=["b990bcc9-0dd3-4fac-91f1-2e1385b34767", "793ca329-e4b3-49fd-943c-5e97bae5366d", "c942d91d-718d-4723-b190-ad85186ac8d9"], prompt="\n\n".join(P))}
for b, o in OUT.items():
    (here / f"{b}.image.r13.prompt.txt").write_text(o["prompt"]); o["model"] = "nano_banana_pro"; print(b, o["v"], len(o["prompt"]))
json.dump(OUT, open(here / "fix_r13.json", "w"), indent=1)
json.dump([{"index": 1400 + i, "params": {"model": "nano_banana_pro", "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in o["refs"]], "prompt": o["prompt"]}} for i, o in enumerate(OUT.values())],
          open(here / "fix_r13_batch.json", "w"), ensure_ascii=False)
