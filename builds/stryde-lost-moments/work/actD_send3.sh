#!/bin/bash
# Body 4 round 3: pinned clips D-01, D-02, D-10 + D-06/D-08 end-frame pairs.
S=/home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts
W=/home/user/global-manual-ai/builds/stryde-lost-moments/work
OUT=/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actD
mkdir -p $OUT/jobs3
for b in D-01:A:4 D-02:A:3 D-10:B:4; do IFS=: read beat pick dur <<< "$b"
  ( python3 $S/kie.py kling --prompt-file $W/prompts/$beat.v1.video.txt --image $OUT/$beat.$pick.png --end-image $OUT/$beat-END.A.png --duration $dur --out $OUT/clips/$beat.v1.mp4 > $OUT/jobs3/$beat.clip.json 2>$OUT/jobs3/$beat.clip.err ) &
  sleep 4; done
for b in D-06 D-08; do for p in A B; do
  ( python3 $S/kie.py image gpt-image-2-5-sunburst-image-to-image --prompt-file $W/prompts/$b-END.v74.txt --ref $OUT/$b.v2.A.png --out $OUT/$b-END.$p.png > $OUT/jobs3/$b-END.$p.json 2>$OUT/jobs3/$b-END.$p.err ) & sleep 3; done; done
wait; echo done
