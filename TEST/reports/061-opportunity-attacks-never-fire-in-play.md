# TEST 061 — opportunity attacks never fire in play, reproducibly, though every piece I can read checks out

**Built against:** `run-app.sh` (always rebuilds). KOTOR-RPG-APP `4c47de1`
(*ACTION-ECONOMY-01 §10 — an enemy leaving your reach is struck at*), PID
`776527` (a01-melee) then `780497` (a02-droid, after switching `[entry]`,
same HEAD, fresh relaunch per the package-config-caching lesson from `TEST
060`). Lodestar `ad699f5` (*reactionsMax — the pool's denominator*), the
commit directly under `4c47de1`'s pin. `pubspec.lock` matches. ⚠ HEAD has
since moved to `26e1540` while I was writing this up — unrelated to §10 by its
own message, named for precision rather than silently left implied current.

**Instrument:** PID-scoped via `run-app.sh`'s `exec`. Both launches killed by
PID. Coder's Loom `517968` confirmed untouched throughout — no Coder app was
running to disturb either.

**Task:** confirm live, not just by Coder's own engine-level tests, whether
leaving melee reach draws a Strike, whether Disengage prevents it, and
whether a droid correctly makes none.

---

## Fixture

`opportunity-attacks`, two areas, identical geometry: a 6×1 corridor, an
explicit arrival two squares from the board edge, a guard adjacent to it.
`a01-melee`'s guard is `species = "human"`; `a02-droid`'s is
`species = "droid"`, otherwise byte-identical blueprints. Loom's `verify`: 0
structural problems on either (only the standard no-doors-between-areas
notices). The 2-square gap on the empty side means retreating one step takes
distance from the guard from 1 (inside melee reach) to 2 (outside it) —
exactly `leavesReach`'s trigger, read from `combat.dart` before building
anything.

## 1. The ordinary pieces all work

- **The guard's own Strike, on its turn**: fired correctly and repeatably —
  `"guard.melee.01 closes 1 square — 2 to 1 · unarmed · rolled 17 … hit ·
  damage 1"`. Dice, distance-closing, damage — all correct.
- **Disengage, as a UI action**: pressing `d` spent the Action (the pip
  dimmed) and printed `"disengaging — your movement provokes nothing this
  turn"`, exactly matching the source I read before testing (`Budgets.disengage`
  spends the Action first, sets the flag only on success).
- **The droid's own Strike, on its turn**: also fired — `"guard.droid.01 …
  unarmed … hit … damage 1"`. ⚠ Worth naming separately from what I was
  asked, not folded into it: `_wouldFight`'s comment reads *"melee is closed
  to every droid chassis,"* and this droid swung in melee on its own turn
  regardless. Whether `§4`'s rule is scoped to opportunity attacks only or is
  a wider ruling this build doesn't yet enforce elsewhere, I did not chase —
  it wasn't the ask, and I'm not the one who gets to decide which reading is
  right. Named so it isn't lost.

## 2. ⚠⚠ The trigger itself never fired — confirmed reproducibly, not a fluke

From adjacent to `guard.melee.01`, stepped back to distance 2. **No strike,
no log line, no damage, three separate times**: once cold, once after
re-approaching and retreating again, once more after pressing Disengage
first (which should have been redundant — nothing to prevent if nothing
fires). Vitality held at `10 of 11` the entire sequence; the recap line
never grew a new clause. Against the droid, from identical geometry: also
nothing — but that half is **unconfirmable as "correctly excluded"** given
the base case already fails for an organic guard that has every reason to
swing.

I read every piece of the chain before concluding this was real rather than
my own error:

- `leavesReach(was: 1, now: 2, reach: 1)` — `was <= reach && now > reach` —
  true by the numbers I placed.
- The watcher's own reaction pool: `combatantFrom` (the NPC path, not just
  the player's) computes `reactionsLeft` via `reactionPool(dexModifier: 0,
  baseAttackBonus: 1)` for this exact blueprint — `byDex` bands to 0,
  `byBab` bands to 1 (the `[1, 6, 11]` ladder), so the guard should hold
  **1** reaction, not zero. I did not find a second, zero-supplying
  construction path.
- Sight: the corridor has no walls at all — `canSee` has nothing to refuse
  against.
- Sides: the guard is plainly hostile — it's already landing ordinary
  Strikes against me all fight.
- The wiring order in `_step`: `_reachSnapshot` runs before `_at` updates,
  `_opportunities` runs after — matching the source's own stated reasoning
  for that order.

Everything I can read from outside the running process says this should
fire. It did not, three times, against a build whose own commit names a
152-line `test/opportunity_attack_test.dart`. My read of why the two
disagree: those tests almost certainly call `Fight.opportunityAttacks`
directly with hand-built `wasApart`/`nowApart`/`sees` callbacks, which
proves the **engine's** clause composition and proves nothing about the
**app's** wiring in `_step`/`_reachSnapshot`/`_opportunities` — the exact
seam a real playthrough exercises and a unit test aimed at the engine does
not. I did not go further into the app's own source hunting for the specific
line, because confirming and finding what's next to a defect is mine; fixing
it is not.

---

## What I did not check

- Why the trigger doesn't fire — traced every input I can read from outside
  the process and they all say it should; did not add print statements or
  otherwise instrument the running app to find the exact break, since that
  starts to shade into diagnosing-to-a-patch rather than confirming.
- Whether Disengage actually prevents anything, since there is nothing
  currently observable to prevent — this half of the ask is blocked on the
  trigger working at all, not answered.
- Whether droids are correctly excluded — same block: indistinguishable from
  the trigger failing generally.
- Whether `§4`'s "melee is closed to every droid chassis" is meant to apply
  to the droid's own ordinary turn-based Strike — flagged, not chased.
- A reach weapon (`hasReach`, reach 2) — this fixture only exercises ordinary
  melee reach 1.

## State

- **`opportunity-attacks` unchanged** — no edits, played only. Two new
  saves, `reach-tester.sav` and `droid-reach-tester.sav`; the package had
  none before this session. `[entry]` reset to `a01-melee` afterward.
- No other package touched — `tester-probe`, `two-enemies`, `mixed-faction`,
  `ranged-detection`, `endar-spire`, `base-rules`, `taris-undercity` all
  confirmed untouched by mtime.
- The NWN install was not read or written.
- Both app processes killed by PID; Coder's Loom `517968` untouched —
  checked before and after both launches.
