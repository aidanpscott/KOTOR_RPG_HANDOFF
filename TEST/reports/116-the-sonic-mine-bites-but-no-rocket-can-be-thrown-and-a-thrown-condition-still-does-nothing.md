# TEST 116 — the sonic mine bites, but no rocket can be thrown and a thrown condition still does nothing

**Build.** App **`80f30ad`** (PT-2409), built from `git archive`. Committed
and working `pubspec.lock` agree on Lodestar **`3415400a`**, which is the
checkout `package_config.json` compiles against. `check_shelf.py` clean.
(Working tree carried edits to `test/sandbox.dart` and an untracked probe
test — test files only, and the build comes from the commit.)

**Verdict.** Item 3 is confirmed and bites. **Items 1, 2 and 4 are not
fixed**, for two independent reasons that sit one after the other in the
same path. Item 5's launcher *gate* works, but nothing can pass through it.

---

## The two blocks, stated once

Everything below turns on these, so they are worth stating together.

**(A) No rocket blueprint can be both openable and selectable.**

```
rocket.takes = { damage_over_time: [amount, kinds, rounds, save, count?, sides?],
                 condition:        [condition, rounds, save] }
```

`deploy` is in neither list, and `takes` is strict both ways — so a blueprint
faithful to the shelf row is refused at open:

```
`Paralysis Dart` carries deploy, which it does not take.
`rocket` doing condition takes condition, rounds, save.
```

Drop `deploy` and it opens — with `deploy = null`. But the selector filters on
`deploy` **before** it ever reaches the rocket branch:

```dart
if (c == null || c.deploy != deploy) continue;      // needs 'thrown'
if (c.base == 'charge') return path;
if (c.base == 'rocket' && _hasLauncher) return path;  // never reached
```

The comment on that branch says *"The eleven rockets carry `deploy = thrown`
read from their own blueprints"* — they cannot, because their base type
refuses the field.

**This is observable as a contradiction inside one bag.** The same save, the
same three Paralysis Darts:

```
bag without the launcher :  throw — a rocket needs the Wrist Launcher, and you are not carrying one
bag WITH the launcher    :  throw — no grenade
```

`_rocketWithoutLauncher` loops the bag with no `deploy` filter and **sees the
rockets**; `_aChargeThat` filters on `deploy` and **cannot**. One function
says you are carrying rockets, the other says you have nothing to throw.

**(B) A thrown non-damage effect is still unimplemented.** Unchanged from
TEST 106:

```dart
if (e.does != EffectKind.damage) {
  return '${who.handle} — ⚠ ${it.does} is not thrown yet';
}
```

So even past (A), the `rocket` base offers only `damage_over_time` and
`condition`, and neither can be thrown.

**Why the suite is green.** `a_rocket_needs_a_launcher_test.dart` asserts
against **catalogue rows** — `row.id`, `e['deploy']` — that all eleven state
`deploy = thrown`. The data does. Nothing in it opens a blueprint or reaches
the throw path, so it cannot see that an authored rocket is refused at one
end and invisible at the other.

## 1. The Paralysis Dart, full loop — not closed

Not reachable, per (A) and (B). What I could confirm:

* The dart's row now **reads correctly**, including the nested branch —
  `consumableAt` returns
  `save: {dc: 20, kind: fortitude, on_save: instead, instead: {does: condition,
  condition: slowed, rounds: 1}}`. PT-2405's fix is real and visible: the
  `instead` the reader used to drop now survives.
* But it can never be thrown, so `paralysed`, its 2-round expiry and the
  made-save `slowed` were all unobservable.

The condition itself was confirmed enforced and expiring in TEST 115 (0 move,
no Action, budget back after its stated 2 rounds); nothing here changes that.

## 2. CryoBan — not fixed, and it cannot do both in any case

Thrown directly, with the grenade in the bag:

```
throw CryoBan Grenade at mark.rg.01 — mark.rg.01 — ⚠ condition is not thrown yet ·
  Rocketeer — ⚠ condition is not thrown yet · 1 left
```

