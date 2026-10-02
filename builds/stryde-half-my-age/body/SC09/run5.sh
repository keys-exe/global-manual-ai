#!/bin/bash
cd /home/user/global-manual-ai/builds/stryde-half-my-age
for bv in SC09-T1:4; do b=${bv%%:*}; v=${bv##*:}
  args=$(python3 -c "
import json,shlex;c=json.load(open('body/SC09/$b.call.json'))
a=['--prompt-file','body/SC09/$b.prompt.txt','--ref-image']+c['files']
if c['audios']: a+=['--ref-audio']+c['audios']
a+=['--duration',str(c['duration'])]
if not c['generate_audio']: a+=['--no-audio']
a+=['--out','body/SC09/${b}_v$v.mp4'];print(' '.join(shlex.quote(x) for x in a))")
  eval python3 ../../.claude/skills/ai-prompt-engineer/scripts/kie.py seedance $args > body/SC09/$b.v$v.kie.log 2>&1 &
  sleep 3
done
wait
