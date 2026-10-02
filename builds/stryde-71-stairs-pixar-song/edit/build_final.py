#!/usr/bin/env python3
"""FINAL-HK1 — the finished music video (§3C).

v2 (user 2026-10-02: "the p01a reverse it to look walking backwards and slow it down, fix the broll placement also use a
caption fitting for a music video and not the plain one"):
- Placement: the cuts come from `music.py cuts` (V7.91.4) on the medium.en sung words (`edit/cuts_v2.json`): each picture
  lands 2 frames before its line's first sung word, or on a beat at most 0.25 s before it, never under the line before.
  v1 used the act map's beat-snapped cuts, on average 0.77 s early.
- P-01a: played in reverse (she comes down the stairs backwards toward the lens) and slowed to 0.65x, motion-interpolated.
- HK-01a: its clip is 0.6 s shorter than its now-correct slot, so it plays at 0.93x, motion-interpolated (no frozen frame).
- Lyrics: music-video captions (§3C V7.91.4) — Poppins ExtraBold, dark outline and soft shadow, no box, each word filled
  gold as it is sung (ASS \\kf on the aligned medium.en word times, `edit/lyric_words.json`), each line popping in.
- End card (F16) as v1: the C-07a clip's last frame held with a slow push over the 5.3 s hummed outro, the held offer and
  guarantee (§17) in the same lyric style.
The song is the whole soundtrack, untouched."""
import json, os, subprocess, textwrap, itertools
from pathlib import Path
H = Path(__file__).parent; B = H.parent
FPS, W, HH = 24, 1080, 1920
SONG = B / "intake/song.mp3"
VOCAL_END = 222.68
cuts = json.load(open(H / "cuts_v2.json"))["rows"]
clips = json.load(open(H / "clips.json"))
words = json.load(open(H / "lyric_words.json"))
lines = [l["line"] for l in json.load(open(B / "work/lyrics.timed.json"))]
SPECIAL = {"P-01a": {"reverse": True, "speed": 0.65}}      # the user's ask
F16_ENDCARD_SRC = "C-07a"
OVERLAYS = ["Buy 1 Get 1 Free", "60-day money-back guarantee"]   # held claims (§17)
OUT = H / "STRYDE_71_Stairs_Pixar_Song_HK1.mp4"
INTERP = "minterpolate=fps=24:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1"
FIT = f"scale={W}:{HH}:force_original_aspect_ratio=increase,crop={W}:{HH},setsar=1"


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True).stdout)


def frames(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-count_packets", "-select_streams", "v:0", "-show_entries", "stream=nb_read_packets",
                        "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout.strip()
    return int(r) if r.isdigit() else -1


def enc(args, out):
    n = int(args[args.index("-frames:v") + 1]) if "-frames:v" in args else None
    if n and Path(out).exists() and frames(out) == n:
        return                                   # already rendered at this length
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args, "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16",
                    "-preset", "medium", str(out)], check=True)


song_len = dur(SONG)
fr = lambda t: int(round(t * FPS))
tmp = H / "_work"; tmp.mkdir(exist_ok=True)
parts, log = [], []
for i, r in enumerate([] if os.environ.get("CAPTIONS_ONLY") else cuts):
    beat = r["beat"]; src = B / clips[beat]
    t0 = r["cut_s"]; t1 = VOCAL_END if i == len(cuts) - 1 else r["end_s"]
    n = fr(t1) - fr(t0); need = n / FPS; d = dur(src); seg = tmp / f"{i:03d}.mp4"
    sp = SPECIAL.get(beat)
    if sp:
        enc(["-i", str(src), "-vf", f"reverse,setpts=PTS/{sp['speed']},{INTERP},{FIT}", "-frames:v", str(n)], seg)
        how = f"reversed, {sp['speed']}x (interpolated)"; tin = 0.0
    elif d - 0.05 >= need:
        tin = max(0.0, min(0.4, d - need - 0.05))
        enc(["-ss", f"{tin:.3f}", "-i", str(src), "-vf", f"fps={FPS},{FIT}", "-frames:v", str(n)], seg)
        how = "1x"
    else:
        speed = round((d - 0.05) / need, 3); tin = 0.0
        enc(["-i", str(src), "-vf", f"setpts=PTS/{speed},{INTERP},{FIT}", "-frames:v", str(n)], seg)
        how = f"{speed}x to fill its slot (interpolated)"
    parts.append(seg)
    log.append({"beat": beat, "clip": clips[beat], "cut_s": round(t0, 3), "end_s": round(t1, 3), "frames": n, "in_s": round(tin, 3), "play": how})
# end card
end_t0 = VOCAL_END; n_end = fr(song_len) - fr(end_t0)
still = tmp / "end.png"
os.environ.get("CAPTIONS_ONLY") or subprocess.run(["ffmpeg", "-v", "error", "-y", "-sseof", "-0.1", "-i", str(B / clips[F16_ENDCARD_SRC]), "-frames:v", "1", "-update", "1", str(still)], check=True)
seg = tmp / "end.mp4"
os.environ.get("CAPTIONS_ONLY") or enc(["-loop", "1", "-i", str(still), "-frames:v", str(n_end), "-vf",
     f"scale={W*2}:{HH*2}:force_original_aspect_ratio=increase,crop={W*2}:{HH*2},"
     f"zoompan=z='1+0.06*on/{n_end}':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d=1:s={W}x{HH}:fps={FPS},setsar=1"], seg)
