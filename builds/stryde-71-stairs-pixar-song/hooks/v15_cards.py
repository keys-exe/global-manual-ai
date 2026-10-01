#!/usr/bin/env python3
"""Board Fix on HK-02a (user 2026-10-01, 16:20 check): "this should show walking behind her" — v10: the daughter walking up the church steps behind her, from the sidewalk (edit of P5).
Current patch for HK-02a (the v9 pair archived to Old, the v10 A/B pair current, To check) + Old doc patch. Ids in patch/v15.ids.json."""
import json, os, time
from pathlib import Path
H = Path(__file__).parent; B = "stryde-71-stairs-pixar-song"
A = json.load(open(H / "assets.json")); U = json.load(open(H / "urls.json")); J = json.load(open(H / "jobs.json"))
CFG = json.load(open(H / "patch" / "v15.ids.json")); NEWA, NEWJ, STAMP = CFG["assets"], CFG["jobs"], CFG["stamp"]
for k in NEWA:
    A[k] = NEWA[k]; J[k] = NEWJ[k]; U[k] = f"https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20261001_{STAMP[k]}_{NEWJ[k]}.png"
json.dump(A, open(H / "assets.json", "w"), indent=1, sort_keys=True); json.dump(U, open(H / "urls.json", "w"), indent=1, sort_keys=True); json.dump(J, open(H / "jobs.json", "w"), indent=1, sort_keys=True)
# Current → Old copies (server-side, confirmed): Current id → Old id
OLD = CFG["old"]
now = int(time.time() * 1000); CRED = 2.14
NOTE = ('user 2026-10-01 Fix on the v14 pair: "i want a new angle they should be inside like at the door step" → a new setup: from inside the open church doorway looking out, '
        'the mother on the threshold turned back to her daughter on the top step, hand on the rail end, mouth open mid-word, the steps and sidewalk beyond (HT24); the v14 pair to Old')
SHOT = {"HK-01a": "SH-LOW · FULL from the plaza (edit of P8), N climbing away with her back to the lens, two women half her age walking up behind her", "HK-01b": "SH-GROUND · CU profile at tread height, her pump past the younger woman's stopped trainers",
        "HK-02a": "SH-LOW · FULL from the sidewalk (edit of P5), N on the 6th step, the daughter walking up two steps behind her", "HK-03a": "MEDIUM from inside the open church doorway (new angle), the two on the doorstep turned to each other"}
REFS = {"HK-01a": ["P8e", "N"], "HK-01b": ["P8"], "HK-02a": ["P5e", "N", "C2"], "HK-03a": ["P5", "N", "C2"]}
RL = {"P5": {"label": "P5-CHURCH plate v1 (confirmed)", "kind": "location", "ref": f"{B}__P5-CHURCH"}, "FR": {"label": "HK-02a v13 A (confirmed frame — the church steps from the sidewalk)", "kind": "frame", "ref": f"{B}__HK-02a", "edited": "§6A rule 3, HT17"}, "P5e": {"label": "P5-CHURCH plate v1 (confirmed)", "kind": "location", "ref": f"{B}__P5-CHURCH", "edited": "§6A rule 3, HT17"}, "P8": {"label": "P8-PLAZA plate v1 (To check)", "kind": "location", "ref": f"{B}__P8-PLAZA"}, "P8e": {"label": "P8-PLAZA plate v1 (To check)", "kind": "location", "ref": f"{B}__P8-PLAZA", "edited": "§6A rule 3, HT17"},
      "N": {"label": "N-NARR sheet v2", "kind": "character", "ref": f"{B}__N-NARR"}, "C2": {"label": "C2-DAUGHTER sheet v2", "kind": "character", "ref": f"{B}__C2-DAUGHTER"}}
