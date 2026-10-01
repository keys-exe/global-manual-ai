"""HK2-03 image v5 (§6A, user Fix 2026-10-01: "change it into a more suitable HK for HK2-01 and HK2-02"). HK2-01 = the letter on her laptop
(over her shoulder), HK2-02 = the bar chart on it (same frame). HK2-03 closes the hook on her reaction at the same desk, from the front:
"none of them are what you would expect" — she lifts her eyes from the screen, thoughtful, a little surprised. The laptop's back to the lens,
so no screen text. Image 1 = HK2-02 v10 (her, front three-quarter, the laptop and the box), Image 2 = TH-HK2 v15 (her face, the room)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": the same woman, room, desk, silver laptop and closed black stryde box as Image 1 — her face exactly as Image 2, grey hair tied back, rust-orange needlecord overshirt over a cream T-shirt, brick wall, soft window light from the left.\n'
    "New camera: closer, in front of her, slightly to her left, at eye level — her head and shoulders fill the upper two thirds of the frame, the open laptop's back edge soft in the lower right foreground, the closed box on the desk beyond it. She has just lifted her eyes from the screen and looks up past the lens to the right, both eyes on a point just off camera, thoughtful, eyebrows slightly raised, lips closed — the look of someone who has read something she did not expect. Her right hand rests on the trackpad, her left forearm on the desk.\n"
    "In frame: one woman, the laptop, the one closed box; every other surface bare. Clothing, walls and laptop lid plain — no lettering, logos or labels except the box's own wordmark; five fingers on each hand.")
call = {"beat": "HK2-03", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": True, "room": True, "product": False, "body": True,
        "refs": [{"label": "HK2-02 v10 (her, laptop, box, front three-quarter)", "kind": "plate"}, {"label": "TH-HK2 v15 (her face, the room)", "kind": "character"}],
        "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro); run on Kie (Higgsfield queue stalled today)",
        "motion_plan": "From this frame: she holds the look past the lens, then a small slow breath out through the nose; the camera holds with a slight sway.",
        "fix_note": "change it into a more suitable HK for HK2-01 and HK2-02"}
json.dump(call, open(D + "HK2-03.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-03_v5.txt", "w").write(prompt)
print(len(prompt))
