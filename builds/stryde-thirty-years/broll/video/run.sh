#!/bin/bash
# one Kling 3.0 (Kie) call per beat, from its confirmed start image (and pinned end image), at its E6 length
# usage: run.sh BEAT [VERSION]   → broll/video/BEAT_vVERSION.mp4
b=$1; v=${2:-1}; cd "$(dirname "$0")/../.."
d=$(python3 -c "import json;print(json.load(open('broll/video/$b.call.json'))['duration'])")
img=$(python3 -c "import json;print(json.load(open('broll/video/_confirmed.json'))['$b'])")
last=$(python3 -c "import json;e=json.load(open('broll/video/$b.call.json')).get('end_image');print('--last '+e if e else '')")
python3 ../../.claude/skills/ai-prompt-engineer/scripts/kie.py kling --prompt-file broll/video/$b.prompt.txt --first $img $last --duration $d --mode pro --out broll/video/${b}_v$v.mp4 > broll/video/${b}_v$v.kie.json 2>&1
echo "$b v$v done rc=$?"
