# TEST 107 — The floored modifier reaches every site I could observe, and one that cannot move

**Build under test.** KOTOR-RPG-APP `8fd74cf` *"PT-2325: the other seven ability modifiers"*.
⚠ **`pubspec.lock` was modified in the working tree** — uncommitted, bumping Lodestar from the
committed `54e21404` to `457de5fd`. I built from a `git archive` of the commit, so the pairing
under test is the committed one. Both refs carry
`int abilityModifier(int score) => ((score - 10) / 2).floor();`, so the commit compiles with the
fix either way and the bump is not part of it. Lens `32b77e3b`. `fresh.py --debug --build` printed
`✓ FRESH — built from exactly this source`. `check_shelf.py` green: 29 rules files, 65 standard
blueprints.

Three of the four routed items confirmed. The fourth **cannot move** — the site was fixed, but the
output it feeds cannot distinguish the old value from the new one, for a reason in the engine.

## The character

One Gamorrean covers every ability the routing needs: its line is
`+4 Strength, −2 Dexterity, −2 Intelligence, −2 Charisma`. A **bought 9** — legal, inside
`record_validate`'s 8..18 — lands each of Dexterity, Intelligence and Charisma on an effective
**7**, which is the odd-below-10 case where the two derivations disagree: `7 − 10 = −3`, floored
**−2**, truncated −1.

## 1. Force pool — confirmed, and it is the Charisma half specifically

```
force 39 of 39
```

Jedi Consular 12, `d8`, Wisdom 10 (modifier 0, deliberately unadjusted) and Charisma 7:

```
8 + (12−1)×5 + (0 + −2)×12  =  8 + 55 − 24  =  39      floored
8 + (12−1)×5 + (0 + −1)×12  =  8 + 55 − 12  =  51      truncated
```

The pool read **39**. Wisdom carries no species adjustment here, so the whole of the difference is
Charisma's modifier, and it is the floored one.

## 2. ⚠ Reaction pool — the site was fixed, but this output cannot show it

`dexModifier` now goes through `abilityModifier` at that call site. The pool still cannot change,
and that is not a defect — it is the shape of the function:

```dart
final byDex = band(dexModifier, const [1, 3, 5]);
final byBab = band(baseAttackBonus, const [1, 6, 11]);
return byDex > byBab ? byDex : byBab;
```

`band` counts how many steps a value reaches, and the lowest step is **1**. Every score the `~/`
bug touches is odd and below ten, so its modifier is −1 or lower — below the first step either
way:

| dexModifier | −3 | −2 | −1 | 0 | 1 | 3 | 5 |
|---|---|---|---|---|---|---|---|
| byDex | 0 | 0 | 0 | 0 | 1 | 2 | 3 |

So `byDex` is 0 for the truncated −1 **and** the floored −2, and the pool is whatever the
base-attack ladder says. In play it read two reactions, which is the ladder's answer and would
have read two before the fix as well. **Reporting this as unobservable rather than as a pass** —
the number agreeing with expectation here says nothing, because no value of the modifier the bug
can produce would have made it disagree.

## 3. The sheet and the fight now agree — confirmed, and this is the sharp one

Both numbers on screen at once, same frame:

```
defence base 10 + Dexterity -2 = 8
hacker.sh.01: Vibro Double-Blade · rolled 19 — d20 16 + attack 3 + Strength 0 ·
              needed 8 — hit · damage 8 — 2d8 4+4 · 66 left
```

The sheet's derivation **names the Dexterity term as −2**, the floored value for an effective 7,
and the incoming attack resolved against **8** — the same number. Under the old truncation the
sheet's term would have been −1 and the displayed Defence 9. The two derivations that used to
disagree now produce one number.

## 4. Skill budget at first level — confirmed, and the screen shows its own arithmetic

```
points remaining                          12 of 12
(5 from your class + -2 for Intelligence) × 4
```

`(5 + −2) × 4 = 12`. The deleted rival formula was
`static int intModifier(int score) => (score - 10) ~/ 2`, which on a 7 gives −1, so
`(5 + −1) × 4 = 16` — **four points the character had not earned**, exactly as the ruling
describes. The budget read 12.

## An eighth reading that fell out on the way

The chargen abilities screen is one of the swept sites, and it displays the modifier directly:

| ability | bought | species | total | bonus shown |
|---|---|---|---|---|
| Strength | 14 | +4 | 18 | **+4** |
| Dexterity | **9** | −2 | **7** | **−2** |
| Constitution | 17 | — | 17 | **+3** |
| Intelligence | **9** | −2 | **7** | **−2** |
| Wisdom | 15 | — | 15 | **+2** |
| Charisma | **9** | −2 | **7** | **−2** |

Every odd-below-ten total shows −2 where the old truncation showed −1, and the even and
above-ten rows are unchanged — which is the control: a sheet that had simply been shifted
downward everywhere would be a different defect.

## ⚠ One adjacent gap, offered as a source reading

`adjustmentBySpeciesId` in `abilities_screen.dart` builds each `AbilityAdjustment` with **str, dex,
con and wis only**; `intg` and `cha` are never passed and default to 0. That map feeds
`abilityAdjustmentBySpecies`, which serves **placed creatures** — so an authored creature of a
species whose line adjusts Intelligence or Charisma would not receive it. The player is unaffected:
`main.dart` builds the player's own `abilityAdjustments` from `adjustmentsFor(...).byAbility`,
which carries all six, and that is what `_ability()` reads — which is why §1's Charisma reading
works at all.

This is the same shape the block's own comment records being fixed once already: wisdom was added
at `PT-2163` because *"a species line that adjusts Wisdom has to reach the roll or the adjustment
is real on the sheet and absent in the fight."* Two of the six are still in that state. Read from
the source, not observed — I did not place a creature to test it, and it is outside this routing.

## Fixture note

⚠ Two windows share the app's PID — a `com.example.kotor_rpg_app` shell and the real
`kotor_rpg_app` surface — and my launcher took `xdotool search --pid | tail -1`, which is not
stable across launches. It picked the wrong one this session and every screenshot came back empty.
The helper now matches on the window **name**.

## Not tested

- The Loom creature-editor site named in the commit. It is a different app and was not routed.
- An odd score below 10 reached any way other than a species −2 on a bought 9. `record_validate`
  refuses a bought 7 outright (*"outside 8 to 18"*), so the species route is the only one a
  legal character has.
- `check_ability_modifier.py`, the guard the commit says makes the single-derivation claim true.
  Running Coder's own guard is not a confirmation of behaviour and I left it alone.
