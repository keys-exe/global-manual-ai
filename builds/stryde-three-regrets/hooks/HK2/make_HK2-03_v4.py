"""HK2-03 image v4 (§6A, user Fix "CHANGE CAMERA ANGLE", 2026-09-30): v3 was an overhead edit of the HK2-01 frame → new setup: desk height, three-quarter front, close; the HK2-01 frame is left off so it can't hold the old angle (this build's lesson); refs P2 plate only (hands described in words; no face, so no sheet)."""
import json, os, shutil
D = os.path.dirname(os.path.abspath(__file__)) + "/"
if os.path.exists(D + "HK2-03.txt") and not os.path.exists(D + "HK2-03_v3.txt"):
    shutil.copy(D + "HK2-03.txt", D + "HK2-03_v3.txt")
LINE = "Twenty five thousand people have written to us about their knees. Three things come up more than anything else, and none of them are what you would expect."
prompt = (f'For the line "{LINE}": three separate piles of letters stand in a row on the worn wooden desk, and her hands are laying the last handful onto the third pile, caught mid-placing.\n'
    "A close shot from desk height, three-quarter from the front right: the three piles run away from us in a diagonal row, the grey post trays full of letters soft behind them.\n"
    "Image 1 is her workroom: the same worn wooden desk, brick wall and sash window, copied exactly.\n"
    "In frame: a woman's hands, fifty-seven, long knuckly fingers, short plain nails, rust-orange needlecord cuffs; exactly three piles of white A4 typed letters of different lengths, some stapled, with long window envelopes, untidy; her right hand holds the last handful just touching the third pile, her left hand rests flat on the desk beside the first pile. The piles fill the lower half of the frame. Nothing else on the desk.\n"
    "Soft morning daylight from the sash window, one direction. An ordinary iPhone photo.\n"
    "No fourth pile, no readable text or logos, no handwriting, no face, no extra fingers.")
call = {"beat": "HK2-03", "kind": "image", "mode": 1, "prompt": prompt, "script_line": LINE,
        "face": False, "room": True, "product": False, "body": True,
        "refs": [{"label": "P2-N-WORKROOM plate", "kind": "location"}],
        "match": None, "edit_of": None, "taste": ["HT09", "HT12", "HT18", "HT19", "HT21"], "anatomy": False,
        "pair": ["nano_banana_pro"], "alt_reason": "existing build keeps its step-2 image lock (nano_banana_pro on Higgsfield, one render per call) — CLAUDE.md: never switch a running build to Sunburst or the A/B pair",
        "ref_urls": ["https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260928_095745_698faa52-95f7-43c6-97f9-a275cd523628.png"],
        "fix_note": "CHANGE CAMERA ANGLE: v3 was overhead (an edit of the HK2-01 frame, so the same angle as HK2-01) → desk height, three-quarter front, close; the HK2-01 frame left off"}
json.dump(call, open(D + "HK2-03.image.json", "w"), ensure_ascii=False, indent=1)
open(D + "HK2-03.txt", "w").write(prompt)
print(len(prompt))
