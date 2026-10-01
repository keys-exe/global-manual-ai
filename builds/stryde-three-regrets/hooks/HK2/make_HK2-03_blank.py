"""HK2-03 clip start frame: the HK2-01 frame render (HK2-01_v10.png) with its screen made plain white (screen tone matched), so Kling
animates only the hand and has no screen text to redraw. Output HK2-03_blank.png."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)) + "/"
base = Image.open(D + "HK2-01_v10.png").convert("RGB")
TL, TR, BR, BL = (265, 1014), (1037, 1045), (1003, 1546), (275, 1500)
m = Image.new("L", base.size, 0); ImageDraw.Draw(m).polygon([TL, TR, BR, BL], fill=255)
inner = m.filter(ImageFilter.MinFilter(9))
bw = np.asarray(base, float); white = np.percentile(bw[np.asarray(inner) > 0], 90, axis=0)
flat = Image.new("RGB", base.size, tuple(int(v) for v in white))
Image.composite(flat, base, inner.filter(ImageFilter.GaussianBlur(3))).save(D + "HK2-03_blank.png")
