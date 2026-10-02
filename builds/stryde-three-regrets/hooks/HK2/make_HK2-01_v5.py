"""HK2-01 v5 (§6A, user Fix 2026-10-01: "a fast scroll in the laptop. Texts should look like reviews/post purchase survey, so they're short paragraphs. use th-hk2 as background"): a new start frame — the laptop from TH-HK2 (confirmed frame v15, Image 1) seen close over her hands, its screen a column of short customer reviews / survey answers (star row + 2–4 line paragraph each, unreadable), her room soft behind. The clip (after the image Confirm) is a fast scroll of that page."""
import json, os
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": the same room, desk, laptop and woman as Image 1 — the brick wall, pinboard, shelves, window light, the closed black box by the wall, her rust-orange needlecord cuffs. Image 1 is that room; keep its light and colour.\n'
    "The camera moves in close behind her right shoulder, looking down at the open laptop on the desk; the screen fills about half the frame, square to the lens, bright and sharp. Her hands rest at the keyboard's edge, right fingers on the trackpad. Behind the screen, the brick wall and pinboard fall soft.\n"
    "On the screen: a plain white web page of customer reviews and after-purchase survey answers — a long column of separate white cards, each a row of five small grey stars over a short paragraph of two to four lines — each card a different length, the column running off the bottom of the screen. Text soft grey and too small to read.\n"
    "In frame: the laptop, her two hands, the desk; every other surface bare. Clothing, walls and papers plain — no lettering, logos or labels; no app names, no extra fingers.")
call = {"beat": "HK2-01", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": False, "body": True,
        "refs": [{"label": "TH-HK2 frame v15 (confirmed) — the room", "kind": "plate"}],
        "taste": ["HT12", "HT17", "HT18", "HT19", "HT20"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call)",
        "motion_plan": "From this frame: her right fingers flick the trackpad and the review column scrolls fast upward through the cards; the camera holds.",
        "fix_note": "a fast scroll in the laptop; reviews / post-purchase survey, short paragraphs; TH-HK2 as background"}
json.dump(call, open(D + "HK2-01.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-01_v5.txt", "w").write(prompt)
print(len(prompt))
