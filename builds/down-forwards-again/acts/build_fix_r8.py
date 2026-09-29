#!/usr/bin/env python3
"""Step 7 · new images after the Act 1 video Fixes (the user, 2026-09-29 ~19:30 UTC). One render each; they go to the board To check before any video.
  BR-05a video "this should be 2 brolls" → NEW BR-05 ("Coming down is worse than going up."): at the top of the flight, looking down it, hesitating,
          seen from the landing behind her (high / three-quarter-back). BR-05a keeps its confirmed image for "Going up, your muscles lift you."
  MECH-03 video "this should be cut into 4 brolls" → NEW MECH-03a ("Two centimetres below your kneecap": front view, one small spot marked below the
          kneecap), NEW BR-03b ("there is a band of tendon about as wide as your thumb.": edit of the confirmed BR-04 v9 — her thumb laid across the band),
          MECH-03 keeps its confirmed image ("Every step you take lands on it."), NEW MECH-03d ("Seventeen times your bodyweight.": the whole bent leg
          at peak load, the band blazing).
  MECH-05 video "new image and mechanism here" → NEW MECH-05 image: close on the knee as the foot lands on the step; the catch drives down onto the band,
          which flares at the landing.
Bases: BR-05b v2 (BR-05), BR-04 r7 (BR-03b), MECH-03 v2 (the three anatomy beats); paragraph swaps and exact replacements, asserted."""
import json, pathlib, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here.parent / "work")); from wardrobe import wear
def paras(f): return (here / f).read_text().split("\n\n")
def rep(t, pairs):
    for o, n in pairs:
        assert t.count(o) == 1, o[:80]; t = t.replace(o, n)
    return t
OUT = {}
# ---- BR-05 -------------------------------------------------------------------------------------------------------------------
P = paras("BR-05b.image.v2.prompt.txt"); assert P[1].startswith("THE CAMERA ANGLE") and P[4].startswith("A snapshot") and P[7].startswith("AVOID")
P[1] = ("THE CAMERA ANGLE: the lens above head height, looking down at the subject, seen from a three-quarter angle behind her, over the top of the flight "
        "and down the stairs below her. This exact angle, not a straight-on eye-level view.")
P[4] = ("A snapshot from a phone held high by someone standing on the landing just behind her, not looking at the screen. THE SAME WOMAN exactly as in the "
        "attached reference sheet — a white British woman of sixty-nine, short and petite with a slight stoop, a small fine-boned oval face, pale grey-blue eyes, "
        "a small straight nose, a thin upper lip with a small mole above its right corner, chin-length layered hair dyed chestnut brown with silver roots at the "
        "parting, tucked behind the ears — unchanged in face, age and build; only her clothes are different today. " + wear("BR-05") + " She has reached the TOP "
        "of her stairs and stopped at the edge of the landing, about to come down: both hands grip the banister rail, the toes of her slippers at the edge of the "
        "top step, and she looks down the long flight below her, hesitating, her shoulders drawn up, her head bowed towards the drop, her face turned in "
        "three-quarter profile, tight and wary, mouth shut. The whole flight falls away below her, steep, down to the hall floor and the front door. Her whole "
        "body from hair to slippers is in frame.")
P[5] = ("THE LIGHT: The tall landing window behind her lights her from the left of the frame, grey even daylight of a grey morning, a pale wash down the "
        "runner below, so she has a lit side toward the left and a softer shadow side. The shadows fall away from that source, one way only.")
P[7] = rep(P[7], [("no walking backwards,", "no step taken yet, no foot off the top step, no walking backwards, no hand off the rail,")])
OUT["BR-05"] = dict(v=1, refs=["176c5c39-ac17-46c4-9e9b-2c06735dc0c8", "02333782-0c9a-4696-b3f1-fcc7480fe8db"], prompt="\n\n".join(P))
# ---- BR-03b (edit of the confirmed BR-04 v9) ---------------------------------------------------------------------------------
P = paras("BR-04.image.r7.prompt.txt"); assert P[4].startswith("EDIT THE FIRST") and P[7].startswith("AVOID")
P[2] = "FOCUS: the kneecap and her thumb lying across the band under it are in sharp focus; her lap and the chair behind fall soft. The blur is optical: soft and round, never smeared."
P[4] = ("EDIT THE FIRST ATTACHED PHOTOGRAPH. Keep everything in it exactly as it is — the framing, her bent knee head-on, her rust jersey sleeve and wedding band, "
        "her camel corduroy skirt and the hand on its hem, the mustard armchair, the rug, the room and the light — and change only the pose of the pressing "
        "hand: instead of pressing with a fingertip, her right hand now lies with its THUMB laid flat and crosswise over the front of the knee, in the soft "
        "band directly below the centre of the kneecap, so the thumb's width covers that band exactly from its top edge to its bottom edge — the kneecap sitting "
        "right above the thumb, the thumbnail facing the lens, her fingers curled loosely round the outer side of the knee. Nothing else changes.")
