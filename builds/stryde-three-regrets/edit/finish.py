"""CapCut finish (§40 block in CAPCUT.md), applied to the picture-locked rough cuts.

    python3 finish.py <n> [--measure-only]

Reads   media/ROUGH-HK<n>.mp4, vo/master/HK<n>.words.json (script-aligned), capcut_times.json,
        assemble_HK<n>.json (timeline) and STEP4_5.md (beat -> location).
Writes  media/STRYDE_THREE_REGRETS_HK<n>.mp4, edit/final/HK<n>.ass, edit/final/finish_HK<n>.json.

Nothing here changes a cut, a spoken word or the pace: text is burnt in on top, colour is a
per-clip match to the location's first clip (no LUT, no grain — Mode 1), the audio is the
master normalised to -14 LUFS / <= -1 dBTP, and the last 0.3 s fades to black.
"""
import json, re, subprocess, sys
from pathlib import Path

import imageio_ffmpeg
from fontTools.ttLib import TTFont

FF = imageio_ffmpeg.get_ffmpeg_exe()
HERE = Path(__file__).resolve().parent
BUILD = HERE.parent
MEDIA = Path("/tmp/claude-0/-home-user-global-manual-ai/10717553-fbf6-591d-840c-948130683a36/scratchpad/media")
FONT = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
W, H, FPS = 1080, 1920, 24

BANNER = {1: ("3 things people wish", "they'd known about their knees"),
          2: ("25,000 people wrote to us", "3 things came up again and again"),
          3: ("The #1 regret we hear", "isn't surgery. It's 2 cm.")}
CARDS = [("BR-003", "Regret No. 1"), ("BR-017", "Regret No. 2"), ("BR-024", "Regret No. 3")]
OVERLAYS = [("MECH-011", "17×", 190), ("BR-043", "34% less strain", 110), ("BR-046", "200,000", 170)]

# ---------- text measurement (libass sizes a font by its win ascent + descent) ----------
_f = TTFont(FONT)
_cmap, _hmtx = _f.getBestCmap(), _f["hmtx"]
_LINE = _f["OS/2"].usWinAscent + _f["OS/2"].usWinDescent


def text_w(s, size):
    return sum(_hmtx[_cmap.get(ord(c), _cmap[ord("?")])][0] for c in s) * size / _LINE


def ts(t):
    t = max(0.0, t)
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


def rounded(w, h, r):
    return (f"m {r} 0 l {w - r} 0 b {w} 0 {w} 0 {w} {r} l {w} {h - r} b {w} {h} {w} {h} {w - r} {h} "
            f"l {r} {h} b 0 {h} 0 {h} 0 {h - r} l 0 {r} b 0 0 0 0 {r} 0")


def boxed(t0, t1, text, cy, size=62, maxw=960):
    """Black bold text on a white rounded box, centred on (540, cy) — EG02 / EG03 style."""
    while text_w(text, size) > maxw - 56 and size > 40:
        size -= 2
    tw = text_w(text, size)
    bw, bh = round(tw + 56), round(size * 1.0 + 30)
    x0, y0 = round(540 - bw / 2), round(cy - bh / 2)
    return [f"Dialogue: 0,{ts(t0)},{ts(t1)},Box,,0,0,0,,{{\\an7\\pos({x0},{y0})\\p1}}{rounded(bw, bh, 22)}{{\\p0}}",
            f"Dialogue: 1,{ts(t0)},{ts(t1)},Cap,,0,0,0,,{{\\an5\\pos(540,{cy})\\fs{size}}}{text}"]


# ---------- EG02 caption groups: 4–8 words, never across a sentence ----------
def groups(words):
    """Per sentence: split at commas into clauses, split any clause over 8 words into even
    parts of <= 7, then pack clauses into groups of <= 8 words. No group crosses a sentence."""
    import math
    sents, cur = [], []
    for w in words:
        cur.append(w)
        if re.search(r"[.!?]$", w[0]):
            sents.append(cur)
            cur = []
    if cur:
        sents.append(cur)
    out = []
    for sent in sents:
        clauses, c = [], []
        for w in sent:
            c.append(w)
            if w[0].endswith(",") and len(c) >= 3:
                clauses.append(c)
                c = []
        if c:
            if clauses and len(c) < 3:
                clauses[-1] += c
            else:
                clauses.append(c)
        pieces = []
        for c in clauses:
            if len(c) > 8:
                k = math.ceil(len(c) / 7)
                step = len(c) / k
                pieces += [c[round(i * step):round((i + 1) * step)] for i in range(k)]
            else:
                pieces.append(c)
        g = []
        for pc in pieces:
            if g and len(g) + len(pc) > 8:
                out.append(g)
                g = []
            g = g + pc
        out.append(g)
    return out


