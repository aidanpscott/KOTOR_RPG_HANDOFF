#!/usr/bin/env python3
"""temporal_classify.py - the classifier behind the Atlas's date figures.

SHIPPED BECAUSE THE NUMBER IS A RELAY AND THIS IS NOT. Under METHOD-RECORD-01
1.5, reconstructing a classification from its reported total is exactly the
failure the rule describes. Run this and get your own numbers.

    python3 tools/temporal_classify.py
    python3 tools/temporal_classify.py --band change

--------------------------------------------------------------------------
v2. THREE DEFECTS FIXED, ALL FOUND BY THE LIBRARY IN LIBRARY-30, PLUS A
PORTABILITY FAILURE THAT MADE v1 UNRUNNABLE OUTSIDE MY CONTAINER.

v1 DID NOT RUN FROM A FRESH CLONE - sys.path was hardcoded to an absolute
path, and resolve.py and m_d.py opened /home/claude/reg/selection.json. A TOOL
SHIPPED TO BREAK A RELAY THAT ONLY RUNS ON THE SHIPPER'S MACHINE IS STILL A
RELAY: the recipient must take its output on trust, which is the whole thing
it was written to avoid. All paths now derive from __file__.

DEFECT 1 - NEGATIVE-EXISTENCE GUARDS WERE LANDING IN `change`. GUARD matched
only "excluded as event", "lies after us" and kin. The Atlas also guards by
saying a thing DOES NOT EXIST YET: Bespin "NOT YET COLONISED IN THIS PERIOD",
Nam Chorios "NOBODY LIVES HERE AT 3956", Taanab "NOT COLONISED UNTIL 2320
BBY", Eres "ARE NOT BUILT UNTIL c.200 BBY", Nubia "does not exist yet".
THE LIBRARY IS RIGHT AND THESE ARE GUARDS. A sentence whose content is "this
had not happened yet at the campaign date" tells a GM what NOT to use. It is
the same instruction as an exclusion, phrased from the other end of time.

DEFECT 2 - SOURCE REFUSALS HAD NO BAND AT ALL. Athiss "REFUSED, fourth time
this session: a roleplaying club's wiki gives..." and Duro "Also refused,
below rank" are neither guards nor state changes. They are SOURCE-DISCIPLINE
records - material seen and declined - and they were falling into `change` on
incidental verbs. New `refusal` band, tested FIRST because a refusal usually
quotes the very material it refuses.

DEFECT 3 - CROSS-REFERENCED SENTENCES COUNTED ONCE PER WORLD. Page-sweep puts
the same quoted sentence into several entries; Taanab's Krath sentence sits in
Taanab, Empress Teta and Onderon. As a COUNT OF CLAIMS that is double-counting;
as a count of PLACES A GM MIGHT READ IT, it is correct. BOTH ARE NOW REPORTED
AND NEITHER IS CALLED "THE" FIGURE.

--------------------------------------------------------------------------
WHICH FILES THIS READS - see decisions/D-CURRENCY-01.md. The Atlas corpus is
SIX NAMED MODULES, not the directory holding them, not worlds/*.md, and not
data/teaching_menus__SUPERSEDED-EXPORT-PRE-PT552.json.
"""

import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
for _p in (os.path.join(_HERE, "menus"), _HERE):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import resolve  # noqa: E402

DATE = re.compile(r"\b\d{1,2},?\d{3}\s*BBY\b|\b\d{1,4}\s*(?:BBY|ABY)\b")

REFUSAL = re.compile(
    r"\brefused\b|not published material|roleplay(?:ing)?[- ]club"
    r"|is not a source|standing refusals|however plausible it looks",
    re.I,
)

GUARD = re.compile(
    r"excluded as event|lies (?:far )?after us|is excluded|EXCLUDED"
    r"|after our date|before our date|lie after us"
    r"|not yet colonis|nobody lives here|no one lives here"
    r"|does not exist yet|do not exist yet|did not exist yet"
    r"|are not built until|is not built until|not colonis\w* until"
    r"|has not been built|nobody has colonised|not settled until",
    re.I,
)

CHANGE = re.compile(
    r"\bconquer|\bsack(?:ed)?\b|\bdestroy|\bfound(?:ed)?\b|\bcolonis"
    r"|\bannex|\btook\b|\bfell\b|\bjoined\b|\bbuilt\b|\bglass(?:ed)?\b"
    r"|\bliberat|\bbesieg|\babandon|\brenamed\b|\bseized\b",
    re.I,
)

BANDS = ("refusal", "guard", "change", "context")
LABELS = {
    "refusal": "source refusals - NOT records",
    "guard": "era guards - NOT records",
    "change": "state changes - C03-shaped",
    "context": "context/provenance - NOT records",
}


def classify():
    """{band: [(world, sentence)]}. ORDER OF TESTS IS LOAD-BEARING."""
    A = resolve.menus()
    out = {b: [] for b in BANDS}
    for world, strata in sorted(A.items()):
        for stratum in strata:
            for sentence in re.split(r"(?<=[.!?]) ", stratum[2]):
                if not DATE.search(sentence):
                    continue
                if REFUSAL.search(sentence):
                    band = "refusal"
                elif GUARD.search(sentence):
                    band = "guard"
                elif CHANGE.search(sentence):
                    band = "change"
                else:
                    band = "context"
                out[band].append((world, " ".join(sentence.split())))
    return out


def report():
    c = classify()
    A = resolve.menus()
    raw = len(DATE.findall(" ".join(y[2] for st in A.values() for y in st)))
    print(f"  corpus {len(A)} worlds - raw date occurrences {raw}\n")
    for b in BANDS:
        uniq = len(set(s for _, s in c[b]))
        dup = len(c[b]) - uniq
        note = f"   ({uniq} distinct + {dup} cross-referenced)" if dup else ""
        print(f"  {LABELS[b]:34s} {len(c[b]):>4d}{note}")
    print()
    print("  SENTENCE counts against an OCCURRENCE total. One sentence can carry")
    print("  two dates, so these do not sum to the raw figure.")
    print("  NO SINGLE NUMBER HERE IS 'THE' FIGURE. The change band counted by")
    print("  claim and by place-a-GM-reads-it differ, and both are true.")
    return c


if __name__ == "__main__":
    c = report()
    if "--band" in sys.argv:
        b = sys.argv[sys.argv.index("--band") + 1]
        print(f"\n=== BAND: {b} ===\n")
        for world, sentence in c[b]:
            print(f"{world}\t{sentence}")
