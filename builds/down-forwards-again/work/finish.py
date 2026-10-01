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
SIZE, PAD_X, PAD_Y, RADIUS, Y_CENTER = 70, 26, 14, 18, 0.65
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
    timed = []
    for i, (s, e, w) in enumerate(ws):
        nxt = ws[i + 1][0] if i + 1 < len(ws) else e + 0.3
        end = nxt if nxt - e <= 0.5 else e + 0.25          # one word per card; a real pause: the card leaves with its word
        timed.append((s, max(end, s + 0.12), w))
    return timed

def render_card(tok, path, font):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    b = d.textbbox((0, 0), tok, font=font); wdt = b[2] - b[0]; asc, desc = font.getmetrics(); th = asc + desc
    bw, bh = wdt + 2 * PAD_X, th + 2 * PAD_Y; x0, y0 = (W - bw) // 2, int(H * Y_CENTER - bh / 2)
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], RADIUS, fill=(255, 255, 255, 245))
    d.text((x0 + PAD_X - b[0], y0 + PAD_Y), tok, font=font, fill=(10, 10, 10, 255)); img.save(path)

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
    bgm = B / f"edit/music/BGM-{hook}.wav"
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
