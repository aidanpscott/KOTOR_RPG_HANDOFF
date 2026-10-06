import csv, sys
r=list(csv.DictReader(open(sys.argv[1])))
FPS=60.0
log=[float(x['log']) for x in r]; fl=[float(x['flash']) for x in r]; hp=[float(x['hp']) for x in r]
nr=[int(x['numred']) for x in r]; nw=[int(x['numwht']) for x in r]
ev=[]
for i in range(1,len(r)):
    if log[i]>0.3 and (not ev or i-ev[-1]>30): ev.append(i)
rows=[]
for k,e in enumerate(ev):
    win=range(max(0,e-6),min(len(r),e+40))
    hpf=next((i for i in win if hp[i]>0.02),None)
    fb=fl[e-3] if e>=3 else fl[0]
    ff=next((i for i in range(e-6,min(len(r),e+40)) if i>=0 and fl[i]-fb>5),None)
    hit=hpf is not None
    nb=min(nr[max(0,e-6):e]) if e>=1 else 0
    nf=next((i for i in range(e-6,min(len(r),e+40)) if i>=0 and nr[i]-nb>=2),None) if hit else None
    wb=min(nw[max(0,e-6):e]) if e>=1 else 0
    mf=next((i for i in range(e-6,min(len(r),e+40)) if i>=0 and nw[i]-wb>=2),None) if not hit else None
    rows.append((k+1,e,'hit' if hit else 'miss',hpf,ff,nf,mf))
print('turn outcome  event_f  hp_f  flash_f  number_f  miss_f   (frames @60; deltas vs the event frame)')
for t,e,o,h,f,n,m in rows:
    d=lambda x: '-' if x is None else f'{x}({x-e:+d})'
    print(f'{t:>3} {o:5} {e:>8} {d(h):>10} {d(f):>11} {d(n):>11} {d(m):>11}')
print('hits',sum(1 for x in rows if x[2]=='hit'),'misses',sum(1 for x in rows if x[2]=='miss'))
