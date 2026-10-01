"""BR-057 clip gen 3 (§22X/§35A, user Fix on clip v4 "the hand must scroll up along with the screen", 2026-10-01 — motion fault: the
composite moved only the page, her hand stayed still). Kling animates the hand only: two fingers slide slowly up the trackpad, camera
locked so the screen stays where it is; start frame = the confirmed v6 render with the screen blank (BR-057_v6.png), so Kling has no
text to redraw. The letter is put back afterwards frame by frame, scrolling with the fingers (make_BR-057_clip_v5.py)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Most of those messages end the same way."
PLAN = "her right forefinger and middle finger slide slowly and steadily up the trackpad in one even stroke, from its lower half to its upper half, about three seconds, the wrist following; her hand stays on the trackpad the whole time"
prompt = (f'For the line "{LINE}": from this frame, {PLAN}. '
          "The camera is locked off on a tripod at desk height and stays perfectly still. "
          "The laptop screen stays plain bright white and evenly lit; the laptop, the closed black box behind it, the desk and the brick wall stay put; one hand, five whole fingers. "
          "No camera move, no zoom, no screen flicker, no sound.")
call = {"beat": "BR-057", "connector": "kling", "mode": 1, "kind": "broll", "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": "BR-057_v6.png (confirmed v6 render, screen blank; the letter is composited back)",
        "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "audio": False,
        "prompt": prompt, "script_line": LINE, "motion_plan": PLAN, "motion_confirmed": True,
        "user_go": "user 2026-10-01: Fix on clip v4: the hand must scroll up along with the screen",
        "taste": ["HT02", "HT12", "HT13"], "generation": 3,
        "fix_note": "motion fault (§22X): clip v4 scrolled the page with the hand still; the user wants the fingers to scroll with it → Kling animates a slow two-finger upward stroke on a locked camera, the letter composited back in step with it",
        "risks": [{"risk": "the camera drifts so the screen corners move", "prevented_by": "locked off on a tripod, stays perfectly still; no camera move, no zoom"},
                  {"risk": "Kling draws content on the screen", "prevented_by": "the laptop screen stays plain bright white"},
                  {"risk": "the stroke is fast or jerky", "prevented_by": "slowly and steadily, one even stroke, about three seconds"},
                  {"risk": "fingers fuse into the trackpad", "prevented_by": "one hand, five whole fingers"},
                  {"risk": "the box slides or morphs", "prevented_by": "the closed black box behind it stays put"}]}
json.dump(call, open(D + "BR-057.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-057.kie_prompt.txt", "w").write(prompt)
print(len(prompt))