Per (B). And separately, **one carried CryoBan cannot carry both effects**:
`ConsumableItem.does` is a single verb, and a blueprint stating the
catalogue's damage *and* condition is refused —

```
`CryoBan Grenade` carries condition, rounds, which it does not take.
`charge` doing damage takes amount, kinds, save, deploy, plus_vs_droid (optional).
```

So whatever the catalogue row states, a CryoBan in play is the damage arm or
the paralysis arm, never both.

**Had I seen it "work" before?** No — and I checked the record rather than
trusting memory. CryoBan appears exactly once in my reports, in TEST 084, and
only in a *data* table of grenade save types. TEST 106 threw **Frag, Adhesive
and Ion** only. What TEST 106 did find is this same branch, in these words:
*"`nade-a.nd.01 — ⚠ condition is not thrown yet`"*. So I have no prior
observation of CryoBan delivering anything, and the failure mode the routing
describes — damage lands, the second effect vanishes silently — is not one I
have ever seen; the product says `not thrown yet` out loud.

## 3. The sonic mine — confirmed, and it bites

Set and stepped on:

```
set — armed at easy (10)
goes off — d20 5 = 5 vs 15 · −2 Dexterity for 5 rounds
```

**And the penalty is not just printed.** The same enemy, same weapon, same
board, its `needed N` against me round by round:

| round | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| needed | 16 | 16 | 16 | 16 | **17** | 17 | 17 | 17 |

Defence **16 while the penalty ran and 17 after it lapsed** — exactly the +1
a −2 Dexterity costs — and the step lands on the stated 5-round clock. A
single self-controlled run: the before and after are the same creature.

⚠ One data note: the five shipped sonic mine rows state **no `save` at all**,
while `charge`'s `takes` for `ability_penalty` requires one. My blueprint had
to author a save that the shipped row does not carry.

## 4. The Concussion Rocket — unreachable, and Knockdown is genuinely absent

Blocked by (A) and (B) like every rocket. Confirming the data half: the
shelf's `w_rocket_11` carries **one** effect, the stun —

```
{does: condition, condition: stunned, rounds: 2,
 save: {dc: 15, on_save: none, kind: fortitude}, deploy: thrown}
```

No Knockdown row at all, which matches the routing's *"deliberately still
unbuilt"*. So the half that should still not apply is correctly absent from
the data; the half that should now land cannot be delivered.

## 5. Deliverability — the gate works, the door does not open

* **The gate is real and it names itself**, which is the PT-2407 improvement:
  `throw — a rocket needs the Wrist Launcher, and you are not carrying one`,
  rather than the bare *"no grenade"*.
* **But nothing passes it** — see (A).
* ⚠ **And the launcher is matched by blueprint FILENAME, not by catalogue
  id.** `_hasLauncher` reads
  `_shortItem(path).contains('g_i_wristlaunch')`, and `_shortItem` is the
  path's last segment. Its own comment says *"BY RESREF, NOT BY NAME … a name
  match would break on any package that renames it."* It is a name match, and
  the rename breaks it — measured with a matched pair, two blueprints with the
  **same `catalogue = "g_i_wristlaunch"` and the same item name**, differing
  only in file name:

  ```
  bag holds g_i_wristlaunch.toml  →  gate passed (reaches "throw — no grenade")
  bag holds launcher.toml         →  throw — a rocket needs the Wrist Launcher
  ```

## What would close items 1, 2 and 4

One reading settles the lot once the path exists: throw a Paralysis Dart and
see `paralysed` land, run its 2 rounds and lapse, with a made Fortitude save
against DC 20 leaving `slowed` for exactly 1. The pieces are all present —
the row reads, the `instead` survives, the condition is enforced — and only
the delivery is missing.

## Fixtures

`tester-rockets` on the shelf (named `0 Rocket Bench (Tester)` so the library
carousel can reach it — it does not scroll past the fourth card). Nine
blueprints including the two launchers that differ only in file name, and the
three CryoBan variants that establish which combinations the format accepts.
