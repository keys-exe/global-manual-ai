"""HK2-01 screen — a formal letter (user Fix 2026-10-01: "change the screen output into a formal letter and she's reading the messages"):
a plain message view, no app name or logo — subject, sender line, then a typed formal letter in a serif face, its wording drawn from the
script's own lines (the postbag, the stairs, "I wish somebody had told me this four years ago"). 1600×1000, for the laptop screen."""
import os
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LB = "/usr/share/fonts/truetype/liberation/"
def F(n, s): return ImageFont.truetype(LB + n, s)
W, H = 1600, 1000
im = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(im)
d.rectangle((0, 0, W, 64), fill="#f3f3f3"); d.line((0, 64, W, 64), fill="#dddddd")
d.text((40, 20), "Inbox  ›  Customer messages", font=F("LiberationSans-Regular.ttf", 20), fill="#555")
d.text((W - 300, 20), "1 of 25,312", font=F("LiberationSans-Regular.ttf", 20), fill="#777")
x0 = 300
d.text((x0, 100), "My knees, and what I wish I had known", font=F("LiberationSans-Bold.ttf", 30), fill="#111")
d.ellipse((x0, 160, x0 + 44, 204), fill="#c9b8a6")
d.text((x0 + 22, 182), "M", font=F("LiberationSans-Bold.ttf", 20), fill="white", anchor="mm")
d.text((x0 + 60, 160), "Margaret Hale", font=F("LiberationSans-Bold.ttf", 19), fill="#222")
d.text((x0 + 60, 184), "to Stryde Customer Care", font=F("LiberationSans-Regular.ttf", 16), fill="#777")
d.text((W - 300, 166), "12 September", font=F("LiberationSans-Regular.ttf", 16), fill="#777")
d.line((x0, 228, W - 300, 228), fill="#e5e5e5")
body = F("LiberationSerif-Regular.ttf", 21)
paras = [
 "Dear Stryde team,",
 "I am writing to thank you, and to tell you something I think other people should hear.",
 "For four years I bought one thing after another for my knee. A sleeve, then a brace with metal sides, then a wrap. None of them changed how the stairs felt, and in the end I simply stopped going down them more than I had to.",
 "I have been wearing the strap for six weeks now. I came down my own stairs forwards this morning, one at a time, with a cup of tea in my hand.",
 "I only wish somebody had told me this four years ago.",
 "Yours sincerely,",
 "Margaret Hale",
]
y = 260; maxw = W - 300 - x0
for p in paras:
    words = p.split(); line = ""
    for w in words:
        t = (line + " " + w).strip()
        if d.textlength(t, font=body) > maxw: d.text((x0, y), line, font=body, fill="#222"); y += 31; line = w
        else: line = t
    d.text((x0, y), line, font=body, fill="#222"); y += 31 + 16
im.save(D + "ref/HK2-01_letter_ref.png"); print(y)
