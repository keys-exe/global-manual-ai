"""BR-057 screen — a long formal letter (user Fix 2026-10-01: "show a long formal letter in the screen"), for the line "Most of those messages end
the same way.": a plain message view, no app name or logo; a different writer from HK2-01; seven paragraphs drawn from the script's own lines
(the drawer of supports, leading with the good leg, saying no to days out, coming down the stairs) and no new claims; it ends the way the script
says they all end. 1600×1000, for the laptop screen."""
import os
from PIL import Image, ImageDraw, ImageFont
D = os.path.dirname(os.path.abspath(__file__)) + "/"
LB = "/usr/share/fonts/truetype/liberation/"
def F(n, s): return ImageFont.truetype(LB + n, s)
W, H = 1600, 1000
im = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(im)
d.rectangle((0, 0, W, 54), fill="#f3f3f3"); d.line((0, 54, W, 54), fill="#dddddd")
d.text((40, 16), "Inbox  ›  Customer messages", font=F("LiberationSans-Regular.ttf", 18), fill="#555")
d.text((W - 260, 16), "2 of 25,312", font=F("LiberationSans-Regular.ttf", 18), fill="#777")
x0, x1 = 260, W - 260
d.text((x0, 76), "A long letter, but I wanted you to have it", font=F("LiberationSans-Bold.ttf", 25), fill="#111")
d.ellipse((x0, 122, x0 + 34, 156), fill="#a9b8c6"); d.text((x0 + 17, 139), "P", font=F("LiberationSans-Bold.ttf", 16), fill="white", anchor="mm")
d.text((x0 + 46, 122), "Patricia Doyle", font=F("LiberationSans-Bold.ttf", 16), fill="#222")
d.text((x0 + 46, 141), "to Stryde Customer Care", font=F("LiberationSans-Regular.ttf", 13), fill="#777")
d.text((x1 - 100, 126), "3 September", font=F("LiberationSans-Regular.ttf", 13), fill="#777")
d.line((x0, 170, x1, 170), fill="#e5e5e5")
body = F("LiberationSerif-Regular.ttf", 20)
paras = [
 "Dear Stryde team,",
 "I have been meaning to write this for a month, and it has turned into rather a long letter, so please forgive me.",
 "For six years I had a drawer full of things for my knees. A stretchy sleeve, then one with metal sides, then a wrap, then the gel one my neighbour swore by. Every one of them went round the whole knee, and not one of them changed how the stairs felt.",
 "Without noticing, I had started leading with my good leg everywhere. Then last winter the good knee began to ache as well, and I was frightened that I would end up downstairs for good.",
 "I said no to a great deal in those years. No to the long walk with my sister, no to the day out with the grandchildren, no to my friend's house because of the steps up to her front door. People thought I had simply gone off things.",
 "When the strap came I put it on one knee only, as you suggested, and went to my own stairs and came down forwards. I stood at the bottom for quite a while afterwards.",
 "I have both knees in them now. Yesterday I walked to the post office and back, and I went up my friend's steps without holding on.",
 "I only wish somebody had told me this four years ago.",
 "Yours sincerely,",
 "Patricia Doyle",
]
y = 192; maxw = x1 - x0
for p in paras:
    line = ""
    for w in p.split():
        t = (line + " " + w).strip()
        if d.textlength(t, font=body) > maxw: d.text((x0, y), line, font=body, fill="#222"); y += 29; line = w
        else: line = t
    d.text((x0, y), line, font=body, fill="#222"); y += 29 + 13
im.save(D + "ref/BR-057_letter_ref.png"); print(y)
