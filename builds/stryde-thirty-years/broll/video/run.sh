#!/bin/bash
# one Kling 3.0 (Kie) call per beat, from its confirmed start image, at its E6 length
b=$1; cd "$(dirname "$0")/../.."
d=$(python3 -c "import json;print(json.load(open('broll/video/$b.call.json'))['duration'])")
img=$(python3 -c "import json;print(json.load(open('broll/video/_confirmed.json'))['$b'])")
python3 ../../.claude/skills/ai-prompt-engineer/scripts/kie.py kling --prompt-file broll/video/$b.prompt.txt --first $img --duration $d --mode pro --out broll/video/${b}_v1.mp4 > broll/video/${b}_v1.kie.json 2>&1
echo "$b done rc=$?"
