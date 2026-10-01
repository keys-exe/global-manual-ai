"""BR-057 clip v5 (user Fix on clip v4 "the hand must scroll up along with the screen", 2026-10-01): Kling gen 3 (BR-057_kling_g3.mp4,
locked camera, her two fingers slide up the trackpad, screen blank) + the long letter (ref/BR-057_letter_ref.png) put back on the screen
frame by frame. The page scrolls up in step with the hand: the scroll offset follows the hand's measured upward travel. Screen corners
measured on Kling frame 1, a per-frame drift (white-screen centroid) applied; then the same breath sway and 3% zoom as the other composites."""
import os, subprocess, math, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)) + "/"
FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
tmp = tempfile.mkdtemp()
subprocess.run([FF, "-v", "error", "-y", "-i", D + "BR-057_kling_g3.mp4", tmp + "/f%03d.png"], check=True)
frames = sorted(f for f in os.listdir(tmp) if f.endswith(".png")); n = len(frames)
page = Image.open(D + "ref/BR-057_letter_ref.png").convert("RGB")
W, H = page.size; HEAD = 55; SCROLL = 170
tall = Image.new("RGB", (W, H + 400), "white"); tall.paste(page, (0, 0))
C0 = [(46.0, 691.5), (503.7, 602.3), (603.2, 1059.3), (181.7, 1278.5)]
def coeffs(dst, src):
    A, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; b += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()
def screen_c(a):
    m = a[600:1300, 40:640] > 232; ys, xs = np.where(m); return xs.mean(), ys.mean()
def hand_y(rgb):
    a = rgb[1050:1450, 780:1072]; r, g, b = a[..., 0], a[..., 1], a[..., 2]
    ys, _ = np.where((r > 170) & (g > 130) & (b > 110) & (r - b > 20)); return ys.mean()
imgs = [Image.open(f"{tmp}/{f}").convert("RGB") for f in frames]
arrs = [np.asarray(im).astype(int) for im in imgs]
sc = [screen_c(a.mean(2)) for a in arrs]
hy = np.array([hand_y(a) for a in arrs])
hy = np.convolve(np.pad(hy, 4, mode="edge"), np.ones(9) / 9, mode="valid")    # smooth
travel = np.maximum.accumulate(hy[0] - hy); travel = travel / max(travel[-1], 1e-6)
out = D + "BR-057_clip_v5.mp4"; w0, h0 = imgs[0].size
p = subprocess.Popen([FF, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w0}x{h0}", "-r", "24", "-i", "-",
                      "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "slow", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
for i, base in enumerate(imgs):
    dx, dy = sc[i][0] - sc[0][0], sc[i][1] - sc[0][1]
    C = [(x + dx, y + dy) for x, y in C0]
    off = SCROLL * travel[i]
    scr = page.copy(); scr.paste(tall.crop((0, round(HEAD + off), W, round(HEAD + off) + (H - HEAD))), (0, HEAD)); scr.paste(page.crop((0, 0, W, HEAD)), (0, 0))
    m = Image.new("L", base.size, 0); ImageDraw.Draw(m).polygon(C, fill=255)
    inner = m.filter(ImageFilter.MinFilter(5)); soft = inner.filter(ImageFilter.GaussianBlur(2))
    white = np.percentile(arrs[i][np.asarray(inner) > 0], 90, axis=0)
    a = np.asarray(scr, float) / 255.0 * white
    warp = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).transform(base.size, Image.PERSPECTIVE, coeffs(C, [(0, 0), (W, 0), (W, H), (0, H)]), resample=Image.BICUBIC).filter(ImageFilter.GaussianBlur(0.5))
    fr = Image.composite(warp, base, soft)
    s = i / 24
    sx = 2.8 * math.sin(2 * math.pi * 0.31 * s) + 1.0 * math.sin(2 * math.pi * 0.83 * s + 1.0)
    sy = 2.1 * math.sin(2 * math.pi * 0.27 * s + 0.5) + 0.8 * math.sin(2 * math.pi * 0.71 * s)
    fr = fr.rotate(0.12 * math.sin(2 * math.pi * 0.23 * s), resample=Image.BICUBIC, center=(w0 / 2, h0 / 2), translate=(sx, sy))
    z = 1.03; cw, ch = w0 / z, h0 / z; x0, y0 = (w0 - cw) / 2, (h0 - ch) / 2
    fr = fr.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch))).resize((w0, h0), Image.LANCZOS)
    p.stdin.write(fr.tobytes())
p.stdin.close(); p.wait(); print(out, n, [round(t, 2) for t in travel[::12]])
