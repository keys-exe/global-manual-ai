import numpy as np, subprocess, sys
u=np.fromfile("u2.rgb",np.uint8).reshape(2000,2000,3).astype(float)
r=np.fromfile("ref.rgb",np.uint8).reshape(1536,2752,3).astype(float)
s=float(sys.argv[1]) if len(sys.argv)>1 else 1140/1396
ys=float(sys.argv[2]) if len(sys.argv)>2 else None
X0,X1=674,2070   # ref slide inner edges
UX0=430          # user left slide inner edge
# ref product mask: dark, between slides, column-filled
lr=r.mean(2)
m=np.zeros(lr.shape,bool)
sub=lr[350:1150,X0+6:X1-6]<100
for c in range(sub.shape[1]):
    idx=np.where(sub[:,c])[0]
    if len(idx): m[350+idx.min():350+idx.max()+1,X0+6+c]=True
# map user pixel -> ref pixel
if ys is None: ys=865-791*s
yy,xx=np.mgrid[0:2000,0:2000]
rx=(xx-UX0)/s+X0; ry=(yy-ys)/s
ok=(rx>=0)&(rx<2751)&(ry>=0)&(ry<1535)
rxi=np.clip(rx,0,2750).astype(int); ryi=np.clip(ry,0,1534).astype(int)
fx=np.clip(rx-rxi,0,1)[...,None]; fy=np.clip(ry-ryi,0,1)[...,None]
def samp(a):
    return (a[ryi,rxi]*(1-fx)*(1-fy)+a[ryi,rxi+1]*fx*(1-fy)+a[ryi+1,rxi]*(1-fx)*fy+a[ryi+1,rxi+1]*fx*fy)
rs=samp(r); ms=samp(m.astype(float)[...,None])[...,0]*ok
# feather 3px box blur
def blur(a,k=3):
    for ax in (0,1):
        c=np.cumsum(np.pad(a,[(k+1,k) if i==ax else (0,0) for i in range(2)],mode='edge'),axis=ax)
        a=(np.take(c,range(2*k+1,c.shape[ax]),axis=ax)-np.take(c,range(0,c.shape[ax]-2*k-1),axis=ax))/(2*k+1)
    return a
alpha=blur(ms)[...,None]
# erase old shell outside the new one
lu=u.mean(2)
bg=np.median(u[1900:1990,50:300].reshape(-1,3),axis=0)
old=np.zeros(lu.shape,bool)
old[460:1040,UX0+4:1570-4]=lu[460:1040,UX0+4:1570-4]<215
old&=ms<0.5
# grow erase by 4px to remove dark fringes
oldf=blur(old.astype(float),4)>0.05
oldf&=~(ms>0.5)
out=u.copy()
out[oldf]=bg
out=out*(1-alpha)+rs*alpha
print("scale",s,"ys",ys,"bg",bg,"erased px",int(oldf.sum()))
out.clip(0,255).astype(np.uint8).tofile("comp.rgb")
subprocess.run(["ffmpeg","-loglevel","error","-y","-f","rawvideo","-pix_fmt","rgb24","-s","2000x2000","-i","comp.rgb","comp.png"],check=True)
subprocess.run(["ffmpeg","-loglevel","error","-y","-i","comp.png","-vf","scale=1000:-2","comp_prev.jpg"],check=True)
# --- joins at the slides ---
out=out.clip(0,255)
a2=alpha[...,0]
L0=int(round(UX0+6)); R0=int(round(UX0+(X1-6-X0)*s))-1
for x0,src,rng in ((L0,L0+2,range(L0-18,L0+2)),(R0,R0-2,range(R0-1,R0+20))):
    rows=a2[:,src]>0.5
    for x in rng:
        out[rows,x]=out[rows,src]
# remnants of the old shell above each slide
for xa,xb in ((290,L0),(R0,1712)):
    box=(slice(620,705),slice(xa,xb))
    d=u[box].mean(2)<242
    seg=out[box]; seg[d]=bg; out[box]=seg
# the user's chrome slides back on top
for xa,xb in ((290,L0+2),(R0-2,1712)):
    box=(slice(684,1060),slice(xa,xb))
    ch=u[box].mean(2)>125
    seg=out[box]; seg[ch]=u[box][ch]; out[box]=seg
out.astype(np.uint8).tofile("comp.rgb")
subprocess.run(["ffmpeg","-loglevel","error","-y","-f","rawvideo","-pix_fmt","rgb24","-s","2000x2000","-i","comp.rgb","comp.png"],check=True)
subprocess.run(["ffmpeg","-loglevel","error","-y","-i","comp.png","-vf","scale=1000:-2","comp_prev.jpg"],check=True)
subprocess.run(["ffmpeg","-loglevel","error","-y","-i","comp.png","-filter_complex","[0]crop=500:600:250:550[a];[0]crop=500:600:1300:550[b];[a][b]hstack","zoom.jpg"],check=True)
print("L0",L0,"R0",R0)
