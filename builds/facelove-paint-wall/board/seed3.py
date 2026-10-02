"""Voice stage: the three talking-head frames on the Current board (To check)."""
import json, time, pathlib
B = "facelove-paint-wall"; now = int(time.time()*1000); out = pathlib.Path("board/json")
jobs = json.load(open("voice/jobs.json")); urls = dict(l.split() for l in open("voice/urls.txt"))
A = {"N-VOICE-SHELF-B": "a748c1a01d693378c7442495a39a7c94", "N-VOICE-WALL-B": "f5d2ab700f4967efdb240ee69ce408c4", "N-VOICE-SHELF-A": "99c0dbec318ff8ef0a975a4c18ffdfc9"}
T = {"N-VOICE-SHELF-B": "Talking-head frame — bare face at the shelves (hook, Act 1; the voice-source start frame)",
     "N-VOICE-WALL-B": "Talking-head frame — bare face at the plaster wall (Acts 2–3)",
     "N-VOICE-SHELF-A": "Talking-head frame — finished face at the shelves (Acts 4–5)"}
REFS = {"N-VOICE-SHELF-B": [("L-SHELF", "Image 1 · room"), ("N-BEFORE", "Image 2 · her sheet")],
        "N-VOICE-WALL-B": [("L-WALL", "Image 1 · room"), ("N-BEFORE", "Image 2 · her sheet")],
        "N-VOICE-SHELF-A": [("L-SHELF", "Image 1 · room"), ("N-AFTER", "Image 2 · her sheet")]}
writes = []
for k, a in A.items():
    size = pathlib.Path(f"voice/{k}_v1.png").stat().st_size
    doc = {"build": B, "act": "Voice", "stage": "voice", "beat": k, "title": T[k], "line": "",
           "imagePrompt": pathlib.Path(f"voice/{k}.prompt.txt").read_text(), "imageModel": "gpt_image_2_5 · sunburst · high · 2k · 9:16",
           "imageStatus": "review", "status": "review", "imageRegens": 0, "imageAsset": a, "imageType": "image/png", "imageConnector": "Higgsfield",
           "imageUrl": urls[k], "imageJob": jobs[k], "imageRes": "1520×2688", "imageCredits": 2.75, "imageAt": now, "updatedAt": now, "flow": ["image"],
           "imageRefs": [{"label": r, "role": role, "kind": "location" if r.startswith("L-") else "character", "ref": f"{B}__{r}"} for r, role in REFS[k]],
           "imageVersions": [{"v": 1, "asset": a, "type": "image/png", "url": urls[k], "model": "gpt_image_2_5 sunburst", "connector": "Higgsfield",
                              "credits": 2.75, "size": size, "at": now, "note": ""}]}
    json.dump(doc, open(out/f"gen_{k}.json", "w"), ensure_ascii=False); writes.append(f"gen_{k}.json")
print(writes)
