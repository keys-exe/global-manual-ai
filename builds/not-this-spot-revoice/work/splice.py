import json,subprocess,sys
X=sys.argv[1]; meta=json.load(open(f"th/{X}_meta.json"))
pix="yuv420p" if X=="C" else "yuv420p10le"
f=["[0:v]format=yuv420p10le[b]","[1:v]scale=1080:1920:flags=lanczos,fps=30,tpad=stop_mode=clone:stop=8,format=yuv420p10le,split=%d%s"%(len(meta),"".join(f"[s{j}]" for j in range(len(meta))))]
off=0; prev="[b]"
for j,(i,a,b) in enumerate(meta):
    n=b-a
    f.append(f"[s{j}]trim=start_frame={off}:end_frame={off+n},setpts=PTS-STARTPTS+{a}/30/TB[l{j}]")
    f.append(f"{prev}[l{j}]overlay=eof_action=pass:repeatlast=0:format=yuv420p10[o{j}]"); prev=f"[o{j}]"; off+=n
fc=";".join(f)
out=f"out/Hook {X} - new VO.mp4"
subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"drive/Hook {X}.mp4","-i",f"th/{X}_LS.mp4","-i",f"mix{X}.wav","-filter_complex",fc,
  "-map",prev,"-map","2:a","-c:v","libx265","-preset","fast","-crf","17","-pix_fmt",pix,"-tag:v","hvc1","-x265-params","log-level=error",
  "-c:a","aac","-b:a","192k","-movflags","+faststart",out],check=True)
print("ok",out)
