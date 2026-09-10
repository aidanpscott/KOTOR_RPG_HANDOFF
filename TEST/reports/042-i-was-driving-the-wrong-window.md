# 042 · I was driving the wrong window — and the standard half, seen at last

**From `Tester`. Unrequested number.** `PT-1512` and `PT-1617` followed;
`BK18/`, `SV-T041/`.

**⚠⚠ BUILT AND MEASURED AGAINST — pins read from the commits I BUILT:**

    Loom 802dec5  →  Lodestar 9aa7382      bundle built 15:59
    app  660134a  →  Lodestar 9aa7382      built 16:07

**⚠ Both pin `9aa7382`, which carries `PT-1622`'s clamp** — so this is the first
build in which the clamp exists. **I did not re-run the healing bug it fixes:
`PT-1623`.**

---

# ⚠⚠ 0 · I WAS DRIVING A WINDOW I DID NOT LAUNCH, AND I HAVE BEEN KILLING CODER'S PROGRAMS

**This is the finding of the run and it is about my own instrument.**

**`pgrep -af "bundle/loom"` returned a Loom launched by session
`e6c77742-…` — not mine (`3eb88090-…`) — whose scratchpad dates from
2026-09-08 and was active at 16:01:47.** ⚠ **That is Coder, running the same
programs on the same X display, and has been for two days.**

    xdotool search --pid <my pid>   →  exactly MY two windows
    xdotool search --class loom     →  ⚠⚠ FOUR windows

**⚠⚠ I HAVE BEEN USING `xdotool search --class loom | tail -1` ALL THREAD. That
picks the last window on the display, not mine.** At 16:02 I captured a "Choose
Directory" dialog with rows already selected that I had not clicked — **it was
Coder's**, and my own Loom had exited without my noticing.

**⚠⚠ AND WORSE: `pkill -f "bundle/loom"` AND `pkill -f kotor_rpg_app` MATCH
THEIR PROCESSES.** I have issued those repeatedly. **I have been killing
Coder's running programs.**

**✅ Fixed, and verified in this run:**

    nohup …/bundle/loom > log 2>&1 &   MYPID=$!
    xdotool search --pid $MYPID        # exactly mine
    kill $MYPID                        # only mine — never pkill -f

**After `kill $MYPID`: three other Looms still running, untouched. After the
app: one other still running.** ⚠ **It is in my notes now, and it is
`PT-1617`'s principle extended — the display and the process table are shared
too.**

---

# ⚠⚠ 1 · AND IT INVALIDATES A CLAIM I MADE IN `041`. THE LEFT PANE DOES COLLAPSE

**`041 §2` said *"the left pane does NOT collapse on open"*. ⚠ THAT WAS WRONG.**
On a window verified mine by PID, opening `tester-probe` gives:

    ▼ areas                    +
      ▸ a01-probe-room  entry
      ▸ a02-probe-hall
      ▸ a03-probe-yard         ⚠ RED, with its fault inline
      ▸ a04-probe-slit         ⚠ RED, with its fault inline
    ▼ conversations            +
      ▸ sentinel-challenge
      ▸ wizard-doc

**✅ Areas and conversations only, every area COLLAPSED, no `blueprints`
section.** And the right pane reads **`pick a kind`** with no contents until one
is chosen. **Both halves of the ruling hold.**

> **⚠ I reported the opposite because I was looking at a window I had not
> opened. The claim is withdrawn.**

---

# ✅ 2 · THE STANDARD HALF — FOUR REPORTS SAID I HAD NEVER SEEN IT. HERE IT IS

**`items` → `standard`:**

    standard   custom
      30 base types — what a custom item is MADE FROM, not something you place
      Blaster Carbine · Blaster Pistol · Blaster Rifle · Bowcaster ·
      Disruptor Pistol · Disruptor Rifle · Double-Bladed Lightsaber ·
      Double-Bladed Sword · Gaffi Stick · …

**✅ `PT-1566`'s exception, in the palette's own words.** The standard side of
`items` is the base types, **and the sentence says what the axis MEANS** rather
than just listing.

## ⚠⚠ And the other nine do not go quiet — they say WHY

**`sounds` → `custom`:**

> ⚠ *"cannot list — no folder is specified for this kind yet, so this list
> cannot be read — **it is not a count**"*

**`sounds` → `standard`:**

> *"`base-rules` ships `rules/` and no `blueprints/` at all, so there is no
> standard sounds — **absent rather than empty**"*

> **⚠⚠ `PT-1500`'s OWN PHRASE, ON BOTH AXES — and the standard one explains why
> `items` is the ONLY kind with a standard side at all: base-rules ships
> `rules/` and no `blueprints/`.** One sentence answers the whole question I have
> been circling for four reports.

**✅ And the rebuild kept the sentence where it is TRUE and removed it where it
was FALSE.** `doors` and `waypoints` now read *"a doorway, painted"* and *"an
arrival point, painted"* in the mode list — **the seven-sighting line is gone,
and the inert kinds kept theirs.** That is the finding closed properly rather
than deleted.

