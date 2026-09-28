"""Board card updates for Fix round 1: append the new version, point the step at it, back to review."""
import json, sys, os, time, subprocess
S = "/tmp/claude-0/-home-user-global-manual-ai/ea15d283-9935-5994-9efa-ae7c21b1ec32/scratchpad/board2/generations/"
OUT = "/tmp/claude-0/-home-user-global-manual-ai/ea15d283-9935-5994-9efa-ae7c21b1ec32/scratchpad/writes"
os.makedirs(OUT, exist_ok=True)
FF = __import__("imageio_ffmpeg").get_ffmpeg_exe()
def dur(p):
    e = subprocess.run([FF, "-i", p], capture_output=True, text=True).stderr
    import re; h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", e).groups(); return round(int(h)*3600+int(m)*60+float(s), 2)
def video(b, asset, note_extra=""):
    d = json.load(open(S + f"stryde-cascade__{b}.json"))
    k = json.load(open(f"renders/fix/{b}.kie.json")); c = json.load(open(f"calls/{b}.v2.json"))
    f = f"renders/fix/{b}_vid_v2.mp4"; now = int(time.time()*1000)
    vv = list(d.get("videoVersions") or [])
    v = {"v": len(vv)+1, "asset": asset, "parts": [asset], "type": "video/mp4", "url": k["urls"][0], "model": "kling-3.0/video · pro 1080p · sound off",
         "connector": "Kie AI (Kling 3.0)", "credits": k["credits"], "size": f"{os.path.getsize(f)} B · {dur(f)}s", "at": now, "note": d.get("fault", "")}
    vv.append(v)
    data = {"videoVersions": vv, "videoAsset": asset, "videoParts": [asset], "videoType": "video/mp4", "videoUrl": k["urls"][0],
            "videoConnector": "Kie AI (Kling 3.0)", "model": "kling-3.0/video", "prompt": c["prompt"], "credits": k["credits"],
            "duration": dur(f), "videoAt": now, "status": "review", "updatedAt": now,
            "note": f"Fix v{v['v']}: {c['fix_note']}" + (f" · {note_extra}" if note_extra else "")}
    return data
if __name__ == "__main__":
    ids = json.loads(sys.argv[1]); extra = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
    for b, a in ids.items():
        json.dump(video(b, a, extra.get(b, "")), open(f"{OUT}/{b}.json", "w"), ensure_ascii=False)
        print(OUT + f"/{b}.json")
