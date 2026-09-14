# TEST 087 — BOTH HALVES OF PT-2029 ARE REAL, AND BOTH ARE HALF-APPLIED.
# Creature versus creature they work exactly as specified: armour takes a
# target from `needed 13` to `needed 22`, a MASK grants its resistance and adds
# no Defence, a compound weapon loses only the kind that is resisted, and a
# weapon's own resists table counts for nothing.
# ⚠⚠ THE PLAYER'S OWN BLOW READS NEITHER. `_defenceOf` passes no armour term
# and the player's `strike` passes no `resists` at all — so an armour-class-9
# creature is `needed 13` to the player and a `fire = 99` mask stops nothing.
# ⚠ And the player can never be armoured or resistant in the first place.

## Build state — and the binary is not HEAD

    Loom            HEAD b1a60fd  pin: lodestar 047e155 — corrected
    KOTOR-RPG-APP   HEAD a8c75b0  pin: lodestar 047e155 — corrected
    ⚠ MEASURED      1eb6da3  worn: everything worn, not just the body
                             -- PT-2029 slice d, option B

**⚠ THE THING THAT COMPILES IS NOT THE THING AT HEAD, and I am naming it
rather than declaring a commit I did not run.** `kernel_blob.bin` is stamped
`2026-09-14 00:17:40`, which is `1eb6da3`. The two commits after it are
`03f5f15` and `a8c75b0`, both repins: `git diff 1eb6da3 HEAD` touches
**`pubspec.lock` and nothing else**, so every `lib/` file I quote below is
byte-identical to what ran.

**Engine: `7981fdf4…` is what is in the binary.** `package_config.json` was
rewritten at `00:59` — after my build — and now names `64a2a52…`. I diffed the
two checkouts rather than assuming: **`combat.dart` and `item_open.dart` are
byte-identical**, and only `effect.dart` and `round.dart` differ, neither of
which is on this path. **So nothing below is qualified by that drift.**

Both trees carry Coder's uncommitted `pubspec.lock`; I did not touch it.
`check_shelf.py`: `✓ 25 rules files, all identical to what the extracts
generate` — re-run at the end as well as the start, because Coder regenerated
the extracts mid-session in a parallel shell.

---

# 1 · CREATURE AGAINST CREATURE — all four claims confirmed

### ✓ Armour changes the attack roll, and it is very much felt

Two creatures, both wearing **armour class 9** on `body` (+9, `max_dex +0`).
Every line the fight printed against one of them:

> `mate.probe.01: Resistant Burner · rolled 20 — d20 15 + attack 1 +
> Strength 4 · **needed 22** — miss`
> `… rolled 19 — d20 14 … needed 22 — miss`
> `… rolled 17 — d20 12 … needed 22 — miss`
> `… rolled 16 — d20 11 … needed 22 — miss`
> `… rolled 22 — d20 17 … **needed 22 — hit**`

`10 + Dexterity 0 + class 3 + **armour 9** = 22`, against the bare **13** that
every unarmoured creature in this package printed. **Three consecutive rolls
of 20, 19 and 17 missed** — all three are comfortable hits against 13. That is
the felt difference Coder asked for, and it is large.

### ✓ A MASK grants its resistance and adds nothing to Defence

A creature wearing **only** `mask = fire-mask` (`base = "object"`,
`[item.resists] fire = 5`), struck by a compound weapon:

> `mate.probe.01: Resistant Burner · rolled 25 — d20 20 + attack 1 +
> Strength 4 · **needed 13** — hit · **damage 26** — 2d6 2+4 + 2d6 fire
> 3+6+1+6 + Strength 4 × 2 critical · **379 left**`

Two facts in one line:

- **`needed 13`.** The mask is worn and it added **nothing** to Defence —
  `wornBy` taking its bonus from `body` alone, working.
- **26 printed, 400 → 379 = 21 landed.** `26 − 21 = 5`, which is the mask's
  fire resistance to the point.

### ✓ And the reduction is PER PART, which is the whole of `PT-2029`

That line decomposes exactly as `afterResistanceParts` says it should:

| part | kinds | rolled | resisted at | landed |
|---|---|---|---|---|
| base | `slashing` | `2d6 2+4` = 6, `+ Strength 4` | fire 5 does not apply | **10** |
| bonus | `fire` | `2d6 3+6+1+6` = 16 | −5 | **11** |
| | | printed **26** | | **21** ✓ |

**Not fully blocked and not fully ignored** — the fire part went 16 → 11 and
the slashing part was untouched. This is the Baragwin-repeater case Coder
named, built from a long sword and a typed bonus of a different kind.

### ✓ A weapon in a weapon slot is not worn

