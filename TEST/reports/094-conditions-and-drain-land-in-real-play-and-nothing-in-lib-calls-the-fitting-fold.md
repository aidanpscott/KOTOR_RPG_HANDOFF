# TEST 094 — THE ON-HIT CHAIN IS REAL AND THE GATE IS EXACT. A Stun Baton
# printed its own d100 against its own 25% on every hit and fired only when it
# should have; a Knockdown weapon, which states no chance at all, printed no
# d100 whatever and landed every time. Ability drain ACCUMULATES and you can
# watch it: one hit took a point of Dexterity and the target's Defence fell
# from 18 to 17, a second took four more and it fell to 15. `stunned` is
# genuinely enforced — it took an Action off me.
# ⚠⚠ AND THE TWO FITTING ASKS CANNOT LAND, because **nothing in `lib/` calls
# `fittedContribution` at all.** Its only caller in either repo is its own test
# file. A creature carrying a legally fitted Refined Phobium Emitter hit me
# twice and printed no `slowed` clause of any kind — while a creature with an
# equippable Stun Baton, in the same fight, against the same target, printed
# its gate both times.
# ⚠⚠ AND A SECOND ONE UNDERNEATH IT: I could not make a worn ability-granting
# catalogue row reach ANY score, on a creature or on the player.

## Build state

    KOTOR-RPG-APP   a719dad  PT-2186 — what I built and what every reading below is from
    lodestar        52aa8b1  — HEAD's own pin
    lens            32b77e3
    Loom            ab5742b  (not launched)

⚠ **The app tree was mid-edit when I started** — `attack.dart`, `play_screen.dart`,
`records.dart` and `pubspec.lock` all dirty, and the lock diff bumped the engine
from `52aa8b1` to `560677a`. That uncommitted work is `PT-2194`, the weapon-damage
layering the routing says is *not* ready. So I did not test the working tree: I
took `git archive a719dad` into my scratchpad, resolved it offline against its
**own** pin, and built there. Three artifacts in agreement, none of them yours.

⚠ **HEAD moved under me during the run** — `c2c581f PT-2194: a weapon's own
damage reaches its strike` landed while I was measuring. Nothing below is from it.

### The stale-bundle question is closed, and I was wrong about it for six sessions

`PT-2171` is right and my diagnosis was wrong. The file I had been reading — the
bundle's executable — is a stable host launcher that never moves for Dart. I had
also been carrying *"no `env.sh` any more, no cmake on this machine"*: **both
false.** `env.sh` is there, cmake/ninja/clang are under `~/spike/prefix`, and a
full `flutter build linux --debug` takes **eighteen seconds**. Six sessions of
`flutter assemble` workarounds were unnecessary.

`scripts/fresh.py --debug --build` now answers it outright, and did:

    ✓ FRESH — built from exactly this source at 09-15 22:45:40

`check_shelf.py` green at both ends — **28** rules files now, up from 26.

### And `PT-2172` is right: my TEST 093 wedge finding was misattributed

The two-key save item was innocent; the defect was `_enemyTurns`' hard-coded
bound of 8 against nine enemies. My bisect pointed at the item because
**initiative is re-rolled every run and `_begin` joins by contact**, so the
fixture was not the same fixture between rows. A bisect over a re-randomised bed
reports the noise. The stall I reported was real; the cause I named was not.

---

# 1 · THE CHANCE GATE IS EXACT, AND IT IS VISIBLY NOT FIRING ON EVERY HIT

**Stun Baton**, `g_w_stunbaton01` — the real row: `stunned`, 2 rounds, DC 10
fortitude, **chance 25**. Every hit prints the gate whether or not it fires,
which is what makes this checkable rather than statistical:

    stunned — d100 70 vs 25% · does not fire
    stunned — d100 35 vs 25% · does not fire
    stunned — d100 52 vs 25% · does not fire
    stunned — d100 77 vs 25% · does not fire
    stunned — d100 81 vs 25% · does not fire
    stunned — d100 97 vs 25% · does not fire
    stunned — d100 37 vs 25% · does not fire
    stunned — d100  2 vs 25% · d20  4 + fortitude 2 + Constitution 2 =  8 vs 10 · takes hold
    stunned — d100 15 vs 25% · d20 16 + fortitude 2 + Constitution 2 = 20 vs 10 · shaken off
    stunned — d100 25 vs 25% · d20  6 + fortitude 2 + Constitution 2 = 10 vs 10 · shaken off

