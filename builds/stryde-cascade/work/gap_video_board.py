"""Write a Current 2 video-version update for a gap clip: gap_video_board.py OUTDIR BEAT:asset[+asset2]:if_version ...
Reads calls/<BEAT>.gapv1.json and the newest Kie result json in renders/gapv1/; prints ArtifactData batch writes."""
import glob, json, os, sys, time
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
now = int(time.time() * 1000); w = []
def result(b):
    for f in sorted(glob.glob(f"renders/gapv1/{b}.*.json"), key=os.path.getmtime, reverse=True):
        t = open(f).read()
        i = t.rfind('{\n  "taskId"')
        try: j = json.loads(t[i:] if i >= 0 else t)
        except Exception: continue
        if j.get("urls"): return j
    raise SystemExit(f"no result for {b}")
for arg in sys.argv[2:]:
    b, assets, ver = arg.split(":"); parts = assets.split("+")
    c = json.load(open(f"calls/{b}.gapv1.json")); j = result(b)
    v = {"v": 1, "asset": parts[0], "type": "video/mp4", "url": j["urls"][0], "model": "kling-3.0", "connector": "Kie AI",
         "credits": j.get("credits"), "size": os.path.getsize(f"renders/gapv1/{b}_vid.mp4"), "at": now,
         "note": "first video from the confirmed frame and its Video will show line"}
    d = {"status": "review", "prompt": c["prompt"], "model": "kling-3.0", "videoConnector": "Kie AI", "videoAsset": parts[0],
         "videoType": "video/mp4", "videoUrl": j["urls"][0], "credits": j.get("credits"), "duration": c["duration"],
         "videoAt": now, "updatedAt": now, "videoVersions": [v]}
    if len(parts) > 1: v["parts"] = parts; d["videoParts"] = parts
    if c.get("pin_waived"): d["pinWaived"] = c["pin_waived"]
    p = f"{OUT}/{b}.json"; json.dump(d, open(p, "w"))
    w.append({"op": "update", "collection": "generations", "doc_id": "stryde-cascade__" + b, "if_version": int(ver), "file_path": p})
print(json.dumps(w))
