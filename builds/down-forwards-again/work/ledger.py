"""Append/update rows in run_ledger.json. usage: ledger.py BEAT key=value ..."""
import json, sys, os, datetime
F = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'run_ledger.json')
d = json.load(open(F)) if os.path.exists(F) else {}
def set_(beat, **kw):
    r = d.setdefault('beats', {}).setdefault(beat, {'beat_id': beat, 'retries': []})
    for k, v in kw.items():
        if k == 'retry': r['retries'].append({**json.loads(v), 'ts': datetime.datetime.utcnow().isoformat()})
        else: r[k] = v
    json.dump(d, open(F, 'w'), indent=1, ensure_ascii=False)
if __name__ == '__main__':
    set_(sys.argv[1], **dict(a.split('=', 1) for a in sys.argv[2:]))
