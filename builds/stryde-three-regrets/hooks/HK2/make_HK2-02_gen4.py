"""HK2-02 clip gen 4 (§22X, user_go): start image v9, a long formal typed letter at the bare desk; strings shared with act6/make_act6_calls.py."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
A6 = D + "../../act6/make_act6_calls.py"
ns = {"__file__": A6}
exec(open(A6).read().split("HPC =")[0], ns)
R1C, HOLD_C, HOLD_HC, PHYS, CAP, NEGW = [ns[k] for k in ("R1C", "HOLD_C", "HOLD_HC", "PHYS", "CAP", "NEGW")]
URL = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260929_202914_ed0c8b59-b0f5-48c7-8de7-b22afb73f54c.png"
motion = ("CONTINUING: she holds the long typed letter up in both hands, reading. "
          "COMPLETING: one slow read down the page, about two seconds — her head tilts a little lower as her eyes move down the letter, the sheet tipping slightly towards her. "
          "UNRESOLVED: she keeps reading near the bottom of the page, still.")
prompt = json.dumps({"shot": "hk2_formal_letter_read",
    "subject": "THE SAME WOMAN, DESK AND LONG TYPED LETTER as in the start frame; unchanged in every respect. The page stays a full page of small typed lines that cannot be read, in every frame.",
    "camera": {"movement": R1C, "framing": "CU as in the start frame: over her right shoulder, the letter in her hands, the bare desk below. FOCUS: her hands and the sheet are sharp."},
    "motion": motion + " " + HOLD_C + " " + HOLD_HC + " " + PHYS, "lighting": CAP,
    "style": "Unremarkable phone clip, soft cool morning window light, no grade.",
    "negatives": NEGW + ", no readable words, no words forming or changing, no page turning, no second sheet, no folding, no stacks of letters, no pinboard, no face to the lens, no talking, no music"},
    ensure_ascii=False, separators=(",", ":"))
call = {"beat": "HK2-02", "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt, "duration": 3, "resolution": "1080p", "aspect_ratio": "9:16",
        "start_image": URL, "start_approved": True, "pinned": False, "subject_motion": "in_place", "prefer_multi_shots": "false", "generation": 4,
        "user_go": "user 2026-09-29: \"MAKE CLIP FOR HK2-02\" (after image v9, told it would be the 4th generation)",
        "fix_note": "frame fault: gen 3 animated the three-stacks frame, then the user asked for a formal letter, no stacks, unreadable, long (image Fixes 7-9) → new start image v9, a long formal typed letter at the bare desk, confirmed by the user; motion is one slow read down the page",
        "risks": [{"risk": "the type turns readable or morphs", "prevented_by": "subject: small typed lines that cannot be read in every frame; no readable words, no words forming or changing"},
                  {"risk": "the page turns, folds or doubles", "prevented_by": "no page turning, no second sheet, no folding; HOLD-C"},
                  {"risk": "fingers fuse with the paper", "prevented_by": "HOLD-HC"}]}
json.dump(call, open(D + "HK2-02.call.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-02.kie_prompt.txt", "w").write(prompt)
print("HK2-02", len(prompt))
