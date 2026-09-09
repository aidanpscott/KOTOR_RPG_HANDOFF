#!/usr/bin/env python3
"""Parse BG3 'Generated/Data' stat files and RESOLVE the `using` prototype chain.

⚠ An entry that says `using "Target_MainHandAttack"` inherits every field it
does not itself define. Counting raw `data` lines therefore UNDER-COUNTS:
685 of 1,764 spell entries declare no UseCosts of their own and are not free.
"""
import re, glob, collections


def parse(paths):
    ent = {}
    order = []
    for f in paths:
        cur = None
        for ln in open(f, encoding='utf-8', errors='replace'):
            ln = ln.rstrip('\n')
            m = re.match(r'new entry "(.*)"', ln)
            if m:
                cur = {'_name': m.group(1), '_file': f.split('/')[-1], '_own': set()}
                ent[m.group(1)] = cur; order.append(m.group(1)); continue
            if cur is None:
                continue
            m = re.match(r'using "(.*)"', ln)
            if m:
                cur['_using'] = m.group(1); continue
            m = re.match(r'data "([^"]+)" "(.*)"$', ln)
            if m:
                cur[m.group(1)] = m.group(2); cur['_own'].add(m.group(1))
            m = re.match(r'type "(.*)"', ln)
            if m:
                cur['_type'] = m.group(1)
    return ent, order


def resolve(ent, name, field, _seen=None):
    """Value of `field` on `name`, following `using` upward. None if unset."""
    _seen = _seen or set()
    if name in _seen or name not in ent:
        return None
    _seen.add(name)
    e = ent[name]
    if field in e:
        return e[field]
    p = e.get('_using')
    return resolve(ent, p, field, _seen) if p else None


if __name__ == '__main__':
    ent, order = parse(sorted(glob.glob('bg3/Spell_*.txt')))
    print(f'{len(ent):,} spell entries')
    has_using = sum(1 for e in ent.values() if '_using' in e)
    print(f'{has_using:,} declare `using` (inherit from a prototype)')

    own = sum(1 for n in ent if 'UseCosts' in ent[n]['_own'])
    res = sum(1 for n in ent if resolve(ent, n, 'UseCosts') is not None)
    print(f'\nUseCosts declared on the entry itself : {own:,}')
    print(f'UseCosts after resolving inheritance  : {res:,}   (+{res-own})')

    costs = collections.Counter()
    fieldcount = collections.Counter()
    for n in ent:
        for fld in ('UseCosts', 'HitCosts', 'DualWieldingUseCosts', 'RitualCosts'):
            v = resolve(ent, n, fld)
            if v:
                fieldcount[fld] += 1
                for term in v.split(';'):
                    term = term.strip()
                    if term:
                        costs[term.split(':')[0]] += 1
    print('\nentries carrying each cost FIELD (inheritance resolved):')
    for f, c in fieldcount.most_common():
        print(f'   {c:6,}  {f}')
    print(f'\n{len(costs)} distinct cost RESOURCES:')
    for r, c in costs.most_common():
        print(f'   {c:6,}  {r}')
