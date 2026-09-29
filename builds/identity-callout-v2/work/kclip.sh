#!/bin/bash
# usage: kclip.sh BEAT uuid-token   (downloads watermark-free clip + contact sheet)
K=https://v15-kling.klingai.com/bs2/upload-ylab-stunt-sgp
curl -sSL -o renders/$1.mp4 "$K/$2-output.mp4?x-kcdn-pid=112372"
python3 ../../.claude/skills/ai-prompt-engineer/scripts/contact_sheet.py renders/$1.mp4 --frames 6 --out work/$1.sheet.jpg | python3 -c "import json,sys;d=json.load(sys.stdin);print('$1',d['duration_s'],d['resolution'],d['aspect_9x16'],d['frozen_runs_s'],d['black_runs_s'])"
