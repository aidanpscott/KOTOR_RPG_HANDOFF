# TEST 120 — Force Confusion works end to end, and the droid fix went to the wrong classifier

**Build.** App **`a384154`** ("Force Confusion works, and four droid species
stop being sentients — PT-2450"), tree clean, built from `git archive` of
that sha. The committed lock resolves Lodestar **`54c5394`**, and that is the
pub-cache checkout `package_config.json` compiles against. `check_shelf.py`
clean: 29 rules files and 65 standard blueprints.

⚠ **The routing named `8d2bfb6`, which is in none of the three repos** —
not `HANDOFF`, not `KOTOR-RPG-APP`, not `Lodestar`. `a384154` is the commit
that carries the fixes and is what I tested.

**Verdict.** **Force Confusion is now genuinely complete** — every clause of
the mechanic confirmed in play, including the two that needed real staging.
**The droid fix is not.** It was applied to a classifier that only ever
serves the player; every enemy on the board is still classified by a second,
untouched copy, so **four of five droid species can still be distracted, and
can now also be confused** — a droid joining the party, which the shelf row
calls immune.

---

## The droid classifier — fixed in one place, and the defect lives in the other

`kindOf` in `power_target.dart` was corrected exactly as ruled: it takes a
required `droids` set, sourced from `species.toml`'s `is_droid`, with a
comment refusing a `{'droid'}` default *"because that is exactly the bug"*.
That part is right.

**But `kindOf` has one caller**, `play_screen.dart:1719`, and its own comment
says what it is for:

> ⚠ THE PLAYER'S KIND IS KNOWN, and a placement's is not — `PT-1488`. A
> record carries `species.id` and `chassis`; **a blueprint carries neither**.

A **placement's** kind is computed somewhere else entirely —
`attack.dart:282`, in `Present.placed`:

```dart
kind = p.chassis != null && p.chassis!.isNotEmpty
    ? 'droid'
    : p.species == null || p.species!.isEmpty
    ? null
    : (p.species == 'droid' ? 'droid' : 'sentient');
```

That is the same `== 'droid'` string test, untouched. `Fight.isDroid` reads
`kinds[handle] == 'droid'`, and `kinds` is built from `Present.kind`. So the
fix reached the one creature that was never the problem and missed every
creature that was.

### Measured, one blueprint per species, all five directly

A board with one sentient guard and five droids differing **only** in
`species`. The cast picker prints them in one line:

```
Force Distraction — 1 Guard · 2 Bare Droid ⚠ Force Distraction does not affect a droid
  · 3 Astromech · 4 Assassin Droid · 5 Battle Droid · 6 Remote · esc
```

The ⚠ is on `Bare Droid` alone. Then each one cast at individually, rather
than inferred from the marker:

| `species` | picker | cast |
|---|---|---|
| `droid` | ⚠ marked | **refused**, nothing spent |
| `droid-astromech` | unmarked | `8f — 127 → 119 · dr-astro.dr.03 is distracted` |
| `droid-assassin` | unmarked | `8f — 119 → 111 · dr-assas.dr.04 is distracted` |
| `droid-battle` | unmarked | `8f — 151 → 143 · dr-battle.dr.05 is distracted` |
| `droid-remote` | unmarked | `8f — 143 → 135 · dr-remote.dr.06 is distracted` |
| `human` (control) | — | `8f — 135 → 127 · guard.dr.01 is distracted` |

**And it is not only Distraction.** Confusion goes through the same kind, so
it is a separate claim and was measured separately:

```
Force Confusion · 20f — 159 → 139 · at dr-battle.dr.05 · dr-battle.dr.05 turns on its own side
```

A **droid is now fighting for the party** — the row's own sentence is *"This
power only works on sentients; beasts and droids are immune."* Before
PT-2450 this was one power leaking; it is now two.

## Force Confusion — every routed clause, confirmed

### It applies, and it says so

```
Force Confusion · 20f — 159 → 139 · ceiling −4 to 155 · at guard.cf.01 · guard.cf.01 turns on its own side
```

### Both directions

**It attacks them.** The confused guard's own attack line, round after
round, against `droid.cf.03`, which fell `400 → 398 → 396 → 395`. On the
wipe board a confused Bruiser crossed eight squares to reach its former ally
and the two traded down to `338` and `341` of 400; a confused Bruiser also
killed the frail guard outright.

**They attack it.** This one needs staging, and the naive setup hides it:
with the player adjacent, the doctrine prefers the player every time —
`ally.cf.02` walked from (3,0) to (1,1), **around** an adjacent confused
enemy, to reach me. Both are in its `foes` list (`fight.dart:729`,
`side(c) != mine`); it simply chooses the player.

So I removed myself as the better target and moved five squares clear:

```
ally.cf.02: 400 → 399 of 400        (its former side struck it)
Whisper:    71 of 86, unchanged for four consecutive rounds
```

The player took no damage across those four rounds, so the point off the
confused creature cannot be attributed to me. Confirmed again, unambiguously,
on the wipe board: a confused `frail.wp.01` went `20 → 7` under its old
side's blows while the player stood clear.

### One of each kind at a time — and it is the active instance, not a flag

```
you already have guard.cf.01 turned · 9 rounds left
```

Force unchanged at 139, Action still available — the refusal is free, names
the handle **and** the remaining clock. ⚠ And it is a real, repeatable limit
rather than K2's latched global: once the first expired, **a second cast on a
different sentient succeeded** (`ally.cf.02 turns on its own side`), which is
`PT-2439` ruling 2's whole point.

### It returns to its original side

Ten rounds after the cast the picker reads:

```
Force Confusion — 1 Second Guard · 2 Guard · 3 Battle Droid ⚠ …
```

`Guard` is `guard.cf.01`, back in the enemy list it had left. While confused
it was **absent** from that list, which is the same fact from the other side.

### No stand-at-1 — it drops past zero

A 20-vitality sentient, confused, then beaten down by its former allies:

```
frail.wp.01: 20 of 20  →  7 of 20  →  -6 of 20
```

**Minus six.** No stand-at-1, which is the party-exclusive rule
`partyWiped`'s `isParty` exists to keep. Seen three separate times across
runs (`-6`, `-5`, `-3`).

### A confused enemy standing is not a win

This is the clause the fixture had to be built around, and it took three
attempts to stage — recorded because the reason is itself the finding.
**Confusion works too well to test naively:** two heavies left within reach
of each other just fight, and leave the player at full health; a confused
*frail* one is killed by its old side long before the player falls. So the
creature to confuse has to be unreachable and has to outlive the player. I
sealed a Bruiser in a one-tile pocket of **water** — impassable like a wall,
but it does not block sight, so the power can still be aimed at it.

```
Whisper: 60 → 46 → 31 → 20 → 8 → falls
bruiser.wp.02 (confused): 400 of 400, standing, untouched throughout

YOU FALL, AND NOBODY IS LEFT STANDING. That is a total party defeat,
and it is the only thing that kills.
```

A confused enemy standing at full health does **not** keep the party alive
and does **not** read as a win. Confirmed.

## Also noticed

* ⚠ **Force Confusion can be aimed at nine or ten squares** — the far pocket
  Bruiser was targetable from across the board. No range limit beyond sight,
  which is worth knowing and is not stated on the row.
* ⚠ **A save the app will not accept loads into an empty party, silently.**
  Building the caster with Constitution 3 produced a save the menu counted as
  `1 unreadable` (Continue greyed); Constitution 8 produced one that *loaded*
  — board drawn, area named `m04-wipe` — with `your party · nobody else` and
  no character, no message, no error. My save writer bypasses chargen so the
  record may well be invalid input; **the silence is the part worth a look**,
  not the rejection.
* The library carousel still shows four cards and does not scroll.

## Fixture

`tester-mind`, `0 Mind Bench (Tester)`. Two boards added for this batch:

* **`m03-droids`** — one sentient and one blueprint per `is_droid` species,
  so a single picker line reads all five classifications at once. The fastest
  way to re-check the classifier after any fix.
* **`m04-wipe`** — `frail` (20 vitality) and two `bruiser`s (Strength 30).
  ⚠ The water pocket at (10,0) is load-bearing, for the reason in the item
  above; and ⚠ the caster must keep Constitution 16, because 8 loads to an
  empty party and 3 will not load at all.
