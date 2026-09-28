import subprocess,numpy as np,json,sys
def fr(f,t):
    r=subprocess.run(["ffmpeg","-loglevel","error","-ss",f"{t:.3f}","-i",f,"-frames:v","1","-vf","scale=108:192,format=gray","-f","rawvideo","-"],capture_output=True).stdout
    return np.frombuffer(r,np.uint8).astype(np.float32)
def dur(f):
    r=subprocess.run(["ffmpeg","-hide_banner","-i",f,"-map","0:v","-f","null","-"],capture_output=True,text=True).stderr
    import re; return re.findall(r"frame=\s*(\d+)",r)[-1]
for X in "ABC":
    o,n=f"drive/Hook {X}.mp4",f"out/Hook {X} - new VO.mp4"
    meta=json.load(open(f"th/{X}_meta.json"))
    print(X,"frames orig",dur(o),"new",dur(n))
    # B-roll checks: midpoints between TH shots
    br=[ (meta[k][2]+meta[k+1][1])/2/30 for k in range(len(meta)-1)]
    print("  B-roll diff (should be ~0):",[round(float(np.mean(abs(fr(o,t)-fr(n,t)))),1) for t in br[:5]])
    ls=f"th/{X}_LS.mp4"; off=0; d=[]
    for i,a,b in meta:
        m=(a+b)//2; d.append(round(float(np.mean(abs(fr(ls,(off+m-a+0.5)/30)-fr(n,(m+0.5)/30)))),1)); off+=b-a
    print("  doctor shots vs lip-sync (should be ~0):",d)
