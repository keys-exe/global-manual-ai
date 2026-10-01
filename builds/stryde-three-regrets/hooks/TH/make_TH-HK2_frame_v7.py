"""TH-HK2 frame v7 (user Fix "use previous camera angle, the laptop place farther to the frame", 2026-10-01): v6 (prompt edit) left the laptop cut by the right edge, so crop v5 (v3 outpainted) back to v3's camera distance — measured from her face size — framed a little to the right so the whole laptop sits inside."""
import os
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)) + "/"
im = Image.open(D + "TH-HK2_frame_v5.png").convert("RGB")
W = 1120; H = round(W * 16 / 9); x1 = 1455; y0 = 600
im.crop((x1 - W, y0, x1, y0 + H)).resize((1536, 2731), Image.LANCZOS).save(D + "TH-HK2_frame_v7.png")
