"""Finish one hook variant: burned-in captions (CAPCUT.md C1 style) + the background music, ducked under the VO.

usage: finish.py VARIANT.mp4 HOOK_ID --bgm edit/v4/bgm_v2.mp3 --hook-slot 16.5 --out OUT.mp4

- Word timings per part (hook alone, body alone), aligned to the verbatim script lines and offset by the
  hook's length on the 24 fps grid, exactly as assemble.py times the B-roll — so captions sit on the words.
- Cards: 1–3 words, broken at punctuation; white rounded box, black bold sans, centred at ~65% height;
  no keyword boxes (user 2026-09-29: plain captions only). Captions are the script's words, verbatim.
- Music: the BGM track is laid so its body sections start where the body starts (the track's hook slot is
  --hook-slot seconds, so a shorter hook starts the music that much later into the track). It is ducked under
  the VO (sidechain), faded out over the last 2 s, and the mix is normalised to −14 LUFS, true peak −1 dB (C9).
"""
import argparse, json, re, subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

B = Path(__file__).resolve().parent.parent
S = B.parents[1] / ".claude/skills/ai-prompt-engineer/scripts"
sys.path.insert(0, str(S))
from trim import words, duration  # noqa: E402
from assemble import align  # noqa: E402
import imageio_ffmpeg  # noqa: E402

FF = imageio_ffmpeg.get_ffmpeg_exe()
W, H, FPS = 1080, 1920, 24
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SIZE, PAD_X, PAD_Y, GAP, RADIUS, Y_CENTER = 66, 28, 16, 30, 20, 0.65
KEY1 = {"weight", "rail", "rails", "seriously", "second", "band", "seventeen", "stryde", "placement"}
KEY2 = {("six", "years"), ("one", "knee"), ("both", "knees")}
norm = lambda s: re.sub(r"[^a-z0-9']", "", s.lower())


def snap(t):
    return round(t * FPS) / FPS


def timed_words(hook):
    out, off = [], 0.0
    for part in (hook, "BODY"):
        audio = B / f"vo/master/{part}.wav"
        sw = (B / f"vo/{part}.lines.txt").read_text(encoding="utf-8").split()
        for s, e, w in align(sw, words(audio, "medium.en")):   # base.en was 0.1-0.7 s off (user 2026-09-29)
            out.append((s + off, e + off, w))
        off += snap(duration(audio))
    return out


def cards(ws):
    cs, cur = [], []
    for k, w in enumerate(ws):
        cur.append(w)
        nxt_gap = ws[k + 1][0] - w[1] if k + 1 < len(ws) else 9
        if len(cur) == 3 or re.search(r"[.,?!;:]$", w[2]) or nxt_gap > 0.35:
            cs.append(cur); cur = []
    if cur:
        cs.append(cur)
    timed = []
    for i, c in enumerate(cs):
        start = c[0][0]
        end = cs[i + 1][0][0] if i + 1 < len(cs) else c[-1][1] + 0.3
        if end - c[-1][1] > 0.5:          # a real pause: the card leaves with its last word
            end = c[-1][1] + 0.25
        timed.append((start, end, [w for _, _, w in c]))
    return timed


def keyflags(tokens):
    return [False] * len(tokens)   # user 2026-09-29: "remove the red caption stay normal caption"
    n = [norm(t) for t in tokens]
    flags = [x in KEY1 for x in n]
    for i in range(len(n) - 1):
        if (n[i], n[i + 1]) in KEY2:
            flags[i] = flags[i + 1] = True
    return flags


def render_card(tokens, flags, path, font):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    sizes = [d.textbbox((0, 0), t, font=font) for t in tokens]
    widths = [b[2] - b[0] for b in sizes]
    asc, desc = font.getmetrics()
    th = asc + desc
    total = sum(widths) + GAP * (len(tokens) - 1)
    box_w, box_h = total + 2 * PAD_X, th + 2 * PAD_Y
    x0, y0 = (W - box_w) // 2, int(H * Y_CENTER - box_h / 2)
    d.rounded_rectangle([x0, y0, x0 + box_w, y0 + box_h], RADIUS, fill=(255, 255, 255, 245))
    x = x0 + PAD_X
    for t, wdt, key in zip(tokens, widths, flags):
        if key:
            d.rounded_rectangle([x - 10, y0 + 6, x + wdt + 10, y0 + box_h - 6], 14, fill=(214, 30, 36, 255))
        d.text((x, y0 + PAD_Y), t, font=font, fill=(255, 255, 255, 255) if key else (10, 10, 10, 255))
        x += wdt + GAP
    img.save(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("hook")
    ap.add_argument("--bgm", required=True); ap.add_argument("--hook-slot", type=float, default=14.5)
    ap.add_argument("--music-db", type=float, default=-29.0, help="music gain before ducking (≈15 dB under a −28 LUFS VO)")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = Path(a.out); work = out.parent / f".{out.stem}_caps"; work.mkdir(parents=True, exist_ok=True)
    font = ImageFont.truetype(FONT, SIZE)
    ws = timed_words(a.hook)
    cs = cards(ws)
    blank = work / "blank.png"; Image.new("RGBA", (W, H), (0, 0, 0, 0)).save(blank)
    lines, t = ["ffconcat version 1.0"], 0.0
    for i, (s, e, toks) in enumerate(cs):
        if s - t > 1e-3:
            lines += [f"file '{blank.resolve()}'", f"duration {s - t:.3f}"]
        p = work / f"c{i:04d}.png"; render_card(toks, keyflags(toks), p, font)
        lines += [f"file '{p.resolve()}'", f"duration {e - s:.3f}"]; t = e
    total = duration(Path(a.video))
    lines += [f"file '{blank.resolve()}'", f"duration {max(total - t, 0.05):.3f}", f"file '{blank.resolve()}'"]
    (work / "caps.txt").write_text("\n".join(lines) + "\n")
    hook_len = snap(duration(B / f"vo/master/{a.hook}.wav"))
    off = max(a.hook_slot - hook_len, 0.0)
    fade_st = max(total - 2.0, 0)
    graph = (f"[1:v]format=rgba[c];[0:v][c]overlay=0:0:eof_action=pass:format=auto,format=yuv420p[v];"
             f"[2:a]atrim=start={off:.3f},asetpts=PTS-STARTPTS,aresample=48000,volume={a.music_db}dB,"
             f"afade=t=out:st={fade_st:.3f}:d=2[m];"
             f"[0:a]aresample=48000,asplit=2[vo][sc];"
             f"[m][sc]sidechaincompress=threshold=0.02:ratio=6:attack=15:release=350[md];"
             f"[vo][md]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1:LRA=11,volume=0.9dB,alimiter=limit=0.8:attack=5:release=80:level=false,aresample=48000[a]")
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-i", a.video,
                    "-f", "concat", "-safe", "0", "-i", str(work / "caps.txt"), "-i", a.bgm,
                    "-filter_complex", graph, "-map", "[v]", "-map", "[a]", "-r", str(FPS),
                    "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-c:a", "aac", "-b:a", "192k",
                    "-t", f"{total:.3f}", str(out)], check=True)
    json.dump({"cards": [{"start": round(s, 3), "end": round(e, 3), "text": " ".join(t)} for s, e, t in cs]},
              open(out.with_suffix(".captions.json"), "w"), indent=1)
    print(json.dumps({"out": str(out), "cards": len(cs), "music_offset_s": round(off, 3),
                      "duration_s": round(duration(out), 3), "video_s": round(total, 3)}))


if __name__ == "__main__":
    main()
