"""Third pass of the account move: fetch the current file of every card into <out>/media/<BEAT>.<ext>."""
import json, os, sys, shutil, pathlib, urllib.request, re, subprocess
OUT = pathlib.Path(sys.argv[1]); M = OUT/"media"; M.mkdir(exist_ok=True)
media = json.load(open(OUT/"media.json"))
H = {"xi-api-key": os.environ["ELEVENLABS_API_KEY"]}
def get(u, headers=None): return urllib.request.urlopen(urllib.request.Request(u, headers=headers or {"User-Agent": "Mozilla/5.0"}), timeout=120).read()
hist = None
def norm(t): return re.sub(r"\W+", " ", re.sub(r"\[[^\]]*\]", "", t)).strip().lower()
for did, m in media.items():
    beat = did.split("__")[1]; src = m["src"]
    if src.startswith("recut:"): continue
    if src.startswith("eleven:"):
        if hist is None:
            hist, start = [], None
            while True:
                d = json.loads(get("https://api.elevenlabs.io/v1/history?page_size=100" + (f"&start_after_history_item_id={start}" if start else ""), H))
                hist += d["history"]
                if not d.get("has_more"): break
                start = d["last_history_item_id"]
        want = norm(src[7:])
        hit = [h for h in hist if h.get("model_id") == "eleven_v4" and norm(" ".join(x.get("text", "") for x in h.get("dialogue") or []) or h.get("text") or "") == want]
        hit.sort(key=lambda h: -h["date_unix"])
        if not hit: print("NO ELEVEN MATCH", beat, want[:60]); continue
        raw = get(f"https://api.elevenlabs.io/v1/history/{hit[0]['history_item_id']}/audio", H)
        mp3 = M/f"{beat}.mp3"; mp3.write_bytes(raw)
        m.update(file=str(mp3), type="audio/mpeg", size=len(raw), eleven=hit[0]["history_item_id"]); print(beat, len(raw)); continue  # ElevenLabs' own file, untouched
    ext = pathlib.Path(src.split("?")[0]).suffix or ".bin"
    dst = M/f"{beat}{ext}"
    if not dst.exists() or dst.stat().st_size == 0:
        if src.startswith("http"): dst.write_bytes(get(src))
        else: shutil.copy(src, dst)
    m["file"] = str(dst); m["size"] = dst.stat().st_size
    if beat.startswith("VOICE-"): m["type"] = "audio/mp4"
    print(beat, m["size"])
json.dump(media, open(OUT/"media.json", "w"), indent=1)
