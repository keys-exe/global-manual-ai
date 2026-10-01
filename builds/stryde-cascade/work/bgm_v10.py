"""stryde-cascade v10 music bed per hook variant (§40A): the hook's own MUS-OPEN cue, then the shared body cue
from the body's first frame. Mix fixes on the body cue (not a regeneration): its opening drone came out ~−40 dB,
so the first 6 s are lifted +10 dB (back to 0 by 10 s) so the music does not vanish at the hook/body handover;
and the offer drops −5 dB from just before "Two for one" (body 135.68 s) to the end, under the price and the CTA.
usage: bgm_v10.py HK1 14.79 → edit/v10/bgm_HK1.wav (then finish.py --bgm it --hook-slot <hook length>)"""
import subprocess, sys
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
h, L = sys.argv[1], float(sys.argv[2])
D = "edit/v10"
env = ("if(lt(t,6),10,if(lt(t,10),10*(10-t)/4,if(lt(t,134.7),0,if(lt(t,135.7),-5*(t-134.7),-5))))")
fc = (f"[0:a]aresample=48000,atrim=0:{L+2:.3f},afade=t=out:st={L:.3f}:d=2[h];"
      f"[1:a]aresample=48000,volume='pow(10,({env})/20)':eval=frame,adelay={int(L*1000)}|{int(L*1000)}[b];"
      f"[h][b]amix=inputs=2:normalize=0:duration=longest[a]")
subprocess.run([FF, "-y", "-v", "error", "-i", f"{D}/hook_{h}.mp3", "-i", f"{D}/body.mp3", "-filter_complex", fc,
                "-map", "[a]", "-ac", "2", "-ar", "48000", f"{D}/bgm_{h}.wav"], check=True)
print(f"{D}/bgm_{h}.wav")