parts.append(seg); log.append({"beat": "END-CARD", "clip": clips[F16_ENDCARD_SRC] + " (last frame held)", "cut_s": end_t0, "end_s": round(song_len, 3), "frames": n_end})

# ---------- lyrics: music-video captions
def rows_of(text, width=16):
    if len(text) <= width:
        return [text]
    w = text.split()
    k = min(range(1, len(w)), key=lambda i: abs(len(" ".join(w[:i])) - len(" ".join(w[i:])))) if len(w) > 1 else 1
    return [" ".join(w[:k]), " ".join(w[k:])]


def chunks_of(text, cap=30):
    """Word index ranges: one chunk when the line fits two short rows, else even pieces, a break after punctuation preferred."""
    ws = text.split()
    if len(text) <= cap:
        return [(0, len(ws))]
    n = -(-len(text) // cap); best = None
    while best is None and n <= len(ws):
        for cut in itertools.combinations(range(1, len(ws)), n - 1):
            b = (0,) + cut + (len(ws),)
            pieces = [" ".join(ws[a:z]) for a, z in zip(b, b[1:])]
            if any(len(x) > cap for x in pieces):
                continue
            score = max(len(x) for x in pieces) - 8 * sum(ws[c - 1][-1] in ",.?!;:" for c in cut)
            if best is None or score < best[0]:
                best = (score, list(zip(b, b[1:])))
        n += 1
    return best[1]


def ts(t):
    t = max(0.0, t); h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


by_line = {}
for w in words:
    by_line.setdefault(w["line"], []).append(w)
chunks = []                      # (start, end, [(word, t)])
for n, text in enumerate(lines, 1):
    lw = by_line[n]
    for a, z in chunks_of(text):
        chunks.append([w for w in lw[a:z]])
ev = []
for k, ch in enumerate(chunks):
    st = ch[0]["t"] - 0.12
    nxt = chunks[k + 1][0]["t"] - 0.12 if k + 1 < len(chunks) else VOCAL_END + 0.2
    en = min(nxt, ch[-1]["end"] + 1.2) if nxt - ch[-1]["end"] > 1.5 else nxt
    if ev and st < ev[-1][1]:
        st = ev[-1][1]
    text_words = [w["w"] for w in ch]
    rws = rows_of(" ".join(text_words))
    split_at = len(rws[0].split())
    body = ""
    lead = max(0, round((ch[0]["t"] - st) * 100))
    if lead:
        body += f"{{\\k{lead}}}"
    for j, w in enumerate(ch):
        nt = ch[j + 1]["t"] if j + 1 < len(ch) else max(w["end"], w["t"] + 0.25)
        cs = max(5, round((nt - w["t"]) * 100))
        sep = "\\N" if j == split_at and len(rws) > 1 else (" " if j else "")
        body += f"{sep}{{\\kf{cs}}}{w['w']}"
    pop = "{\\fad(60,140)\\fscx82\\fscy82\\t(0,140,\\fscx100\\fscy100)}"
    ev.append((st, en, pop + body, "Lyric"))
ev.append((end_t0 + 0.2, song_len, "{\\fad(120,0)\\fscx80\\fscy80\\t(0,180,\\fscx100\\fscy100)}Buy 1 Get 1 Free", "Over0"))
ev.append((end_t0 + 0.7, song_len, "{\\fad(120,0)\\fscx80\\fscy80\\t(0,180,\\fscx100\\fscy100)}60-day money-back guarantee", "Over1"))
ass = H / "captions_HK1.ass"
# ASS colours are &HAABBGGRR: gold sung fill #FFC93C → &H003CC9FF; unsung white; outline dark brown #2B1A10 → &H00101A2B
head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {HH}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Lyric,Poppins ExtraBold,94,&H003CC9FF,&H00FFFFFF,&H00101A2B,&H96000000,0,0,0,0,100,100,1,0,1,7,4,2,60,60,500,1
Style: Over0,Poppins Black,96,&H003CC9FF,&H003CC9FF,&H00101A2B,&H96000000,0,0,0,0,100,100,1,0,1,7,4,2,70,70,640,1
Style: Over1,Poppins ExtraBold,66,&H00FFFFFF,&H00FFFFFF,&H00101A2B,&H96000000,0,0,0,0,100,100,1,0,1,6,4,2,70,70,520,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
ass.write_text(head + "".join(f"Dialogue: 0,{ts(a)},{ts(b)},{s},,0,0,0,,{t}\n" for a, b, t, s in ev))
if os.environ.get("CAPTIONS_ONLY"):
    raise SystemExit(f"captions only: {len(ev)} events → {ass}")
lst = tmp / "list.txt"; lst.write_text("".join(f"file '{p}'\n" for p in parts))
joined = tmp / "joined.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(joined)], check=True)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(joined), "-i", str(SONG), "-map", "0:v", "-map", "1:a",
                "-vf", f"ass={ass}:fontsdir={H / 'fonts'}", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-preset", "slow",
                "-r", str(FPS), "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", str(OUT)], check=True)
(H / "cutlist_HK1.json").write_text(json.dumps({"version": 2, "song_s": round(song_len, 3), "rows": log, "captions": len(ev)}, indent=1))
print(json.dumps({"out": str(OUT), "video_s": dur(OUT), "song_s": song_len, "rows": len(log), "captions": len(ev)}))
