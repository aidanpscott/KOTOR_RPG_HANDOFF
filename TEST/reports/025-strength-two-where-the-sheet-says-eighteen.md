# 025 · Strength 2, where the sheet says 18

**From `Tester`. Unrequested number.** `PT-1512` followed.

**Built 21:40 from:**

    Lodestar 1f3e47a · Lens 9ca5982 · Loom fc289e6 · app 645cab3

**Pins honest.** 1280×720.

---

## ⚠⚠ THE MELEE PROOF — `PT-1533` AS A WRONG NUMBER, NOT AN ABSENT TERM

**At `024` the gap showed as an omission: a ranged attack takes Dexterity, the
bought Dexterity was 10, the modifier was zero, and a zero term is not printed.
You said melee would make it show as a number. It does.**

**I authored `items/weapons/vibroblade` in Loom** (`NewItemDialog`, base
`vibroblade` read out of the rules) **and made a Gamorrean Duelist**, because
`duelist → Vibroblade` is one of only two class arrays whose first weapon is
melee. **Its character sheet at the end of chargen:**

    abilities   STR 18 · DEX 12 · CON 16 · INT 8 · WIS 14 · CHA 6

**Its first swing:**

> `Vibroblade · rolled 18 — d20 16 + attack 0 + **Strength 2** · needed 10 —
> hit · 10 damage · 50 left`

**`Strength 2`.**

**STR 18 is a +4 modifier. The fight used +2, which is STR 14 — the score I
bought, before the Gamorrean +4.** The sheet and the blow disagree by four
points of Strength, **and now the screen prints the wrong number instead of
hiding it.**

**Both discriminators were set up deliberately and both point the same way:**

| | bought | sheet | modifier used |
|---|---|---|---|
| Strength | 14 | **18** | **+2 — the bought one** |
| Dexterity | 14 | 12 | (defence, not isolated) |

**`ledger.dart:280` stores the event's raw `score` and nothing applies the
species adjustment on replay.** `024` inferred this; **this is the arithmetic on
screen.**

### ⚠ And a smaller thing beside it

**`+ attack 0` IS printed. A zero ability term is NOT.** The Duelist's base
attack bonus at level 1 is zero and the line shows it as a term anyway, while
`attackTerms` drops the ability at `if (ability.value != 0)`. **Two zeroes, two
different treatments, in one line.** The one that is shown is the one a player
can do nothing about; the one that is hidden is the one they spent points on.

---

## ⚠⚠ THE SPENT PIP NEVER RENDERS — AND IT IS NOT A CAPTURE PROBLEM

**Two reports old, and now closed with an explanation rather than another
negative.**

**The pip row does render spending. Move proves it** — I moved twice and
captured each frame:

    ◆ 10 move   →   ◆ 9 move   →   ◆ 8 move

**The action pip is the one that never goes grey.** I struck and captured three
frames back to back, as fast as the tooling allows:

    frame 0:  ◆ 8 move    ● action (bright)
    frame 1:  ◆ 10 move   ● action (bright)   ← strike line appears
    frame 2:  ◆ 10 move   ● action (bright)

**Move jumped 8 → 10 in the same frame the strike line appeared.** The budgets
had already reset.

**Why, and the code says it out loud:** `play_screen.dart` — *"⚠ RESOLVING THE
ACTION ENDS THE TURN — §1"*. The strike spends the action, ends the turn, runs
the enemy's turn and begins a new round **inside one keypress**. **The spent
state exists between two statements and never reaches a frame.**

**⚠ So `PT-1517`'s *"a spent pip goes grey with its shape intact"* is unobservable
for the action pip as the turn flow stands.** I now have it from three fights,
including a 60-vitality one built specifically so the fight would not end.

---

## ⚠⚠ THE CORPSE IS STILL AN OCCUPANT — `023`'s F2 REPRODUCED ON THIS BUILD

**At `024` I would not claim it fixed. It is not.**

**`probe-anvil.probe-slit.01`, its whole history in `blade-tester.sav`:**

    encounter.ended  -2
    character.died
    encounter.ended  -6
    character.died
    encounter.ended   0
    character.died

