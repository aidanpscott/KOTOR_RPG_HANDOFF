#!/usr/bin/env python3
"""Per-frame feedback metrics v2 (regions read off a real fight frame at 480x270):
 flash  = mean red excess R-(G+B)/2 over the lower-screen glow band y172..200, x120..460
 hp     = mean abs diff of the 'N of M' text of the player's card (y92..104, x70..112) against the previous frame
 log    = mean abs diff of the combat-log rows (y232..258)
 numred = pixels red-ish (R-(G+B)/2>60) in the window over the player's token (y84..112, x250..300)
 numwht = bright near-white pixels in that window, excluding the token ring rows (y84..108)"""
import sys, subprocess, numpy as np, csv
v=sys.argv[1]; out=sys.argv[2] if len(sys.argv)>2 else 'metrics2.csv'
W,H=480,270
p=subprocess.Popen(['ffmpeg','-loglevel','error','-i',v,'-vf',f'scale={W}:{H}','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
num,den=subprocess.check_output(['ffprobe','-v','error','-select_streams','v:0','-show_entries','stream=r_frame_rate','-of','csv=p=0',v]).decode().strip().split('/')
fps=float(num)/float(den)
n=W*H*3; prev=None; rows=[]; i=0
while True:
    b=p.stdout.read(n)
    if len(b)<n: break
    a=np.frombuffer(b,np.uint8).reshape(H,W,3).astype(np.int16)
    r,g,bl=a[...,0],a[...,1],a[...,2]
    exc=r-(g+bl)//2
    flash=float(exc[172:200,120:460].mean())
    hp=a[92:104,70:112]; lg=a[232:258,:]
    d_hp=0.0 if prev is None else float(np.abs(hp-prev[0]).mean())
    d_lg=0.0 if prev is None else float(np.abs(lg-prev[1]).mean())
    prev=(hp.copy(),lg.copy())
    nr=int((exc[104:118,258:284]>60).sum())
    nw=int(((r[104:112,260:288]>120)&(g[104:112,260:288]>120)&(bl[104:112,260:288]>100)).sum())
    rows.append((i,round(i*1000/fps,2),round(d_lg,3),round(flash,2),round(d_hp,3),nr,nw)); i+=1
w=csv.writer(open(out,'w')); w.writerow(['frame','t_ms','log','flash','hp','numred','numwht']); w.writerows(rows)
print('frames',i,'fps',fps)
