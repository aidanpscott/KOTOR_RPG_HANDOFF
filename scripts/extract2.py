"""Extraction run 2: skills (26) and class skill lists (14 standard + 6 Force).

⚠ PARSING NOTE. The SKILLS-01 §1 master table is INTERRUPTED by prose at lines
49-52 and resumes at line 53. A parser that reads *consecutive* rows stops at
line 48 and silently loses Swim and Xenology. This one collects every table row
within a bounded line window instead, and asserts the expected count.
"""
import json, re, hashlib, sys, os

REF = ('/tmp/claude-1001/-mnt-ga-SteamLibrary-steamapps-common/'
       'fe58f391-547f-4b93-ac84-96c2992c43d8/scratchpad/handoff/STUDY/_reference/')
SK = 'STUDY/_reference/SKILLS-01.md'
FC = 'STUDY/_reference/CLASSES-FORCE-PHB.md'

ATTR = {'Str': 'Strength', 'Dex': 'Dexterity', 'Con': 'Constitution',
        'Int': 'Intelligence', 'Wis': 'Wisdom', 'Cha': 'Charisma'}


def load(rel):
    p = REF + os.path.basename(rel)
    b = open(p, 'rb').read()
    return b.decode('utf-8').split('\n'), hashlib.md5(b).hexdigest()


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def bold(s):
    return re.sub(r'\*\*', '', s).strip()


def rows_in(lines, lo, hi):
    """Every markdown table row between 1-indexed lo..hi, interruptions skipped."""
    out = []
    for i in range(lo - 1, min(hi, len(lines))):
        l = lines[i]
        if l.startswith('|') and not re.match(r'^\|[\s:\-|]+\|?$', l):
            out.append((i + 1, l))
    return out


sk_lines, sk_md5 = load(SK)
fc_lines, fc_md5 = load(FC)
h1 = next(l for l in sk_lines if l.startswith('## 1.'))

FP_SK = {'file': SK, 'md5': sk_md5, 'md5_short': sk_md5[:8],
         'lines': len(sk_lines) - 1, 'section_1_heading': h1.lstrip('# ').strip()}
FP_FC = {'file': FC, 'md5': fc_md5, 'md5_short': fc_md5[:8],
         'lines': len(fc_lines) - 1}

print('=== SOURCE FINGERPRINTS ===')
print('  %s  md5 %s  %d lines' % (SK, FP_SK['md5_short'], FP_SK['lines']))
print('     §1: %s' % FP_SK['section_1_heading'])
print('  %s  md5 %s  %d lines' % (FC, FP_FC['md5_short'], FP_FC['lines']))
print('  manifest expects e157dea6/735 and ebc82531/222 -> %s'
      % ('MATCH' if FP_SK['md5_short'] == 'e157dea6' and FP_SK['lines'] == 735
         and FP_FC['md5_short'] == 'ebc82531' and FP_FC['lines'] == 222 else '*** MISMATCH ***'))

# ---------------------------------------------------------------- RUN 1
master = rows_in(sk_lines, 25, 54)          # §1 table window (header at 23-24)
desc_rows = rows_in(sk_lines, 708, 733)     # Descriptions table

DESC = {}
for ln, raw in desc_rows:
    c = cells(raw)
    DESC[bold(c[0])] = (ln, re.sub(r'\s+', ' ', c[1]).strip())

skills = []
for ln, raw in master:
    c = cells(raw)
    name = bold(c[0])
    key = c[1].strip()
    cons = c[3] if len(c) > 3 else ''
    beast = 'BEAST ONLY' in cons.upper()
    d = DESC.get(name)
    skills.append({
        'id': re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-'),
        'name': name,
        'attribute': ATTR.get(key),
        'description': d[1] if d else None,
        'beast_only': beast,
        'source': '%s:%d' % (SK, ln) if not d else '%s:%d,%d' % (SK, ln, d[0]),
    })

print('\n=== RUN 1 — SKILLS ===')
print('  master-table rows read      : %d  (lines %d..%d, interruption at 49-52 skipped)'
      % (len(master), master[0][0], master[-1][0]))
print('  records                     : %d' % len(skills))
char = [s for s in skills if not s['beast_only']]
beast = [s for s in skills if s['beast_only']]
print('  character skills            : %d' % len(char))
print('  beast-only                  : %d  -> %s' % (len(beast), [s['name'] for s in beast]))
nodesc = [s['name'] for s in skills if not s['description']]
print('  descriptions populated      : %d of %d' % (len(skills) - len(nodesc), len(skills)))
if nodesc:
    print('  *** EMPTY DESCRIPTIONS: %s ***' % nodesc)
print('  unique ids / names          : %d / %d'
      % (len(set(s['id'] for s in skills)), len(set(s['name'] for s in skills))))
print('  null attributes             : %s'
      % [s['name'] for s in skills if s['attribute'] is None])

# diff by NAME, master table vs descriptions table
mnames = set(s['name'] for s in skills)
dnames = set(DESC)
print('  ⚠ DIFF BY NAME, master vs descriptions:')
print('     in master not in descriptions: %s' % sorted(mnames - dnames))
print('     in descriptions not in master: %s' % sorted(dnames - mnames))

