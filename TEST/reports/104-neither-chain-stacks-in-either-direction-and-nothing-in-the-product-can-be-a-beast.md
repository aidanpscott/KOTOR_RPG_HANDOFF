# TEST 104 — Neither chain stacks in either direction, and nothing in the product can be a beast

**Build under test.** KOTOR-RPG-APP `618a544` *"PT-2304: a higher tier takes the lower one off
before putting its own on"*, working tree clean. Lodestar **`25ad8e2c`** (the lock moved this
session — it was `2d5d696b` in TEST 102/103), Lens `32b77e3b`; `package_config.json` resolves to
the checkouts that compiled, which are the ones I read the engine from. `fresh.py --debug --build`
printed `✓ FRESH — built from exactly this source`. `check_shelf.py` green: 29 rules files, 65
standard blueprints.

Items 1 and 2 confirmed. Item 3 cannot be confirmed as asked, for a reason that is ruled and
stated in the engine.

---

## 1. Force Valor no longer stacks — confirmed, both directions, exactly

The reading is the `Strength` term in the caster's own attack line. An ability bonus is a **score**
the derivation re-reads, not a roll, so this is exact and needs no dice. The caster carries
Strength 18 (+4), which makes the three outcomes land on different printed terms:

| state | score | attack term | damage term |
|---|---|---|---|
| no Valor | 18 | `Strength 4` | `Strength 6` |
| Force Valor (+2) | 20 | `Strength 5` | `Strength 7` |
| **Master replacing (+5)** | 23 | **`Strength 6`** | **`Strength 9`** |
| *both appended (+7)* | *25* | *`Strength 7`* | *`Strength 10`* |

**Forward — Force Valor, then Master Valor:**

```
baseline   Vibrosword · rolled 29 — d20 16 + attack 9 + Strength 4 · damage 16 — 1d12 10 + Strength 6
Force      Vibrosword · rolled 29 — d20 15 + attack 9 + Strength 5 · damage 19 — 1d12 12 + Strength 7
+ Master   Vibrosword · rolled 33 — d20 18 + attack 9 + Strength 6 · damage 14 — 1d12  5 + Strength 9
```

`Strength 6` / `Strength 9`, not `7` / `10`. **The higher tier replaced the lower.** Two
independent terms agree.

**Reverse — Master Valor first, then Force Valor** (fresh fight, same board):

```
Master     Vibrosword · rolled 24 — d20  9 + attack 9 + Strength 6 · damage 15 — 1d12 6 + Strength 9
+ Force    Vibrosword · rolled 28 — d20 14 + attack 9 + Strength 5 · damage 12 — 1d12 5 + Strength 7
```

Not stacked — the old defect is gone in this direction too, which is what the routing asked. But
note **what** it settles on: `Strength 5` / `7`, the score back down at 20. **The lower tier
replaced the higher one**, so casting Force Valor on top of Master Valor downgrades the caster
from +5 to +2.

⚠ Reporting the number rather than a verdict, because this looks deliberate: `superseded()` also
returns true when the *standing* power's `replaces` names the incoming one, and the commit message
says *"The relation is read BOTH WAYS, which is not the same as saying the document is
symmetric."* The document's sentence is one-directional — *"Knight Valor replaces the bonus
granted by Force Valor"* — and says nothing about the reverse. So "most recent cast wins" is a
ruling, not a transcription, and whether a player should be able to weaken themselves by casting a
power is yours to decide. The routed claim — no stacking, either order — holds.

## 2. Force Camouflage no longer stacks — confirmed exactly, twelve numbers

The hide line prints only a total, so this is done by making the **die streams identical** rather
than by comparing averages. The stream is a deterministic function of the action sequence, so the
reference run spends the same number of turns as the test run — Master cast twice, against
Improved then Master:

