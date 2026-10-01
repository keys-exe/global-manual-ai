"""stryde-cascade v10 music bed per hook variant (§40A): the hook's own MUS-OPEN cue, then the shared body cue
from the body's first frame. Fades are 0.5 s (user 2026-10-01: "it should only be 0.5s for the fade").
- The hook cues were composed to hold full level past the hook's end, so the cut is a 0.5 s fade at the body start.
- The body cue (two generations) stops at ~137 s, 15 s before the body ends: it is extended from itself — its
  120–137 s passage repeated after 137 s with a 0.5 s crossfade (same track, same family) → body_ext.wav.
- The offer drops −5 dB from just before "Two for one" (body 135.68 s) to the end, under the price and the CTA.
usage: bgm_v10.py HK1 14.792 → edit/v10/bgm_HK1.wav (then finish.py --bgm it --hook-slot <same value>)"""
import subprocess, sys
from pathlib import Path
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
h, L = sys.argv[1], float(sys.argv[2])
D = "edit/v10"
CUT, LOOP_FROM = 137.0, 120.0
ext = Path(f"{D}/body_ext.wav")
if not ext.exists():
    subprocess.run([FF, "-y", "-v", "error", "-i", f"{D}/body.mp3", "-i", f"{D}/body.mp3", "-filter_complex",
                    f"[0:a]aresample=48000,atrim=0:{CUT}[a];[1:a]aresample=48000,atrim={LOOP_FROM}:{CUT},asetpts=PTS-STARTPTS[b];"
                    f"[a][b]acrossfade=d=0.5:c1=tri:c2=tri[o]", "-map", "[o]", "-ac", "2", str(ext)], check=True)
env = "if(lt(t,134.7),0,if(lt(t,135.7),-5*(t-134.7),-5))"
fc = (f"[0:a]aresample=48000,atrim=0:{L+0.5:.3f},afade=t=out:st={L:.3f}:d=0.5[h];"
      f"[1:a]aresample=48000,afade=t=in:st=0:d=0.5,volume='pow(10,({env})/20)':eval=frame,adelay={int(L*1000)}|{int(L*1000)}[b];"
      f"[h][b]amix=inputs=2:normalize=0:duration=longest[a]")
subprocess.run([FF, "-y", "-v", "error", "-i", f"{D}/hook_{h}.mp3", "-i", str(ext), "-filter_complex", fc,
                "-map", "[a]", "-ac", "2", "-ar", "48000", f"{D}/bgm_{h}.wav"], check=True)
print(f"{D}/bgm_{h}.wav")
