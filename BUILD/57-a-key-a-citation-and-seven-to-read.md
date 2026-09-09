# BUILD 57 — `PT-1478` closed, `PT-1480` the key, `PT-1479` the leak, and the seven

**681 green** — Lodestar 303 · Lens 4 · Loom 120 · app 252.

---

## The three Sith dice

They are stated in a **blockquote table under a different shape** from the
per-class stat rows, so `read_phb` returned null for all three. A derived-dice
reader matches on the heading rather than on *"a row that looks like a class"*,
and `force_die_source` travels with each value. **All six Force classes carry a
die and they mirror pairwise.** The test asserted the gap, so it went red on
the ruling.

## 1 — `equipment.section` is a key

The labels were **the extractor's own strings**, not the document's headings,
and two carried an aside. Split into key and note; *"named placeholder
values"* is not discarded, because those three rows really are placeholders.

⚠ **And it has its first reader.** `resolveStartingWeapon` considers only rows
a character can carry. **Not cosmetic:** `Heavy` names *both* a wield class and
a plating grade, and `Rifle` is a wield class sitting in the same map as
`Blaster Rifle`. Nothing names either in an array today — the filter is there
so it cannot start silently.

## 2 — The seven

`HANDOFF/TEST/THE-SEVEN-powers-effect.md`, full cell text, one per section,
with tier, cost and targets beside each. **Not mine to decide**, as you said.

## ⚠⚠ And `PT-1479`, which arrived mid-slice and was all mine

**The Brawler.** `_whyUnarmed` returned one fixed sentence for every unarmed
character, so **the one class for which unarmed is correct got a defect notice
as flavour text** — and blamed the grant, which is unrelated. It reads the
record's own field now. `dax-roon.sav` already said the right thing and the
screen printed over it: `PT-1471`'s diagnostic **surviving past the gap it
diagnosed.**

**The literal.** `check_player_strings.py` reads Dart string **literals** in the
play client — comments excluded, because they cite freely and should, and prose
only, because a key or a path has no room to hide a citation. **Nine found and
fixed**; each keeps its rule and loses its reference. Scoped to the play client
deliberately: **Loom's user is an author and is owed the citation.**

⚠ **Three tests asserted the citations were ON SCREEN** — they encoded the
defect. They now assert the fact reaches the player and the reference does not.

**The two spellings — not title-casing.** **My own Loom tool** authored the
blueprint with `EQUIPMENT-01`'s then-current `Hold-Out Blaster`, and `PT-1477`
corrected the data without correcting the copy. **An authored artifact is a
copy of the data, and nothing compared them.** `bed_weapons_test` compares them
now.

**§4a's label in a save.** An `upgrade` grant is an **instruction** — Hunter's
reads *"TAKES THE CLASS'S OWN melee UPGRADE FROM §4a — Soldier → Long Sword…"*
— and writing it as `item` persisted a table's label as an item's name. Only a
slot-filler names an item.

⚠ **And a bare `§` is the THIRD citation form the check could not see**, after
`PT-1474` found the second. **42 → 52** shipped cells: the instrument seeing
more, not the corpus getting worse.

---

## ⚠ Is `targets` worth wiring alone? — measured, and the answer changed

**Not as a gate. As a check, immediately.**

`targets` needs only the defender's KIND, which the app already has at the seam
— so it is genuinely cheaper than conditional damage, which additionally needs
a damage expression that is a list of terms and a grammar. That was my
expectation.

⚠⚠ **Then I measured the column against the prose, and it inverts the answer:**

| | |
|---|---|
| powers whose **prose** says *"does not affect droids"* | **23** |
| of those, whose `targets` column says so | **2** |
| ⚠ **silent** | **21** |

**A gate built on `targets` today would block 17 powers and silently permit 21
that the prose says should be blocked** — a wrong answer with a machine's
confidence, which is worse than no answer. The column is not under-read, it is
**under-populated**, and nobody could have known because nothing read it.

**So the cheap, high-value step needs no runtime work at all:** the same fact is
stated 23 times in prose and 2 times in the column, and a check comparing them
is the shape this project already has three of. Populate `targets` from what
the prose already says — or report the 21 — and *then* the gate is worth
building, at which point conditional damage shares the "a combatant knows its
kind" half with it.

## Still open

- The seven, for you.
- 52 cells where a citation is load-bearing in a sentence.
- `targets` under-populated by 21 against its own prose.
- Conditional damage — costed at `BUILD 55`.
- `§4a`'s grant offer reaching classes it does not name.
