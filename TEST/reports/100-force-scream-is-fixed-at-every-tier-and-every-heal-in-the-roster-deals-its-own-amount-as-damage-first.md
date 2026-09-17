# TEST 100 — Force Scream is fixed at every tier, and every heal in the roster deals its own amount as damage first

**Build under test.** KOTOR-RPG-APP `d33bc2d` *"PT-2287: a buff stops at its own radius, and the
guard that proves it"*. Lodestar `c9ddd86`, clean, and `pubspec.lock`'s resolved ref matches the
pub-cache checkout that compiled (`Lodestar-c9ddd867…`, `Lens-32b77e3b…`). `fresh.py --debug
--build` printed `✓ FRESH — built from exactly this source`. `check_shelf.py` green: 29 rules
files, 65 standard blueprints. `lib/play/play_screen.dart` was modified in Coder's working tree
throughout; **everything below was run against the committed `d33bc2d`**, built from a `git
archive` of that commit into my own tree.

Fixtures: `blast-kind` (TEST 099's board, reused deliberately) and a new `ally-ward`.

---

## 1. Force Scream — confirmed at all three tiers, and the tiers are now distinct

Cast from one Consular 12 (Wis/Cha 18), on TEST 099's own board, against the same three
creatures. TEST 099's pre-fix reading on this board was `12d6 40` and `12d6 41`.

| tier | cost | dice rolled | on m-org-near | on m-org-far | ability penalty |
|---|---|---|---|---|---|
| Force Scream | 8f | **3d6** | 13 | 13 | −2 to all six, 10r |
| Improved Force Scream | 15f | **5d6** | 23 | 16 | −4 to all six, 10r |
| Master Force Scream | 24f | **7d6** | 20 | 24 | −6 to all six, 10r |

3d6 / 5d6 / 7d6 exactly as documented, every roll inside its band, and the three tiers are
genuinely different from base and from each other. The pool moved 159 → 151 → 136 → 112, i.e.
8 / 15 / 24, and the ceiling degraded −1 / −3 / −8 as authored.

The arithmetic closes independently: `m-org-far.probe.03` took 13 + 16 + 24 = 53, and the panel
read `147 of 200`.

**A second discriminator I had not expected.** Each tier also carries `ability_penalties` at
2 / 4 / 6 points, so the tiers differ on a field that has nothing to do with the damage dice.
They landed at −2, −4 and −6. A fix that had only corrected the dice would not have moved these.

The droid was excluded from all three casts (`m-droid.probe.02` sat at `200 of 200` throughout,
between the two organics that were hit) — TEST 099's finding still holds at this commit.

---

## 2. The healing family — the formulae are all correct, and every one of them injures first

The three Heal formulae are exactly as you specified, and the app prints its own derivation:

| power | derivation printed | total | reach |
|---|---|---|---|
| Heal | `5 +4 cha +4 wis +12 level` | **25** | single target — only the aimed ally was named |
| Improved Heal | `15 +4 cha +4 wis +12 level` | **35** | area, radius 7 |
| Master Heal | `15 +4 cha +4 wis +24 level` | **47** | area, radius 7 |

Base Heal named one creature; both higher tiers named several. The single-target/area split is
real, and `2×` Force levels on Master is real (24, not 12).

### ⚠⚠ THE DEFECT — a `heals: ally` row travels the damage path before it travels the heal path

`play_screen.dart:8933` removes the damage row only for `heals: self`:

```dart
final dmg = p.damage?['heals'] == 'self' ? null : p.damage;
```

`heals: ally` is not removed, so the row reaches `if (dmg != null)` at `:9183` and is applied
through `applyDamage` at `:9223` to every creature in `caught` — which, for an ally power, is
the party. The heal block at `:9380` then runs afterwards and heals the same creatures.

**Measured on a standing ally, inside one turn, with nothing else acting between the two frames:**

```
Revitalize · 12f — 139 → 127 · at ward-near.ward.01 · ward-near.ward.01 — 10 10
  before  ward-frail -3/10 · ward-far 60/60 · brute 197/200 · ward-near 50 of 60 · Warden 70/74
  after   ward-frail -3/10 · ward-far 60/60 · brute 197/200 · ward-near 40 of 60 · Warden 70/74
```

ward-near lost exactly 10 — Revitalize's `flat`. Every other combatant is byte-identical.
**Revitalize took vitality off a standing ally.**

The Heal tiers hide it, because the damage and the heal are the same number and cancel:

```
Heal · 8f — at ward-near.ward.01
  ward-near.ward.01 — 5 +4 cha +4 wis +12 level 25        <- damage, 40 -> 15
  ward-near.ward.01 — healed 5 +4 cha +4 wis +12 level 25 · 15 → 40
```

The `15 → 40` is the tell: the heal's *before* is 25 below where the ally started. Net zero.
**Heal, Improved Heal and Master Heal restore nobody** — in every cast I made, each named
creature ended on exactly the vitality it started with.

Where the two do *not* cancel is Revitalize, because `only_if_fallen` correctly gates the heal
but nothing gates the damage. Improved Revitalize, radius 7, one cast:

```
Improved Revitalize · 20f — 103 → 83 · at ward-near.ward.01
  ward-near.ward.01 — 25 25 · ward-frail.ward.02 — 25 25
  ward-far.ward.04  — 25 25 · Warden — 25 25
  ward-frail.ward.02 — healed 25 25 · -29 → -4
```

| | before | after |
|---|---|---|
| ward-near (standing) | 34/60 | **9/60** |
| ward-far (standing) | 60/60 | **35/60** |
| Warden (the caster) | 65/74 | **40/74** |
| ward-frail (fallen) | −4/10 | **−4/10 — not revived** |

**One cast of Improved Revitalize took 25 vitality off every standing party member including the
caster, and revived nobody.** The fallen ally was driven to −29 and healed back to where it
started. The heal's fallen-only gate is working correctly and is the reason the damage on the
standing three is unopposed.

So, against your spec for group 2: the numbers are right, the reach is right, the fallen-only
gate is right — and the family is net-harmful. Revitalize on a standing ally does not "refuse or
do nothing"; it injures them for its flat amount.

⚠ The same unguarded line is in your working tree as well as at HEAD (`:8933` in both), so this
is not something already half-fixed in flight.

---

## 3. Force Valor and the area buffs

**Both halves land.** One cast, and the app reported each mechanism separately:

```
Force Valor · 8f — 159 → 151 · ceiling −1 to 158 · at ward-near.ward.01 · ⚠
  Force Valor does not say what it may be aimed at
  the party — +2 saves
  the party — +2 str 6r · +2 dex 6r · +2 con 6r
```

The saving-throw modifier and the attribute bonus both applied. Ally-aiming is functional —
nothing refused.

**The reach.** The UI names nobody for a buff ("the party — …"), so I measured the reach on the
*same pool*: for an ally power `buffed` is built from `caught` on one line,
`buffed = [for (final x in caught) x.combatant]` (`:9019`), and `caught` is `_reachedBy`'s
output. Improved Heal is ally-aimed at radius 7 like Force Valor and **names every creature it
reaches**, so it reads that identical pool out loud. Cast on the first action of a fight, before
anything had moved:

```
Improved Heal · 16f — at ward-near.ward.01
  reached: ward-near.ward.01 · ward-frail.ward.02 · Warden
  not reached: ward-far.ward.04 · brute.ward.03 · nipper.ward.05
```

Board at that instant: caster (0,2), ward-near (1,2), ward-frail (2,2), **brute (3,2)**,
**ward-far (10,2)**, nipper (0,1). Centre was ward-near.

- **The hostile is excluded, and not by distance.** `brute` stood 2 squares from the centre,
  well inside radius 7, in plain sight, in the fight. It was not reached.
- **The far companion is excluded, and not by role.** `ward-far` is a `role = "henchman"` party
  member that appears in the party panel and rolled initiative — and at 9 squares it was not
  reached. In sight the whole time, so this is the radius and not the line of sight.

Both controls are the ones your brief asked for, and neither can be passed by accident.

⚠ **Scope, stated plainly:** I confirmed Force Valor's two bonuses land by watching Force Valor.
I confirmed *who an ally power reaches* through Improved Heal, because it is the same `caught`
list on the same line of code and it is the only ally power that names names. I did not watch
Force Valor's `+2` appear on one companion and fail to appear on another — the UI has no
per-creature readout for a buff. `modifiersPresentForTest` / `bonusesPresentForTest` exist for
exactly that assertion and are the right instrument if you want it nailed down further.

### ⚠⚠ Battle Meditation's caster-centred friendly half is NOT in the commit you routed

I could not confirm it because it is not there to confirm. At `d33bc2d`:

```
$ git show HEAD:lib/play/play_screen.dart | grep -c 'asParty\|centreOn\|PT-2288'
0
$ grep -c 'asParty\|centreOn\|PT-2288' lib/play/play_screen.dart     # working tree
10
```

At HEAD the non-ally branch of `buffed` is party-wide with no geometry at all:

```dart
final buffed = p.affects == 'ally'
    ? [for (final x in caught) x.combatant]
    : [
        for (final c in f?.encounter.combatants ?? const <Combatant>[])
          if (c.role != Role.enemy) c
      ];
```

Battle Meditation is one of the five powers deliberately silent on `affects`, so its friendly
rows take the second arm: **every non-enemy in the fight, regardless of where anyone stands.**
Allies near the caster do get it — but so does an ally on the far side of the board, so the
behaviour cannot distinguish "centres on the caster" from "centres on nothing".

`asParty` / `centreOn` and the PT-2288 split are in your uncommitted working tree. This is a
build-state fact from `git`, not a reading of behaviour. Re-route it when it lands and I will
confirm it.

---

## What I did not test

- Base Revitalize against a fallen ally *specifically*. Base Revitalize has no radius, so it
  takes the auto-picked aim, and the aim is `target.first` — always a standing companion on my
  board. Improved Revitalize covers the same gate at radius 7 and is reported above.
- Master Revitalize. Same root cause as Improved; I stopped once the mechanism was established.
- Force Valor's Improved and Master tiers.

## Fixture notes

`ally-ward` is on the shelf (`AAA Ally Ward`, named to sort first because the library carousel
does not scroll to a fifth card). `role = "henchman"` on an area `[[contents]]` placement is the
lever that makes a companion, and it works — all three appear in the party panel and roll
initiative.

⚠ **A companion will not hold its ground once a fight starts, including after "Wait here".**
`Ward Far` was placed at (10,2) and acknowledged *"Ward Far will wait here"*; by my third turn it
had walked to (5,2), and on a later fight it reached (1,1). My first attempt at the radius
measurement was invalidated by exactly this — ward-far was reached because it had walked into
range, not because the radius leaked. **Every geometry reading above was taken on the first
action of a fight, with the board screenshotted at the instant of the cast.** I am reporting
this as a fixture hazard rather than a defect: I have not checked what "Wait here" is specified
to do in combat, and it may be out-of-combat following only.
