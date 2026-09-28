import json, subprocess, os
FF='/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2'
C='/home/user/global-manual-ai/builds/six-weeks-ago/scenes-4-9/renders/SC05/v7/clips'
X=json.load(open('tx.json')); os.makedirs('ed',exist_ok=True)
# silent beats: (start,end) seconds kept, audio muted (room tone laid later)
SIL={1:(0,4),5:(0,4),6:(0,4),7:(0.3,4),8:(0,4),12:(0.4,3.0),14:(0.4,3.0),21:(0.4,3.0),31:(0.3,3.6),35:(0.3,3.6),40:(0,4),42:(0.3,4)}
OVR={2:(None,6.9)}   # end before the repeated 'every morning'
parts=[]
for cid,x in X.items():
    n=int(cid[-2:]); src=f'{C}/{cid}.mp4'
    if n in SIL:
        a,b=SIL[n]; mute=True
    else:
        w=[t for t in x['words'] if t[2].strip()]
        a=max(0,w[0][0]-0.15); b=min(x['dur'],w[-1][1]+0.45); mute=False
        if n in OVR and OVR[n][1]: b=OVR[n][1]
    out=f'ed/{n:02d}.mp4'
    vf="scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24"
    if mute:
        cmd=[FF,'-v','error','-y','-ss',str(a),'-to',str(b),'-i',src,'-f','lavfi','-i','anullsrc=r=48000:cl=stereo','-vf',vf,'-map','0:v','-map','1:a','-shortest']
    else:
        d=b-a; af=f"afade=t=in:d=0.04,afade=t=out:st={max(0,d-0.08):.2f}:d=0.08,aresample=48000"
        cmd=[FF,'-v','error','-y','-ss',str(a),'-to',str(b),'-i',src,'-vf',vf,'-af',af,'-ac','2']
    subprocess.run(cmd+['-c:v','libx264','-crf','20','-preset','veryfast','-c:a','aac','-b:a','192k',out],check=True)
    parts.append((n,round(b-a,2),mute))
open('ed/list.txt','w').write(''.join(f"file '{n:02d}.mp4'\n" for n,_,_ in parts))
subprocess.run([FF,'-v','error','-y','-f','concat','-safe','0','-i','ed/list.txt','-c','copy','ed/cat.mp4'],check=True)
tot=sum(p[1] for p in parts)
# room-tone bed: soft brown noise + faint fridge hum, under the whole scene
subprocess.run([FF,'-v','error','-y','-i','ed/cat.mp4','-f','lavfi','-i',f'anoisesrc=c=brown:r=48000:a=0.012:d={tot+1}','-f','lavfi','-i',f'sine=f=100:r=48000:d={tot+1}',
 '-filter_complex','[2:a]volume=0.004[h];[1:a]lowpass=f=900[n];[n][h]amix=inputs=2:normalize=0,aformat=channel_layouts=stereo[bed];[0:a][bed]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-16:TP=-1.5:LRA=11[a]',
 '-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','SC05-V7-cut-v2.mp4'],check=True)
print(len(parts),'clips',round(tot,1),'s'); print(parts)
