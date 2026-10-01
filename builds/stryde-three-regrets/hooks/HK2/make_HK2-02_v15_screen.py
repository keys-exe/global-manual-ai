"""HK2-02 v15 screen: the Kie render HK2-02_v15.png (over her right shoulder, screen blank) with Eileen Ward's long letter
(ref/HK2-02_letter_ref.png, make_HK2-02_v14.py) warped onto the measured screen corners. Output HK2-02_v15s.png."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)) + "/"
base = Image.open(D + "HK2-02_v15.png").convert("RGB")
ref = Image.open(D + "ref/HK2-02_letter_ref.png").convert("RGB")
TL, TR, BR, BL = (60, 1039), (904, 892), (956, 1427), (193, 1631)
W, H = ref.size
def coeffs(dst, src):
    A, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; b += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()
warp = ref.transform(base.size, Image.PERSPECTIVE, coeffs([TL, TR, BR, BL], [(0, 0), (W, 0), (W, H), (0, H)]), resample=Image.BICUBIC)
m = Image.new("L", base.size, 0); ImageDraw.Draw(m).polygon([TL, TR, BR, BL], fill=255)
inner = m.filter(ImageFilter.MinFilter(7))
bw = np.asarray(base, float); ww = np.asarray(warp, float) / 255.0 * np.percentile(bw[np.asarray(inner) > 0], 90, axis=0)
warp = Image.fromarray(np.clip(ww, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
Image.composite(warp, base, inner.filter(ImageFilter.GaussianBlur(3))).save(D + "HK2-02_v15s.png")
