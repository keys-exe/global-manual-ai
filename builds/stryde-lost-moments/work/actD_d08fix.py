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
def write_end():
    start = SP + "D-08.v2.A.png"
    p = (f'For the line "{LINE}": Keep this photo exactly as it is — the camera, the place, the light, the clothes, the strap and everything in it. '
         "Image 1 is the photo. Change only where he is: he has walked two steps straight toward the camera, a little larger in the frame, "
         "still head to shins, his left leg now forward, the strap still seated just below his right kneecap. The camera has not moved: "
         "the empty buggy and the path stay exactly where and how big they are in the photo. Right hand stays on the bag strap, left arm swinging; "
         "looking ahead past the lens, smiling, mouth closed. An ordinary iPhone photo, nothing restyled. "
         "Clothing and bag plain — no lettering or logos but the strap's own wordmark; no second strap.")
    (HERE / "prompts" / "D-08-END.v74b.txt").write_text(p)
    c = {"beat": "D-08-END", "kind": "image", "mode": 1, "prompt": p, "script_line": LINE, "face": True, "room": True, "product": False,
         "body": True, "refs": [{"label": "D-08 start (picked A, v3)", "kind": "frame"}], "match": "frame", "edit_of": start,
         "taste": ["FP01", "FP03", "FP11", "HT01", "HT13"], "anatomy": False, "pair": ["gpt_image_2_5", "gpt_image_2_5"], "ref_urls": [start],
         "fix_note": "fix this error (D-08 clip): clip jumped back mid-way and the strap flickered legs → end frame had the camera travel; new end frame with the camera fixed"}
    (HERE / "clips" / "D-08-END.img2.call.json").write_text(json.dumps(c, indent=1)); print("END", len(p))
if __name__ == "__main__":
    write_end()
