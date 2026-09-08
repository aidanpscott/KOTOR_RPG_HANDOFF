# 20 · Combat slice 2 — the check fix, then pools and damage

**`Lodestar` `8c281e8` · `KOTOR-RPG-APP` `508f741`+.** 143 Lodestar tests, 182
app tests, analyze clean.

---

## 1 · The check, on its own, before the emission

**`PT-1420`'s rule, and it is about lifetime rather than about replay's
switch:**

> **A `permanent` kind replay ignores is the bug. A `transient` one is the
> design.**

`emitted == handledByReplay` **held only because the two sets coincided**, and
that was never the rule.

**⚠ AND THE NEW RULE IS PROVED AGAINST A CASE IT DOES NOT YET HAVE.**
`emitted − handled` is empty until combat writes, so the assertion would pass
**vacuously** — and a vacuous check is one nobody has run. A third test names
`character.alignment-shifted`, which **is** `permanent` and **is** unfolded,
and shows that emitting it would fail the rule.

**A second assertion was scoped, not weakened.** *"Every emitted kind is
permanent"* was true only while chargen was the only thing emitting — **the
same coincidence, one line down.** It now says every **creation** kind is
permanent, which is what `PT-1418` actually ruled.

**Committed alone**, at `508f741`, before anything that could break it.

---

## 2 · Pools — and `§6b`'s trap was avoided by reading what it corrects

**`PORT-01 §3` models two values. We have one and three.**

| | |
|---|---|
| **Vitality** | **ONE pool with a negative band.** `wound points` do not exist (`PT-559`). **`Constitution` is a THRESHOLD, not a capacity** — a Con-14 character with 30 vitality dies at −14, and there is no second pool to run out |
| **Force** | **THREE values** — current, **working maximum**, true maximum |

> **⚠ `PORT-01 §3.1`'s whole argument rests on `pool.wounds`, a pool we
> deleted**, and its own note says *"all formulas reconstructed."* Implementing
> its two-value model faithfully would have been the fifth instance of that
> shape.

### The third value is the one that carries the fiction

**Degradation is cost AND tier together** — 10% · 20% · 30%, rounded up, and
`§4.2`'s own three examples are the test. *"Cost alone would make an expensive
tier-1 power tire you as much as a cheap tier-3 one."*

    cast Force Storm (cost 24, tier 3) from a full 40:
      current 40 → 16      ceiling 40 → 32      true max 40

    sleep      pool to the WORKING maximum · ceiling unchanged   → 32 / 32 / 40
    meditate   refills AND restores the ceiling                  → 40 / 40 / 40

**⚠ After a night, "full" and "capable" are different numbers — 32 of a true
40 — and two values cannot say that.** *"A Force user who sleeps normally wakes
healed, pool full, ceiling still degraded."*

**The ceiling floors at half the true maximum**, tested by casting a day away.

---

## 3 · Damage, and the death boundary

**⚠ This is where `§5`'s difficulty arrives, and the only signature that needs
it.** `resolve` never sees it; the boundary does.

| Mode | |
|---|---|
| **Easy** | **No negative band at all.** 0 is `down`. **And damage below 0 is not tracked** — stored as 0, not merely ignored, because a pool quietly remembering −40 would resurface the moment the table changed mode mid-campaign |
| **Normal** | standing · down at 0 · dying to −(Con−1) · dead at −Con. **⚠ A henchman uses the Easy rule** — `PT-571`: *"a hired NPC is not the player's to lose permanently"* |
| **Hard** | the same band **for everyone** — *"no distinction between player, companion and henchman"* |

**⚠ The author's escape hatch is respected.** `AUTHORED-CHARACTER-01 §3`:
`override = 0` means **derive normally**, and it is **not a vitality of zero**.
A boss at 200 takes 40 and stands at 160.

### ⚠ A contradiction inside `DEATH-AND-DIFFICULTY-01` — reported, not resolved

| Where | Says |
|---|---|
| **`§2` Hard** | *"No distinction between player, companion and henchman. **−10 is −10.**"* |
| **`§5b`** | *"**`E-2`'s flat `−10` is superseded. The threshold SCALES with Constitution**, so a beast with Con 18 and a character with Con 10 are handled by ONE RULE at their own scales."* |

**The superseding line is followed** — and Hard's actual point is that no
**role** is distinguished, not that the number is ten.

---

## ⚠ 4 · CHECK A DID NOT FIRE — and for a different reason than last time

**Slice 1 wrote nothing. Slice 2 writes, and the kinds were already there.**

    character.died · character.downed · character.revived     all campaign

**`§4`'s list and `EVENT-KINDS-01`'s Character group were written together**, so
the vocabulary already had combat's outcomes. **Nothing is owed.** A test in
Lodestar asserts all three are declared and `campaign` — check A's twin, on the
side that emits.

**⚠ And `campaign` kinds replay ignores are not a bug — they are owed to a
projection that does not exist.** `CharacterRecord` has no *alive* field, by
design: `PLAY-STATE-01` owns current state and nothing has built it. The new
lifetime rule permits this correctly, and **the debt is a second projection,
not a missing case.**

**And a wound is not a fact.** Losing four points writes nothing at all — only
crossings do.

---

## ⚠ 5 · What had to behave somehow, this time

`PT-1420` ruled the tie and the confirmation roll. **Applying damage surfaced
three more**, all flagged in the code:

| | What it does | Why it is not settled |
|---|---|---|
| **Healing past `max`** | clamps at the working maximum for Force, **and is NOT clamped for vitality** | Nothing read says whether a heal can exceed the capacity. Vitality is left unclamped deliberately so the gap is visible rather than papered over |
| **Negative damage** | is healing, through the same boundary logic | Nothing states that healing and damage are one operation. It is the simplest reading and it produces `character.revived` correctly |
| **`down → dead` in one blow** | writes **only** `character.died` | Nothing says whether passing through `down` on the way to `dead` should record both. One crossing, one event, is the reading taken |

**All three had to do something to be testable — which is how the tie was
found.**

---

## What was NOT built

**No turn order, no initiative, no enemy decisions** — `§6`'s *"real
question"*, and slice 3. **No grid, no targeting, no screen.** Nothing in the
app calls any of this yet: combat is a library the play screen does not use.

**No dying countdown.** `§6b` says a dying character *"loses 1 per round"*, and
a round does not exist until slice 3.