**✅ And the grammar slip from `040` is fixed:** *"**an** arrival point,
painted"*.

---

# ⚠⚠ 3 · A GAMORREAN FROM THE REBUILT PALETTE STILL SWINGS AT +2

**`PT-1597`'s chain, closed on one side and open on the other.**

**✅ The authoring half works.** `creatures` → `custom` → `+` → New creature,
`str = 14`, species **Gamorrean**, and the file:

    species    = "gamorrean"
    [abilities]
    str = 14

**Placed at `7,4` in `a03-probe-yard` as `probe-boar.probe-yard.06`, walked
into:**

    probe-boar.probe-yard.06: unarmed · rolled 21 — d20 16 + attack 1
      + ⚠⚠ Strength 2 + closed on a ranged weapon 2 · needed 13 · 1 square
      — hit · 3 damage

> **⚠⚠ `+ Strength 2`. A Gamorrean's `+4` makes a bought 14 an 18 and a modifier
> of `+4`. The species reaches the FILE and `combatantFrom` still never asks for
> it** — `round.dart`'s body carries no species term, only doc comments about
> speed. **`033 §4` unchanged, on a creature authored in the rebuilt palette.**

**✅ Two things I had not seen in an attack line before:
`+ closed on a ranged weapon 2` — `§6.2a`'s closing bonus, in the expression —
and `needed 13 · 1 square`, the reach printed beside the target number.**

---

# ⚠⚠ 4 · A HENCHMAN CANNOT BE AUTHORED, SO `down` IS NARROWER THAN `041` SAID

**You asked whether a henchman is the cheap way to make `downed` fire often.
⚠ There is no way to make one.**

    character_open.dart      ⚠ no `role` field on a blueprint AT ALL
    attack.dart:246          combatantFrom(…, role: Role.enemy)   ⚠ HARDCODED

**And the comment on that line is the answer in Coder's own words:** *"THE PARTY
IS THE PLAYER, TODAY. There are no companions yet… so everything from
`[[contents]]` is an enemy. **The day a placement can join the party, this line
is where that is decided.**"*

**`Role.henchman` occurs twice in any `lib/`:**

    pools.dart:79         partyStandsAtOne — READS it
    doctrine_open.dart:31 'henchman': Role.henchman — a TARGETING match key,
                          for "prefer targets whose role is henchman"

> **⚠⚠ NEITHER PRODUCES ONE. `Role.henchman` is readable in a doctrine's
> vocabulary and emitted by nothing, so `partyStandsAtOne`'s
> `normal && henchman` branch is unreachable in the product.**

**⚠ Which narrows `down` further than `041` did.** I said the producer was one
call site, one role, one exact value. **It is that because the wider band cannot
exist**: the only creature that could go down on any value ≤ 0 is a henchman,
and there are none. ⚠ **So there is no cheap way to make `downed` fire often,
and the once-in-six-cycles route is the only one.**

---

# 5 · Scoped negatives

- **⚠⚠ HOW MUCH OF THIS THREAD IS AFFECTED BY `§0` — I CANNOT SAY.** Every GUI
  observation I have reported since `TEST 026` used `--class … | tail -1`. **I
  know `041 §2` was wrong and I have corrected it; I have not re-verified the
  rest, and under `PT-1623` I do not intend to** — but the possibility is real
  and it is stated here rather than left implicit.
- **⚠ The `30 base types` count** is the palette's own. My earlier *"~40 base
  types"* in `016`/`028`/`031` was an eyeball estimate of a scrolling list.
  **I did not reconcile the two** and I am not asserting a discrepancy.
- **⚠ I checked `sounds` only** of the nine inert kinds. `encounters`,
  `placeables`, `stores` and `triggers` are the same family and I read none of
  them.
- **⚠ `probe-boar` was never fought to a conclusion** — one blow, one line. Its
  damage, vitality and death were not exercised.
- **⚠ `PT-1622`'s clamp is in this build and I did NOT test it** — `PT-1623`,
  and testing the fix was not on the brief. **`probe-feeble` is still `str = 1`
  in the bed and is the fixture for it.**
- **⚠ I did not paint terrain from the rebuilt palette this run** — only
  creatures. The disarm test in `041 §2` was on an unverified window and **is
  not re-confirmed here.**
- **Painting tiles with a TILESET** — still never.

## What I left behind — two fixtures

    blueprints/characters/probe-boar.toml     species = "gamorrean", str = 14
    a03-probe-yard  probe-boar.probe-yard.06  at 7,4   ⚠ tag_seq 6

**`probe-boar` is the POST-REBUILD control**: a Gamorrean authored through the
new palette rather than the old dialog, so the day `combatantFrom` reads a
species, `+4` can be checked against a creature that was made the current way.

**All 20 saves restored byte-identical. `diff -rq` against `BK18/` shows only
the two fixtures above.**

**Backups: `BK3/`–`BK18/`, `SV-T031/`–`SV-T041/`.**
