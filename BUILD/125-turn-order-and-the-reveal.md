# BUILD 125 — turn order on screen, and striking reveals you

Both from my own `BUILD 124` not-done list. `PT-1422`, `PT-1550`, `PT-1678`.

---

## 1 · ⚠⚠ THE ORDER IS THE FIGHT'S, NOT THE DISPLAY'S

    turn order
    ▶ Vess Taran        14
    › probe-pair.01      9
      probe-pair.02      9

`rollInitiative` sorts once — **initiative descending, then Dexterity modifier
descending, then tag ascending** — and `turn` is an index into **that same
list**. `Fight.order` hands it over unsorted; `Fight.nextUp` is the same skip
`advance` walks.

**⚠ `nextUp` exists so the skip is not written twice.** `advance` also ends the
round when the order wraps; `nextUp` answers *whose turn is next* and changes
nothing. **Two copies would be two answers to one question** — the strip naming
one combatant while the fight hands the turn to another.

**⚠ The rows keep their order and the strip carries the other one.** Membership
has a join order (`PT-1672`); turn order is a different question about the same
set — `STUDY 32 §5`: *"whose turn is next is a question about an ordered
sequence of participants."* Re-sorting the rows each round would move a health
bar out from under the eye reading it, and the player's card would have to leave
the top or break the sequence.

**⚠ Shape carries identity** — `PT-1517`. `▶` is now and `›` is next, so the two
survive a monochrome screenshot. Out of the fight is **dimmed and still
listed**: a name that vanished mid-round would make the sequence unreadable, and
it is `PT-1672`'s reason for keeping a hidden row one level down.

## 2 · ⚠⚠ THE OWNER'S QUESTION, ANSWERED FROM BOTH ENDS

> *"If a tie-break actually shows on screen, confirm the display order matches
> `PT-1422`'s rule rather than just matching `rollInitiative`'s internal sort
> order by coincidence — they should be the same thing, but say so rather than
> assuming it."*

**They are the same LIST, so at that layer there is nothing to coincide.**
`Fight.order` returns `encounter.combatants` — the object `turn` indexes. The
risk is one layer up, and it is real:

> **A panel that sorted by the initiative NUMBER would agree on every board
> where nobody ties, and break a tie by whatever the sort happened to do on the
> first board where two do.**

So it is tested from both ends, each where it lives:

| | |
|---|---|
| `fight_test` | a **real tie** — equal rolls, equal Dexterity — and the order is **ascending tag**, not the order the caller built the list in. Every number identical, which is what makes it a statement about the tie-break rather than about the rolls. Plus Dexterity outranking the tag. |
| `roster_panel_test` | the strip is handed **ASCENDING** numbers and must render them **in the order given**. A panel-side sort reverses them and fails. |

**⚠⚠ AND ONE MUTATION PASSED, WHICH IS ITSELF THE ANSWER.** Replacing
`Fight.order` with a stable sort by initiative alone **changes nothing** — the
list is already in that order, because `rollInitiative` put it there. *They
really are the same thing*, and the only way to make them differ is to sort
somewhere the rule is not. **Reversing `order` fails both tie cases**, and
sorting inside the panel fails the strip case; the stable-sort mutation is
invisible for the right reason and is recorded rather than papered over.

## 3 · ⚠⚠ STRIKING REVEALS YOU

`PT-1550` is *"not shown until something reveals it"*, and **shooting somebody
is something.**

**⚠ `PT-1678` made it reachable and made it wrong.** Before multi-enemy fights a
hidden creature could not be in a fight at all — contact starts one and contact
reveals. A creature pulled in by adjacency **joins concealed**, and could then
shoot you every round from a square the board does not draw.

**⚠ ONLY ON A STRIKE, and `r == null` is the difference.** `enemyTurn` returns
null when it holds or breaks off; **moving is not a reveal** and neither is
standing still. **A miss reveals**, because what gives you away is the shot
rather than the hit.

**⚠ The attacker is taken BEFORE the turn runs.** `enemyTurn` reads `current`
itself and the advance moves it, so asking afterwards would name whoever is up
next rather than whoever just swung.

### ⚠ And the concealed window is real but rarely observable — said, not glossed

`_begin` runs the enemy turns **itself** when the player loses initiative, the
dice are seeded, and in the `two-enemies` bed a droid wins — so the lurker
strikes and reveals **inside the same synchronous call that starts the fight.**
There is no frame in that fixture where it is both in the fight and concealed.

**So the joins-concealed half is what the MUTATION proves**: remove the reveal
and the case fails with the lurker still in `concealed`, which is only possible
if it joined that way. The marked ROW is asserted directly in
`roster_panel_test`, where it is deterministic.

## 4 · ⚠ One of my own assertions was the wrong shape

The screen test first asserted that pressing space lands on whoever `next`
named. **It does not, and should not:** space is `_endTurn`, which runs the
**whole enemy half of the round**, so the combatant on screen afterwards is the
player again.

**`nextUp` versus `advance` belongs one layer down**, and `fight_test` walks it
directly — including the skip over a fallen combatant, and the null case.
Removed from the screen rather than weakened into something that would pass.

## 5 · Every guard was seen to fail — `PT-1661`

| Mutation | What broke |
|---|---|
| striking does not reveal | the hidden-combatant case |
| no turn order is handed over | the strip on screen |
| the **panel** sorts its input | `THE STRIP DOES NOT SORT` |
| `Fight.order` reversed | both tie cases |
| `Fight.order` stable-sorted by number | **nothing — and §2 is why** |

## 6 · Tests

| | before | after |
|---|---|---|
| `Lodestar` | 545 | **545** |
| `Loom` | 253 | **253** |
| `Lens` | 10 | **10** |
| `KOTOR-RPG-APP` | 426 | **436** |
| | 1,234 | **1,244** |

`gate.py` SENDABLE, 2 advisory warnings, both pre-existing in
`PLAYTEST-RULINGS-01`. `check_engine_pin.py`: 4 pins level.

## 7 · Not done, named rather than skipped

- **The strip does not show the round number**, and `endRound` has one. A fight
  that has gone eight rounds looks like one that has gone two.
- **Nothing reveals on being HIT.** A hidden creature that is struck by an area
  effect — when one exists — would stay hidden; today the only way to hit one is
  to walk into it, which already reveals.
- **A revealed creature stays revealed only for the visit** — `PT-1550`'s own
  rule, unchanged: walk out and back and it is hidden again, including one that
  shot at you. That is the ruling, and it now has a case where it reads oddly.
- **Detection at range and faction-aware hostility are untouched**, held for a
  ruling as instructed.
