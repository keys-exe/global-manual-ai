"""BR-057 v6 (§6A, user Fix 2026-10-01: "change camera angle"): v5 was close over her shoulders from behind (the same side as HK2-01/HK2-02).
New angle: low, from her right side at desk height — the open laptop in the foreground, its screen turned about 40 degrees toward the lens,
her right hand on the trackpad, her rust-orange cuff, the closed box behind. The screen is asked blank white; the same long letter
(ref/BR-057_letter_ref.png) is warped on afterwards (make_BR-057_v6_screen.py), so it stays word for word. Image 1 = BR-057 v5 (the laptop,
desk, cuffs), Image 2 = HK2-01 v11 (the room and the box)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Most of those messages end the same way."
prompt = (f'For the line "{LINE}": the same silver laptop, wooden desk, rust-orange needlecord cuffs and hands as Image 1, and the same room and closed black box as Image 2 — brick wall, soft window light from the left. Copy them exactly.\n'
    "New camera angle: low, from her right side at desk height, close. The open laptop is in the foreground on the left half of the frame, its screen turned about 40 degrees toward the lens, large and sharp, lit and plain blank white from edge to edge. Her right hand rests on the trackpad, her rust-orange cuff and forearm coming in from the right edge. Behind the laptop, soft and out of focus, the closed black box on the desk with its lowercase grey stryde wordmark, and the brick wall.\n"
    "In frame: the laptop, her right hand and forearm, the one closed box; every other surface bare. Clothing, packaging and walls plain — no lettering, logos or labels except the box's own wordmark; five fingers on the hand.")
call = {"beat": "BR-057", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": False, "body": True,
        "refs": [{"label": "BR-057 v5 (laptop, desk, cuffs)", "kind": "plate"}, {"label": "HK2-01 v11 (room, box)", "kind": "plate"}],
        "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro); run on Kie (Higgsfield queue stalled today); screen text warped in afterwards",
        "motion_plan": "From this frame: the letter scrolls slowly up to its last lines and stops on the sign-off; the camera holds (composited — the letter stays word for word).",
        "fix_note": "change camera angle"}
json.dump(call, open(D + "BR-057.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "BR-057_v6.txt", "w").write(prompt)
print(len(prompt))
