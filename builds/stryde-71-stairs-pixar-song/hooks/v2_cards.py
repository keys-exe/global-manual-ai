#!/usr/bin/env python3
"""v2 pairs for HK-01b / HK-02a / HK-03a: Current patches (v1/v2 archived, v3/v4 the new A/B) + Old docs (v1/v2)."""
import json, os, time, sys
from pathlib import Path
H = Path(__file__).parent; B = "stryde-71-stairs-pixar-song"
S = Path("/tmp/claude-0/-home-user-global-manual-ai/4a41b68d-7221-5f39-91cc-25c07de6bbd2/scratchpad/hooks_now/generations")
A = json.load(open(H / "assets.json")); U = json.load(open(H / "urls.json")); J = json.load(open(H / "jobs.json"))
OLD = {"2ccfeff7cbea225f68958845eaec5615": "d91b10dbba9c4371d804ebd9d5bd7cb2", "b162abcedff4c72196fbfd303bbfc321": "7d61c3add3495102197849cbcf3e0f8f",
       "2be33d780c1b97a7e4e1c52daea04a06": "69bedec6423694ced7635d8ae07730fc", "069ac4366d876edb3e91933e6b5667c1": "c3d50bdb4d1ab3d963191ddcb4dd5f8e",
       "fc0e0fcca290a725350f24207eab04ca": "5cb241f3716ed4e7c2b62beef21f3263", "25220af65f761e2752ab9bf3f46df75c": "3627c8b90c69488223745f44ab047247"}
now = int(time.time() * 1000); CRED = 2.14
NOTE = 'user 2026-10-01: "we dont need end frame generate new ones" — new pair from a rewritten prompt (§6A read-back)'
for b in ["HK-01b", "HK-02a", "HK-03a"]:
    cur = json.load(open(S / f"{B}__{b}.json"))
    old_vers = []
    for v in cur["imageVersions"]:
        v = dict(v); v["archived"] = True; v["archiveAsset"] = OLD[v["asset"]]; v["note"] = v.get("note") or "not chosen — replaced by the v2 pair"
        old_vers.append(v)
    new = []
    for i, ab in enumerate("AB"):
        k = f"{b}@v2{ab}"; f = H / f"{b}_v2{ab}.png"
        new.append({"v": 3 + i, "pair": ab, "asset": A[k], "type": "image/png", "url": U[k], "job": J[k], "model": "nano_banana_pro → logged nano_banana_2",
                    "connector": "Higgsfield", "credits": CRED, "size": os.path.getsize(f), "res": "1536×2752", "at": now, "note": NOTE})
    patch = {"imageVersions": old_vers + new, "imagePair": [3, 4], "imageAsset": new[0]["asset"], "imageType": "image/png", "imageUrl": new[0]["url"], "imageJob": new[0]["job"],
             "imageConnector": "Higgsfield", "imageCredits": CRED, "imageRes": "1536×2752", "imageAt": now, "imageStatus": "review", "imageRegens": 1,
             "imagePrompt": (H / f"{b}.v2.prompt.txt").read_text(), "imageFault": NOTE, "updatedAt": now}
    json.dump(patch, open(H / "patch" / f"{b}.v2done.json", "w"), ensure_ascii=False, indent=1)
    c = json.load(open(H.parent / "board/json" / f"beat_{b}.json")); c.update({k: v for k, v in cur.items() if not k.startswith("__")}); c.update(patch)
    json.dump(c, open(H.parent / "board/json" / f"beat_{b}.json", "w"), ensure_ascii=False, indent=1)
    ov = [dict(v, asset=OLD[v["asset"]]) for v in cur["imageVersions"]]
    for v in ov: v["archived"] = True
    old = {"build": B, "act": cur["act"], "hook": cur.get("hook", 1), "stage": "hooks", "beat": b, "title": cur["title"] + " — v1 pair (replaced)", "line": cur["line"], "flow": ["image"],
           "status": "regenerate", "imageStatus": "regenerate", "imageVersions": ov, "imagePair": [1, 2], "imageAsset": ov[0]["asset"], "imageType": "image/png", "imageUrl": ov[0]["url"],
           "imageConnector": "Higgsfield", "imageCredits": CRED, "imageRes": "1536×2752", "imageModel": cur["imageModel"], "imagePrompt": cur["imagePrompt"], "imageRefs": cur.get("imageRefs", []),
           "imageFault": NOTE, "updatedAt": now}
    json.dump(old, open(H.parent / "board/json" / f"old_{b}.json", "w"), ensure_ascii=False, indent=1)
print("v2 cards ok")
