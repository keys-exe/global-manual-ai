#!/usr/bin/env python3
"""Step 7 · image Fix round 7 (the user, 2026-09-29 ~19:00 UTC): "BR-04 this is the point she should be pressuring her finger" + a second photo
(refs/BR-04_point_ref2.png, Higgsfield media 8227e906…): a head-on, knee-height close-up of a seated older woman's bent knee, the pressing tip on the
front of the knee right under the centre of the kneecap. That photo becomes the BASE of the edit — its framing, the knee and the tip's exact spot kept;
the pressing hand becomes her own right hand; her clothes and chair swapped for hers (P-B2, the front room's mustard armchair).
Base prompt: acts/BR-04.image.r6.prompt.txt; the camera, focus and prose paragraphs are rewritten, the rest kept."""
import json, pathlib
here = pathlib.Path(__file__).parent
REF2 = "8227e906-5c92-428a-b483-c699d956d55f"
P = (here / "BR-04.image.r6.prompt.txt").read_text().split("\n\n")
assert P[1].startswith("THE CAMERA ANGLE") and P[4].startswith("EDIT THE FIRST") and P[7].startswith("AVOID")
P[1] = ("THE CAMERA ANGLE: exactly the framing of the FIRST attached photograph — the lens at the height of her knee, level, close and square in front of "
        "her bent knee, the knee filling the middle of the frame head-on, her lap and hands soft above it, the shin running down to the bottom edge. "
        "Keep that framing exactly. This exact angle, not a straight-on eye-level view.")
P[2] = "FOCUS: the kneecap and the pressing fingertip are in sharp focus; her lap and the chair behind fall soft. The blur is optical: soft and round, never smeared."
P[4] = ("EDIT THE FIRST ATTACHED PHOTOGRAPH. Keep its composition exactly: the bent knee head-on in the middle of the frame, the rounded kneecap, and the "
        "pressing fingertip in EXACTLY the same spot on the knee as in that photograph — on the front of the knee, in the soft band directly below the "
        "centre of the kneecap (the patellar tendon), the kneecap sitting right above the tip, the skin dimpling round it. Do not move the tip. "
        "Change only these: the pressing hand is now HER OWN right hand, coming in from the right of the frame in the same place, its forefinger doing the "
        "pressing — thin skin, a plain gold wedding band, the cuff of a rust jersey sleeve; nobody else is in the picture. She is the woman of sixty-nine from "
        "the attached reference sheet, face out of frame above: she wears a rust long-sleeve jersey top and a knee-length camel corduroy skirt, its hem pushed "
        "back above the knee by her left hand, bare legs — slim, pale, a little swollen at the knee, fine creases, faint thread veins. She sits in the mustard "
        "armchair of the attached front-room photograph instead of the sofa, the patterned rug below.")
P[7] = P[7].replace("no man, no hairy legs, no shorts, no khaki, no olive t-shirt, no white socks, no staircase, no wooden floor,",
                    "no second person, no green sleeve, no man, no fleece jacket, no black shorts, no trousers, no rust sofa, no thumb pressing,")
P[7] = P[7].replace("no finger pointing sideways, ", "").replace("no finger coming down from above, ", "")  # the reference's hand comes in from the side
assert "no second person" in P[7] and "pointing sideways" not in P[7]
txt = "\n\n".join(P); (here / "BR-04.image.r7.prompt.txt").write_text(txt)
refs = [REF2, "d0eeaf2a-abad-4a79-a9da-624c5eef41a1", "02333782-0c9a-4696-b3f1-fcc7480fe8db"]
json.dump({"BR-04": dict(v=9, src="BR-04.image.r6.prompt.txt", model="nano_banana_pro", ref_jobs=refs, chars=len(txt), prompt=txt)}, open(here / "fix_r7.json", "w"), indent=1)
json.dump([{"index": 800, "params": {"model": "nano_banana_pro", "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in refs], "prompt": txt}}], open(here / "fix_r7_batch.json", "w"), ensure_ascii=False)
print(json.dumps(txt))
