#!/usr/bin/env python3
"""V7.78.0 (§40A): two compositions, one family — A (investigation) until the product, B (warm, major) from it.
B is placed so its first full chord (hit_b seconds into B) lands on the product's first frame; A fades out under B's soft intro.
B's offer section is extended with one crossfaded repeat when the composer ends early. Then levels: pre-product -2 dB,
a 4 dB dip under the link / price / guarantee, a fade after the video ends.
Usage: music_splice.py A.mp3 B.mp3 OUT.wav --product 72.28 --hit-b 7.2 [--a-fade 66.0] [--b-loop 108,122] [--length 212.6]"""
import argparse, subprocess, imageio_ffmpeg
ap=argparse.ArgumentParser(); ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("out")
ap.add_argument("--product",type=float,required=True); ap.add_argument("--hit-b",type=float,required=True)
ap.add_argument("--a-fade",type=float,default=None); ap.add_argument("--a-loop",default=None); ap.add_argument("--b-loop",default="108,122"); ap.add_argument("--b-end",type=float,default=135.5)
ap.add_argument("--dip",default="193.45,199.55"); ap.add_argument("--cue",default=None,help="cue with sections + energy: levels low -6, mid 0, high +2.5 dB (+ a section's gain_db), 1 s ramps"); ap.add_argument("--length",type=float,default=212.6); ap.add_argument("--video-end",type=float,default=210.92)
a=ap.parse_args(); FF=imageio_ffmpeg.get_ffmpeg_exe()
l0,l1=[float(x) for x in a.b_loop.split(",")]; d0,d1=[float(x) for x in a.dip.split(",")]
off=a.product-a.hit_b                      # B starts here so its hit is on the product frame
pre=f"if(lt(t,{a.product-0.3}),-2,if(lt(t,{a.product}),-2+2*(t-{a.product-0.3})/0.3,0))"
if a.cue:
    import json
    G={"low":-6.0,"mid":0.0,"high":2.5}; pts=[]
    for i,sx in enumerate(json.load(open(a.cue))["sections"]):
        gg=G[sx["energy"]]+float(sx.get("gain_db",0)); st=sx["start"]; ramp=0.3 if abs(st-a.product)<0.01 else 0.5   # the product step is quick, the others 1 s
        pts+=[(st+(ramp if i else 0),gg),(sx["end"]-(0.3 if abs(sx["end"]-a.product)<0.01 else 0.5),gg)]
    pts=sorted(pts)+[(a.length,pts[-1][1])]; pre="0"
    for (t0,g0),(t1,g1) in reversed(list(zip(pts,pts[1:]))):
        pre=f"if(lt(t,{t1}),({g0}+({g1}-{g0})*(t-{t0})/max({t1}-{t0},0.001)),{pre})"
dip=f"if(between(t,{d0-0.45},{d0}),-4*(t-{d0-0.45})/0.45,if(between(t,{d0},{d1}),-4,if(between(t,{d1},{d1+0.75}),-4+4*(t-{d1})/0.75,0)))"
import os, tempfile
td=tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(a.out)))
cut=lambda ss,to,o: subprocess.run([FF,"-v","error","-y","-ss",str(ss),"-to",str(to),"-i",a.b,"-ar","44100","-ac","2","-c:a","pcm_s16le",o],check=True)
p1,p2,p3,q,bx=[f"{td}/{n}.wav" for n in ("p1","p2","p3","q","bx")]
# the repeat runs from l0 to l1 + 1.5 s and the tail from l1 - 1.5 s, so each crossfade joins the same bars it replaces
cut(0,l1,p1); cut(l0,l1+1.5,p2); cut(l1-1.5,a.b_end,p3)
# A: when the composer thins out before the product, repeat its last bars so the investigation runs to the frame
ax=a.a
if a.a_loop:
    m0,m1=[float(x) for x in a.a_loop.split(",")]; r1,r2,ax=f"{td}/r1.wav",f"{td}/r2.wav",f"{td}/ax.wav"
    ca=lambda ss,to,o: subprocess.run([FF,"-v","error","-y","-ss",str(ss),"-to",str(to),"-i",a.a,"-ar","44100","-ac","2","-c:a","pcm_s16le",o],check=True)
    ca(0,m1,r1); ca(m0,a.product+1,r2)  # the repeat runs on past the product frame; it is faded under B's hit
    subprocess.run([FF,"-v","error","-y","-i",r1,"-i",r2,"-filter_complex","[0:a][1:a]acrossfade=d=1.5:c1=tri:c2=tri[o]","-map","[o]","-c:a","pcm_s16le",ax],check=True)
    os.remove(r1); os.remove(r2)
afade=a.a_fade if a.a_fade is not None else a.product-1.0
subprocess.run([FF,"-v","error","-y","-i",p1,"-i",p2,"-filter_complex","[0:a][1:a]acrossfade=d=1.5:c1=tri:c2=tri[o]","-map","[o]","-c:a","pcm_s16le",q],check=True)
subprocess.run([FF,"-v","error","-y","-i",q,"-i",p3,"-filter_complex","[0:a][1:a]acrossfade=d=1.5:c1=tri:c2=tri[o]","-map","[o]","-c:a","pcm_s16le",bx],check=True)
g=(f"[0:a]aresample=44100,aformat=channel_layouts=stereo,atrim=0:{afade+1.2},asetpts=PTS-STARTPTS,afade=t=out:st={afade}:d=1.2[A];"
   f"[1:a]aformat=channel_layouts=stereo,adelay={int(off*1000)}:all=1[B];"
   f"[A][B]amix=inputs=2:duration=longest:normalize=0,apad=whole_dur={a.length},atrim=0:{a.length},"
   f"afade=t=out:st={a.video_end}:d={a.length-a.video_end-0.1},volume='pow(10,(({pre})+({dip}))/20)':eval=frame[o]")
subprocess.run([FF,"-v","error","-y","-i",ax,"-i",bx,"-filter_complex",g,"-map","[o]","-ac","2","-c:a","pcm_s16le",a.out],check=True)
for x in (p1,p2,p3,q,bx)+((ax,) if a.a_loop else ()): os.remove(x)
os.rmdir(td)
print(f"bed {a.out}: B starts {off:.2f}s, its hit on the product frame {a.product:.2f}s")