P[7] = rep(P[7], [("no thumb pressing,", "no fingertip pressing, no thumb pointing up or down, no thumb on the kneecap,"),
                  ("no finger moved from where the photograph has it,", "no thumb off the band,")])
OUT["BR-03b"] = dict(v=1, refs=["7527b4ef-2b3e-43c6-b59f-5e39cb223893", "d0eeaf2a-abad-4a79-a9da-624c5eef41a1", "02333782-0c9a-4696-b3f1-fcc7480fe8db"],
                     prompt="\n\n".join(P))
# ---- anatomy -----------------------------------------------------------------------------------------------------------------
M = (here / "MECH-03.image.v2.prompt.txt").read_text()
FRAME = "in true lateral profile, edge-on, the limb running vertically, framed from mid-thigh to mid-shin and dominating the frame, the limb falling away out of frame at both ends."
assert M.count(FRAME) == 1
SP = [p for p in M.split("\n\n") if p.startswith("STATE —")]; assert len(SP) == 1; STATE = SP[0]
def mech(frame, state, extra=()):
    t = M.replace(FRAME, frame).replace(STATE, state)
    return rep(t, list(extra))
OUT["MECH-03a"] = dict(v=1, refs=[], prompt=mech(
  "seen from straight in front, the kneecap facing the lens, framed close from just above the kneecap to the top of the shin and dominating the frame, the limb falling away out of frame at both ends.",
  "STATE — AT REST, ONE SPOT MARKED. The knee is straight and at rest, no load on it. The only emission is one small, tight, glowing red spot a thumb's width "
  "below the lower tip of the kneecap, on the patellar tendon, on the centre line of the knee, near-white at its core — marking the place. Everything else "
  "stays calm: the kneecap plain unlit ivory above it, the bones and muscles uncoloured beyond a faint warm spill."))
OUT["MECH-03d"] = dict(v=1, refs=[], prompt=mech(
  "seen from a low three-quarter angle, the whole left leg from the hip to the foot, the knee deeply bent as the leg takes the body's full weight stepping down onto a simple dark step, the leg dominating the frame.",
  "STATE — AT PEAK LOAD. The body's whole weight bears down through the deeply bent leg: the thigh muscles drawn long and taut to brake it, the knee compressed, "
  "and the patellar tendon under the kneecap blazing at full intensity, near-white at its core and hot red around it, a deep-red bloom spreading into the tissue "
  "round it — by far the brightest thing in frame, the peak. The rest of the anatomy stays calm by comparison, uncoloured beyond a warm spill.",
  [("no limb falling off into darkness,", "no limb falling off into darkness, no text, no numbers,")]))
OUT["MECH-05"] = dict(v=2, refs=[], prompt=mech(
  "seen from a low three-quarter front angle, close on the left knee: the lower thigh, the kneecap, the patellar tendon and the top of the shin dominating the frame, the foot just landing on the edge of a simple dark step below, the limb falling away out of frame above.",
  "STATE — THE CATCH. The foot has just landed on the step below and the knee is bending under the arriving weight: the quadriceps above drawn long and taut to "
  "brake the descent, the kneecap pulled down into its groove, and the load arriving all at once on the patellar tendon below it — the tendon flares bright "
  "red, near-white at its core, at the instant of the landing, sudden and sharp-edged, the brightest thing in frame. The bones and the muscles around it stay "
  "calm by comparison."))
for b, o in OUT.items():
    assert "[" not in o["prompt"], b
    (here / f"{b}.image.r8.prompt.txt").write_text(o["prompt"]); o["model"] = "nano_banana_pro"; print(f"{b:8s} v{o['v']} {len(o['prompt']):5d}")
json.dump(OUT, open(here / "fix_r8.json", "w"), indent=1)
json.dump([{"index": 900 + i, "params": {"model": "nano_banana_pro", "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in o["refs"]], "prompt": o["prompt"]}} for i, o in enumerate(OUT.values())],
          open(here / "fix_r8_batch.json", "w"), ensure_ascii=False)
