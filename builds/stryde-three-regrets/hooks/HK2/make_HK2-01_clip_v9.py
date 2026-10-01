"""HK2-01 clip v9 (user Fix on clip v8, 2026-10-01: "make it a fast scroll in the laptop. Texts should look like reviews/post purchase survey,
so they're short paragraphs"). Kling gen 9 (HK2-01_kling_g9.mp4 — locked camera, two quick finger flicks on the trackpad, screen blank) + the
tall page (ref/HK2-01_reviews_tall.png: the user's own page on top, then short reviews and post-purchase survey answers) put back on the
screen frame by frame. LESSONS L09: the scroll is driven by the hand — each flick (found from the hand's frame-to-frame motion, frames 19-21
and 61-62) sends the list racing up, then it coasts to a stop (trackpad momentum)."""
import os, subprocess, math, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)) + "/"
FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
tmp = tempfile.mkdtemp()
subprocess.run([FF, "-v", "error", "-y", "-i", D + "HK2-01_kling_g9.mp4", tmp + "/f%03d.png"], check=True)
frames = sorted(f for f in os.listdir(tmp) if f.endswith(".png"))
imgs = [Image.open(f"{tmp}/{f}").convert("RGB") for f in frames]; arrs = [np.asarray(im).astype(int) for im in imgs]
page = Image.open(D + "ref/HK2-01_reviews_tall.png").convert("RGB")
TW, TH = page.size; W, H = 1600, 1000; HEAD = 0
tall = page
C0 = [(64.0, 782.8), (700.2, 668.4), (760.7, 1080.1), (158.8, 1256.4)]
def coeffs(dst, src):
    A, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; b += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()
def sc(a):
    m = a.mean(2)[700:1200, 120:680] > 228; ys, xs = np.where(m); return xs.mean(), ys.mean()
gray = [a.mean(2) for a in arrs]
y0, y1, x0, x1 = 1310, 1450, 670, 900; T = gray[0][y0:y1, x0:x1]; T = T - T.mean()
dys, prev = [], (0, 0)
for f in gray:
    best = None
    for dy in range(prev[0] - 6, prev[0] + 4):
        for dx in range(prev[1] - 6, prev[1] + 7, 2):
            P = f[y0 + dy:y1 + dy, x0 + dx:x1 + dx]; P = P - P.mean(); s = ((P - T) ** 2).mean()
            if best is None or s < best[0]: best = (s, dy, dx)
    prev = (best[1], best[2]); dys.append(-best[1])
up = np.convolve(np.pad(np.array(dys, float), 6, mode="edge"), np.ones(13) / 13, mode="valid")
E = [0.0] + [float(np.abs(gray[k][1150:1550, 550:1000] - gray[k - 1][1150:1550, 550:1000]).mean()) for k in range(1, len(gray))]
peaks = [k for k in range(2, len(E) - 1) if E[k] > 9 and E[k] >= E[k - 1] and E[k] >= E[k + 1]]
starts = []
for k in peaks:
    k0 = k
    while k0 > 1 and E[k0 - 1] > 6: k0 -= 1
    if not starts or k0 - starts[-1] > 8: starts.append(k0)
TAU, DIST = 0.33 * 24, 1750.0                       # coast time constant (frames) and page px per flick
v = np.zeros(len(gray))
for k0 in starts:
    for k in range(k0, len(gray)): v[k] += (DIST / TAU) * np.exp(-(k - k0) / TAU)
offs = np.cumsum(v); offs = np.minimum(offs, TH - H - 2)
print("flicks at frames", [k + 1 for k in starts], "end offset", round(offs[-1]))
s0 = [sc(a) for a in arrs]; w0, h0 = imgs[0].size; out = D + "HK2-01_clip_v9.mp4"
p = subprocess.Popen([FF, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w0}x{h0}", "-r", "24", "-i", "-",
                      "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "slow", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
for i, base in enumerate(imgs):
    dx, dy = s0[i][0] - s0[0][0], s0[i][1] - s0[0][1]; C = [(x + dx, y + dy) for x, y in C0]
    off = offs[i]
    scr = tall.crop((0, round(off), W, round(off) + H))
    m = Image.new("L", base.size, 0); ImageDraw.Draw(m).polygon(C, fill=255)
    inner = m.filter(ImageFilter.MinFilter(5)); soft = inner.filter(ImageFilter.GaussianBlur(2))
    white = np.percentile(arrs[i][np.asarray(inner) > 0], 90, axis=0)
    a = np.asarray(scr, float) / 255.0 * white
    warp = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).transform(base.size, Image.PERSPECTIVE, coeffs(C, [(0, 0), (W, 0), (W, H), (0, H)]), resample=Image.BICUBIC).filter(ImageFilter.GaussianBlur(0.5))
    fr = Image.composite(warp, base, soft); s = i / 24
    sx = 2.8 * math.sin(2 * math.pi * 0.31 * s) + 1.0 * math.sin(2 * math.pi * 0.83 * s + 1.0)
    sy = 2.1 * math.sin(2 * math.pi * 0.27 * s + 0.5) + 0.8 * math.sin(2 * math.pi * 0.71 * s)
    fr = fr.rotate(0.12 * math.sin(2 * math.pi * 0.23 * s), resample=Image.BICUBIC, center=(w0 / 2, h0 / 2), translate=(sx, sy))
    z = 1.03; cw, ch = w0 / z, h0 / z; xa, ya = (w0 - cw) / 2, (h0 - ch) / 2
    p.stdin.write(fr.crop((round(xa), round(ya), round(xa + cw), round(ya + ch))).resize((w0, h0), Image.LANCZOS).tobytes())
p.stdin.close(); p.wait(); print(out, len(imgs))
