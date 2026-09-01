#!/usr/bin/env python3
"""temporal_classify.py — the classifier behind the 750 / 121 figures.

SHIPPED BECAUSE THE NUMBER IS A RELAY AND THIS IS NOT. Under METHOD-RECORD-01
§1.5, reconstructing a classification from its reported total is exactly the
failure the rule describes. Run this and get your own numbers.

⚠⚠ WHY THE LIBRARY COULD NOT REPRODUCE 750 FROM THE MARKDOWN

The Atlas's live text is NOT in worlds/*.md. It is in the Python menu modules
under tools/menus/, which is what every Atlas tool reads via resolve.menus().

    live menu objects (tools/menus/*.py)   1,150,136 chars · 297 worlds · 750 dates
    worlds/*.md                                                            327 dates
    all markdown, 131 files                1,604,373 bytes

The markdown files are the BATCH RECORD of how entries were written. The menu
modules are the ENTRIES. They diverged the moment expansion began appending to
the modules rather than rewriting the batches.

⚠⚠⚠ THIS IS THE teaching_menus.json VERSUS MENUS-BATCH-* CURRENCY QUESTION,
arriving in a third form. Two records of the same thing, disagreeing on
coverage, and WHICH GOVERNS HAS NEVER BEEN STATED. For the Atlas it is the
menu modules, and this file is the first place that has been written down.
"""

import re
import sys

sys.path.insert(0, "/home/claude/menu")   # or tools/menus in a fresh clone
import resolve

DATE = re.compile(r"\b\d{1,2},?\d{3}\s*BBY\b|\b\d{1,4}\s*(?:BBY|ABY)\b")

# An era guard. Content is "a GM must not use this date", which is a statement
# about admissibility, not a temporal record.
GUARD = re.compile(
    r"excluded as event|lies (?:far )?after us|is excluded|EXCLUDED"
    r"|after our date|before our date|lie after us",
    re.I,
)

# A dated state change: something was one way and then another. This is the
# only class matching C03's record shape, which carries before: and after:.
CHANGE = re.compile(
    r"\bconquer|\bsack(?:ed)?\b|\bdestroy|\bfound(?:ed)?\b|\bcolonis"
    r"|\bannex|\btook\b|\bfell\b|\bjoined\b|\bbuilt\b|\bglass(?:ed)?\b"
    r"|\bliberat|\bbesieg|\babandon|\brenamed\b|\bseized\b",
    re.I,
)


def classify():
    A = resolve.menus()
    out = {"guard": [], "change": [], "context": []}
    for world, strata in sorted(A.items()):
        for stratum in strata:
            for sentence in re.split(r"(?<=[.!?]) ", stratum[2]):
                if not DATE.search(sentence):
                    continue
                if GUARD.search(sentence):
                    bucket = "guard"
                elif CHANGE.search(sentence):
                    bucket = "change"
                else:
                    bucket = "context"
                out[bucket].append((world, " ".join(sentence.split())))
    return out


def report():
    c = classify()
    A = resolve.menus()
    total = len(DATE.findall(" ".join(y[2] for st in A.values() for y in st)))
    print(f"  worlds                     {len(A)}")
    print(f"  raw date occurrences       {total}")
    print()
    for k, label in (("guard", "era guards — NOT records"),
                     ("change", "state changes — C03-shaped"),
                     ("context", "context/provenance — NOT records")):
        print(f"  {label:34s} {len(c[k]):>4d}")
    print()
    print("  ⚠ These are SENTENCE counts and the raw figure is OCCURRENCE count.")
    print("    One sentence can carry two dates. They will not sum to the total")
    print("    and are not meant to.")
    return c


if __name__ == "__main__":
    c = report()
    if "--enumerate" in sys.argv:
        print("\n=== THE C03-SHAPED SUBSET, IN FULL ===\n")
        for world, sentence in c["change"]:
            print(f"{world}\t{sentence}")
