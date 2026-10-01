#!/bin/bash
# Round 2: E-03 new A/B pair + 8 clips (Kie Kling 3.0, sound off).
S=/home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts
W=/home/user/global-manual-ai/builds/stryde-lost-moments/work
OUT=/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actE
TQ=https://tempfile.redpandaai.co/kieai/329820/pipeline/product_tq_left.jpg
BENT=https://tempfile.redpandaai.co/kieai/329820/pipeline/worn_bent.jpg
mkdir -p $OUT/jobs2 $OUT/clips
E04=$(python3 $S/kie.py upload $OUT/E-04.A.png | python3 -c "import json,sys;print(json.load(sys.stdin)['url'])")
C5=https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260928_131041_578389bd-200a-401e-a6d9-c0ec3c5f32fe.png
for p in A B; do
  ( python3 $S/kie.py image gpt-image-2-5-sunburst-image-to-image --prompt-file $W/prompts/E-03.v74b.txt --ref $TQ $BENT $E04 $C5 --out $OUT/E-03.v2.$p.png > $OUT/jobs2/E-03.$p.json 2>$OUT/jobs2/E-03.$p.err ) &
  sleep 3
done
for b in E-01:B:4 E-02:A:3 E-04:A:3 E-05:B:3 E-06:B:3 E-07:A:3 E-08:A:4 E-09:A:3; do
  IFS=: read beat pick dur <<< "$b"
  ( python3 $S/kie.py kling --prompt-file $W/prompts/$beat.v1.video.txt --image $OUT/$beat.$pick.png --duration $dur --out $OUT/clips/$beat.v1.mp4 > $OUT/jobs2/$beat.clip.json 2>$OUT/jobs2/$beat.clip.err ) &
  sleep 4
done
wait; echo done
