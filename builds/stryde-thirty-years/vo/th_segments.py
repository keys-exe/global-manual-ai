"""§22U step 12: cut the body talking-head lines out of the master variant by word timestamps (cut mid-gap between words)."""
import json, re, subprocess, sys, difflib
import imageio_ffmpeg
from faster_whisper import WhisperModel
FF = imageio_ffmpeg.get_ffmpeg_exe()
SRC = sys.argv[1]            # e.g. variants/T2.HK1.mp3 (HK1 + BODY, house cut)
TH = {
 "TH-01": "Leave it there and the list of things you have stopped doing keeps growing.",
 "TH-02": "Here is what I have watched fail for thirty years.",
 "TH-03": "that was not you failing. You were wrapping the wrong part of your leg.",
 "TH-04": "You do not wrap the joint. You go under it. Three things have to be right.",
 "TH-05": "Do not take my word for it. One knee only. Leave the other bare.",
 "TH-06": "Not because the arthritis is gone. Because the force is not landing where it hurts.",
 "TH-07": "Go and do your stairs.",
}
NUM = {"30": "thirty", "17": "seventeen", "34": "thirty four", "60": "sixty", "10": "ten"}
def norm(s):
    s = s.lower()
    for k, v in NUM.items(): s = re.sub(rf"\b{k}\b", v, s)
    return re.sub(r"[^a-z' ]", " ", s).split()
m = WhisperModel("medium.en", compute_type="int8")
segs, info = m.transcribe(SRC, word_timestamps=True, language="en", beam_size=5)
W = []
for s in segs:
    for w in s.words:
        for t in norm(w.word): W.append((t, w.start, w.end))
hyp = [w[0] for w in W]
out = {}
for k, line in TH.items():
    ref = norm(line)
    sm = difflib.SequenceMatcher(None, hyp, ref, autojunk=False)
    # find best window: search every start
    best = None
    for i in range(len(hyp) - len(ref) + 1):
        r = difflib.SequenceMatcher(None, hyp[i:i + len(ref)], ref).ratio()
        if best is None or r > best[0]: best = (r, i)
    r, i = best; j = i + len(ref) - 1
    prev_end = W[i - 1][2] if i > 0 else 0.0
    next_start = W[j + 1][1] if j + 1 < len(W) else info.duration
    a = (prev_end + W[i][1]) / 2 if i > 0 else max(0, W[i][1] - 0.05)
    b = (W[j][2] + next_start) / 2 if j + 1 < len(W) else info.duration
    subprocess.run([FF, "-v", "error", "-y", "-i", SRC, "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-c:a", "libmp3lame", "-b:a", "192k", f"th/{k}.mp3"], check=True)
    out[k] = dict(line=line, heard=" ".join(hyp[i:j + 1]), match=round(r, 3), start=round(a, 3), end=round(b, 3), dur=round(b - a, 2))
    print(k, out[k])
json.dump(dict(src=SRC, segments=out), open("th/segments.json", "w"), indent=1)
