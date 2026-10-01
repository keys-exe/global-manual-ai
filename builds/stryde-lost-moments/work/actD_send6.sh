#!/bin/bash
# D-HKb end-frame A/B pair (edit of the picked start A).
S=/home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts
W=/home/user/global-manual-ai/builds/stryde-lost-moments/work
OUT=/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actD
mkdir -p $OUT/jobs6
for p in A B; do
  ( python3 $S/kie.py image gpt-image-2-5-sunburst-image-to-image --prompt-file $W/prompts/D-HKb-END.v74.txt --ref $OUT/D-HKb.v2.A.png --out $OUT/D-HKb-END.$p.png > $OUT/jobs6/D-HKb-END.$p.json 2>$OUT/jobs6/D-HKb-END.$p.err ) & sleep 3; done
wait; echo done
