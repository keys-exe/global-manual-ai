import re, json, subprocess, sys, difflib
from faster_whisper import WhisperModel
import imageio_ffmpeg, numpy as np
FF = imageio_ffmpeg.get_ffmpeg_exe()
lines = [l.strip() for l in open("voice.lines.txt") if l.strip()]
norm = lambda t: re.findall(r"[a-z0-9']+", t.lower().replace("thirty four","thirty-four"))
ref = norm(" ".join(lines))
NUM = {"400":"four hundred","34":"thirty four","17":"seventeen","200,000":"two hundred thousand","60":"sixty","2":"two"}
m = WhisperModel("small.en", compute_type="int8")
out = {}
for t in sys.argv[1:]:
    segs, _ = m.transcribe(t, word_timestamps=True)
    ws = [w for s in segs for w in s.words]
    txt = " ".join(w.word.strip() for w in ws)
    for k, v in NUM.items(): txt = re.sub(rf"\b{re.escape(k)}\b", v, txt)
    txt = txt.replace("%", " percent").replace("-", " ")
    hyp = norm(txt); r = [x.replace("-", " ") for x in ref]; r = norm(" ".join(r))
    sm = difflib.SequenceMatcher(a=r, b=hyp); diffs = [(op, " ".join(r[i1:i2]), " ".join(hyp[j1:j2])) for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]
    raw = subprocess.run([FF, "-v", "quiet", "-i", t, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(float) / 32768
    tail = a[-800:]; tail_db = 20*np.log10(np.sqrt((tail**2).mean())+1e-9)
    gaps = [(round(ws[i].end,2), round(ws[i+1].start-ws[i].end,2)) for i in range(len(ws)-1) if ws[i+1].start-ws[i].end > 0.6]
    out[t] = {"dur": round(len(a)/16000,2), "words": len(hyp), "ref_words": len(r), "ratio": round(sm.ratio(),4), "diffs": diffs, "tail_db": round(tail_db,1), "long_gaps": gaps,
              "wpm": round(len(hyp)/(len(a)/16000)*60)}
    json.dump([{"w": w.word.strip(), "s": w.start, "e": w.end} for w in ws], open(t.replace(".mp3", ".words.json"), "w"))
print(json.dumps(out, indent=1))
