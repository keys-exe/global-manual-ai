"""TH-HK2 frame v13 (user Fix "use the lighting effect of the 1st version", 2026-10-01): v12's layout kept pixel for pixel; its colour and light matched to v1 (neutral daylight, no pink cast) by a CIE Lab mean/std colour transfer, then a light unsharp mask for the softness the edits built up. No model call."""
import os
import numpy as np
from PIL import Image, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)) + "/"
M = np.array([[0.4124, 0.3576, 0.1805], [0.2126, 0.7152, 0.0722], [0.0193, 0.1192, 0.9505]])
WP = np.array([0.95047, 1.0, 1.08883])
def to_lab(p):
    c = np.asarray(Image.open(p).convert("RGB"), dtype=np.float64) / 255
    c = np.where(c > 0.04045, ((c + 0.055) / 1.055) ** 2.4, c / 12.92)
    xyz = c @ M.T / WP
    f = np.where(xyz > 0.008856, np.cbrt(xyz), 7.787 * xyz + 16 / 116)
    return np.stack([116 * f[..., 1] - 16, 500 * (f[..., 0] - f[..., 1]), 200 * (f[..., 1] - f[..., 2])], -1)
def to_rgb(lab):
    fy = (lab[..., 0] + 16) / 116; fx = fy + lab[..., 1] / 500; fz = fy - lab[..., 2] / 200
    f = np.stack([fx, fy, fz], -1)
    xyz = np.where(f ** 3 > 0.008856, f ** 3, (f - 16 / 116) / 7.787) * WP
    c = xyz @ np.linalg.inv(M).T
    c = np.where(c > 0.0031308, 1.055 * np.clip(c, 0, None) ** (1 / 2.4) - 0.055, 12.92 * c)
    return (np.clip(c, 0, 1) * 255 + 0.5).astype(np.uint8)
ref, tgt = to_lab(D + "TH-HK2_frame_v1.png"), to_lab(D + "TH-HK2_frame_v12.png")
out = np.empty_like(tgt)
for c in range(3):
    t, r = tgt[..., c], ref[..., c]
    out[..., c] = (t - t.mean()) / (t.std() + 1e-6) * r.std() + r.mean()
img = Image.fromarray(to_rgb(out)).filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=3))
img.save(D + "TH-HK2_frame_v13.png")
