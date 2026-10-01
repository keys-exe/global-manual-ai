"""HK3-02 clip gen 2 (§22X, user "make clip for HK3-02", 2026-09-30): new start frame v4 (amber painkiller bottle over his open palm, one pill in it) after the image Fixes; §35A form; sound off."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "The most common regret I read is not about surgery. It is not about painkillers. It is not about waiting too long. It is about two centimetres."
PLAN = "he tilts the amber bottle a little further and one more white pill rolls out into his open palm beside the first — one small tilt, about two seconds — ending with the bottle eased back upright just above his palm"
prompt = (f'For the line "{LINE}": from this frame, {PLAN}. '
          "Handheld phone, a gentle breath sway, the camera stays where it is, looking down at his hands. "
          "The same amber bottle with its plain white label and red band, rigid, the same size; exactly two pills in his palm at the end; two hands, every finger whole and separate. "
          "No pills spilling, no lettering on the label, no bottle changing shape, no extra fingers, no sound.")
call = {"beat": "HK3-02", "connector": "kling", "mode": 1, "kind": "broll", "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_172836_d24aeaec-5899-4c19-8c5b-46642f9d1535.png",
        "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "audio": False,
        "prompt": prompt, "script_line": LINE, "motion_plan": PLAN, "motion_confirmed": True,
        "taste": ["HT04", "HT12", "HT13", "HT18"], "generation": 2,
        "fix_note": "frame fault: v1 clip was made from the foil-card frame (user Fixes: pill under the pack → a bottle → a real painkiller bottle) → new confirmed start frame v4; one small tilt, one more pill, sound off",
        "risks": [{"risk": "pills pour out in a heap", "prevented_by": "one more pill; exactly two pills at the end; no pills spilling"},
                  {"risk": "the bottle melts or the label grows text", "prevented_by": "the same amber bottle, rigid, same size; no lettering on the label"},
                  {"risk": "fingers fuse into the bottle", "prevented_by": "two hands, every finger whole and separate"}]}
json.dump(call, open(D + "HK3-02.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK3-02.kie_prompt.txt", "w").write(prompt)
print(len(prompt))