def caption_events(gs, master):
    ev, spans = [], []
    for k, g in enumerate(gs):
        t0 = g[0][1]
        t1 = g[-1][2] + 0.25
        if k + 1 < len(gs):
            nxt = gs[k + 1][0][1]
            t1 = nxt if nxt - g[-1][2] < 0.6 else min(t1, nxt)
        t1 = min(t1, master)
        text = " ".join(w for w, _, _ in g)
        spans.append((t0, t1))
        ev += boxed(t0, t1, text, 1100)
    return ev, spans


# ---------- colour: per-clip match to the location's first clip ----------
def location_map():
    loc = {}
    for line in (BUILD / "STEP4_5.md").read_text().splitlines():
        m = re.match(r"\| (HK\d-\d+|BR-\d+\w?|PR-\d+\w?|MECH-\d+) \|", line)
        if m:
            c = [x.strip() for x in line.split("|")]
            loc[m.group(1)] = c[6]
    return loc


def mean_rgb(src, t):
    raw = subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", str(src), "-frames:v", "1",
                          "-vf", "scale=54:96", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         capture_output=True, check=True).stdout
    n = len(raw) // 3
    return [sum(raw[c::3]) / n for c in range(3)]


def colour_plan(src, timeline):
    loc = location_map()
    ref, plan = {}, []
    for seg in timeline:
        b = seg.get("beat")
        if seg["kind"] != "BR" or not b or b.startswith("MECH"):
            continue  # talking head and anatomy shots stay as rendered
        L = loc.get(b)
        if not L or not L.startswith("L-"):
            continue
        s, e = seg["start"], seg["end"]
        ms = [mean_rgb(src, s + (e - s) * f) for f in (0.25, 0.5, 0.75)]
        R, G, B = (sum(m[c] for m in ms) / 3 for c in range(3))
        Y = 0.2126 * R + 0.7152 * G + 0.0722 * B
        row = {"beat": b, "loc": L, "start": s, "end": e, "rgb": [round(R, 1), round(G, 1), round(B, 1)]}
        if L not in ref:
            ref[L] = (R / G, B / G, Y)
            row["ref"] = True
        else:
            rr, rb, ry = ref[L]
            clamp = lambda x, d: max(1 - d, min(1 + d, x))
            kg = clamp((ry / Y) ** 0.5, 0.04)                   # half-strength exposure match
            kr = kg * clamp((rr / (R / G)) ** 0.5, 0.03)          # half-strength white balance
            kb = kg * clamp((rb / (B / G)) ** 0.5, 0.03)
            if max(abs(kr - 1), abs(kg - 1), abs(kb - 1)) >= 0.02:
                row["gain"] = [round(kr, 3), round(kg, 3), round(kb, 3)]
        plan.append(row)
    return plan


