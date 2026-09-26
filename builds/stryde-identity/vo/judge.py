import json,re,glob,os,subprocess,numpy as np
from faster_whisper import WhisperModel
import imageio_ffmpeg
FF=imageio_ffmpeg.get_ffmpeg_exe()
m=WhisperModel("small.en",compute_type="int8")
def norm(s): return re.sub(r"[^a-z0-9' ]","",s.lower().replace("-"," ").replace("’","'")).split()
refs={k:norm(open(f"{k}.lines.txt").read()) for k in["HK1","HK2","HK3","BODY"]}
def pitch(f):
    raw=subprocess.run([FF,"-v","error","-i",f,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True).stdout
    x=np.frombuffer(raw,np.int16).astype(float)/32768; fr=640; ps=[]
    for i in range(0,len(x)-fr,fr):
        s=x[i:i+fr]
        if np.sqrt((s**2).mean())<0.02: continue
        c=np.correlate(s,s,'full')[fr-1:]; lo,hi=16000//300,16000//70
        k=lo+np.argmax(c[lo:hi]); 
        if c[k]>0.3*c[0]: ps.append(16000/k)
    return float(np.median(ps)) if ps else 0
out={}
for f in sorted(glob.glob("takes/*.mp3")):
    segs,info=m.transcribe(f,word_timestamps=True,language="en")
    words=[w for s in segs for w in s.words]
    txt=" ".join(w.word.strip() for w in words); nw=norm(txt)
    best=max(refs,key=lambda k:len(set(refs[k])&set(nw))/len(set(refs[k])|set(nw)))
    ref=refs[best]
    import difflib
    sm=difflib.SequenceMatcher(None,ref,nw); diff=[(t,ref[a:b],nw[c:d]) for t,a,b,c,d in sm.get_opcodes() if t!='equal']
    gaps=[round(words[i+1].start-words[i].end,2) for i in range(len(words)-1)]
    speech=words[-1].end-words[0].start
    out[os.path.basename(f)[:-4]]=dict(script=best,dur=round(info.duration,2),lead=round(words[0].start,2),tail=round(info.duration-words[-1].end,2),
      wpm=int(round(len(ref)/speech*60)),max_gap=float(max(gaps)) if gaps else 0.0,gaps_over_0_6=int(sum(g>0.6 for g in gaps)),diff=diff,pitch=round(pitch(f),1),text=txt)
json.dump(out,open("judge.json","w"),indent=1)
for k,v in sorted(out.items(),key=lambda kv:(kv[1]['script'],kv[1]['dur'])):
    print(v['script'],k,v['dur'],'wpm',v['wpm'],'lead',v['lead'],'maxgap',v['max_gap'],'>0.6:',v['gaps_over_0_6'],'F0',v['pitch'],'diff',v['diff'][:4])
