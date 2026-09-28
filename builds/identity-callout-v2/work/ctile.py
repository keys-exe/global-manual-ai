import sys
from PIL import Image
ims=[Image.open(f'work/{b}.sheet.jpg') for b in sys.argv[2:]]
h=min(i.height for i in ims); ims=[i.resize((i.width*h//i.height,h)) for i in ims]
W=sum(i.width for i in ims)+8*len(ims); c=Image.new('RGB',(W,h),'white'); x=0
for i in ims: c.paste(i,(x,0)); x+=i.width+8
c.resize((c.width*1000//c.height,1000)).save(sys.argv[1],quality=80)
