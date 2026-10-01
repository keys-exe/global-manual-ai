"""HK2-02 v11 (§6A, user Fix 2026-10-01: "don't show the woman, show the screen of the laptop that shows a bar chart that shows the
three things come up more than anything else"). No person: the same laptop, desk and closed stryde box as HK2-01 v11, the camera in front
of the laptop, close, its screen square to the lens and blank white. The bar chart is built in PIL and warped onto the screen afterwards
(make_HK2-02_v11_screen.py), so every word on it is exact. Image 1 = HK2-01 v11 (the scene)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": the same silver laptop, wooden desk, closed black stryde box, brick wall and soft window light from the left as Image 1, copied exactly.\n'
    "New camera: the room is empty, only the objects. The camera is in front of the open laptop, eye level with the screen, close — the screen faces the lens straight on and fills about two thirds of the frame width, its top edge level, the keyboard edge at the bottom of the frame. The screen is lit, plain blank white from edge to edge. To the right of the laptop, part of the closed black box lies on the desk, its lowercase grey stryde wordmark on the lid. Behind, the brick wall soft and out of focus.\n"
    "In frame: the laptop and the one closed box; every other surface bare; the laptop, packaging and walls plain — no lettering, logos or labels except the box's own wordmark.")
call = {"beat": "HK2-02", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": False, "body": False,
        "refs": [{"label": "HK2-01 v11 (laptop, desk, box, room)", "kind": "plate"}],
        "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro); run on Kie (Higgsfield queue stalled today); screen text warped in afterwards",
        "motion_plan": "From this frame: the three tall bars rise one after another on the screen; the camera holds with a slight breath sway.",
        "fix_note": "don't show the woman, show the screen of the laptop that shows a bar chart that shows the three things come up more than anything else"}
json.dump(call, open(D + "HK2-02.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-02_v11.txt", "w").write(prompt)
print(len(prompt))
