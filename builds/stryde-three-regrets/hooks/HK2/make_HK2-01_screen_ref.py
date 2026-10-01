"""HK2-01 screen reference (user, 2026-10-01: "use this as reference in screen" + a screenshot of the STRYDE product page's review carousel).
The screenshot arrived as a chat image with no file, so this rebuilds it 1:1 in layout and wording at 1600×1000 (a laptop screen):
stryde header + nav, thumbnail strip, black Add to Cart bar, then the centred review — round photo, Emma H., Denver, CO,
Verified Purchase, five gold stars, the quote, carousel dots. The round photo and thumbnails are cut from products/stryde/stryde_refs."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps
D = os.path.dirname(os.path.abspath(__file__)) + "/"
R = D + "../../../../products/stryde/stryde_refs/"
LB = "/usr/share/fonts/truetype/liberation/"
def F(name, size): return ImageFont.truetype(LB + name, size)
W, H = 1600, 1000
im = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(im)
d.text((58, 18), "stryde", font=F("LiberationSans-BoldItalic.ttf", 50), fill="black")
nav = F("LiberationSans-Regular.ttf", 17)
for x, t, c in ((232, "Home", "#111"), (294, "Track My Order", "#555"), (427, "Contact Us", "#555")): d.text((x, 34), t, font=nav, fill=c)
d.text((1410, 34), "PHP", font=nav, fill="#111"); d.line((1449, 41, 1454, 47, 1459, 41), fill="#111", width=2)
d.ellipse((1485, 35, 1500, 50), outline="#111", width=2); d.line((1498, 48, 1505, 55), fill="#111", width=2)
d.rounded_rectangle((1530, 34, 1548, 54), radius=3, outline="#111", width=2)
thumbs = ["front.webp", "worn_front.jpg", "worn_bent.jpg", "product_side.jpg", "worn_rear.jpg", "product_tq_left.jpg", "inner_face.jpg", "worn_front.jpg", "product_macro.jpg", "back.webp", "product_tq_right.jpg", "worn_bent.jpg", "front.webp"]
x = 58
for i, t in enumerate(thumbs):
    th = ImageOps.fit(Image.open(R + t).convert("RGB"), (48, 48))
    im.paste(th, (x, 132))
    if i == 0: d.rectangle((x - 2, 130, x + 49, 181), outline="#111", width=1)
    x += 55
d.rounded_rectangle((825, 82, 1550, 136), radius=12, fill="black")
cf = F("LiberationSans-Bold.ttf", 17); t = "\U0001F6D2  Add to Cart"
d.text((1187, 109), "Add to Cart", font=cf, fill="white", anchor="mm")
d.text((825, 148), "More details", font=F("LiberationSans-Regular.ttf", 16), fill="#111")
cx = W // 2
ph = ImageOps.fit(Image.open(R + "worn_front.jpg").convert("RGB"), (106, 106))
m = Image.new("L", (106, 106), 0); ImageDraw.Draw(m).ellipse((0, 0, 105, 105), fill=255)
im.paste(ph, (cx - 53, 262), m)
d.text((cx, 396), "Emma H.", font=F("LiberationSans-Bold.ttf", 19), fill="#111", anchor="mm")
d.text((cx, 423), "Denver, CO", font=F("LiberationSans-Regular.ttf", 14), fill="#777", anchor="mm")
d.ellipse((cx - 75, 444, cx - 59, 460), fill="#c8650f"); d.line((cx - 71, 452, cx - 68, 456, cx - 62, 448), fill="white", width=2)
d.text((cx - 50, 452), "Verified Purchase", font=F("LiberationSans-Bold.ttf", 15), fill="#c8650f", anchor="lm")
star = F("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf".replace(LB, ""), 1) if False else ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
d.text((cx, 490), "★★★★★", font=star, fill="#f5a623", anchor="mm")
q = ['"45 minutes on the elliptical every morning', "and my knee never used to make it past 20.", "With this strap I'm finishing the full session", "every single time. Comfortable, breathable,", "doesn't budge.\""]
qf = F("LiberationSans-Regular.ttf", 17)
for i, l in enumerate(q): d.text((cx, 528 + i * 25), l, font=qf, fill="#333", anchor="mm")
for i in range(7):
    x0 = cx - 51 + i * 17
    d.ellipse((x0 - 4, 653, x0 + 4, 661), fill="#111" if i == 3 else "#ccc")
im.save(D + "ref/HK2-01_screen_ref.png")
print("ok")
