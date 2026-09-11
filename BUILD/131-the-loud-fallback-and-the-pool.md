# BUILD 131 — the loud fallback, and the reaction pool was never the problem

`PT-1699`, then `PT-1675` — which turned out not to need the attack-roster
subsystem at all.

---

## 1 · `PT-1699` — AN UNKNOWN STEP NAME DISCARDS EVERYTHING, LOUDLY

`clear`'s `switch` had no default, so a step name this build does not have was
**silently ignored** — the exact failure the discard list exists to prevent,
invisible. It returns whether it recognised the name now.

### ⚠⚠ "Everything after it" has no smaller safe bound, and that is why it is everything

The list is ordered — the reopened step, then every step after it — so **every
step forward of an unknown name is already behind it in the list** and the loop
clears it anyway. A bound derived from the list's order would be free.

> **The case that bound misses is the one the ruling is for: a RENAMED step.**
> Its slice is the unknown name's own, it sits **earlier** than the names that
> follow it, and nothing in the list points at it. **An unplaceable name has no
> position, so everything is forward of it.**

That case is pinned by its own test, and it is what a mutation to a narrower
bound would pass.

### ⚠ Loud, and not a refusal to load — `PT-1526`'s shape a second time

The record comes back **short rather than not at all**, and the pre-hub choices
are untouched: `clear` has never had a case for species, variant, model or
class, and a re-lock has never claimed to reach them.

`ReplayOutcome.unknownDiscards` is the fault a future check can catch, sitting
beside `ignoredKinds` for the reason that channel exists — *"the silent no-op is
the failure this exists to prevent."* **Nothing consumes it yet, and that is
said in the field rather than implied.**

### ⚠ And `CHARACTER-RECORD-01`'s section was stale in both halves

It read *"six fields today, by assignment… **Nothing has ruled what it
writes**"*. `EVENT-KINDS-01` had described the payload since `PT-1418`, the
writer had been writing it, `replay` had been honouring it — and `clear` handles
**nine** steps, not six fields. Corrected.

## 2 · ⚠⚠ `PT-1675` — THE POOL WAS NEVER WAITING ON ATTACK ROSTERS

I have reported for four slices that `highestReactionTier` has no source: no
`attacks.toml`, no attacks field on `CharacterRecord`, no pick step in chargen.
**Every word of that is true and none of it was the reason Interrupt was dead.**

```dart
return allowance < highestReactionTier ? allowance : highestReactionTier;
```

That is `ATTACKS-01 §10` — *"uses per encounter = the lower of your highest
reaction tier and your ability allowance"* — **read as the pool.**

> **`§12.7` OF THE SAME DOCUMENT EXISTS TO SAY THAT READING IS WRONG:**
> *"`§10`'s lower of tier and allowance caps how many times a **CHAIN** may
> fire. **It does not gate the pool itself.** Opportunity attacks are universal
> — a character with a Dexterity or base-attack allowance has reactions whether
> or not they own Parry, Snap Shot, or Overwatch."*

And `ACTION-ECONOMY-01 §10` says it from the other side: opportunity attacks
*"exist. They are universal. They draw on the reaction pool… **No chain
applies.**"*

**⚠⚠ SO THE ZERO CASE IS `+0` IN BOTH MEASURES, NOT *HOLDS NO CHAIN*** — and
**both documents name the same character for it**: *"a character with Dexterity
+0 and base attack bonus +0 has no reactions at all. That is a Consular, and it
reads correctly."*

With the chain cap inside the pool and no chain acquirable anywhere, **every
character in the product was the Consular** — including for opportunity attacks,
which no chain gates at all. That is what kept `PT-1664`'s Interrupt built,
tested and unreachable for eleven slices.

**⚠ THIS IS NOT A RULING I MADE.** `PT-1697` needed the owner because two
documents disagreed with nothing to reconcile them. Here the reconciling text
**is the document**, it names `§10` explicitly, and it is unambiguous. What was
missing was that anything had read it.

### ⚠ And `§10`'s chain cap is not written anywhere yet, deliberately

No chain exists to cap: Parry, Snap Shot and Overwatch are in `ATTACKS-01` and
in **no extract**, and `§11` makes attacks a third currency with a pick schedule
nothing spends. **A cap with nothing to apply it to would be declared and read
by nothing** — the shape this corpus has a name for. It arrives with the first
chain, and `§10` is where its number is.

