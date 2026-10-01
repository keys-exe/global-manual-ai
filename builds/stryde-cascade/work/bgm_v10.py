"""stryde-cascade v10 music bed per hook variant (§40A). Fades are 0.5 s (user 2026-10-01).
- Hook: its own MUS-OPEN cue, held at full level to the cut, 0.5 s fade into the body.
- Body: two cues that switch where the product first shows (user 2026-10-01: "THE MUSIC SHOULD CHANGE WHEN THE
  PRODUCT SHOWS") — A4-P1's first frame, body 79.74 s (HK1 94.533 s). bodyA (MUS-OPEN → EDU → EXPOSE) up to that
  frame, a 0.5 s crossfade, bodyB (MUS-TURN → AFTER → OFFER) full on that frame.
  bodyA's first 8.3 s came out ~−30 dB: lifted +12 dB to meet the hook. bodyB opens with 3.75 s of silence (trimmed)
  and dies at ~69 s, so its 49.5–69 s passage is repeated with a 0.5 s crossfade to reach the body's end.
- The offer drops −5 dB from just before "Two for one" (body 135.68 s) to the end, under the price and the CTA.
usage: bgm_v10.py HK1 14.792 → edit/v10/bgm_HK1.wav (then finish.py --bgm it --hook-slot <same value>)"""
import subprocess, sys
from pathlib import Path
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
h, L = sys.argv[1], float(sys.argv[2])
D = "edit/v10"
PRODUCT, B_IN, B_OUT, B_LOOP = 79.74, 3.75, 69.0, 49.5
body = Path(f"{D}/body_mix.wav")
if not body.exists():
    fc = (f"[0:a]aresample=48000,atrim=0:{PRODUCT + 0.5:.3f},volume='pow(10,(if(lt(t,8.0),12,if(lt(t,8.5),12*(8.5-t)/0.5,0)))/20)':eval=frame[a];"
          f"[1:a]aresample=48000,atrim={B_IN}:{B_OUT},asetpts=PTS-STARTPTS[b1];"
          f"[2:a]aresample=48000,atrim={B_LOOP}:{B_OUT},asetpts=PTS-STARTPTS[b2];"
          f"[b1][b2]acrossfade=d=0.5:c1=tri:c2=tri[b];[a][b]acrossfade=d=0.5:c1=tri:c2=tri[o]")
    subprocess.run([FF, "-y", "-v", "error", "-i", f"{D}/bodyA.mp3", "-i", f"{D}/bodyB.mp3", "-i", f"{D}/bodyB.mp3",
                    "-filter_complex", fc, "-map", "[o]", "-ac", "2", str(body)], check=True)
env = "if(lt(t,134.7),0,if(lt(t,135.7),-5*(t-134.7),-5))"
fc = (f"[0:a]aresample=48000,atrim=0:{L+0.5:.3f},afade=t=out:st={L:.3f}:d=0.5[h];"
      f"[1:a]aresample=48000,afade=t=in:st=0:d=0.5,volume='pow(10,({env})/20)':eval=frame,adelay={int(L*1000)}|{int(L*1000)}[b];"
      f"[h][b]amix=inputs=2:normalize=0:duration=longest[a]")
subprocess.run([FF, "-y", "-v", "error", "-i", f"{D}/hook_{h}.mp3", "-i", str(body), "-filter_complex", fc,
                "-map", "[a]", "-ac", "2", "-ar", "48000", f"{D}/bgm_{h}.wav"], check=True)
print(f"{D}/bgm_{h}.wav")
