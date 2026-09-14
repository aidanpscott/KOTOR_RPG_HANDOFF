# TEST 089 — POISON IS REAL IN PLAY, ON BOTH SIDES, AND IT IS RIGHT.
# Both shipped blades poison through the catalogue join; the save is genuinely
# rolled and genuinely goes both ways; five ticks land and then stop; the dice
# are fresh every round; the bar is EXACTLY `#8CB021` and never the accent.
# The player poisons an enemy and an enemy poisons the player by one code path.
# ⚠⚠ BUT THE SAVE IS NEVER SHOWN. `onHitNote` carries `poison — d20 14 = 14 vs
# 10 · takes hold`, five tests assert it, and NO PRODUCTION CODE READS IT — so
# on screen a poisoning blow and an ordinary one are the same line.
# ⚠ And the poison-resist half IS testable, contrary to the brief: I authored a
# resisting target and the tick dropped by exactly the resistance.

## Build state

    Loom            HEAD 61718e0
    KOTOR-RPG-APP   HEAD b918d37  PT-2059: guard every shipped catalogue id
                                  against the real shelf
    lodestar        4901ab97 — lock, pubspec ref and the pub-cache checkout all
                    agree, in both repos

Both trees clean. `check_shelf.py` green at the start and at the end:
`✓ 25 rules files and 50 standard blueprints`.

### ⚠⚠ THE SHIPPED APP BUNDLE IS STALE AGAIN — the same trap as TEST 088

`build/linux/x64/debug/bundle/.../kernel_blob.bin` is stamped
**`2026-09-14 00:17:40`**, which is **older than every commit made today** —
including `5d80601` (the on-hit seam and the green bar, `10:10`) and `12e5309`
(the catalogue join, `11:03`). **Launching the app from the tree gets a build
with no poison in it at all.**

This is now twice in two sessions, so it is worth saying plainly: *the debug
bundle in the repo is not rebuilt when you commit Dart*, and anyone who runs it
to look at today's work will see yesterday's.

There is no `cmake` here, so `flutter build linux` cannot run, and
`flutter build bundle` fails on this app (`Target build_hooks failed: Android
SDK could not be found`). What works is going straight at the Linux assemble
target:

    flutter assemble -dTargetPlatform=linux-x64 -dBuildMode=debug \
      --output=<dir> debug_bundle_linux-x64_assets

I ran that, copied the runnable bundle into my scratchpad, dropped the fresh
`kernel_blob.bin` into **the copy**, and ran that. **The shared tree's bundle
is byte-for-byte as I found it**, verified after.

---

# 1 · NAGA SADOW'S POISON BLADE — player against an enemy

A blueprint naming `catalogue = "g_w_lngswrd03"`, put in the player's hand at
`items/weapons/blaster-rifle` (the path chargen equips). The blow:

> `Naga Sadow's Poison Blade · rolled 24 — d20 20 + attack 1 + Strength 3 ·
> needed 13 — hit · damage 9 — 2d6 2+4 + Strength 3 × 2 critical · 391 left`

**The join works**: the blade is named, the base type's dice are the base
type's, and the poison rides on the catalogue row rather than on the blueprint.

### ✓ Five ticks, and then it stops

`foe-target` has 400 vitality, no weapon and a `never-player` doctrine, so
**nothing but its own tick moves its bar**. I hit it once and then only ended
turns:

| round | vitality | tick |
|---|---|---|
| the blow | 400 → 391 | *(blade, not poison)* |
| 1 | 391 → 384 | **7** |
| 2 | 384 → 377 | **7** |
| 3 | 377 → 365 | **12** |
| 4 | 365 → 356 | **9** |
| 5 | 356 → 347 | **9** |
| 6 | 347 → 347 | — |
| 7 | 347 → 347 | — |

**Exactly five, matching `rounds = 5` on the catalogue row**, and then nothing.

### ✓ The dice are fresh every round

`7 · 7 · 12 · 9 · 9`. Not one number five times. **The 12 is the 2d6 maximum**
and is arithmetically impossible on the other blade's 2d4, which is what makes
this pair of runs discriminating rather than merely plausible.

**And the control proves nothing else was moving bars:** `foe-control`, placed
beside it and identical, sat at **400 of 400 through all seven rounds**.

### ✓ The save is real and goes BOTH ways

The bar turns green the instant an `Ongoing` attaches, so each hit on a clean
target is one readable save. On `foe-control`, DC 10:

