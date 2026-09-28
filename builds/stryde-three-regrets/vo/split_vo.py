"""One-go VO take -> verbatim check (whole script) -> split into HK1/HK2/HK3/BODY at the silences between them."""
import json, re, sys, glob, difflib, subprocess, os
import imageio_ffmpeg
from faster_whisper import WhisperModel
FF = imageio_ffmpeg.get_ffmpeg_exe()
NUM = {"25000": "twenty five thousand", "17": "seventeen", "34": "thirty four", "60": "sixty", "200000": "two hundred thousand", "10": "ten", "2": "two", "4": "four", "1": "one", "3": "three"}
EQ = {"body weight": "bodyweight", "post bag": "postbag", "stride": "stryde", "anymore": "any more", "2cm": "two centimetres",
      "centimeters": "centimetres", "centimeter": "centimetre", "neighbor": "neighbour", "orthopaedic": "orthopedic",
      "draw": "drawer", "bear": "bare"}   # spelling / homophone noise from the transcriber, not word changes
def norm(s):
    s = s.lower().replace("%", " percent").replace("-", " ").replace("’", "'")
    s = re.sub(r"(\d),(\d)", r"\1\2", s); s = re.sub(r"(\d) (\d{3})\b", r"\1\2", s)
    for k, v in EQ.items(): s = re.sub(rf"\b{k}\b", v, s)
    for k, v in NUM.items(): s = re.sub(rf"\b{k.replace(',', '')}\b", v, s)
    return re.sub(r"[^a-z0-9' ]", " ", s).split()
if __name__ != "__main__": pass
parts = {k: norm(open(f"{k}.lines.txt").read().replace("\n", " ")) for k in ["HK1", "HK2", "HK3", "BODY"]}
ref = parts["HK1"] + parts["HK2"] + parts["HK3"] + parts["BODY"]
m = WhisperModel("medium.en", compute_type="int8")
out = {}
for f in sorted(glob.glob("full/*.mp3")):
    tid = os.path.basename(f)[:-4]
    cache = f"full/{tid}.words.json"
    if os.path.exists(cache):
        raw, dur = json.load(open(cache))
    else:
        segs, info = m.transcribe(f, word_timestamps=True, language="en")
        raw = [(w.word, w.start, w.end) for s in segs for w in s.words]; dur = info.duration
        json.dump([raw, dur], open(cache, "w"))
    class I: pass
    info = I(); info.duration = dur
    words = []
    for (ww, a, b) in raw:
        for t in norm(ww): words.append((t, a, b))
    hyp = [w[0] for w in words]
    sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
    diff = [(t, " ".join(ref[a:b]), " ".join(hyp[c:d])) for t, a, b, c, d in sm.get_opcodes() if t != "equal"]
    # map each ref index to hyp index for the boundary words
    rmap = {}
    for blk in sm.get_matching_blocks():
        for k in range(blk.size): rmap[blk.a + k] = blk.b + k
    bounds, cut = [], []
    i = 0
    for k in ["HK1", "HK2", "HK3"]:
        i += len(parts[k])
        last, first = rmap.get(i - 1), rmap.get(i)
        if last is None or first is None: cut = None; break
        gap = (words[last][2], words[first][1])
        cut.append(round((gap[0] + gap[1]) / 2, 3)); bounds.append([round(g, 2) for g in gap])
    out[tid] = dict(dur=round(info.duration, 2), diff=diff, cuts=cut, gaps=bounds)
    print(tid, info.duration, "diff:", diff, "cuts:", cut)
    if cut:
        edges = [0.0] + cut + [info.duration]
        for n, k in enumerate(["HK1", "HK2", "HK3", "BODY"]):
            subprocess.run([FF, "-v", "error", "-y", "-i", f, "-ss", str(edges[n]), "-to", str(edges[n + 1]),
                            "-c:a", "libmp3lame", "-b:a", "192k", f"full/{tid}.{k}.mp3"], check=True)
json.dump(out, open("split.json", "w"), indent=1)
