#!/usr/bin/env python3
"""check_landed.py — find rulings that CHANGED something and never reached the rules.

⚠ WHY. Five instances are on record of a ruling living in a reply or a findings
document and not in the rules a reader consults — PT-88, PT-118, PT-139, PT-140,
PT-190. Check 17 catches IDs that are cited but unwritten. It cannot catch a
ruling that was made, reasoned, applied, and never registered anywhere.

⚠ AND WHY IT FILTERS. The naive version — "every PT with no trace" — returns 56
of 185, which is 30% and unreadable. Most of those are confirmations, and a
confirmation has nothing to land. A check that reports things needing no action
is one people learn to skim; that lesson is PT-173's.

Filtered to rulings whose own text says they changed something, it returns 10.
"""
import re, glob, os, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else 'docs'
log = open(os.path.join(ROOT, 'PLAYTEST-RULINGS-01.md'), errors='ignore').read()
docs = {os.path.basename(p): open(p, errors='ignore').read()
        for p in glob.glob(os.path.join(ROOT, '*.md')) if 'PLAYTEST-RULINGS' not in p}

CHANGES = re.compile(r'\b(Ruled|Authored|Corrected|Cut\b|Replaced|Added|Renamed|'
                     r'Reversed|Withdrawn|supersede)', re.I)
CONFIRMS = re.compile(r'\b(Confirmed|No change|Vacuous|Stands unchanged|Verified, no)', re.I)

missing = []
for b in re.split(r'\n## PT-', log)[1:]:
    m = re.match(r'(\d{1,3})', b)
    if not m:
        continue
    i, head = int(m.group(1)), b[:400]
    if CONFIRMS.search(head) and not CHANGES.search(head):
        continue                      # a confirmation has nothing to land
    if not CHANGES.search(head):
        continue                      # only changes must leave a trace
    if not any(('PT-%d' % i) in t for t in docs.values()):
        missing.append((i, b.split('\n')[0].strip()[:70]))

print("rulings that changed something and left no trace in any rules document: %d"
      % len(missing))
for i, t in missing:
    print("  PT-%-5d %s" % (i, t))
print("\n(a ruling is 'landed' when its ID is cited in the document it governs.\n"
      " citing the ID is the cheap part — it is what makes this checkable at all.)")
sys.exit(1 if missing else 0)
