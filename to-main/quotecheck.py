"""quotecheck.py - does a menu NAMED IN PROSE match the menu the entry HOLDS?

Sixth member of the family, and the first about QUOTATION rather than LOCATION.
Found by D-URKUPP-01: the INELIG record for Urkupp names its legacy menu as
'Scavenging - Stealth - Intimidate' while the corpus held four skills, two of
them different. Survival was the tell - readmitted at PT-552, so the live menu
changed and the prose describing it never did.

NOTHING ELSE CHECKS THIS. validate.py tests skills against the vocabulary,
menus against the selection, and heads against bodies. IT HAS NO WAY TO KNOW
THAT A SENTENCE NAMING THREE SKILLS DISAGREES WITH A LIST HOLDING FOUR.

Scope: entry prose in the six governing modules, plus every INELIGIBLE/INELIG
dict reachable from them. Reports, does not fix.
"""
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (_HERE, '/home/claude/b1', '/home/claude/b2', '/home/claude/menu'):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import resolve  # noqa: E402

MODULES = ('menus', 'menus2', 'm_a', 'm_b', 'm_c', 'm_d')
# separators seen in this corpus: middle dot, comma, slash, the word 'and'
SEP = r'\s*(?:\u00b7|,|/|\band\b)\s*'


def _vocab():
    A = resolve.menus()
    v = set(s for st in A.values() for y in st for s in y[1])
    # skills whose only live use was removed still need recognising in prose
    v |= {'Scavenging', 'Awareness', 'Survival', 'Athletics', 'Intimidate',
          'Stealth', 'Alertness', 'Persuade'}
    return v


def scan():
    import importlib
    A = resolve.menus()
    V = _vocab()
    names = '|'.join(sorted((re.escape(x) for x in V), key=len, reverse=True))
    pat = re.compile(r'(?<![A-Za-z])((?:%s)(?:%s(?:%s)){2,})(?![A-Za-z])' % (names, SEP, names))

    def quoted_in(text):
        out = []
        for m in pat.finditer(text):
            parts = [x.strip(' *_') for x in re.split(SEP, m.group(1))]
            parts = [x for x in parts if x in V]
            if len(parts) >= 3:
                out.append(parts)
        return out

    findings = []
    # 1. entry prose against its own menu
    for w, strata in sorted(A.items()):
        for label, skills, text in strata:
            for q in quoted_in(text):
                if skills and set(q) != set(skills):
                    findings.append(('entry', w, q, list(skills)))
    # 2. INELIGIBLE dicts against the entry they describe
    seen = {}
    for mod in MODULES:
        try:
            m = importlib.import_module(mod)
        except ImportError:
            continue
        for attr in ('INELIGIBLE', 'INELIG'):
            for w, txt in (getattr(m, attr, None) or {}).items():
                seen[w] = str(txt)
    for w, txt in sorted(seen.items()):
        k = resolve.key(w, A)
        live = list(A[k][0][1]) if k else []
        for q in quoted_in(txt):
            if set(q) != set(live):
                findings.append(('INELIG', w, q, live))
    return findings


# A quoted menu may legitimately disagree with the live one. Three shapes so far,
# and only the first is a defect:
#   STALE   the prose recorded a decision that was later overturned. Nar Kreeta
#           refused a Swim slot; D-EXCEPT-01 admitted it; the sentence stayed.
#           KEPT ON PURPOSE - it is why D-EXCEPT-01 exists - so the check must
#           keep firing and the entry must say why.
#   PARTIAL the prose explains SOME members of a menu as a rationale group.
#           Trandosha names three and then says "Scavenging kept" in the next
#           clause. NOT A QUOTATION OF THE MENU AT ALL.
#   REMOVED the entry is ineligible and its menu is now empty by D-MAL-01, so
#           any quoted legacy menu differs by construction. Urkupp.
#
# ACKNOWLEDGED, NOT SUPPRESSED. An entry naming this constant has been read and
# ruled on; the check still reports it, and the count of unreviewed ones is what
# matters. SUPPRESSION WOULD MAKE THE NEXT ONE INVISIBLE, WHICH IS THE FAMILY
# THIS CHECK EXISTS TO CATCH.
ACKNOWLEDGED = {
    "Nar Kreeta": "STALE - refusal overturned by D-EXCEPT-01, sentence kept as the reason it exists",
    "Trandosha": "PARTIAL - prose explains three of four, 'Scavenging kept' follows",
    "Urkupp": "REMOVED - menu emptied under D-MAL-01, legacy list withdrawn by D-URKUPP-01",
}


def report():
    f = scan()
    new = [x for x in f if x[1] not in ACKNOWLEDGED]
    if not f:
        print("  quoted_menus         clean")
        return f
    tag = "   <-- PROBLEM" if new else ""
    print(f"  quoted_menus         {len(new)} unreviewed, {len(f) - len(new)} acknowledged{tag}")
    for where, w, q, live in (new or []):
        print(f"   [{where}] {w}")
        print(f"       prose names : {q}")
        print(f"       entry holds : {live or '(empty - menu removed)'}")
    return f


if __name__ == "__main__":
    report()
