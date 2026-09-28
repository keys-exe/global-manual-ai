"""Write generations/<build>__<BEAT> card JSON for every B-roll beat into work/board/cards/ (Automatic: status use)."""
import json, os, glob, time, subprocess, re
from pathlib import Path
os.chdir(Path(__file__).resolve().parent.parent)
B = "stryde-cascade"
ids = dict(l.split() for l in open("work/board/asset_ids.txt"))
rows = json.load(open("actmap.json"))
man = {m["beat"]: m for m in json.load(open("prompts/frames/manifest.json"))}
furl = json.load(open("work/frame_urls.json")); furl1 = json.load(open("work/frame_urls_v1.json"))
kurl = json.load(open("work/kling_urls.json"))
FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
# §22V / §22W verdict notes for rerolled beats (image v -> note that produced the NEXT version)
IMG_FAULT = {
 "HK2-B2": "Q6: camera at floor level, not the row's angle -> regenerated at the planned height",
 "HK2-B3": "Q1: profile instead of the planned angle -> regenerated",
 "HK3-B3": "Q1: floor level wrong for the row -> regenerated",
 "A1-B4": "Q1: angle not from the landing looking down -> regenerated from the landing",
 "A1-B7": "Q4: timestamp text in frame -> edited out / regenerated",
 "A2-M2": "Q1: side view, row asks front -> regenerated; second try still side-on, kept best of two (Flag)",
 "A2-B3": "Q1: stair geometry inverted -> regenerated",
 "A3-B2": "Q1: medium shot, gel on the shin -> CU on the knee; v2 Q3: three hands -> one hand only",
 "A3-B3": "Q1: not overhead, odd fireplace foreground -> overhead CU of the hands",
 "A4-B2": "Q2: strap above the kneecap (on the thigh) -> strap below the kneecap, seated",
 "A4-P2": "Q1: showed the front, line is about the pad inside -> back view, pad facing up",
}
VID_FAULT = {
 "A2-M1": "Q1: glow on the joint, not the tendon -> motion names the tendon strap only, joint and kneecap unlit",
 "A2-M3": "Q1: glow inside the joint -> tendon strap only, continuous motion",
 "A2-M4": "Q1: glow in the joint; Q6: freeze 1.4-2.0s -> tendon only, continuous, no-freeze negatives",
}
VIDEO_NOTE = {"A1-B2": "§22W USE — camera follows the legs slightly; reads natural at 1.7s on screen (logged)",
              "A2-B3": "§22W USE — clean to 2.1s (he crouches after); used up to 2.1s",
              "A2-M2": "§22W USE (frame best of two, side-on)", "A4-M1": "§22W USE — frame front view (row: profile), placement correct"}
def dur(f):
    o = subprocess.run([FF, "-i", f], capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", o); return round(float(m[3]) + 60 * int(m[2]), 2)
def asset(f):
    stem, ext = os.path.splitext(os.path.basename(f))
    if f in ids: return [ids[f]]
    ps = sorted(k for k in ids if k.startswith(f"renders/parts/{stem}.part"))
    return [ids[p] for p in ps]
now = int(time.time() * 1000)
out = Path("work/board/cards"); out.mkdir(exist_ok=True)
for r in rows:
    b = r["beat"]; hook = r["act"].startswith("Hook")
    m = man[b]
    fv = sorted(glob.glob(f"renders/{b}_f_v*.png")) + [f"renders/{b}_f.png"]
    iv = []
    for i, f in enumerate(fv):
        key = b if i == 0 and len(fv) > 1 else (f"{b}_v{i+1}" if i < len(fv) - 1 else None)
        url = furl1.get(key, furl1.get(b)) if key else furl.get(b)
        a = asset(f)
        iv.append({"v": i + 1, "asset": a[0], "parts": a, "type": "image/png", "url": url, "model": m["model"],
                   "connector": "Higgsfield", "size": "1536×2752", "at": now,
                   "note": "" if i == 0 else IMG_FAULT.get(b, "regenerated")})
    cv = sorted(glob.glob(f"renders/{b}_v[0-9].mp4")) + [f"renders/{b}.mp4"]
    vv = []
    for i, f in enumerate(cv):
        a = asset(f); d = dur(f)
        vv.append({"v": i + 1, "asset": a[0], "parts": a, "type": "video/mp4", "url": kurl.get(b) if i == len(cv) - 1 else "",
                   "model": "kling-video-v3_0_omni · 1080p · audio off", "connector": "Kling", "credits": int(round(d)) * 8,
                   "size": f"{d}s", "at": now, "note": "" if i == 0 else VID_FAULT.get(b, "regenerated")})
    cur_i, cur_v = iv[-1], vv[-1]
    c = {"build": B, "beat": b, "act": r["act"], "stage": "hooks" if hook else "broll",
         "title": r["action"][:90], "line": r["phrase"],
         "imagePrompt": open(f"prompts/frames/{b}.v2.txt" if os.path.exists(f"prompts/frames/{b}.v2.txt") else f"prompts/frames/{b}.txt").read(),
         "imageModel": m["model"], "imageConnector": "Higgsfield", "imageStatus": "confirmed",
         "imageAsset": cur_i["asset"], "imageParts": cur_i["parts"], "imageType": "image/png", "imageUrl": cur_i["url"],
         "imageRes": "1536×2752", "imageAt": now, "imageRegens": len(iv) - 1, "imageVersions": iv,
         "prompt": open(f"prompts/clips/{b}.kling.json").read(), "model": "kling-video-v3_0_omni", "videoConnector": "Kling",
         "duration": r["duration"], "credits": cur_v["credits"], "status": "use",
         "videoAsset": cur_v["asset"], "videoParts": cur_v["parts"], "videoType": "video/mp4", "videoUrl": cur_v["url"],
         "videoAt": now, "regens": len(vv) - 1, "videoVersions": vv,
         "note": VIDEO_NOTE.get(b, "§22V frame USE · §22W clip USE · preflight PASS"), "updatedAt": now}
    if b in IMG_FAULT: c["imageFault"] = IMG_FAULT[b]
    if b in VID_FAULT: c["fault"] = VID_FAULT[b]
    if b == "A2-B3": c["videoOut"] = 2.1; c["videoOutV"] = len(vv)
    json.dump(c, open(out / f"{b}.json", "w"), ensure_ascii=False, indent=1)
print(len(rows), "cards")
