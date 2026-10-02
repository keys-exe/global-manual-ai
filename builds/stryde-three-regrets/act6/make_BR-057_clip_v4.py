"""BR-057 clip v4 (user "make clip for BR-057", 2026-10-01, confirmed frame v6 — low side view from her right): composited, no model, as clip v3 —
the Kie render BR-057_v6.png with the long letter page (ref/BR-057_letter_ref.png) warped onto the screen, its body scrolling up slowly and evenly toward the
sign-off (inbox bar fixed, nothing added), plus a gentle handheld breath sway. 3.04 s, 25 fps, 1080x1920, silent."""
import os, subprocess, math
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)) + "/"
FF = "/usr/local/lib/python3.11/dist-packages/imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2"
base = Image.open(D + "BR-057_v6.png").convert("RGB")          # the v11 frame before its screen paste
page = Image.open(D + "ref/BR-057_letter_ref.png").convert("RGB")
TL, TR, BR, BL = (65, 985), (722, 857), (866, 1523), (260, 1823)
W, H = page.size; HEAD = 55
tall = Image.new("RGB", (W, H + 400), "white"); tall.paste(page, (0, 0))
def coeffs(dst, src):
    A, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; b += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()
c = coeffs([TL, TR, BR, BL], [(0, 0), (W, 0), (W, H), (0, H)])
m = Image.new("L", base.size, 0); ImageDraw.Draw(m).polygon([TL, TR, BR, BL], fill=255)
inner = m.filter(ImageFilter.MinFilter(9)); soft = inner.filter(ImageFilter.GaussianBlur(3))
bw = np.asarray(base, float); white = np.percentile(bw[np.asarray(inner) > 0], 90, axis=0)
FPS, DUR, SCROLL = 25, 3.04, 170        # 150 page-px over the clip ≈ 4–5 lines, slow and even
n = int(round(FPS * DUR)); out = D + "BR-057_clip_v4.mp4"
p = subprocess.Popen([FF, "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1080x1920", "-r", str(FPS), "-i", "-",
                      "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "slow", "-movflags", "+faststart", out], stdin=subprocess.PIPE)
for i in range(n):
    t = i / (n - 1); off = SCROLL * t                     # linear: the same pace from the first frame to the last
    scr = page.copy()
    body = tall.crop((0, HEAD + off, W, HEAD + off + (H - HEAD)))
    scr.paste(body, (0, HEAD)); scr.paste(page.crop((0, 0, W, HEAD)), (0, 0))
    a = np.asarray(scr, float) / 255.0 * white
    warp = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).transform(base.size, Image.PERSPECTIVE, c, resample=Image.BICUBIC).filter(ImageFilter.GaussianBlur(0.6))
    fr = Image.composite(warp, base, soft)
    s = i / FPS                                           # breath sway: slow, small, two frequencies
    dx = 4.0 * math.sin(2 * math.pi * 0.31 * s) + 1.5 * math.sin(2 * math.pi * 0.83 * s + 1.0)
    dy = 3.0 * math.sin(2 * math.pi * 0.27 * s + 0.5) + 1.2 * math.sin(2 * math.pi * 0.71 * s)
    rot = 0.12 * math.sin(2 * math.pi * 0.23 * s)
    fr = fr.rotate(rot, resample=Image.BICUBIC, center=(768, 1376), translate=(dx, dy))
    z = 1.03; cw, ch = 1536 / z, 2752 / z; x0, y0 = (1536 - cw) / 2, (2752 - ch) / 2
    fr = fr.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch))).resize((1080, 1920), Image.LANCZOS)
    p.stdin.write(fr.tobytes())
p.stdin.close(); p.wait(); print(out, n)
