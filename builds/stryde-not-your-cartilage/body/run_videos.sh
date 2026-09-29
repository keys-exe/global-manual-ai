#!/bin/bash
# Step 7 body videos on Kie kling-3.0 (one render per call), in parallel.
cd "$(dirname "$0")"
K=../../../.claude/skills/ai-prompt-engineer/scripts/kie.py
run() { b=$1; img=$(python3 -c "import json;print(json.load(open('$b.call.json'))['start_image'])"); d=$(python3 -c "import json;print(json.load(open('$b.call.json'))['duration'])")
  python3 $K kling --prompt-file $b.kling.json --image "$img" --duration $d --out $b.v1.mp4 > $b.video.log 2>&1; echo "$b rc=$?"; }
export -f run; export K
printf "%s\n" "$@" | xargs -P 8 -I{} bash -c 'run {}'
