"""Split one TTS take (all hooks + body in one request) into its parts at the silences between them.
usage: split_parts.py TAKE.mp3 OUTDIR   -> OUTDIR/raw_HK1.wav … raw_BODY.wav
Each part is cut from 0.03s before its first word to just before the next part's first word (−0.03s),
so no word decay is lost; vo_trim.py then shortens the air."""
import json, sys, subprocess, difflib, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / ".claude/skills/ai-prompt-engineer/scripts"))
from trim import words, duration
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
B = Path(__file__).resolve().parent.parent
take, outdir = Path(sys.argv[1]), Path(sys.argv[2]); outdir.mkdir(parents=True, exist_ok=True)
parts = ["HK1", "HK2", "HK3", "BODY"]
toks, owner = [], []
for p in parts:
    t = (B / f"vo/{p}.lines.txt").read_text().split(); toks += t; owner += [p] * len(t)
ws = words(take, "base.en")
norm = lambda s: re.sub(r"[^a-z0-9']", "", s.lower())
sm = difflib.SequenceMatcher(None, [norm(t) for t in toks], [norm(w) for _, _, w in ws], autojunk=False)
first = {}
for blk in sm.get_matching_blocks():
    for k in range(blk.size):
        p = owner[blk.a + k]
        first.setdefault(p, ws[blk.b + k][0])
total = duration(take)
rep = {}
for n, p in enumerate(parts):
    a = max(0.0, first[p] - 0.03)
    b = first[parts[n + 1]] - 0.03 if n + 1 < len(parts) else total
    out = outdir / f"raw_{p}.wav"
    subprocess.run([FF, "-v", "error", "-y", "-i", str(take), "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-ac", "1", "-ar", "44100", str(out)], check=True)
    rep[p] = {"from": round(a, 2), "to": round(b, 2), "s": round(b - a, 2)}
print(json.dumps(rep))
