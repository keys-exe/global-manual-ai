#!/usr/bin/env python3
"""stryde-lost-moments — D-08 clip Fix (board, 2026-10-01): "fix this error".
§22X diagnosis of clip v1 (8 fps contact sheet): halfway through the clip jumps back to the start (the buggy snaps big again)
and the strap flickers onto his left leg while the legs cross. Source = the frame pair: the picked end frame (D-08-END A)
has the buggy much smaller and the path re-framed — the camera has travelled with him — while the prompt says the camera
stays where it is, so Kling bridged the two with a cut. Fix at the source: a new end frame with the camera fixed (buggy and
path exactly where they are in the start; he is two steps nearer the lens), then a new pinned clip from it."""
import json, pathlib
from actD import B
HERE = pathlib.Path(__file__).parent
SP = "/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actD/"
LINE = B["D-08"]["line"]
def write_end(start_name="D-08.v2.A.png", out="D-08-END.v74b", call="D-08-END.img2"):
    start = SP + start_name
    p = (f'For the line "{LINE}": Keep this photo exactly as it is — the camera, the place, the light, the clothes, the strap and everything in it. '
         "Image 1 is the photo. Change only where he is: he has walked two steps straight toward the camera, a little larger in the frame, "
         "still head to shins, his left leg now forward, the strap still seated just below his right kneecap. The camera has not moved: "
         "the empty buggy and the path stay exactly where and how big they are in the photo. Right hand stays on the bag strap, left arm swinging; "
         "looking ahead past the lens, smiling, mouth closed. An ordinary iPhone photo, nothing restyled. "
         "Clothing and bag plain — no lettering or logos but the strap's own wordmark; no second strap.")
    (HERE / "prompts" / f"{out}.txt").write_text(p)
    c = {"beat": "D-08-END", "kind": "image", "mode": 1, "prompt": p, "script_line": LINE, "face": True, "room": True, "product": False,
         "body": True, "refs": [{"label": f"D-08 start (picked, {start_name})", "kind": "frame"}], "match": "frame", "edit_of": start,
         "taste": ["FP01", "FP03", "FP11", "HT01", "HT13"], "anatomy": False, "pair": ["gpt_image_2_5", "gpt_image_2_5"], "ref_urls": [start],
         "fix_note": "fix this error (D-08 clip): clip jumped back mid-way and the strap flickered legs → end frame had the camera travel; new end frame with the camera fixed"}
    (HERE / "clips" / f"{call}.call.json").write_text(json.dumps(c, indent=1)); print("END", len(p))
if __name__ == "__main__":
    write_end()

# Round 2 (user "FIX THOSE", 2026-10-01): clip Fix "THE RESULT LOOK LIKE AI AND ERROR". The start frame (v3 A) has the same glossy,
# over-saturated low wide-angle look as D-HKb → restage the start the D-HKb way; the camera-fixed end frame is remade from the new pick.
def write_start2():
    from actD import C4, HKA, COURSE, TQ, WF, STRAP, R
    refs = [R("product_tq_left.jpg", "product", TQ), R("worn_front.jpg", "product", WF), R("P6-COURSE plate (buggy)", "location", COURSE),
            R("C4 Graham sheet", "character", C4), R("D-HKa (his golf bag)", "frame", HKA), R("D-05 (good-round outfit)", "frame", SP + "D-05.A.png")]
    p = f"""For the line "{LINE}": he walks toward the camera past the empty white buggy parked behind him, bag on his shoulder, mid-stride.
Medium-full shot from hip height, three-quarter front, a normal phone lens, head to feet, the buggy on the left behind him.
Image 1: the strap (three-quarter). Image 2: the strap worn. Image 3: the course and buggy. Image 4: the man. Image 5: his bag. Image 6: his outfit.
{STRAP} The same man as Image 4 in the polo and sleeveless pullover of Image 6, grey shorts, white-and-tan golf shoes, the bag of Image 5 on his right shoulder; the empty buggy of Image 3, its seats bare.
Right hand on the bag strap, left arm swinging; looking ahead, a small smile, mouth closed.
In the frame: one man, one bag, one empty buggy, the fairway; nothing else.
Soft late-afternoon light through thin cloud, muted natural colour, real skin texture. An ordinary iPhone photo, nothing retouched.
Clothing and bag plain — no lettering or logos but the strap's own wordmark."""
    (HERE / "prompts" / "D-08.v74c.txt").write_text(p)
    c = {"beat": "D-08", "kind": "image", "mode": 1, "prompt": p, "script_line": LINE, "face": True, "room": True, "product": True, "body": True,
         "refs": [{"label": r["label"], "kind": r["kind"]} for r in refs], "match": None, "edit_of": None,
         "taste": ["FP01", "FP02", "FP03", "FP07", "FP11", "FP12", "HT01", "HT06", "HT18"], "anatomy": False, "pair": ["gpt_image_2_5", "gpt_image_2_5"],
         "motion_plan": "From this frame: he walks on past the empty buggy toward the camera at a normal walking pace, three steps, about three seconds.",
         "ref_urls": [r["url"] for r in refs],
         "fix_note": "THE RESULT LOOK LIKE AI AND ERROR → glossy/saturated low wide-angle frame + camera-travel end frame → restaged: hip height, normal lens, soft late light; end frame camera-fixed"}
    (HERE / "clips" / "D-08.img3.call.json").write_text(json.dumps(c, indent=1)); print("START2", len(p))

# Round 3 (user "No buggy — MAKE A BROLL HERE", 2026-10-01): end frame A picked → the clip, generation 2, pinned start A (v5) → end A.
def write_clip():
    from actD_v4 import CAM
    motion = "From this frame: he walks on past the empty buggy toward the camera at a normal walking pace, two steps, about three seconds."
    facts = ("He ends exactly as in the end frame; the same man, bag on his right shoulder and the strap below his right kneecap the whole way, "
             "on his right leg only; the empty buggy parked and still. One continuous shot, no cut. No second person.")
    p = f'For the line "{LINE}": {motion} {CAM} {facts}'
    (HERE / "prompts" / "D-08.v2.video.txt").write_text(p)
    c = {"beat": "D-08", "connector": "kling", "mode": 1, "kind": "broll", "prompt": p, "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
         "start_image": SP + "D-08.v3.A.png", "start_approved": True, "pinned": True, "end_image": SP + "D-08-END.v3.A.png", "end_approved": True,
         "approved_by": "user picked the restaged start (A) and the camera-fixed end frame (A) on the board (2026-10-01)", "subject_motion": "travels",
         "prefer_multi_shots": "false", "generation": 2,
         "fix_note": "THE RESULT LOOK LIKE AI AND ERROR: glossy low wide-angle frames + camera-travel end frame (clip cut back halfway, strap flickered legs) → natural restaged start + camera-fixed end frame, one continuous shot, strap on the right leg only",
         "script_line": LINE, "motion_plan": motion, "motion_confirmed": True, "risk_class": "travel", "pilot": "confirmed", "taste": ["HT01", "HT12", "HT18"],
         "risks": [{"risk": "mid-clip cut back to the start", "prevented_by": "camera-fixed end frame; one continuous shot, no cut"},
                   {"risk": "strap swaps legs", "prevented_by": "on his right leg only"},
                   {"risk": "buggy moves", "prevented_by": "the empty buggy parked and still"}]}
    (HERE / "clips" / "D-08.v2.call.json").write_text(json.dumps(c, indent=1)); print("CLIP", len(p))
