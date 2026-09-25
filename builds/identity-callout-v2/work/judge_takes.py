import sys, re, json, subprocess, numpy as np, wave, tempfile, os
from faster_whisper import WhisperModel
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
NUM = {"17":"seventeen","34":"thirty four","60":"sixty","200,000":"two hundred thousand","200000":"two hundred thousand","%":" percent"}
def norm(t):
    t = t.lower().replace("-", " ").replace("body weight","bodyweight")
    for k,v in NUM.items(): t = t.replace(k.lower(), v)
    t = t.replace("thirty four percent","thirty four percent")
    return re.findall(r"[a-z']+", t)
m = WhisperModel("small.en", compute_type="int8")
def judge(path, target):
    segs,_ = m.transcribe(path, word_timestamps=True, language="en")
    words = [w for s in segs for w in s.words]
    got = norm(" ".join(w.word for w in words)); want = norm(target)
    import difflib
    sm = difflib.SequenceMatcher(None, want, got); miss = [want[i1:i2] for op,i1,i2,j1,j2 in sm.get_opcodes() if op in ("delete","replace")]
    extra = [got[j1:j2] for op,i1,i2,j1,j2 in sm.get_opcodes() if op in ("insert","replace")]
    gaps = [round(words[i+1].start-words[i].end,2) for i in range(len(words)-1) if words[i+1].start-words[i].end>0.4]
    tmp = tempfile.mktemp(suffix=".wav"); subprocess.run([FF,"-y","-loglevel","error","-i",path,"-ac","1","-ar","16000",tmp])
    w = wave.open(tmp); x = np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(float)/32768; os.remove(tmp)
    f0=[]
    for i in range(0,len(x)-1024,320):
        fr=x[i:i+1024]
        if np.sqrt((fr**2).mean())<0.02: continue
        fr=fr-fr.mean(); ac=np.correlate(fr,fr,'full')[1023:]; k=np.argmax(ac[40:228])+40
        if ac[k]>0.4*ac[0]: f0.append(16000/k)
    return {"file":path,"dur":round(len(x)/16000,2),"first_word":round(words[0].start,2) if words else None,
            "tail":round(len(x)/16000-words[-1].end,2) if words else None,"missing":miss,"extra":extra,"gaps>0.4":gaps,
            "f0_med":round(float(np.median(f0)),0) if f0 else None,"peak":round(float(np.abs(x).max()),3),
            "words":[(w.word.strip(),round(w.start,2),round(w.end,2)) for w in words]}
if __name__=="__main__":
    target = open(sys.argv[1]).read(); out=[]
    for p in sys.argv[2:]:
        r = judge(p, target); out.append(r)
        print(json.dumps({k:v for k,v in r.items() if k!="words"}))
    json.dump(out, open(sys.argv[2].rsplit("_",1)[0]+".judge.json","w"))
