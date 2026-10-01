"""HK2-01 v9 screen restore (2026-10-01): the v9 render (job 67a7b04e — our closed box beside the laptop) redrew the review page and garbled its text, so v6's screen is pasted back: v6 aligned to v9 by a fitted similarity (scale 1.01 about (600,1350), shift +16 px down, -2 px left; mean residual 4.45/255 over the laptop) and composited inside the screen's quad with a soft edge. Output: HK2-01_v9c.png."""
import os
from PIL import Image, ImageDraw, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)) + "/"
v6 = Image.open(D + "HK2-01_v6.png").convert("RGB"); v9 = Image.open(D + "HK2-01_v9.png").convert("RGB")
s, dy, dx, cx, cy = 1.01, 16, -2, 600, 1350
a = 1 / s
v6a = v6.transform(v6.size, Image.AFFINE, (a, 0, cx - a * (cx + dx), 0, a, cy - a * (cy + dy)), resample=Image.BICUBIC)
k = 1536 / 1116
quad = [(70, 805), (735, 690), (795, 1145), (110, 1290)]
m = Image.new("L", v9.size, 0)
ImageDraw.Draw(m).polygon([(x * k, y * k) for x, y in quad], fill=255)
m = m.filter(ImageFilter.GaussianBlur(4))
Image.composite(v6a, v9, m).save(D + "HK2-01_v9c.png")
