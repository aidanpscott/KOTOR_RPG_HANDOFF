# BUILD 78 — `PT-1531`: I looked before authoring, and the answers differ

**829 green** — Lodestar 381 · Lens 5 · Loom 131 · app 314.

---

## ✅ BASE ATTACK BONUS — **PRESENT AND UNEXTRACTED.** A re-run, not a decision.

**All four `CLASS-TABLES-*` files carry a per-level `BAB` column — 38 tables** —
and `CLASS-TABLES-BASE` names the rate per class **in words**:

    | Soldier  | d10 | full — CLS_ATK_1            |
    | Scout    | d8  | three-quarters — CLS_ATK_2  |
    ⚠ CLS_ATK_1 is full (+1 per level, +20 at 20) · CLS_ATK_2 is
      three-quarters (+15 at 20) · CLS_ATK_3 is half and NO CLASS USES IT

### ⚠⚠ THE EXTRACTOR'S MERGE WAS FIRST-WINS

    §3  read_phb   → progression = feats · attack_picks · fort · ref · will
    §5  AUTHORED   → `if not classes[k].get('progression')`   ← skipped

**Two tables, DIFFERENT COLUMNS, and one dropped whole.** The PHB tables have
`attack_picks`; the source tables have `BAB`. First-wins meant a class that had
a PHB read **never got its BAB**.

⚠ **And `CLASS-TABLES-BASE`'s own progressions were read by NOTHING.** The
Soldier, Scout and Smuggler have their per-level BAB there, in a file no
progression reader opened — its heading shape differs from `AUTHORED`'s
(`— d10, Strength,` against ``— d10, `…``), **so one regex did not reach both.**

**Merged by level, adding rather than replacing: 25 → 35 of 38.**

⚠ **THE DIFF IS CONTROLLED:** exactly **ten** classes changed and **every change
is `bab` added plus a `bab_source`.** No field moved, no class lost.

⚠ **AND IT CROSS-CHECKS AGAINST THE DOCUMENT'S OWN CLOSED FORM:** the soldier
reads **+1 at 1 and +20 at 20**, which is `CLS_ATK_1` end to end. Asserted
against the **shipped** `classes.toml`, not a fixture — a fixture would pass
whatever it was given.

⚠ **Three have no per-level table anywhere:** `engineer`, `marksman`,
`saboteur`. The Engineer's *rate* is named in prose (`CLS_ATK_2`) and **a ladder
derived from an endpoint is authoring, not extraction.** The term is omitted for
those three; a zero would claim it was computed.

---

## ⚠⚠ DEFENCE'S CLASS BONUS — **NEITHER.** Not extractable, and not mine.

`PT-1531` ruled the expression while I was looking, and it matches what the
corpus supports: **`10 + Dex modifier + class bonus + grants`**, from `RCR`.
Built, on **both** sides — it was a flat `10` in `play_screen` *and* in
`fight.dart`, so **a nimble creature was no harder to hit than a slow one, in
either direction.**

**The class term has nowhere to read from, and our own corpus already said so.**

> **`CLASS-TABLES-JEDI §5A`:** *"RCR class tables carry a `Defense Bonus` that
> progresses by level. Confirmed on the Noble (RCR pp.42–43), where it runs +2
> at 1st to +10 at 20th. **The three tables above carry the column with values
> unextracted — the Jedi progressions are in RCR Chapter 3 and have not been
> read.**"*

⚠⚠ **SO IT IS NOT AN EXTRACTION GAP, AND I CAN PROVE IT:** `classes.json`
**already carries a `defence` key** for the three Jedi classes — and **every
value in it is an em dash.** The column *was* extracted. There was nothing in
it.

⚠ `§5A` even predicted the consequence: *"Defense Bonus joins the ordered field
list for every class read from RCR. It was not in the original order and would
otherwise have been missed on all nine."*

**One data point is attested in the whole corpus — the Noble, +2 to +10.**
Nineteen base classes plus prestige across thirty levels is **a read of RCR
Chapter 3.** **Stopped, as instructed.**

---

## ⚠ AND I CORRUPTED A FIXTURE, AND THE FIXTURE CAUGHT IT

An edit script of mine searched for `"\n"` **as a two-character escape** and
matched one **inside a Dart string literal**, injecting a function call into the
middle of a TOML blueprint. It surfaced as:

    characters/brute — will not open
    TOML parse error: newline or end of input expected at 1:14

**Which is the fixture reporting exactly what was wrong with it.** Repaired, and
worth naming: **an edit script that pattern-matches source text can land inside
a string**, and a "no such element" three frames later is what that looks like.

## Still open

- ⚠⚠ **The class defence bonus needs an RCR Chapter 3 read** — 19 base classes
  plus prestige, one attested data point.
- ⚠ **Three classes have no BAB table**: `engineer`, `marksman`, `saboteur`.
- ⚠ A creature's weapon kind is unknown in `fight.dart` — absent reads as melee.
- ⚠ `PT-1509`'s perception half; `PT-1532`; `tester-probe`'s failure node; no
  `unlink` button; `PT-1484`, `PT-1485`, effect columns, 45 annotation cells.
