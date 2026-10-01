"""HK2-01 clip gen 6 (§22X/§35A, user Fix on clip v5 "change the scroll into scrolls up slowly", 2026-10-01 — motion fault: v5 jumped and the page crowded, now one slow steady glide): confirmed start frame v11 (over her left shoulder, a formal letter open on the laptop, the closed stryde box beside it). She reads while the letter glides slowly up the whole clip; sound off."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
PLAN = "she reads while her right forefinger slides slowly up the trackpad and the letter on the screen scrolls up slowly and steadily, the typed lines gliding upward at an even, gentle pace from the first second to the last, the same lines and the same size the whole time — about three seconds, slow and smooth"
prompt = (f'For the line "{LINE}": from this frame, {PLAN}. '
          "Handheld phone over her left shoulder, a gentle breath sway, the camera stays where it is. "
          "The letter stays the same white page of typed paragraphs as it moves; the laptop, the closed black box beside it, her left hand, the desk and the brick wall stay put; two hands, every finger whole. "
          "No camera move, no zoom, no extra fingers, no screen flicker, no sound.")
call = {"beat": "HK2-01", "connector": "kling", "mode": 1, "kind": "broll", "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": "https://tempfile.redpandaai.co/kieai/329820/pipeline/HK2-01_v11.png",
        "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "audio": False,
        "prompt": prompt, "script_line": LINE, "motion_plan": PLAN, "motion_confirmed": True,
        "user_go": "user 2026-10-01: Fix on clip v5: change the scroll into scrolls up slowly",
        "taste": ["HT02", "HT12", "HT13"], "generation": 6,
        "fix_note": "motion fault (§22X): clip v5 jumped and the text crowded; user: change the scroll into scrolls up slowly → one slow, even upward glide the whole clip, same lines same size; same confirmed frame v11, sound off",
        "risks": [{"risk": "the scroll jumps or speeds up", "prevented_by": "an even, gentle pace from the first second to the last, slow and smooth"}, {"risk": "the letter turns into a different page as it scrolls", "prevented_by": "the same white page of typed paragraphs"},
                  {"risk": "the box slides or morphs", "prevented_by": "the closed black box beside it stays put"},
                  {"risk": "the camera pushes in on the screen", "prevented_by": "the camera stays where it is; no camera move, no zoom"},
                  {"risk": "fingers fuse into the trackpad", "prevented_by": "two hands, every finger whole"}]}
json.dump(call, open(D + "HK2-01.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-01.kie_prompt.txt", "w").write(prompt)
print(len(prompt))
