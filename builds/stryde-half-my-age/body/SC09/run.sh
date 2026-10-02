#!/bin/bash
cd /home/user/global-manual-ai/builds/stryde-half-my-age
for b in SC09-T1 SC09-T2 SC09-T3 SC10-T1 SC10-T2 SC10-T3 SC10-T4 SC10-T5; do
  args=$(python3 -c "
import json,shlex;c=json.load(open('body/SC09/$b.call.json'))
a=['--prompt-file','body/SC09/$b.prompt.txt','--ref-image']+c['files']
if c['audios']: a+=['--ref-audio']+c['audios']
a+=['--duration',str(c['duration'])]
if not c['generate_audio']: a+=['--no-audio']
a+=['--out','body/SC09/${b}_v1.mp4'];print(' '.join(shlex.quote(x) for x in a))")
  eval python3 ../../.claude/skills/ai-prompt-engineer/scripts/kie.py seedance $args > body/SC09/$b.v1.kie.log 2>&1 &
  sleep 3
done
wait
