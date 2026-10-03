#!/usr/bin/env python3
"""Board docs for landed takes: Current (review, cleaned version current when music was taken out) and Old (the music version).
Usage: board_docs.py TAKE... — writes ../board/json/land_<TAKE>.json and old_<TAKE>.json, prints batch writes."""
import json, sys, time, pathlib
H = pathlib.Path(__file__).parent; J = H.parent / "board/json"
L = json.load(open(H / "landed.json")); A = json.load(open(H / "assets.json")); JOBS = json.load(open(H / "jobs.json"))
now = int(time.time() * 1000); cur, old = [], []
for t in sys.argv[1:]:
    r = L[t]; c = json.load(open(H / f"{t}.call.json")); cr = round(c["duration"] * 7)
    gen = json.load(open(J / f"gen_{t}_generating.json"))
    v1 = {"v": 1, "asset": A["old"].get(t, A["cur"][t]), "type": "video/mp4", "url": r["url"], "model": "seedance_2_5", "connector": "Higgsfield", "credits": cr, "size": r["size"], "at": now, "note": ""}
    if r.get("clean"):
        v1.update(archived=True, archiveAsset=A["old"][t], note="as generated — had music; moved to Old")
        v2 = {"v": 2, "asset": A["cur"][t], "type": "video/mp4", "url": r["url"], "model": "seedance_2_5 → unmusic.py", "connector": "unmusic.py", "credits": 0, "size": r["clean_size"], "at": now,
              "note": "v1 with the music taken out (TIGER-DnR; voice and effects kept, picture untouched) — " + r["clean_check"].split("—")[-1].strip()}
        vers = [v1, v2]
        o = dict(gen, build="facelove-walmart", beat=t, status="regenerate", videoAsset=A["old"][t], videoType="video/mp4", videoUrl=r["url"], credits=cr, videoAt=now, updatedAt=now,
                 note="v1 as generated, with music — replaced by the cleaned v2 on Current", videoVersions=[{k: v for k, v in v1.items() if k not in ("archived", "archiveAsset")}])
        json.dump(o, open(J / f"old_{t}.json", "w"), ensure_ascii=False)
        old.append({"op": "set", "collection": "generations", "doc_id": f"facelove-walmart__{t}", "file_path": str((J / f"old_{t}.json").resolve())})
    else:
        vers = [v1]
    music = "silent clip (no dialogue, pre-V7.101 build)" if not r["audio"] else ("music taken out" if r.get("clean") else "no music found")
    d = {"status": "review", "videoAsset": A["cur"][t], "videoType": "video/mp4", "videoConnector": "Higgsfield", "videoUrl": r["url"], "videoJob": JOBS[t], "videoAt": now, "credits": cr,
         "duration": round(r["dur"]), "videoRes": "720×1280", "videoVersions": vers, "note": f"One Seedance 2.5 take, {len(c['covers'])} shots, {r['dur']} s; {music}. To check.", "updatedAt": now}
    json.dump(d, open(J / f"land_{t}.json", "w"), ensure_ascii=False)
    cur.append({"op": "update", "collection": "generations", "doc_id": f"facelove-walmart__{t}", "file_path": str((J / f"land_{t}.json").resolve()), "if_version": 2})
print(json.dumps(cur)); print(json.dumps(old))
