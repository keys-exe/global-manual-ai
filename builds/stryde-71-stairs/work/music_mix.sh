#!/bin/bash
# §40A/§24M: lay the build's music bed under a finished video. Voice to about -14 LUFS, music about 18 LU under it, ducked about 8 dB more while anyone speaks.
# Usage (from the build dir): bash work/music_mix.sh <in.mp4> <bed.wav> <out.mp4> [voice_gain_db] [music_gain_db]
FF=/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2
IN=$1; BED=$2; OUT=$3; VG=${4:-9.5}; MG=${5:--6.3}
$FF -hide_banner -loglevel error -y -i "$IN" -i "$BED" -filter_complex \
"[0:a]aresample=48000,aformat=channel_layouts=stereo,volume=${VG}dB,asplit=2[v][sc];\
[1:a]aresample=48000,aformat=channel_layouts=stereo,volume=${MG}dB[m];\
[m][sc]sidechaincompress=threshold=0.015:ratio=6:attack=30:release=450:makeup=1[md];\
[v][md]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.89:level=false[a]" \
-map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -movflags +faststart "$OUT"
