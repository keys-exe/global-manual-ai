"""BR-057 v5 (§6A, user Fix 2026-10-01: "change the letter into a laptop, use HK2-01 as reference, show a long formal letter in the screen"):
the paper letter becomes the laptop from HK2-01 — same workroom, desk, laptop, closed stryde box, her rust-orange cuffs (Image 1 = HK2-01 v11).
A closer angle than HK2-01 so the two shots don't repeat: low over her right shoulder, the screen large. The screen text is put on afterwards
by warp (a long formal letter, exact), as HK2-01."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Most of those messages end the same way."
prompt = (f'For the line "{LINE}": the same workroom, wooden desk, silver laptop, closed black box and woman as Image 1 — her rust-orange needlecord cuffs, the brick wall, soft window light from the left. Image 1 is that scene.\n'
    "New camera: closer, low over her RIGHT shoulder, looking at the open laptop on the desk so the screen fills about half the frame, square to the lens, bright and sharp. On the screen: one long typed letter on a plain white page, many paragraphs running down to a short sign-off and a name at the bottom, the type small. Her right hand rests beside the trackpad, her left hand on the desk by the keyboard; the closed black box just visible at the right edge, soft.\n"
    "In frame: the laptop, her two hands, the edge of the box; every other surface bare. Clothing, walls and papers plain — no lettering or logos on anything but the screen; no app names, no extra fingers.")
call = {"beat": "BR-057", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": False, "body": True,
        "refs": [{"label": "HK2-01 v11 (the scene)", "kind": "plate"}],
        "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro); run on Kie (Higgsfield queue stalled earlier today)",
        "motion_plan": "From this frame: the letter scrolls slowly up to its last lines and stops on the sign-off; the camera holds.",
        "fix_note": "change the letter into a laptop, use HK2-01 as reference, show a long formal letter in the screen"}
json.dump(call, open(D + "BR-057.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-057_v5.txt", "w").write(prompt)
print(len(prompt))
