# TEST 118 — rest and both meditations confirmed in play, and alignment has no readout to confirm it with

**Build.** App **`9d69f33`** ("the alignment engine gets its input — PT-2433"),
built from `git archive` with HEAD's **committed** lock, Lodestar
**`4cf6dce`**. `check_shelf.py` clean.

⚠ The working tree was dirty — `records.dart`, `play_screen.dart` and
`pubspec.lock`, bumping Lodestar to `3ed4fde` ("perception: distraction is a
perception fact", PT-2435/2436). That is a different thread and its diff
touches nothing in this batch. I tested the committed state.

**Verdict.** Items 1, 2 and 3 confirmed in play, to the point. **Items 4 and
5 cannot be confirmed in play at all: nothing in the app displays an
alignment score or band.** `alignmentFrom` has no caller anywhere in `lib/`
— every match for "alignment" in the app is Flutter's `CrossAxisAlignment`.
What I could do instead, and did, is verify both halves of the seam: the app
writes correct inputs from real play, and the production fold produces the
right answers over that real log.

---

## 1. Rest — confirmed, both halves, and it names the distinction

**Vitality, at the rate rather than the cap:**

```
you rest a day · vitality 1 → 161 of 162
```

A gain of exactly **160 = level 20 × 8 hours**, landing one short of the
maximum — so it is demonstrably the rate and not a fill-to-full.

⚠ Getting that reading needed deliberate engineering, and it is worth
recording why: a night's gain is `level × 8`, while maximum vitality is
roughly `level × (die average + con modifier)`. For an ordinary build the
nightly gain **always exceeds the maximum**, so every full night heals to
full and the rate is invisible behind the cap. This character is
Constitution 18 at level 20 — max 162 against a nightly 160 — and was taken
to 1 by a 161-damage mine. Any gentler setup would have "confirmed" the rate
without testing it.

**Force, to the working maximum, with the reason stated:**

```
you rest a day · Force 87 → 171 of 171 · ceiling still 171 of 183 — rest does not restore it
```

The pool refills to **171**, the degraded ceiling, not the true 183 — and
the product **says why in words**. The sidebar carries the same fact as
`force 171 of 171 · exhausted from 183`.

## 2. Short meditation — 75% of what was lost, twice a day, and the cap survives a reload

```
ceiling 165 → 178 of 183 · Force 39 · nothing mended
```

* **75% of LOST, exactly.** Lost was `183 − 165 = 18`; the restore is
  `18 × 3 ÷ 4 = 13`; `165 + 13 = 178`. Not 75% of the maximum (137) and not
  75% of the current ceiling.
* **It does not refill the pool** — `Force 39` is unchanged; only the ceiling
  moves.
* **It heals nothing** — `nothing mended`.
* Confirmed twice, at two different ceilings: the earlier run read
  `ceiling 171 → 180 of 183` (lost 12, restore 9).

**The cap, and its persistence:**

```
you have already composed yourself twice today — a full night is what is left
```

⚠ **The decisive detail is which two:** the first of the day was taken
*before* a reload and the second after it. The third was refused. So the
two-a-day cap counted across the reload — the hole PT-2432 shipped knowingly
and PT-2433 closed by reading the log. The save carries `meditation.short: 2`.

⚠ **But the ceiling itself does not persist.** Immediately after the reload
the pool read `force 183 of 183` — a ceiling degraded to 165 came back at
its true maximum, and `b` then answered `there is nothing to restore`. So a
reload restores a degraded ceiling for free while the meditations spent
against it stay spent. The log-derived fact survives and the runtime pool
does not. Reporting the asymmetry; whether the pool is meant to be
session-scoped is not mine to rule.

## 3. Long meditation — the refusal names both keys, and the night is whole

```
n  (no side chosen) → you have not chosen a side · l to walk the light · k to walk the dark
l                   → you set yourself to walk the light · n to meditate the night
n                   → you meditate the night · ceiling 178 → 183 · Force 183 of 183 · you have not healed
```

* The refusal is clean and **names both options** rather than meditating to
  no effect — `PT-2277`'s rule, applied.
* The ceiling is restored **in full** to the true maximum, and the pool with
  it.
* `you have not healed` — no vitality.

The alignment shift it grants is written to the log (`meditation.long
{side: light}`) and is not visible anywhere, per below.

## 4 and 5. Alignment — not observable in play

**There is no readout.** `alignmentFrom` is never called by the app; no
screen shows a score or a band name. So "cast a dark power and confirm your
alignment score moves" cannot be done through the product as it stands.

What exists and is correct is everything either side of the missing display.

**The app writes the right inputs.** Decoded from the real save after real
play:

```
power.cast  {power: force_scream,        tier: 1, side: dark}
power.cast  {power: force_lightning,     tier: 2, side: dark}
power.cast  {power: master_force_scream, tier: 3, side: dark}
encounter.ended {...}                      session.started {}
meditation.long {side: light}              time.advanced {days: 1}
character.side-chosen ×1                   meditation.short ×2
```

Side and tier are carried per cast, light powers are marked `light`, and the
encounter and day boundaries the fold needs are all present.

**And the production fold gives the right answer over that real log** —
`alignmentFrom(log, wisdomModifier: 2)` returns **score 51, band Neutral**,
which reconstructs exactly: 50, minus 2 for the session's drift (tier 3's 4,
less 1 for being in Neutral, less 1 Wisdom resistance) to 48, plus the quiet
window's passive recovery capped at 50, plus 1 for the light night.

**The four claims, exercised against the production functions.** Not in
play, and labelled as such:

| claim | reading |
|---|---|
| highest tier once per encounter | one tier-3 cast → **47**; t1+t2+t3 in ONE fight → **47**; t3 in TWO fights → 44 |
| resistance never fully cancels | wisdom +0/+2/+4/+8 → drift **1, 1, 1, 1** — at +4 the resistance (2) exceeds the raw drift (1) and the floor still yields 1 |
| band flips away from Neutral immediately | falling into Committed Dark at **28** → Committed Dark |
| returning needs overshoot | climbing out at 29 and 30 → still Committed Dark; at **31** → Leaning Dark. Rising into Deep Light at **86** → Deep Light; falling out at 84 and 85 → still Deep Light; at **83** → Committed Light |
| meditation cannot cross away from Neutral | a dark night at 30 → 29; at 29 → **29**, stopped at the band edge; a light night at 29 → 30, toward Neutral, free |

That is item 5's asymmetry exactly, on the document's own four numbers.

## What would make 4 and 5 testable in play

One readout. A band name and score on the character sheet — the sheet
already has an `info` section carrying Species — would turn every row of
that table into something a player and a tester can see. Until then the
system is complete at both ends and invisible in the middle.

## Fixture

`tester-rest` on the shelf, named `0 Rest Bench (Tester)` so the carousel can
reach it. One mark to cast at, and a 161-damage mine sized against a measured
162 maximum. ⚠ Force Valor is the ceiling-degrading tool because it is
ally-aimed and so can be cast with no fight running, which is what allows a
rest or a meditation in the same sitting — the rest and meditation verbs all
refuse mid-fight.
