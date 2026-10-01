#!/usr/bin/env python3
"""Finish one hook variant (step 9): the hook cut + the body cut, burned-in captions (EG01) and the §40A music bed, ducked under the VO.
Adapted from builds/stryde-cascade/work/finish.py (user 2026-10-01: "confirm proceed, use the latest bgm update").

usage: finish.py HK1 → edit/final/FINAL-HK1.mp4

- Picture: hooks/plan/<HK>.rough.v4.mp4 (the confirmed hook cut) then edit/body/BODY.rough.mp4 (the body cut), joined frame-exact at 24 fps.
- Captions (EG01, the reference's): ONE word at a time, black bold sans on a small white rounded box, centred at ~65% height (mid-chest on the
  doctor; on the five split shots that is the top of the doctor's band). Words timed by faster-whisper medium.en aligned to the verbatim
  script lines (vo/<HK>.lines.txt, work/BODY.lines.txt), the body offset by the hook's length on the 24 fps grid; the caption is the script's word.
- Music: edit/music/BGM-<HK>.wav (the hook's MUS-OPEN cue, then the body bed from the hook's last word — work/bgm_mix.py), set ~18 dB under
  the voice (by measured loudness of the speech), ducked ~8 dB more while he speaks (sidechain), faded over the last 2 s; the mix normalised
  to −14 LUFS, true peak −1 dB (§24M levels, C9). EG08 (the reference has no music bed) is overridden by the user's call for music.
"""
import json, re, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np
B = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(B.parents[1] / ".claude/skills/ai-prompt-engineer/scripts"))
from trim import words, duration  # noqa: E402
from assemble import align  # noqa: E402
import imageio_ffmpeg  # noqa: E402
FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H, FPS = 1080, 1920, 24
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SIZE, PAD_X, PAD_Y, RADIUS, Y_CENTER, LINE_GAP, MAXW = 46, 20, 10, 14, 0.79, 4, 4   # user 2026-10-01: "THE CAPTION IS TOO BIG AND TOO HIGH"; "THE CAPTON SHOULD NOT COVER THE STRAP BRAND LOGO MOVE IT A BIT DOWN" (0.70 -> 0.79)
SAFE_L, SAFE_R = 100, 940          # the right-side rail (likes, comments, share) starts ~960 px
SAFE_CX, SAFE_W = (SAFE_L + SAFE_R) / 2, SAFE_R - SAFE_L
snap = lambda t: round(t * FPS) / FPS

def audio_of(video, out):
    subprocess.run([FF, "-y", "-v", "error", "-i", str(video), "-vn", "-ac", "1", "-ar", "48000", str(out)], check=True); return out