Ten firings, one rule, no exceptions: **it fires exactly when `d100 ≤ 25`.**
Seven of ten hits did not fire, so it is plainly not firing on every blow. Both
boundaries showed up without being hunted: **`d100 25` fired** (the test is
inclusive) and **a save total of exactly 10 against DC 10 succeeded**.

And when it fires the roll is the target's own, with its full derivation —
`PT-2163`'s chain from TEST 093 still standing.

# 2 · THE NULL-CHANCE CASE, WHICH IS THE ONE THAT PROVES THE FIELD IS READ

**Charric**, `w_brifle_23` — `prone`, **no `chance` key and no `rounds` key**,
which is `PT-2170`'s shape: all seventeen real Knockdown properties carry
`Param1 255`, so the shelf omits the duration.

    prone — d20 15 + Dexterity 2 = 17 vs 14 · shaken off
    prone — d20 12 + Dexterity 2 = 14 vs 14 · shaken off
    prone — d20  1 + Dexterity 2 =  3 vs 14 · takes hold · ⚠ nothing enforces it yet

**No `d100` anywhere on any of them.** A null chance fires always and spends no
die, exactly as `chanceFires` states — and set against the baton's ten lines
that all carry one, that is the chance field being *read* rather than defaulted.

Two more things fall out of the same lines:

- **It is a REFLEX save** — `Dexterity 2`, not fortitude. TEST 093 read fortitude
  only, so this is the second save kind confirmed end to end.
- **`prone` applies, displays, and says it is inert** — `⚠ nothing enforces it
  yet`, because `honouredConditions` is `{'stunned'}`, one of the nineteen
  `§7` names. That is exactly the "confirm it applies and displays even if it
  doesn't restrict" half of the ask, and the app volunteers it.

# 3 · `stunned` IS ENFORCED — it took an Action off me

A Stun Baton in a creature's hands landed one on the player:

    d-baton.probe.06: Stun Baton · … 9 left · stunned — d100 2 vs 25% ·
    d20 4 + fortitude 2 + Constitution 2 = 8 vs 10 · takes hold

and my very next turn:

    you have already acted

That is `beginRound` resetting budgets through `legalityOf`, and it is the one
condition of nineteen that does anything. **It works.**

⚠ **But the refusal names the wrong reason.** I had not already acted — I was
stunned, and the condition had taken the Action before I reached for it. In a
corpus that keeps ruling that a refusal has to say *why*, this one reports the
generic no-Action-left message and leaves the player to guess.

⚠ **And I could not settle the round count.** The item states **2 rounds** and I
was refused **exactly one** turn, acting normally on the next. One observation
cannot tell me whether that is `roundsLeft`'s stated *"including this one"*
accounting consuming the round it landed in, or a round going missing. Worth one
guard rather than another play session.

# 4 · ABILITY DRAIN ACCUMULATES, AND YOU CAN WATCH IT IN THE DEFENCE

**Sonic Pistol**, `g_w_sonicpstl01` — `ability_damage`, dexterity, 1d4, DC 14
fortitude, no chance, so every hit rolls the save. Against one target, Dex 20:

| # | the save | drained | that target's `needed` |
|---|---|---|---|
| 1 | `d20 17 + fortitude 2 + Constitution 2 = 21 vs 14 · resisted` | — | 18 |
| 2 | `d20  1 + fortitude 2 + Constitution 2 =  5 vs 14` | **1d4 1 off Dexterity** | 18 → **17** |
| 3 | `d20  2 + fortitude 2 + Constitution 2 =  6 vs 14` | **1d4 4 off Dexterity** | 17 → **15** |