**Three `character.died` for one creature. Zero revives.**

**And it happened in front of me**: the strike line read
`probe-anvil.probe-slit.01 falls — … −2 left · character.died`, and the very
next line was **`initiative — Blade Tester 19 · probe-anvil.probe-slit.01 3`**.
**I kept fighting it after it died, twice more.**

**`PT-1421` is one crossing, one event. This is one crossing and three events**,
and the third fires at **vitality 0** without a new crossing at all. **The revive
half is fixed and the duplicate-death half is not** — they had the same cause at
`022` and only one of them has been closed.

---

## ⚠ THE DICE ARE NOT SEEDED — THE `024` COINCIDENCE WAS A COINCIDENCE

**I flagged two identical strike lines at `024` and said I did not have enough
rolls. I have them now.**

**`d20` values observed this run**, across two characters and several separate
fights:

    1 · 2 · 9 · 10 · 10 · 12 · 14 · 16 · 16 · 16 · 18 · 18 · 19

**Thirteen values spanning the whole range, including a natural 1 and a 19, with
three 16s.** `PT-1013` makes the die injected and replayable by design, and
**nothing here suggests a fixed sequence.** Two identical lines out of that
spread is ordinary luck. **Withdrawn as a concern.**

---

## ⚠ THE TRIPLE PLACEMENT DOES NOT REPRODUCE — I AM NOT FILING IT

**You asked me to file it. I tried to reproduce it first and could not, so I am
not going to.**

**Counted rows before and after one deliberate, isolated click:**

    contents rows before palette click:  4
    after selecting the creature:        4
    after ONE grid click:                5

**One click, one placement.** The three stacked creatures at `024` came from my
own repeated clicks across three separate command blocks — I ran a palette-plus-
grid pair three times while trying to reach a different area's tab, and a missed
tab click leaves the previous area open. **The defect was mine, not Loom's, and
`024` implied otherwise. That is the correction.**

**⚠ Third time that checking before filing has stopped a false report** — the
doctrine dialog at `016`, the effect button at `020`, and this.

---

## Confirmations in passing

- **The item I authored reached play and named itself** — `Vibroblade` in my own
  strike line, equipped by the producer through the class array's path. **Second
  artifact after the blaster rifle.**
- **The palette lists both items** — `weapons/blaster-rifle`, `weapons/vibroblade`.
- **A creature authored with `override = 60`** got 60 vitality in play
  (`probe-anvil.probe-slit.01: 60 of 60`), so the vitality override works.
- **Verify stayed at 3** across a new item, a new creature and three placements.
- **`a04-probe-slit` now shows `set as entry`** in the module tree — an
  affordance I had not seen before and did not use.

---

## ⚠ SCOPED NEGATIVES

- **I did not isolate the Dexterity half.** Defence is now `10 + Dex + class +
  grants`, and bought DEX 14 versus sheet 12 would differ by one — **but no
  screen shows my defence**, so I could not read it. **The Strength proof stands
  alone.**
- **One species with an adjustment, one class, one weapon.** A species with no
  adjustment would show no discrepancy, which is why this survived so long.
- **I did not check whether the creature blueprint's abilities suffer the same
  gap** — a blueprint has no species step, so probably not, but I did not test.
- **The spent-pip finding is about the ACTION pip only.** `gear` and `reaction`
  I still have never seen change state at all.
- **I never saw five budget rows** — no class I have played grants a bonus.
- **The corpse re-engagement was in one area, one creature.**
- **Not touched:** the eight inert blueprint kinds, other window sizes, BG3.

---

## What this run changed

**Packages — four deliberate additions, all authored through Loom:**
`blueprints/items/weapons/vibroblade.toml`,
`blueprints/characters/probe-anvil.toml`, one placement in `a01-probe-room`
(`probe-sentinel.probe-room.08`, from the click test) and one in
`a04-probe-slit` (`probe-anvil.probe-slit.01`, now dead).

**Saves — one new**, `blade-tester.sav`. **Nineteen saves. Nothing deleted.**
