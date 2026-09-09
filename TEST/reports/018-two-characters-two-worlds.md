# 018 · Two characters, two worlds

**From `Tester`. Unrequested number.**

**Built 17:22 from:**

    Lodestar 7fc7620 · Lens 9ca5982 · Loom cc9dc60 · app 776f088

**Pins honest** — both locks resolve `lodestar` to `7fc7620`, which is `HEAD`.
**1280×720.** `tester-probe` was backed up before anything and is restored
**IDENTICAL**; every breakage was reversed.

**⚠ ONE CONTAMINATION, DECLARED.** Mid-run the owner was using the app on the
same machine, which rewrote `probe-walker.sav` and left a game mid-conversation.
**My first `Continue` observation was theirs, not the app's**, and I nearly
recorded *"Continue picked the older save"* as a finding. I restored the saves
from my own backup, re-ran the test in isolation, and **the real answer is the
opposite** — below. **Two agents share one data folder, and this is the second
time that has bitten** (`BUILD 38`/`39` was the first).

---

## ⚠⚠ THE HEADLINE — TWO CHARACTERS IN ONE PACKAGE HAVE SEPARATE WORLDS

**`PT-1427` makes an encounter outcome campaign-lifetime. It is per-CHARACTER,
and nothing anywhere says so.**

**Demonstrated with numbers, on one creature, across two characters:**

| when | who | `probe-sentinel.probe-room.04` |
|---|---|---|
| report `016` | **Probe Walker** fought it and walked out | **left at 3 of 8** |
| today, first sight | **Yard Tester** walks into the same tag | **8 of 8 — whole** |
| today | Yard Tester fights it and leaves | **left at 2 of 8** |
| today, after quit + `Continue` | Yard Tester returns | **2 of 8 — its own wound kept** |

**The same tagged creature is at 3 for one character and 2 for the other, in the
same package, at the same time.** Persistence works perfectly; it is **scoped to
the character**.

**Why, and it is structural rather than a slip:** an outcome is written into the
**character's own log** (`_writeOutcome` → `_log` → that character's `.sav`), and
`SAVE-LOAD-01 §5·0` / `PT-1416` make a save **one file per character**. A second
character replays only its own log, so it **cannot** see the first's outcomes.
**There is no code that would need to be wrong for this to happen** — it falls
out of the format.

**⚠ WHAT IS NEXT TO IT, AND IS THE ACTUAL PROBLEM:** the app's own words imply
the opposite. The line a player reads is *"encounter a01-probe-room **left you
at 3**"* — phrased about the room, not about them. A player who makes a second
character walks into a creature they personally beat to 3 vitality and finds it
untouched, **with no explanation offered anywhere**: not on the hub, not on
`Load Game`, not on arrival.

**⚠ I am not calling this a defect.** It is the ruling's unstated half, and you
said nobody has decided it. **The decision is: is a package a WORLD that
characters visit, or a MODULE each character plays their own copy of?** Today it
is the second, by construction, and only the file format says so.

---

## ⚠ `Load Game` AND `Continue` WITH TWO SAVES — `PT-1416`'s OWN CASE, RUN AT LAST

**`Continue` is right.** With `yard-tester.sav` at 15:53 and
`probe-walker.sav` at 15:39, `Continue` opened **Yard Tester**, at the entry
area. `mostRecentHandle` asks the disk for `modified` and the disk answers —
`PT-1416`'s *"which save is most recent is not a fact about the save, it is a
fact about the disk"* holds in practice.

**`Load Game` lists both, and they ARE distinguishable** — this closes request
`001`'s open question for the two-character case:

    probe-walker.sav                        rules 0.1.0
    yard-tester.sav                         rules 0.1.0

**Because `PT-1416` names the file for the character**, the id is the label, and
two saves no longer look identical. **That was the sharpest thing `PT-1443`
found and it is answered by the naming rule rather than by a header field.**

**⚠ Two things it still does not do, and I am reporting them as observations:**

- **The order is not recency.** `probe-walker` is older and listed first;
  `Continue` would take `yard-tester`. **With two saves I cannot tell whether
  the list is alphabetical or directory order** — only that it is not the order
  `Continue` uses. **The screen that offers a choice and the button that makes
  one disagree about which is first.**
- **The only distinguishing field is the id.** Both rows read `rules 0.1.0`.
  No level, no class, no where, no when. **A player with two Soldiers named
  similarly gets no more than the filename.**

---

## ⚠ THE NINE STEPS TO A WALL CANNOT HAPPEN — `017`'s F2 IS FIXED, AND BETTER

**I could not reach chargen at all.** All three entry failures are now refused
**at the hub**, with `Continue`, `New Game` and `Load Game` **all greyed**, and
**three different, accurate sentences**:

