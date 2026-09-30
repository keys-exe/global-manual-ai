#!/usr/bin/env python3
"""fetch.py <name> <taskId> — wait for a Kie task, then download its clip through Kie's download-url (a direct signed link; the tempfile host
stalls mid-transfer). The size is checked against the GET response's Content-Length."""
import sys, json, subprocess, os, re
sys.path.insert(0, '/home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts'); import kie
name, tid = sys.argv[1], sys.argv[2]
out = f'/home/user/global-manual-ai/builds/down-forwards-again/acts/video/clips/{name}.mp4'
r, code = kie.wait(tid, timeout=3000)
if code: print(name, 'FAILED', r); sys.exit(1)
ok = False
for i in range(5):
    d = kie.call('POST', f'{kie.API}/common/download-url', {'url': r['urls'][0]})
    u = d.get('data') if d.get('code') == 200 else r['urls'][0]
    hp = out + '.hdr'
    subprocess.run(['curl', '-sS', '--max-time', '240', '-D', hp, '-o', out + '.part', u])
    m = re.findall(r'content-length:\s*(\d+)', open(hp).read().lower()) if os.path.exists(hp) else []
    size = int(m[-1]) if m else -1
    if os.path.exists(out + '.part') and os.path.getsize(out + '.part') == size: ok = True; break
os.path.exists(out + '.hdr') and os.remove(out + '.hdr')
if ok: os.replace(out + '.part', out)
r['size'] = size; r['ok'] = ok
json.dump(r, open(out.replace('.mp4', '.result.json'), 'w'), indent=1)
print(name, 'OK' if ok else 'INCOMPLETE', size, r.get('credits'))
