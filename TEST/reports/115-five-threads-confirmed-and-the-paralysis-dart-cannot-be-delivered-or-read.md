# TEST 115 — five threads confirmed, and the Paralysis Dart can neither be delivered nor read

**Build.** App **`c4916fb`** (PT-2401), tree clean, built from `git archive`.
Committed and working `pubspec.lock` agree on Lodestar **`c9a59eeb`**, which
is the checkout `package_config.json` compiles against. `check_shelf.py`
clean.

**Verdict.** Items 1, 3, 4, 5 and 6 confirmed. Item 2 is **unreachable on two
independent counts**, and its routing carries one substantive error: the
Paralysis Dart's condition *does* expire.

---

## 1. Casting costs the Action — confirmed, both halves

```
Force Scream · 8f — 263 → 255 · at mark.ba.01 · mark.ba.01 — 3d6 9 · −2 to all six abilities
```

Immediately after the cast the verb line collapses from
`f powers · c scan · d disengage · s hide · h hurry · t treat · r repair ·
o throw · g gear` to just **`g gear · space to end your turn`**, and the
`action` pip goes dark. Move is untouched at 5, which is right — casting
takes the Action, not the movement.

A second cast in the same turn:

```
Force Scream — you have already acted · nothing spent
```

and the pool is still `255 of 262` — **nothing spent** is verified, not
taken on trust.

**And a caster who cannot act is refused for free.** Paralysed (applied as
in §2 below), with the pool at full:

```
Force Scream — you are paralysed · nothing spent          force 263 of 263
```

The refusal names the reason and the pool does not move.

⚠ Minor: the cast **menu** still opens after the Action is spent — it lists
all eight powers and only refuses when one is chosen. Harmless, and the
refusal is free, but the menu is offering something it will not do.

## 2. Paralyze — the dart cannot be delivered, its row cannot be read, and the condition does expire

### (a) Nothing in the product can fire a dart

`w_rocket_09` is base **`rocket`**, whose own note says it *"REQUIRES A WRIST
LAUNCHER"*. Play consumes base `charge`, medpacs and shields — and the
strings `rocket` and `launcher` **appear nowhere in `lib/`**. All eleven
rockets and darts, the Tranquilizer Dart included, have no delivery path.

### (b) Even wielded, the row is refused — and this is the real defect

I paired the dart's real catalogue row with a wieldable base so its shipped
effect could reach the on-hit path at all. With the player holding it, the
product says exactly what is wrong:

```
`Paralysis Dart` saves for a different effect and names none.
```

The row **does** name it — `save.instead = {condition: slowed, rounds: 1}`.
The reader drops it: `_onHitFrom` builds the save with **`instead: null`
hardcoded** (`attack.dart:2333`), so `effectFromShelf` hits
`if (os == OnSave.instead && save.instead == null)` and **refuses the whole
effect**.

**The `instead` arm is dead code.** Its consumer is built and correct —
`attack.dart:2132`, `if (save.onSave == OnSave.instead && save.instead
?.condition != null)` — but *both* producers pass null: the on-hit reader
above, and the hazard path, where `_springsAs` also writes `instead: null`.
Nothing in the product can put a non-null `instead` into a `Save`. Scope
today is exactly **one shipped row**, the Paralysis Dart — which is also the
only thing that would exercise it.

⚠ **And it is silent from the receiving end.** That refusal is printed on the
*wielder's* line. When the **enemy** held the dart I watched five separate
hits land — 142 → 130 → 110 → 103 → 97 → 90 vitality — with no condition
clause and no note at all. An enemy weapon whose effect is refused looks
exactly like an ordinary weapon.

### (c) The condition itself is enforced — and it expires

Applied directly by a charge (the only other producer):

```
goes off — d20 20 + fortitude 12 + Constitution 3 = 35 vs 99 · paralysed for 2 rounds
```

Next turn: **`0 move`**, action pip dark, verbs collapsed to `g gear`. Cannot
act, cannot move — as ruled, and with no *"nothing enforces it yet"* marker.

**But it expires.** Two rounds later the budget is fully back — `5 move`,
action available, the whole verb list — and stays that way for four further
turns.

⚠ **The routing says paralysis "should NEVER expire on its own like a normal
condition would". It is not that condition.** `w_rocket_09` states
`rounds: 2`, and paralysed is **not** in `endableConditions` — so unlike
prone there is no standing out of it either. `prone` is the durationless one
(all seventeen Knockdown rows carry no duration, which is why it needed `u`);
paralysed carries a number and runs it down. The two behaviours are
consistent with each other: a condition with no clock needs a way out, a
timed one does not.

The made-save branch (slowed for 1 round) is unreachable for the reason in
(b).

## 3. Overload — two outcomes, and only the aimed creature loses its weapon

