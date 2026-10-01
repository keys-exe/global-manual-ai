#!/usr/bin/env python3
"""stryde-lost-moments — Body 4 round 3 (user "CONFIRM", 2026-10-01).
End frames picked: D-01-END A, D-02-END A, D-10-END A → pinned first-and-last clips (§35A rule 3, E7).
D-06, D-08 new frames picked (A, v3) — walking (travel) → end-frame A/B pairs as edits of the picked starts.
"""
import json, pathlib
from actD import B
HERE = pathlib.Path(__file__).parent
SP = "/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actD/"
CAM = "Handheld phone, a gentle breath sway, the camera stays where it is."
PIN = {
 "D-01": ("A", 4, "travel", "They end exactly as in the end frame; the same two men, bag and trolley the whole way, the fairway unchanged. No third person, no camera move.",
          [("the men morph or swap", "the same two men, bag and trolley"), ("they overshoot", "end exactly as in the end frame"), ("pace too quick", "normal walking pace, three steps")]),
 "D-02": ("A", 3, "travel", "The feet end exactly as in the end frame; exactly two feet in the same white-and-tan shoes, the grass still. No third foot, no hopping.",
          [("extra foot", "exactly two feet; no third foot"), ("shoes change", "the same white-and-tan shoes"), ("odd gait", "one step per second, two strides")]),
 "D-10": ("B", 4, "hand_product", "It ends exactly as in the end frame; both straps keep their exact shape, the worn one still below his right kneecap, his left hand on his thigh. No strap bending, no third strap.",
          [("the held strap deforms", "both straps keep their exact shape; no strap bending"), ("worn strap slides", "the worn one still below his right kneecap"), ("extra strap", "no third strap")]),
}
END2 = {
 "D-06": ("Change only where he is: he has taken two more steps toward the lens, a little larger in the frame but still head to shins, his left leg now forward, the same bag on his right shoulder, the strap still seated below his right kneecap.",
          "Clothing and bag plain — no lettering or logos but the strap's own wordmark; no second strap."),
 "D-08": ("Change only where he is: he has taken three more steps, the empty buggy now further behind him at the left edge, his left leg now forward, the same bag on his right shoulder, the strap still seated below his right kneecap.",
          "Clothing and bag plain — no lettering or logos but the strap's own wordmark; no second strap."),
}
if __name__ == "__main__":
    for b, (pick, dur, rc, facts, risks) in PIN.items():
        p = f'For the line "{B[b]["line"]}": {B[b]["motion"]} {CAM} {facts}'
        (HERE / "prompts" / f"{b}.v1.video.txt").write_text(p)
        c = {"beat": b, "connector": "kling", "mode": 1, "kind": "broll", "prompt": p, "duration": dur, "resolution": "1080p", "aspect_ratio": "9:16",
             "start_image": SP + f"{b}.{pick}.png", "start_approved": True, "pinned": True, "end_image": SP + f"{b}-END.A.png", "end_approved": True,
             "approved_by": "user picked the start and end frames (A) + CONFIRM (2026-10-01)", "subject_motion": "travels" if rc == "travel" else "in_place",
             "prefer_multi_shots": "false", "generation": 1, "script_line": B[b]["line"], "motion_plan": B[b]["motion"], "motion_confirmed": True,
             "risk_class": rc, "pilot": "confirmed", "taste": B[b]["taste"], "risks": [{"risk": r, "prevented_by": q} for r, q in risks]}
        (HERE / "clips" / f"{b}.v1.call.json").write_text(json.dumps(c, indent=1)); print(b, len(p))
    for b, (change, plain) in END2.items():
        start = SP + f"{b}.v2.A.png"
        p = (f'For the line "{B[b]["line"]}": Keep this photo exactly as it is — the place, the camera, the light, the clothes, the strap and everything in it. '
             f'Image 1 is the photo. {change} Right hand stays on the bag strap, left arm swinging; looking ahead past the lens, smiling, mouth closed. An ordinary iPhone photo, nothing restyled. {plain}')
        (HERE / "prompts" / f"{b}-END.v74.txt").write_text(p)
        c = {"beat": f"{b}-END", "kind": "image", "mode": 1, "prompt": p, "script_line": B[b]["line"], "face": True, "room": True, "product": False,
             "body": True, "refs": [{"label": f"{b} start (picked A, v3)", "kind": "frame"}], "match": "frame", "edit_of": start,
             "taste": ["FP01", "FP03", "FP11", "HT01", "HT13"], "anatomy": False, "pair": ["gpt_image_2_5", "gpt_image_2_5"], "ref_urls": [start]}
        (HERE / "clips" / f"{b}-END.img.call.json").write_text(json.dumps(c, indent=1)); print(b + "-END", len(p))
