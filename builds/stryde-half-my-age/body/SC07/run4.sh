#!/bin/bash
cd /home/user/global-manual-ai/builds/stryde-half-my-age
for b in SC07-T2; do
  args=$(python3 -c "
import json,shlex;c=json.load(open('body/SC07/$b.call.json'))
a=['--prompt-file','body/SC07/$b.prompt.txt','--ref-image']+c['files']
if c['audios']: a+=['--ref-audio']+c['audios']
a+=['--duration',str(c['duration'])]
if not c['generate_audio']: a+=['--no-audio']
a+=['--out','body/SC07/${b}_v2.mp4'];print(' '.join(shlex.quote(x) for x in a))")
  eval python3 ../../.claude/skills/ai-prompt-engineer/scripts/kie.py seedance $args > body/SC07/$b.v2.kie.log 2>&1 &
  sleep 3
done
wait
