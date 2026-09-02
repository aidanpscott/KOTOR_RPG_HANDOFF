# `F-INDEX` — every finding in this repository, and whether anyone has been told

**Written 2026-09-01, after `F-OVERLAP-01` sat here for nine days.**

> ### **Filing is not sending.** *`F-OVERLAP-01` was correct on 24 August, carried a measurement nobody else had, and waited until 1 September because it was in the wrong place to be acted on.*

**Main names this the eighth failure shape.** ⟡ *The seven before it were things that returned less than the truth. **This one returns the truth to a place nobody is looking.***

---

## ⚠⚠⚠ Measured: **twelve findings, ~49,000 characters, never named in a message to anyone**

    F-ORD-CRUSADE        14,500ch   the Ords are crusade infrastructure
    F-SITH-ROADS          4,750ch   the road map of Sith space, and why sixteen worlds should stay blocked
    F-SITH-EMPTY          3,526ch
    F-ZIOST-REFINE        3,483ch
    F-KORRIBAN-REFINE     3,374ch
    F-STEREOTYPE          3,301ch   the menus default to the tier's cliche whenever the world is thin
    F-WORTANDELL          3,001ch
    F-ORD-NETWORK         2,961ch
    F-BLOCK-TRIAGE-2      2,852ch
    F-CALDERA             2,821ch
    F-TION                2,469ch
    F-WONDERS             2,416ch   the Twenty Wonders of the Galaxy, three of them already mine

**Four findings have been named in a handoff message. Sixteen exist.**

### Two of those twelve are not world notes at all

**`F-STEREOTYPE`** — *"the menus default to the tier's cliché whenever the world is thin… derived from a floor-distribution count across all 292 menus… **it is the same failure three times and I only saw it the third**."* ⟡ **That is a systemic finding about my own method, and no other agent has ever seen it.**

**`F-WONDERS`** — *a **canonical closed list of twenty destinations**, three already in the selection.* ⟡ **That is selection input, and the selection has been ruled on twice this week without it.**

---

## The rule this establishes

**A finding is not delivered when it is written. It is delivered when it is named to someone who can act on it.**

⚠ **And the failure is invisible from inside the repository**, because the file exists, the content is correct, and every check passes. ⟡ *`validate.py` cannot see it. `quotecheck.py` cannot see it. **Nothing can see it except a diff between what was written and what was said.***

**That diff is what this index is.** ✅ *Regenerate it with:*

    grep -L -F -f <(ls worlds/F-*.md | xargs -n1 basename | sed 's/.md$//') \
         handoff-messages/*.md

*or more simply: for each `worlds/F-*.md`, ask whether its name appears in anything sent.*

---

## ⚠ And a false start, recorded because it is the same lesson

**My first attempt at this measured *"files containing a pending-style marker."*** ⟡ *It returned **40 of 55**, because decision files legitimately contain the words `OPEN`, `unresolved` and `flagged, not fixed` as **content**.*

**`PT-917` measured Main's checks at a ~95% false-positive rate. I nearly shipped one at the same rate, one message after quoting that figure approvingly.** ⟡ **The question was wrong, not the threshold: "which files look pending" is a different question from "which findings were never sent."**