def loud_measure(src):
    err = subprocess.run([FF, "-hide_banner", "-i", str(src), "-vn", "-af",
                          "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return json.loads(err[err.rindex("{"):err.rindex("}") + 1])


def main():
    n = int(sys.argv[1])
    src = MEDIA / f"ROUGH-HK{n}.mp4"
    out = MEDIA / f"STRYDE_THREE_REGRETS_HK{n}.mp4"
    times = json.loads((HERE / "capcut_times.json").read_text())[str(n)]
    master = times["master"]
    timeline = json.loads((HERE / f"assemble_HK{n}.json").read_text())["timeline"]
    words = json.loads((BUILD / "vo" / "master" / f"HK{n}.captions.json").read_text())

    # ASS layer
    gs = groups(words)
    cap_ev, spans = caption_events(gs, master)
    ev = list(cap_ev)
    b1, b2 = BANNER[n]
    ev.append(f"Dialogue: 2,{ts(0)},{ts(times['hook_end'])},Banner,,0,0,0,,{b1}\\N{b2}")
    for beat, label in CARDS:
        t0 = times[beat][0]
        after = [sp for sp in spans if sp[1] > t0 + 0.05]
        t1 = after[min(2, len(after) - 1)][1]  # held for the first 3 caption groups of the regret
        ev += boxed(t0, t1, label, 972, size=64)
    for beat, label, size in OVERLAYS:
        t0, t1 = times[beat]
        ev.append(f"Dialogue: 2,{ts(t0)},{ts(t1)},Big,,0,0,0,,{{\\an5\\pos(540,720)\\fs{size}\\fad(120,120)}}{label}")
    ev += boxed(times["PR-061a"][0], times["BR-061b"][1], "Buy 1 Get 1 Free", 300, size=84)
    t0, t1 = times["PR-062"]
    ev.append(f"Dialogue: 2,{ts(t0)},{ts(t1)},Big,,0,0,0,,{{\\an5\\pos(540,330)\\fs200\\fad(120,120)}}stryde")

    ass = HERE / "final" / f"HK{n}.ass"
    ass.parent.mkdir(exist_ok=True)
    ass.write_text(f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Liberation Sans,62,&H00000000,&H00000000,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,0,0,5,0,0,0,1
Style: Box,Liberation Sans,62,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: Banner,Liberation Sans,70,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,5,0,8,40,40,125,1
Style: Big,Liberation Sans,150,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,8,3,5,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
""" + "\n".join(ev) + "\n", encoding="utf-8")

    col = colour_plan(src, timeline)
    report = {"variant": n, "caption_groups": len(gs), "colour": col}
    if "--measure-only" in sys.argv:
        print(json.dumps(report, indent=1))
        return

    vf = [f"colorchannelmixer=rr={r}:gg={g}:bb={b}:enable='between(t,{c['start']:.3f},{c['end'] - 0.001:.3f})'"
          for c in col if "gain" in c for r, g, b in [c["gain"]]]
    vf += [f"ass={ass}", f"fade=t=out:st={master - 0.3:.3f}:d=0.3"]
    lm = loud_measure(src)
    af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={lm['input_i']}:measured_TP={lm['input_tp']}:"
          f"measured_LRA={lm['input_lra']}:measured_thresh={lm['input_thresh']}:offset={lm['target_offset']}:"
          f"linear=true,aresample=48000,afade=t=out:st={master - 0.3:.3f}:d=0.3")
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-i", str(src), "-vf", ",".join(vf), "-af", af,
                    "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", "-r", str(FPS),
                    "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-movflags", "+faststart", "-t", f"{master:.3f}",
                    str(out)], check=True)

    # checks: length, loudness, black frames outside the planned fade
    hh, mm, ss = re.search(r"Duration: (\d+):(\d+):([\d.]+)", subprocess.run(
        [FF, "-hide_banner", "-i", str(out)], capture_output=True, text=True).stderr).groups()
    dur = int(hh) * 3600 + int(mm) * 60 + float(ss)
    err = subprocess.run([FF, "-hide_banner", "-i", str(out), "-vn", "-af", "ebur128=peak=true", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    summ = err[err.rindex("Summary:"):]
    I = float(re.search(r"I:\s+(-?[\d.]+) LUFS", summ).group(1))
    TP = float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", summ).group(1))
    bd = subprocess.run([FF, "-hide_banner", "-i", str(out), "-vf", "blackdetect=d=0.1:pix_th=0.08", "-an", "-f", "null", "-"],
                        capture_output=True, text=True).stderr
    blacks = [(float(a), float(b)) for a, b in re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", bd)]
    blacks = [x for x in blacks if x[0] < master - 0.35]
    report.update({"file": str(out), "duration_s": round(dur, 2), "master_s": master,
                   "duration_ok": abs(dur - master) < 0.05, "lufs_i": I, "true_peak_dbtp": TP,
                   "loudness_ok": abs(I + 14) <= 0.5 and TP <= -1.0, "black_frames": blacks,
                   "size_bytes": out.stat().st_size})
    report["status"] = "PASS" if report["duration_ok"] and report["loudness_ok"] and not blacks else "FAIL"
    (HERE / "final" / f"finish_HK{n}.json").write_text(json.dumps(report, indent=1))
    print(json.dumps({k: v for k, v in report.items() if k != "colour"}, indent=1))


if __name__ == "__main__":
    main()
