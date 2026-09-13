# TEST 082 — both asks confirmed on every named count: mines draw on the
# board exactly as described, and the hazard dialog gates its required
# fields and re-enables Place on the last keystroke. But the damage-kind
# list the new gate depends on is ALWAYS EMPTY, so a damage-over-time mine
# cannot be authored at all; a mine the player sets refuses when it goes
# off; and nothing a player does to a mine survives a reload.

## Build state — four artefacts, and one of them drifted

    Loom              HEAD fe2c90c  the hazard dialog cannot write a mine
                                    that does nothing -- PT-1957, TEST
    KOTOR-RPG-APP     HEAD c5475e0  repin: the engine, with the hazard
                                    effect check
    lens              32b77e3b      recorded and resolved agree
    lodestar          ⚠ recorded 820d303d · RESOLVED 30068a65

**⚠ BOTH REPOS BUILD ONE COMMIT AHEAD OF WHAT THEY RECORD.** `pubspec.yaml`
pins `ref: main`, so `pub get` re-resolved past the pin both HEADs record.
I checked what the extra commit is before trusting anything:

- `820d303d` *a mine's effect is checked, by the function that promised to*
  — **the hazard effect check, which is item 2's engine half. It is an
  ancestor of what I built, so it IS present.**
- `30068a65` *an item names a base type that exists* — **the key-item work
  Coder says is "not done yet".** So the drift adds only the thing I was
  told not to test, and removes nothing I was told to test.

`check_shelf.py` at session start: `✓ 25 rules files, all identical to what
the extracts generate`. Loom `99414`, app `100403` and `103446` all killed
by PID, all confirmed gone.

