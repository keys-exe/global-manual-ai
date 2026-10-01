#!/usr/bin/env python3
"""Body beats — Current patches for an A/B pair round: python3 act_cards.py <ids.json>.
ids.json: {"beats":[...], "v":<prompt version>, "assets":{"<BEAT>@v<n>A":id,...}, "urls":{...}, "jobs":{...}, "ifv":{beat:version}, "note":"...", "refs":{beat:[...]}, "old":{cur_id:old_id}}"""
import json, os, sys, time
from pathlib import Path
H = Path(__file__).parent; B = "stryde-71-stairs-pixar-song"
CFG = json.load(open(sys.argv[1])); V = CFG["v"]; now = int(time.time() * 1000); CRED = 2.14
rows = {r["beat"]: r for r in json.load(open(H.parent / "work/actmap_rows.json"))}
RL = {"P0": {"label": "P0-PROP-N plate (confirmed)", "kind": "location", "ref": f"{B}__P0-PROP-N", "edited": "§6A rule 3, HT17"},
      "P2": {"label": "P2-KITCHEN plate v2 (confirmed)", "kind": "location", "ref": f"{B}__P2-KITCHEN", "edited": "§6A rule 3, HT17"},
      "P7": {"label": "P7-CLINIC plate (confirmed)", "kind": "location", "ref": f"{B}__P7-CLINIC", "edited": "§6A rule 3, HT17"},
      "P3": {"label": "P3-RECEPTION plate (confirmed)", "kind": "location", "ref": f"{B}__P3-RECEPTION", "edited": "§6A rule 3, HT17"},
      "N": {"label": "N-NARR sheet v2", "kind": "character", "ref": f"{B}__N-NARR"}, "C1": {"label": "C1-LORETTA sheet v2", "kind": "character", "ref": f"{B}__C1-LORETTA"},
      "C2": {"label": "C2-DAUGHTER sheet v2", "kind": "character", "ref": f"{B}__C2-DAUGHTER"}}
writes = []
for b in CFG["beats"]:
    pre = H / "patch" / f"{b}.versions_pre_v{V}.json"; vers = json.load(open(pre)) if pre.exists() else []
    n0 = max([v["v"] for v in vers], default=0); OLD = CFG.get("old", {}); moved = []
    for v in vers:
        if v.get("asset") in OLD and not v.get("archived"):
            v["archived"] = True; v["archiveAsset"] = OLD[v["asset"]]; v["note"] = (v.get("note") or "") + " · " + CFG.get("oldnote", "replaced"); moved.append(dict(v, asset=OLD[v["asset"]]))
    new = []
    for i, ab in enumerate("AB"):
        k = f"{b}@v{V}{ab}"; f = H / f"{b}_v{V}{ab}.png"
        new.append({"v": n0 + 1 + i, "pair": ab, "asset": CFG["assets"][k], "type": "image/png", "url": CFG["urls"][k], "job": CFG["jobs"][k], "model": "nano_banana_pro → logged nano_banana_2",
                    "connector": "Higgsfield", "credits": CRED, "size": os.path.getsize(f), "res": "1536×2752", "at": now, "note": CFG["note"]})
    r = rows[b]; a = r.get("angle") or {}
    refs = []
    for i, x in enumerate(CFG["refs"][b]):
        d = dict(RL[x]); e = d.pop("edited", None); d["role"] = f"Image {i + 1}" + (f" · edited ({e})" if e and i == 0 else ""); refs.append(d)
    patch = {"imageVersions": vers + new, "imagePair": [n0 + 1, n0 + 2], "imageAsset": new[0]["asset"], "imageType": "image/png", "imageUrl": new[0]["url"], "imageJob": new[0]["job"],
             "imageModel": "nano_banana_pro (requested) · Higgsfield logged nano_banana_2 · 2k · 9:16 · A/B pair", "imageConnector": "Higgsfield", "imageCredits": CRED, "imageRes": "1536×2752", "imageAt": now,
             "imageStatus": "review", "imagePick": {"__delete__": True}, "imageUnused": {"__delete__": True}, "imagePrompt": (H / f"{b}.v{V}.prompt.txt").read_text(), "imageFault": CFG["note"] if V > 1 else None,
             "imageMatch": "plate", "imageRefs": refs, "shot": f"{a.get('height','')} · {a.get('side','')} · {a.get('fg','')} · {a.get('scale','')}", "angle": f"{a.get('height','')} · {a.get('side','')} · {a.get('fg','')} · {a.get('scale','')} — {a.get('why','')}",
             "framing": r["framing"], "motionPlan": f"From this frame: {r['action']} — {r['pace']}; camera {r['camera']}", "location": r["location"], "line": r["line"], "title": r["function"], "act": r["act"],
             "imageTaste": ["HT02", "HT03", "HT04", "HT08", "HT09", "HT12", "HT17", "HT18", "HT19", "HT22"], "updatedAt": now}
    json.dump(patch, open(H / "patch" / f"{b}.v{V}done.json", "w"), ensure_ascii=False, indent=1)
    writes.append({"op": "update", "collection": "generations", "doc_id": f"{B}__{b}", "file_path": str((H / "patch" / f"{b}.v{V}done.json").resolve()), "if_version": CFG["ifv"][b]})
    if moved:
        json.dump({"moved": moved}, open(H / "patch" / f"{b}.v{V}old.json", "w"), ensure_ascii=False, indent=1)
json.dump(writes, open(H / "patch" / f"v{V}.writes.json", "w"), indent=1)
print("cards ok", [(w["doc_id"][-6:], w["if_version"]) for w in writes])
