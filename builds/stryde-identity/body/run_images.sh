#!/bin/bash
# one Kie GPT Image call per beat (one render per call); logs to <BEAT>.kie.json
b=$1; U=https://tempfile.redpandaai.co/kieai/329820/pipeline
refs=$(python3 -c "import json;print(' '.join('$U/'+r for r in json.load(open('body_v1.json'))['$b']['refs']))")
python3 /home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts/kie.py image gpt-image-2-5-sunburst-image-to-image --prompt-file $b.t2i.txt --ref $refs --out ${b}_r2.png > $b.r2.kie.json 2>&1
echo "$b $(python3 -c "import json;d=json.load(open('$b.r2.kie.json'));print(d.get('state'),d.get('failMsg') or '')" 2>/dev/null || echo error)"
