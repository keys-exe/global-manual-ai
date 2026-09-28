"""One-go VO take (all five variants) -> verbatim check -> split into V1..V5 (hook n + its body) at the silences
between variants -> vo_trim.py house cut on each (raw hook + raw body of the same take, one pass) -> re-verify."""
import json, re, sys, glob, difflib, subprocess, os
import imageio_ffmpeg
from faster_whisper import WhisperModel
FF = imageio_ffmpeg.get_ffmpeg_exe()
VT = "/home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts/vo_trim.py"
NUM = {"17": "seventeen", "60": "sixty", "200000": "two hundred thousand", "18": "eighteen", "2": "two"}
def norm(s):
    s = s.lower().replace("-", " ").replace("’", "'").replace("getstryde.co", "get stryde dot co")
    s = re.sub(r"(\d),(\d)", r"\1\2", s)
    for k, v in NUM.items(): s = re.sub(rf"\b{k}\b", v, s)
    return re.sub(r"[^a-z0-9' ]", " ", s).split()
V = [open(f"HK{n}.lines.txt").read().strip() + " " + open(f"BODY{n}.lines.txt").read().strip() for n in range(1, 6)]
for n, t in enumerate(V, 1): open(f"V{n}.lines.txt", "w").write(t + "\n")
parts = [norm(t) for t in V]; ref = sum(parts, [])
m = WhisperModel("medium.en", compute_type="int8")
def words_of(f):
    segs, info = m.transcribe(f, word_timestamps=True, language="en", beam_size=5)
    w = [(t, x.start, x.end) for s in segs for x in s.words for t in norm(x.word)]
    return w, info.duration
def diff(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return sm, [(t, " ".join(a[i:j]), " ".join(b[k:l])) for t, i, j, k, l in sm.get_opcodes() if t != "equal"]
out = {}
takes = sys.argv[1:] or sorted(glob.glob("full/T?.mp3"))
os.makedirs("trim", exist_ok=True)
for f in takes:
    tid = os.path.basename(f)[:-4]
    words, dur = words_of(f); hyp = [w[0] for w in words]
    sm, d = diff(ref, hyp)
    rmap = {blk.a + k: blk.b + k for blk in sm.get_matching_blocks() for k in range(blk.size)}
    cuts, i = [], 0
    for p in parts[:-1]:
        i += len(p); last, first = rmap.get(i - 1), rmap.get(i)
        if last is None or first is None: cuts = None; break
        cuts.append(round((words[last][2] + words[first][1]) / 2, 3))
    rec = dict(dur=round(dur, 2), whole_diff=d, cuts=cuts, parts={})
    if cuts:
        edges = [0.0] + cuts + [dur]
        for n in range(5):
            raw = f"full/{tid}.V{n+1}.raw.mp3"; tr = f"trim/VO_{tid}_V{n+1}.mp3"
            subprocess.run([FF, "-v", "error", "-y", "-i", f, "-ss", str(edges[n]), "-to", str(edges[n+1]), "-c:a", "libmp3lame", "-b:a", "192k", raw], check=True)
            r = subprocess.run([sys.executable, VT, raw, "--out", tr, "--script", f"V{n+1}.lines.txt", "--max-wpm", "179"], capture_output=True, text=True)
            try: rep = json.loads(r.stdout)
            except Exception: rep = {"raw": r.stdout[-800:], "err": r.stderr[-800:]}
            w2, d2 = words_of(tr); _, dd = diff(parts[n], [x[0] for x in w2])
            json.dump([[a, round(b, 3), round(c, 3)] for a, b, c in w2], open(f"trim/VO_{tid}_V{n+1}.words.json", "w"))
            rec["parts"][f"V{n+1}"] = dict(raw_s=round(edges[n+1] - edges[n], 2), trim_s=round(d2, 2), verbatim=not dd, diff=dd, trim=rep)
    out[tid] = rec
    print(tid, json.dumps({k: (v if k != "parts" else {p: (x["trim_s"], x["verbatim"], x["diff"]) for p, x in v.items()}) for k, v in rec.items() if k != "whole_diff"}), "whole diff:", d[:8], flush=True)
    json.dump(out, open(f"split_{'_'.join(os.path.basename(t)[:-4] for t in takes)}.json", "w"), indent=1)
