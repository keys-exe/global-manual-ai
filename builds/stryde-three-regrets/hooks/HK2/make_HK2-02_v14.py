"""HK2-02 v14 (user Fix 2026-10-01: "show long formal letter in the screen"): the HK2-01 frame (Kie render HK2-01_v10.png, same corners
as HK2-01 v11) with a long formal letter on the screen in place of the bar chart — the same plain message view as HK2-01 and BR-057, no app
name or logo, a third writer (Eileen Ward, "3 of 25,312"); paragraphs drawn from the script's own three regrets (the drawer of supports,
leading with the good leg, saying no) and no new claims. Built in PIL (ref/HK2-02_letter_ref.png), warped on. 0 credits. Output HK2-02_v14.png."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LB = "/usr/share/fonts/truetype/liberation/"
def F(n, s): return ImageFont.truetype(LB + n, s)
W, H = 1600, 1000
im = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(im)
d.rectangle((0, 0, W, 54), fill="#f3f3f3"); d.line((0, 54, W, 54), fill="#dddddd")
d.text((40, 16), "Inbox  ›  Customer messages", font=F("LiberationSans-Regular.ttf", 18), fill="#555")
d.text((W - 260, 16), "3 of 25,312", font=F("LiberationSans-Regular.ttf", 18), fill="#777")
x0, x1 = 260, W - 260
d.text((x0, 76), "Three things I wish I had known", font=F("LiberationSans-Bold.ttf", 25), fill="#111")
d.ellipse((x0, 122, x0 + 34, 156), fill="#b9a9c6"); d.text((x0 + 17, 139), "E", font=F("LiberationSans-Bold.ttf", 16), fill="white", anchor="mm")
d.text((x0 + 46, 122), "Eileen Ward", font=F("LiberationSans-Bold.ttf", 16), fill="#222")
d.text((x0 + 46, 141), "to Stryde Customer Care", font=F("LiberationSans-Regular.ttf", 13), fill="#777")
d.text((x1 - 100, 126), "26 September", font=F("LiberationSans-Regular.ttf", 13), fill="#777")
d.line((x0, 170, x1, 170), fill="#e5e5e5")
body = F("LiberationSerif-Regular.ttf", 20)
paras = [
 "Dear Stryde team,",
 "You asked customers to write and tell you how they got on, and I have been putting it off because I knew it would not be a short letter.",
 "The first thing is the drawer. I had a whole drawer of supports for my knees, sleeves and wraps and one with metal hinges, and I kept buying the next one because I thought the last one simply wasn't good enough. None of them changed how the stairs felt.",
 "The second thing is my good leg. I had been leaning on it for years without knowing, at the bus stop, in the kitchen, on every step, and by the time I noticed it was aching too.",
 "The third thing is the hardest to write. I said no to so much. No to walks, no to the garden centre with my daughter, no to the school play because of the hall steps. I told everyone I was tired. I wasn't tired.",
 "For a long time I thought this was simply what getting older looked like. My mother had bad knees, and her mother before her, and I assumed the stairs would win in the end and that there was nothing to be done but be careful.",
 "My daughter was the one who ordered the strap. I will be honest, I put it in the drawer with the others for a fortnight before I tried it.",
 "I started with one knee, as your leaflet said, and wear it on both now. Last Sunday I walked my granddaughter to the park and back, and I sat on the floor with her afterwards and got up again on my own.",
 "Those are my three, and I suspect I am not the only one.",
 "With kind regards,",
 "Eileen Ward",
]
y = 192; maxw = x1 - x0
for p in paras:
    line = ""
    for w in p.split():
        t = (line + " " + w).strip()
        if d.textlength(t, font=body) > maxw: d.text((x0, y), line, font=body, fill="#222"); y += 29; line = w
        else: line = t
    d.text((x0, y), line, font=body, fill="#222"); y += 29 + 13
im.save(D + "ref/HK2-02_letter_ref.png"); print("page bottom", y)
base = Image.open(D + "HK2-01_v10.png").convert("RGB")
TL, TR, BR, BL = (265, 1014), (1037, 1045), (1003, 1546), (275, 1500)
def coeffs(dst, src):
    A, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        A += [[x, y, 1, 0, 0, 0, -u * x, -u * y], [0, 0, 0, x, y, 1, -v * x, -v * y]]; b += [u, v]
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()
warp = im.transform(base.size, Image.PERSPECTIVE, coeffs([TL, TR, BR, BL], [(0, 0), (W, 0), (W, H), (0, H)]), resample=Image.BICUBIC)
m = Image.new("L", base.size, 0); ImageDraw.Draw(m).polygon([TL, TR, BR, BL], fill=255)
inner = m.filter(ImageFilter.MinFilter(9))
bw = np.asarray(base, float); ww = np.asarray(warp, float) / 255.0 * np.percentile(bw[np.asarray(inner) > 0], 90, axis=0)
warp = Image.fromarray(np.clip(ww, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
Image.composite(warp, base, inner.filter(ImageFilter.GaussianBlur(3))).save(D + "HK2-02_v14.png")
