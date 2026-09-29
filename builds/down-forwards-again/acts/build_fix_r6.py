#!/usr/bin/env python3
"""Step 7 · image Fix round 6 (hourly Fix check, 2026-09-29 ~18:45 UTC). One new render.
  BR-04 "the patellar tendon is below the center of the knee cap. will never be at the side fix this" — seven text-led renders kept drifting the finger to the
        side of the knee. Fixed at the source: the user's own photo of the point (refs/BR-04_point_ref.png, Higgsfield media 6a2715d9…) becomes the BASE of an
        edit — its framing, knee and fingertip position are kept exactly; only the person, clothes and room are swapped for hers.
Base prompt: acts/BR-04.image.r5.prompt.txt; edits are exact replacements, asserted."""
import json, pathlib
here = pathlib.Path(__file__).parent
POINT_REF = "6a2715d9-de51-420d-844b-99abba716adb"
t = (here / "BR-04.image.r5.prompt.txt").read_text()
P = t.split("\n\n")
assert P[1].startswith("THE CAMERA ANGLE") and P[4].startswith("A snapshot") and P[7].startswith("AVOID")
P[1] = ("THE CAMERA ANGLE: exactly the framing of the FIRST attached photograph — the lens a little above the seated person's knee, in front of them, looking down "
        "along the bent leg at the front of the knee and the shin, the kneecap facing the lens. Keep that framing exactly. This exact angle, not a straight-on eye-level view.")
P[2] = "FOCUS: the knee and the fingertip are in sharp focus; the room behind falls to a soft, recognisable shape. The blur is optical: soft and round, never smeared."
P[4] = ("EDIT THE FIRST ATTACHED PHOTOGRAPH. Keep its composition exactly: the bent knee in the middle of the frame, seen from the front; the forefinger coming up "
        "from below and pressing its tip into the soft dip DIRECTLY BELOW THE CENTRE OF THE KNEECAP — the patellar tendon, on the same vertical line as the middle "
        "of the kneecap, the kneecap sitting right above the fingertip — the fingertip in exactly the same place on the knee as in that photograph, never moved "
        "to the side of the knee. Change only the person, the clothes and the room: the person is now a white British woman of sixty-nine, short and petite, "
        "sitting in the mustard armchair of the front room; her legs are bare, slim and pale, a little swollen at the knee, fine creases and a few faint thread "
        "veins, almost no leg hair; the hem of her knee-length camel corduroy skirt sits a hand's width above the knee, her left hand resting on her thigh by "
        "the hem; the pointing hand is her own right hand — thin skin, a plain gold wedding band, the cuff of a rust jersey sleeve; her bare feet on the patterned "
        "rug. Her face is out of frame above.")
P[7] = P[7].replace("no man, no shorts,", "no man, no hairy legs, no shorts, no khaki, no olive t-shirt, no white socks, no staircase, no wooden floor,")
P[7] = P[7].replace("no view from directly overhead, no finger coming down from above,", "no finger coming down from above, no finger moved from where the photograph has it,")
txt = "\n\n".join(P); (here / "BR-04.image.r6.prompt.txt").write_text(txt)
out = {"BR-04": dict(v=8, src="BR-04.image.r5.prompt.txt", model="nano_banana_pro",
       ref_jobs=[POINT_REF, "d0eeaf2a-abad-4a79-a9da-624c5eef41a1", "02333782-0c9a-4696-b3f1-fcc7480fe8db"], chars=len(txt), prompt=txt)}
json.dump(out, open(here / "fix_r6.json", "w"), indent=1)
json.dump([{"index": 700, "params": {"model": "nano_banana_pro", "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in out["BR-04"]["ref_jobs"]], "prompt": txt}}], open(here / "fix_r6_batch.json", "w"), ensure_ascii=False)
print(len(txt)); print(txt)
