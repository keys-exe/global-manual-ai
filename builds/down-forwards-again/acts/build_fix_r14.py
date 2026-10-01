#!/usr/bin/env python3
"""Step 7 · image Fix round 14 (the user, 2026-09-30 ~12:50 UTC: "fix those and generate the new ones").
  BR-23 v3  video Fix "she should be going up normally she is not touching the hand rail" → the confirmed frame has her coming DOWN; going up needs a
            new frame (§22X: fix at the source): the lens on the landing at the top, looking down the flight; she climbs UP towards it at a normal pace,
            hands free and off the rail, a small smile. Act-map row updated (high · front · FULL; angles PASS). Its video waits for the Confirm.
Base: the board's v2 prompt (acts/BR-23.image.v2.board.prompt.txt), paragraph swaps asserted."""
import json, pathlib
here = pathlib.Path(__file__).parent
def rep(t, pairs):
    for o, n in pairs:
        assert t.count(o) == 1, o[:80]; t = t.replace(o, n)
    return t
P = (here / "BR-23.image.v2.board.prompt.txt").read_text().split("\n\n"); assert P[4].startswith("A snapshot") and P[7].startswith("AVOID")
P[1] = "THE CAMERA ANGLE: the lens above her, on the landing at the top of the stairs, looking down at the subject, seen from the front of the woman climbing up the stairs towards it. This exact angle, not a straight-on eye-level view."
i = P[4].find("She is at the very TOP"); j = P[4].find("a small private smile.") + len("a small private smile.")
P[4] = rep(P[4][:i] + ("She is going UP her stairs at a normal, easy pace, about halfway up the flight, facing up the stairs towards the lens, caught mid-step as "
       "her LEFT foot lands on the tread above and the LEFT knee bends to lift her, both hands swinging free at her sides, well away from the banister and "
       "not touching the rail, her face lifted towards the landing with a small private smile, the rest of the flight dropping away below and behind her.") + P[4][j:],
       [("held at hip height by someone standing at the foot of the stairs, off to one side, looking up the whole flight,",
         "held by someone standing on the landing at the top of the stairs, looking down the flight at her,")])
P[5] = ("THE LIGHT: The tall landing window behind the phone lights her from the right of the frame, morning sun, a warm patch on the stairs, the after, so "
        "the face has a lit side toward the right and a softer shadow side, with a small catchlight in the eyes. The shadows fall away from that source, one way only.")
P[7] = rep(P[7], [("no hand on the rail, no bottom of the stairs, no woman near the hall floor, no walking backwards,",
                   "no hand on the rail, no hand on the banister, no coming down, no back to the camera, no woman at the top of the stairs, no walking backwards,")])
OUT = {"BR-23": dict(v=3, refs=["75cc01d9-d616-477a-9d0e-51fc89823ad0", "c942d91d-718d-4723-b190-ad85186ac8d9", "793ca329-e4b3-49fd-943c-5e97bae5366d",
                                "02333782-0c9a-4696-b3f1-fcc7480fe8db", "176c5c39-ac17-46c4-9e9b-2c06735dc0c8"], prompt="\n\n".join(P))}
OUT["BR-23"]["prompt"] = OUT["BR-23"]["prompt"].replace("THE SAME WOMAN exactly as in the attached reference sheet", "THE SAME WOMAN, in the same clothes, as in the first attached photograph and the attached reference sheet", 1)
assert "first attached photograph" in OUT["BR-23"]["prompt"]
for b, o in OUT.items():
    (here / f"{b}.image.r14.prompt.txt").write_text(o["prompt"]); o["model"] = "nano_banana_pro"; print(b, o["v"], len(o["prompt"]))
json.dump(OUT, open(here / "fix_r14.json", "w"), indent=1)
json.dump([{"index": 1500 + i, "params": {"model": "nano_banana_pro", "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in o["refs"]], "prompt": o["prompt"]}} for i, o in enumerate(OUT.values())],
          open(here / "fix_r14_batch.json", "w"), ensure_ascii=False)
