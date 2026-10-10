#!/usr/bin/env python3
# seg.py VIDEO [thresh] : split a 60 fps capture into runs of near-identical frames (downsampled 192x108),
# print each run's start time, length in frames and mean RGB, so a brief screen (Saving/Loading picture) shows as its own run.
import subprocess, sys
v=sys.argv[1]; th=float(sys.argv[2]) if len(sys.argv)>2 else 2.0
W,H=192,108
raw=subprocess.run(['ffmpeg','-loglevel','error','-i',v,'-vf',f'scale={W}:{H}','-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
n=len(raw)//(W*H*3); fr=[raw[i*W*H*3:(i+1)*W*H*3] for i in range(n)]
def mean(b): return tuple(sum(b[c::3])/(W*H) for c in range(3))
def diff(a,b): return sum(abs(x-y) for x,y in zip(a[::7],b[::7]))/len(a[::7])
runs=[[0]]
for i in range(1,n):
    if diff(fr[i],fr[runs[-1][-1]])>th: runs.append([i])
    else: runs[-1].append(i)
for r in runs:
    m=mean(fr[r[0]]); print(f"t={r[0]/60:6.3f}s frame {r[0]:4d}  len {len(r):4d} ({len(r)/60:.3f}s)  rgb {m[0]:.0f},{m[1]:.0f},{m[2]:.0f}")
