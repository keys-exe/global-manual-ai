"""HK2-01 clip gen 8 (user "make clip for HK2-01", 2026-10-01, image v12 = the user's own image). LESSONS L09: Kling animates the hand only —
her right fingers slide up the trackpad — on a locked camera, start frame = the user's image with the screen whitened (HK2-01_v12_blank.png);
the user's page (ref/HK2-01_v12_page.png) is put back per frame, scrolling with the hand (make_HK2-01_clip_v8.py)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
PLAN = "her right forefinger and middle finger slide slowly and steadily up the trackpad in one even stroke, from its lower half to its upper half, about three seconds, the wrist following; her left hand stays resting on the edge of the laptop"
prompt = (f'For the line "{LINE}": from this frame, {PLAN}. '
          "The camera is locked off on a tripod over her right shoulder and stays perfectly still. "
          "The laptop screen stays plain bright white and evenly lit; the laptop, the closed black box behind it, the desk, the pinboard and the brick wall stay put; two hands, every finger whole. "
          "No camera move, no zoom, no screen flicker, no sound.")
call = {"beat": "HK2-01", "connector": "kling", "mode": 1, "kind": "broll", "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": "HK2-01_v12_blank.png (the user's image v12 with the screen whitened; their page is composited back)",
        "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "audio": False,
        "prompt": prompt, "script_line": LINE, "motion_plan": PLAN, "motion_confirmed": True,
        "user_go": "user 2026-10-01: make clip for HK2-01 (on their own image v12)",
        "taste": ["HT02", "HT12", "HT13"], "generation": 8,
        "fix_note": "new image v12 (the user's own) replaces v11; LESSONS L09 (a still hand under a scrolling screen) → Kling animates the hand stroke only, locked camera, blank screen; the user's page composited back scrolling with the hand",
        "risks": [{"risk": "the camera drifts so the screen corners move", "prevented_by": "locked off on a tripod, stays perfectly still; no camera move, no zoom"},
                  {"risk": "Kling draws content on the screen", "prevented_by": "the laptop screen stays plain bright white"},
                  {"risk": "the stroke is fast or jerky", "prevented_by": "slowly and steadily, one even stroke, about three seconds"},
                  {"risk": "fingers fuse into the trackpad", "prevented_by": "two hands, every finger whole"},
                  {"risk": "the box slides or morphs", "prevented_by": "the closed black box behind it stays put"}]}
json.dump(call, open(D + "HK2-01.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-01.kie_prompt.txt", "w").write(prompt)
print(len(prompt))
