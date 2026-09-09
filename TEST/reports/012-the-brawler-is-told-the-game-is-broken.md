# 012 · The producer works — and the Brawler is told the game is broken

**From `Tester`. ⚠ NO REQUEST FILE — next free number.** App `2eea873` ·
`Lodestar b7e9198`; pin checked, `resolved-ref` = engine HEAD. Played.

---

## ✓ 1 · The attack line names a real weapon — the first time it ever has

**`Sero Kade`, Human Agent:**

    Hold-Out Blaster · rolled 17 — d20 16 + attack 1 · needed 10 — hit · 2 damage · 16 left

**And the save carries the reference, not a description:**

    character.equipment-set
      { "route": "standard", "credits": 100,
        "items": ["items/weapons/hold-out-blaster"],
        "weapon_r_1": "items/weapons/hold-out-blaster" }

⚠ **`items: []` is closed for new characters** — a path, in the trooper's own
shape. **`Ilyana Sorr` is still unarmed**, because her save predates the
producer: **an existing save does not gain a weapon, it has to be re-made.**
Worth knowing before anyone tests against an old one.

## ✓ 2 · `PT-1477` holds — the Agent is armed

`EQUIPMENT-01.md` now spells it without the hyphen (the ruling is in the file),
`base-rules` was regenerated at `12:15`, and **the Agent swings a Hold-Out
Blaster rather than a fist.** The four-classes-by-one-hyphen case is closed for
`Agent`. ⚠ **I did not build a `Medic`**, organic or droid — same array string,
untested by me.

**And a good new disclosure:** `Hold-Out Blaster: on-hit stun is not modelled`,
said on screen rather than silently dropped.

## ✓ 4 · The death sequence speaks, and both things I pushed on in `007` are closed

    YOU FALL. The fight ends and you stand at 1 — PT-559: anyone left down
    stands at 1 when combat ends.

and the status line, **in alert colour rather than dim grey**:

    Sero Kade: 1 of 9 — encounter a01-command-deck left you at -1 · revived at 1
    · you were struck down here

⚠ **The player's working line now shows OUTSIDE a fight.** That was the second
of the two open items — a dead character was previously indistinguishable from
a healthy one, and now it says *you were struck down here* and explains the
revive rather than announcing it retroactively mid-next-fight. **Both halves
land.**

---

## ⚠⚠ 3 · THE BRAWLER IS TOLD THE GAME IS BROKEN — and the record knows better

**You asked whether a Brawler reads sensibly. It reads as a data error, and the
save proves the app had the right answer in hand.**

**`Dax Roon`, Human Brawler. The record is correct:**

    character.equipment-set
      { "route": "standard", "credits": 100, "items": [],
        "unarmed": "the array names no weapon — this class starts with its hands" }

**That sentence is right, and it is well written.** `starting_weapon.dart:76`
produces it and `ledger_writer.dart:150` writes it.

**The screen says this instead:**

    Dax Roon: 11 of 11 · unarmed — your record carries no [equipment]:
    chargen records THAT you took the grant, not WHICH item

⚠⚠ **That is a bug report, shown to the one class for which unarmed is
correct.** It is wrong twice: it says the record is deficient when the record
is right, and it blames the grant, which has nothing to do with it.

**The mechanism, and it is one line:**

    play_screen.dart:756   a HARDCODED string, printed for every unarmed character
    play/*.dart            never reads the record's `unarmed` field at all

**The producer writes the reason and the play screen ignores it**, so every
legitimately-unarmed character gets the failure text. ⚠ **And `Dax Roon` hits
for 1 damage** — the same generic fixture as a broken unarmed — so nothing on
screen or in the numbers distinguishes *"his hands are the weapon"* from
*"your equipment is missing"*.

**Repro:** Human → **Brawler** → complete chargen → Play → walk into the
trooper → *"Stand aside."* → press `Down` and read the two lines.

### ⚠ And the Equipment screen never says it either

    weapon    NONE

**Raw, in shouting capitals, where every other class shows an item name.** The
app already owns the right idiom and uses it two rows below —
*"empty by design — implant · head · hands · arms · belt"* — and the weapon row
does not use it. The Brawler's `consumable` row even lists **Sparring Gloves**,
which is the game agreeing that the hands are the point.

---

## ⚠ Smaller, all new

**S1 · One item, two spellings, two screens.** The Equipment step shows
**`Hold Out Blaster`**; the attack line and the status line show
**`Hold-Out Blaster`**. `PT-1477` took the hyphen out of the data — `equipment.toml`,
`items.toml` and both array files all spell it without — and **the display puts
it back**, almost certainly by title-casing the path slug
`items/weapons/hold-out-blaster`. **The ruling removed one hyphen and the
renderer re-creates it one layer down.**

**S2 · A brand-new string carries a citation.** *"YOU FALL. The fight ends and
you stand at 1 — **PT-559**: anyone left down stands at 1 when combat ends."*
⚠ **Not the powers or species citations you told me not to re-file — this is a
new message, written this slice**, and the convention did not reach it.

**S3 · A bracketed field name reaches the player.** *"your record carries no
**[equipment]**"*. Whatever replaces the Brawler message should not carry that
either.

**S4 · ⚠ The grant's `item` is the whole §4a label, now persisted.** Taking the
melee upgrade as an **Agent** records:

    character.grant-resolved
      { "taken": "item",
        "item": "TAKES THE CLASS'S OWN melee UPGRADE FROM §4a —  Soldier → Long Sword
                 + Short Sword or a Double-Bladed Sword; Scout → Double-Bladed Sword;
                 Duelist → Vibrosword + Vibroblade",
        "kind": "upgrade" }

⚠ **The label is now inside the save as the item's name.** I checked: this file
contains **no `item_unresolved`, no `resref`, no `cost`.** ⚠ **Scoped:** you
described `item_unresolved` landing for **the Guardian** case, and **I tested an
Agent, not a Guardian** — so this may be a second path rather than a
contradiction. **Not re-filing `D3`**; what is new is that D3's text now
survives into the record.

---

## ⚠ Scoped negatives

**Built and fought this session:** `Sero Kade` (Human Agent) · `Dax Roon`
(Human Brawler). **Reloaded and fought:** `Ilyana Sorr`.

**NOT checked:**

- **`Medic`, organic or droid** — the other class in `PT-1477`'s four. Same
  array string as Agent, **untested**
- **The droid `Agent`** — I tested the organic only
- **A `Guardian` under the new producer** — so `item_unresolved` is unverified
  by me either way
- **The other three of the five that do not arm.** ⚠ I checked **one** — the
  Brawler's `NONE`. **I did not identify or visit the other four**
- **Whether `weapon_r_1` is read for anything but the attack line**
- **Any window size but 1280×720**

**Not re-filed, per your list:** powers cannot be cast, the droid gender
assertion, the §4a label itself. **`items: []` is closed and I am reporting it
closed, not re-filing it.**

**No exception, no overflow, nothing red.**

---

## Data

**Added `sero-kade.sav`** — ⚠ **the first save on this machine carrying a weapon
path**, and **`dax-roon.sav`** — ⚠ **the only one carrying the `unarmed`
sentence.** Both are worth keeping: they are the before-and-after for the
Brawler message, and `dax-roon` is the one that proves the record was right.

`Ilyana Sorr` has been through another death and now stands at 1 of 11 again.
Twelve saves. **I deleted nothing and fixed nothing.**
