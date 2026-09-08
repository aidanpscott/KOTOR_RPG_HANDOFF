# 19 · Combat slice 1 — `resolve()` and one attack

**`Lodestar` `442b600`.** 128 Lodestar tests, 180 app tests, analyze clean.
**425 lines of `ENGINE-SPEC-04` had never run. Thirteen of them do now.**

---

## What was built

`resolve(check, dice)` and `resolveAttack(...)`, in `Lodestar/lib/src/combat.dart`.

**⚠ Callable without a game — `§3`, `PT-1023`.** No grid, no turn order, no
enemy, no screen, no character record. **The test file is the proof: nothing in
it constructs a world**, which is what lets the Builder ask *"what does this
fight cost a level-4 party?"* with nothing running.

---

## ⚠ The return value is the derivation, and the test caught me spoiling it

Every term carries a value **and where it came from**; the outcome keeps the
raw die face. **If this returned `17`, the inspect-a-check setting could not
exist and neither could a GM asking why.**

**⚠ AND MY FIRST VERSION PUT THE SOURCES INSIDE `PT-1326`'s OWN LINE.**

    mine       rolled 17 — d20 11 + rank 4 (skills) + aptitude 2 (homeworld) …
    PT-1326    rolled 17 — d20 11 + rank 4 + aptitude 2 · needed 14

**Split into two forms.** `line` is `PT-1326`'s exactly; `detailedLine` is what
the inspect setting shows. **A settled format is settled, and lengthening it is
how two things end up shown in one shape** — which is the error `PT-1326` was
written to correct.

---

## ⚠ `§6b` checked before building, as asked — and it did not bite here

`§6b` says pools are **three values, not two**, and `PORT-01 §3` models two.
**Slice 1 models no pool at all**, so the faithful-implementation-of-the-wrong-
thing did not get a chance to happen — but the shape is real and it is waiting
for whoever applies damage:

- **Vitality is ONE pool with a negative band**, not two. `wound points` **do
  not exist** (`PT-559`), and `Constitution` is **a threshold, not a capacity**.
- **The Force pool has three values** — current, **working maximum** (degrades
  per cast, floored at half), true maximum. *"You cannot rest off exhaustion."*
- **`PORT-01 §3.1`'s whole argument rests on a pool we deleted**, and its own
  note says *"all formulas reconstructed"*.

---

## Other rulings this slice had to obey

| | |
|---|---|
| **`§6e`** | **Four check types, one die** — attack, save, opposed, skill. **A save stays roll-vs-static-DC.** `PORT-01`'s `C7` folds saves into contests; **`Dominion`'s *"+1 to the saving throw DC"* would have nothing to modify** if it did |
| **`§6c`** | **The threat range is the column that carries information.** `critOn` decides a critical; the multiplier only multiplies dice. A 19 crits a threat-19 weapon and not a threat-20 one |
| **`§2`, `PT-1013`** | **The die is injected.** A resolution reaching for a global random could not be replayed, tested, or made to explain itself. `FixedDice` refuses a face not on the die and says so when a sequence runs out |
| **`§4`** | **Nothing is applied to anything.** No hit, no miss, no current vitality |

---

## ⚠ CHECK A DID NOT FIRE, AND THAT IS THE FINDING

The brief expected an undeclared kind. **There is no new kind, because this
slice writes nothing to the ledger.**

`§4`: *"almost nothing DURING the fight. A round is transient state, not
canon."* **Not written: hit/miss, current vitality, position, whose turn it
is.** Written: who died, what was destroyed, what the party took, alignment
shifts — **and this slice produces none of those**, because a death needs
damage applied to a pool and that is `§6b`'s and the next slice's.

**So `resolve` returns a value and emits nothing.** `attack.resolved` and
`check.resolved` are already declared, both **`transient`** — and
`EVENT-KINDS-01 §5`'s *"one vocabulary, two consumers"* means a transient kind
may be **raised for a reaction to hear without being persisted**. **Nothing
subscribes yet**, so raising one would be writing into a bus that does not
exist.

### ⚠ And the day combat does emit, one assertion breaks first

Check A currently asserts **`emitted == handledByReplay`**. That held because
the two sets coincided. **`attack.resolved` is transient and replay will never
fold it**, so the right generalisation is:

> **an emitted kind that replay ignores must be declared with a lifetime that
> says it need not persist.** A **`permanent`** kind replay ignores is the bug;
> a `transient` one is the design.

**Named as the next slice's first task rather than changed here** — nobody
asked for it, and it is a check, not combat.

---

## ⚠ `§5` difficulty — the signature needs nothing, now or later

`§5`: *"the engine resolves identically in all three modes and branches only at
the death boundary. `Easy` does not make the Sith miss more."*

**So `resolve` never sees difficulty.** What needs it is whatever applies
damage and decides **what happens at zero** — `DEATH-AND-DIFFICULTY-01`'s three
modes act there, and `PT-991`'s `Triage` was built against exactly that. **The
mode belongs to the death boundary's signature, not to this one.**

---

## What was NOT built, and one thing left unruled

**No turn order, no initiative, no enemy decisions** (`§6` calls those *"the
real question"*). **No grid, no targeting, no screen. No damage applied to a
character record. No pools.**

**⚠ And a tie in an opposed roll goes to the defender — nothing rules that.**
It had to behave somehow to be testable; it is flagged in the code and here
rather than presented as settled.

**No critical confirmation roll.** Nothing read for this slice states one, and
inventing it would be a rule.