| hit | bar right after | meaning |
|---|---|---|
| first | `#B0342A` still red | **save made — no poison** |
| second | `#8CB021` green | **save failed — poison took hold** |

So a landed blow does **not** automatically poison. Both branches observed on a
shipped weapon at its own DC.

---

# 2 · ⚠⚠ AND THE SAVE IS NEVER PUT ON SCREEN

`_onHitTakesHold` builds exactly the sentence a player needs:

```dart
note: 'poison — $shown = ${out.total} vs ${save.dc} · takes hold'
note: 'poison — $shown = ${out.total} vs ${save.dc} · resisted'
```

It is returned as `AttackReport.onHitNote` (`attack.dart:1051`). **Nothing
reads it.** `grep -rn "onHitNote" lib/` returns three hits — the field
declaration, the constructor parameter and that one assignment — **and no
consumer anywhere**. `AttackReport.line`, the one string a player reads, is
built from the weapon, the to-hit derivation, the range note, the damage
derivation and the vitality; `onHitNote` is not in it.

**The test suite asserts it five times** — `attack_seam_test.dart:250, 302,
309, 310, 318` and `catalogue_join_test.dart:87` — all against the returned
object. So the value is verified and the screen is not.

**Measured, not just read:** every line I captured this session, including the
one that poisoned `foe-target` and the two that decided `foe-control`'s fate,
ends at `… 391 left` with no poison clause. **A blow that poisons you and a
blow that does not are the same sentence.**

**Why this matters more than a missing nicety.** The field's own docstring says
it: *"`PT-1326`, the derivation IS the return value. A poison that silently
failed to land and a weapon that never had one are the same absence and
different facts."* Right now they are the same absence **and the same screen**.
And this file already carries `PT-1464` about precisely this shape, two hundred
lines up — *"THE PLAYER'S OWN LINE WAS COMPUTED AND NEVER RENDERED… `Tester`
never saw its own attack across FOUR fights"*. Same failure, one field over.

The only reason I could confirm the save at all is that the **bar colour**
happens to expose the outcome. Remove that and the mechanic would be invisible.

---

# 3 · THE GREEN BAR — measured, not eyeballed

`C.poison` is `0xFF8CB021` and `C.accent` is `0xFF1AB28C`. I sampled the
rendered pixels rather than calling it green:

| bar | measured | |
|---|---|---|
| poisoned enemy | **`#8CB021`** | exactly `C.poison` |
| unpoisoned enemy (control) | `#B0342A` | exactly `C.alert` |
| **poisoned == accent?** | **no** | the collision is genuinely avoided |

**The colour-collision fix holds.** A poisoned bar cannot be mistaken for a
healthy one, because the healthy teal `#1AB28C` and the sickly `#8CB021` do not
sit near each other in any channel.

### ✓ And it is live state, not a permanent mark

| | bar |
|---|---|
| ticks 1–4 | `#8CB021` |
| the frame the **fifth** tick lands | `#B0342A` |
| every round after | `#B0342A` |

It goes false the round the last tick is spent, exactly as the docstring
promises — the `Ongoing` is dropped rather than kept at zero.

---

# 4 · THE PLAYER GETS POISONED THE SAME WAY

`foe-striker` carries the same blade through the same catalogue join and walks
over to use it:

> `foe-striker.probe.03: Naga Sadow's Poison Blade · rolled 21 — d20 18 +
> attack 1 + Strength 2 · needed 13 — hit · damage 5 — 1d6 3 + Strength 2 ·
> 9 left`

| the player's own bar | measured |
|---|---|
| 14/14, before | `#1AB28C` — `C.accent`, healthy |
| 14/14, striker just joined | `#1AB28C` |
| **9/14, right after the blade landed** | **`#8CB021` — `C.poison`** |

**One token, one code path, both sides.** `play_screen.dart:418` computes
`poisoned:` from `c?.ongoing` for every row in the fight, and the enemy roster
and the party card are the same widget — which is why the enemy's horizontal
bar and the player's vertical strip both changed to the same value.

The character then died, 9 → 0, to the blade plus its own tick. **That is the
mechanic working**, not a defect: a level-1 character with 14 vitality has no
business standing next to 2d6 a round for five rounds.

---

# 5 · ⚠ THE RESIST HALF *IS* TESTABLE — and it works

