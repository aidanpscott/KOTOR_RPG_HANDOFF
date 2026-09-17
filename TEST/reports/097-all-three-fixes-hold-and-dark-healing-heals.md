# TEST 097 — ALL THREE OF TEST 096's DEFECTS ARE CLOSED, confirmed on the same
# fixtures that found them. The blow-and-cast discriminator now pays TWICE
# where it paid once: `100` for the vibrosword kill and `125` for the Force
# Lightning kill, in one fight. A level landed **in the same session** off
# weapon kills alone, and moved the derived numbers with it — vitality 8 of 14,
# pool 29 of 29. Four simultaneous kills from one Force Storm wrote four awards
# and a save that reads back perfectly.
# AND DARK HEALING HEALS: `healed 12d8 48 · 6 → 54`, aimed at its caster, and
# clamped on the second cast at `46 → 74`.
# ⚠ ONE ASK COULD NOT BE EXERCISED AS WRITTEN: a self-power cannot be aimed at
# an ally or an enemy, because the aim is not a choice — `affects: self` forces
# the candidate list to the player. The protection is structural rather than a
# refusal a player can trigger.
# ⚠ AND ONE NEW, SMALL THING: at fifteen saves the `Load Game` dialog OVERFLOWS
# its own box — Flutter's hazard stripe across the bottom and the last row
# clipped behind it.

## Build state

    KOTOR-RPG-APP   704e3b7  PT-2241 — built and measured from this
    lodestar        4be1002  — HEAD's own pin, and the pub-cache checkout
    lens            32b77e3

    ✓ FRESH — built from exactly this source at 09-16 21:59:25

⚠ **The app tree was mid-edit when I started** — `play_screen.dart` and
`a_power_aimed_at_yourself_test.dart`, which is the Dark Healing area itself —
so I tested HEAD rather than your bench. By the end you had more in flight
(`records.dart`, `save_store.dart`, two more tests) and Lodestar had moved to
`0d7b554`. Nothing below is from any of that.

`check_shelf.py` green at both ends, 29 rules files.

---

# 1 · A WEAPON KILL PAYS — on the fixture that found it

The TEST 096 discriminator, unchanged: two priced one-vitality enemies in one
fight, one killed by a vibrosword and one by Force Lightning.

    character.xp-awarded  {subject: Both Again, amount: 125, from: x-cr1.probe.02, cr: 1.0, level: 1}
    character.xp-awarded  {subject: Both Again, amount: 100, from: x-cr0.probe.01, cr: 0.0, level: 1}
    REC level 1 xp 225

**Two awards where there was one**, and the record totals to their sum. The
blow kill is the `cr: 0.0` row — which also keeps TEST 096's other reading
standing: CR 0 still pays its real 100 and records itself as a real CR rather
than as an absence.

And on its own, a weapon-only fight:

    character.xp-awarded  {subject: Weapon Kill, amount: 3000, from: x-cr9.probe.02, cr: 9.0, level: 1}

⚠ The unpriced creature in that same fight (`x-none`, no `challenge`) still
paid nothing. The "absent is not zero" branch is intact — it has simply stopped
swallowing real kills as well.

# 2 · THE LEVEL LANDS IN THE SAME SESSION

No reload, no second rest. Weapon kills, then `e`:

    you rest a day. Nothing needed mending. · level 2 — jedi_consular

and the record:

    REC level 2 xp 3000 classes [{id: jedi_consular, levels: 2}]
    character.xp-awarded  {amount: 3000, from: x-cr9.probe.02, cr: 9.0, level: 1}
    character.levelled    {level: 2, class: jedi_consular, xp: 3000}

The party panel read **`Jedi Consular · 2`** live, in the session that earned it.
TEST 096 needed load-then-rest and got silence twice; this took it first time.

⚠ **And the level is not just a number.** Loading that character afterwards
reads `8 of 14` vitality and `force 29 of 29` — the level-2 Consular's pool is
`8 + (2−1)×5 + (4+4)×2 = 29`, and the vitality die has paid out a second time.
The class list upserted to `jedi_consular 2` against `progress.level` 2, so
`record_validate` rule 5 is satisfied and the save opens cleanly — the
"a save that fails its own validation on load" risk your commit names did not
materialise.

# 3 · THE MULTI-KILL WRITES A CLEAN SAVE

Four priced bodies packed together, **all four killed by one Force Storm**:

    Force Storm · 24f — 159 → 135 · ceiling −8 to 151 · at x-cr0.probe.01 ·
    x-cr0.probe.01 — 12d6 52 · x-cr1.probe.02 — 12d6 35 ·
    x-cr8.probe.03 — 12d6 36 · x-cr9.probe.04 — 12d6 40

Four deaths in one blow, four appends, one settlement — and four awards:

    xp-awarded {amount:  25, from: x-cr1.probe.02, cr: 1.0, level: 12}
    xp-awarded {amount:  25, from: x-cr0.probe.01, cr: 0.0, level: 12}
    xp-awarded {amount: 150, from: x-cr9.probe.04, cr: 9.0, level: 12}
    xp-awarded {amount: 125, from: x-cr8.probe.03, cr: 8.0, level: 12}
    REC level 12 xp 66325   ← 66000 authored + 325 earned