Two armed gunners standing together, both inside the radius of 2. The picker
opens (Overload is `anchor = 'target'`), so I could aim deliberately — and I
ran it **both ways**, which is what separates the blast from the weapon:

```
aimed at ov.01:  ov.01 — Blaster Rifle is destroyed · ov.01 — 10d6 44 · ov.02 — 10d6 28
aimed at ov.02:  ov.01 — 10d6 48 · ov.02 — Blaster Rifle is destroyed · ov.02 — 10d6 28
```

The blast reaches **both** either way; the weapon outcome follows **only the
creature aimed at**, and it swaps when the aim swaps. And the bystander goes
on shooting:

```
aimed at ov.01 → next turn:  gunner.ov.01: unarmed · rolled 12 …
aimed at ov.02 → next turn:  gunner.ov.01: Blaster Rifle · rolled 12 …
```

The disarmed one attacks `unarmed`; the untouched one still names its rifle.

⚠ **Two things I could not see.** The save **rolls** are not printed — neither
the Reflex nor the Will appears as a `d20 … vs …` derivation, only their
outcomes, so "two separate saves resolve" is inferred from the two
independent outcomes rather than read. And the Will save **failed in both
runs**, so the made-Will branch — *weapon inert for 10 rounds* rather than
destroyed — was never observed.

## 4. Blinded — the square-naming mode

Blinded lands and shows itself on the sheet line as
`defence base 10 + class 11 + power -2 = 19`. It forbids nothing: 5 move,
Action available.

`a` opens the mode, and every clause holds:

```
aiming — arrows to choose a square · enter to swing · esc      ← starts unnamed, on my own square
aiming at 1,1 · enter to swing · esc                            ← after one arrow
you swing where you thought it was — there is nothing there · that was your Action
```

* **Bounded by reach:** five right-arrows and the cursor still reads
  `aiming at 1,1` — it caps at one square, which is unarmed reach.
* **The Action is spent:** the pip goes dark and the verbs collapse.
* **No damage:** the mark stays at `400 of 400`.

⚠ Minor: `a` is not listed in the verb line while blinded, so the mode is
discoverable only by knowing the key.

## 5. Deflection — a reaction, and only against a blow that would land

This confirmed itself on the paralysis board, where the caster happened to
hold both powers:

```
darter: Paralysis Dart · rolled 29 — d20 18 + attack 12 + Dexterity 3 − point blank 4 ·
  needed 21 · — rolled 35 — d20 17 + attack 15 + Strength 0 + Force Redirection 3 ·
  needed 29 — deflected, and sent back
```

* **It is a reaction, and it is priced:** the reaction pips are consumed and
  the Force pool drops per deflection (263 → 239 → 227).
* **Only after a roll that would otherwise hit:** the deflection roll is made
  against **29** — the attacker's own total — and the incoming rolls of 13,
  16, 20 and 15, all short of my Defence 21, produced no deflection at all.
* **Redirection sends it back:** *"deflected, and sent back"*.

⚠ **Force Deflection alone was not isolated.** The caster knew both powers and
the engine used the better one every time — the term in the roll reads
`Force Redirection 3`. So *"with Deflection alone the bolt just stops"* is
not confirmed; it needs a caster who knows only the tier-1 power.

## 6. Force Camouflage — the bonus, and it expires

Measured as a matched pair, using **the base tier as the control**: it
carries no `skill_bonus` at all, costs an Action and rolls no dice, so two
runs differ by the bonus and nothing else. Both arms: swing, cast a
camouflage, end turn, hide.

| | at turn 3 | after 11 rounds |
|---|---|---|
| Force Camouflage (base, inert) | `hidden — 18 beat 9` | `hidden — 19 beat 18` |
| Improved Force Camouflage (+4) | `hidden — 22 beat 9` | `hidden — 19 beat 18` |

**+4 exactly** while running — and the cast line says so itself
(`Bench Caster — +4 Stealth`) — and **identical to the inert control after
11 rounds**, so the 10-round clock expires on its own. The die streams stayed
in step across all eleven rounds (same opposition, same total), which is what
makes the second row a reading rather than a coincidence.

The base tier being inert is confirmed as a by-product: it is the control,
and it moved nothing.

## Also noticed

`⚠ <power> does not say what it may be aimed at` printed on Overload,
Improved Force Camouflage and Force Redirection — the same family-wide
`targets` gap measured in TEST 113 (84 of 106 powers, 38 of them
enemy-aimed).

## Fixtures

`tester-batch` on the shelf: six boards, three creature blueprints, and two
weapon blueprints. ⚠ The darter is **level 12, Dexterity 16 deliberately** —
a level-1 shooter rolled `d20 20 + attack 1 + Dexterity 0 − point blank 4 =
17` against a Consular 20's Defence of 21, so a natural twenty missed and the
board measured nothing.
