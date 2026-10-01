"""HK2-02 v13 (user Fix 2026-10-01: "add word under the bar chart but not readable") on v12 ("use HK2-01 as reference, don't show any letter at the laptop screen, just the bar chart will do").
v13: a short two-line label under every bar, drawn then blurred so it reads as words but cannot be read.
The HK2-01 frame (Kie render HK2-01_v10.png: over her left shoulder, laptop, closed stryde box) with the letter swapped for a bar chart
with no words at all — three tall orange bars far above six short grey ones — warped onto the same screen corners as HK2-01 v11.
No model call (0 credits). Output HK2-02_v13.png; chart page ref/HK2-02_chart_v13.png."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
D = os.path.dirname(os.path.abspath(__file__)) + "/"
W, H = 1640, 1000
ch = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(ch)
x0, x1, yb, yt = 120, W - 120, 790, 120
for i in range(5):
    y = yb - (yb - yt) * i / 4; d.line((x0, y, x1, y), fill="#e6e6e6", width=3)
d.line((x0, yb, x1, yb), fill="#999", width=4)
vals = [0.96, 0.88, 0.80, 0.22, 0.17, 0.14, 0.11, 0.08, 0.06]
slot = (x1 - x0) / len(vals); bw = slot * 0.62
for i, v in enumerate(vals):
    cx = x0 + slot * (i + 0.5); top = yb - (yb - yt) * v
    d.rectangle((cx - bw / 2, top, cx + bw / 2, yb), fill="#c4502a" if i < 3 else "#cfcfcf")
LB = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
lab = Image.new("RGB", (W, H - yb - 6), "white"); dl = ImageDraw.Draw(lab)
words = [("Wrong", "supports"), ("The good", "leg"), ("Saying", "no"), ("Sizing", "query"), ("Delivery", "times"),
         ("Returns", "policy"), ("Washing", "the strap"), ("Gift", "orders"), ("Other", "topics")]
for i, (a, b) in enumerate(words):
    cx = x0 + slot * (i + 0.5)
    dl.text((cx, 40), a, font=ImageFont.truetype(LB, 34), fill="#444" if i < 3 else "#888", anchor="mm")
    dl.text((cx, 82), b, font=ImageFont.truetype(LB, 34), fill="#444" if i < 3 else "#888", anchor="mm")
ch.paste(lab.filter(ImageFilter.GaussianBlur(13)), (0, yb + 6))
ch.save(D + "ref/HK2-02_chart_v13.png")
base = Image.open(D + "HK2-01_v10.png").convert("RGB")
TL, TR, BR, BL = (265, 1014), (1037, 1045), (1003, 1546), (275, 1500)
def coeffs(dst, src):
    A, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; b += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()
c = coeffs([TL, TR, BR, BL], [(0, 0), (W, 0), (W, H), (0, H)])
warp = ch.transform(base.size, Image.PERSPECTIVE, c, resample=Image.BICUBIC)
m = Image.new("L", base.size, 0); ImageDraw.Draw(m).polygon([TL, TR, BR, BL], fill=255)
inner = m.filter(ImageFilter.MinFilter(9))
bw_ = np.asarray(base, float); ww = np.asarray(warp, float); mi = np.asarray(inner) > 0
ww = ww / 255.0 * np.percentile(bw_[mi], 90, axis=0)
warp = Image.fromarray(np.clip(ww, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
Image.composite(warp, base, inner.filter(ImageFilter.GaussianBlur(3))).save(D + "HK2-02_v13.png")
