# 031 · What click-to-move must answer, what the keys are doing, and what stands between Cleave and a player

**From `Tester`. Unrequested number.** Three specification questions rather than
three tests — *what a thing needs*, not built.

**⚠ BUILT AND TESTED AGAINST:**

    app 3942e39 · Lodestar 44dd556 · Lens 6b55219 · Loom df15adf

All four clean at build time, and `KOTOR-RPG-APP/pubspec.lock` carried
`resolved-ref: 44dd556…`, matching `Lodestar` HEAD.

**⚠ Three corrections to the brief, up front, because two of them change the
question:**

1. **`species` has already landed.** `PT-1582` is in `Loom 9df9fb9`, under
   `df15adf`. **I reported it in `030 §5`** — 35 species as a closed button
   list, and `derived 8 · override 0 = vitality 8`. The bed is ready.
2. **The movement remainder IS driven** — see `§1a`. I watched it read
   **`◆ 10 → 8 move`** on screen.
3. **The attack chains are NOT in the data.** See `§3`. The gap is one hop
   longer than the brief assumes.

---

# 1 · WHAT CLICK-TO-MOVE MUST ANSWER

**`PT-1443` ruled it; nothing has been designed. Here is the list, taken from
what `_step` actually does rather than from what movement usually needs.**

## 1a · ⚠ First, the correction: the remainder is not half-built

**`_afterNextStep` (`play_screen.dart:1646`) is complete and it runs.**
Standing at `5,3` in `a03-probe-yard`, adjacent to the difficult block at cols
2–4, in a fight, the strip read:

    ◆ 10 → 8 move
    ● action
    ▪ gear

**Ten now; eight if you step onto the rough square beside you.** `PT-1513`'s
doubling, shown before it is paid, exactly as `PT-1519` asked.

## 1b · ⚠⚠ AND ITS OWN COMMENT IS THE REASON CLICK-TO-MOVE BREAKS IT

> *"**THE DIRECTION IS NOT KNOWN AND DOES NOT NEED TO BE.** `PT-1513` puts the
> multiplier on the CREATURE and the source on the GROUND KIND, so every
> difficult neighbour costs the same — the pending cost is a fact about rough
> ground, not about which way you press."*

**That reasoning is sound for one step in an unknown direction and false the
moment a click names a destination.**

- Today: *"is any neighbour rough? then one step costs 2."* One number, no path.
- With a click: the path may cross **three** rough squares, or none, and
  **`10 → 8` would be wrong in both directions.**

> **⚠ So the display does not need building. It needs RE-DERIVING from a path
> that does not exist yet.** `_afterNextStep` should become *"what this route
> costs"*, and its current answer is a special case of that with a path of
> length one.

## 1c · The seven things a click must answer, from `_step` itself

**`_step` (`:588`) makes seven decisions per square, in this order.** A click
names a destination, so it must answer each one **for every square on the
route**, and decide what to do when one of them interrupts:

| # | `_step` does | a click must decide |
|---|---|---|
| 1 | bounds check | — |
| 2 | **`_occupant(nx,ny)` → begin fight or strike** | ⚠ **a click on an occupied square: walk adjacent and stop? walk and attack? refuse?** And a creature *on the route* is not the destination — does the route stop, or path around? |
| 3 | **`passable` → "the wall blocks the way"** | ⚠ **a click across a wall: is there a pathfinder, or is a blocked route refused whole?** There is no pathfinder today. |
| 4 | **`canAfford(1, ground)` with `moveCostSource`** | ⚠ **the whole route's cost, not one square's** — and `PT-1513` prices it per creature, so it is `costOf(route)` and not `route.length` |
| 5 | move | ⚠ **all at once, or square by square?** `§1b` and `§1f` both turn on this |
| 6 | **`_lookAround()` — the find, on approach** | ⚠⚠ **once at the destination, or at every square passed?** `PT-1573` is *on approach* and settled-once; a route that skips the evaluation walks past a hidden thing that would have been found |
| 7 | **connection → `_enter()` travels** | ⚠ **a route crossing a doorway travels mid-route.** Does the click stop at the door, or step through and abandon the rest? |

**⚠ `6` is the one I would decide first**, because it is the only one where the
wrong answer is silent: a route that finds nothing looks exactly like a route
where nothing was there.

## 1d · ⚠ And a click out of range has two honest answers

