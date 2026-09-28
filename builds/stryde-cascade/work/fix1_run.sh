#!/bin/bash
# usage: fix1_run.sh BEAT...  — Kie Kling 3.0 from calls/<b>.v2.json, one render per beat, in parallel
cd "$(dirname "$0")/.."
K=../../.claude/skills/ai-prompt-engineer/scripts/kie.py
for b in "$@"; do
  (
  python3 -c "import json;c=json.load(open('calls/$b.v2.json'));open('renders/fix/$b.prompt.txt','w').write(c['prompt']);print(c['start_image']);print(c['duration'])" > renders/fix/$b.meta
  img=$(sed -n 1p renders/fix/$b.meta); dur=$(sed -n 2p renders/fix/$b.meta)
  python3 $K kling --prompt-file renders/fix/$b.prompt.txt --image "$img" --duration $dur --out renders/fix/${b}_vid_v2.mp4 > renders/fix/$b.kie.json 2>&1
  echo "$b rc=$?"
  ) &
done
wait
