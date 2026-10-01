#!/usr/bin/env python3
"""User re-angle (cinematic): Current patches for the four hook cards — earlier versions archived, the new A/B pair current, status review."""
import json, os, time
from pathlib import Path
H = Path(__file__).parent; B = "stryde-71-stairs-pixar-song"
A = json.load(open(H / "assets.json")); U = json.load(open(H / "urls.json")); J = json.load(open(H / "jobs.json"))
now = int(time.time() * 1000); CRED = 2.14
NOTE = 'user 2026-10-01: "USE THE CINEMATIC CAMERA ANGLES CAUSE THIS HOOK IS TOO WEAK" — re-angled (§30I; §24K shot names on the user\'s call), from the confirmed HK-01a frame + sheets'
SHOT = {"HK-01a": "SH-LOW (full, through the newel)", "HK-01b": "SH-GROUND (through the balusters)", "HK-02a": "SH-HIGH (from the landing)", "HK-03a": "SH-OTS (over the daughter's shoulder)"}
REFS = {"HK-01a": ["frame", "N", "C2"], "HK-01b": ["frame"], "HK-02a": ["frame", "C2", "P0"], "HK-03a": ["frame", "N", "C2"]}
RL = {"frame": {"label": "HK-01a v1 A (confirmed frame)", "kind": "frame", "ref": f"{B}__HK-01a"}, "N": {"label": "N-NARR sheet v2", "kind": "character", "ref": f"{B}__N-NARR"},
      "C2": {"label": "C2-DAUGHTER sheet v2", "kind": "character", "ref": f"{B}__C2-DAUGHTER"}, "P0": {"label": "P0-PROP-N plate", "kind": "location", "ref": f"{B}__P0-PROP-N"}}
for b in ["HK-01a", "HK-01b", "HK-02a", "HK-03a"]:
    vers = json.load(open(H / "patch" / f"{b}.versions_pre_v4.json")); n0 = max(v["v"] for v in vers)
    new = []
    for i, ab in enumerate("AB"):
        k = f"{b}@v4{ab}"; f = H / f"{b}_v4{ab}.png"
        new.append({"v": n0 + 1 + i, "pair": ab, "asset": A[k], "type": "image/png", "url": U[k], "job": J[k], "model": "nano_banana_pro → logged nano_banana_2",
                    "connector": "Higgsfield", "credits": CRED, "size": os.path.getsize(f), "res": "1536×2752", "at": now, "note": NOTE + " · " + SHOT[b]})
    patch = {"imageVersions": vers + new, "imagePair": [n0 + 1, n0 + 2], "imageAsset": new[0]["asset"], "imageType": "image/png", "imageUrl": new[0]["url"], "imageJob": new[0]["job"],
             "imageConnector": "Higgsfield", "imageCredits": CRED, "imageRes": "1536×2752", "imageAt": now, "imageStatus": "review", "imagePick": {"__delete__": True}, "imageUnused": {"__delete__": True},
             "imagePrompt": (H / f"{b}.v4.prompt.txt").read_text(), "imageFault": NOTE, "imageMatch": None,
             "imageRefs": [dict(RL[r], role=f"Image {i + 1}") for i, r in enumerate(REFS[b])],
             "imageTaste": ["HT03", "HT04", "HT05", "HT08", "HT09", "HT12", "HT17", "HT18", "HT19", "HT22", "HT23"], "shot": SHOT[b], "updatedAt": now}
    if b == "HK-01a":
        patch["videoNote"] = "clip v1 was made from image v1 A (confirmed, status use); a clip from the new angle waits on the user's pick"
    json.dump(patch, open(H / "patch" / f"{b}.v4done.json", "w"), ensure_ascii=False, indent=1)
    c = json.load(open(H.parent / "board/json" / f"beat_{b}.json")); c.update({k: v for k, v in patch.items() if not isinstance(v, dict) or "__delete__" not in v}); c.pop("imagePick", None); c.pop("imageUnused", None)
    json.dump(c, open(H.parent / "board/json" / f"beat_{b}.json", "w"), ensure_ascii=False, indent=1)
print("v4 cards ok")
