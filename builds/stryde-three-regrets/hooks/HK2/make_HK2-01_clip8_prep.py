"""HK2-01 clip v8 prep (user "make clip for HK2-01", 2026-10-01, image v12 = the user's own image, HK2-01_v12_user.webp). As LESSONS L09:
(1) the user's screen is lifted off flat (inverse perspective) as ref/HK2-01_v12_page.png — their page kept exactly as they made it;
(2) the start frame for Kling = their image with the screen whitened (HK2-01_v12_blank.png), so Kling animates only the hand.
Screen corners measured on their image (1116×2000)."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)) + "/"
im = Image.open(D + "HK2-01_v12_user.webp").convert("RGB")
TL, TR, BR, BL = (66.4, 812), (726.3, 693.3), (789.1, 1120.4), (164.7, 1303.3)
W, H = 1600, 1000
def coeffs(dst, src):
    A, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; b += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()
page = im.transform((W, H), Image.PERSPECTIVE, coeffs([(0, 0), (W, 0), (W, H), (0, H)], [TL, TR, BR, BL]), resample=Image.BICUBIC)
pa = np.asarray(page, float); white = np.percentile(pa.reshape(-1, 3), 95, axis=0)
page = Image.fromarray(np.clip(pa / white * 255, 0, 255).astype(np.uint8))       # normalise to a white page
page.save(D + "ref/HK2-01_v12_page.png")
m = Image.new("L", im.size, 0); ImageDraw.Draw(m).polygon([TL, TR, BR, BL], fill=255)
inner = m.filter(ImageFilter.MinFilter(5))
flat = Image.new("RGB", im.size, tuple(int(v) for v in white))
Image.composite(flat, im, inner.filter(ImageFilter.GaussianBlur(2))).save(D + "HK2-01_v12_blank.png")
print(white)
