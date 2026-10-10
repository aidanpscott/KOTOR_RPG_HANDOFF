import json,sys
v=sys.argv[1]; o=json.load(open(f'score-{v}.json'))
for kind in ('hit','miss'):
    s=[x for x in o if x['hit']==(kind=='hit')]
    print(v,kind,len(s),'PASS',sum(x['verdict']=='PASS' for x in s),'FAIL',[x['n'] for x in s if x['verdict']!='PASS'])
for x in o:
    if x['hit']:
        d=lambda a: None if a is None or x['hp'] is None else a-x['hp']
        print('  hit',x['n'],'-%s'%x['amt'],'flash-hp',d(x['flash']),'num-hp',d(x['num']),'lag',x['lag_ms'],'gap',x['gap_ms'],x['verdict'])
