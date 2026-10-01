"""HK2-01 v9 exact screen (2026-10-01): after the v6-screen paste (make_HK2-01_v9b.py → v9c), warp the clean rebuilt page (ref/HK2-01_screen_ref.png) onto the screen's four corners so every word reads right, toned to the screen's own white and softened to match the photo. Output: HK2-01_v9d.png."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)) + "/"
base = Image.open(D + "HK2-01_v9c.png").convert("RGB")
ref = Image.open(D + "ref/HK2-01_screen_ref.png").convert("RGB")
TL, TR, BR, BL = (88, 1112), (1000, 950), (1088, 1550), (225, 1795)
W, H = ref.size
def coeffs(dst, src):
    A, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; b += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()
c = coeffs([TL, TR, BR, BL], [(0, 0), (W, 0), (W, H), (0, H)])
warp = ref.transform(base.size, Image.PERSPECTIVE, c, resample=Image.BICUBIC)
m = Image.new("L", base.size, 0); ImageDraw.Draw(m).polygon([TL, TR, BR, BL], fill=255)
inner = m.filter(ImageFilter.MinFilter(9))
bw = np.asarray(base, float); ww = np.asarray(warp, float); mi = np.asarray(inner) > 0
white_screen = np.percentile(bw[mi], 90, axis=0); ww = ww / 255.0 * white_screen
warp = Image.fromarray(np.clip(ww, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
Image.composite(warp, base, inner.filter(ImageFilter.GaussianBlur(3))).save(D + "HK2-01_v9d.png")
