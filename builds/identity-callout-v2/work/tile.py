import sys
from PIL import Image
ims=[Image.open(f'renders/{b}.view.jpg') for b in sys.argv[2:]]
W=sum(i.width for i in ims)+10*len(ims); c=Image.new('RGB',(W,900),'white'); x=0
for i in ims: c.paste(i,(x,0)); x+=i.width+10
c.save(sys.argv[1],quality=85)
