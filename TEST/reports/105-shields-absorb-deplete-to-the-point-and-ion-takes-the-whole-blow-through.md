# TEST 105 — Shields absorb, deplete to the point, and ion takes the whole blow through

**Build under test.** KOTOR-RPG-APP `9358ca4` *"PT-2314: `g` raises a shield — the fifth budget
finally spends"*, working tree clean. Lodestar **`2538653c`** (moved again — `25ad8e2c` in
TEST 104), Lens `32b77e3b`; `package_config.json` resolves to the checkouts that compiled, which
are the ones I read the engine from. `fresh.py --debug --build` printed
`✓ FRESH — built from exactly this source`. `check_shelf.py` green: 29 rules files, 65 standard
blueprints.

All five routed items confirmed.

---

## 1. Absorption works, and raising spends Gear rather than the Action

```
gear yourself — Mandalorian Melee Shield up, 50 against bludgeoning, piercing, slashing
              · ⚠ ion goes straight through · 2 left
```

The line names the pool, the flagged kinds, the hole and the charges remaining (3 carried → 2).

**Gear is not the Action** — I attacked in the same turn, immediately after raising:

```
Vibrosword · rolled 28 — d20 18 + attack 8 + Strength 2 · needed 14 — hit
           · damage 12 — 1d12 9 + Strength 3 · 388 left
```

**And the pool absorbs.** The attacker's next connecting blow:

```
hacker.sh.01: Vibro Double-Blade · hit · damage 9 — 2d8 6+3 · 60 left
```

Nine damage printed; Warder unmoved at `60 of 68`. Vitality is the reading here — the strike
line reports what was rolled, so absorption shows as the gap between the printed damage and the
vitality that actually moved.

## 2. Ion takes the WHOLE blow through, not just its own part

The control and the test differ by one thing: a 5-point ion rider on the same base weapon.

- **Control** (item 1 above): `Vibro Double-Blade`, 2d8 slashing, against the 50-point melee
  shield — **absorbed entirely**.
- **Test**: `Yusanis' Brand`, catalogue `g_w_vbrdblswd05`, the same `vibro-double-blade` base with
  `[[items.stats]] stat = "damage", kind = "ion", base = 5`.

```
Yusanis' Brand · damage 11 — 2d8 1+2 + 5 ion + 3  8 · 41 left     Warder 52 → 41   (−11, all of it)
Yusanis' Brand · damage 17 — 2d8 6+3 + 5 ion + 3  8 · 24 left     Warder 41 → 24   (−17, all of it)
Yusanis' Brand · damage 17 — 2d8 1+8 + 5 ion + 3  8 ·  7 left     Warder 24 →  7   (−17, all of it)
```

Shield up the whole time with a **full 50-point pool** against a blow whose slashing half it
stops. Every point landed. Had the shield stopped the non-ion portion, Warder would have lost
about 5 a hit; it lost 11, 17 and 17. **The hole is in the shield, not in the damage** — confirmed.

## 3. The pool depletes, and the crossing is exact

One fight, 50-point pool, tracked hit by hit:

| hit | printed damage | vitality | absorbed | pool left |
|---|---|---|---|---|
| 1 | 9 | 60 → 60 | 9 | 41 |
| 2 | 9 | 60 → 60 | 9 | 32 |
| 3 | 7 | 60 → 60 | 7 | 25 |
| 4 | 15 (crit, 4d8 ×2) | 60 → 60 | 15 | 10 |
| 5 | 6 | 60 → 60 | 6 | 4 |
| **6** | **7** | **60 → 57** | **4** | **0** |
| 7 | 9 | 57 → 48 | 0 | 0 |
| 8 | 9 | 48 → 39 | 0 | 0 |

Hit 6 is the boundary: 7 damage against 4 points left, so **4 absorbed and 3 landed**. After that
the shield is spent and hits land in full — no silent continued absorption, and no partial.

Total absorbed = 9+9+7+15+6+4 = **50**, exactly the pool. The arithmetic closes on the nose.

## 4. The flagged-kinds list is read — a 2×2 on identical dice

Runs B and D used the same board, the same attacker and produced **identical dice** (`rolled 19`
critical for 18, then `rolled 16` for 6, misses in between), so the only variable is which shield
was raised:

| shield raised | flagged kinds | vs Vibro Double-Blade (slashing) | vs Blaster Rifle (energy) |
|---|---|---|---|
| Mandalorian Melee Shield | bludgeoning, piercing, slashing | **absorbed** (§1) | **landed** — 68→50, 50→44 |
| Droid Deflector Mark I | electrical, energy | — | **absorbed** — 68→68→68 |

The energy blows that took 18 and 6 off Warder under the physical shield took **nothing** under
the energy shield, on the same rolls. The list is being read, not merely the presence of a shield.

## 5. Both families behave identically

```
gear yourself — Droid Deflector Mark I up, 50 against electrical, energy · ⚠ ion goes straight through · 2 left
```

Same sentence, same mechanism, same absorption as the organic armbands. Both families' catalogue
rows carry `base = "shield-generator"`, and all 31 absorb items in the catalogue share the same
shape — I surveyed them: every one carries `vulnerable = ["ion"]`, and they differ only in `pool`,
`kinds` and `category` (`forearm` for the armbands, `shield` for the droid units).

⚠ **What that cross-check does and does not prove.** `catalogue = "..."` does **not** carry an
item's effect fields into a blueprint: `item_open` builds `values` from the `[item]` table's own
keys, so a blueprint must state `pool`, `kinds` and `vulnerable` itself. Mine transcribe the
shipped rows verbatim (`a_shield_02`, `a_shield_01`, `d_shield_01`), so the numbers are real — but
both families necessarily reach the engine through the same base type, so "identical" is partly
true by construction rather than only by observation.

⚠ **A field with no reader, offered as a source reading and not as a finding.** Every droid shield
in the catalogue carries a `[[items.gates]]` feat gate (`Droid Upgrade 1/2/3`, and a
`UseLimitationPC (T3-M4)` on the renewable one). Nothing on the raise path consults it —
`consumableAt` and `_aShield` never look at gates, and `item_open` does not parse a `gates` key at
all. So a droid-only shield sitting in an organic's bag would be raised without objection. I could
not construct that case honestly in play, because a package blueprint cannot carry a gate to
begin with, so this is read from the source rather than observed. Flagging it because a gate that
nothing reads is the shape this project keeps finding.

## Fixture note

The bag is folded from `item.acquired` events keyed on `payload['subject']`, which for the player
is `_me.handle` — the character's name. The chargen equipment `items` list never reaches
`_carriedItems`, which is why the first attempt answered `gear — nothing to use` with three
shields apparently in inventory. Authoring the acquire events directly is the lever.

## Not tested

- The K2 Repair-skill duration scaling, as routed — the pool ended every shield well before any
  clock did, exactly as predicted.
- A shield raised on an **ally** rather than yourself. The picker offers it (`used_on` is
  *"yourself or an ally within reach"*) and the cast auto-took `yourself` with nobody else on the
  board; I kept the fixtures to one attacker because `_enemyTurns` overwrites the status line and
  the reading needs both the printed damage and the vitality that moved.
- Whether a second shield can be raised over a standing one. `raiseShield` refuses it explicitly
  and says why; I did not exercise the refusal.
