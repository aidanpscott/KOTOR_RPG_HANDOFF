# TEST 095 — _cast IS LIVE AND THE PARTS I COULD REACH ARE RIGHT. A real power
# applies a real condition: Force Stun printed `stunned` on a failed save and
# `slowed` on a made one, which is the shelf's own `condition` /
# `condition_on_save` pair. §7.4's two-handed grip lands exactly — the same
# vibrosword reads `Strength 6` in damage with an empty off-hand and
# `Strength 4` with the off-hand filled, while the attack roll keeps `Strength 4`
# in both. The DC's ability half is exact: DC 6 at WIS/CHA 10 and DC 14 at
# WIS/CHA 18.
# ⚠⚠ AND THE THREE ASKS YOU CALLED HIGHEST PRIORITY CANNOT BE OBSERVED AT ALL,
# for one reason underneath all of them: **this product cannot represent a
# character above level 1.** `record_validate` requires class levels to sum to
# `progress.level`; `progress` defaults to level 1 and **nothing ever writes
# it** — `character.levelled` is declared in the shelf and implemented nowhere.
# A Soldier 24 / Jedi 6 is refused on load, by name.
# ⚠⚠ AND A SECOND ONE IN THE DATA: **18 of the 22 damage powers that state a
# save branch carry no `save_kind`**, so they roll no save and the branch can
# never fire. Force Kill — the one you named — is one of the 18.

## Build state

    KOTOR-RPG-APP   18f41d8  PT-2222 — built and measured from this
    lodestar        5470bb3  — HEAD's own pin, and the pub-cache checkout
    lens            32b77e3

    ✓ FRESH — built from exactly this source at 09-16 13:22:55

⚠ **Lodestar's working tree was mid-edit** (`item_open.dart`, plus an untracked
`a_custom_weapon_test.dart` — the custom-weapon shape you say is in progress).
It does not reach me: the app compiles the **pub-cache checkout** of the
committed pin, so the three artifacts agree and none of them is your bench.
The app tree was clean at start; by the end you had moved on (`attack.dart`
dirty, Lodestar at `acd19ae`). Nothing below is from that.

`check_shelf.py` green at both ends — 28 rules files, 65 standard blueprints.

**And both TEST 094 findings are closed** — `066b9ad PT-2201: fittedContribution
reaches a real fight` and `84ae894 PT-2201: worn ability bonuses reach a
creature and the player`. Noted in passing, not re-tested.

---

# ⚠⚠ THE BLOCKER — NOTHING IN THIS PRODUCT CAN BE ABOVE LEVEL 1

You asked for a Soldier 24 / Jedi 6 and said the single-class level-1 default is
the blind spot. It is worse than a default. **It is the only shape that exists.**

