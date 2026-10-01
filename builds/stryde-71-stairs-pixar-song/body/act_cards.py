#!/usr/bin/env python3
"""Body beats — Current patches for an A/B pair round: python3 act_cards.py <ids.json>.
ids.json: {"beats":[...], "v":<prompt version>, "assets":{"<BEAT>@v<n>A":id,...}, "urls":{...}, "jobs":{...}, "ifv":{beat:version}, "note":"...", "refs":{beat:[...]}, "old":{cur_id:old_id}}"""
import json, os, sys, time
from pathlib import Path
H = Path(__file__).parent; B = "stryde-71-stairs-pixar-song"
CFG = json.load(open(sys.argv[1])); V = CFG["v"]; OUTV = CFG.get("outv", {}); now = int(time.time() * 1000); CRED = 2.14
rows = {r["beat"]: r for r in json.load(open(H.parent / "work/actmap_rows.json"))}
RL = {"P0": {"label": "P0-PROP-N plate (confirmed)", "kind": "location", "ref": f"{B}__P0-PROP-N", "edited": "§6A rule 3, HT17"},
      "P2": {"label": "P2-KITCHEN plate v2 (confirmed)", "kind": "location", "ref": f"{B}__P2-KITCHEN", "edited": "§6A rule 3, HT17"},
      "P7": {"label": "P7-CLINIC plate (confirmed)", "kind": "location", "ref": f"{B}__P7-CLINIC", "edited": "§6A rule 3, HT17"},
      "P3": {"label": "P3-RECEPTION plate (confirmed)", "kind": "location", "ref": f"{B}__P3-RECEPTION", "edited": "§6A rule 3, HT17"},
      "N": {"label": "N-NARR sheet v2", "kind": "character", "ref": f"{B}__N-NARR"}, "C1": {"label": "C1-LORETTA sheet v2", "kind": "character", "ref": f"{B}__C1-LORETTA"},
      "C2": {"label": "C2-DAUGHTER sheet v2", "kind": "character", "ref": f"{B}__C2-DAUGHTER"},
      "P03A": {"label": "P-03a frame v3 A (confirmed) — the brace", "kind": "frame", "ref": f"{B}__P-03a"}}
writes = []
for b in CFG["beats"]:
    pre = H / "patch" / f"{b}.versions_pre_v{V}.json"; vers = json.load(open(pre)) if pre.exists() else []
    n0 = max([v["v"] for v in vers], default=0); OLD = CFG.get("old", {}); moved = []
    for v in vers:
        if v.get("asset") in OLD and not v.get("archived"):
            v["archived"] = True; v["archiveAsset"] = OLD[v["asset"]]; v["note"] = (v.get("note") or "") + " · " + CFG.get("oldnote", "replaced"); moved.append(dict(v, asset=OLD[v["asset"]]))
    new = []
    PV = OUTV.get(b, V)
    for i, ab in enumerate("AB"):
        k = f"{b}@v{PV}{ab}"; f = H / f"{b}_v{PV}{ab}.png"
        new.append({"v": n0 + 1 + i, "pair": ab, "asset": CFG["assets"][k], "type": "image/png", "url": CFG["urls"][k], "job": CFG["jobs"][k], "model": "nano_banana_pro → logged nano_banana_2",
                    "connector": "Higgsfield", "credits": CRED, "size": os.path.getsize(f), "res": "1536×2752", "at": now, "note": CFG.get("notes", {}).get(b, CFG["note"])})
    r = rows[b]; a = r.get("angle") or {}
    refs = []
    for i, x in enumerate(CFG["refs"][b]):
        d = dict(RL[x]); e = d.pop("edited", None); d["role"] = f"Image {i + 1}" + (f" · edited ({e})" if e and i == 0 else ""); refs.append(d)
    patch = {"imageVersions": vers + new, "imagePair": [n0 + 1, n0 + 2], "imageAsset": new[0]["asset"], "imageType": "image/png", "imageUrl": new[0]["url"], "imageJob": new[0]["job"],
             "imageModel": "nano_banana_pro (requested) · Higgsfield logged nano_banana_2 · 2k · 9:16 · A/B pair", "imageConnector": "Higgsfield", "imageCredits": CRED, "imageRes": "1536×2752", "imageAt": now,
             "imageStatus": "review", "imagePick": {"__delete__": True}, "imageUnused": {"__delete__": True}, "imagePrompt": (H / f"{b}.v{PV}.prompt.txt").read_text(), "imageFault": CFG.get("notes", {}).get(b, CFG["note"]) if V > 1 else None, "imageNote": {"__delete__": True},
             "imageMatch": "frame" if CFG["refs"][b][0] == "P03A" else "plate", "imageRefs": refs, "status": "ready" if vers or True else "ready", "shot": f"{a.get('height','')} · {a.get('side','')} · {a.get('fg','')} · {a.get('scale','')}", "angle": f"{a.get('height','')} · {a.get('side','')} · {a.get('fg','')} · {a.get('scale','')} — {a.get('why','')}",
             "framing": r["framing"], "motionPlan": f"From this frame: {r['action']} — {r['pace']}; camera {r['camera']}", "location": r["location"], "line": r["line"], "title": r["function"], "act": r["act"],
             "imageTaste": ["HT02", "HT03", "HT04", "HT08", "HT09", "HT12", "HT17", "HT18", "HT19", "HT22"], "updatedAt": now}
    if not vers:   # a new beat: the base fields of a generation doc
        patch.update({"build": B, "stage": "broll", "beat": b, "flow": ["image", "video"], "duration": r["duration"], "key": r["key"], "lines": r["lines"], "body": 1, "bars": r.get("bars"), "focus": f"{r['focus']['plane']} · {r['focus']['dof']}", "eg": r.get("eg", ""), "createdAt": now})
    json.dump(patch, open(H / "patch" / f"{b}.v{V}done.json", "w"), ensure_ascii=False, indent=1)
    w = {"op": "update" if vers else "set", "collection": "generations", "doc_id": f"{B}__{b}", "file_path": str((H / "patch" / f"{b}.v{V}done.json").resolve())}
    if CFG["ifv"].get(b): w["if_version"] = CFG["ifv"][b]
    if not vers: [patch.pop(k) for k in [k for k, v in patch.items() if isinstance(v, dict) and v.get("__delete__")]]   # a set rejects __delete__
    json.dump(patch, open(H / "patch" / f"{b}.v{V}done.json", "w"), ensure_ascii=False, indent=1)
    writes.append(w)
    if moved:
        json.dump({"moved": moved}, open(H / "patch" / f"{b}.v{V}old.json", "w"), ensure_ascii=False, indent=1)
json.dump(writes, open(H / "patch" / f"v{V}.writes.json", "w"), indent=1)
print("cards ok", [(w["doc_id"][-6:], w["op"], w.get("if_version")) for w in writes])
