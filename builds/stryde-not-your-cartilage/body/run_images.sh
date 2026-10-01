#!/bin/bash
# one Kie render per beat (one render per call); result JSON in body/<BEAT>_v<N>.json (N = $2, default 1)
cd "$(dirname "$0")/.."
b=$1; v=${2:-1}
read model refs < <(python3 -c "import json,sys;d=json.load(open('body/body.json'))['$b'];print(d['model'],' '.join(d['refs']))")
python3 ../../.claude/skills/ai-prompt-engineer/scripts/kie.py image $model --prompt-file body/$b.t2i.txt $( [ -n "$refs" ] && echo --ref $refs ) --out body/${b}_v${v}.png > body/${b}_v${v}.json 2>&1
echo "$b rc=$?"
