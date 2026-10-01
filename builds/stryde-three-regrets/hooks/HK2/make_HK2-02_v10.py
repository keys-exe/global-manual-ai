"""HK2-02 v10 (§6A, user Fix 2026-10-01: "make it suitable to HK2-01"): HK2-01 now shows the formal letter open on her laptop (over her left
shoulder, the closed stryde box beside it). HK2-02 joins it: the same desk, laptop and box, the camera in front of her at three-quarters, her face
reading the screen — the laptop's back to the lens, so no screen text. Image 1 = TH-HK2 v15 (her, the room, the laptop, the box, as confirmed);
Image 2 = HK2-01 v11 (the laptop and the box from the other side)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": the same woman, room, desk, silver laptop and closed black stryde box as Image 1 — her grey hair tied back, rust-orange needlecord overshirt over a cream T-shirt, the brick wall and pinboard, soft window light from the left. Image 1 is that scene; Image 2 is the same laptop and box seen over her shoulder.\n'
    "New camera: in front of her at three-quarters, eye level, closer — her head and shoulders and the open laptop fill the frame, its back to the lens. She reads the letter on the screen: eyes down on the screen, lips closed, a small frown of attention, her right hand on the trackpad, her left hand resting on the desk. The closed black box lies on the desk beside the laptop, its lowercase grey stryde wordmark on the lid.\n"
    "In frame: one woman, the laptop, the one closed box; every other surface bare. Clothing, walls and papers plain — no lettering or logos except the box's own wordmark; no extra fingers.")
call = {"beat": "HK2-02", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": False, "body": True,
        "refs": [{"label": "TH-HK2 v15 (her, the room, laptop, box)", "kind": "plate"}, {"label": "HK2-01 v11 (laptop + box from behind)", "kind": "plate"}],
        "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro); run on Kie (Higgsfield queue stalled today)",
        "motion_plan": "From this frame: she reads on, her eyes moving down the screen line by line, then a slow breath; the camera holds.",
        "fix_note": "make it suitable to HK2-01"}
json.dump(call, open(D + "HK2-02.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-02_v10.txt", "w").write(prompt)
print(len(prompt))