def speech_db(wav):
    raw = subprocess.run([FF, "-v", "error", "-i", str(wav), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(float) / 32768; w = 8000
    v = [np.sqrt((a[i:i + w] ** 2).mean()) for i in range(0, len(a) - w, w)]; v = [x for x in v if x > 0.01]
    return 20 * np.log10(np.median(v))

def timed_words(hook, hook_wav, body_wav):
    out, off = [], 0.0
    for wav, lines in ((hook_wav, B / f"vo/{hook}.lines.txt"), (body_wav, B / "work/BODY.lines.txt")):
        sw = lines.read_text(encoding="utf-8").split()
        for s, e, w in align(sw, words(wav, "medium.en")):
            out.append((s + off, e + off, w))
        off += snap(duration(wav))
    return out

def cards(ws):
    """2-4 words a card (user 2026-10-01: "the caption should not be one word only use the safezone"),
    broken at punctuation or a pause; a lone word joins its neighbour when they run together."""
    phrases, cur = [], []                      # phrases end at punctuation or a pause
    for k, w in enumerate(ws):
        cur.append(w)
        gap = ws[k + 1][0] - w[1] if k + 1 < len(ws) else 9
        if re.search(r"[.,?!;:]$", w[2]) or gap > 0.35:
            phrases.append(cur); cur = []
    if cur: phrases.append(cur)
    out = []
    for ph in phrases:
        if len(ph) == 1 and out and len(out[-1]) < MAXW and not re.search(r"[.?!]$", out[-1][-1][2]) \
                and ph[0][0] - out[-1][-1][1] <= 0.35:
            out[-1] = out[-1] + ph; continue      # a lone word joins its phrase before, inside one sentence
        k = -(-len(ph) // MAXW); q, r = divmod(len(ph), k); i = 0
        for j in range(k):                        # balanced: 5 words -> 3 + 2, never 4 + 1
            n = q + (1 if j < r else 0); out.append(ph[i:i + n]); i += n
    timed = []
    for i, c in enumerate(out):
        end = out[i + 1][0][0] if i + 1 < len(out) else c[-1][1] + 0.3
        if end - c[-1][1] > 0.5: end = c[-1][1] + 0.25          # a real pause: the card leaves with its last word
        timed.append((c[0][0], max(end, c[0][0] + 0.2), " ".join(w for _, _, w in c)))
    return timed

def wrap(text, font, d):
    """One line when it fits; else the two-line split with the most even widths."""
    ws, room = text.split(), SAFE_W - 2 * PAD_X
    if d.textlength(text, font=font) <= room: return [text]
    best = min(((" ".join(ws[:i]), " ".join(ws[i:])) for i in range(1, len(ws))),
               key=lambda l: max(d.textlength(x, font=font) for x in l))
    return list(best)

def render_card(text, path, font):
    """Centred in the 9:16 safe zone: clear of the top 14 %, the bottom 25 % (caption/CTA UI) and the right-side
    button rail; at most SAFE_W wide, wrapped to two lines."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    lines = wrap(text, font, d); asc, desc = font.getmetrics(); lh = asc + desc
    widths = [d.textlength(l, font=font) for l in lines]
    bw = int(max(widths)) + 2 * PAD_X; bh = lh * len(lines) + LINE_GAP * (len(lines) - 1) + 2 * PAD_Y
    x0 = int(SAFE_CX - bw / 2); y0 = int(H * Y_CENTER - bh / 2)
    assert x0 >= SAFE_L and x0 + bw <= SAFE_R and y0 >= H * 0.14 and y0 + bh <= H * 0.84, (text, x0, bw, y0, bh)
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], RADIUS, fill=(255, 255, 255, 245))
    for i, (l, wd) in enumerate(zip(lines, widths)):
        d.text((SAFE_CX - wd / 2, y0 + PAD_Y + i * (lh + LINE_GAP)), l, font=font, fill=(10, 10, 10, 255))
    img.save(path)

def main():
    hook = sys.argv[1]
    outd = B / "edit/final"; outd.mkdir(parents=True, exist_ok=True); work = outd / f".{hook}_caps"; work.mkdir(exist_ok=True)
    hv, bv = B / f"hooks/plan/{hook}.rough.v4.mp4", B / "edit/body/BODY.rough.mp4"
    joined = work / "joined.mp4"
    subprocess.run([FF, "-y", "-v", "error", "-i", str(hv), "-i", str(bv), "-filter_complex",
                    "[0:v]fps=24,scale=1080:1920,setsar=1[v0];[1:v]fps=24,scale=1080:1920,setsar=1[v1];"
                    "[0:a]aresample=48000[a0];[1:a]aresample=48000[a1];[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a]",
                    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-c:a", "pcm_s16le", str(joined.with_suffix(".mov"))], check=True)
    joined = joined.with_suffix(".mov")
    hook_wav = audio_of(hv, work / "hook.wav"); body_wav = audio_of(bv, work / "body.wav")
    font = ImageFont.truetype(FONT, SIZE)
    cs = cards(timed_words(hook, hook_wav, body_wav))
    blank = work / "blank.png"; Image.new("RGBA", (W, H), (0, 0, 0, 0)).save(blank)
    lines, t = ["ffconcat version 1.0"], 0.0
    for i, (s, e, tok) in enumerate(cs):
        if s - t > 1e-3: lines += [f"file '{blank.resolve()}'", f"duration {s - t:.3f}"]
        p = work / f"c{i:04d}.png"; render_card(tok, p, font); lines += [f"file '{p.resolve()}'", f"duration {e - s:.3f}"]; t = e
    total = duration(joined)
    lines += [f"file '{blank.resolve()}'", f"duration {max(total - t, 0.05):.3f}", f"file '{blank.resolve()}'"]
    (work / "caps.txt").write_text("\n".join(lines) + "\n")
    bgm = B / f"edit/music/v2/BGM-{hook}.wav"   # music v2 (user 2026-10-01: investigation, lifts when the product shows, not sad)
    vo_db = speech_db(joined); mus_db = speech_db(bgm)
    gain = vo_db - 18 - mus_db
    fade_st = max(total - 2.0, 0)
    graph = (f"[1:v]format=rgba[c];[0:v][c]overlay=0:0:eof_action=pass:format=auto,format=yuv420p[v];"
             f"[2:a]aresample=48000,volume={gain:.2f}dB,afade=t=out:st={fade_st:.3f}:d=2[m];"
             f"[0:a]aresample=48000,asplit=2[vo][sc];"
             f"[m][sc]sidechaincompress=threshold=0.02:ratio=4:attack=20:release=350[md];"
             f"[vo][md]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1:LRA=11,alimiter=limit=0.89:level=false,aresample=48000[a]")
    out = outd / f"FINAL-{hook}.mp4"
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-i", str(joined), "-f", "concat", "-safe", "0", "-i", str(work / "caps.txt"),
                    "-i", str(bgm), "-filter_complex", graph, "-map", "[v]", "-map", "[a]", "-r", str(FPS),
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.3f}", str(out)], check=True)
    json.dump({"cards": [{"start": round(s, 3), "end": round(e, 3), "text": w} for s, e, w in cs]}, open(out.with_suffix(".captions.json"), "w"), indent=1)
    print(json.dumps({"out": str(out), "cards": len(cs), "music_gain_db": round(gain, 2), "duration_s": round(duration(out), 3)}))

if __name__ == "__main__":
    main()
