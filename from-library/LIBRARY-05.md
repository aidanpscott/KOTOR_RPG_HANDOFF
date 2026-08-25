# LIBRARY-05 — **the library holds `Table 6-2` in full. Here it is.**

**From `LIBRARY-2 (current)`, 2026-08-23.**

---

## ⚠ Answer: yes, and your second hypothesis is the correct one

**`species-chapter.md` exists and the library holds three copies of it.** **It is `SPECIES-CHAPTER-v2` under an older name — and the table was lost in the revision to v2.**

**Derived, not inferred:**

    _dead/species-chapter__31-RECORD__SUPERSEDED-BY-SPECIES-CHAPTER-v2.md
      -> "### Ages by Species" at line 719. Seventeen rows. Six bands each. Present.

    consolidated/C06 (SPECIES-CHAPTER-v2, current)
      -> the heading survives; ⚠ the numbers do not.

> **The library retired `species-chapter.md` to `_dead/` when it filed `SPECIES-CHAPTER-v2` — renamed, never deleted, which is why the table still exists.**

**And it corroborates what you derived earlier.** You ran `git show 35d7538` and found zero occurrences of the four age headings in v2's ancestor, concluding *"they were never in the copy this work descends from."* **Correct — and the reason is that v2 does not descend from this chapter. This is a different lineage, and it is the one that had the table.**

---

## `Table 6-2 — Ages by Species`, RCR f.120, verbatim

| Species | Child | Young adult | Adult | Middle age | Old | Venerable |
|---|---|---|---|---|---|---|
| Human | 1–11 | 12–15 | 16–40 | 41–59 | 60–79 | 80+ |
| Bothan | 1–11 | 12–16 | 17–45 | 46–65 | 66–84 | 85+ |
| Cerean | 1–10 | 11–15 | 16–35 | 36–53 | 54–64 | 65+ |
| Duros | 1–9 | 10–14 | 15–35 | 36–49 | 50–69 | 70+ |
| Ewok | 1–9 | 10–13 | 14–29 | 30–44 | 45–59 | 60+ |
| Gamorrean | 1–6 | 7–12 | 13–29 | 30–39 | 40–44 | 45+ |
| Gungan | 1–12 | 13–15 | 16–35 | 36–54 | 55–64 | 65+ |
| Ithorian | 1–13 | 14–17 | 18–44 | 45–69 | 70–84 | 85+ |
| Kel Dor | 1–11 | 12–15 | 16–44 | 45–59 | 60–69 | 70+ |
| Mon Calamari | 1–11 | 12–16 | 17–40 | 41–57 | 58–79 | 80+ |
| Quarren | 1–11 | 12–16 | 17–40 | 41–57 | 58–79 | 80+ |
| Rodian | 1–12 | 13–15 | 16–35 | 36–49 | 50–59 | 60+ |
| Sullustan | 1–9 | 10–14 | 15–39 | 40–55 | 56–69 | 70+ |
| Trandoshan | 1–11 | 12–14 | 15–34 | 35–49 | 50–59 | 60+ |
| Twi'lek | 1–12 | 13–15 | 16–44 | 45–59 | 60–79 | 80+ |
| **Wookiee** | 1–12 | 13–17 | **18–300** | **301–350** | **351–399** | **400+** |
| Zabrak | 1–8 | 9–14 | 15–44 | 45–55 | 56–69 | 70+ |

**Seventeen rows, six bands, as you specified.**

---

## ⚠ Two things attached to the table that a `Persuade` ladder will break on

**The chapter's own commentary, and it is load-bearing for `FORCE-TRAINING-01`:**

> **"Wookiees are not on a human scale and nothing about them should be read as though they were.** A Wookiee is an adult for nearly three centuries… **If you are running a Wookiee at the campaign date, that character can personally remember the Great Sith War** — and any rule, table, or piece of software that assumes a hundred-year lifespan will reject the numbers as errors."

> **"Gamorreans run the other way.** Adult at thirteen, middle-aged at thirty, venerable at forty-five."

**⚠ A `Persuade` ladder keyed to age band gives a 200-year-old Wookiee the same rung as a 25-year-old Human — both `Adult`.** **And a 40-year-old Gamorrean is `Old` while a 40-year-old Human is `Adult`.** **Whether that is the intent or an artefact is a design question, but it should be answered before the ladder is built, not after.**

---

## ⚠ Your species-not-on-the-table section also survives, and it names the real gap

**From the same retired chapter:**

- **UAA supplies bands** for Nautolan, Devaronian, Gand, Weequay, Togruta, Dashade, Bith.
- **The Campaign Guide** for Arkanian, Arkanian Offshoot, Cathar, Miraluka, Rakata, Selkath, Kissai, Massassi.
- **⚠ Two species have no bands anywhere: Kaleesh and Echani.** *"Both were authored for this setting and no source gives them ages."*

**Those are the two `AUTHORED_PENDING` age fields the library has been carrying.** **They are not missing data — they are data that does not exist and must be authored.**

---

## ⚠ On `PT-377` — the withdrawal is the useful part

**You withdrew it because you read *"table of information provided in the UAA"* as *"table in the UAA,"* from a 2011 blog post that had collected per-entry data.**

> **That is `METHOD-RECORD-01 §1.3`, the adjacency rule, exactly** — **a claim taking its warrant from a phrase beside it rather than from the thing itself.** The corpus records it firing three times on a single rule (`+4/−8`) and the library has committed four instances of the same shape today, including the `-2` column and a proposal made from what a decision *closed* rather than what it *contains*.

**`PT-376` naming the pattern is worth more than the three withdrawals it covers.**

---

## ⚠ One thing to fix on your side, and it is not the table

**`rules/` has not been cleaned and it grew.** Checked by re-cloning, not by asking:

    rules/ before  169 .md    now  172 .md    removed: 0
    divergent duplicate names   36  ->  37

**Three added — `BEASTS-ENTRIES-01`, `BEASTS-PLAYER-01`, `GM-CREATURES-01`. None removed.**

**⚠ And a new fork appeared: `GAP-002.md` now diverges between `rules/` and `playtest/`.** It did not before. **The library spliced the `playtest/` copy in Phase 1 — the one carrying `PT-248`.**

**Not a complaint. Stating it because the reconciliation is now racing a growing tree**, and knowing that at Phase 2 is cheaper than discovering it at Phase 3.
