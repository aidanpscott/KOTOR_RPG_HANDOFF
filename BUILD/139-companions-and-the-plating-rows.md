# BUILD 139 — companions, and the plating rows were never missing

---

## 1 · ⚠⚠ A SECOND COMBATANT ON THE PARTY'S SIDE — `PT-1735`

`combatantsIn` read `Role.enemy` and said, before any of this existed:

> *"THE PARTY IS THE PLAYER, TODAY… **the day a placement can join the party,
> this line is where that is decided**, and it is one line rather than a rule
> scattered through the fight."*

**It was one line.** `isParty` — `PT-1636` — is what the wipe rule, the
doctrine's sides, the roster and `§10`'s opportunity attacks **all already
ask**, so a companion reaches every one of them **without any of them being
told that companions exist.**

### ⚠ The role is the PLACEMENT's, not the blueprint's

A blueprint is a **template** — `§4`, *"template and instance"* — and the same
guard can be an ally in one room and a hostile in the next. `PT-1515` put the
decision at the placement for that reason and this is the field it was waiting
for.

**⚠ THE VOCABULARY IS `roleNames`, WHICH A DOCTRINE ALREADY USED.** It became
shared the moment a second program needed it, which is exactly the
`kindFromSection` move at `PT-1713`. `enemy` is deliberately absent from it: a
doctrine matching *enemy* matches everything it fights, and a placement is an
enemy by **default**.

**⚠ AN UNKNOWN ROLE IS AN ERROR, NOT AN ENEMY.** A misspelling is an author who
believes they placed an ally, and defaulting it puts a friend on the wrong side
**silently**. `role = "player"` gets its own sentence — the player is not placed
by an area, they arrive in it.

### ⚠⚠ `PT-1683` FINALLY HAS A SECOND PARTY MEMBER TO BE RIGHT ABOUT

`PT-1636` said: *"build it as a fact about the party, not about the character —
**it will be wrong the day a companion exists otherwise**."* Until now there was
no way to make a second party member, so **the distinction was untestable and
the rule was taken on trust.** It is asserted now: the player going down is not
a wipe while the companion stands, and both down is.

### ⚠ You do not walk into somebody on your own side

Every branch there is *talk to it* or *fight it*, and neither is what a player
means by pressing toward the person fighting beside them.

**⚠⚠ REFUSED RATHER THAN SWAPPED, AND THE CORPUS DECIDES IT.** Nothing rules
moving through an ally directly — but `BEASTS-ATTACKS-01`'s `Underfoot` is a
**FEAT** granting *"it may move through any square occupied by a creature larger
than itself"*, and **a feat that granted something already free would be worth
nothing.** So the default is that an occupied square is not walked through, and
swapping would quietly contradict something somebody paid for.

**⚠ AND IT DOES NOT STRAND ANYONE THE WAY A WALL DOES** — `PT-1638`. A companion
**moves on its own turn** and `PT-1707`'s diagonals reach past it; a wall does
neither.

### ⚠⚠ AND LOOM'S OWN RATCHET CAUGHT THE HALF I HAD NOT DONE

I added `role` to the reader, ran Loom's suite, and `loom_can_write_test`
failed with `area_open.dart: role` **before any control existed** — *"anything
the Builder cannot write, the Builder eventually destroys."* **A companion the
engine can read and the Builder cannot place is a format only a text editor can
author.**

The picker **reverses `roleNames`** rather than listing the words again, and
`enemy` writes **null** so the line goes — the rule `hidden` and `range` already
follow, and the reason no area on any shelf diffs on a default it already had.
The round trip is **proved** rather than declared; the ratchet only checks the
list.

## 2 · ⚠⚠ `PT-1734` — THE PLATING ROWS WERE NEVER MISSING

`PT-1734` queued this because a courier reported six numbers and the router
could not reproduce them: *"the tab-delimited copy… is truncated… the fuller
`k1_baseitems.2da` has no field delimiters I could parse."*

**Both obstacles are the wrong file or the wrong reader.**
`data/2da/k1/k1_baseitems.2da` is a **TSV export** beginning `row⇥name⇥`; the
parseable originals are the **binary `2DA V2.b`** files beside it, and
`scripts/parse2da.py` has read them all along:

    data/2da/k1/baseitems.2da       92 rows · 61 columns
    data/2da/k2/k2_baseitems.2da   104 rows · 61 columns

**Ninety-two rows, so 66–68 were never past the end.**

| Plating | Row | `baseac` | K1 `dexbonus` | K2 `dexbonus` |
|---|---|---|---|---|
| `Droid_Light_Plating` | 66 | **3** | 6 | **−1** |
| `Droid_Medium_Plating` | 67 | **4** | 3 | **−1** |
| `Droid_Heavy_Plating` | 68 | **9** | 1 | **1** |

**⚠ THE SUMS CONFIRM IT INDEPENDENTLY.** `§223` attested *"9, 7 and 10"* before
the rows were readable, and K1's columns add to exactly that — **the figure that
was attested and the figures that were guessed now come from the same rows.**

**⚠⚠ THE PLACEHOLDER WAS WRONG IN BOTH DIRECTIONS.** It read a smooth
`+4 / +6 / +8`; the real ladder is `+3 / +4 / +9`. **Medium is two lower and
Heavy one higher**, and the jump sits at the medium/heavy boundary — which is
`§199`'s own sentence appearing in the data. **Every droid Defence in
`PREGENS-01` computed from the old table moves.**

**⚠ WHAT IS STILL NOT CONFIRMED IS AUTHOR'S SIX NUMBERS THEMSELVES.** Its report
is not in `HANDOFF/` and `PT-1734` records the claim rather than the values, so
**I could not compare its list to mine.** What is confirmed is the ground truth
and the consistency check the claim rested on.

## 3 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| the seam goes back to hardcoding `Role.enemy` | 2 |
| walking into an ally fights it again | 1 |
| the refusal catches enemies too | 1 |

## 4 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 619 | **625** |
| `Loom` | 258 | **261** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 497 | **503** |
| | 1,384 | **1,399** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing. `check_engine_pin`:
4 pins level. `flutter build linux --debug` ✓.

**⚠ `whole_loop_test` FLAKED ONCE MORE**, failed in the full suite and passed
alone **both with and without my changes**, then passed the full suite on
re-run. **Second sighting of the same class** — the file reads the shared real
shelf, which now holds nine packages and grows while a run is in flight. Named
rather than chased.

## 5 · ⚠ Companions — what is NOT done

- **Nothing recruits.** A companion is placed by an author and is in the party
  from the moment the area opens. `§5`'s *"a companion is authored, and the log
  applies to it from the moment it joins"* has no **joining** yet.
- **Nothing switches control.** The companion is driven by the doctrine, which
  is what makes the slice work at all — and a player cannot take its turn.
- **It does not travel.** Walk through a door and the companion stays in the
  room, because `[[contents]]` is an area's and nothing carries a party across
  one.
- **`§10`'s enemy-side trigger is now reachable** — `BUILD 132` named it as
  waiting for exactly this — and **nothing has driven it yet.** Worth a `TEST`
  pass: an enemy walking past a companion to reach the player.
