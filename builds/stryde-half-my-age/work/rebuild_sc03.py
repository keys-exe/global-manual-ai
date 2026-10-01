"""Account move, catch-up: the SC03 clips rendered on the first boards after the move started → cards for the new Current board."""
import json, re, glob, pathlib, urllib.request, time
B = "stryde-half-my-age"; out = pathlib.Path("renders/w"); up = pathlib.Path("renders/up")
def ref(f):
    n = pathlib.Path(f).stem
    m = re.match(r"([CNX]\d?)_voice_master", n)
    if m: return f"{B}__VOICE-{m.group(1)}", "voice"
    n = re.sub(r"_v\d+$", "", n)
    kind = "character" if f.startswith("cast/") else "location" if f.startswith("plates/") else "info"
    return f"{B}__{n}", kind
for c in sorted(glob.glob("body/SC03/SC03-SH*.call.json")):
    call = json.load(open(c)); beat = call["beat"]
    t = open(c.replace(".call.json", ".v1.kie.log")).read(); k = json.loads(t[t.find("{\n"):])
    url = k["urls"][0]; at = int(re.search(r"/(\d{13})-", url).group(1))
    ing = []
    for i, f in enumerate(call.get("files", [])):
        r, kind = ref(f); ing.append({"label": pathlib.Path(r.split("__")[1]).name, "role": f"@image{i+1}", "kind": kind, "ref": r})
    for i, f in enumerate(call.get("audios", []) or []):
        r, kind = ref(f); ing.append({"label": r.split("__")[1], "role": f"@audio{i+1}", "kind": "voice", "ref": r})
    dst = up / f"{beat}.mp4"
    if not dst.exists(): dst.write_bytes(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=120).read())
    d = {"build": B, "act": "Scene 3", "scene": 3, "stage": "broll", "beat": beat, "title": call.get("title", beat),
         "line": call.get("script_line") or call.get("dialogue") or "", "flow": ["video"], "ingredients": ing, "prompt": call["prompt"],
         "model": f"{call['model']} · 720p · 9:16 · {call['duration']}s" + ("" if call.get("generate_audio", True) else " · silent"),
         "videoConnector": "Kie AI", "duration": int(call["duration"]), "status": "review", "taste": call.get("taste", []),
         "videoUrl": url, "videoType": "video/mp4", "videoJob": k["taskId"], "videoAt": at, "credits": k.get("credits"), "videoRes": "720×1280",
         "videoVersions": [{"v": 1, "type": "video/mp4", "url": url, "model": call["model"], "connector": "Kie AI", "credits": k.get("credits"),
                            "job": k["taskId"], "size": dst.stat().st_size, "at": at, "note": "first render (CONFIRMED PROCEED)"}],
         "updatedAt": int(time.time() * 1000)}
    json.dump(d, open(out / f"{B}__{beat}.json", "w"), ensure_ascii=False)
    print(beat, dst.stat().st_size, len(ing), d["line"][:40])
