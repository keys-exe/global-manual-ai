"""HK2-03 clip gen 5 (§22X, user's go "MAKE CLIP FOR HK2-03", 2026-09-30): start frame v3 (edit of HK2-01 v4: her hands dividing the letters into three piles). §35A form; sound off."""
import json, os, shutil
D = os.path.dirname(os.path.abspath(__file__)) + "/"
if not os.path.exists(D + "HK2-03_g4.call.json"):
    shutil.copy(D + "HK2-03.call.json", D + "HK2-03_g4.call.json")
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
PLAN = "her right hand sets the last handful of letters down on the third pile — one set-down, about two seconds — ending with three separate piles in a row and both hands at rest"
prompt = (f'For the line "{LINE}": from this frame, {PLAN}. '
          "The sheets sag a little and settle flat. "
          "Handheld phone, a gentle breath sway, the camera stays where it is, low at desk height. "
          "Exactly three piles the whole time, the same grey trays full of the same white typed letters, every finger whole and separate. "
          "No fourth pile, no letters flying, no handwriting, no readable text, no sound.")
call = {"beat": "HK2-03", "connector": "kling", "mode": 1, "kind": "broll", "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260930_164750_cd5eff63-cbc2-4020-8ef0-0220cb43b7ad.png",
        "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "audio": False,
        "prompt": prompt, "script_line": LINE, "motion_plan": PLAN, "motion_confirmed": True,
        "taste": ["HT04", "HT12", "HT13", "HT18", "HT19"], "generation": 5,
        "user_go": "MAKE CLIP FOR HK2-03 (user in chat, 2026-09-30, after the image v4 Fix CHANGE CAMERA ANGLE; also taken as the Confirm of image v4 and its motion line)",
        "fix_note": "frame fault: the user fixed the image (CHANGE CAMERA ANGLE) — gen 4 was made from the overhead v3 frame → new start frame v4 at desk height, three-quarter front; same single set-down on the third pile, the camera clause now low at desk height; §35A, sound off",
        "risks": [{"risk": "a fourth pile appears or the piles merge", "prevented_by": "exactly three piles the whole time; no fourth pile"},
                  {"risk": "fingers fuse into the paper", "prevented_by": "every finger whole and separate"},
                  {"risk": "the typed letters morph into handwriting", "prevented_by": "same white typed letters; no handwriting, no readable text"}]}
json.dump(call, open(D + "HK2-03.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-03.kie_prompt.txt", "w").write(prompt)
print(len(prompt))
