#!/usr/bin/env python3
"""Card updates for finished B-roll videos: python3 cards.py BEAT[:V]=ASSET_ID ... → prints an ArtifactData batch (uses _versions.json).
For V > 1 (a Fix), the card's earlier videoVersions are read from _cards/<BEAT>.json (the downloaded card) and kept."""
import json, sys, time, subprocess, re, pathlib, imageio_ffmpeg
H = pathlib.Path(__file__).resolve().parent
V = json.loads((H / "_versions.json").read_text())
A = json.loads((H / "_assets.json").read_text()) if (H / "_assets.json").exists() else {}
w = []
for arg in sys.argv[1:]:
    bv, a = arg.split("="); b, n = (bv.split(":") + ["1"])[:2]; n = int(n); A[f"{b}_v{n}"] = a
    t = (H / f"{b}_v{n}.kie.json").read_text()
    k = json.loads(t[t.index("{\n"):])  # skip the one-line taskId notice if stderr was captured too
    out = subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-i", str(H / f"{b}_v{n}.mp4")], capture_output=True, text=True).stderr
    dur = re.search(r"Duration: (\d+):(\d+):([\d.]+)", out).groups(); dur = round(int(dur[1]) * 60 + float(dur[2]), 2)
    res = "×".join(re.search(r"Video:.*?(\d{3,4})x(\d{3,4})", out).groups())
    now = int(time.time() * 1000); url = (k.get("urls") or [""])[0]
    up = {"status": "review", "videoAsset": a, "videoType": "video/mp4", "videoUrl": url, "videoConnector": "Kie AI",
          "videoRes": res, "credits": k.get("credits"), "videoAt": now, "updatedAt": now,
          "videoVersions": [{"v": n, "asset": a, "type": "video/mp4", "url": url, "model": "Kling 3.0 (kling-3.0/video) on Kie, pro",
                             "connector": "Kie AI", "credits": k.get("credits"), "size": f"{dur}s", "at": now,
                             "note": ("first render from the confirmed start image" if n == 1 else
                                      json.loads((H / f"{b}.call.json").read_text()).get("fix_note", ""))
                                     + " (task " + k.get("taskId", "")[:8] + "…)"}]}
    if n > 1:
        old = json.loads((H / f"_cards/{b}.json").read_text())
        up["videoVersions"] = [x for x in old.get("videoVersions", []) if x.get("v") != n] + up["videoVersions"]
    (H / f"{b}.video.json").write_text(json.dumps(up))
    w.append({"op": "update", "collection": "generations", "doc_id": f"stryde-thirty-years__{b}", "if_version": V[b],
              "file_path": str(H / f"{b}.video.json")})
    V[b] += 1
(H / "_assets.json").write_text(json.dumps(A, indent=1)); (H / "_versions.json").write_text(json.dumps(V, indent=1))
print(json.dumps(w))
