# score.py — run frames.dart around every traced attack on Onjo and decide each one from the trace's outcome.
import json, bisect, subprocess, csv, io, sys
RUN='/tmp/claude-1000/-mnt-Games-Steam-steamapps-common/30d54131-dd12-490d-938b-a58a67e13c5c/scratchpad/proof/run'
video=sys.argv[1] if len(sys.argv)>1 else 'take1.mkv'
PTS=f'{RUN}/pts-{video}.txt'
pts=[float(l) for l in open(PTS)]
tr=[json.loads(l) for l in open(f'{RUN}/trace-{video}.jsonl')]
PRE,POST=20,90
out=[]
for n,e in enumerate(tr,1):
    t=e['us']/1e6
    k=bisect.bisect_left(pts,t)
    cache=f'{RUN}/ev-{video}-{n:02d}.csv'
    import os
    class R: pass
    r=R()
    if os.path.exists(cache): r.stdout=open(cache).read()
    else: r=subprocess.run([f'{RUN}/frames',f'{RUN}/{video}',PTS,str(k-PRE),str(PRE+POST)],capture_output=True,text=True,cwd='/mnt/Games/Steam/steamapps/common/KOTOR_APP_PROJECT/KOTOR-RPG-APP')
    if not os.path.exists(cache): open(cache,'w').write(r.stdout)
    rows=list(csv.DictReader(io.StringIO(r.stdout)))
    for i,x in enumerate(rows): x['k']=k-PRE+i
    pre=[x for x in rows if x['k']<k]; post=[x for x in rows if x['k']>=k]
    bf=max(float(x['flash']) for x in pre); bn=max(int(x['num']) for x in pre); bm=max(int(x['miss']) for x in pre)
    def first(cond):
        return next((x['k'] for x in post if cond(x)),None)
    hp=first(lambda x: float(x['hp'])>0.5)
    # ⚠ ABSOLUTE AND RELATIVE: the board's own green edge sat in the band until the status line grew (first attack), and leaving
    # it moved the band from -4 to 0. Red over black reads 30+ on a real flash's first frame.
    fl=first(lambda x: float(x['flash'])>max(5,bf+3))
    nu=first(lambda x: int(x['num'])>=bn+8)
    mi=first(lambda x: int(x['miss'])>=bm+8)
    # the largest capture gap within 3 frames either side of the HP (or miss) frame: a dropped frame could merge two moments
    ref=hp if e['hit'] else mi
    gap=None
    if ref is not None:
        gap=round(max(pts[j+1]-pts[j] for j in range(ref-3,ref+3))*1000)
    out.append(dict(n=n,hit=e['hit'],amt=e['amount'],k=k,hp=hp,flash=fl,num=nu,miss=mi,lag_ms=None if ref is None else round((pts[ref]-t)*1000),gap_ms=gap))
    o=out[-1]
    if e['hit']: ok = hp is not None and hp==fl==nu and mi is None
    else: ok = mi is not None and fl is None and nu is None and hp is None
    o['verdict']='PASS' if ok else 'FAIL'
    print(o,flush=True)
json.dump(out,open(f'{RUN}/score-{video}.json','w'))