| what I broke | what the hub says |
|---|---|
| `[entry]` names an area not in the manifest | *this package begins in "a09-nowhere", **which it does not list among its areas** — so there is nowhere to start* |
| entry listed, **file removed** | *this package begins in "a01-probe-room" **and that area is missing** — so there is nowhere to start* |
| entry listed, present, **corrupt TOML** | *this package begins in "a01-probe-room" **and that area cannot be read** — so there is nowhere to start* |

**⚠ The guard is no longer a null test**, and it distinguishes three causes that
`017` saw collapse into one. **A player never builds a character against a
package that cannot start it.**

**⚠ AND `017`'s F5 IS FIXED IN THE SAME PLACE.** The raw
*"TOML parse error: end of input expected at 40:1"* does not reach this screen —
it says **"cannot be read"** in the same voice as everything else. The parse
detail belongs to the author, and it stayed with the author.

**⚠ `017`'s F3 IS ALSO CLOSED.** Verify went 4 → 3: the duplicated at-rest
equipment fault, and its false *"It is authored and has never been placed"*
clause, are both gone. The dead reference is reported **once**, by the
placement. **⚠ Whether the at-rest check still fires for a blueprint that is
genuinely never placed is untested by me** — I did not author one to find out.

---

## ⚠ A WALL UNDER A CREATURE — TODAY IT IS NOTHING, AND IT IS A LATENT TRAP

**Asked whether it is nothing or very bad. It is nothing, and here is exactly
why, and what would change that.**

**I painted a wall on `4,3`, the square `probe-sentinel.probe-room.04` stands
on.**

- **Loom wrote it without comment.** The map is `....#.` on row 3.
- **Verify does not flag it.** Still 3 problems. **There is no
  `PackageProblem` for a creature on an impassable tile.**
- **Loom draws the creature on top of the wall**; the app draws it **inside**
  it — a red combatant in a dark mass. Odd, but legible, and arguably honest.
- **The creature is completely unaffected.** I walked into it and the fight
  started normally; it hit me, I hit it, it took me to −1.

**Why it does not matter today:** `play_screen.dart` tests **occupancy before
passability** — an occupied square is talked to or struck and the handler
returns, so `passable` is never consulted while something is standing there.
**The wall changes nothing about reaching the creature.**

**⚠ Why it is a trap in waiting:** the moment the creature is gone, the square
is impassable again. **Anything left on it becomes unreachable** — a body, a
drop, a container. Nothing is dropped today, so nothing is lost today. **The
day `INVENTORY-01` puts something on the floor, an author who painted a wall
under a creature has made an item that cannot be picked up, and neither program
will say a word.**

**I am filing it as that: not a defect, a named future one.**

---

## ⚠ SCOPED NEGATIVES

- **Two characters in ONE package only** (`tester-probe`). I did not make a
  second character in `endar-spire` and check the trooper, which is the case
  with shipped content and someone else's fixture.
- **Two saves, not three.** Ordering claims rest on two rows; I cannot separate
  alphabetical from directory order.
- **I did not test `Load Game` picking the OLDER save and then playing it** —
  I loaded via `Continue` throughout after the ordering check.
- **I did not delete a save**, or test what `Continue` does when the most recent
  file is corrupt.
- **I never reached chargen against a broken package**, because the hub refuses
  — so **whether the nine steps would survive a mid-way break is still
  untested**, and now unreachable by this route.
- **The wall-under-creature test used one creature, one wall, one square.** I
  did not paint **water** under a creature (impassable but sight-passable), did
  not wall in a creature on all four sides, and **did not check what a wall
  under a creature does to line of sight** — `wall.blocksSight` is true and I
  tested nothing that reads it.
- **I did not kill the wall-standing creature** — it survived at 1 — so
  **the vacated-wall-square case is unobserved**; the trap above is reasoned
  from `passable`, not watched.
- **`items` has a `+` now and I still have not opened it.**
- **Not touched:** the eight inert blueprint kinds, other window sizes.
- **⚠ And the owner was using the app during part of this run.** Everything
  above was re-run in isolation afterwards, but that is why the saves folder
  shows my restores rather than a clean history.

---

## What `tester-probe` is now

**Unchanged from `017` except its two saves.** Four areas, three doorways, the
painted yard, the 64×2 strip, five placements — two still unresolving on
purpose and saying so — a gate that never rolls, a doctrine nothing lists, a
warden with a blaster that does not exist.

**And two characters who do not share a world:** `Probe Walker`, who left a
sentinel at 3, and `Yard Tester`, who left the same sentinel at 2, neither
aware of the other.

**I fixed nothing.** Every breakage was reversed and the package `diff`s clean
against the backup I took before starting.
