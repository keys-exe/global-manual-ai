#!/bin/bash
# split every trimmed variant (T<n>_V1 / T<n>_V2) into its hook and body part files for the board (mid-gap cut)
F=$(python3 -c "import imageio_ffmpeg as f;print(f.get_ffmpeg_exe())")
mkdir -p parts
for t in 1 2 3 4 5 6 7 8; do for v in 1 2; do
  src=cut/T${t}_V$v.mp3; [ -f parts/T${t}_BODY$v.mp3 ] && continue
  python3 split_vo.py $src HK$v,BODY$v > /dev/null 2>&1
  c=$(python3 -c "import json;print(json.load(open('$src.cuts.json'))['cuts'][0])")
  $F -loglevel error -y -i $src -t $c -c:a libmp3lame -b:a 192k parts/T${t}_HK$v.mp3
  $F -loglevel error -y -ss $c -i $src -c:a libmp3lame -b:a 192k parts/T${t}_BODY$v.mp3
  echo "T$t V$v cut at $c"
done; done
