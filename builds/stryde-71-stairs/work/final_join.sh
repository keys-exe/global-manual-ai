#!/bin/bash
# FINAL-HK<n> = hook clip (mother's VO 0–8.0 s laid over, clip ducked to 0.4 until 7.9 s, the daughter's own line after) + body (rough cut from 10.0 s, "Six weeks ago").
# Usage (from the build dir): bash work/final_join.sh <rough.mp4> <version>
FF=/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2; R=$1; V=$2
for p in "1 A_v3" "2 B_v2"; do set -- $p; n=$1; h=$2
$FF -hide_banner -loglevel error -y -i hooks/sd/HK-$h.mp4 -i vo/cut/v3/VO_T2.mp3 -filter_complex "[0:v]trim=0:10.95,setpts=PTS-STARTPTS,scale=1080:1920:flags=lanczos,fps=24,setsar=1,format=yuv420p[v];[0:a]atrim=0:10.95,asetpts=PTS-STARTPTS,aresample=48000,volume='if(lt(t,7.9),0.4,1)':eval=frame,afade=t=out:st=10.75:d=0.2[ca];[1:a]atrim=0:8.0,asetpts=PTS-STARTPTS,aresample=48000,afade=t=out:st=7.9:d=0.1,apad=whole_dur=10.95[vo];[ca][vo]amix=inputs=2:duration=first:normalize=0,aformat=channel_layouts=stereo[a]" -map "[v]" -map "[a]" -c:v libx264 -crf 18 -r 24 -c:a aac -b:a 192k -ar 48000 edit/HOOK_$h.mp4
$FF -hide_banner -loglevel error -y -i edit/HOOK_$h.mp4 -ss 10.0 -i $R -filter_complex "[0:v]setsar=1,fps=24,format=yuv420p[v0];[1:v]setpts=PTS-STARTPTS,setsar=1,fps=24,format=yuv420p[v1];[0:a]aresample=48000,aformat=channel_layouts=stereo[a0];[1:a]asetpts=PTS-STARTPTS,aresample=48000,aformat=channel_layouts=stereo,afade=t=in:d=0.03[a1];[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]" -map "[v]" -map "[a]" -c:v libx264 -crf 18 -c:a aac -b:a 192k -movflags +faststart edit/FINAL-HK${n}_v$V.mp4
done
