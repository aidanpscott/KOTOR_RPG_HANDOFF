# TEST 103 — The Revitalize sentence lands, and two annotation fragments survive in player-facing prose

**Build under test.** KOTOR-RPG-APP `18bed1b` *"PT-2298: a cast that revives nobody says so"*,
working tree clean. Lodestar `2d5d696b`, Lens `32b77e3b` — `package_config.json` resolves to the
checkouts that compiled. `fresh.py --debug --build` printed
`✓ FRESH — built from exactly this source`. `check_shelf.py` green: 29 rules files, 65 standard
blueprints, all identical to what the extracts generate.

Both routed items confirmed. One new finding, from a sweep beyond the brief.

---

## 1. Revitalize's wording — confirmed, the prose dump is gone

Cast on a party that is entirely on its feet. The **whole** status line:

```
Revitalize · 12f — 143 → 131 · ceiling −2 to 153 · at kin-near.leak.01 · nobody here has fallen
```

Against the same power's reading in TEST 101, on the same build family:

```
Revitalize · 12f — 99 → 87 · ceiling −2 to 142 · at ward-fallen.fallen.01 · This power allows the
Jedi to rekindle the life energies of any non-droid fallen ally. This brings the single closest
fallen ally back to consciousness with 10 Vitality Points. ⚠⚠ THE PERCENTAGE IS DEAD CODE. The
developers replaced it with fixed amounts and said so in the script, dated and with a bug number;
our own figures matched neither what ships nor what they removed, and inverted the tiers besides.
```

Completely replaced. No effect prose, no `⚠`, no `PT-2284`, no dead-code commentary. It still
resolves and charges — 143 → 131 is the full 12, and the ceiling still takes its −2 — which is the
ruling as written rather than a refusal.

---

## 2a. The annotation leak — closed on every power I could reach

All 37 remaining `⚠` glyphs in `powers.toml` now sit on a `note` key, and **nothing in the app
renders a power's `note`** — the `.note` hits in `lib/` are weapon and on-hit notes and chargen
fields, none of them `PowerRecord.note`. Three casts, three clean readings:

```
Sever Force · 22f — 131 → 109 · ceiling −7 to 146 · at dummy.leak.03 · Developed as a punishment
for Dark Jedi and Sith, though the Sith learned to turn it outward. The target's connection to the
Force is cut for 10 rounds: its Force Points are LOST, and regeneration stops for the duration. A
Will save at DC 5 + the attacking character's level + Wisdom and Charisma modifiers negates.

Force Static Field is aimed at droid, not a sentient — nothing spent

Shutdown · ... The user draws the energy from a weapon's power cell and disperses it. One blaster
or vibro-cell weapon held by a target within 10 metres. ...
```

Sever Force's own `note` — *"⚠ The third tier of the Force Suppression → Force Breach chain —
PT-473. ⚠ The only power in the corpus that attacks a Force POOL…"* — did not appear. Force Static
Field gave a plain refusal and spent nothing. No bug numbers, no glyphs, no source commentary.

## 2b. The data check — radius and kind exclusion both intact, in one cast

Both mechanical dependencies the annotation move touched, measured by a single Improved Heal on
the first action of a fight, with the board screenshotted at the instant of the cast:

```
(0,2) caster   (1,2) kin-near HUMAN   (2,2) kin-droid DROID   (3,2) dummy ENEMY   (10,2) kin-far HUMAN

Improved Heal · 16f — 159 → 143 · ceiling −4 to 155 · at kin-near.leak.01
  kin-near.leak.01 — healed 15 +4 cha +4 wis +12 level 35 · 58 → 60
  Leaker           — healed 15 +4 cha +4 wis +12 level 35 · 74 → 74
```

Reached exactly two. Not named, and both still at `60 of 60` afterwards:

- **`kin-droid.leak.02`** — a companion standing **1 square from the centre**, comfortably inside
  radius 7. Excluded by KIND, and distance cannot explain it.
- **`kin-far.leak.04`** — a companion **9 squares from the centre**, in plain sight and in the
  fight. Excluded by RADIUS, and role cannot explain it.

`kin-near` at the centre and the caster at 1 are the positive controls — without them "nothing was
named" and "the radius has vanished" would read alike. The derivation is also unchanged from
TEST 100 and TEST 101: `15 +4 cha +4 wis +12 level` = 35.

So the thirteen powers' radius data survived the move, at least on the row I could exercise, and
the droid exclusion the same fix depended on is still honoured.

---

## ⚠ NEW — two annotation fragments are still in the player-facing `effect` field

The sweep moved whole annotation *sentences* into `note`. Two rows had the annotation joined to
the prose with `. — ` instead, and on those the fragment stayed behind in `effect`:

```
force_plague   "… A Fortitude save at DC 5 + Force levels + Wisdom and Charisma modifiers.
                — ruled Fortitude, never written down."
shutdown       "… or the weapon is inert for 10 rounds.
                — a well-maintained cell is harder to bleed."
```

Those are the only two in the file (`. — clause.` at the end of an `effect`), so this is a narrow
miss, not a general failure.

**`force_plague`'s is the one that matters.** *"ruled Fortitude, never written down"* is a
statement about the authoring process — that the save kind was ruled rather than transcribed —
and it is exactly the category this fix set out to remove. Its sibling annotation is already in
`note` (*"⚠ PT-2189, and the same gap Force Contagion's row had…"*), so the clause was left behind
rather than deliberately kept.

**Shutdown's I rendered live**, in the cast quoted in §2a — it is the tail of that sentence. It
explains a rule that is NOT in the prose it is attached to: the +2-per-upgrade-slot save bonus
lives in `note`, so the player is given the justification for a mechanic they are never told
about. Its `note` carries a matching orphan (*"⚠ Lightsabers are immune.— a beast holds nothing.
PT-463."*), which is the same join in the other direction.

⚠ **Scope, stated plainly.** I rendered **Shutdown's** fragment in play. I did **not** render
`force_plague`'s: it is single-target with no kind exclusion, so `caught` is never empty and the
cast path's prose fallback is unreachable for it. Its exposure is the other render site —
`chargen/powers_screen.dart:206-209` draws `p.effect` when a power row is expanded, which is a
plain player-facing surface. I stopped short of walking the ten-step chargen strip to photograph
it, so that half is a data-and-source reading rather than an observation, and I am marking it as
such rather than implying I saw it.

Neither is a bug number reaching a player, and neither breaks a mechanic. Filing it because the
routing asked me to confirm the category is gone, and on two rows it is not.

## Not tested

- Improved/Master Energy Resistance, the fourth power named for the leak check. Three of the four
  were clean and the mechanism is shared; I spent the remaining slice on the data sweep instead.
- The other twelve radius rows individually. One was exercised end to end; the rest are the same
  column read by the same code path.
