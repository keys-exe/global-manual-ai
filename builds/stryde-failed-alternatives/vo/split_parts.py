"""Split one TTS take into this build's six parts (HK1, BODY1, HK2, BODY2, HK3, BODY3) at the mid-gap between
parts, by word timestamps — the §22U step-12 method of cut_points.py, for this build's part order.
Usage: split_parts.py TAKE.mp3  ->  TAKE.parts.json + TAKE_<PART>.mp3 (raw, untrimmed)"""
import json, re, sys, difflib, subprocess
import imageio_ffmpeg
from faster_whisper import WhisperModel
FF = imageio_ffmpeg.get_ffmpeg_exe()
SRC = sys.argv[1]; STEM = SRC.rsplit(".", 1)[0]
ORDER = ["HK1", "BODY1", "HK2", "BODY2", "HK3", "BODY3"]
NUM = {"17": "seventeen", "94": "ninety four", "60": "sixty", "3": "three"}
def norm(s):
    s = s.lower().replace("%", " percent").replace("-", " ")
    for k, v in NUM.items(): s = re.sub(rf"\b{k}\b", v, s)
    return re.sub(r"[^a-z' ]", " ", s).split()
parts = {k: norm(open(f"../work/script_{k}.txt").read()) for k in ORDER}
ref = [w for k in ORDER for w in parts[k]]
m = WhisperModel("medium.en", compute_type="int8")
segs, info = m.transcribe(SRC, word_timestamps=True, language="en", beam_size=5)
W = [(t, w.start, w.end) for s in segs for w in s.words for t in norm(w.word)]
hyp = [w[0] for w in W]
sm = difflib.SequenceMatcher(None, ref, hyp, autojunk=False)
rmap = {blk.a + k: blk.b + k for blk in sm.get_matching_blocks() for k in range(blk.size)}
def near(i, step):
    while i not in rmap: i += step
    return rmap[i]
cuts, i = [], 0
for k in ORDER[:-1]:
    i += len(parts[k])
    last, first = near(i - 1, -1), near(i, 1)
    cuts.append(round((W[last][2] + W[first][1]) / 2, 3))
bounds = [0.0] + cuts + [round(info.duration, 3)]
ranges = {k: [bounds[j], bounds[j + 1]] for j, k in enumerate(ORDER)}
for k, (a, b) in ranges.items():
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", SRC, "-ss", str(a), "-to", str(b), "-c:a", "libmp3lame", "-q:a", "2", f"{STEM}_{k}.mp3"], check=True)
diff = [(t, " ".join(ref[a:b]), " ".join(hyp[c:d])) for t, a, b, c, d in sm.get_opcodes() if t != "equal"]
json.dump({"src": SRC, "duration": round(info.duration, 3), "ranges": ranges, "diff": diff}, open(STEM + ".parts.json", "w"), indent=1)
print(json.dumps({"duration": round(info.duration, 3), "ranges": ranges}), "diff:", diff)
