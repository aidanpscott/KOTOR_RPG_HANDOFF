# TEST 109 — A two-handed grip lifts a bonus and leaves a penalty alone

**Build under test.** KOTOR-RPG-APP `abec19d` *"PT-2338: the app-side two-handed pin follows the
ruling"*. ⚠ **`pubspec.lock` was modified in the working tree** — the committed lock resolves
Lodestar to `4032d57c`, the uncommitted one to `4e85e240`. Built from a `git archive` of the
commit, so the pairing under test is the committed one. **Both refs carry the identical rule**, so
the dirty lock changes nothing here — I checked rather than assumed:

```dart
final lifts = twoHanded && strengthModifier > 0;
final v = lifts ? (strengthModifier * 3 / 2).floor() : strengthModifier;
```

Lens `32b77e3b`. `fresh.py --debug --build` printed `✓ FRESH — built from exactly this source`.
`check_shelf.py` green: 29 rules files, 65 standard blueprints.

Both directions confirmed.

## Which weapon is actually two-handed

Worth stating, because it is not the obvious one. `attack.dart` computes
`twoHanded: !isDoubleWeapon(base) && <off-hand empty>`, and `isDoubleWeapon` is `attacks == 2`.
So the **vibrosword** (1 attack) is two-handed with an empty off-hand, while the **vibro-double-blade**
(2 attacks) is *not*. Every reading below uses a vibrosword in `weapon_r_1` with no off-hand item.

## The readings

| who | Strength | attack term | damage term | expected |
|---|---|---|---|---|
| caster | 18 (+4) | `+ Strength 4` | **`+ Strength 6`** | floor(4 × 1.5) = 6 |
| `weakarm` | 4 (**−3**) | `− Strength 3` | **`− Strength 3`** | unmultiplied |
| `strongarm` | 18 (+4) | `+ Strength 4` | **`+ Strength 6`** | floor(4 × 1.5) = 6 |

**The negative case**, which is the routed one:

```
weakarm.ar.01: Vibrosword · rolled 17 — d20 17 + attack 3 − Strength 3 ·
               needed 17 — hit · damage 3 — 1d12 6 − Strength 3 · 81 left
```

`−3`, and the arithmetic closes independently: the die rolled 6, the term took 3 off, damage was
3, and my vitality moved 84 → 81. The two readings that multiply a penalty would have given

- truncate `(-3 × 3) ~/ 2` = **−4** → damage 2, vitality 82
- floor `(-3 × 1.5).floor()` = **−5** → damage 1, vitality 83

Strength 4 is the right fixture value for exactly the reason the ruling gives: at −1 all three
readings return −1, which is why the old pin could not tell the rule from the accident.

**The positive case:**

```
Vibrosword · rolled 34 — d20 20 + attack 10 + Strength 4 · needed 14 — hit ·
             damage 24 — 2d12 8+10 + Strength 6 × 2 critical · 376 left
```

`+4` on the attack and `+6` on the damage, from one modifier — the multiplier is damage-only and
rounds down, both still correct.

## ⚠ The control the negative reading needed

A negative modifier reads the same whether the weapon is two-handed or not — `lifts` requires
`twoHanded` **and** `modifier > 0`, so a weapon that never lifted at all would also print `−3`.
The negative reading alone therefore does not establish that `weakarm`'s vibrosword was
two-handed on the creature path, and without that it is a test that would pass with the rule
deleted.

So I ran `strongarm`: **the same blueprint and the same single-slot equipment shape, Strength 18
instead of 4**. It lifted — `damage 16 — 1d12 10 + Strength 6`, and again `damage 7 — 1d12 1 +
Strength 6`. The creature path does apply 1.5× with this weapon, so `weakarm`'s `−3` is a genuine
"two-handed, negative, unmultiplied" reading rather than a grip that was never two-handed.

That also means the positive half is confirmed on **both** paths — the player's own attack and a
placed creature's — which the routing only asked for once.

## Not tested

- The species route the brief suggested (`droid-remote` at −4, or the four species at −2). I used
  a creature blueprint at Strength 4 instead: `record_validate` caps a *bought* score at 8..18, so
  a player needs a species adjustment to get below it, and a droid player brings `PT-1458`'s
  separate no-bought-abilities rule with it. The creature route reaches the same modifier through
  the same `damageTerms`, and the caster covers the player path for the positive half.
- A **negative** modifier on the *player* path specifically. Both paths agree on the positive half
  here, and the rule is one expression in `combat.dart` with no player/creature branch, but I did
  not observe it and am not claiming it.
- Whether an occupied off-hand correctly switches the multiplier off. `twoHanded` reads the
  off-hand slot and every fixture here left it empty.
