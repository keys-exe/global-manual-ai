"""HK2-01 clip v9 page (user Fix on clip v8, 2026-10-01: "make it a fast scroll in the laptop. Texts should look like reviews/post purchase
survey, so they're short paragraphs"). A tall page: the user's own page on top (ref/HK2-01_v12_page.png, as their image v12), then a long
list of short customer reviews and post-purchase survey answers in the same white page style — name, verified badge, five stars, one or two
short lines. Text drawn in PIL so every word is real; lines drawn from the script's themes, no new claims. Output ref/HK2-01_reviews_tall.png."""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LB = "/usr/share/fonts/truetype/liberation/"
def F(n, s): return ImageFont.truetype(LB + n, s)
top = Image.open(D + "ref/HK2-01_v12_page.png").convert("RGB"); W, H = top.size
bg = (246, 246, 248)
items = [
 ("R", "Margaret H.", "I came down my own stairs forwards this morning. First time in four years."),
 ("S", "What made you finally try STRYDE?", "My drawer of sleeves and braces. None of them changed the stairs."),
 ("R", "Ken A.", "Didn't realise how much I'd been leaning on my good leg until it started aching too."),
 ("R", "Joan P.", "I stopped saying no to the grandchildren's days out. That's the review."),
 ("S", "What would you tell someone on the fence?", "Start with one knee, like the leaflet says. Give it a week."),
 ("R", "Patricia D.", "Walked to the post office and back. Went up my friend's steps without holding on."),
 ("R", "Brian C.", "Stairs again, finally. One at a time, with a cup of tea in my hand."),
 ("S", "What surprised you most?", "How small it is. I expected another bulky brace for the drawer."),
 ("R", "Linda M.", "Six weeks in. I stood at the bus stop without shifting from foot to foot."),
 ("R", "Susan R.", "My daughter ordered it and I wasn't hopeful. I wear it most days now."),
 ("S", "What did you try before?", "Sleeves, a hinged brace, a wrap, the gel one. Eleven in total."),
 ("R", "David P.", "Back on my knees at the allotment for the first time in two summers."),
 ("R", "Carol J.", "I thought it would be another sleeve for the drawer. It wasn't."),
 ("S", "What do you wish you'd known sooner?", "That it wasn't just getting older. I lost four years to that idea."),
 ("R", "Alan F.", "If somebody had told me this four years ago I'd have saved a lot of no's."),
 ("R", "Maureen K.", "Eleven steps up to our church. I counted every one, and I didn't stop."),
 ("S", "Who would you recommend it to?", "My sister. She's been saying no to walks for as long as I was."),
 ("R", "Peter W.", "Walked into town and back without planning where to sit down."),
 ("R", "Eileen W.", "Started with one knee as you suggested. Now I wear it on both."),
 ("S", "What changed in the first week?", "I came downstairs facing forwards. My husband noticed before I did."),
 ("R", "Graham T.", "I used to stand with all my weight on one side and never noticed."),
 ("R", "Pauline B.", "Danced two songs at my niece's wedding. Two more than in five years."),
 ("S", "Anything else you'd like to tell us?", "Please tell others. Someone out there has a drawer like mine."),
 ("R", "Derek H.", "For the first time in four years I came downstairs facing forwards."),
]
CW = 760; x0 = (W - CW) // 2; pad = 34
fn, fq, fb, fs = F("LiberationSans-Bold.ttf", 26), F("LiberationSans-Bold.ttf", 24), F("LiberationSans-Regular.ttf", 26), F("LiberationSans-Regular.ttf", 19)
def wrap(d, t, f, w):
    out, line = [], ""
    for word in t.split():
        s = (line + " " + word).strip()
        if d.textlength(s, font=f) > w: out.append(line); line = word
        else: line = s
    return out + [line]
probe = ImageDraw.Draw(Image.new("RGB", (10, 10)))
blocks = []
for kind, a, b in items:
    lines = wrap(probe, ("“" + b + "”") if kind == "R" else b, fb, CW - 2 * pad)
    blocks.append((kind, a, lines, 116 + 36 * len(lines) if kind == "R" else 112 + 36 * len(lines)))
LH = sum(h + 22 for *_, h in blocks) + 120
lst = Image.new("RGB", (W, LH), bg); d = ImageDraw.Draw(lst)
d.text((W // 2, 40), "Customer reviews · 25,312", font=F("LiberationSans-Bold.ttf", 30), fill="#222", anchor="mm")
y = 90
for kind, a, lines, h in blocks:
    d.rounded_rectangle((x0, y, x0 + CW, y + h), 18, fill="white", outline="#e6e6e6", width=2)
    if kind == "R":
        d.ellipse((x0 + pad, y + 24, x0 + pad + 44, y + 68), fill="#c9b8a6")
        d.text((x0 + pad + 22, y + 46), a[0], font=F("LiberationSans-Bold.ttf", 20), fill="white", anchor="mm")
        d.text((x0 + pad + 60, y + 30), a, font=fn, fill="#222")
        d.text((x0 + pad + 60, y + 62), "Verified purchase", font=fs, fill="#c58a1c")
        for k in range(5):                                   # five drawn stars (the font has no star glyph)
            cx, cy, R, r = x0 + CW - pad - 12 - k * 28, y + 46, 12, 5
            pts = [(cx + (R if j % 2 == 0 else r) * np.sin(j * np.pi / 5), cy - (R if j % 2 == 0 else r) * np.cos(j * np.pi / 5)) for j in range(10)]
            d.polygon(pts, fill="#f0a020")
        ty = y + 100
    else:
        d.text((x0 + pad, y + 26), "POST-PURCHASE SURVEY", font=fs, fill="#8a8a8a")
        d.text((x0 + pad, y + 52), a, font=fq, fill="#222")
        ty = y + 94
    for ln in lines:
        d.text((x0 + pad, ty), ln, font=fb, fill="#333"); ty += 36
    y += h + 22
tall = Image.new("RGB", (W, H + LH + 600), bg); tall.paste(lst, (0, H))
ta = np.asarray(top, float); g = np.clip((np.arange(H) - (H - 160)) / 160.0, 0, 1)[:, None, None]   # fade the user's page into the list
tall.paste(Image.fromarray((ta * (1 - g) + np.array(bg, float) * g).astype(np.uint8)), (0, 0))
tall.save(D + "ref/HK2-01_reviews_tall.png"); print(tall.size)
