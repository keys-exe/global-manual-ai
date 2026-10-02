"""HK3-03 clip gen 2 (§22X, user "make clip for HK3-03", 2026-09-30): new start frame v3 (fallen on the lounge carpet, wincing, gripping her knee); §35A form; one failed effort to rise; sound off."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "The most common regret I read is not about surgery. It is not about painkillers. It is not about waiting too long. It is about two centimetres."
PLAN = "she pushes once on the armchair seat with her right hand, lifts a few centimetres, winces harder and sinks back onto the carpet, her left hand still on her knee — one small effort, about three seconds, slow — ending seated as she was"
prompt = (f'For the line "{LINE}": from this frame, {PLAN}. '
          "Handheld phone, a gentle breath sway, the camera stays where it is, high in the doorway. "
          "She stays on the floor; the armchair, side table and telephone stay put; one slipper stays on the carpet; two hands, every finger whole. "
          "No standing up, no second person, no furniture moving, no extra fingers, no sound.")
call = {"beat": "HK3-03", "connector": "kling", "mode": 1, "kind": "broll", "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_174142_1a496eff-2af5-4884-8baa-2ee7bded827c.png",
        "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "audio": False,
        "prompt": prompt, "script_line": LINE, "motion_plan": PLAN, "motion_confirmed": True,
        "taste": ["HT02", "HT12", "HT13"], "generation": 2,
        "fix_note": "frame fault: v1 clip was made from the armchair/clock frame (user Fixes: fallen and waiting for help → in pain) → new confirmed start frame v3; one failed push up, sound off",
        "risks": [{"risk": "she stands up fully (breaks the line's helplessness)", "prevented_by": "lifts a few centimetres and sinks back; she never stands up"},
                  {"risk": "the armchair slides or deforms under her hand", "prevented_by": "the armchair, side table and telephone stay put; no furniture moving"},
                  {"risk": "hands fuse into the knee or seat", "prevented_by": "two hands, every finger whole"}]}
json.dump(call, open(D + "HK3-03.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK3-03.kie_prompt.txt", "w").write(prompt)
print(len(prompt))
