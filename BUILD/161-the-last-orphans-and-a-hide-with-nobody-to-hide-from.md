# BUILD 161 — the last orphans close, and a Hide with nobody to roll against

---

## 1 · ⚠⚠ `PT-1832` — THE LAST 22 ORPHAN ROWS, ON TWO CONSTRAINTS

The 118 went on a unique blueprint string. These 22 had none, and **both rules
that close them are facts the documents state**, not rankings of guesses.

**Rule 2 — one item carries one description.** `extract_items.py`'s own
reading: *"a description is its own table row… and it attaches to the item
above it."* So a candidate that already has one cannot own an orphan too. One
row had two candidates and exactly one was still free.

**Rule 3 — the permutation is immaterial, and it is PROVED.** The other 21 fall
into groups where **N rows share exactly N candidates, every row carries the
same text, and every candidate carries the same blueprint description.** Any
assignment therefore produces a byte-identical document. There is nothing to
get wrong, which is why this is not the guessing the ruling rules out: the
question has one answer and the order of the pairing is not part of it. The
rule refuses the moment any of the three conditions fails.

**⚠ AND I RAN IT TWICE WITH THE PAIRING REVERSED AND DIFFED THE BYTES.** The
first harness said the files **differed** — because it reversed across the whole
document rather than within each group, so an emitter's description landed on a
grip. **That was my check grouping by the wrong thing, not the claim failing.**
Corrected, the output is byte-identical. Recorded because the harness was seen
discriminating before it was believed.

Nine rows remain and **are not orphans** — the known multiline rows
`extract_items.py` already documents. The fifteen crystal rows stay unresolved
as ruled.

## 2 · ⚠ §2 IS GATED, AND PT-1443 IS NOT THE GATE I THOUGHT

`§2`'s entry point is *"clicking into the player card"*, and this screen has
never taken a pointer. **But the keyboard is not blocked** — and the play
screen's own comments say why:

> *"`space` ENDS THE TURN — `PT-1540`. A key rather than a click, because
> `PT-1443` wants the keyboard path to reach everything the pointer does."*

> *"`d` DISENGAGES… **the FIRST Action in this product that is not Attack**…
> A KEY BECAUSE THIS SCREEN HAS NEVER TAKEN A POINTER."*

**So an Action needs no pointer ruling** — `f`, `m`, `i`, `d` and `space` are
already the ruled vocabulary. I had been carrying *§2 is behind PT-1443* as
though it blocked everything; it blocks the **card and the click**, not the
verb. Corrected by reading it.

## 3 · ⚠⚠ `PT-1108` — HIDING IS BUILT, AND HAS NOBODY TO ROLL AGAINST

`ACTION-ECONOMY-01 §1`'s **Hide** and `SKILL-RESOLUTION-01 §4`, of which the
product had **no trace**: `hidden` existed only as an authored placement
property (`PT-1550`), so nothing could ever hide.

Nothing here rolls — `CheckType.opposed`, `Check` and `resolve` already exist,
so this is the two facts the documents state and a `Check` built from them.

**⚠⚠ THE PENALTY IS APPLIED BEFORE THE COMPARISON, AND THE ORDER IS THE RULE.**
`§4.1` is entirely about the field changing **which sense answers** —
*"excellent against a watchful guard and useless against a Selkath."* Comparing
first and docking after reads identically in most cases and is wrong in exactly
the ones the section exists for. Guarded, and the guard was watched failing
against that mutation.

`hideDefence` returns **which skill answered**, not just a number, because the
sense changing is the thing being modelled.

**Two readings, said out loud:** a tie after the penalty is reported as
*hearing* (it changes a word, not a number); and **Hidden from everyone or
Hidden from nobody**, because `§4` has one Hidden condition and every rule that
reads it — `PT-1550`, `PT-1682` — reads it as one state of one creature.

## 4 · ⚠⚠ AND THEN IT HAS NO CALLER, BECAUSE A CREATURE CARRIES NO SKILLS

    Combatant        dexModifier · strengthModifier · constitution ·
                     budgets · role          — and no skill of any kind
    OpenedCharacter  abilities · vitality · protection · equipment ·
                     doctrine · reactions    — and no skills either

**The player has ranked skills from chargen. The thing on the other side of the
roll does not.** So the defender's half of *"against the better of enemy
Awareness or Alertness"* cannot be supplied by anything.

**⚠ AND IT IS NOT ONLY HIDE.** Five of `§1`'s fourteen Actions are skill checks
against or on a creature — **Hide, Scan, Slice, Treat, Repair** — and
`PT-1123`'s exploration catalogue aims `Repair` at a droid and `Pick Pocket` at
a person. **One missing field**, and it is a FORMAT question:
`AUTHORED-CHARACTER-01` is the owner's.

**⚠ SHIPPING AN UNCALLED FUNCTION IS THE DEFECT CLASS THIS CORPUS NAMES**, so
it is pinned rather than left quiet — `stealth_gap_test` asserts nothing in
`lib/` calls it, **with an instrument check beside it**: the same scrape *does*
find `followOneStep`, so an empty result is a fact about callers and not a typo
in the search. Written to fail the day a creature can carry a skill.

## 5 · ⚠ AND `Hidden disables running` HAS NOTHING TO DISABLE

`PT-1108`'s second stealth borrowing is *"Hidden disables running"*. Running is
**Dash** — `§1`: *"double your movement this round"* — and **Dash does not
exist**, in the engine or the app. Not built, and named rather than quietly
skipped.

⚠ Its natural key is taken: `d` is Disengage. That is a real, small question
for the owner rather than a letter for me to pick.

---

## Tests

    Lodestar   716 pass   (stealth_test +11)
    App        579 pass   (stealth_gap_test +3)

`check_shelf` ✓ 25 identical · `check_extracts` **stale 0** ·
`check_engine_pin` 4 compared, all level · gate **SENDABLE**.
