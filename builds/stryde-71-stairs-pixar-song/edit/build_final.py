#!/usr/bin/env python3
"""FINAL-HK1 — the finished music video (§3C): the 61 confirmed clips cut on the act map's beat-snapped lyric cuts
(`work/actmap_rows.json` t_in/t_out = docs/actmap), the song laid under whole and untouched, EG01 lyric captions
(black text on white boxes, one or two short rows at ~72 % height, phrase by phrase, verbatim from work/lyrics.timed.json),
and the 5.34 s instrumental outro as the end card (F16: the two straps in the box + the held offer and guarantee as overlays, §17).
No speed change, no slowed clip; each clip enters 0.4 s in (its frozen opening skipped) unless it is too short for that."""
import json, subprocess, sys, tempfile, textwrap
from pathlib import Path
H = Path(__file__).parent; B = H.parent
FPS, W, HH = 24, 1080, 1920
SONG = B / "intake/song.mp3"
rows = json.load(open(B / "work/actmap_rows.json"))
clips = json.load(open(H / "clips.json"))           # beat -> confirmed clip file (the board's current video version)
lyr = json.load(open(B / "work/lyrics.timed.json"))
F16_ENDCARD_SRC = "C-07a"                            # its last frame: lid aside, wordmark clear, two straps in the box
OVERLAYS = ["Buy 1 Get 1 Free", "60-day money-back guarantee"]   # held claims (Product Sheet register), §17 post overlays
LINE37 = (84.5, 86.3)                                # F4: "Stryde." carried by the caption
OUT = H / "STRYDE_71_Stairs_Pixar_Song_HK1.mp4"

def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True).stdout)

song_len = dur(SONG)
fr = lambda t: int(round(t * FPS))
tmp = H / "_work"; tmp.mkdir(exist_ok=True); parts = []; log = []
REUSE = (tmp / "joined.mp4").exists()
# --- picture: one segment per act-map row, frame-exact on the 24 fps grid
for i, r in enumerate(rows):
    src = B / clips[r["beat"]]; n = fr(r["t_out"]) - fr(r["t_in"]); need = n / FPS
    tin = max(0.0, min(0.4, dur(src) - need - 0.05))
    seg = tmp / f"{i:03d}.mp4"
    if not REUSE: subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{tin:.3f}", "-i", str(src), "-frames:v", str(n), "-an",
                    "-vf", f"scale={W}:{HH}:force_original_aspect_ratio=increase,crop={W}:{HH},fps={FPS},setsar=1",
                    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "medium", str(seg)], check=True)
    parts.append(seg); log.append({"beat": r["beat"], "clip": clips[r["beat"]], "cut_s": r["t_in"], "end_s": r["t_out"], "frames": n, "in_s": round(tin, 3)})
# --- end card: the source clip's last frame held, a slow 6 % push, to the end of the song
end_t0 = rows[-1]["t_out"]; n_end = fr(song_len) - fr(end_t0)
still = tmp / "end.png"
src = B / clips[F16_ENDCARD_SRC]
REUSE or subprocess.run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.1", "-i", str(src), "-frames:v", "1", "-update", "1", str(still)], check=True)
seg = tmp / "end.mp4"
REUSE or subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", str(still), "-frames:v", str(n_end),
                "-vf", f"scale={W*2}:{HH*2}:force_original_aspect_ratio=increase,crop={W*2}:{HH*2},"
                       f"zoompan=z='1+0.06*on/{n_end}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:s={W}x{HH}:fps={FPS},setsar=1",
                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", str(seg)], check=True)
parts.append(seg); log.append({"beat": "END-CARD", "clip": clips[F16_ENDCARD_SRC] + " (last frame held)", "cut_s": end_t0, "end_s": round(song_len, 3), "frames": n_end})
# --- captions (EG01)
def rows_of(text, width=18):
    """One row when it fits; else two balanced rows split at the word break nearest the middle (EG01: one or two short rows)."""
    if len(text) <= width:
        return [text]
    w = text.split()
    k = min(range(1, len(w)), key=lambda i: abs(len(" ".join(w[:i])) - len(" ".join(w[i:])))) if len(w) > 1 else 1
    return [" ".join(w[:k]), " ".join(w[k:])] if len(w) > 1 else [text]
def chunks_of(text, cap=34):
    """One caption when the line fits two short rows; else even pieces at word breaks, a break after punctuation preferred."""
    if len(text) <= cap:
        return [rows_of(text)]
    import itertools
    words = text.split(); n = -(-len(text) // cap); best = None
    while best is None and n <= len(words):
        for cut in itertools.combinations(range(1, len(words)), n - 1):
            pieces = [" ".join(words[a:b]) for a, b in zip((0,) + cut, cut + (len(words),))]
            if any(len(x) > cap for x in pieces):
                continue
            score = max(len(x) for x in pieces) - 8 * sum(words[c - 1][-1] in ",.?!;:" for c in cut)
            if best is None or score < best[0]:
                best = (score, pieces)
        n += 1
    return [rows_of(x) for x in best[1]]
def ts(t):
    t = max(0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"
ev = []
for i, l in enumerate(lyr):
    st, en = (l["start"], l["end"]) if l["start"] is not None else LINE37
    if i + 1 < len(lyr) and lyr[i + 1]["start"] is not None and lyr[i + 1]["start"] - en < 0.35:
        en = lyr[i + 1]["start"]                      # no flicker between touching lines
    chunks = chunks_of(l["line"])                     # at most two rows a caption
    tot = sum(len(" ".join(c)) for c in chunks); t = st
    for c in chunks:
        d = (en - st) * len(" ".join(c)) / tot
        ev.append((t, t + d, "\\N".join(c))); t += d
for k, o in enumerate(OVERLAYS):
    ev.append((end_t0 + 0.25 + 0.5 * k, song_len, o, "Over" + str(k)))
ass = H / "captions_HK1.ass"
head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {HH}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Lyric,DejaVu Sans,58,&H00000000,&H00000000,&H00FFFFFF,&H00FFFFFF,0,0,0,0,100,100,0,0,3,14,0,2,80,80,470,1
Style: Over0,DejaVu Sans,64,&H00000000,&H00000000,&H00FFFFFF,&H00FFFFFF,-1,0,0,0,100,100,0,0,3,16,0,2,80,80,560,1
Style: Over1,DejaVu Sans,56,&H00000000,&H00000000,&H00FFFFFF,&H00FFFFFF,0,0,0,0,100,100,0,0,3,14,0,2,80,80,440,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
body = "".join(f"Dialogue: 0,{ts(e[0])},{ts(e[1])},{e[3] if len(e) > 3 else 'Lyric'},,0,0,0,,{e[2]}\n" for e in ev)
ass.write_text(head + body)
# --- join, captions burnt in, the song whole under it
lst = tmp / "list.txt"; lst.write_text("".join(f"file '{p}'\n" for p in parts))
joined = tmp / "joined.mp4"
REUSE or subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(joined)], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(joined), "-i", str(SONG), "-map", "0:v", "-map", "1:a",
                "-vf", f"ass={ass}", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "slow", "-r", str(FPS),
                "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", str(OUT)], check=True)
(H / "cutlist_HK1.json").write_text(json.dumps({"song_s": round(song_len, 3), "rows": log, "captions": len(ev)}, indent=1))
print(json.dumps({"out": str(OUT), "video_s": dur(OUT), "song_s": song_len, "rows": len(log), "captions": len(ev)}))
