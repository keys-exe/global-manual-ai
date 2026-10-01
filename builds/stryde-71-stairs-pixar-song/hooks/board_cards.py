#!/usr/bin/env python3
"""Board docs for the hook A/B pairs: patches for the 4 start cards, full docs for the 3 END cards. Needs hooks/assets.json complete."""
import json, os, time
from pathlib import Path
H = Path(__file__).parent; B = "stryde-71-stairs-pixar-song"
A = json.load(open(H / "assets.json")); U = json.load(open(H / "urls.json")); J = json.load(open(H / "jobs.json"))
now = int(time.time() * 1000)
CRED = 2.14   # measured off the Higgsfield balance: 10377.65 → 10347.65 for 14 renders (30 / 14)
MODEL = "nano_banana_pro (requested) · Higgsfield logged nano_banana_2 · 2k · 9:16 · A/B pair"
def ver(beat, ab, v, note):
    k = f"{beat}@{ab}"; f = H / f"{beat}_v1{ab}.png"
    return {"v": v, "pair": ab, "asset": A[k], "type": "image/png", "url": U[k], "job": J[k], "model": "nano_banana_pro → logged nano_banana_2",
            "connector": "Higgsfield", "credits": CRED, "size": os.path.getsize(f), "res": "1536×2752", "at": now, "note": note}
def fields(beat, prompt):
    vA, vB = ver(beat, "A", 1, ""), ver(beat, "B", 2, "")
    return {"imageVersions": [vA, vB], "imagePair": [1, 2], "imageAsset": vA["asset"], "imageType": "image/png", "imageUrl": vA["url"], "imageJob": vA["job"],
            "imageConnector": "Higgsfield", "imageCredits": CRED, "imageRes": "1536×2752", "imageAt": now, "imageModel": MODEL, "imageStatus": "review",
            "imageRegens": 0, "imagePrompt": prompt, "preflight": "PASS (§6A, kind image)", "updatedAt": now,
            "routingFault": "§5: nano_banana_pro requested, Higgsfield logged nano_banana_2 on both renders (same fault as the cast and plates; Kie Pro route costs 963/render — not used without the user's word)"}
P = lambda b: (H / f"{b}.prompt.txt").read_text()
(H / "patch").mkdir(exist_ok=True)
for b in ["HK-01a", "HK-01b", "HK-02a", "HK-03a"]:
    json.dump(fields(b, P(b)), open(H / "patch" / f"{b}.review.json", "w"), ensure_ascii=False, indent=1)
LINES = {"HK-01a": "I'm seventy-one, and I take the stairs", "HK-01b": "faster than women half my age.", "HK-02a": "Last Sunday, my daughter walked behind me the whole way up and said,"}
ENDS = {"HK-01a": "two steps higher — N on the 8th step, C2 on the 6th", "HK-01b": "two steps higher — the pumps on the 8th/9th, the trainers on the 6th", "HK-02a": "one step higher — C2 on the 13th step, face up to the lens"}
for b, what in ENDS.items():
    e = f"{b}-END"
    doc = {"build": B, "act": "Hook 1", "hook": 1, "stage": "hooks", "beat": e, "title": f"{b} — pinned end frame (§27G rule 10, stairs): {what}", "line": LINES[b],
           "flow": ["image"], "status": "review", "endOf": b, "pinEnd": "yes", "location": "L-N-STAIRS", "storyDay": "N-D4", "section": "Hook — MUS-OPEN",
           "imageRefs": [{"label": f"{b} start frame (A for A, B for B)", "role": "Image 1 · edited (§6A rule 3)", "kind": "frame", "ref": f"{B}__{b}"}],
           "imageMatch": "frame", "imageTaste": ["HT03", "HT04", "HT09", "HT12", "HT13", "HT17", "HT18", "HT22"],
           "note": "The end frame of the pinned stairs clip: Kling runs first-and-last frame between the start pick and this pick (§27G rule 5). Use A with start A, B with start B."}
    doc.update(fields(e, P(e)))
    doc["imageVersions"][0]["note"] = f"edit of {b} start A"; doc["imageVersions"][1]["note"] = f"edit of {b} start B"
    json.dump(doc, open(H / "patch" / f"{e}.doc.json", "w"), ensure_ascii=False, indent=1)
    json.dump(doc, open(H.parent / "board/json" / f"beat_{e}.json", "w"), ensure_ascii=False, indent=1)
print("cards ok")