Both creatures held **`Resistant Burner`** — a compound weapon whose own item
table says **`fire = 99`**. If a weapon counted as worn, every fire point
would have vanished. Three hits, printed against the bar:

| printed | vitality | landed | reduced by |
|---|---|---|---|
| `damage 16 — 1d6 5 + 2d6 fire 4+3 + Strength 4` | 376 → 360 | **16** | **0** |
| `damage 21 — 2d6 1+1 + 2d6 fire 6+2+6+1 + Strength 4 × 2 critical` | 360 → 339 | **21** | **0** |
| `damage 30 — 2d6 4+4 + 2d6 fire 4+6+4+4 + Strength 4 × 2 critical` | 339 → 309 | **30** | **0** |

Seven, fifteen and eighteen points of **fire** landed in full through a
`fire = 99` table. `wornBy`'s `e.key.startsWith('weapon_')` skip, holding.

---

# 2 · ⚠⚠ AND NONE OF IT REACHES THE PLAYER'S OWN BLOW

This is the half that is not built, and it is the half a player actually
touches. **Same room, same items, same fight — the player swinging.**

### ⚠⚠ Armour does not raise Defence against the player

`foe-armoured` wears `body = items/armour/plate`, armour class 9, in a package
whose bare creatures print `needed 13`:

> `Probe Burner · rolled 7 — d20 2 + attack 1 + Strength 4 · **needed 13** —
> miss`  *(twice, two separate turns)*

**I confirmed the target rather than counting squares** — selecting
**Foe Armoured** in the roster highlighted the token directly above me, and
that is the token I stepped into. The creature that reads **22** to a
companion reads **13** to the player.

### ⚠⚠ Resistance reduces nothing the player deals

`foe-fireproof` wears `mask = fire-wall`, **`fire = 99`**. Three hits with the
same compound weapon:

| printed | vitality | landed | reduced by |
|---|---|---|---|
| `damage 11 — 1d6 4 + 2d6 fire 1+2 + Strength 4` | 400 → 389 | **11** | **0** |
| `damage 15 — 1d6 5 + 2d6 fire 1+5 + Strength 4` | 389 → 374 | **15** | **0** |
| `damage 11 — 1d6 3 + 2d6 fire 2+2 + Strength 4` | 374 → 363 | **11** | **0** |

A ninety-nine point fire resistance removed **nothing**.

### The cause, and it is two arguments

**`play_screen.dart:5561`** builds the player's swing with

```dart
defence: defenceFrom(_defenceOf(p)),
```

and `_defenceOf` (`play_screen.dart:6371`) is the whole of it:

```dart
List<Term> _defenceOf(PlacedCombatant p) => defenceTerms(
      dexterityModifier: p.combatant.dexModifier,
      classBonus: classDefenceBonus(p.characterClass, p.level),
    );
```

**No `armourBonus`. No `maxDex`.** And the `strike(...)` call it sits in —
`play_screen.dart:5519–5581` — **passes no `resists:` at all**, so `strike`'s `Map<String,int> resists = const {}`
default applies and `afterResistanceParts` is handed an empty table.

One file over, the creature's own blow passes both:

```dart
// fight.dart:622
armourBonus: armourOn(d.target!.handle).bonus,
maxDex:      armourOn(d.target!.handle).maxDex,
// fight.dart:582 and :782
resists: resistsFor(d.target!.handle),
```

**The maps are correct and complete.** `play_screen.dart:5321` builds both
`resists` and `armour` from `_present`, *"every creature, not only the
player"*, and the comment beside it says exactly what this slice was for. The
data arrives. The player's blow simply never asks for it.

**This is the thirteenth instance of the shape this corpus keeps naming**, and
`strike`'s own docstring names it twice, unprompted, about these very two
parameters:

> `distanceSquares` — *"it gates BOTH SIDES because both sides come through
> here… a reach rule applied to one of them would be the shape this corpus has
> found eleven times."*
> `resists` — *"**here because both sides come through here**… a reduction
> applied in only one of them would be the shape this corpus has now found
> twelve times."*

The parameter was put on `strike` for precisely this reason, and the player's
call site is the one that did not fill it in.

### ⚠ And the player cannot be armoured or resistant at all

Coder's brief says *"an armored character (**player** or enemy)"*. **Scoped
negative, and here is where I looked.**

- **Chargen never writes a `body` slot.** `LedgerWriter.equipmentPayload`
  (`ledger_writer.dart:186–196`) returns `route`, `credits`, `items`,
  `weapon_r_1`, and the two explanatory strings — and nothing else. The
  Equipment step displays `armour  clothing` and that row reaches no
  `[equipment]` map.
