#!/bin/bash
# Body 3 / Act 4: nine A/B beat-image pairs (GPT Image 2.5 Sunburst i2i on Kie).
S=/home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts
W=/home/user/global-manual-ai/builds/stryde-lost-moments/work
OUT=/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actC
mkdir -p $OUT/jobs $OUT/clips
MAP="{'products/stryde/stryde_refs/front.webp':'https://tempfile.redpandaai.co/kieai/329820/pipeline/front.webp','products/stryde/stryde_refs/worn_front.jpg':'https://tempfile.redpandaai.co/kieai/329820/pipeline/worn_front.jpg','products/stryde/stryde_refs/product_tq_left.jpg':'https://tempfile.redpandaai.co/kieai/329820/pipeline/product_tq_left.jpg'}"
refs() { python3 -c "import json;m=$MAP;print(' '.join(m.get(u,u) for u in json.load(open('$W/clips/$1.img.call.json'))['ref_urls']))"; }
for b in C-01 C-02 C-03 C-04 C-05 C-06 C-07 C-08 C-09; do r=$(refs $b); for p in A B; do
  ( python3 $S/kie.py image gpt-image-2-5-sunburst-image-to-image --prompt-file $W/prompts/$b.v74.txt --ref $r --out $OUT/$b.$p.png > $OUT/jobs/$b.$p.json 2>$OUT/jobs/$b.$p.err ) & sleep 3; done; done
wait; echo done