| run | first cast | second cast | pool | rolls |
|---|---|---|---|---|
| reference | Master (20f) | Master (20f) | 159 → 139 → 119, ceiling 147 | 18, 23, 20, 28, 17, 27 |
| test | **Improved (14f)** | Master (20f) | 159 → **145** → 125, ceiling **150** | 18, 23, 20, 28, 17, 27 |

Watcher totals identical too: 57, 44, 59, 60, 49, 42 in both. **All twelve numbers match.** The
Stealth rank was the same in both runs, so Master after Improved is `+8`, not `+12`.

The differing pool and ceiling figures are the control that the two runs really did cast different
first powers — 14f and −3 for Improved against 20f and −6 for Master. Without that, two identical
result sets would also be what a dropped keypress looks like.

An earlier attempt compared six rolls under Improved against six under Improved+Master **within
one fight** and produced a difference of about −1, which is neither answer. That was my error, not
a finding: the two phases were far apart in the die stream and their watcher sequences shared no
shift, so the rows could not be paired. Recorded because the noisy version looked like a result.

---

## 3. Beast Confusion and Beast Trick — the targeting works; there is nothing to aim it at

**Nothing in the product can be a beast, and that is ruled rather than incidental.** `kindOf`
(`lib/play/power_target.dart:38`) returns `droid`, `sentient` or null and has no third branch; the
engine's own `CreatureKind.beast` carries the ruling: *"`kindOf` can never return it: `beast`
exists in the `targets` vocabulary and nothing in a package is one yet."*

So the two halves I could test:

**The gate refuses a sentient, correctly and for free:**

```
Beast Confusion is aimed at beast, not a sentient — nothing spent
```

Pool untouched at 159 of 159.

**The only creature a `targets: ["beast"]` power will resolve against is one whose kind is
UNRECORDED** — I authored a blueprint with no `species` key at all, which makes `kindOf` return
null and `mayTarget` answer `silent`:

```
Beast Confusion · 20f — 127 → 107 · ceiling −4 to 146 · at hulk.stack.01
  · ⚠ nothing records what this is, so its kind cannot be checked · [the power's effect prose]
Beast Trick     · ... · ⚠ nothing records what this is, so its kind cannot be checked · [prose]
```

Both spent the pool and landed nothing. That is **not** a defect in the new powers, and it is not
a beast being hit — it is a permissive branch for an unknown kind, and the status line says so.

**Both DO behave exactly like their generic counterparts — because neither counterpart does
anything either.** Comparing what the four rows actually carry:

```
force_confusion   id name alignment tier cost degradation prerequisites effect affects save_kind excludes   subtables: NONE
beast_confusion   id name alignment tier cost degradation prerequisites effect note targets affects save_kind   subtables: NONE
mind_trick        id name alignment tier cost degradation effect note excludes   subtables: NONE
beast_trick       id name alignment tier cost degradation effect note targets   subtables: NONE
```

No condition, no damage, no modifier, no ability penalty — on any of the four. The Confusion and
Trick family is prose-and-a-save-kind with no modelled effect, and the two new rows match their
counterparts field for field. The only real difference is the targeting vocabulary: `targets =
["beast"]` where the generics carry `excludes = ["beast", "droid"]`.

**So "confirm each lands normally" cannot be satisfied on this build**, for two independent
reasons: there is no creature that is a beast, and even against a permissive target there is no
modelled effect to observe landing. What I can say is that the new rows are correctly authored,
the kind gate accepts and refuses on exactly the right creatures, and they are not broken relative
to Force Confusion and Mind Trick. Re-route them when a beast is placeable, or when the family
gains its condition rows — either would make the question answerable.

## Not tested

- Knight Valor as the middle tier of the stacking check. Force → Master is the wider gap and both
  terms discriminated cleanly; Knight carries the same `replaces` list shape.
- Improved Force Camouflage cast *after* Master (the reverse direction for chain 2). The Valor
  reverse is reported above and the two chains share one predicate, so I spent the slice on
  getting the forward Camouflage reading exact rather than on a second instance of the same code.