- **There is no equip surface in play.** I grepped `lib/play/play_screen.dart`
  for `'body'`: **one hit, and it is a comment.** Nothing writes the slot.
- **And the player is not in the Fight's maps either.** Both `resists` and
  `armour` are built `for (final x in _present)` — placements. The player is
  not a placement, so an NPC striking the player looks up `(0, null)` and
  `const {}` regardless.

So the player half of *"armor now affects Defence for real"* is not merely
unwired at the call site — **there is no path by which a player character can
be wearing armour in the first place.** My own Defence line read
`defence base 10 + Dexterity 2 + class 3 = 15` in the first run and
`… + Dexterity 3 + class 3 = 16` in the rest — terms, total, **and no armour
term**, with nowhere for one to come from.

---

## Method — and why the fixture is shaped the way it is

**⚠ The play screen keeps exactly ONE combat line, and that is the binding
constraint on testing combat.** The line shown is whoever acted immediately
before the player in initiative; everything else is overwritten. I did not
take that on inspection — I recorded the screen with `ffmpeg` at **30 fps**
across a whole round and found **zero** intermediate frames, twice. In a room
of seven creatures, six of the seven lines a round produces cannot be read at
all.

So the fixture went through four shapes before it could measure anything, and
the last one is the only one that works: **put everything under test on the
TARGET side, and use exactly one attacker whose line survives to my turn.** In
the final run both combatants carry identical kit, so whichever of the two
lines the initiative roll leaves on screen answers the same question.

Two observables carry the whole report, and both are printed:

- **`needed N` IS the target's Defence.**
- **The printed damage is the UNRESISTED roll and the vitality bar is what
  landed** (`attack.dart:939` — `amount: landed`, *"what landed, not what was
  rolled"*, while `outcome.damage.line` still prints the blow the weapon
  produced). **printed − drop IS the resistance.**

## Also seen, not filed

- **A `[[never]] match = { role = "player" }` creature still hits the player on
  a REACTION.** Walking a row of eight foes that every turn printed
  `holds — none:all-excluded`, my character went 12 → 10 → 7. The strip shows
  `reaction · per encounter` spent. I think this is probably correct — an
  opportunity attack is not a choice of target, and the exclusion governs
  choosing — but it is worth a ruling, because it is the one way an excluded
  creature can still hurt what it may never target.
- **`wornAt` builds `'blueprints/$path' + '.toml'` literally**
  (`attack.dart:1075`), as do `equippedFrom`, `consumableAt` and `supplyAt`.
  That looked like a `PT-1991` gap — an armour authored in Loom today lands as
  `.item`. **It is not one:** `openItem` resolves the dual read itself
  (`PackageFiles.resolve(path, PackageFiles.item)`), so both extensions open.
  Checked before filing rather than after.
- **`fc95d18 fight: the fallback doctrine is lent, not handed over entire`** is
  in the tree — TEST 086's ⚠⚠ finding looks addressed. **I did not exercise
  it**: every creature in this fixture names its own doctrine precisely so the
  fallback could not confound the measurement. Naming it, not confirming it.

## What I did not do

- **Did not exercise `max_dex`.** Armour class 9 is `max_dex +0` and every
  creature here has Dexterity 10, so the cap never bit. The capping branch is
  untested by this run.
- **Did not test droid plating** (`light` / `medium` / `heavy`) — same `body`
  slot, same `defence` column, same read.
- **Did not test a target that resists BOTH kinds** of a compound weapon, nor
  `mergedResists` taking the per-kind maximum across two worn tables.
- **Did not re-test TARGETING-01, the extension rename, the grenade save types
  or the Long Sword table.** All closed in TESTs 084–086 and untouched here.

## State

- **`resist-probe` is mine and is left on disk**, in its final shape: two
  creatures, two doctrines (`plain-aggro`, `never-player`), five item
  blueprints, one area. ⚠ **It was rewritten four times during this session**,
  so it no longer contains the eight-foe gallery that produced §2's readings —
  the area file's header comment records what each shape was for.
  It loads with **no problems**.
- ⚠ **`blueprints/items/weapons/blaster-rifle.toml` is deliberately not a
  blaster rifle.** It is the compound melee weapon under test, authored at that
  path because `items/weapons/<base id>` is the only way to put a chosen weapon
  in the PLAYER's hand — chargen resolves the class array's weapon name to that
  path (`starting_weapon.dart:122`). Declared so nobody reads it as a mistake.
- `targeting-probe`, `strongroom-rebuilt`, `locked-and-trapped` and
  `tester-strongroom` **untouched**.
- Four new-game runs' saves in `resist-probe`, not cleaned up.
- All app PIDs mine were killed by PID and confirmed gone. Coder's Loom and
  any Coder-owned app were left alone.