`highestReactionTier` is gone from `combatantFrom` too: **declared, defaulted to
zero, passed as a literal zero by its one caller, and gating every reaction in
the product.**

## 3 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| `clear` silently ignores again | three discard cases |
| reported, but nothing discarded | two |
| discarded, but nothing reported | two |
| `discardableSteps` drifts from `clear` | two |
| the chain cap goes back into the pool | all three pool cases, and the seam |

## 4 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 573 | **579** |
| `Loom` | 254 | **254** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 455 | **456** |
| | 1,292 | **1,299** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level.

## 5 · Not done, named rather than skipped

- **Nothing consumes `unknownDiscards`.** It is a fault a check can catch and no
  check catches it yet — the standing `ignoredKinds` has had since it was
  written.
- **The reaction chains themselves are still unbuilt**, and that is now a
  content gap rather than a blocker: Parry, Snap Shot and Overwatch need
  extraction, an attacks field, and `§11`'s pick schedule. **Interrupt and
  opportunity attacks no longer wait on any of it.**
- **Nothing spends a reaction outside a conversation.** `ACTION-ECONOMY-01 §10`'s
  opportunity attack has a pool to draw on now and still no trigger — *an enemy
  leaves your melee reach on foot* is not detected anywhere.

---

## 6 · ⚠⚠ `PT-1701` — THE BUILD IS NOT BROKEN, AND THE CHECK THAT SAID SO COULD NOT SEE THE DECIDING ARTIFACT

`PT-1701` reports the two halves of this slice disagreeing: *"Lodestar's current
`reactionPool` signature now **requires** a `highestReactionTier` argument;
`play_screen.dart` still calls it without one."*

**That is the opposite of what the commits contain, and the reverse of the
direction of the change.** `PT-1675` REMOVED the parameter. Measured just now,
at the two heads named in the ruling:

| Artifact | What it says |
|---|---|
| `Lodestar ce48793` `round.dart` | `reactionPool({dexModifier, baseAttackBonus})` — **no tier** |
| `40ba86b`'s **own committed** `pubspec.lock` | `resolved-ref: ce48793…` |
| `.dart_tool/package_config.json` | `…/Lodestar-ce48793…/` |
| `flutter analyze` | **0 errors** (12 pre-existing infos, all in tests) |
| `flutter build linux --debug` | **✓ Built**, `kernel_blob.bin` 15:00 |
| four suites | 579 · 254 · 10 · 456 — **1,299 green** |

`Tester` is unblocked; `run-app.sh` compiles at HEAD right now.

### ⚠⚠ The reason the two-artifact check cleared a broken build: THE THIRD ARTIFACT IS NOT EITHER OF THEM

`PT-1701` records the diagnostic as *"not a stale pin — pubspec.lock's ref
matches Lodestar's actual HEAD exactly."* **Both of those can agree while the
compiler reads neither.**

> A Dart build resolves through `.dart_tool/package_config.json`. It is
> **generated, gitignored, and per-checkout** — it is not the lock and it is not
> the repo. `flutter pub upgrade` rewrites the lock and that file together, so
> between them they are usually level; **the source tree is the one that moves
> on its own.**

**⚠ And the window is a SHARED WORKING TREE, not two disagreeing commits.**
`Tester` and I edit the same checkout. Mid-slice it holds an edited
`play_screen.dart` calling the new signature against a lock still naming the old
engine — **which produces the reported error exactly**, and produces it from a
tree where `git status` on both repos looks like ordinary in-progress work. I
hit that same error myself in this slice and fixed it by repinning.

**⚠ I cannot reconstruct the minute `Tester` measured, and I am not going to
assert one.** What is provable is the shape: no pair of pushed commits produces
this error — `4a710cb`'s lock names the old Lodestar and its source passes the
old argument; `40ba86b`'s names the new and passes neither. **Every committed
pair is internally consistent.** Only the uncommitted middle is not.

### ⚠ `Tester` stopping was right, and the report is the useful half

Holding a broken build rather than patching around it is the correct call and I
would not want it made differently. The finding that survives is about the
instrument: **"the lock matches HEAD" is two of three artifacts**, and the third
— the one that actually compiles — is the one a shared tree breaks first.

**Not fixed here:** nothing serialises a slice against a second agent building
the same tree. `run-app.sh` always rebuilds, which is what makes it honest, and
it has no way to know the tree is mid-edit. Naming it rather than inventing a
lock for it.