`canAfford` today refuses with *"no move left this turn — X costs double"*.
For a route the choice is **refuse the whole click**, or **walk as far as the
budget allows and stop** — which is what `move()` already returns (*"what it
managed"*, per its own comment at `:169`). **The engine can already answer
"how far did I get"; nothing asks it.**

## 1e · ⚠ The diagonal dissolves, and that is the point

`030` proved a diagonal is one square and that **no diagonal key exists**. A
click names a square, so **the four-key limit disappears without four more
bindings** — and `squaresBetween`, which has one caller today, gains its second.

## 1f · ⚠ One thing that does NOT need answering, and would be easy to invent

**Facing.** Nothing in the product has a facing; `Adjust Location`'s bearing is
Aurora's, not ours. A route need not decide which way you end up looking.

---

# 2 · THE KEYS — what the eleven are doing, and it is not eleven

**⚠ There is no settings surface anywhere, and the bindings live in FOUR
separate handlers with no shared table.** Enumerated from source and confirmed
in play.

## 2a · The four handlers

| handler | when | keys |
|---|---|---|
| **board** `:2098` | walking / fighting | `←` `→` `↑` `↓` · `space` · `M` · `F` · `esc` |
| **`_talkKey`** `:934` | a conversation is open | `esc` · `enter`/`numpadEnter` · `backspace` · **digits 1–9** · **every printable character** |
| **`_castKey`** `:1839` | the power list is open | `esc` · `F` · **digits 1–9** |
| **`_refusal`** `:2015` | an area that cannot be drawn | `esc` |

> **⚠⚠ SO IT IS NOT ELEVEN BINDINGS. It is eight named keys, plus TWO WHOLE
> CLASSES — the digits and every printable character — across four modal
> contexts.**

## 2b · ⚠ `esc` means four different things

    board      leave the screen
    talk       end the conversation
    cast       close the power list
    refusal    leave the screen

**Never destructive, always "back one level"** — which is a coherent rule, and
**nothing writes it down.**

## 2c · ⚠ `F` and the digits are each two things

**`F`** opens the power list from the board and **closes it** from inside — a
toggle split across two handlers.

**Digits** pick a power in `_castKey`, and pick a reply in `_talkKey` — **but
only while the typed box is empty.** Its own comment:

> *"A DIGIT PICKS ONLY WHILE THE BOX IS EMPTY — otherwise `"50 credits"` could
> not be typed. **The box wins once you are in it.**"*

**⚠ That is the sharpest piece of key design in the product and it is the one a
settings screen would break**, because it is not a binding — it is a
context-sensitive rule about a conflict.

## 2d · What a player would want to change — the list a settings screen is built from

| binding | rebindable? | why |
|---|---|---|
| `←` `→` `↑` `↓` | ⚠⚠ **yes, first** | **WASD is the single most-expected rebinding in the medium**, and `PT-1443` wants keys as the alternative to clicking |
| `space` end turn | **yes** | it is a verb, and BG3's own End Turn is rebindable (`STUDY 20`) |
| `M` map · `F` powers | **yes** | mnemonics in English only — **a non-English keyboard has no `M` for map** |
| `esc` | ⚠ **no** | it is the universal back; rebinding it strands a player in a modal with no way out |
| `enter` · `backspace` | ⚠ **no** | they are text editing, not game verbs |
| digits | ⚠ **no, and say why** | they index the list on screen (`PT-1303`), and `§2c`'s conflict rule cannot survive rebinding |
| **every printable character** | **not a binding at all** | it is the typed box, and a settings screen must not list it |

**⚠ So the surface is four rebindable rows and three explicitly-not rows** —
and `PT-1500`'s rule applies: **the three that cannot change should say why
rather than be absent**, or an author will look for them.

**⚠ And one thing is missing from every context: there is no key that lists the
keys.** The board's footer carries *"arrows to move · m map · esc to leave"* and
**never mentions `space` or `F`** — the two verbs a fight needs.

---

# 3 · ⚠⚠ CLEAVE — the gap is one hop longer than the brief assumes

**The brief asks what stands between *"the chain is in the data"* and *"a player
uses it"*. Checked, and the chain is NOT in the data.**

## 3a · What IS in the data

`base-rules/rules/feats.toml` — **320 feats, 121 distinct chains**, each row
carrying:

    id · name · chain · is_chain_head · level · section · description
    effect · availability · note

**The chain machinery exists as data**: `chain` groups the tiers,
`is_chain_head` marks the first, `level` gates them.

## 3b · ⚠⚠ And none of the attack chains is among them

    cleave        ⚠ ABSENT        flurry    ⚠ ABSENT
    power attack  ⚠ ABSENT        rapid     ⚠ ABSENT
    spread        ⚠ ABSENT

**`ATTACKS-05` specifies Cleave completely — `§47`–`§49` and `§139`'s table —
and it exists in no rules file.** There is no `attack_chains.toml`, and
`feats.toml` does not carry it.

## 3c · ⚠ And the feat shape could not hold it as it stands

Cleave needs three things `feats.toml` has no field for:

| Cleave needs | `feats.toml` has |
|---|---|
| **`Strength 12`** — an ability requirement | ⚠ **no requirement field of any kind** |
| **a target count** — 2 · 3 · every enemy within 2 squares | ⚠ `effect` is **prose**: `"+3 Demolitions and Stealth."` |
| **an attack modifier** — −3 · −2 · −1 | ⚠ same — a sentence, not a number |

> **⚠⚠ `effect` IS A HUMAN SENTENCE. Every one of the 320 feats carries its
> mechanics as text nothing reads.** That is `PT-1500`'s shape at scale, and it
> is why Cleave cannot simply be added as a 321st row.

## 3d · So the answer is "all three, and two more upstream"

**You asked: a verb, a target picker, a budget cost, or all three.**

| # | missing | evidence |
|---|---|---|
| 1 | ⚠ **the data** | not in `feats.toml`, no `attack_chains.toml` — `§3b` |
| 2 | ⚠ **a shape that can hold it** | no requirement field; `effect` is prose — `§3c` |
| 3 | ⚠ **a verb** | the complete key set has nothing that declares — `030 §2` |
| 4 | ⚠ **a target picker** | the only targeting in the product is *"the square you stepped into"* (`_occupant(nx,ny)`) |
| 5 | ✅ **a budget cost — THIS ONE EXISTS** | `spendAction()` works and is called twice |

## 3e · ⚠⚠ And the budget half is the same family as `areAdjacent`

**`Budgets` offers six spenders. The app calls two.**

    move()              ✅ play_screen.dart:667
    spendAction()       ✅ fight.dart:134 · play_screen.dart:1310
    spendBonus()        ⚠ NO CALLER
    spendGear()         ⚠ NO CALLER      (BUILD 84 found this one itself)
    spendInteraction()  ⚠ NO CALLER
    spendReaction()     ⚠ NO CALLER

**`029 §9` said two of five budgets have no producer. It is four of six
spenders, and `areAdjacent` makes seven.**

> **⚠⚠ THAT IS `PT-1529`'s KIND WITH NEITHER END, ARRIVING AS A METHOD — and it
> is now a pattern rather than an instance. `Cleave` would need `spendAction`
> (exists), `areAdjacent` (exists, zero callers) and `squaresBetween` (exists,
> one caller). THE ENGINE IS READY AND NOTHING ASKS IT.**

---

# 4 · A seventh orthogonal-only site, for `030`'s census

**`_afterNextStep` (`:1652`) hardcodes the four orthogonal offsets:**

    for (final d in const [Point(1,0), Point(-1,0), Point(0,1), Point(0,-1)])

**So the remainder does not see a rough square on the diagonal.** Standing
beside difficult ground diagonally, `10 → 8` would not show — and by `PT-1581`
that square is one away.

**`030` found two orthogonal-only sites (`_step`'s call sites, and melee reach
via `_occupant`). This is the third, and it is the one that is silently wrong
rather than merely absent.**

---

# 5 · Scoped negatives

- **`§1` and `§2` are a specification, not a test.** I ran the remainder
  (`§1a`) and the key set (`030`); **I did not build click-to-move and I have
  not tested a route across anything.**
- **`§3` is a data and source read.** I did not attempt to add Cleave.
- **`§4`'s diagonal-rough case is DERIVED from the code, not observed** — I did
  not build a fixture with difficult ground diagonally adjacent and confirm the
  remainder stays silent. **That is a one-fixture test and I did not run it.**
- **`PT-1582` in play** — still only looked at, `030 §5`. Whether a Gamorrean
  created in Loom hits at `+4` is untested.
- **Painting tiles in Loom** — still not done, seven sessions.

---

# 6 · What I left behind

**`a03-probe-yard` gains one fixture and it is the `PT-1519` bed:**

    probe-anvil.probe-yard.04   at 6,3    tag_seq 3 → 4

**Placed so a fight can be started from `5,3`, which is orthogonally adjacent to
the difficult block at cols 2–4, rows 2–3.** Standing there in a fight, the
strip reads **`◆ 10 → 8 move`**. Sixty vitality, so the fight lasts long enough
to read it.

**`a04`'s five and `a01`'s zoo are unchanged**, including
`probe-warden.probe-room.10` — `hidden` with no stealth — kept as the
demonstration that a find test alone proves nothing.

**Backups: `BK3/`–`BK7/`.**
