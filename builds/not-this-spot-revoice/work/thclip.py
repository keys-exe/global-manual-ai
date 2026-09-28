import json,subprocess,sys,numpy as np,soundfile as sf
X=sys.argv[1]; segs=json.load(open("th.json"))[X]; FPS=30
mix,sr=sf.read(f"mix{X}.wav",dtype="float32")
parts=[];aud=[];meta=[]
for i,s,e in segs:
    a,b=round(s*FPS),round(e*FPS)
    o=f"th/{X}_{i:03d}_v.mp4"
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"drive/Hook {X}.mp4","-vf",f"trim=start_frame={a}:end_frame={b},setpts=PTS-STARTPTS,format=yuv420p",
        "-an","-r","30","-c:v","libx264","-crf","14","-preset","medium",o],check=True)
    parts.append(o); aud.append(mix[int(a/FPS*sr):int(a/FPS*sr)+int((b-a)/FPS*sr)]); meta.append((i,a,b))
open(f"th/{X}_list.txt","w").write("".join(f"file '{p.split('/')[1]}'\n" for p in parts))
subprocess.run(["ffmpeg","-y","-loglevel","error","-f","concat","-safe","0","-i",f"th/{X}_list.txt","-c","copy",f"th/{X}_TH_v.mp4"],check=True)
sf.write(f"th/{X}_TH.wav",np.concatenate(aud),sr)
subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"th/{X}_TH_v.mp4","-i",f"th/{X}_TH.wav","-map","0:v","-map","1:a","-c:v","copy","-c:a","aac","-b:a","192k","-shortest",f"th/{X}_TH.mp4"],check=True)
subprocess.run(["ffmpeg","-y","-loglevel","error","-i",f"th/{X}_TH.wav","-c:a","libmp3lame","-b:a","192k",f"th/{X}_TH.mp3"],check=True)
json.dump(meta,open(f"th/{X}_meta.json","w"))
print(X,"frames",sum(b-a for _,a,b in meta),"=",round(sum(b-a for _,a,b in meta)/FPS,2),"s")
