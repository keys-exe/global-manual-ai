#!/bin/bash
cd /home/user/global-manual-ai/builds/stryde-half-my-age
for bv in SC11/SC12-T1:2 SC11/SC13-T2:2; do p=${bv%%:*}; v=${bv##*:}; d=${p%%/*}; b=${p##*/}
  args=$(python3 -c "
import json,shlex;c=json.load(open('body/$d/$b.call.json'))
a=['--prompt-file','body/$d/$b.prompt.txt','--ref-image']+c['files']
if c['audios']: a+=['--ref-audio']+c['audios']
a+=['--duration',str(c['duration'])]
if not c['generate_audio']: a+=['--no-audio']
a+=['--out','body/$d/${b}_v$v.mp4'];print(' '.join(shlex.quote(x) for x in a))")
  eval python3 ../../.claude/skills/ai-prompt-engineer/scripts/kie.py seedance $args > body/$d/$b.v$v.kie.log 2>&1 &
  sleep 3
done
wait
