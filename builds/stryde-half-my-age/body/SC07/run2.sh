#!/bin/bash
cd /home/user/global-manual-ai/builds/stryde-half-my-age
b=SC07-T2
args=$(python3 -c "
import json,shlex;c=json.load(open('body/SC07/$b.call.json'))
a=['--prompt-file','body/SC07/$b.prompt.txt','--ref-image']+c['files']+['--duration',str(c['duration']),'--no-audio','--out','body/SC07/${b}_v1.mp4'];print(' '.join(shlex.quote(x) for x in a))")
eval python3 ../../.claude/skills/ai-prompt-engineer/scripts/kie.py seedance $args > body/SC07/$b.v1.kie.log 2>&1
