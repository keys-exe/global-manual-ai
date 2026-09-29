"""BR-003 clip gen 2 (§22X): start image v2 after the user's Fix (drawer physics); strings shared with act6/make_act6_calls.py."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
A6 = D + "../act6/make_act6_calls.py"
ns = {"__file__": A6}
exec(open(A6).read().split("HPC =")[0], ns)
R1C, HOLD_C, HOLD_HC, PHYS, CAP, NEGW = [ns[k] for k in ("R1C", "HOLD_C", "HOLD_HC", "PHYS", "CAP", "NEGW")]
URL = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_204021_dc89a3d7-c7bd-46a4-92a4-ae49e93e79e7.png"
motion = ("CONTINUING: her hand is on the knob of the open top drawer. "
          "COMPLETING: one pull, about two seconds — the drawer slides straight out a little further on its runners, level and square, with a small catch as it sticks and then gives, the pile of supports jostling inside. "
          "UNRESOLVED: she holds the drawer open, looking down into it.")
prompt = json.dumps({"shot": "act1_drawer_pull",
    "subject": "THE SAME WOMAN, CHEST OF DRAWERS AND BEDROOM as in the start frame; unchanged in every respect.",
    "camera": {"movement": R1C, "framing": "MEDIUM as in the start frame: eye height, three-quarter-back, the chest and the room beyond. FOCUS: her hand and the drawer are sharp."},
    "motion": motion + " " + HOLD_C + " " + HOLD_HC + " " + PHYS, "lighting": CAP,
    "style": "Unremarkable phone clip, grey flat late-morning daylight from the window on the right, no grade.",
    "negatives": NEGW + ", no drawer coming out of the chest, no drawer tilting or floating, no chest tipping or sliding, no other drawers moving, no supports falling out, no talking, no face to the lens, no music"},
    ensure_ascii=False, separators=(",", ":"))
call = {"beat": "BR-003", "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt, "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": URL, "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": 2,
        "fix_note": "frame fault: v1 drawer skewed and floating, wider than the chest (user Fix: proper physics) → new start image v2, drawer level in its runners, confirmed by the user; motion keeps the drawer rigid and in its opening",
        "risks": [{"risk": "the drawer comes out or floats", "prevented_by": "a short pull on its runners; no drawer coming out, no tilting or floating"},
                  {"risk": "the chest warps or tips", "prevented_by": "HOLD-C; no chest tipping or sliding, no other drawers moving"},
                  {"risk": "the supports spill", "prevented_by": "no supports falling out"}]}
json.dump(call, open(D + "BR-003.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-003.kie_prompt.txt", "w").write(prompt)
print("BR-003", len(prompt))
