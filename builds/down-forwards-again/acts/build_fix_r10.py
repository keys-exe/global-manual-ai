#!/usr/bin/env python3
"""Step 7 · image Fix round 10 (the user, 2026-09-29 ~20:10 UTC: "fix and generate the act 4 videos"; board Fix notes). One render each, to the board To check.
  BR-06 v5  "she should be half way down so we can emphasize the going down backwards" → halfway down the flight (about eight steps up), facing the
            steps, the stairs above AND below her in frame. (Its video Fix waits for this image.)
  BR-15 v2  "generate a new image for this different concept" → her own knee with the strap on it, her fingertip resting on the notch where it meets the
            kneecap's lower edge (placement checked on her; was the doctor's finger on a desk model). Act-map row + wardrobe (P-A2) updated.
  PR-12 v4  "this is too big the product" — three renders framed on the hand still read big → frame her from the waist up at the kitchen window, the
            strap held up beside her face, so her body sets the scale (a tenth of the frame's width).
  MECH-03 v3 (video Fix "make a new image") → the whole leg in profile taking one ordinary walking step, heel strike, the band lighting at mid
            intensity — to carry "Every step you take lands on it." with the normal walk the user asked for.
Bases: BR-06 v4, BR-13 v2 (BR-15), PR-12 v3, MECH-03 v2; paragraph swaps and exact replacements, asserted."""
import json, pathlib, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here.parent / "work")); from wardrobe import wear
def rep(t, pairs):
    for o, n in pairs:
        assert t.count(o) == 1, o[:80]; t = t.replace(o, n)
    return t
SLIM = (" On the leg it is a small, slim strap: the shell is only about three centimetres tall — shorter than the kneecap — and hugs the front of the knee "
        "just below it; the band is a narrow strip round the leg. It looks light and discreet, never chunky, never a big block on the knee.")
OUT = {}
OUT["BR-06"] = dict(v=5, refs=["176c5c39-ac17-46c4-9e9b-2c06735dc0c8", "02333782-0c9a-4696-b3f1-fcc7480fe8db"], prompt=rep((here / "BR-06.image.v4.prompt.txt").read_text(), [
 ("facing the steps, four steps above the hall floor,", "facing the steps, HALFWAY down the flight — about eight steps above the hall floor, as many stairs below her as above her,"),
 ("Her whole body from hair to feet is in frame, the flight rising behind her to the landing.",
  "Her whole body from hair to feet is in frame, in the middle of the flight: the stairs rising above her to the landing and the stairs dropping away below her to the hall floor, both in frame."),
 ("no facing forwards,", "no woman near the bottom of the stairs, no woman near the top of the stairs, no facing forwards,")]))
P = (here / "BR-13.image.v2.prompt.txt").read_text().split("\n\n"); assert P[4].startswith("A snapshot") and P[7].startswith("AVOID")
P[1] = "THE CAMERA ANGLE: the lens above her knee, looking down at the subject, seen from a three-quarter angle of her left knee, close. This exact angle, not a straight-on eye-level view."
P[2] = "FOCUS: her fingertip on the strap's notch is in sharp focus; the room behind falls to a soft, recognisable shape. The blur is optical: soft and round, never smeared."
P[4] = rep(P[4], [("A snapshot from a phone held at knee height by someone crouched beside her,", "A snapshot from a phone held above her knee by someone standing beside her,"),
                  ("the bare knee filling the middle of the frame, still, resting.",
                   "her LEFT knee close in the middle of the frame, and her right forefinger resting lightly on the centre of the strap's notch, just where it meets "
                   "the lower edge of her kneecap — checking that it sits right there, on the tendon, not a centimetre higher. Her face is out of frame above."),
                  ("Her hands rest on her thigh above the knee, not touching the strap.", "Her left hand rests on her thigh; only the right forefinger touches the strap, lightly, at the notch.")]) + SLIM
P[7] = rep(P[7], [("no hands on the strap,", "no finger on the kneecap face, no finger pressing the kneecap, no hand covering the wordmark, no hand gripping the strap, "
                   "no oversized strap, no chunky strap, no strap taller than the kneecap,")])
