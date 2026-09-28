"""§22U step 12 (2026-09-28): cut TH-xx out of the one Avatar V render of master HK1, between words."""
import json, re, subprocess, difflib, os, imageio_ffmpeg
from faster_whisper import WhisperModel
FF = imageio_ffmpeg.get_ffmpeg_exe()
def norm(w): return re.sub(r"[^a-z0-9']", "", w.lower())
cache = "vo/master/HK1.words.json"
if os.path.exists(cache): words = json.load(open(cache))
else:
    m = WhisperModel("medium.en", compute_type="int8")
    segs, _ = m.transcribe("vo/master/HK1.wav", word_timestamps=True, language="en")
    words = [[w.word.strip(), round(w.start, 3), round(w.end, 3)] for s in segs for w in s.words]
    json.dump(words, open(cache, "w"))
hyp = [norm(w[0]) for w in words]
rows = [r for r in json.load(open("work/actmap.json")) if r["type"] == "TH"]
out = []
for r in rows:
    ref = [norm(w) for w in r["line"].replace("-", " ").split() if norm(w)]
    sm = difflib.SequenceMatcher(None, hyp, ref, autojunk=False)
    blocks = [b for b in sm.get_matching_blocks() if b.size]
    # best window: longest match, then extend by ref length
    b = max(blocks, key=lambda b: b.size)
    near = [x for x in blocks if abs(x.a - b.a) <= 2 * len(ref)]
    i0 = min(x.a for x in near); i1 = max(x.a + x.size - 1 for x in near)
    ratio = difflib.SequenceMatcher(None, hyp[i0:i1 + 1], ref).ratio()
    s = (words[i0 - 1][2] + words[i0][1]) / 2 if i0 else 0.0
    e = (words[i1][2] + words[i1 + 1][1]) / 2 if i1 + 1 < len(words) else words[i1][2] + 0.15
    f = f"th/{r['beat']}.mp4"
    subprocess.run([FF, "-v", "error", "-y", "-ss", f"{s:.3f}", "-i", "th/N_TH_HK1_avatarV.mp4", "-t", f"{e - s:.3f}",
                    "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", f], check=True)
    out.append(dict(beat=r["beat"], act=r["act"], start=round(float(s), 3), end=round(float(e), 3), dur=round(float(e - s), 3), match=round(ratio, 3),
                    first=words[i0][0], last=words[i1][0], file=f))
    print(out[-1])
json.dump(out, open("th/segments.json", "w"), indent=1)
