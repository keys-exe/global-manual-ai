"""HK2-02 v15 (§6A, user Fix 2026-10-01: "change camera angle"): v14 was the HK2-01 frame (over her LEFT shoulder) — the same angle as
HK2-01 and HK2-03. New angle: over her RIGHT shoulder, higher and closer, looking down at the open laptop, the screen large and blank white;
the long letter (ref/HK2-02_letter_ref.png) is warped on afterwards (make_HK2-02_v15_screen.py). Image 1 = HK2-01 v11 (her, the room, the
laptop, the box), Image 2 = TH-HK2 v15 (her overshirt, hair and the room from the front)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": the same workroom, wooden desk, silver laptop and closed black stryde box as Image 1 — her grey hair tied back and rust-orange needlecord overshirt from behind as Image 2, brick wall, soft window light from the left.\n'
    "New camera angle: over her RIGHT shoulder, higher and closer, looking down at the open laptop at about 40 degrees. Her right shoulder and the back of her head soft at the right edge; the screen large in the middle of the frame, turned slightly toward the lens, lit and plain blank white from edge to edge. Her right hand rests on the trackpad, her left hand on the keyboard. The closed black box on the desk to the right of the laptop, its lowercase grey stryde wordmark on the lid.\n"
    "In frame: her back, shoulder and hands, the laptop, the one closed box; every other surface bare. Clothing, packaging and walls plain — no lettering, logos or labels except the box's own wordmark; five fingers on each hand.")
call = {"beat": "HK2-02", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": False, "body": True,
        "refs": [{"label": "HK2-01 v11 (her, room, laptop, box)", "kind": "plate"}, {"label": "TH-HK2 v15 (her overshirt, hair, room)", "kind": "plate"}],
        "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro); run on Kie (Higgsfield queue stalled today); screen text warped in afterwards",
        "motion_plan": "From this frame: her fingers slide up the trackpad and the letter scrolls up with them; the camera holds (the letter composited, word for word).",
        "fix_note": "change camera angle"}
json.dump(call, open(D + "HK2-02.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-02_v15.txt", "w").write(prompt)
print(len(prompt))
