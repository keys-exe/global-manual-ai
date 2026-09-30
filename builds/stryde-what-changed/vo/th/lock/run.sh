set -e
python3 - <<'PY'
import json,subprocess
F="/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
c=json.load(open('../VO_LOCK.mp3.cuts.json'))['ranges']; b0=c['BODY'][0]
for n in [1,2,3]:
    a,b=c[f'HK{n}']
    fc=f"[0:v]trim={a}:{b},setpts=PTS-STARTPTS[v0];[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS[a0];[0:v]trim={b0},setpts=PTS-STARTPTS[v1];[0:a]atrim={b0},asetpts=PTS-STARTPTS[a1];[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]"
    subprocess.run([F,"-loglevel","error","-y","-threads","4","-i","TH_ALL_LOCK.mp4","-filter_complex",fc,"-map","[v]","-map","[a]","-c:v","libx264","-crf","17","-preset","medium","-c:a","aac","-b:a","192k",f"lock/TH_HK{n}_raw.mp4"],check=True)
    print("cut",n,flush=True)
PY
for n in 1 2 3; do
  python3 ../../../../.claude/skills/ai-prompt-engineer/scripts/trim.py lock/TH_HK${n}_raw.mp4 --out lock/TH_HK${n}.mp4 --style natural 2>&1 | grep -v Warning | tail -12 > lock/trim_HK$n.log
  /usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2 -loglevel error -y -threads 4 -i lock/TH_HK${n}.mp4 -c:v libx264 -b:v 4000k -maxrate 4500k -bufsize 8000k -preset medium -c:a aac -b:a 192k -movflags +faststart lock/TH_HK${n}_board.mp4
  echo "HK$n done"
done
