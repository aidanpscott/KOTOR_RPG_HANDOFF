# TEST 068 — the melee/ranged upgrade screen (BUILD 151, PT-1780) driven
# end-to-end: single auto-applies, multiple gates OK, Agent/Treasure
# Hunter's four weapons are one grant not a choice, droids and
# Conscript/Acolyte correctly show nothing rather than a false success

**Built against:** `run-app.sh` (always rebuilds). Reconstructed from
timestamps since HEAD moved twice more while this ran: my build's process
started 07:33, and `f26d62f` (*PT-1780 — the profession's weapon upgrade is
applied, and the save says which*, 07:27) is the last KOTOR-RPG-APP commit
before that; `pubspec.lock`'s `lodestar` pin at that point was `30954f0`
(*PT-1772*, per commit `7497018`'s own message, 06:42) — confirmed present
as an actual checkout at
`~/.pub-cache/git/Lodestar-30954f0cb90aa2fbc3f772d33fda81d5fb64c505`. Ran
`check_shelf.py` first, per the new standing practice: `✓ 25 rules files,
all identical to what the extracts generate`.

App PID `86742`, killed by PID at the end of the session, confirmed gone.
Coder's Loom (`12445`/`12443`) checked running, untouched, before and
after.

Five throwaway characters built and abandoned in `companion-fixture`
(mine) — `Veya Onder`, `Mira Dray`, `Mira Vestic`, `Veya Malick`, and one
droid — none saved past a corridor bump-fight, `Play` reached each time
only to confirm the resulting weapon in combat.

---

## 1. Single alternative (Bounty Hunter, Veteran) — auto-applies, CONFIRMED

Bounty Hunter + Veteran, no Two-Weapon Fighting. The upgrade offer
(`bounty-hunter-veteran-0`, one row: `["Heavy Blaster"]`) showed as **"and
it is this"** — not "and now you choose which" — pre-marked selected
without a click, matching `_upgrade = widget.upgrades.single` in
`initState`. `OK` was enabled the moment "takes item" was picked, no
second tap needed.

## 2. Multiple alternatives (Soldier, Hunter + Two-Weapon Fighting) —
## OK gates, array replaces, hand assignment correct — CONFIRMED

Soldier + Hunter + Two-Weapon Fighting → `soldier-both-0`
(`Long Sword`+`Short Sword`) and `soldier-both-1` (`Double-Bladed Sword`),
heading **"and now you choose which"**, both offers unmarked. Clicking
`OK` before picking either did nothing (still on Equipment, confirming the
block coded in `equipment_screen.dart`: `!(_takesItem == true &&
upgrades.isNotEmpty && _upgrade == null)`). Picked `Long Sword + Short
Sword`; `OK` enabled immediately after.

In play: the array's own weapon (`Blaster Rifle`) never fired — the first
attack read **`Long Sword · rolled 16 ... hit · damage 9 — 1d12 10 −
Strength 1 · 7 left`** — confirming (a) the array was replaced rather than
added to, and (b) the first-named (unbalanced) weapon landed in the
attack-usable main hand, per `ledger_writer.dart`'s `weapon_r_1 =
paths.first`.

*(Needed two of the four missing item blueprints for `companion-fixture`
— see State, below.)*

## 3. Agent/Treasure Hunter's four weapons — ONE grant, not a choice
## between two — CONFIRMED, the exact case named in the task

Agent + Hunter + Two-Weapon Fighting → `agent-both-0`, the single "both"
row for this class: `weapons = ["Blaster Pistol", "Blaster Pistol", "Long
Sword", "Short Sword"]`. The screen showed **"and it is this"** (not "and
now you choose which") with the label **"Blaster Pistol + Blaster Pistol +
Long Sword + Short Sword"** — read as one 4-object grant, pre-selected,
`OK` enabled without a tap. Confirms the AND reading: `weapon_upgrades.toml`
packs all four into one row's `weapons` list rather than splitting them
into two `alternative` rows the way Soldier's two swords-vs-double-blade
choice does — had the AND/OR reading gone the other way, this would have
rendered as two separate offers ("Blaster Pistol ×2" vs "Long Sword + Short
Sword") needing a pick, and it did not.

In play: **`Blaster Pistol · rolled 16 ... hit · damage 6 — 1d8 6 · 10
left`** — the main-hand pistol fired for real damage, confirming
`weapon_r_1`/`weapon_l_1` took the two pistols (first two in the list) and
the sword pair rode along as inventory (per `ledger_writer.dart`'s
`_upgraded`: only `paths.first`/`paths[1]` get a hand, the rest stay in
`items`).

## 4a. Droid — no upgrade offer at all — CONFIRMED

Droid (`Astromech · T3-series`) + `Scout` — a class that DOES carry
`scout-hunter-0`/`scout-both-0` rows for an organic Hunter. A droid has no
`profession` step at all (`Backstory` is `Programming` instead — a
structurally different concept, its own `grant`/`cost`/`upgrade` fields,
none of them "melee weapon"/"ranged weapon"). Equipment showed the droid's
plain array (`weapon`/`kit`/`repair`) and **"This profession grants no
starting item and no aptitude."** — no "the profession grants one of
these" section at all, confirming `upgradesFor`'s `profession` parameter is
simply never populated for a droid, so Scout's own weapon-upgrade rows are
unreachable regardless of class. Not a special droid check in the
equipment screen — a consequence of droids never producing a `profession`
value to ask `upgradesFor` about.

## 4b. Conscript/Acolyte — correctly show nothing applies, not a false
## success — CONFIRMED

Soldier + Conscript (armour grant, `kind = "upgrade"`, no
`weapon_upgrades.toml` row for it — `WEAPON-MATRIX-01` doesn't answer
armour). Backstory read **"armour — proposed, not yet settled"**.
Equipment's offer read **"the best armour the character's Armour
Proficiency allows"** with note **"an upgrade on the gear you already have
— and this one is not applied yet: taking it changes nothing you carry,
and the save records that"** — the exact fallback sentence for
`widget.upgrades.isEmpty`, distinct from Hunter/Veteran's now-resolved
wording. Selecting it enabled `OK` immediately (no sub-choice section
renders when there's nothing to choose between) — correctly not claiming a
resolution PT-1780 doesn't cover. Didn't separately drive Acolyte (robe) —
same code path, same `profession_grants.toml` shape (`kind = "upgrade"`,
no weapon row), so treating it as covered by the same finding rather than
re-running an equivalent case.

---

## What I did not check

- `Scout`'s own single-alternative case (`scout-both-0`, one row,
  `Double-Bladed Sword`) and `Duelist`'s (`Vibrosword`+`Vibroblade` vs
  `Vibro Double-Blade`) — same two shapes as Soldier's, not separately
  driven.
- Whether the sword pair riding as unequipped inventory in the
  Agent/Treasure Hunter case is switchable to in play (a weapon-swap UI,
  if one exists) — confirmed only that both pistols and both swords are
  present in `items`, not that the swords are reachable mid-fight.
- Whether `Treasure Hunter`'s identical four-weapon row
  (`treasure-hunter-both-0`, `Heavy Blaster` ×2 + swords) renders and
  resolves the same way — read the data and the code path is identical to
  Agent's; not independently played.
- A critical hit on any of the upgraded weapons.
- Taking the aptitude instead of the item, for any of these professions —
  only the item half was exercised throughout.

## State

- `companion-fixture` (mine) — added five item blueprints it did not
  ship before, needed to get past "which will not open" and observe real
  damage rolls rather than only the chargen-time offer text:
  `long-sword.toml`, `short-sword.toml`, `double-bladed-sword.toml`,
  `heavy-blaster.toml`, `blaster-pistol.toml`, all mirroring the
  `[item] name/base` shape `endar-spire` already ships for the weapons it
  has. Kept in place — mine, iterated on across sessions like the rest of
  this fixture.
- No other package touched — confirmed by mtime.
- Four throwaway saves created this session (`veya-onder`, `mira-dray`,
  `mira-vestic`, `veya-malick`), none reached past a corridor bump-fight —
  ordinary Tester artifacts, not cleaned up. The droid and Conscript runs
  (§4) were checked only through the Equipment screen's own text and
  never reached `Play`, so neither created a save.
- App PID `86742` killed by PID, confirmed gone. Coder's Loom (`12445`/
  `12443`) checked running, untouched, before and after.
