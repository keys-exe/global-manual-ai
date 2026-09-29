#!/usr/bin/env python3
"""Step 7 · new images after the BR-10 video Fix (the user, 2026-09-29 ~19:50 UTC: "this should be 3 separate brolls"). One render each, to the board To check.
  BR-10  keeps its confirmed image for "It was never how hard she tried."
  BR-10b "It was never a weak muscle." — same session (P-B9): her left leg held straight out from the armchair, her hand flat on the thigh as the muscle
         tightens hard under the jogging bottoms; low, profile, close.
  BR-10c "It was where the load was landing." — same day, in the hall: her left foot lands on the hall floor off the bottom stair, the left knee bending to
         take the weight; ground level, three-quarter, close.
Bases: BR-10 v2 (BR-10b), BR-05b v2 (hall paragraph, BR-10c); paragraph swaps, asserted."""
import json, pathlib, sys
here = pathlib.Path(__file__).parent
sys.path.insert(0, str(here.parent / "work")); from wardrobe import wear
OUT = {}
P = (here / "BR-10.image.v2.prompt.txt").read_text().split("\n\n"); assert P[4].startswith("A snapshot") and P[7].startswith("AVOID")
P[1] = "THE CAMERA ANGLE: the lens low, at the height of her seat, looking up at the subject, seen in profile to her leg held straight out, close. This exact angle, not a straight-on eye-level view."
P[2] = "FOCUS: her hand on her thigh is in sharp focus; the room behind falls to a soft, recognisable shape. The blur is optical: soft and round, never smeared."
P[4] = ("A snapshot from a phone held low by someone crouched beside the armchair, not looking at the screen. The woman of sixty-nine from the attached reference "
        "sheet sits in the mustard armchair, wearing a raspberry-red polo shirt under an open grey zip fleece, grey jogging bottoms and white trainers. Seen side-on "
        "and close: her LEFT leg held out straight in front of her, level with the seat, the heel of her white trainer off the rug, and her right hand laid flat "
        "on the top of her left thigh, fingers spread, as the big thigh muscle tightens hard under it — the muscle's firm rounded shape standing up clearly "
        "through the soft grey jogging bottoms, the fabric pulled smooth over it. A strong leg, held steady. Her face is out of frame above.")
P[5] = ("THE LIGHT: The bay window on the room's east wall lights her leg and hand from the left of the frame, grey even daylight through the net curtains, "
        "the problem days, so it has a lit side toward the left and a softer shadow side. The shadows fall away from that source, one way only.")
P[7] = P[7].replace("no band snapping, no logo on the band,", "no exercise band, no weights, no bare leg, no shorts, no face,")
assert "no exercise band" in P[7]
OUT["BR-10b"] = dict(v=1, refs=["d0eeaf2a-abad-4a79-a9da-624c5eef41a1", "02333782-0c9a-4696-b3f1-fcc7480fe8db"], prompt="\n\n".join(P))
H = (here / "BR-05b.image.v2.prompt.txt").read_text().split("\n\n"); assert H[3].startswith("This room is part of")
Q = [H[0],
     "THE CAMERA ANGLE: the lens down at floor level, looking up at the subject, seen from a three-quarter angle of her left foot landing off the bottom stair, close. This exact angle, not a straight-on eye-level view.",
     "FOCUS: her left knee and foot are in sharp focus; the hall behind falls to a soft, recognisable shape. The blur is optical: soft and round, never smeared.",
     H[3],
     ("A snapshot from a phone held on the hall floor by someone crouched at the foot of the stairs, not looking at the screen. Only her legs from the thigh "
      "down, in grey jogging bottoms and white trainers: she is stepping DOWN off the bottom stair onto the hall floor, caught at the moment her LEFT foot lands "
      "flat on the floorboards — the LEFT knee bending to take her whole weight, the jogging bottoms creasing over it, the landing foot square and planted — "
      "while her right foot is still on the bottom stair behind it, heel lifting. The bottom stair with its patterned runner and brass rod, the newel post and "
      "the hall floor are around her feet."),
     ("THE LIGHT: The stained-glass panel in the front door lights her legs from the right of the frame, a grey morning, a pale wash along the floorboards, "
      "so it has a lit side toward the right and a softer shadow side. The shadows fall away from that source, one way only."),
     H[6],
     ("AVOID: no AI face, no plastic skin, no extra fingers, no fused fingers, no melted hands, no CGI look, no fake commercial gloss, no moody dark grade, "
      "no glowing skin, no shadows falling in two directions, no lens flare, no face, no third leg, no extra feet, no feet sliding over the step, no stumbling, "
      "no falling, no bare legs, no strap product, no brace, no readable text, logos, brand names or labels anywhere")]
OUT["BR-10c"] = dict(v=1, refs=["176c5c39-ac17-46c4-9e9b-2c06735dc0c8"], prompt="\n\n".join(Q))
for b, o in OUT.items():
    (here / f"{b}.image.r9.prompt.txt").write_text(o["prompt"]); o["model"] = "nano_banana_pro"; print(b, len(o["prompt"]))
json.dump(OUT, open(here / "fix_r9.json", "w"), indent=1)
json.dump([{"index": 1000 + i, "params": {"model": "nano_banana_pro", "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in o["refs"]], "prompt": o["prompt"]}} for i, o in enumerate(OUT.values())],
          open(here / "fix_r9_batch.json", "w"), ensure_ascii=False)
