#!/usr/bin/env python3
"""§40A/§24M: shape a composed track into the mix bed. Section levels by energy (low -4, mid 0, high +2.5 dB, 1 s ramps),
a 4 dB dip under the link / price / guarantee, and the final held chord extended with a crossfade when the composer ends early.
Usage: music_bed.py CUE.json TRACK.mp3 OUT.wav [--tail-from 201.0 --tail-to 208.0 --cut 206.5]"""
import json, subprocess, sys, argparse, imageio_ffmpeg
ap=argparse.ArgumentParser(); ap.add_argument("cue"); ap.add_argument("track"); ap.add_argument("out")
ap.add_argument("--tail-from",type=float,default=201.0); ap.add_argument("--tail-to",type=float,default=208.0); ap.add_argument("--cut",type=float,default=206.5)
ap.add_argument("--dip",default="193.45,199.55"); ap.add_argument("--length",type=float,default=212.6)
a=ap.parse_args(); FF=imageio_ffmpeg.get_ffmpeg_exe()
cue=json.load(open(a.cue)); gain={"low":-4.0,"mid":0.0,"high":2.5}
pts=[]
for i,s in enumerate(cue["sections"]):
    g=gain[s["energy"]]; pts+= [(s["start"]+(0.5 if i else 0),g),(s["end"]-0.5,g)]
d0,d1=[float(x) for x in a.dip.split(",")]
pts=[p for p in pts if not (d0-0.6<p[0]<d1+0.8)]+[(d0-0.45,0.0),(d0,-4.0),(d1,-4.0),(d1+0.75,0.0),(a.length,0.0)]
pts=sorted(pts); expr="0"
for (t0,g0),(t1,g1) in reversed(list(zip(pts,pts[1:]))):
    expr=f"if(lt(t,{t1}),({g0}+({g1}-{g0})*(t-{t0})/max({t1}-{t0},0.001)),{expr})"
graph=(f"[0:a]atrim=0:{a.cut},asetpts=PTS-STARTPTS[x];[0:a]atrim={a.tail_from}:{a.tail_to},asetpts=PTS-STARTPTS[y];"
       f"[x][y]acrossfade=d=1.5:c1=tri:c2=tri,apad=whole_dur={a.length},afade=t=out:st={a.length-1.7}:d=1.6[c];"
       f"[c]volume='pow(10,({expr})/20)':eval=frame[o]")
subprocess.run([FF,"-v","error","-y","-i",a.track,"-filter_complex",graph,"-map","[o]","-ar","44100","-c:a","pcm_s16le",a.out],check=True)
print("bed:",a.out)
