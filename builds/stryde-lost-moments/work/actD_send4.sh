#!/bin/bash
# Body 4 round 4: pinned clips D-06, D-08 (3s, start A v3 → end A).
S=/home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts
W=/home/user/global-manual-ai/builds/stryde-lost-moments/work
OUT=/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actD
mkdir -p $OUT/jobs4
for b in D-06 D-08; do
  ( python3 $S/kie.py kling --prompt-file $W/prompts/$b.v1.video.txt --image $OUT/$b.v2.A.png --end-image $OUT/$b-END.A.png --duration 3 --out $OUT/clips/$b.v1.mp4 > $OUT/jobs4/$b.clip.json 2>$OUT/jobs4/$b.clip.err ) &
  sleep 4; done
wait; echo done
