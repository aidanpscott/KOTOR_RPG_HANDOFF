#!/usr/bin/env python3
# hfnum.py VIDEO : full-res crop above Onjo's token (x 880-1020, y 270-330): per frame red-text and white-text pixel counts
# + bottom band (full-res y 750-770, x 520-1740 at 1/4) red excess. Writes VIDEO.num.json
import subprocess,sys,json
v=sys.argv[1]
def stream(vf,W,H):
    p=subprocess.Popen(['ffmpeg','-loglevel','error','-i',v,'-vf',vf,'-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
    FS=W*H*3
    while True:
        b=p.stdout.read(FS)
        if len(b)<FS: return
        yield b
out=[]
for b in stream('crop=140:60:880:270',140,60):
    red=wht=0
    for o in range(0,len(b),3):
        r,g,bl=b[o],b[o+1],b[o+2]
        if r>150 and g<100 and bl<100: red+=1
        elif r>170 and g>170 and bl>170: wht+=1
    out.append([red,wht])
i=0
for b in stream('crop=1220:20:520:750,scale=305:5',305,5):
    n=len(b)//3; out[i].append(sum(b[o]-b[o+1] for o in range(0,len(b),3))/n); i+=1
json.dump(out,open(v+'.num.json','w')); print(len(out),'frames')
