"""HK2-03 v6 (user Fix 2026-10-01: "use HK2-01 as reference, show a lots of message in google"). The HK2-01 frame (Kie render
HK2-01_v10.png: over her left shoulder, laptop, closed stryde box) with a mail inbox on the screen — a web-mail list in the familiar
layout (search bar, left rail, one row per message: sender, subject, a line of preview, date), no brand logo or product name — full of
customer messages about their knees. Built in PIL (ref/HK2-03_inbox.png) and warped on as HK2-01 v11. 0 credits. Output HK2-03_v6.png."""
import os, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LB = "/usr/share/fonts/truetype/liberation/"
def F(n, s): return ImageFont.truetype(LB + n, s)
W, H = 1640, 1000
im = Image.new("RGB", (W, H), "#f6f8fc"); d = ImageDraw.Draw(im)
d.rounded_rectangle((300, 18, 1180, 74), 28, fill="#e9eef6"); d.text((360, 46), "Search mail", font=F("LiberationSans-Regular.ttf", 26), fill="#5f6368", anchor="lm")
d.rounded_rectangle((24, 100, 250, 160), 18, fill="#c2e7ff"); d.text((60, 130), "Compose", font=F("LiberationSans-Bold.ttf", 24), fill="#001d35", anchor="lm")
rail = [("Inbox", "25,312", True), ("Starred", "", False), ("Snoozed", "", False), ("Sent", "", False), ("Drafts", "", False)]
for k, (t, c, on) in enumerate(rail):
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
        ("Eileen Ward", "Both knees now", "I started with one knee as you suggested and now I wear it on both")]
dates = ["10:42", "09:17", "08:55", "08:03", "Yesterday", "Yesterday", "30 Sept", "30 Sept", "29 Sept", "29 Sept", "28 Sept", "28 Sept", "27 Sept", "27 Sept", "26 Sept", "26 Sept"]
y = 160
for k, (s, sub, pre) in enumerate(rows):
    unread = k % 3 != 2
    d.rectangle((285, y, W - 16, y + 52), fill="white" if unread else "#f2f6fc"); d.line((285, y + 52, W - 16, y + 52), fill="#eceff1", width=1)
    d.rectangle((318, y + 17, 336, y + 35), outline="#9aa0a6", width=2)
    fb, fr = F("LiberationSans-Bold.ttf", 22), F("LiberationSans-Regular.ttf", 22)
    d.text((370, y + 26), s, font=fb if unread else fr, fill="#202124", anchor="lm")
    x = 640; d.text((x, y + 26), sub, font=fb if unread else fr, fill="#202124", anchor="lm")
    x += d.textlength(sub, font=fb if unread else fr) + 8
    t = "– " + pre
    while d.textlength(t, font=fr) > W - 175 - x: t = t[:-1]
    d.text((x, y + 26), t.rstrip(), font=fr, fill="#5f6368", anchor="lm")
    d.rectangle((W - 150, y + 2, W - 16, y + 50), fill="white" if unread else "#f2f6fc")
    d.text((W - 36, y + 26), dates[k], font=fb if unread else fr, fill="#202124", anchor="rm")
    y += 52
im.save(D + "ref/HK2-03_inbox.png")
base = Image.open(D + "HK2-01_v10.png").convert("RGB")
TL, TR, BR, BL = (265, 1014), (1037, 1045), (1003, 1546), (275, 1500)
def coeffs(dst, src):
    A, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; b += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()
warp = im.transform(base.size, Image.PERSPECTIVE, coeffs([TL, TR, BR, BL], [(0, 0), (W, 0), (W, H), (0, H)]), resample=Image.BICUBIC)
m = Image.new("L", base.size, 0); ImageDraw.Draw(m).polygon([TL, TR, BR, BL], fill=255)
inner = m.filter(ImageFilter.MinFilter(9))
bw = np.asarray(base, float); ww = np.asarray(warp, float) / 255.0 * np.percentile(bw[np.asarray(inner) > 0], 90, axis=0)
warp = Image.fromarray(np.clip(ww, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
Image.composite(warp, base, inner.filter(ImageFilter.GaussianBlur(3))).save(D + "HK2-03_v6.png")
