#!/usr/bin/env python3
"""Captions (cut 8: no background box) for a finished video: the script's spoken lines verbatim, timed to the video's own audio
(Whisper word times aligned to the script by assemble.align), phrase by phrase, white text with a black outline, no box (user 2026-10-01: "remove the caption background"),
one or two short lines, centred at ~72% height. Writes an .ass file and burns it in.
Usage: captions.py FINAL.mp4 OUT.mp4 [--script work/script.lines.txt] [--ass out.ass]"""
import sys, re, json, argparse, subprocess
from pathlib import Path
sys.path.insert(0, "/home/user/global-manual-ai/.claude/skills/ai-prompt-engineer/scripts")
import imageio_ffmpeg
from trim import words
from assemble import align
FF = imageio_ffmpeg.get_ffmpeg_exe()
ap = argparse.ArgumentParser(); ap.add_argument("video"); ap.add_argument("out")
ap.add_argument("--script", default="work/script.lines.txt"); ap.add_argument("--ass", default=None)
ap.add_argument("--max-words", type=int, default=6); ap.add_argument("--line-chars", type=int, default=22)
a = ap.parse_args()
wav = Path(a.out).with_suffix(".cap.wav")
subprocess.run([FF, "-v", "error", "-y", "-i", a.video, "-vn", "-ac", "1", "-ar", "16000", str(wav)], check=True)
ws = [(float(s), float(e), w) for s, e, w in words(wav, "base")]
wav.unlink()
sw = " ".join(Path(a.script).read_text().split()).split(" ")
tm = align(sw, ws)
# phrases: break after . , ? ! ; : or at max words
import math
clauses, cur = [], []
for (s, e, _w), w in zip(tm, sw):
    cur.append((w, s, e))
    if re.search(r"[.,?!;:]\W*$", w): clauses.append(cur); cur = []
if cur: clauses.append(cur)
caps = []
for c in clauses:                                   # a long clause splits into even chunks, never a greedy run
    n = math.ceil(len(c) / a.max_words); k = math.ceil(len(c) / n); i = 0
    WEAK = {"the","a","an","my","to","of","and","her","his","in","on","at","for","with","that","this","them","your","i","is","was","be","so","just","right"}
    while i < len(c):
        j = min(len(c), i + k)
        # never end a caption on a small word: move the break back (or forward) by one
        if j < len(c) and re.sub(r"\W", "", c[j - 1][0].lower()) in WEAK:
            j = j - 1 if j - 1 > i + 1 else j + 1
        if len(c) - j == 1: j = len(c)                  # never leave one word on its own
        caps.append(c[i:j]); i = j
def two_lines(ws_):
    t = " ".join(w for w, _, _ in ws_)
    if len(t) <= a.line_chars: return t
    best = min(range(1, len(ws_)), key=lambda k: abs(len(" ".join(w for w, _, _ in ws_[:k])) - len(" ".join(w for w, _, _ in ws_[k:]))))
    return " ".join(w for w, _, _ in ws_[:best]) + r"\N" + " ".join(w for w, _, _ in ws_[best:])
def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"
ev = []
for i, c in enumerate(caps):
    st = c[0][1]; en = c[-1][2]
    nxt = caps[i + 1][0][1] if i + 1 < len(caps) else en + 0.6
    en = min(max(en + 0.25, st + 0.6), nxt)            # hold a beat after the last word, never over the next caption
    ev.append((st, en, two_lines(c)))
hdr = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Box,DejaVu Sans,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,1,0,0,0,100,100,0,0,1,5,2,5,60,60,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ass = a.ass or str(Path(a.out).with_suffix(".ass"))
Path(ass).write_text(hdr + "".join(f"Dialogue: 0,{ts(s)},{ts(e)},Box,,0,0,0,,{{\\pos(540,1382)}}{t}\n" for s, e, t in ev))
subprocess.run([FF, "-v", "error", "-y", "-i", a.video, "-vf", f"ass={ass}", "-c:v", "libx264", "-crf", "18", "-c:a", "copy", "-movflags", "+faststart", a.out], check=True)
matched = sum(1 for x in __import__("difflib").SequenceMatcher(None, [re.sub(r"[^a-z0-9']","",w.lower()) for w in sw], [re.sub(r"[^a-z0-9']","",w.lower()) for _,_,w in ws], autojunk=False).get_matching_blocks() for _ in range(x.size))
print(json.dumps({"captions": len(ev), "script_words": len(sw), "matched_to_audio": matched, "ass": ass, "out": a.out}))
