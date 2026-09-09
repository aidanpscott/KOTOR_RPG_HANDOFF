#!/usr/bin/env python3
"""sync_docs.py — copy every changed working file into handoff/docs/.

⚠ PT-245. For eight files the designer was reading a version older than the
rules, and two agents spent three exchanges arguing about a gating figure
that was correct in the repo and stale in docs/.

Copying by hand meant copying only the files I remembered touching.
This copies by comparison.
"""
import os, glob, hashlib, shutil, sys

# PT-1463 - both paths were wrong and it printed a match anyway.
#   DOCS pointed at handoff/handoff/docs, which does not exist, so the glob
#   returned nothing and the loop never ran.
#   src looked for the file at ROOT, and sources live in rules/ design/ playtest/.
ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, 'docs')

CANDIDATES = ['../KOTOR_RPG_MAIN_WORK', '../MAIN_WORK', '../main']
SRC = None
for c in CANDIDATES:
    t = os.path.normpath(os.path.join(ROOT, c))
    if os.path.isdir(os.path.join(t, 'rules')):
        SRC = t
        break

SUBDIRS = ['rules', 'design', 'playtest', 'force', '.']

def h(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()

def find(name):
    for d in SUBDIRS:
        p = os.path.join(SRC, d, name)
        if os.path.exists(p):
            return p
    return None

docs = sorted(glob.glob(os.path.join(DOCS, '*.md')))

# PT-1451 - a script that examined NOTHING must not report success.
if SRC is None or not docs:
    print('  CANNOT RUN - this has NOT looked and is reporting nothing,')
    print('     not finding nothing. SRC=%s, %d doc(s) found.' % (SRC, len(docs)))
    raise SystemExit(2)

changed, missing = [], []
for d in docs:
    n = os.path.basename(d)
    src = find(n)
    if src is None:
        missing.append(n)
        continue
    if h(src) != h(d):
        shutil.copy2(src, d)
        changed.append(n)

print("  %d of %d file(s) refreshed in docs/" % (len(changed), len(docs)))
for c in changed:
    print("    %s" % c)
if missing:
    print("  WARNING - %d doc(s) have no source in the tree:" % len(missing))
    for m in missing:
        print("    %s" % m)
if not changed and not missing:
    print("  docs/ matches the working tree - %d file(s) compared" % len(docs))