The save **reads back through `readSave` and `replay`** with no complaint, and
the listing counted no new damage. ⚠ Note the table is being read at the
CASTER'S level: at 12, CR 0 and CR 1 both pay `25`, which is `awards.floor` —
*"no cell is worth nothing"* — where at level 1 they paid 100 and 125.

## And the format-3 length check catches a bad write

I hand-built a save whose header is perfect and whose declared payload length is
40 bytes longer than the body — the quiet shape TEST 096's pair had. The
listing named it before anything was chosen:

    15 saves · 1 unreadable: Damaged save: it says it holds 569 bytes of
    contents and the file has 529. Part of another save may have been written
    over it.

`569 − 529 = 40`, exactly the lie. And it is **not offered in the list at all** —
TEST 096's complaint was that a damaged save listed cleanly and failed only
after the player chose it.

⚠ The two format-2 files are still on the disk and are correctly **not** among
the "1 unreadable" — the stated, accepted limit holds, and it is visible rather
than assumed.

# 4 · DARK HEALING HEALS

    Dark Healing · 24f — 159 → 135 · ceiling −8 to 151 · at Healer Two ·
    Healer Two — healed 12d8 48 · 6 → 54

**Aimed at its caster**, `12d8` at Force level 12 (the 15d8 cap not reached),
and the roster confirmed `54 of 74`. A second cast, at 46 after another blow:

    Healer Two — healed 12d8 44 · 46 → 74

`46 + 44 = 90` and it stopped at **74**, the character's maximum. The clamp
holds.

## ⚠ The refusal half cannot be exercised as written

You asked me to confirm it refuses if aimed at an ally or an enemy. **There is
no way to aim it at either.** `_cast` builds its candidate list as:

    final selfAimed = p.affects == 'self';
    final target = selfAimed
        ? _present.where((x) => x.isPlayer).toList()
        : …the enemy filter…

so for a self-affecting power the candidates are the player and nothing else.
The aim is not a choice a player makes, and no refusal is reachable from the
screen — the protection is the candidate list rather than a gate a player can
trip. That is arguably the better design; it is just not the thing that can be
confirmed by trying it.

**What I confirmed instead is the complement**, which is the half `PT-2240`
actually fixed — that the two aims no longer share a picker. From the same
caster, in the same fight, immediately afterwards:

    Force Lightning · 14f — 111 → 97 · at x-hitter.probe.01 · 12d6 39

aimed at the **enemy** (4000 → 3961) while my own vitality stayed `74 of 74`.
Self power to the caster, offensive power to the enemy, one after the other.

---

# ⚠ NEW — THE LOAD GAME DIALOG OVERFLOWS AT FIFTEEN SAVES

With fifteen saves in the list, the dialog runs past its own box: Flutter's
black-and-yellow overflow stripe across the bottom, **`BOTTOM OVERFLOWED BY 32
PIXELS`**, with the last row half-hidden behind it and `Back` pushed to the
screen edge. Captured at `scratchpad/overflow.png`.

It is only a layout fault and the list still works, but it is in shipped UI on
a screen every player uses, and the number of saves only goes up. A release
build will not draw the stripe — it will just clip the row silently, which is
the worse half.

---

## Method

⚠ Every player is an authored save, in the product's own format — the same
lever as TEST 095/096, now writing **format 3** with the payload length, which
is also what let me forge the bad-length file deliberately rather than waiting
for a race. I read every save back through `readSave` + `replay` in a throwaway
test inside **my scratchpad copy**; your `test/` was never touched.

⚠ Two fixture notes, declared: `x-hitter` began at level 10 with Strength 18
and killed me outright in four rounds, so I softened it to level 3 / Strength
10 — what is under test is the heal, not its survival odds. And a save whose
log carries `character.moved` resumes in the area it recorded, overriding the
package's `[entry]`, so each area needed a fresh authored character.

## What I did not do

- **Did not exercise a refusal on a mis-aimed self-power** — see above; it is
  not reachable from the screen.
- **Did not test aiming at an ALLY specifically** — my fixture has no companion,
  and the candidate list makes the question moot either way.
- **Did not re-test the two format-2 damaged files** — you named that limit and
  I only confirmed they are still excluded from the count.
- **Loom not launched.**

## State

- `xp-probe` is mine, now eight areas; `a04-both` is the blow-and-cast
  discriminator and `a07-cluster` the four-at-once one.
- ⚠ **`badlen.sav` is left on disk deliberately** — a perfect header over a
  mis-stated length, so the new listing check reproduces in one launch.
  `xp-two.sav` and `kaeda-sabek.sav` are also still there, as the format-2
  pair that is knowingly out of reach.
- My build lives in the scratchpad copy only. **Your `build/` was never written
  to and neither shared bundle was touched.**
- App pids `339631`, `340547`, `341858`, `344266`, `344767`, `345618` all
  killed by pid and confirmed gone; no Loom; nothing of yours touched.
