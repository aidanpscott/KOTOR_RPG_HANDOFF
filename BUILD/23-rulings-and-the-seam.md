# 23 · Three rulings, and the seam

**`Lodestar` `3edf2b7` · `KOTOR-RPG-APP` `ae4a87f`.** 186 Lodestar tests, 187
app tests, analyze clean.

---

## 1 · The three rulings

| | |
|---|---|
| **Clamp both** | A maximum you can exceed is not a maximum. Vitality clamps at `max`; the Force pool clamps at the **working ceiling**, not the true one — *"you cannot rest off exhaustion"* and **a heal cannot either**. `restore()` is the named door for that |
| **Two doors, one boundary** | Negative damage still heals and still produces `character.revived`; **`heal()` is named** because one function doing two things with only one of them named is how a caller heals by accident. A test asserts the two doors give identical results |
| **`PT-1422`** | A tie breaks on **Dexterity**, then on **tag**, and **never on a roll** — *"no re-rolls settles it: a tiebreak roll IS a re-roll"* |

**⚠ The stable sort by declaration order is gone**, and the test proves it by
building the same encounter **both ways round** and getting the same order. A
third test asserts **no third die was drawn**.

> **And it closed the targeting tie with it**, because a targeting tie takes
> the first in initiative order. **Four open behaviours became one.**

---

## 2 · The seam — and the vitality formula was already ruled

`combatantFrom` takes `AUTHORED-CHARACTER-01 §2a`'s file and produces what the
round needs.

**⚠ No new behaviour was required**, because `PT-648` had already ruled it in
`CLASS-TABLES-BASE`:

    LEVEL 1     the MAXIMUM of the hit die, plus the Constitution modifier
    EACH LEVEL  the die's AVERAGE ROUNDED UP, plus the modifier
                d12 → 7 · d10 → 6 · d8 → 5 · d6 → 4

> *"Nothing is rolled. A character's vitality is the same at level 12 whoever
> plays them."* A Sith Trooper is **25**, every time. `PT-559` makes it
> load-bearing: *"the only thing standing between a character and the dying
> track."*

**⚠ And what the blueprint does not carry is asked for rather than invented.**
`§2a`'s file has **no speed field** — a beast entry has one and a character has
not — and no base attack bonus and no reaction tier. **Speed is a required
argument; the reaction pool defaults to none**, which is the honest answer.

### App side

`lib/play/attack.dart` reads an area's `[[contents]]`, opens the blueprint each
placement names, and strikes. **The line a player reads is the derivation:**

    rolled 17 — d20 13 + attack 4 · needed 14 — hit · 17 left

- **Anything that is not a character is skipped, not refused.**
  `PACKAGE-FORMAT-01` has nine blueprint categories and this reads one.
- **Killing something carries what it owes the ledger** rather than dropping
  it. Nothing writes it — the play screen is not a campaign — and
  `character.died` comes back on the report.

---

## ⚠ 3 · WHAT STOPPED — the test bed has nothing in it

**`Endar Spire` is two areas, a door each way, and no `blueprints/` folder at
all.** So **no person can reach any of the above through the app.**

**The need:** a creature blueprint and a `[[contents]]` placement in the test
bed. **`PT-1346` rules that the Builder makes it** — *"the test bed is the
Builder's first output, not a hand-written file"* — and I did not write one.

**⚠ And Loom can already do it.** It has `lib/creature/new_creature.dart`,
`lib/creature/character_writer.dart` and `lib/area/contents_writer.dart`.
**Nothing is missing but the act.**

**What the test uses instead** is a throwaway package built in a temp
directory, the way every loader test does. **That is scaffolding, not content**,
and it is why the seam is tested and still unreachable.

---

## ⚠ 4 · The second projection — still not forced, and the reason narrowed

An attack from the play screen needs to know who is standing. **It asks the
combatant it just hit**, and that combatant lives for as long as the screen
does.

**`§4` still makes it transient**: *"not written — hit/miss, current
vitality."* **Nothing about this attack survives the fight**, so nothing has to
be projected.

> **⚠ BUT THE MARGIN IS THINNER NOW.** The moment a placed creature's **damage
> persists between visits to an area** — walk out, walk back, and it is still
> hurt — that is state outliving a fight, and `PLAY-STATE-01`'s projection
> stops being deferrable. **This slice does not do that. The next one that
> keeps a wound will.**

---

## ⚠ 5 · WHAT HAD TO BEHAVE SOMEHOW — six, and five are ruled

| Slice | | |
|---|---|---|
| 1 | opposed-roll tie | **ruled `PT-1420`** |
| 1 | critical confirmation | **ruled `PT-1420`** |
| 2 | healing past `max` | **ruled — clamp both** |
| 2 | negative damage as healing | **ruled — two doors, one boundary** |
| 3 | initiative tie | **ruled `PT-1422`** |
| 4 | targeting tie | **closed by `PT-1422`** |
| 2 | `down → dead` in one blow | **still open** |

**One left, and it is the smallest of the six.** A blow that takes a character
from `down` past `dead` writes **only `character.died`** — nothing says whether
passing through `down` on the way should record both crossings. **One crossing,
one event, is the reading taken.**

**⚠ And this slice added none.** Six across five slices, and the fifth produced
zero — because everything it needed was already ruled and the two things that
were not had just been ruled by the brief.

---

## What was NOT built

**No turn order in the app**, no doctrine in the app, no encounter. **One
attack, not a fight.** No screen affordance to trigger it — `attack.dart` is
called by a test and by nothing else. **No content in the test bed.**