rows = {r["beat"]: r for r in json.load(open(H.parent / "work/actmap_rows.json")) if r["beat"].startswith("HK-")}
IFV = CFG["ifv"]; OLDV = CFG["oldv"]
writes = []
for b in ["HK-03a"]:
    vers = [dict(v) for v in json.load(open(H / "patch" / f"{b}.versions_pre_v15.json"))]; n0 = max(v["v"] for v in vers)
    moved = []
    for v in vers:
        if v.get("asset") in OLD and not v.get("archived"):
            v["archived"] = True; v["archiveAsset"] = OLD[v["asset"]]; v["note"] = (v.get("note") or "") + " · replaced by the v15 pair (user: fix those — the v14 pair stayed mid-flight)"
            moved.append(dict(v, asset=OLD[v["asset"]]))
    new = []
    for i, ab in enumerate("AB"):
        k = f"{b}@v15{ab}"; f = H / f"{b}_v15{ab}.png"
        new.append({"v": n0 + 1 + i, "pair": ab, "asset": A[k], "type": "image/png", "url": U[k], "job": J[k], "model": "nano_banana_pro → logged nano_banana_2",
                    "connector": "Higgsfield", "credits": CRED, "size": os.path.getsize(f), "res": "1536×2752", "at": now, "note": NOTE + " · " + SHOT[b]})
    r = rows[b]
    refs = []
    for i, x in enumerate(REFS[b]):
        d = dict(RL[x]); e = d.pop("edited", None); d["role"] = f"Image {i + 1}" + (f" · edited ({e})" if e else ""); refs.append(d)
    patch = {"imageVersions": vers + new, "imagePair": [n0 + 1, n0 + 2], "imageAsset": new[0]["asset"], "imageType": "image/png", "imageUrl": new[0]["url"], "imageJob": new[0]["job"],
             "imageConnector": "Higgsfield", "imageCredits": CRED, "imageRes": "1536×2752", "imageAt": now, "imageStatus": "review", "imagePick": {"__delete__": True}, "imageUnused": {"__delete__": True},
             "imagePrompt": (H / f"{b}.v15.prompt.txt").read_text(), "imageFault": NOTE, "imageMatch": None, "imageRefs": refs, "shot": SHOT[b],
             "title": r["function"], "framing": r["framing"], "angle": (lambda a: f"{a['height']} · {a['side']} · {a['fg']} · {a['scale']} — {a['why']}" if isinstance(a, dict) else a)(r.get("angle")), "location": "L-CHURCH",
             "motionPlan": f"From this frame: {r['action']} — {r['pace']}; camera {r['camera']}",
             "imageTaste": ["HT03", "HT04", "HT05", "HT08", "HT09", "HT12", "HT17", "HT18", "HT19", "HT22", "HT23", "HT24"], "updatedAt": now}
    if b in ("HK-01a", "HK-02a"):
        patch["videoNote"] = "the home-stairs clip(s) were made from the earlier confirmed picks — kept as versions, superseded by the plaza concept; a clip from the plaza frame follows the user's pick"
    json.dump(patch, open(H / "patch" / f"{b}.v15done.json", "w"), ensure_ascii=False, indent=1)
    writes.append({"op": "update", "collection": "generations", "doc_id": f"{B}__{b}", "file_path": str(H / "patch" / f"{b}.v15done.json"), "if_version": IFV[b]})
    c = json.load(open(H.parent / "board/json" / f"beat_{b}.json")); c.update({k: v for k, v in patch.items() if not isinstance(v, dict) or "__delete__" not in v}); c.pop("imagePick", None); c.pop("imageUnused", None)
    json.dump(c, open(H.parent / "board/json" / f"beat_{b}.json", "w"), ensure_ascii=False, indent=1)
    if moved:
        o = json.load(open(H.parent / "board/json" / f"old_{b}.json")); have = {v["v"] for v in o["imageVersions"]}; ov = o["imageVersions"] + [m for m in moved if m["v"] not in have]; last = moved[0]
        op = {"imageVersions": ov, "imagePair": [m["v"] for m in moved], "imageAsset": last["asset"], "imageType": "image/png", "imageUrl": last["url"], "imageConnector": "Higgsfield", "imageCredits": CRED,
              "imageRes": "1536×2752", "imagePrompt": c.get("imagePrompt", ""), "imageFault": NOTE, "imageStatus": "regenerate", "status": "regenerate",
              "title": c["title"].split(" · ")[0] + f" — v1–v{last['v'] - 1} pairs (replaced; latest: the v14 pair, still mid-flight)", "updatedAt": now}
        json.dump(op, open(H / "patch" / f"{b}.v15old.json", "w"), ensure_ascii=False, indent=1); o.update(op)
        json.dump(o, open(H.parent / "board/json" / f"old_{b}.json", "w"), ensure_ascii=False, indent=1)
        writes.append({"op": "update", "collection": "generations", "doc_id": f"{B}__{b}", "file_path": str(H / "patch" / f"{b}.v15old.json"), "if_version": OLDV[b], "_board": "old"})
json.dump(writes, open(H / "patch" / "v15.writes.json", "w"), indent=1)
print("v15 cards ok", [(w["doc_id"][-6:], w.get("_board", "cur"), w["if_version"]) for w in writes])
