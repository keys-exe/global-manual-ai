#!/usr/bin/env python3
"""User 2026-10-01: "i want new ones cause these hooks looks the same as the others i want more powerfull hooks" — the plaza hook (P8-PLAZA).
Current patches for the four hook cards (the church / second-floor pairs archived to Old, the plaza A/B pair current, To check) + Old doc patches."""
import json, os, time
from pathlib import Path
H = Path(__file__).parent; B = "stryde-71-stairs-pixar-song"
A = json.load(open(H / "assets.json")); U = json.load(open(H / "urls.json")); J = json.load(open(H / "jobs.json"))
NEWA = {"HK-01a@v8A": "3ad574799ab20025416537dae1fcbe8e", "HK-01a@v8B": "980fcb229480f75ed6e446c00cdc49c1", "HK-01b@v8A": "235530cb28c1a1981beaa4fa87ba7ec5", "HK-01b@v8B": "6972393110f25934e4ff4c287b1ab1e5",
        "HK-02a@v8A": "cddf0ac2f721b0dd9781e4e2eac5560a", "HK-02a@v8B": "2d3f286823b8d158efdb694572167a8b", "HK-03a@v8A": "db12fd9f10da85ef2596b645e49367a0", "HK-03a@v8B": "26d10b8af5fd273301faf91c1742b903"}
NEWJ = {"HK-01a@v8A": "7752c6e5-21f4-4931-9529-79265df20246", "HK-01a@v8B": "ebdf42f6-3aeb-4f72-bd3e-53d6a9823e23", "HK-01b@v8A": "f728fe86-7a0c-4a6f-a8ea-eb1b7829acde", "HK-01b@v8B": "071d3919-f2a5-42bc-af06-a30467cde0bd",
        "HK-02a@v8A": "9165a953-9350-4196-bce3-cf11cf85e768", "HK-02a@v8B": "9cfea58d-a851-45f6-bde5-2be0dd348d1b", "HK-03a@v8A": "1c7e8a7c-3c72-459f-81de-18e1a9dd4ede", "HK-03a@v8B": "3af1b688-fec6-478c-8d3e-dfede38e1338"}
STAMP = {"HK-01a@v8A": "155624", "HK-01a@v8B": "155624", "HK-01b@v8A": "155623", "HK-01b@v8B": "155623", "HK-02a@v8A": "155624", "HK-02a@v8B": "155625", "HK-03a@v8A": "155623", "HK-03a@v8B": "155624"}
for k in NEWA:
    A[k] = NEWA[k]; J[k] = NEWJ[k]; U[k] = f"https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20261001_{STAMP[k]}_{NEWJ[k]}.png"
json.dump(A, open(H / "assets.json", "w"), indent=1, sort_keys=True); json.dump(U, open(H / "urls.json", "w"), indent=1, sort_keys=True); json.dump(J, open(H / "jobs.json", "w"), indent=1, sort_keys=True)
# Current → Old copies (server-side, confirmed): Current id → Old id
OLD = {"3b2ff917e1dc6fa2d3427c4e5ea4d4a7": "6cce4acba4efdbf4fe676c24c8f267c2", "2c3d99d8c6911128237ecedb33d5007c": "70f978a6c30c9f139ad364316ea0cff1",
       "036d0ac3e3467550176a467b7527f69d": "f3e9e6d830dcfd3769aa24e51f123031", "de55d05575cc0ae3e9b26eaa66aded49": "b355f8c7215782c7d0b2d4a6d419f26e",
       "b01047e313ee4a5096ee9338e23a8df6": "21e3c8fe2115d3f92fa1e2be16eae982", "3e79561427b3fdf9b6b47ccd8e84e175": "dc05fd8662d57ada5685515610651ccb"}
now = int(time.time() * 1000); CRED = 2.14
NOTE = ('user 2026-10-01: "i want new ones cause these hooks looks the same as the others i want more powerfull hooks" → a new hook concept (HT05): one monumental public staircase out in the world — '
        'the downtown arena plaza steps (new plate P8-PLAZA, generated with these renders, To check too), the younger crowd stopped on them while she climbs; the church and second-floor pairs to Old')
SHOT = {"HK-01a": "SH-LOW · FULL from the plaza (edit of P8), the crowd below her", "HK-01b": "SH-GROUND · CU profile at tread height, her pumps past the stopped trainers",
        "HK-02a": "SH-HIGH · MEDIUM front from the top landing, the daughter ten steps below", "HK-03a": "SH-OTS · over the mother's shoulder from above, the daughter stopped at the rail"}
REFS = {"HK-01a": ["P8e", "N"], "HK-01b": ["P8"], "HK-02a": ["C2", "P8"], "HK-03a": ["N", "C2", "P8"]}
RL = {"P8": {"label": "P8-PLAZA plate v1 (To check)", "kind": "location", "ref": f"{B}__P8-PLAZA"}, "P8e": {"label": "P8-PLAZA plate v1 (To check)", "kind": "location", "ref": f"{B}__P8-PLAZA", "edited": "§6A rule 3, HT17"},
      "N": {"label": "N-NARR sheet v2", "kind": "character", "ref": f"{B}__N-NARR"}, "C2": {"label": "C2-DAUGHTER sheet v2", "kind": "character", "ref": f"{B}__C2-DAUGHTER"}}
