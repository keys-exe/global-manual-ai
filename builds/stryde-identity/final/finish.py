#!/usr/bin/env python3
"""Final finish for the three STRYDE ads: the rough cut from assemble.py (PASS) + captions + the post overlays the
build sheet names (§17: numbers are post overlays, never generated; EG04 offer card). Master audio copied untouched.

v2 (user, 2026-09-28: "add captions use the safe zone and for the other caption … make it more appealing to an ads"):
- Captions: the body's spoken words (vo/master/<HK>.words.json, verbatim), up to 3 words a chunk, the word being said
  in yellow, Montserrat Black with a heavy outline. The hook keeps its own caption (make_hooks.py), so captions start
  at the body. Placed in the 9:16 safe zone: bottom of text at y 1280 (clear of the bottom ~420 px of app UI),
  shifted left of the right-hand button column (margins L 150 / R 190).
- Overlays in the top safe band (below y 300): stat number pops in (Anton, yellow), label on a dark rounded pill;
  offer card = yellow pill "Buy 1 Get 1 Free" with a pulse + dark pill with a green check "60-DAY MONEY-BACK
  GUARANTEE", from BR-22 to the end. Overlays: 17x on MECH-01 · 34% on BR-09 · 200,000+ on BR-21.
EG04 in the reference also has a URL box — no URL is on file for STRYDE, so it is left out (flagged)."""
import difflib, json, re, subprocess, sys
from pathlib import Path
import imageio_ffmpeg
from PIL import ImageFont

FF = imageio_ffmpeg.get_ffmpeg_exe()
B = Path(__file__).resolve().parent
FONTS = B / "fonts"
W, H = 1080, 1920
YEL, WHITE, BLACK = "&H0000D4FF&", "&H00FFFFFF&", "&H00000000&"
PILL = "&H1A111111&"          # near-black, slightly see-through
GREEN = "&H005EC522&"


def t(x):
    x = max(0.0, x)
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def text_w(font, size, text, spacing=0):
    """Width in px as libass draws it: libass sizes a font so ascent+descent = the ASS size."""
    f = ImageFont.truetype(str(FONTS / font), 100)
    a, d = f.getmetrics()
    f = ImageFont.truetype(str(FONTS / font), round(size * 100 / (a + d)))
    return f.getlength(text) + spacing * len(text)


def rrect(w, h, r):
    w, h, r = round(w), round(h), round(r)
    return (f"m {r} 0 l {w-r} 0 b {w} 0 {w} 0 {w} {r} l {w} {h-r} b {w} {h} {w} {h} {w-r} {h} "
            f"l {r} {h} b 0 {h} 0 {h} 0 {h-r} l 0 {r} b 0 0 0 0 {r} 0")


HEAD = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Montserrat Black,76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H99000000,0,0,0,0,100,100,1,0,1,8,4,2,150,190,640,1
Style: Hook,Montserrat Black,84,&H00FFFFFF,&H00FFFFFF,&H00000000,&H99000000,0,0,0,0,100,100,1,0,1,9,4,5,110,110,0,1
Style: Num,Anton,230,&H0000D4FF,&H0000D4FF,&H00000000,&H99000000,0,0,0,0,100,100,2,0,1,9,6,5,0,0,0,1
Style: Lbl,Montserrat Black,54,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,3,0,1,0,0,5,0,0,0,1
Style: Box,Montserrat Black,10,&H00FFFFFF,&H00FFFFFF,&H00000000,&H99000000,0,0,0,0,100,100,0,0,1,0,5,5,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def ev(layer, style, a, b, text):
    return f"Dialogue: {layer},{t(a)},{t(b)},{style},,0,0,0,,{text}\n"


def pill(layer, a, b, cx, cy, w, h, colour, extra=""):
    return ev(layer, "Box", a, b, f"{{\\an5\\pos({cx},{cy})\\c{colour}\\bord0{extra}\\p1}}{rrect(w, h, h / 2)}{{\\p0}}")


