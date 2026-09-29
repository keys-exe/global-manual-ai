#!/bin/bash
# usage: kget.sh BEAT NAME.mp4  (Kling urlWithoutWatermark file name)
cd "$(dirname "$0")/.."
U="https://v15-kling.klingai.com/bs2/upload-ylab-stunt-sgp/$2?x-kcdn-pid=112372"
curl -sSL -o renders/$1.mp4 "$U" && python3 - "$1" "$U" <<'P'
import json,sys,os
p='work/kling_urls.json'; d=json.load(open(p)) if os.path.exists(p) else {}
d[sys.argv[1]]=sys.argv[2]; json.dump(d,open(p,'w'),indent=1)
P
python3 ../../.claude/skills/ai-prompt-engineer/scripts/contact_sheet.py renders/$1.mp4 --out renders/$1_sheet.jpg 2>/dev/null | python3 -c "import json,sys;d=json.load(sys.stdin);print('$1',d.get('duration_s'),d.get('frozen_runs_s'),d.get('black_runs_s'))"
