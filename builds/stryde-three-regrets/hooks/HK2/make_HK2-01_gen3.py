"""HK2-01 clip gen 3 (§22X/§35A, user "make clip for HK2-01", 2026-10-01 — their go for a third generation): new confirmed start frame v6 (over her shoulder, the STRYDE review page on the laptop); a fast scroll of the page; sound off."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
PLAN = "her right fingers flick down the trackpad twice and the page on the screen scrolls fast upward, review after review sliding past — the same white page, round photos, gold stars and short quotes — about two seconds, fast, then it slows to a stop on another review"
prompt = (f'For the line "{LINE}": from this frame, {PLAN}. '
          "Handheld phone over her right shoulder, a gentle breath sway, the camera stays where it is. "
          "Only the page on the screen moves; the laptop, her left hand, the desk and the brick wall stay put; two hands, every finger whole. "
          "No camera move, no zoom, no extra fingers, no screen flicker, no sound.")
call = {"beat": "HK2-01", "connector": "kling", "mode": 1, "kind": "broll", "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20261001_101938_ae40b51c-fe63-4bcf-9030-82287f93594a.png",
        "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "audio": False,
        "prompt": prompt, "script_line": LINE, "motion_plan": PLAN, "motion_confirmed": True, "user_go": "user 2026-10-01: make clip for HK2-01 (new confirmed frame v6)",
        "taste": ["HT02", "HT12", "HT13"], "generation": 3,
        "fix_note": "new shot (user Fixes: a fast scroll in the laptop, reviews / survey answers, TH-HK2 as background, their review page on screen) → confirmed start frame v6; one fast scroll, sound off",
        "risks": [{"risk": "the camera pushes in on the screen instead of holding", "prevented_by": "the camera stays where it is; no camera move, no zoom"},
                  {"risk": "the page turns into a different layout as it scrolls", "prevented_by": "the same white page, round photos, gold stars and short quotes"},
                  {"risk": "fingers fuse into the trackpad", "prevented_by": "two hands, every finger whole"}]}
json.dump(call, open(D + "HK2-01.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-01.kie_prompt.txt", "w").write(prompt)
print(len(prompt))
