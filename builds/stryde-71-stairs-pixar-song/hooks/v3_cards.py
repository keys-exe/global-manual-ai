#!/usr/bin/env python3
"""Fix round (user "FIX THOSE"): Current patches for HK-01b / HK-02a / HK-03a — v3/v4 archived, v5/v6 the new A/B pair, status review."""
import json, os, time
from pathlib import Path
H = Path(__file__).parent
A = json.load(open(H / "assets.json")); U = json.load(open(H / "urls.json")); J = json.load(open(H / "jobs.json"))
now = int(time.time() * 1000); CRED = 2.14
NOTES = {"HK-01b": "WRONG CHARACTER", "HK-02a": "INCORRECT PLACEMENTS OF PICTURE FRAMES FIX THE LOCATION", "HK-03a": "WRONG LOCATION"}
for b, n in NOTES.items():
    vers = json.load(open(H / "patch" / f"{b}.versions_pre_v3.json"))
    new = []
    for i, ab in enumerate("AB"):
        k = f"{b}@v3{ab}"; f = H / f"{b}_v3{ab}.png"
        new.append({"v": 5 + i, "pair": ab, "asset": A[k], "type": "image/png", "url": U[k], "job": J[k], "model": "nano_banana_pro → logged nano_banana_2",
                    "connector": "Higgsfield", "credits": CRED, "size": os.path.getsize(f), "res": "1536×2752", "at": now,
                    "note": f'user 2026-10-01 Fix: "{n}" → an image edit of the confirmed HK-01a frame A (HT17), scene-so-far line (HT23)'})
    patch = {"imageVersions": vers + new, "imagePair": [5, 6], "imageAsset": new[0]["asset"], "imageType": "image/png", "imageUrl": new[0]["url"], "imageJob": new[0]["job"],
             "imageConnector": "Higgsfield", "imageCredits": CRED, "imageRes": "1536×2752", "imageAt": now, "imageStatus": "review", "imageRegens": 3,
             "imagePrompt": (H / f"{b}.v3.prompt.txt").read_text(), "imageFault": f'user 2026-10-01: "{n}" → fixed as an edit of the confirmed HK-01a frame A',
             "imageMatch": "frame", "imageRefs": [{"label": "HK-01a v1 A (confirmed frame)", "role": "Image 1 · edited (§6A rule 3, HT17)", "kind": "frame", "ref": "stryde-71-stairs-pixar-song__HK-01a"}],
             "imageTaste": ["HT03", "HT04", "HT05", "HT08", "HT09", "HT12", "HT17", "HT18", "HT19", "HT22", "HT23"], "updatedAt": now}
    json.dump(patch, open(H / "patch" / f"{b}.v3done.json", "w"), ensure_ascii=False, indent=1)
    c = json.load(open(H.parent / "board/json" / f"beat_{b}.json")); c.update(patch); json.dump(c, open(H.parent / "board/json" / f"beat_{b}.json", "w"), ensure_ascii=False, indent=1)
print("v3 cards ok")
