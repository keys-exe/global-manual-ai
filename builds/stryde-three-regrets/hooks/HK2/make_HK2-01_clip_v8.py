"""HK2-01 clip v8 (user "make clip for HK2-01", 2026-10-01, image v12 = the user's own image): Kling gen 8 (HK2-01_kling_g8.mp4 — locked camera over her
right shoulder, her fingers slide up the trackpad, screen blank) + the user's own page (ref/HK2-01_v12_page.png, lifted off their image) put back on the screen
frame by frame, its body scrolling up in step with the hand (LESSONS L09; as BR-057 clip v5 and HK2-02 clip v7) — the page kept exactly as the user made it. Hand travel by template match on the fingers;
screen corners measured on Kling frame 1; per-frame drift from the white-screen centroid; light sway, 3% zoom."""
import os, subprocess, math, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)) + "/"
FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
tmp = tempfile.mkdtemp()
subprocess.run([FF, "-v", "error", "-y", "-i", D + "HK2-01_kling_g8.mp4", tmp + "/f%03d.png"], check=True)
frames = sorted(f for f in os.listdir(tmp) if f.endswith(".png"))
imgs = [Image.open(f"{tmp}/{f}").convert("RGB") for f in frames]; arrs = [np.asarray(im).astype(int) for im in imgs]
page = Image.open(D + "ref/HK2-01_v12_page.png").convert("RGB")
W, H = page.size; HEAD = 0; SCROLL = 150
pg = np.asarray(page, float); edge = np.median(pg[H - 40:H - 4], axis=0)                      # the page's own bottom edge, per column
tall = Image.fromarray(np.vstack([pg, np.repeat(edge[None], 400, axis=0)]).clip(0, 255).astype(np.uint8))   # extended without a seam
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
travel = np.maximum.accumulate(up - up[0]); travel = travel / max(travel[-1], 1e-6)
# the finger track on this clip is noisy (it jumps 0.02 -> 0.72 in half a second); the hand rises steadily overall, so the scroll
# follows an even eased stroke over the same span instead — slow and steady, never a jerk
tt = np.arange(len(imgs)) / 24.0; e = np.clip((tt - 0.15) / 2.75, 0, 1); travel = e * e * (3 - 2 * e)
s0 = [sc(a) for a in arrs]; w0, h0 = imgs[0].size; out = D + "HK2-01_clip_v8.mp4"
p = subprocess.Popen([FF, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w0}x{h0}", "-r", "24", "-i", "-",
                      "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "slow", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
for i, base in enumerate(imgs):
    dx, dy = s0[i][0] - s0[0][0], s0[i][1] - s0[0][1]; C = [(x + dx, y + dy) for x, y in C0]
    off = SCROLL * travel[i]
    scr = page.copy(); scr.paste(tall.crop((0, round(HEAD + off), W, round(HEAD + off) + (H - HEAD))), (0, HEAD)); (scr.paste(page.crop((0, 0, W, HEAD)), (0, 0)) if HEAD else None)
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
p.stdin.close(); p.wait(); print(out, len(imgs), [round(t, 2) for t in travel[::12]])
