#!/bin/bash
# Body 4 round 2: 7 clips + 3 end-frame pairs + D-06/D-08 new pairs.
S=/home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts
W=/home/user/global-manual-ai/builds/stryde-lost-moments/work
OUT=/tmp/claude-0/-home-user-global-manual-ai/d5ebeecb-012d-539f-a9cc-ff2ce5209b53/scratchpad/actD
mkdir -p $OUT/jobs2 $OUT/clips
MAP="{'products/stryde/stryde_refs/front.webp':'https://tempfile.redpandaai.co/kieai/329820/pipeline/front.webp','products/stryde/stryde_refs/worn_front.jpg':'https://tempfile.redpandaai.co/kieai/329820/pipeline/worn_front.jpg','products/stryde/stryde_refs/product_tq_left.jpg':'https://tempfile.redpandaai.co/kieai/329820/pipeline/product_tq_left.jpg'}"
refs() { python3 -c "import json;m=$MAP;print(' '.join(m.get(u,u) for u in json.load(open('$W/clips/$1.call.json'))['ref_urls']))"; }
for b in D-03:B:5 D-04:A:3 D-05:A:3 D-07:A:3 D-09:B:3 D-11:B:3 D-12:A:3; do
  IFS=: read beat pick dur <<< "$b"
  ( python3 $S/kie.py kling --prompt-file $W/prompts/$beat.v1.video.txt --image $OUT/$beat.$pick.png --duration $dur --out $OUT/clips/$beat.v1.mp4 > $OUT/jobs2/$beat.clip.json 2>$OUT/jobs2/$beat.clip.err ) &
  sleep 4
done
for b in D-01-END D-02-END D-10-END; do r=$(refs $b.img); for p in A B; do
  ( python3 $S/kie.py image gpt-image-2-5-sunburst-image-to-image --prompt-file $W/prompts/$b.v74.txt --ref $r --out $OUT/$b.$p.png > $OUT/jobs2/$b.$p.json 2>$OUT/jobs2/$b.$p.err ) & sleep 3; done; done
for b in D-06 D-08; do r=$(refs $b.img2); for p in A B; do
  ( python3 $S/kie.py image gpt-image-2-5-sunburst-image-to-image --prompt-file $W/prompts/$b.v74b.txt --ref $r --out $OUT/$b.v2.$p.png > $OUT/jobs2/$b.$p.json 2>$OUT/jobs2/$b.$p.err ) & sleep 3; done; done
wait; echo done
