#!/usr/bin/env python3
# hftable.py VIDEO : per attack window (split on long quiet gaps between activity), table of
# first HP change, edge run (top/right/bottom), red number run, white 'miss' run, frames relative to the HP change / log change.
import json,sys,statistics
v=sys.argv[1]; a=json.load(open(v+'.json')); n=json.load(open(v+'.num.json'))
N=min(len(a),len(n))
bt=statistics.median(x[3] for x in a); br=statistics.median(x[4] for x in a); bb=statistics.median(x[2] for x in n)
edge=[a[i][3]-bt>3 or a[i][4]-br>3 for i in range(N)]
red=[n[i][0]>=15 for i in range(N)]; wht=[n[i][1]>=int(__import__("os").environ.get("WT","340")) for i in range(N)]
bot=[n[i][2]-bb for i in range(N)]
hpc=[i for i in range(1,N) if a[i][1]!=a[i-1][1]]
logc=[i for i in range(1,N) if a[i][2]!=a[i-1][2]]
def runs(m):
    out=[];s=None
    for i,x in enumerate(m):
        if x and s is None: s=i
        if not x and s is not None: out.append((s,i-s)); s=None
    return out
E,Rr,Wr=runs(edge),runs(red),runs(wht)
# attack instants: start of each red or white run (the number or 'miss' appears once per attack) plus edge runs
events=sorted(set([s for s,_ in Rr]+[s for s,_ in Wr]+[s for s,_ in E]))
# group events within 1.5 s
groups=[]
for e in events:
    if groups and e-groups[-1][-1]<90: groups[-1].append(e)
    else: groups.append([e])
print("turn  hp_change  log_change  edge(start,len,peakTop,peakRight,peakBottom)  red(start,len)  miss(start,len)")
k=0
for g in groups:
    s0=g[0]-30; s1=g[-1]+120
    h=[i for i in hpc if s0<=i<=s1][:1]; l=[i for i in logc if s0<=i<=s1][:1]
    e=[x for x in E if s0<=x[0]<=s1]; r=[x for x in Rr if s0<=x[0]<=s1]; w=[x for x in Wr if s0<=x[0]<=s1]
    ref=h[0] if h else (l[0] if l else g[0])
    def fm(x): return f"{x[0]}({x[0]-ref:+d}) {x[1]}f" if x else "-"
    ed="-"
    if e:
        s,L=e[0]; ed=f"{s}({s-ref:+d}) {L}f top+{max(a[i][3] for i in range(s,s+L))-bt:.1f} right+{max(a[i][4] for i in range(s,s+L))-br:.1f} bottom+{max(bot[s:s+L]):.1f}"
    k+=1
    print(f"{k:3d}  {h[0] if h else '-':>6}  {l[0] if l else '-':>6}  {ed:<52} {fm(r[0] if r else None):<16} {fm(w[0] if w else None)}")
print("hits(red runs):",len(Rr)," misses(white runs):",len(Wr)," edge runs:",len(E))
