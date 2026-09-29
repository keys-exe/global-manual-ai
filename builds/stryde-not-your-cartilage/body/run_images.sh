#!/bin/bash
# one Kie render per beat (one render per call); result JSON in body/<BEAT>_v1.json
cd "$(dirname "$0")/.."
b=$1
read model refs < <(python3 -c "import json,sys;d=json.load(open('body/body.json'))['$b'];print(d['model'],' '.join(d['refs']))")
python3 ../../.claude/skills/ai-prompt-engineer/scripts/kie.py image $model --prompt-file body/$b.t2i.txt $( [ -n "$refs" ] && echo --ref $refs ) --out body/${b}_v1.png > body/${b}_v1.json 2>&1
echo "$b rc=$?"
