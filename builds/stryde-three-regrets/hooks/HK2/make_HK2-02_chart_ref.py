"""HK2-02 chart page (user Fix 2026-10-01: a bar chart on the laptop screen that shows "three things come up more than anything else").
Built in PIL so every word is exact: the line as the title, three tall bars (Regret No. 1–3, the EG03 cards' names) far above
six short grey bars (everything else). Output ref/HK2-02_chart_ref.png (16:10, the screen's shape)."""
import os
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LB = "/usr/share/fonts/truetype/liberation/"
def F(n, s): return ImageFont.truetype(LB + n, s)
W, H = 1640, 1000
im = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(im)
d.rectangle((0, 0, W, 64), fill="#f3f3f3"); d.line((0, 64, W, 64), fill="#dddddd", width=2)
d.text((48, 32), "Customer messages  ›  Knees", font=F("LiberationSans-Regular.ttf", 26), fill="#666", anchor="lm")
d.text((W - 48, 32), "25,312 messages", font=F("LiberationSans-Regular.ttf", 26), fill="#777", anchor="rm")
d.text((96, 130), "Three things come up more than anything else", font=F("LiberationSans-Bold.ttf", 54), fill="#111")
d.text((96, 205), "What 25,000 people wrote to us about their knees", font=F("LiberationSans-Regular.ttf", 32), fill="#666")
x0, x1, yb, yt = 140, W - 100, 850, 300
for i in range(5):
    y = yb - (yb - yt) * i / 4; d.line((x0, y, x1, y), fill="#e6e6e6", width=2)
d.line((x0, yb, x1, yb), fill="#999", width=3)
vals = [0.96, 0.88, 0.80, 0.22, 0.17, 0.14, 0.11, 0.08, 0.06]
n = len(vals); slot = (x1 - x0) / n; bw = slot * 0.62
for i, v in enumerate(vals):
    cx = x0 + slot * (i + 0.5); top = yb - (yb - yt) * v
    d.rectangle((cx - bw / 2, top, cx + bw / 2, yb), fill="#c4502a" if i < 3 else "#cfcfcf")
    if i < 3:
        d.text((cx, yb + 34), "Regret", font=F("LiberationSans-Bold.ttf", 30), fill="#222", anchor="mm")
        d.text((cx, yb + 72), f"No. {i + 1}", font=F("LiberationSans-Bold.ttf", 30), fill="#222", anchor="mm")
gx0, gx1 = x0 + slot * 3 + 10, x1 - 10
d.line((gx0, yb + 28, gx1, yb + 28), fill="#aaa", width=2)
d.text(((gx0 + gx1) / 2, yb + 62), "everything else", font=F("LiberationSans-Regular.ttf", 28), fill="#888", anchor="mm")
im.save(D + "ref/HK2-02_chart_ref.png")
