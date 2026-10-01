#!/bin/bash
# D-HKb Fix MAKE HE HIITING THE BALL: address-on-the-tee A/B pair.
S=/home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts
W=/home/user/global-manual-ai/builds/stryde-lost-moments/work
OUT=/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actD
mkdir -p $OUT/jobs14
MAP="{'products/stryde/stryde_refs/front.webp':'https://tempfile.redpandaai.co/kieai/329820/pipeline/front.webp','products/stryde/stryde_refs/worn_front.jpg':'https://tempfile.redpandaai.co/kieai/329820/pipeline/worn_front.jpg','products/stryde/stryde_refs/product_tq_left.jpg':'https://tempfile.redpandaai.co/kieai/329820/pipeline/product_tq_left.jpg'}"
r=$(python3 -c "import json;m=$MAP;print(' '.join(m.get(u,u) for u in json.load(open('$W/clips/D-HKb.img5.call.json'))['ref_urls']))")
for p in A B; do
  ( python3 $S/kie.py image gpt-image-2-5-sunburst-image-to-image --prompt-file $W/prompts/D-HKb.v74d.txt --ref $r --out $OUT/D-HKb.v5.$p.png > $OUT/jobs14/D-HKb.$p.json 2>$OUT/jobs14/D-HKb.$p.err ) & sleep 3; done
wait; echo done
