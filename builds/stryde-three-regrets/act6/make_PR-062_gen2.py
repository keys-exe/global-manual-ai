"""PR-062 clip gen 2 (§22X): new start frame v4 after three image Fixes; strings shared with make_act6_calls.py."""
import json, os, sys
D = os.path.dirname(os.path.abspath(__file__)) + "/"
ns = {"__file__": D + "make_act6_calls.py"}
exec(open(D + "make_act6_calls.py").read().split("B = [")[0], ns)
LOCK, HOLD_C, HOLD_HC, PHYS, CAP, NEGW, HPC = [ns[k] for k in ("LOCK", "HOLD_C", "HOLD_HC", "PHYS", "CAP", "NEGW", "HPC")]
URL = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_172625_d1d8e58f-69fe-495e-a269-c4f902201561.png"
motion = ("CONTINUING: he holds the two straps upright side by side on his palm, fronts to the lens, bands hanging below. "
          "COMPLETING: one small lift of the hand, about two seconds — the hand rises a little and settles, the straps staying exactly as they are, never turning or tipping. "
          "UNRESOLVED: he holds them still, the bands swaying a little." + HPC)
prompt = json.dumps({"shot": "act6_two_on_palm", "subject": "THE SAME HAND AND TWO STRAPS as in the start frame; unchanged in every respect.",
    "camera": {"movement": LOCK, "framing": "CU as in the start frame: eye height, square to his palm. FOCUS: both straps are sharp."},
    "motion": motion + " " + HOLD_C + " " + HOLD_HC + " " + PHYS, "lighting": CAP,
    "style": "Unremarkable phone clip, warm broken-cloud afternoon sun, no grade.",
    "negatives": NEGW + ", no turning the straps, no straps tipping over, no strap sliding off, no fingers over the straps, no third strap, no one strap only, no straps growing or shrinking, no face, no music"},
    ensure_ascii=False, separators=(",", ":"))
call = {"beat": "PR-062", "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt, "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": URL, "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": 2,
        "fix_note": "Image Fixes x3 (product -> true to size -> fit a knee): new start frame v4 (knee-sized straps, one hand). Gen 1 was made from the old v2 frame; gen 2 animates v4 with the same single palm lift, locked camera, straps rigid and never turning, size held by HOLD-PC and 'no straps growing or shrinking'.",
        "risks": [{"risk": "the straps turn or tip and are redrawn", "prevented_by": "upright and never turning or tipping; HOLD-PC"},
                  {"risk": "the straps change size again", "prevented_by": "HOLD-C/HOLD-PC; no straps growing or shrinking"},
                  {"risk": "a strap slides off the palm", "prevented_by": "small lift and settle; no strap sliding off"}]}
json.dump(call, open(D + "PR-062.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "PR-062.kie_prompt.txt", "w").write(prompt)
print("PR-062", len(prompt))
