#!/bin/bash
# usage: fix_send.sh ROUND BEAT...  — Kie Kling 3.0 from calls/<b>.<ROUND>.json, one render per beat, in parallel
cd "$(dirname "$0")/.."
R=$1; shift
K=../../.claude/skills/ai-prompt-engineer/scripts/kie.py
mkdir -p renders/$R
for b in "$@"; do
  (
  python3 -c "import json;c=json.load(open('calls/$b.$R.json'));open('renders/$R/$b.prompt.txt','w').write(c['prompt']);print(c['start_image']);print(c['duration'])" > renders/$R/$b.meta
  img=$(sed -n 1p renders/$R/$b.meta); dur=$(sed -n 2p renders/$R/$b.meta)
  python3 $K kling --prompt-file renders/$R/$b.prompt.txt --image "$img" --duration $dur --out renders/$R/${b}_vid.mp4 > renders/$R/$b.kie.json 2>&1
  echo "$b rc=$?"
  ) &
done
wait
