#!/usr/bin/env python3
"""sync_docs.py — copy every changed working file into handoff/docs/.

⚠ PT-245. For eight files the designer was reading a version older than the
rules, and two agents spent three exchanges arguing about a gating figure
that was correct in the repo and stale in docs/.

Copying by hand meant copying only the files I remembered touching.
This copies by comparison.
"""
import os, glob, hashlib, shutil, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, 'handoff', 'docs')

def h(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()

changed = []
for d in sorted(glob.glob(os.path.join(DOCS, '*.md'))):
    n = os.path.basename(d)
    src = os.path.join(ROOT, n)
    if os.path.exists(src) and h(src) != h(d):
        shutil.copy2(src, d)
        changed.append(n)

print(f"  {len(changed)} file(s) refreshed in docs/")
for c in changed:
    print(f"    {c}")
if not changed:
    print("  docs/ matches the working tree")