OUT["BR-15"] = dict(v=2, refs=["c942d91d-718d-4723-b190-ad85186ac8d9", "793ca329-e4b3-49fd-943c-5e97bae5366d", "02333782-0c9a-4696-b3f1-fcc7480fe8db", "d0eeaf2a-abad-4a79-a9da-624c5eef41a1"],
                    prompt="\n\n".join(P))
P = (here / "PR-12.image.v3.prompt.txt").read_text().split("\n\n"); assert P[4].startswith("A snapshot") and P[7].startswith("AVOID")
P[1] = "THE CAMERA ANGLE: the lens at the subject's eye height, level, seen from the front of the woman at the kitchen window holding up the strap. This exact angle, not a straight-on eye-level view."
P[2] = "FOCUS: the product and its wordmark is in sharp focus; her face and the kitchen behind fall a little soft. The blur is optical: soft and round, never smeared."
P[4] = rep(P[4], [("A snapshot from a phone held at eye height by someone standing across from her, not looking at the screen. An older woman's hand — thin skin, a plain gold wedding band, the rolled cuff of a cornflower-blue linen shirt — holds her knee strap up into the window light at arm's length, its front face square to the lens; her hand, wrist and forearm and the kitchen around them are in frame, the strap a small object in the middle of the picture, taking up about a quarter of the frame's width.",
  "A snapshot from a phone held at eye height by someone standing across the kitchen from her, not looking at the screen. The woman of sixty-nine from the attached "
  "reference sheet, seen from the waist up standing by the kitchen window — " + wear("PR-12").replace("She wears ", "wearing ").rstrip(".") + ", a plain gold wedding band — holds her "
  "knee strap up beside her face in the window light, its front face square to the lens, a small quiet smile. Her upper body, her face and the kitchen around her "
  "are in frame; the strap is a small object between her fingers, no wider than her palm and far narrower than her face — about a tenth of the frame's width.")])
P[7] = rep(P[7], [("no face, no packaging,", "no packaging, no strap as wide as her face, no strap held close to the lens,")])
OUT["PR-12"] = dict(v=4, refs=["c942d91d-718d-4723-b190-ad85186ac8d9", "4a56cffe-69bc-4f77-ac90-38258b124e65", "abc2c220-b0f0-43d2-b583-d22b5696225b", "02333782-0c9a-4696-b3f1-fcc7480fe8db"],
                    prompt="\n\n".join(P))
M = (here / "MECH-03.image.v2.prompt.txt").read_text()
FRAME = "in true lateral profile, edge-on, the limb running vertically, framed from mid-thigh to mid-shin and dominating the frame, the limb falling away out of frame at both ends."
ST = [p for p in M.split("\n\n") if p.startswith("STATE —")][0]
OUT["MECH-03"] = dict(v=3, refs=[], prompt=rep(M, [(FRAME,
  "in true lateral profile: the whole left leg from the hip to the foot, walking, caught at the moment the heel strikes a simple dark floor at an ordinary walking pace — the knee almost straight with only a slight bend, the leg dominating the frame."),
  (ST, "STATE — ONE ORDINARY STEP LANDING. As the heel lands and the weight comes onto the leg, the patellar tendon under the kneecap lights red along its "
       "whole length, clearly glowing, near-white at its core, mid-intensity — an ordinary step, not a heavy load. The bones and the muscles stay calm by comparison.")]))
for b, o in OUT.items():
    assert "[" not in o["prompt"], b
    (here / f"{b}.image.r10.prompt.txt").write_text(o["prompt"]); o["model"] = "nano_banana_pro"; print(f"{b:8s} v{o['v']} {len(o['prompt']):5d}")
json.dump(OUT, open(here / "fix_r10.json", "w"), indent=1)
json.dump([{"index": 1100 + i, "params": {"model": "nano_banana_pro", "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in o["refs"]], "prompt": o["prompt"]}} for i, o in enumerate(OUT.values())],
          open(here / "fix_r10_batch.json", "w"), ensure_ascii=False)