rows = {r["beat"]: r for r in json.load(open(H.parent / "work/actmap_rows.json")) if r["beat"].startswith("HK-")}
IFV = {"HK-01a": 23, "HK-01b": 22, "HK-02a": 21, "HK-03a": 21}; OLDV = {"HK-01a": 2, "HK-01b": 4, "HK-03a": 5}
writes = []
for b in ["HK-01a", "HK-01b", "HK-02a", "HK-03a"]:
    vers = [dict(v) for v in json.load(open(H / "patch" / f"{b}.versions_pre_v8.json"))]; n0 = max(v["v"] for v in vers)
    moved = []
    for v in vers:
        if v.get("asset") in OLD and not v.get("archived"):
            v["archived"] = True; v["archiveAsset"] = OLD[v["asset"]]; v["note"] = (v.get("note") or "") + " · replaced by the plaza pair (user 2026-10-01: more powerful hooks)"
            moved.append(dict(v, asset=OLD[v["asset"]]))
    new = []
    for i, ab in enumerate("AB"):
        k = f"{b}@v8{ab}"; f = H / f"{b}_v8{ab}.png"
        new.append({"v": n0 + 1 + i, "pair": ab, "asset": A[k], "type": "image/png", "url": U[k], "job": J[k], "model": "nano_banana_pro → logged nano_banana_2",
                    "connector": "Higgsfield", "credits": CRED, "size": os.path.getsize(f), "res": "1536×2752", "at": now, "note": NOTE + " · " + SHOT[b]})
    r = rows[b]
    refs = []
    for i, x in enumerate(REFS[b]):
        d = dict(RL[x]); e = d.pop("edited", None); d["role"] = f"Image {i + 1}" + (f" · edited ({e})" if e else ""); refs.append(d)
    patch = {"imageVersions": vers + new, "imagePair": [n0 + 1, n0 + 2], "imageAsset": new[0]["asset"], "imageType": "image/png", "imageUrl": new[0]["url"], "imageJob": new[0]["job"],
             "imageConnector": "Higgsfield", "imageCredits": CRED, "imageRes": "1536×2752", "imageAt": now, "imageStatus": "review", "imagePick": {"__delete__": True}, "imageUnused": {"__delete__": True},
             "imagePrompt": (H / f"{b}.v8.prompt.txt").read_text(), "imageFault": NOTE, "imageMatch": "plate" if b == "HK-01a" else None, "imageRefs": refs, "shot": SHOT[b],
             "title": r["function"], "framing": r["framing"], "angle": (lambda a: f"{a['height']} · {a['side']} · {a['fg']} · {a['scale']} — {a['why']}" if isinstance(a, dict) else a)(r.get("angle")), "location": "L-PLAZA",
             "motionPlan": f"From this frame: {r['action']} — {r['pace']}; camera {r['camera']}",
             "imageTaste": ["HT03", "HT04", "HT05", "HT08", "HT09", "HT12", "HT17", "HT18", "HT19", "HT22", "HT23"], "updatedAt": now}
    if b in ("HK-01a", "HK-02a"):
        patch["videoNote"] = "the home-stairs clip(s) were made from the earlier confirmed picks — kept as versions, superseded by the plaza concept; a clip from the plaza frame follows the user's pick"
    json.dump(patch, open(H / "patch" / f"{b}.v8done.json", "w"), ensure_ascii=False, indent=1)
    writes.append({"op": "update", "collection": "generations", "doc_id": f"{B}__{b}", "file_path": str(H / "patch" / f"{b}.v8done.json"), "if_version": IFV[b]})
    c = json.load(open(H.parent / "board/json" / f"beat_{b}.json")); c.update({k: v for k, v in patch.items() if not isinstance(v, dict) or "__delete__" not in v}); c.pop("imagePick", None); c.pop("imageUnused", None)
    json.dump(c, open(H.parent / "board/json" / f"beat_{b}.json", "w"), ensure_ascii=False, indent=1)
    if moved:
        o = json.load(open(H.parent / "board/json" / f"old_{b}.json")); have = {v["v"] for v in o["imageVersions"]}; ov = o["imageVersions"] + [m for m in moved if m["v"] not in have]; last = moved[0]
        op = {"imageVersions": ov, "imagePair": [m["v"] for m in moved], "imageAsset": last["asset"], "imageType": "image/png", "imageUrl": last["url"], "imageConnector": "Higgsfield", "imageCredits": CRED,
              "imageRes": "1536×2752", "imagePrompt": c.get("imagePrompt", ""), "imageFault": NOTE, "imageStatus": "regenerate", "status": "regenerate",
              "title": c["title"].split(" · ")[0] + f" — v1–v{last['v'] - 1} pairs (replaced; latest: the church / second-floor pair)", "updatedAt": now}
        json.dump(op, open(H / "patch" / f"{b}.v8old.json", "w"), ensure_ascii=False, indent=1); o.update(op)
        json.dump(o, open(H.parent / "board/json" / f"old_{b}.json", "w"), ensure_ascii=False, indent=1)
        writes.append({"op": "update", "collection": "generations", "doc_id": f"{B}__{b}", "file_path": str(H / "patch" / f"{b}.v8old.json"), "if_version": OLDV[b], "_board": "old"})
json.dump(writes, open(H / "patch" / "v8.writes.json", "w"), indent=1)
print("v8 cards ok", [(w["doc_id"][-6:], w.get("_board", "cur"), w["if_version"]) for w in writes])