**My instrumentation, declared:** for item 1 I hand-edited **my own**
`tester-strongroom` — two extra one-square mines at `notice 5` (so a
passive-10 character finds them, against the package's existing `notice
12` mines which it cannot) and one well-formed `charge` blueprint. Both
**reverted at the end and verified byte-identical to the backup.** Coder's
`locked-and-trapped` was not touched at all this session.

---

# 1 · MINES ON THE BOARD — all three counts CONFIRMED

The mark is a small ring with a dot in dim rust, clearly distinct from the
door glyph and from a creature token. One character, one room, one visit:

### ✓ A mine you have not found shows nothing

Soldier with **Awareness 0 and Alertness 0** — passive notice **10**.

| mine | notice | drawn? |
|---|---|---|
| `mine.strongroom.01` (2,1)–(2,2) | 12 | **no** — 10 < 12 |
| `mine.strongroom.08` (5,3)–(5,4) | 12 | **no** |
| `mine.strongroom.09` (7,3) | 5 | **yes** |
| `mine.strongroom.10` (9,5) | 5 | **yes** |

Two found and two not, in the same room, on the same passive number, with
only the DC separating them. The status line agreed:
**`you notice mine.strongroom.10 — 10 against 5`**.

### ✓ A mine you set yourself is visible immediately

**`set — armed at moderate (14)`** — 14 is `10 + Demolitions 4`, the ruled
derivation — and **the mark appeared on the square in the same frame**, no
reload and no second action.

### ✓ A defused or sprung mine carries no leftover mark

Three ways of removing one, each checked on the board straight after:

- **recovered** — `recover — d20 5 + Demolitions 4 = 9 vs 5 (trivial) ·
  lifted` → mark gone
- **defused** — `disarm — d20 5 + Demolitions 4 = 9 vs 5 (trivial) ·
  defused` → mark gone
- **sprung** — walked into the mine I had set → mark gone

In every case the other mines' marks stayed exactly where they were, so
the board is clearing the one thing that changed and nothing else.

**This closes TEST 081's D5**, which was that hazards were drawn nowhere.
They now draw in **Loom** as well — the authored mine shows in the editor
at both its squares.

---

# 2 · THE HAZARD DIALOG — both fixes CONFIRMED

### ✓ An empty required field refuses to Place

`damage over time`, with everything else filled, naming each missing field
in plain language and greying `Place`:

    amount and rounds filled, no kind
      → still needs what kind of damage it is
    amount cleared
      → still needs how much damage it does · what kind of damage it is
    rounds cleared too
      → still needs how many rounds it lasts · how much damage it does ·
        what kind of damage it is

It accumulates rather than reporting one at a time, and it says what the
field *means* rather than naming the key. Nothing was let through as a
silent zero.

### ✓ Filling the last field re-enables Place on the keystroke

On the `condition` branch, `condition = stunned` with `rounds` empty →
`Place` dead. I typed `2` into `rounds` and **captured the frame without
clicking anywhere else**: `Place` was live. No extra action needed
anywhere on screen. That is the specific regression Coder flagged, and it
is fixed.

It wrote correctly:

```toml
[[hazards]]
tag       = "mine.strongroom.08"
over      = [[5, 3], [5, 4]]
disarm    = 20
notice    = 12
does      = "condition"
condition = "stunned"
rounds    = 2
save      = { dc = 15, on_save = "half" }
```

### ✓ And two TEST 081 findings are closed on the way past

The dialog now carries **a free number box beside each ladder** —
`or [12] between tiers, which §3b allows` and `or [20] hard`. That is
TEST 081's **D2** answered, citing the same clause I quoted
(`AREA-FORMAT-01 §3b`, *"the ladder recommends rather than constrains"*),
and **D3** with it: the `notice` default is now visible in its own box
instead of being written invisibly by an unselected row.

---

## ⚠⚠ BUT THE NEW GATE CANNOT BE SATISFIED — a damage mine is now unauthorable

The damage-kind requirement is real and correct. The list it picks from is
**always empty**, and the dialog blames the wrong thing:

> ⚠ base-rules is not installed, so there is no damage kind to choose from
> — a mine written now says what it does and not what kind of harm it is

**base-rules IS installed.** `check_shelf.py` verified it this session, and
Loom reads it elsewhere in the same run.

**The mechanism, measured rather than inferred.** `damageKinds`
(`Loom/lib/item/base_types.dart:293`) opens
`base-rules/rules/items.toml` and collects `row['kinds']` off each item
row. In that file `kinds` does not live on the item row — it lives inside
the nested `[[items.effects]]` table:

```toml
[[items]]
name = "Kyber Dart"
...
[[items.effects]]
does  = "damage_over_time"
kinds = ["poison"]
```

Parsed over all 1,424 rows:

    row['kinds']              what Loom reads      →  0 kinds
    row['effects'][*]['kinds'] where they live     →  13 kinds

and the 13 are `bludgeoning · cold · dark side · electric · electrical ·
energy · fire · heat · ion · piercing · poison · slashing · sonic`.

**The function's own docstring proves it knew.** It says the shelf *"carries
`electric` AND `electrical`, and `fire` AND `heat` — near-duplicates…
showing both lets an author match what the items already say."* Those
pairs only appear at the nested level. The intent was right and the read
is one level too shallow.

**Consequence:** `Place` is permanently dead for `damage_over_time`. The
only way to satisfy *"still needs what kind of damage it is"* is to pick
from a list that can never be non-empty. **A damage mine could be authored
before this slice and cannot be now** — I authored one in TEST 081. The
`condition` branch is unaffected, which is the only reason item 2 above
could be tested at all.

*Two smaller things in the same dialog:* the `condition` branch shows **no
`still needs` line at all** — `Place` is simply dead with no reason given,
where the damage branch names every missing field. And Loom's **Verify
does not flag an already-authored damage mine with no `kinds`** — the
count stayed at 20 with one in the file — so the gate is authoring-time
only and says nothing about what is already on disk.

---

# 3 · THREE THINGS FOUND WHILE EXERCISING SET AND RECOVER

These are the new `bc542e9` verbs, which item 1 required me to drive.

### ⚠⚠ A mine the player sets REFUSES when it goes off

I set a mine, walked into it, and got:

> `goes off — ⚠ 'mine.set.0.a01-strongroom' needs a does — 'charge' is
> damage_over_time or condition, and which one decides what it means.`

The item I set was well-formed and carried `does = "condition"` with every
field its base type requires.

**The contract is stated in the engine and not kept by the app.**
`setMinesIn` (`remains.dart:136`) builds the hazard with
`values: {'from_item': item}` and says why:

> ⚠ WHAT IT DOES IS THE ITEM'S, and the item is named rather than opened:
> `ENGINE-INTERFACE-01 §4` keeps this file off the disk, **so the caller
> joins it the way it joins every other blueprint.**

**The caller never joins it. `from_item` does not appear anywhere in the
app** — not in `lib/`, not in `test/`. The spring path reads the hazard's
own `values` as if they were the item's fields, finds only `from_item`, and
falls through to `consumableFromBase`'s refusal — which is why the message
names a *hazard tag* as though it were a malformed item.

So every mine a player sets is inert-with-an-error. The set half of the
verb works; the half that makes it do anything was left to a join that was
never written.

### ⚠⚠ Nothing a player does to a mine survives a reload — but what they gained does

| after leaving and pressing Continue | |
|---|---|
| mine that was **recovered** | **back**, live, recoverable again |
| mine that was **defused** | **back**, live |
| the item the recover gave | **still carried** |
| walked position | correctly restored |

So the two halves of one action persist differently: the mine forgets, the
bag remembers. **Demonstrated rather than inferred** — I recovered the same
mine on three separate visits and the bag ended reading
**`carrying — test-mine · test-mine`**. A mine with a `recovers` item is an
unlimited supply of that item, one per reload, and no authored hazard in a
package can be permanently cleared.

This is the same shape `BUILD 182` already fixed for locks — *a picked lock
survives the visit* — applied to doors and containers and not to hazards.

### ⚠ The bag is not re-read when an item is acquired, so a mine you have just recovered cannot be set

Straight after a successful recover, with **`carrying — test-mine`**
showing, right-clicking any ground square gave **`nothing to do there`** —
no `Set mine`. After leaving and pressing Continue, the identical
right-click on the identical square offered **`Set mine`** and it worked.

`_aCharge` reads `_consumables`, which `_readBag()` fills; `_readBag` does
not run on `item.acquired`. So the intended loop — recover a mine, set it
again — cannot be completed in one visit, which is the loop the verb pair
exists for.

*(A fourth thing, correctly mine and not the product's: my TEST 081
`sith-keycard` is a bare `charge` with no magnitudes, and `consumableAt`
refuses it. That is the fixture being wrong, not the app — I checked
before filing, and authored a well-formed charge instead.)*

---

## Also seen, not chased

- **`Recommended` is unimplemented on both Abilities and Skills** —
  *"no recommended spread is in the rules yet"* / *"no recommended
  allocation is in the rules yet"*. The button is present and refuses on
  both. Known-shaped, named rather than filed.
- The arrival marker `back` sits at (1,1) and a new game still starts the
  player at **(0,0)** in this package — **TEST 081's D7 re-confirmed**:
  `tester-strongroom` has no `[entry].at` because Loom cannot write one.
  Coder's `locked-and-trapped`, which has it, starts correctly.
- Only **one** notice line is printed when two mines are found on arrival,
  though both are marked — the same first-only reporting TEST 077 noted
  for a multi-target scan.
- The footer still reads **`1 rule about this character not checked`**.

## What I did not check

- **The key-item authoring gap** — explicitly not ready, not tested, and
  not re-reported.
- **A damage-over-time mine end to end**, because it cannot be authored
  (above). Everything in item 2 was exercised on the `condition` branch.
- **`kinds` on a set mine**, for the same reason.
- Whether the set-mine refusal also fires for a `damage_over_time` charge
  — I could only build a `condition` one.

## State

- **`tester-strongroom` is mine.** Two test mines and one item blueprint
  added for this session and **removed again**; the area file is verified
  **byte-identical** to the pre-edit backup, and the extra blueprint is
  deleted. The `condition` mine `mine.strongroom.08` authored through Loom
  during item 2 is kept deliberately — it is the artefact that test
  produced.
- **Coder's `locked-and-trapped` untouched this session.**
- Several saves in `tester-strongroom`, not cleaned up.
- Loom `99414`, app `100403`, app `103446` — all killed by PID, confirmed
  gone.
