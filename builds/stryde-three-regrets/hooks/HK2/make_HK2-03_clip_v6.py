"""HK2-03 clip v6 (user "make clip for HK2-03", 2026-10-01, from confirmed image v6): Kling gen 6 (HK2-03_kling_g6.mp4 — locked camera,
her fingers slide up the trackpad, screen blank) + the inbox put back on the screen frame by frame (as BR-057 clip v5). The search bar,
left rail and "1–50 of 25,312" stay fixed; the message list scrolls up in step with the hand's measured travel, through more and more
messages (32 rows, the first 16 as image v6). Corners measured on Kling frame 1; per-frame drift from the white-screen centroid; light sway."""
import os, subprocess, math, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
D = os.path.dirname(os.path.abspath(__file__)) + "/"
FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
LB = "/usr/share/fonts/truetype/liberation/"
def F(n, s): return ImageFont.truetype(LB + n, s)
W, H = 1640, 1000
page = Image.new("RGB", (W, H), "#f6f8fc"); d = ImageDraw.Draw(page)
d.rounded_rectangle((300, 18, 1180, 74), 28, fill="#e9eef6"); d.text((360, 46), "Search mail", font=F("LiberationSans-Regular.ttf", 26), fill="#5f6368", anchor="lm")
d.rounded_rectangle((24, 100, 250, 160), 18, fill="#c2e7ff"); d.text((60, 130), "Compose", font=F("LiberationSans-Bold.ttf", 24), fill="#001d35", anchor="lm")
for k, (t, c, on) in enumerate([("Inbox", "25,312", True), ("Starred", "", False), ("Snoozed", "", False), ("Sent", "", False), ("Drafts", "", False)]):
    y = 200 + k * 52
    if on: d.rounded_rectangle((10, y - 22, 270, y + 22), 22, fill="#d3e3fd")
    d.text((60, y), t, font=F("LiberationSans-Bold.ttf" if on else "LiberationSans-Regular.ttf", 24), fill="#202124", anchor="lm")
    if c: d.text((255, y), c, font=F("LiberationSans-Bold.ttf", 22), fill="#202124", anchor="rm")
d.rounded_rectangle((285, 92, W - 16, H + 20), 20, fill="white")
d.text((320, 122), "1–50 of 25,312", font=F("LiberationSans-Regular.ttf", 20), fill="#5f6368", anchor="lm")
rows = [("Margaret Hale", "My knees, and what I wish I had known", "I am writing to thank you, and to tell you something I think other people"),
        ("Patricia Doyle", "A long letter, but I wanted you to have it", "I have been meaning to write this for a month, and it has turned into"),
        ("Gail Thornton", "The drawer full of braces", "Four years of sleeves and wraps and none of them changed how the stairs"),
        ("Ken Ashworth", "About my good leg", "I didn't notice I was leaning on it until my other knee started"),
        ("Joan Pritchard", "I kept saying no", "No to the walk with my sister, no to the grandchildren's day out"),
        ("Brian Collins", "Stairs again, finally", "Came down my own stairs this morning one at a time with a cup of tea"),
        ("Linda Marsh", "Wish I'd known sooner", "Six weeks in and I want to tell you what happened at the bus stop"),
        ("Susan Reed", "Thank you from Leeds", "My daughter ordered it for me and I was not hopeful, I'll be honest"),
        ("David Price", "Knees and the allotment", "Back on my knees at the allotment for the first time in two summers"),
        ("Carol Jennings", "Not what I expected", "I thought it would be another sleeve for the drawer. It wasn't"),
        ("Alan Fletcher", "Four years too late", "If somebody had told me this four years ago I would have saved"),
        ("Maureen Kelly", "The church steps", "There are eleven steps up to our church and I counted every one"),
        ("Peter Walsh", "Walked to the post office", "Yesterday I walked to the post office and back without stopping"),
        ("Janet Hughes", "For your team", "Please pass this on to whoever reads these, it matters to me that"),
        ("Robert Hall", "My wife made me write", "She says I've stopped complaining about my knee, so here I am"),
        ("Eileen Ward", "Both knees now", "I started with one knee as you suggested and now I wear it on both"),
        ("Graham Turner", "The bus stop", "I used to stand with all my weight on one side and never noticed"),
        ("Pauline Brooks", "Dancing at my niece's wedding", "Only two songs, but two more than I'd managed in five years"),
        ("Stephen Lloyd", "Golf, believe it or not", "Eighteen holes on Saturday and I could still get out of the car"),
        ("Barbara Moore", "Too many sleeves", "I counted them the other day. Eleven. Eleven sleeves in a drawer"),
        ("Keith Morgan", "Thank you", "Just a short note to say the stairs at the station are no longer"),
        ("Sheila Bennett", "My grandson asked", "He asked why I don't go to the park with him any more. Now I do"),
        ("Trevor Hughes", "Wrong knee all along", "Turns out my good knee was doing all the work and paying for it"),
        ("Diane Foster", "The walk to the shops", "Twenty minutes each way, and I used to take the car for it"),
        ("Colin Shaw", "Should have listened", "My physio said the same thing two years ago and I didn't believe"),
        ("Valerie King", "Saying yes again", "I've said yes to three things this month I would have refused"),
        ("Roy Atkinson", "From a sceptic", "I'll admit I bought it expecting to send it back. I haven't"),
        ("Hilary Grant", "My knees, my regret", "The regret isn't the money I spent. It's the years I said no"),
        ("Norman Webb", "Back on the bike", "Only round the village, but the first time since my sixties"),
        ("Gillian Rose", "Thank you from Cardiff", "I wanted you to know it arrived on a Tuesday and by Friday"),
        ("Derek Hammond", "Downstairs, forwards", "For the first time in four years I came downstairs facing forwards"),
        ("Irene Clarke", "Please tell others", "If you can share this with anyone who has a drawer like mine")]
