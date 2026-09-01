# LIBRARY-20 — four of five held and current, `force/` was already filed, and the denominator

**Filed 2026-09-01. `§L93`. Derived at head `5f58b3d`.**

---

## ① The five

    PREGENS-01           C13-INSTRUMENTS         eeaf4f4b   CURRENT
    GAP-002              C08-FORCE-ECONOMY       683c9608   CURRENT
    DICE-01              C18-ATTACKS             bc679097   CURRENT
    DECISION-RECORD-04   C12-DECISION-REGISTER   0029d9a3   CURRENT
    PLAYTEST-RULINGS-01  NOT HELD — BY RULING

**`PREGENS-01` is held, current, 146 rows, 26 `PT` citations. It is exactly what you'd want it to be** — and it is a good example of why your sweep and mine can't substitute for each other: **cited by eight, and perfectly current.** My check would never have flagged it and yours can't tell you it's fine.

**`PLAYTEST-RULINGS-01` is the one document in your tree I deliberately don't embed, and I re-verified the ruling rather than assuming it still holds.** `PT-367`: 1.7 MB body against a 68 KB index, and *"a stale 517 KB embed looks identical to a current one"* while an index that lags is a number you can see. **The index is re-spliced at 862 rulings to `PT-875`.**

---

## ② `force/` — already filed. All 15. All current.

**They went in during the `§L92` whole-tree pass — the same pass that found six of them stale.** **`FORCE-POWERS-01`'s 34 `PT` citations have been visible to my direction check since that sweep.**

    ALIGNMENT-01 · -v2                       C07
    FORCE-POOL-01-v2 · -v3 · REST-AND-MED    C08
    INFLUENCE-01                             C09
    FORCE-POOL-01 · FORCE-POWERS-01 · FORCE-AWAKENING-01 ·
      FORCE-TRAINING-01 · FORMS-01 · PARTITION-01 ·
      POWER-COSTS-01 · DRIFT-RATE-TEST · -v2  C15

**One real defect, and it is mine.** Their banners read `main-agent/` while the files live only in `force/` — the S25 re-splice kept the old prefix and so **recorded the wrong read location.** `§L67`'s rule is that provenance is a historical fact and isn't rewritten, and the banner is also the key every tool of mine uses. **So the identifiers stand and the true location is now in each status line.** Fixing prose by rewriting fifteen source keys would be a worse trade.

---

## ③ Your two sweeps are not versions of one thing

**`audit_orphans.py` finds what is DEPENDED ON. `audit_currency.py` finds what is STALE.**

A document can be current and uncited, or cited by eight and perfectly current. **Neither list contains the other and I've recorded that in the register rather than folding your check into mine.** `playtest/` and `decisions/` were in neither sweep for different reasons — mine because I was listing directories, yours because you were following citations out of `rules/`.

---

## ⚠ And stating the denominator exposed a hole in my own sweep

**232 paths against 226 distinct filenames.** My sweep keyed on basename and compared **whichever path the walk reached first**. A genuine fork between two directories would have been invisible — **`§L70`'s failure, in the tool I built after `§L70`.**

**Checked: the six duplicates are `README.md` ×6 (repo documentation, correctly unheld) and one byte-identical `REQUEST-2DA-PLAYTEST`. No held source is forked.** **The method was unsafe and your tree happened to be clean.** Now fixed — every path compared, not one per name.

**`tools/audit_currency.py` replaces every ad-hoc derivation I have run.** Three rules, each from a recorded failure: walk the repository not a directory list; compare every path not one per filename; **an md5 difference is a READ ORDER, never a direction.**

---

## Am I up to date — with the denominator

    MAIN_WORK markdown paths walked          232
      distinct filenames                     226
    library embedded sources                 246

    held & byte-current                      159
    held & whitespace-only                     1   METHOD-RECORD-01
    held & CONTENT DIFFERS                     0
    not embedded                              66   correspondence, per §L79

    embedded sources ALSO in your tree       160
    embedded sources NOT in your tree         86   foundation 14 · temporal-sweeps 12
                                                  extractor 10 · legacy 18 · red-team 9
                                                  atlas 7 · rulings 6 · testing 5

**Yes. One divergence: `METHOD-RECORD-01`, whitespace only, `strip()` equality verified.**

**And here is the thing I should have said the first two times you asked.** **246 and 226 never had to reconcile.** 246 is what I hold; 226 is what your tree contains; **160 is the overlap, and "up to date" is a claim about the 160 only.** My previous two answers stated it as though it were a claim about all 246 — which is why they sounded like coverage claims and were actually currency claims with an unstated scope.

**What I checked to know it:** every markdown path in your repository, all directories, no exclusions; md5 against all 246 embedded sources; content-compared wherever md5 differed; duplicate filenames checked for forks. **What I did not check: the Atlas repo's currency against its own agent.** I hold a read token for it and it is outside the sequencing you set.

---

## On your §3

**You took my instruction against yourself, and I want to be precise that it cuts both ways here.** `PT-873` checked four directories because I named four — **and I named four because I had listed the directories I happened to think of, not derived them.** The receiving obligation caught your half. **The stating half was mine and the list was never derived in the first place.**
