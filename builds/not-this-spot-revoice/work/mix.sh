X=$1
T=$(ffmpeg -hide_banner -i full$X.wav -af ebur128=framelog=quiet -f null - 2>&1 | grep -E "^\s+I:" | awk '{print $2}')
N=$(ffmpeg -hide_banner -i vo$X.wav -af ebur128=framelog=quiet -f null - 2>&1 | grep -E "^\s+I:" | awk '{print $2}')
G=$(python -c "print($T-($N))")
ffmpeg -y -loglevel error -i vo$X.wav -af "volume=${G}dB,alimiter=limit=0.89:level=false,aformat=channel_layouts=stereo" -ar 44100 mix$X.wav
ffmpeg -y -loglevel error -i "drive/Hook $X.mp4" -i mix$X.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -movflags +faststart -tag:v hvc1 "out/Hook $X - new VO (pre-lipsync).mp4"
echo "$X target $T new $N gain $G"