dates = ["10:42", "09:17", "08:55", "08:03", "Yesterday", "Yesterday", "30 Sept", "30 Sept", "29 Sept", "29 Sept", "28 Sept", "28 Sept", "27 Sept", "27 Sept", "26 Sept", "26 Sept",
         "25 Sept", "25 Sept", "24 Sept", "24 Sept", "23 Sept", "23 Sept", "22 Sept", "22 Sept", "21 Sept", "21 Sept", "20 Sept", "20 Sept", "19 Sept", "19 Sept", "18 Sept", "18 Sept"]
LX0, LY0 = 285, 150; RH = 52
lst = Image.new("RGB", (W - 16 - LX0, RH * len(rows) + 10), "white"); dl = ImageDraw.Draw(lst)
fb, fr = F("LiberationSans-Bold.ttf", 22), F("LiberationSans-Regular.ttf", 22)
for k, (s, sub, pre) in enumerate(rows):
    y = 10 + k * RH; unread = k % 3 != 2; bg = "white" if unread else "#f2f6fc"; f = fb if unread else fr
    dl.rectangle((0, y, lst.width, y + RH), fill=bg); dl.line((0, y + RH, lst.width, y + RH), fill="#eceff1", width=1)
    dl.rectangle((33, y + 17, 51, y + 35), outline="#9aa0a6", width=2)
    dl.text((85, y + 26), s, font=f, fill="#202124", anchor="lm")
    x = 355; dl.text((x, y + 26), sub, font=f, fill="#202124", anchor="lm"); x += dl.textlength(sub, font=f) + 8
    t = "– " + pre
    while dl.textlength(t, font=fr) > (W - 175 - LX0) - x: t = t[:-1]
    dl.text((x, y + 26), t.rstrip(), font=fr, fill="#5f6368", anchor="lm")
    dl.text((lst.width - 20, y + 26), dates[k], font=f, fill="#202124", anchor="rm")
VIEW = H - LY0; SCROLL = 7 * RH                      # about seven messages pass over the clip
def screen_at(off):
    p = page.copy(); p.paste(lst.crop((0, round(off), lst.width, round(off) + VIEW)), (LX0, LY0)); return p
tmp = tempfile.mkdtemp()
subprocess.run([FF, "-v", "error", "-y", "-i", D + "HK2-03_kling_g6.mp4", tmp + "/f%03d.png"], check=True)
frames = sorted(f for f in os.listdir(tmp) if f.endswith(".png"))
imgs = [Image.open(f"{tmp}/{f}").convert("RGB") for f in frames]; arrs = [np.asarray(im).astype(int) for im in imgs]
C0 = [(185, 710), (722, 735), (699, 1084), (193, 1046)]
def coeffs(dst, src):
    A, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; b += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()
def sc(a):
    m = a.mean(2)[650:1150, 150:780] > 225; ys, xs = np.where(m); return xs.mean(), ys.mean()
def hand(a):
    h = a[1150:1500, 300:750]; r, g, b = h[..., 0], h[..., 1], h[..., 2]
    ys, _ = np.where((r > 150) & (g > 110) & (b > 90) & (r - b > 25) & (r - b < 90)); return ys.mean()
s0 = [sc(a) for a in arrs]; hy = np.array([hand(a) for a in arrs])
hy = np.convolve(np.pad(hy, 4, mode="edge"), np.ones(9) / 9, mode="valid")
travel = np.maximum.accumulate(hy[0] - hy); travel = travel / max(travel[-1], 1e-6)
w0, h0 = imgs[0].size; out = D + "HK2-03_clip_v6.mp4"
p = subprocess.Popen([FF, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w0}x{h0}", "-r", "24", "-i", "-",
                      "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "slow", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
for i, base in enumerate(imgs):
    dx, dy = s0[i][0] - s0[0][0], s0[i][1] - s0[0][1]; C = [(x + dx, y + dy) for x, y in C0]
    scr = screen_at(SCROLL * travel[i])
    m = Image.new("L", base.size, 0); ImageDraw.Draw(m).polygon(C, fill=255)
    inner = m.filter(ImageFilter.MinFilter(5)); soft = inner.filter(ImageFilter.GaussianBlur(2))
    white = np.percentile(arrs[i][np.asarray(inner) > 0], 90, axis=0)
    a = np.asarray(scr, float) / 255.0 * white
    warp = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).transform(base.size, Image.PERSPECTIVE, coeffs(C, [(0, 0), (W, 0), (W, H), (0, H)]), resample=Image.BICUBIC).filter(ImageFilter.GaussianBlur(0.5))
    fr_ = Image.composite(warp, base, soft); s = i / 24
    sx = 2.8 * math.sin(2 * math.pi * 0.31 * s) + 1.0 * math.sin(2 * math.pi * 0.83 * s + 1.0)
    sy = 2.1 * math.sin(2 * math.pi * 0.27 * s + 0.5) + 0.8 * math.sin(2 * math.pi * 0.71 * s)
    fr_ = fr_.rotate(0.12 * math.sin(2 * math.pi * 0.23 * s), resample=Image.BICUBIC, center=(w0 / 2, h0 / 2), translate=(sx, sy))
    z = 1.03; cw, ch = w0 / z, h0 / z; x0, y0 = (w0 - cw) / 2, (h0 - ch) / 2
    p.stdin.write(fr_.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch))).resize((w0, h0), Image.LANCZOS).tobytes())
p.stdin.close(); p.wait(); print(out, len(imgs), [round(t, 2) for t in travel[::12]])
