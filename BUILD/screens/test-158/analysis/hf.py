#!/usr/bin/env python3
# hf.py VIDEO : per-frame features of a hit-feedback take (fight layout, Onjo token at full-res (948,340)).
# Streams at 480x270. Prints: HP-text changes, log-line changes, and frames where edge red excess or
# red/white pixel counts around the token leave their baseline.
import subprocess, sys, statistics, json
v=sys.argv[1]; W,H=480,270; FS=W*H*3
p=subprocess.Popen(['ffmpeg','-loglevel','error','-i',v,'-vf',f'scale={W}:{H}','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
def reg(b,x0,y0,x1,y1):
    return [b[(y*W+x)*3:(y*W+x)*3+3] for y in range(y0,y1) for x in range(x0,x1)]
def rg(px): return sum(q[0]-q[1] for q in px)/len(px)
rows=[]; i=0
while True:
    b=p.stdout.read(FS)
    if len(b)<FS: break
    hp=bytes(b''.join(reg(b,75,70,105,77)))
    log=bytes(b''.join(reg(b,40,239,230,247)))
    top=rg(reg(b,40,20,440,24)); right=rg(reg(b,436,30,442,200)); bottom=rg(reg(b,40,225,440,229))
    tok=reg(b,205,55,270,105)
    red=sum(1 for q in tok if q[0]>150 and q[1]<90 and q[2]<90)
    wht=sum(1 for q in tok if q[0]>200 and q[1]>200 and q[2]>200)
    rows.append((i,hash(hp),hash(log),top,right,bottom,red,wht)); i+=1
json.dump(rows,open(v+'.json','w'))
print(len(rows),'frames')