# ---------------------------------------------------------------- RUN 2
std_rows = rows_in(sk_lines, 350, 363)
classes = []
for ln, raw in std_rows:
    c = cells(raw)
    nm = bold(c[0])
    sk = [s.strip() for s in bold(c[2]).split('·') if s.strip()]
    classes.append({'id': re.sub(r'[^a-z0-9]+', '-', nm.lower()).strip('-'),
                    'name': nm, 'category': 'standard', 'skills': sk,
                    'declared_count': int(c[1]) if c[1].isdigit() else None,
                    'source': '%s:%d' % (SK, ln)})

# Force classes: read CLASSES-FORCE-PHB, then verify against §9.2
force = []
for i, l in enumerate(fc_lines):
    if l.strip() == '## Class skills':
        # class name is the nearest preceding '# Name'
        nm = None
        for j in range(i, -1, -1):
            m = re.match(r'^# ([A-Za-z ]+)$', fc_lines[j])
            if m:
                nm = m.group(1).strip()
                break
        for j in range(i + 1, min(i + 5, len(fc_lines))):
            if fc_lines[j].strip().startswith('**'):
                sk = [s.strip() for s in bold(fc_lines[j]).split('·') if s.strip()]
                force.append({'name': nm, 'skills': sk, 'line': j + 1})
                break

# §9.2 Force entries, for the agreement check
s92 = {}
for i in range(264, 342):
    m = re.match(r'^\*\*((?:Jedi|Sith) \w+) — (\d+)\*\*$', sk_lines[i].strip())
    if m:
        s92[m.group(1)] = ([s.strip() for s in sk_lines[i + 1].split('·') if s.strip()], i + 1)

print('\n=== RUN 2 — CLASS SKILL LISTS ===')
print('  standard classes from §9.2b : %d  (lines %d..%d)'
      % (len(std_rows), std_rows[0][0], std_rows[-1][0]))
bad = [c['name'] for c in classes if c['declared_count'] != len(c['skills'])]
print('  declared # vs actual length : %s' % ('all agree' if not bad else 'MISMATCH %s' % bad))
print('  Force classes from PHB      : %d' % len(force))
print('  ⚠ AGREEMENT CHECK, CLASSES-FORCE-PHB vs SKILLS-01 §9.2:')
agree = True
for f in force:
    a = s92.get(f['name'])
    if a is None:
        print('     %-16s *** not found in §9.2 ***' % f['name']); agree = False; continue
    same = a[0] == f['skills']
    if not same:
        agree = False
        print('     %-16s DIFFER  phb=%s  §9.2=%s' % (f['name'], f['skills'], a[0]))
    else:
        print('     %-16s AGREE (%d skills)  phb:%d  §9.2:%d' % (f['name'], len(f['skills']), f['line'], a[1]))
print('     -> %s' % ('ALL SIX AGREE EXACTLY' if agree else '*** DISAGREEMENT ***'))

for f in force:
    classes.append({'id': re.sub(r'[^a-z0-9]+', '-', f['name'].lower()).strip('-'),
                    'name': f['name'], 'category': 'force', 'skills': f['skills'],
                    'declared_count': len(f['skills']),
                    'source': '%s:%d' % (FC, f['line'])})

# every class skill must be one of the 25 CHARACTER skills
charnames = set(s['name'] for s in char)
unknown = {}
for c in classes:
    for s in c['skills']:
        if s not in charnames:
            unknown.setdefault(s, []).append(c['name'])
print('  ⚠ class skills not in the 25 character skills: %s'
      % (unknown if unknown else 'NONE — all resolve'))
print('  Fly appears on any class list: %s'
      % any('Fly' in c['skills'] for c in classes))

if len(skills) != 26 or len(char) != 25 or len(beast) != 1 or nodesc \
        or len(std_rows) != 14 or len(force) != 6 or not agree or unknown:
    print('\n*** A CHECK FAILED — NOT WRITING ***')
    sys.exit(1)

OUT = ('/tmp/claude-1001/-mnt-ga-SteamLibrary-steamapps-common/'
       'fe58f391-547f-4b93-ac84-96c2992c43d8/scratchpad/handoff/data/extracted/')
json.dump({'source': FP_SK, 'count': len(skills),
           'character_skills': len(char), 'beast_only': len(beast),
           'records': skills},
          open(OUT + 'skills.json', 'w'), indent=2, ensure_ascii=False)
open(OUT + 'skills.json', 'a').write('\n')
json.dump({'sources': [FP_SK, FP_FC],
           'section_extracted': 'SKILLS-01 §9.2b, lines 350-363 (standard); '
                                'CLASSES-FORCE-PHB (force)',
           'counts': {'standard': 14, 'force': 6, 'prestige': 0},
           'prestige_note': 'Prestige classes have no skill lists in any source. '
                            'Open design question — deliberately not synthesised.',
           'classes': classes},
          open(OUT + 'class-skills.json', 'w'), indent=2, ensure_ascii=False)
open(OUT + 'class-skills.json', 'a').write('\n')
print('\nWROTE skills.json and class-skills.json')
