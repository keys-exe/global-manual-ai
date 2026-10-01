#!/bin/bash
# usage: kie_fetch.sh DIR BEAT:TASKID ...  — wait for each Kie task, then download with resumable curl
# (the Kie file host is slow and cuts transfers; kie.py's own download often dies half-way).
cd "$(dirname "$0")/.."
D=$1; shift
K=../../.claude/skills/ai-prompt-engineer/scripts/kie.py
for a in "$@"; do
  (
  b=${a%%:*}; t=${a##*:}
  for i in $(seq 1 60); do
    python3 $K wait $t > renders/$D/$b.result.json 2>&1
    grep -q '"urls"' renders/$D/$b.result.json && break
    sleep 20
  done
  u=$(grep -o 'https://tempfile[^"]*' renders/$D/$b.result.json | head -1)
  for i in 1 2 3 4 5 6 7 8; do
    curl -sS --retry 5 --retry-all-errors -C - -o renders/$D/${b}_vid.mp4 "$u" 2>/dev/null
    ffmpeg -v error -xerror -i renders/$D/${b}_vid.mp4 -f null - >/dev/null 2>&1 && break
  done
  ffmpeg -v error -xerror -i renders/$D/${b}_vid.mp4 -f null - >/dev/null 2>&1 && echo "$b OK" || echo "$b BAD"
  ) &
done
wait