I authored the character in the product's own format — there is no other route:
chargen builds one class at level 1, and the premade roster is a declared gap
(`entry_screen.dart`: *"blueprint format for a playable premade and nothing
writes one"*; `main.dart` passes `premadeCount: 0`). The save loader refused it
and said exactly why:

    THIS SAVE WILL NOT OPEN
    • Class levels add to 30 and the character is level 1.

That is `record_validate.dart:175`, rule 5 — *classes non-empty, ≤ 3 entries,
levels sum to `progress.level`*. And the other half of that comparison can never
move:

- `progress` is a `CharacterRecord` field declared at `ledger.dart:353` and
  defaulted at `369` to `{'level': 1, 'xp': 0}`.
- `replay()` has **no case that writes it** — `progress` appears exactly three
  times in the whole file: the field, the default, and `toMap`.
- `progress:` is **never passed at any construction site** in either repo.
- `character.levelled` is declared in `event_kinds.toml` and has **no
  `CharacterEventKind` constant, no writer and no replay case** in either repo.

So every record is level 1, and rule 5 then refuses every class-level total but
1. The validator is doing its job — the inconsistency it names is real. What is
missing is the event that would make a level-2 character representable.

### Which is why asks 1, 2 and 3 cannot be answered in play

| ask | what it needs | what stops it |
|---|---|---|
| 1 · DC off Force levels | a gap between character level and Force level | both are pinned to 1, so `5 + Force levels` and `5 + character level` **give the same number** |
| 2 · the pool's die half | Force level > 1 | the die half is `sides + (forceLevels − 1) × perLevel`; with `forceLevels ≡ 1` that term is **always 0** |
| 3 · the second damage band | Force level > 20 | Force level cannot exceed 1 |

`PT-2216`'s own note says *"A Soldier 24 / Jedi 6 cast at DC 29 before this and
casts at DC 11 now"* — that character cannot be loaded, so the fix is correct in
the source and **unfalsifiable in play**. Same for `PT-2215`'s die half and
`PT-2218`'s band.

⚠ The three refused/blocked saves are still on disk (`gap-soldier.sav`,
`deep-consular.sav`) so the refusal reproduces in one click.

---

# WHAT I COULD MEASURE, AND IT IS EXACT

## 1 · the DC's ability half — both terms, live

Two characters identical but for WIS and CHA, each casting Force Stun:

| character | WIS / CHA | printed DC | `5 + FL 1 + WIS + CHA` |
|---|---|---|---|
| New Consular | 10 / 10 (+0/+0) | **`vs 6`** | 5 + 1 + 0 + 0 = 6 ✓ |
| High Mind | 18 / 18 (+4/+4) | **`vs 14`** | 5 + 1 + 4 + 4 = 14 ✓ |

An eight-point jump for two +4s. The ability half of `FORCE-POWERS-01`'s formula
is right; the Force-level half is the part nothing can move.

⚠ `record_validate` caps every ability at 8–18 and said so by name when I tried
20 — *"WIS is 20, outside 8 to 18"* — so +4 is the ceiling on each.

## 2 · the pool — the ability half scales, the die half cannot

    New Consular   WIS/CHA 10    force  8 of 8     = 8 + (1−1)×5 + (0+0)×1
    High Mind      WIS/CHA 18    force 16 of 16    = 8 + (1−1)×5 + (4+4)×1

Zeroing both modifiers on the first was deliberate: it makes the pool **equal to
its die half**, which is the half you asked about. It reads **8** — the
Consular's d8 and nothing else — and it is 8 for every character this product
can build, because `(forceLevels − 1)` is always zero.

So: the ability half is confirmed to scale. **The die half is confirmed not to,
and cannot be made to.**

Two smaller things fell out: the pool **persists across save and load** rather
than refreshing (`force 4 of 14 (max 16)` came back unchanged), and `e` refuses
mid-fight with *"not in the middle of a fight"*.

## 3 · two-band damage — unreachable, and the shelf agrees on the count

Nine powers carry `band_to: 20` with a `band_divisor` — `death_field`,
`destroy_droid`, `drain_life`, `force_choke`, `force_lightning`, `force_shock`,
`force_storm`, `force_whirlwind`, `force_strangle`. That is exactly the nine you
named, so the data half is right. The band only differs above Force level 20 and
no character can be there.

⚠ **And there is a consequence at the level that DOES exist: eight powers roll
zero dice.** `1 ~/ 2 == 0`, so every `divisor: 2` power deals **`0d6`** at Force
level 1 — `force_push`, `force_kill`, `force_wave`, `force_crush`,
`advanced_throw_lightsaber`, `deadly_sight`, `overload`, `throw_lightsaber`.
Measured, not inferred: Force Push printed `0d6 0`.

## 4 · a real power applies a real condition — confirmed both ways

Force Stun at `t-weak`, DC 14, its Fortitude modifier −2:

    d20  9 = 7  vs 14 · stunned        ← failed
    d20 10 = 8  vs 14 · stunned        ← failed
    d20 16 = 14 vs 14 · slowed         ← made (14 ≥ 14, inclusive)
    d20 18 = 16 vs 14 · slowed         ← made

The shelf states `condition = "stunned"`, `condition_on_save = "slowed"`,
`save_kind = "fortitude"`, `condition_rounds = 3` — and that is precisely what
happened, on both branches. This is a `Condition` pushed onto the target with a
`character.condition-applied` event beside it, not prose: the prose is what the
line prints **only** where a power models nothing.

The pool and its degradation are in the same line and correct:
`6f — 16 → 10 · ceiling −1 to 15`.

## 5 · the save branches

**Force Push — the rule is wired, selected, and labelled:**

    t-weak.probe.01 — d20 18 = 14 vs 14 · resists ·
    t-weak.probe.01 — 0d6 0 · saved · 0.5× level 1

The target made the save, took **no stun** (`resists`), and the damage took the
`on_save_times_level` road — named in the derivation. `0.5 × level 1` is 0, and
`0d6` is the divisor-2 problem above. **The branch is confirmed to fire; the
number it produces cannot be made non-zero while Force level is 1.**

**⚠⚠ Force Kill cannot roll a save at all — and it is not alone.**

`force_kill`'s extracted row carries `damage.on_save = "dice_only"` and **no
`save_kind` and no `condition`**, while its own effect prose says *"If the target
makes a Fortitude save versus DC 5 + …"* and *"causes the target to choke for 2
rounds"*. `PowerRecord` reads `saveKind: m['save_kind']`, so it is null;
`_applyPower` then leaves `check` null, `made` false, and **every `on_save`
branch is skipped**. The behaviour you asked for — dice stand, no choke — comes
out right by accident: there is no choke in the data to apply and no save to
make.

Counted across the shelf:

    damage powers that STATE a save branch            22
      … carrying a save_kind, so it can fire           4   force_choke, force_push,
                                                            force_wave, force_strangle
      ⚠ carrying NO save_kind, so it cannot           18   incl. force_kill, force_lightning,
                                                            death_field, drain_life,
                                                            destroy_droid, force_crush …

**Eighteen of twenty-two save branches are unreachable.** That is a data gap, not
a code one — `_applyPower` handles all four branch kinds correctly — and it is
invisible from the code side because the reader is right.

⚠ Force Kill also costs 22 against a maximum representable pool of 16, so it
could not have been cast in any case.

## 6 · Dark Healing — refused, and there is no heal to reach

    Dark Healing is aimed at self, not a sentient — nothing spent

The targeting gate refuses it and the pool is untouched, so the *"doesn't attempt
to damage a target"* half holds — and `_applyPower` would have skipped damage
anyway, since `heals: 'self'` nulls the damage row. But **the caster is not
healed, because nothing heals**: `heals` appears **exactly once in the whole
app**, on `play_screen.dart:8179`, the line that excludes a self-heal from the
damage path. There is no other reader of it. `death_field` and `drain_life`
carry `heals: "caster"`, which that line does not match at all and nothing else
looks at.

⚠ It also costs 24 against a maximum pool of 16, so it is uncastable twice over.

## 7 · §7.4's two-handed grip — all three cases, one variable each

Same Strength 18 (+4), same target, three loadouts:

| weapon | off-hand | attack term | **damage term** |
|---|---|---|---|
| Vibrosword (`attacks = 1`) | **empty** | `Strength 4` | **`Strength 6`** |
| Vibrosword (`attacks = 1`) | filled | `Strength 4` | `Strength 4` |
| Double-Bladed Sword (`attacks = 2`) | empty | `Strength 4` | `Strength 4` |

    Vibrosword · rolled 22 — d20 18 + attack 0 + Strength 4 · needed 9 — hit ·
    damage 15 — 1d12 9 + Strength 6 · 3985 left

`(4 × 3) ~/ 2 = 6`, and **both terms are in the same line**, so the rule shows
itself: the attack roll takes 1× and the damage takes 1.5×. Filling the off-hand
with a short sword — changing nothing else — drops it back to 4. A §7.6 double
weapon with an empty off-hand does **not** take it, which is the half that would
have gone wrong had any of the three existing columns been threaded instead.

---

## How the player was built, and why

⚠⚠ **The player in every reading above is an authored save**, written by
`scratchpad/mksave.py` in the product's own format — `writeSave`'s field order
from `save_file.dart`, and an event log whose every `kind` is in
`event_kinds.toml` with a `replay` case. There is no checksum, so nothing is
forged past what the header states, and the product's own reader accepted them:
six loaded and played, and three were **refused with precise reasons** (the
level-sum rule twice, the ability range once). The validator is the reason I
trust the fixtures — it rejected exactly the illegal ones.

I used it because there is no alternative: chargen gives one class at level 1 and
premades are unimplemented. It is the same lever the level-1 characters use, so
the six that loaded are ordinary records.

## What I did not do

- **No Force Wave, Stun Droid, Force Choke or Destroy Droid cast.** They cost
  14–22 against a maximum pool of 16 and most are unaffordable; Force Stun and
  Force Push are the two condition powers a representable character can pay for.
- **No droid target**, so `stun_droid` and `destroy_droid` are untested against
  their own subject.
- **Did not confirm `stunned` costs the target its Action here** — TEST 094
  established that separately and a closed test is not re-run.
- **Loom not launched.**

## State

- **New package `force-probe` is mine and left on disk.** ⚠ Its display name is
  `AAA Force Probe` only so it sorts to the front of a 24-package library —
  the id is `force-probe`, which is what the saves reference.
- **Eight authored saves** in `~/.local/share/kotor-rpg/saves/`: `gap-soldier`
  and `deep-consular` are the two the loader **refuses** (left deliberately, so
  the blocker reproduces in one click), plus `new-consular`, `high-mind`,
  `offhand-full`, `double-blade`, `stunner-a`, `stunner-b`.
- ⚠ Targets carry 4000 vitality so a 22d6 power could not kill the instrument
  mid-measurement; `t-tough` is Dex/Con/Wis 30 so that "a target who saves" is a
  fixture property rather than a wait.
- ⚠ **The dice are deterministic across a reload** — two different characters
  taking the same actions produced the identical sequence (d20 16, then 18). I
  got a failed save by changing how many dice were drawn first, not by retrying.
  Worth knowing before anyone re-rolls for a different outcome.
- My build lives in the scratchpad copy only. **Your `build/` was never written
  to and neither shared bundle was touched.**
- App pids `227827`, `228278` killed by pid and confirmed gone; no Loom;
  nothing of yours touched.
