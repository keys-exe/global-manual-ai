#!/bin/bash
# Send the Act 6 A/B pairs: 2 × Sunburst image-to-image per beat (refs from the call json; product refs pre-uploaded to Kie).
S=/home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts
W=/home/user/global-manual-ai/builds/stryde-lost-moments/work
OUT=/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actE
mkdir -p $OUT/jobs
TQ=https://tempfile.redpandaai.co/kieai/329820/pipeline/product_tq_left.jpg
BENT=https://tempfile.redpandaai.co/kieai/329820/pipeline/worn_bent.jpg
for b in "$@"; do
  refs=$(python3 -c "import json,sys;print(' '.join(u.replace('products/stryde/stryde_refs/product_tq_left.jpg','$TQ').replace('products/stryde/stryde_refs/worn_bent.jpg','$BENT') for u in json.load(open('$W/clips/$b.img.call.json'))['ref_urls']))")
  for p in A B; do
    ( python3 $S/kie.py image gpt-image-2-5-sunburst-image-to-image --prompt-file $W/prompts/$b.v74.txt --ref $refs --out $OUT/$b.$p.png > $OUT/jobs/$b.$p.json 2>$OUT/jobs/$b.$p.err ) &
    sleep 3
  done
done
wait
echo done