The brief said *"likely nothing shipping resists poison yet, so this may not be
testable directly."* Nothing shipping does — but a package can author one, and
the chain is already wired: `wornBy` takes resists from every non-weapon slot,
and `fight.dart:359` hands the same map to `endRound`. So I authored a mask
with `[item.resists] poison = 3` and gave it to one of two otherwise identical
targets, both struck by the **GenoHaradan** blade (2d4).

| | tick 1 | 2 | 3 | 4 | 5 | |
|---|---|---|---|---|---|---|
| `foe-plain` — nothing worn | 3 | 7 | 5 | 4 | 7 | raw 2d4, all inside 2–8 |
| `foe-resist` — mask, `poison = 3` | **2** | **3** | **0** | **3** | **1** | 2d4 − 3, all inside 0–5 |

Mean `5.2` against `1.8`. **And a tick of `0` appeared** — the floor working,
from a 2d4 that rolled 2 or 3. Both sequences vary round to round, so both are
rolling fresh dice; the resisting one is simply rolling the same dice and
losing three off every one.

*(This also re-confirms `PT-2029`'s tick path, which `5d80601`'s own commit
message flagged as having been written while inert.)*

---

# 6 · THE GENOHARADAN BLADE — the second shipped weapon, and it is distinct

`catalogue = "geno_blade"` → `2d4`, five rounds, **DC 14**. Ticks on a clean
target: `3 · 7 · 5 · 4 · 7`, five of them, then stop.

**The two blades are measurably different weapons**, which is the point of
testing both: Naga Sadow's rolled a **12**, impossible on 2d4; GenoHaradan
never exceeded 7 and its DC is four points harder. Both numbers come off their
own catalogue rows, so the join is reading the right row per blueprint rather
than one shared effect.

*(Worth knowing, from the source rather than from me: the **milder** poison
carries the **harder** save — `POISON_DAMAGE_MILD` is DC 14 and
`POISON_DAMAGE_AVERAGE` is DC 10. That is what `items.toml` says and I am not
calling it wrong, only noting it reads backwards at a glance.)*

---

## Method notes, and one thing that was mine

- **The tick amount is printed nowhere**, so every number above is a
  round-over-round **vitality drop**. That is only sound if nothing else can
  touch the target, which is what the `never-player` doctrine, the unarmed
  targets, the 400 vitality and the untouched control are all for.
- ⚠ **Mine, not the product's:** twice I confounded a tick sequence by
  continuing to attack the target I was measuring, and had to let the poison
  expire and start the measurement again. The numbers reported are from runs
  where exactly one blow landed and nothing else was pressed but *end turn*.
- ⚠ **Also mine:** my first attempt to walk past a foe spent five turns
  attacking it instead, because the foe was directly east and `Right` is both
  *move* and *attack*. No harm; it is why `foe-control` reads 260 of 400.

## What I did not do

- **Did not test a poison whose save leaves `half` or `instead`.** Both are
  refused by name (`a made save leaving half is not modelled for something that
  ticks`) and no shipped row carries one.
- **Did not test two different poisons stacking** as two separate `Ongoing`s,
  though I did stack the same one by accident and it behaved additively.
- **Did not test an ability-damage poison** — named in the tokens docstring as
  the half this build cannot model.
- **Did not re-test** the palette (TEST 088), `PT-2029` (TEST 087) or
  `TARGETING-01`. Noted in passing only: chargen now writes a `body` slot
  (`e1f1096`), which is the other end of TEST 087's finding.

## State

- **New package `poison-probe` is mine and left on disk**, in its run-2 shape:
  two areas' worth of history in one file, four item blueprints, two doctrines,
  two creatures, and a copy of the shelf's `clothing.item` so chargen's armour
  row resolves. It loads with **no problems**.
- ⚠ **`blueprints/items/weapons/blaster-rifle.toml` is deliberately not a
  blaster rifle** — it is whichever poison blade the run needed, authored at
  that path because `items/weapons/<base id>` is the only way to put a chosen
  weapon in the PLAYER's hand. Declared so nobody reads it as a mistake.
- ⚠ **`KOTOR-RPG-APP/build/flutter_assets/` and a scratch `--output` dir now
  hold my `flutter assemble` output** — gitignored, regenerable, and they do
  not shadow the desktop bundle, which is byte-for-byte as I found it.
- Saves from two runs in `poison-probe`, not cleaned up. One total-party defeat,
  deliberately.
- My app PIDs `104325` and `107951` killed by PID, confirmed gone. No Loom ran
  this session and nothing of Coder's was touched.
