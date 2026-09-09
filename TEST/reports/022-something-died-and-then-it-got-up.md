# 022 · Something died, and then it got up

**From `Tester`. Unrequested number.** `PT-1512` followed.

**Built 19:26 from:**

    Lodestar 3ae6f0e · Lens 9ca5982 · Loom a6c6ceb · app bd47c4c

**Pins honest.** 1280×720.

---

## ⚠⚠ FOR THE FIRST TIME IN THIS PROJECT, SOMETHING DIED

**`character.died` exists in a save file. Six of them, all for
`probe-sentinel.probe-room.04`, and the deepest blow left it at `vitality: -12`
against `con = 10`.**

**How I built the fight you asked for**, since none of my characters could:

- **`attack`, `damageModifiers` and `defence` are all hardcoded** in
  `play_screen.dart` (`Term('attack', 1)`, `const []`, `defence: 10`). **So
  Strength buys no damage and Dexterity buys no defence.** The only ability that
  changes a fight is **Constitution**, through vitality.
- **So the lever was a weapon**, and `tester-probe` had no items — which is why
  every character there punches for `1d3`.
- **I authored one.** `NewItemDialog` is reachable now and **it reads the rules
  file**: its base-type list is populated from `base-rules/rules/equipment.toml`
  — the exact thing `BUILD 67` said `Loom` could not do. I made
  `items/weapons/blaster-rifle` on base `blaster-rifle`, **`1d12`**.
- **Then a Gamorrean Soldier, `CON 18` → 14 vitality, named Grave Digger.**

**And the producer picked the item up.** My own attack line:

> `probe-sentinel.probe-room.04 falls — **Blaster Rifle** · rolled 12 — d20 11 +
> attack 1 · needed 10 — hit · 3 damage · −3 left`

**⚠ THAT ANSWERS `PT-1480`'s AIM, which has been open since `014`.** An artifact
authored in Loom — an item, on a base type read out of the rules — reached the
play client, was equipped by the equipment producer through the path the class
array names, and **named itself in a strike.** End to end, author to blow.

---

## ⚠⚠ AND THEN IT GOT UP. THE DEATH IS UNDONE BY THE NEXT EVENT

**The log, in order, for `probe-sentinel.probe-room.04` in `grave-digger.sav`:**

    encounter.ended   0
    character.revived
    encounter.ended   0
    character.revived
    encounter.ended  -12
    character.died          ← it died
    encounter.ended   0
    character.revived       ← ⚠ revived, after dying
    encounter.ended   0
    character.revived       ← again
    encounter.ended   0
    character.revived       ← again

**`character.revived` is written for an enemy that `character.died` has already
been written for.** Three times.

**⚠ `PT-1515`'s own comment forbids exactly this pair and predicts exactly this
consequence** — `play_state.dart`:

> ⚠⚠ AND NOT AFTER A DEATH — `PT-1515`. A `revived` reaching a dead subject
> would undo the death silently, which is the exact shape of the defect this
> ruling closes. **Order does not save us**: the writer emits one or the other,
> **and this refuses the pair anyway, because a projection that depends on a
> producer being careful is a projection with a rule it does not enforce.**

**The projection was right to defend itself. The producer is emitting the pair.**

**⚠ And the guard reads as though it should not.** `play_screen.dart:1249` is
`if (c.vitality.current <= 0 && c.role != Role.enemy)`, and
`attack.dart:221` builds every placed creature with `role: Role.enemy`. **I did
not isolate why the guard does not hold** — I am reporting the log, which is not
ambiguous.

### ⚠ And six deaths for one creature

`PT-1421` is *one crossing, one event*. **`character.died` was written six times
for the same subject.** Every fight after the first death crossed the threshold
again, because the revive had put it back.

---

## ⚠⚠ SO THE VACATED SQUARE STILL DOES NOT EXIST — FOR A NEW REASON

**At `019` nothing could die. At `021` I could not kill anything. Now something
dies and the square is still occupied.**

**After a full quit and `Continue`:**

- The working line reads **`probe-sentinel.probe-room.04: 0 of 8 — in your
  campaign, a01-probe-room left you at 0`**. **Not dead. Zero.**
- **The creature is still drawn** on `4,3`, as a hollow marker, on the wall
  square I painted under it.
- **It is still an occupant.** I walked into it and a fresh fight rolled
  initiative — `probe-sentinel.probe-room.04 8 · Grave Digger 5`.

**So of the claims you named, on this build:**

| claim | result |
|---|---|
| `character.died` is written | **yes** — six times |
| it survives a quit | **no** — the revive after it wins, and the reload reads `0 of 8` |
| the marker goes | **no** — still drawn |
| `_occupant` releases | **no** — still starts fights |
| a dead creature leaves nothing | **untestable** — nothing stays dead long enough to leave anything |

**⚠ AND THE WALL-UNDER-A-CREATURE QUESTION IS STILL UNANSWERED, SINCE `018`** —
for the third distinct reason. The wall is painted, the creature standing on it
has now genuinely died, and **the square still never empties.**

---

## ⚠ A REFUSAL RENDERED WHERE THE BUTTON ISN'T

**My new status-bar step caught this rather than a retraction.**

Pressing `Create` in `NEW ITEM` with the prefilled path `items/weapons/`
appeared to do nothing — no file, nothing in the status bar. **The refusal
exists**:

> An item needs a path — where it lives IS what it is.

**It is rendered as the last element of the dialog's `body`, after the
description field, below a list of about forty base types. `Create` is in
`actions:` and is pinned.** So you press a pinned button at the bottom of the
frame and the reason appears at the bottom of a **scrolled region you are not
looking at** — I had to scroll down twenty-five notches to find it.

**⚠ Same family as `PT-1501`**: computed, rendered, and out of view. There it
was truncation; here it is scroll position. **The path prefill is itself
invalid** (`_problem()` refuses a path ending in `/`), so **the dialog opens in
a state that will refuse, and says so somewhere you cannot see.**

---

## ⚠ SCOPED NEGATIVES

- **I did not isolate why the `role != Role.enemy` guard does not hold.** The
  log is the evidence; the cause is not mine.
- **I did not test whether the death holds WITHIN a session** — only across a
  quit. It may be correct until the revive lands.
- **One creature, one Constitution (10), one weapon (`1d12`).** No other
  threshold tested.
- **I did not fight the bed's trooper with Grave Digger**, so everything here is
  from `tester-probe`.
- **`character.downed` is declared and I never looked for it** in a log.
- **The wall under the creature is restored**; I never observed an empty square,
  so a body, a drop, or a marker on one remain untested by anyone.
- **I did not re-check `listFor`** against `021`'s open question.
- **Not touched:** the eight inert blueprint kinds, other window sizes, BG3.

---

## What this run changed

**Packages: one addition, deliberate** —
`tester-probe/blueprints/items/weapons/blaster-rifle.toml`, authored through
Loom. **The test wall was painted and removed; `diff -r` shows nothing else.**

**Saves: one new** — `grave-digger.sav`, format 02. **Eighteen saves now.**
Nothing was deleted.