Dex 20 → 19 → 15 gives modifiers +5 → +4 → +2, so Defence 18 → 17 → 15. **Every
step matches `floor((score − 10) / 2)` exactly**, and the drain is visible as a
felt thing: the target gets easier to hit as you keep shooting it.

**Two hits are genuinely worse than one, and the reason is the summing.** Totals
of 1 then 4 give 5; a `§4` fold would have taken the best of them — 4 — and left
Defence at 16, not 15. The deliberate decision to make this a separate summed
type is the difference between the reading I got and the one I would have got,
and it is one point apart, which is as clean as this gets.

The save gates it: the resisted line drained nothing.

⚠ **Small false positive.** The status bar reports `Sonic Pistol: Dex damage is
not modelled`. That is the base type's `threat` column (`20 · Dex damage`)
leaving an unparsed remainder — but Dex damage IS modelled now, by the catalogue
effect, three lines further along the same blow. Same shape as TEST 090's
`only is not modelled`: a warning that teaches players to ignore warnings.

---

# ⚠⚠ THE FINDING — NOTHING IN `lib/` CALLS THE FITTING FOLD

Both fitting asks rest on `fittedContribution`. **It has no caller in `lib/`.**

    lib/play/attack.dart:1852   }) fittedContribution({        ← the definition
    lib/play/attack.dart:775    // … `fittedContribution` folds …  ← a comment

and its slot table is the same:

    lib/chargen/chargen_source.dart:145   static Future<…> upgradeSlots(…)
    test/upgrade_fitting_test.dart:21     slots = await ChargenSource.upgradeSlots(where);   ← the only call

Every call to either, in either repo, is in `test/upgrade_fitting_test.dart`.
Creature weapons are built by `equippedFrom` at `attack.dart:602`, which reads
`weapon_r_1` and the weapon's own catalogue row and **never consults
`equipment.fitted`**. So a fitted component contributes nothing — not an
on-hit, not an ability, not a stat — to anybody, in any fight. True at
`a719dad` and still true in your working tree.

### Confirmed in play, with the control in the same fight

One creature carrying `items/weapons/sabre-plain` with the **Refined Phobium
Emitter** (`u_l_emit_13` — `slowed`, 3 rounds, DC 18, chance 50, exactly the
shape the routing names) fitted into its emitter slot, legal by
`upgrade_slots.toml` and `lightsaber_slots.toml`:

    d-fitted.probe.05: Tester Plain Sabre · rolled 19 — … hit · damage 5 — 1d2 1 + Strength 4 · 7 left
    d-fitted.probe.05: Tester Plain Sabre · rolled 24 — … hit · damage 6 — 1d2 2 + Strength 4 · 1 left

**No `slowed` clause at all.** Not `takes hold`, not `shaken off`, not even
`does not fire` — and §1 above shows that a gate prints on *every* hit when the
effect is there at all. And in the same fight, against the same target, the
other creature's equippable weapon:

    d-baton.probe.06: Stun Baton · … -4 left · stunned — d100 52 vs 25% · does not fire

Same wielder stats, same target, same round. **The equippable route speaks and
the fitted route is silent**, which puts the difference on the route and
nothing else.

⚠ **And the guards over it are green** — `flutter test test/upgrade_fitting_test.dart`,
**13 of 13**, including *"A FITTED EMITTER CONTRIBUTES ITS ON-HIT — and this is
how `slowed` becomes reachable"*. The fold is correct; it is simply not wired
to anything that plays.

---

# ⚠⚠ AND UNDERNEATH IT — A WORN ABILITY ROW REACHED NO SCORE I COULD READ

This started as the control for the fitted crystal and became its own finding.

### On a creature it cannot arrive, and the code says why

`abilitySources` is assigned in **exactly one place in the app**:

    lib/play/play_screen.dart:4705   me.abilitySources = _armour?.abilitySources ?? const [];

`me` is the player. Creature combatants come from `combatantFrom(...)` at
`attack.dart:501`, which is handed tag, speed, role, baseAttackBonus, saves and
adjust — **and no abilities**. The worn bundle IS computed for them one line
above (`final worn = await _worn(...)`) and IS carried onto the placement
(`armour: worn`), and then nothing ever moves `armour.abilitySources` onto the
combatant. Measured live, three creatures identical but for how the same row
reaches them:

| creature | Crystal, Kaiburr (`u_l_crys_25`, **Con +3**) | its Fortitude line |
|---|---|---|
| `c-plain` | nothing | `Constitution 2` |
| `c-worn` | **worn**, forearms | `Constitution 2` |
| `c-fitted` | **fitted**, sabre crystal slot | `Constitution 2` |

All three Con 15. Both routes silent.

### And on the player I could not make it arrive either

This is the half I expected to pass, and it did not. The player's clothing
blueprint carries `qcrystal_5_0` — **Str +4, Dex +3, Cha +3** — and the save
confirms the equipment actually points at it:

    "weapon_r_1":"items/weapons/blaster-rifle","body":"items/armour/clothing"

`body` is a slot `wornBy` reads, the blueprint resolves, `_abilitiesFrom` would
return `{strength: 4, dexterity: 3, …}` off that row. Three separate instruments,
all of which derive from the combatant, all unmoved:

    defence base 10 + Dexterity 2 + class 3 = 15        ← Dex 14, not 17
    prone — d20 12 + Dexterity 2 = 14 vs 14             ← the save's own term
    Stun Baton · rolled 22 — d20 17 + attack 1 + Strength 2 …   ← Str 14, not 18

And a separate run with `u_l_crys_25` (Con +3) in the same slot left max vitality
at **12**, where `PT-2177`'s own note says a worn Constitution moves it by
`Δmodifier × level` — one point at level 1.

⚠ **I am not calling the player half diagnosed.** `_armour` is filled by an async
read and the source says so in as many words — *"`_armour` IS FILLED BY AN ASYNC
READ and is null until it lands"* — and `me.abilitySources` is assigned once, from
it. A race between that read and the combatant being built would produce exactly
what I saw, and I cannot separate that from a missing wire by playing. The
creature half needs no such caveat: there is no assignment to race.

⚠ `test/worn_abilities_test.dart` is **20 of 20 green**. It covers the fold —
`§4`, both signs, two sources — and not the arrival, which is the part that
failed for me.

---

## Not a finding, checked and dropped

`Continue` and `Load Game` are greyed for several seconds after opening a package
even when saves exist. I nearly filed it; it is an async list load and the buttons
enable on their own. Waiting eight seconds is the whole story.

## What I did not do

- **Did not watch a stun expire.** See §3 — one refused turn against a stated two.
- **Did not test the other sonic weapons**, the Bothan Shrieker included. One
  family member, `g_w_sonicpstl01`, exercised end to end.
- **Did not exercise a fitted component's `stats`** (`PT-2186`'s attack/damage
  half) separately — it folds through the same uncalled function, so the same
  finding covers it, but I read it rather than measured it.
- **Did not launch Loom.** Every item is hand-transcribed from its catalogue row.

## State

- **New package `condition-probe` is mine and left on disk**, in the state that
  produced the readings above.
- ⚠ Its `items/weapons/{short-sword,long-sword,blaster-rifle}.toml` are whatever
  variant was last swapped in — those three paths are the chargen lever and are
  deliberately not what their names say. `scratchpad/swap.sh` is what moved them.
- ⚠ `items/armour/clothing.toml` is the same lever for the player's body slot.
- ⚠ The duellists' `damage` is authored down to `1d2` and their Strength to 10.
  They swing at the PLAYER, who has 12 vitality; what is under test is the
  condition, not the arithmetic. Declared rather than hidden.
- ⚠ `items/weapons/emitter-as-weapon` variant puts a COMPONENT's catalogue id on
  a holdable weapon. Not a legal item, and only ever the control.
- Four saves (`marek-sarn`, `cassar-dray`, `vash-tarkis`, `vash-brannis`); two
  record a death.
- My build lives in the scratchpad copy only. **Your `build/` was never written
  to and neither shared bundle was touched.**
- App pids `71171`, `74683`, `76689`, `79084` all killed by pid and confirmed
  gone; no Loom launched; nothing of yours touched.