def stat(a, b, num, label):
    s = ev(3, "Num", a, b, f"{{\\an5\\pos({W//2},470)\\fad(0,150)\\fscx30\\fscy30\\t(0,170,\\fscx114\\fscy114)"
                           f"\\t(170,280,\\fscx100\\fscy100)}}{num}")
    lw = text_w("Montserrat-Black.ttf", 54, label, 3) + 90
    a2 = a + 0.18
    s += pill(1, a2, b, W // 2, 660, lw, 96, PILL, "\\fad(150,150)")
    s += ev(2, "Lbl", a2, b, f"{{\\an5\\pos({W//2},662)\\fad(150,150)}}{label}")
    return s


def offer(a, b):
    s = ""
    top = "Buy 1 Get 1 Free"
    w1 = text_w("Montserrat-Black.ttf", 80, top, 1) + 110
    pulse = "".join(f"\\t({k},{k+300},\\fscx106\\fscy106)\\t({k+300},{k+600},\\fscx100\\fscy100)"
                    for k in range(900, int((b - a) * 1000) - 600, 1800))
    pop = "\\fscx40\\fscy40\\t(0,180,\\fscx108\\fscy108)\\t(180,280,\\fscx100\\fscy100)"
    s += pill(1, a, b, W // 2, 470, w1, 136, YEL, "\\fad(0,200)" + pop + pulse)
    s += ev(2, "Lbl", a, b, f"{{\\an5\\pos({W//2},473)\\fs80\\fsp1\\c{BLACK}\\fad(0,200){pop}{pulse}}}{top}")
    low = "60-DAY MONEY-BACK GUARANTEE"
    tw = text_w("Montserrat-Black.ttf", 44, low, 2)
    w2 = tw + 70 + 80
    a2 = a + 0.25
    s += pill(1, a2, b, W // 2, 630, w2, 90, PILL, "\\fad(180,200)")
    x0 = W // 2 - w2 / 2 + 40            # check disc at the pill's left, text to its right
    s += ev(2, "Box", a2, b, f"{{\\an5\\pos({x0+22:.0f},630)\\c{GREEN}\\bord0\\shad0\\fad(180,200)\\p1}}"
                             f"{rrect(46, 46, 23)}{{\\p0}}")
    s += ev(3, "Box", a2, b, f"{{\\an7\\pos({x0+10:.0f},618)\\c{WHITE}\\bord0\\shad0\\fad(180,200)\\p1}}"
                             f"m 3 12 l 9 18 l 22 4 l 25 7 l 9 24 l 0 15{{\\p0}}")
    s += ev(2, "Lbl", a2, b, f"{{\\an4\\pos({x0+62:.0f},632)\\fs44\\fsp2\\fad(180,200)}}{low}")
    return s


def norm(w):
    return re.sub(r"[^a-z0-9]", "", w.lower())


def script_words(hk, words):
    """The script's own words (verbatim, §22U) timed from the transcript: exact matches are anchors, the words
    between two anchors share that span by length (numerals vs spelled numbers, split compounds)."""
    lines = (B.parent / f"vo/master/{hk}+BODY.lines.txt").read_text().split("\n")
    toks = [(i, w) for i, l in enumerate(lines) for w in l.strip().strip('"“”').split()]
    S = [norm(w) for _, w in toks]; T = [norm(w["w"]) for w in words]
    sm = difflib.SequenceMatcher(None, S, T, autojunk=False)
    tm = [None] * len(S)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            tm[blk.a + k] = (words[blk.b + k]["s"], words[blk.b + k]["e"])
    tb = [None] * len(S)                      # transcript index per anchored script word
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            tb[blk.a + k] = blk.b + k
    i = 0
    while i < len(S):
        if tm[i]:
            i += 1; continue
        j = i
        while j < len(S) and not tm[j]:
            j += 1
        pb = tb[i - 1] if i else -1; nb = tb[j] if j < len(S) else len(words)
        span = words[pb + 1:nb]
        a = span[0]["s"] if span else (words[pb]["e"] if pb >= 0 else 0.0)
        e = span[-1]["e"] if span else (words[nb]["s"] if nb < len(words) else words[-1]["e"])
        L = [len(S[k]) + 1 for k in range(i, j)]; tot = sum(L); x = a
        for k, l in zip(range(i, j), L):
            d = (e - a) * l / tot; tm[k] = (x, x + d); x += d
        i = j
    return [{"w": w, "s": tm[k][0], "e": tm[k][1], "line": ln} for k, (ln, w) in enumerate(toks)]


def clean(w):
    w = w.strip().strip('"“”')
    w = re.sub(r"[.,;:]+$", "", w)
    return w.upper()


def chunk(ws):
    chunks, cur = [], []
    for w in ws:
        c = clean(w["w"])
        if not c:
            continue
        if cur and (len(cur) == 3 or sum(len(x[0]) + 1 for x in cur) + len(c) > 17 or w["line"] != cur[-1][1]["line"]
                    or re.search(r"[.,;:?!]$", cur[-1][1]["w"]) or w["s"] - cur[-1][1]["e"] > 0.35):
            chunks.append(cur); cur = []
        cur.append((c, w))
    if cur:
        chunks.append(cur)
    out = []                                  # no orphan word: a lone word joins the chunk before it on its line
    for ch in chunks:
        p = out[-1] if out else None
        if (len(ch) == 1 and p and p[-1][1]["line"] == ch[0][1]["line"] and not re.search(r"[.,;:?!]$", p[-1][1]["w"])
                and sum(len(x[0]) + 1 for x in p) + len(ch[0][0]) <= 20 and ch[0][1]["s"] - p[-1][1]["e"] <= 0.35):
            p.extend(ch)
        else:
            out.append(ch)
    return out


def captions(ws, a0, a1, style, pos=""):
    chunks = chunk([w for w in ws if a0 - 0.05 <= w["s"] < a1])
    s = ""
    for i, ch in enumerate(chunks):
        c_end = min(chunks[i + 1][0][1]["s"] if i + 1 < len(chunks) else a1, ch[-1][1]["e"] + 0.4, a1)
        for j, (c, w) in enumerate(ch):
            a = max(w["s"] if j else ch[0][1]["s"], a0)
            b = ch[j + 1][1]["s"] if j + 1 < len(ch) else c_end
            if b - a < 0.02:
                continue
            parts = [(f"{{\\c{YEL}}}{x}{{\\c{WHITE}}}" if k == j else x) for k, (x, _) in enumerate(ch)]
            pop = "\\fscx86\\fscy86\\t(0,90,\\fscx100\\fscy100)" if j == 0 else ""
            s += ev(5, style, a, b, "{" + pos + pop + "}" + " ".join(parts))
    return s


ONLY = sys.argv[1:] and sys.argv[1].split(",")   # optional: finish.py HK1 [t1,t2,… stills only]
STILLS = sys.argv[2:] and [float(x) for x in sys.argv[2].split(",")]
for hk in ONLY or ["HK1", "HK2", "HK3"]:
    run = json.loads((B / f"edit/run_{hk}.json").read_text())
    edl = {e["beat"]: e for e in run["edl"]}
    total = run["master_s"]
    words = script_words(hk, json.loads((B.parent / f"vo/master/{hk}.words.json").read_text()))
    s = HEAD
    hook_end = edl[f"EDIT-{hk}"]["end"]
    s += captions(words, 0.0, hook_end, "Hook", f"\\an5\\pos({W//2},{H//2})")   # on the split seam (VN01–03)
    s += captions(words, hook_end, total, "Cap")
    e = edl["MECH-01"]; s += stat(e["start"] + 0.25, e["end"], "17X", "YOUR BODYWEIGHT")
    e = edl["BR-09"]; s += stat(e["start"] + 0.2, e["end"], "34%", "LESS STRAIN")
    e = edl["BR-21"]; s += stat(e["start"] + 0.2, e["end"], "200,000+", "PEOPLE WEAR ONE")
    s += offer(edl["BR-22"]["start"], total)
    ass = B / f"edit/overlays_{hk}.ass"; ass.write_text(s)
    if STILLS:
        for x in STILLS:
            subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", "-ss", f"{x}", "-copyts", "-i",
                            str(B / f"edit/rough_{hk}.mp4"), "-vf", f"subtitles='{ass}':fontsdir={FONTS},scale=540:-2",
                            "-frames:v", "1", str(B / f"edit/still_{hk}_{x}.jpg")], check=True)
        continue
    out = B / f"STRYDE_Identity_{hk}_final.mp4"
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", "-i", str(B / f"edit/rough_{hk}.mp4"),
                    "-vf", f"subtitles='{ass}':fontsdir={FONTS}",
                    "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-pix_fmt", "yuv420p", "-r", "24",
                    "-c:a", "copy", "-movflags", "+faststart", str(out)], check=True)
    print(hk, out.name, f"{total:.2f}s")
