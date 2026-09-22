# TEST 133 — the payment-gated bed, and the defect reproduced in play

Approved at `PT-2568`. This is the fixture build, not the re-check — Coder's
credits fix has not landed yet, and that is deliberate: **a bed that does not
discriminate before the fix proves nothing after it.**

**Build.** App **`e6c2e4a`** (unchanged from TEST 132), tree clean, built from
`git archive` of that sha. The lock resolves Lodestar
**`4fe831be1054d3050a793ff2090ac4ef9f286956`** and Lens **`32b77e3b`**, and
those are the pub-cache checkouts `package_config.json` compiles against.
`check_shelf.py` clean: 29 rules files and 65 standard blueprints.

**Result.** The bed is built, validated through the real parser, and
**reproduces PT-2566's dialogue half in play** with a control that
discriminates. Three readers of one number, measured on one save at one
moment:

```
the Store's readout       Credits  600
the Inventory's readout   CREDITS  500
the dialogue's payment gate        500   — the 600-gated reply stays hidden
```

---

## What the bed is

`tester-purse` — my own package, so nothing of Coder's or the owner's is
touched. A merchant (`Vess`) on an 8×6 board, two squares from the arrival,
whose conversation carries **three** replies behind the store one:

```toml
replies = [
  "browse",                                      # opens the store
  { to = "pay-low",  gate = { payment = 400 } }, # THE CONTROL
  { to = "pay-high", gate = { payment = 600 } }, # the reading
  "leave",
]
```

The character starts on **500** credits and carries two vibroblades worth
**100** each, so **one sale crosses 600 and nothing else does.**

⚠ **The low gate is there so a total silence is diagnosable.** If neither
gated reply ever appeared, the fault would be my authoring rather than the
product's fold — and I would have filed a defect against a bed that never
worked. It is the same shape as every control this session has needed.

## It parses, and both gates are read

Through `openConversation` itself rather than a reimplementation:

```
purse.toml -> OpenedConversation
   id purse  npc 2  player 4
   link greet -> browse
   link greet -> pay-low   gate {payment: 400}
   link greet -> pay-high  gate {payment: 600}
   link greet -> leave
```

The library also loads the package with **no problems** listed.

## The reproduction

**Before any sale — 500 credits:**

```
MERCHANT.PURSE.01
Credits talk. What have you got?

  [Opens-store]          Show me what you have.
  [Bribe · 400 credits]  I can cover four hundred.     ← the control, shown
                         Another time.
```

`I can cover six hundred.` is **absent**, correctly: 500 < 600.

**Sold one vibroblade. The Store's own readout moved 500 → 600**, and the
save carries the pair:

```
{"kind":"item.lost","payload":{"subject":"Purser","item":"items/weapons/vibroblade"}}
{"kind":"item.acquired","payload":{"subject":"Purser","item":"credits","count":100}}
```

**After the sale — 600 credits by the Store's reading:**

```
MERCHANT.PURSE.01
Credits talk. What have you got?

  [Opens-store]          Show me what you have.
  [Bribe · 400 credits]  I can cover four hundred.     ← still shown
                         Another time.
```

**Identical. The 600-gated reply is still hidden.** The control is still
there, so the gate machinery works and gated replies do render — only the
number the gate compares against never moved.

**And the Inventory agrees with the dialogue, not the Store:** `CREDITS 500`,
with one vibroblade left in the bag, so the item half of the transaction
landed and the credit half did not reach either reader.

## Why it is the field and not the fold

`dialogue_run.dart:249` compares `v.credits` against the gate's figure, and
`DialogueView.credits` is fed `widget.character!.equipment?['credits']`
(`play_screen.dart:5688`) — the authored starting purse.

⚠ **The engine's own prose already says so.** `creditsAfter`'s doc in
`remains.dart:340`:

> *"A character's starting credits are authored on the `CharacterRecord`
> itself (`equipment['credits']`), **the same field `DialogueView.credits`
> already reads for a `payment` gate**. This fold is the log's own ADJUSTMENT
> on top of that starting figure."*

The adjustment exists and the dialogue never asks for it.

## What the bed will say when the fix lands

* `I can cover six hundred.` appears **after** the sale and not before.
* `[Bribe · 400 credits]` stays visible throughout — if it ever disappears,
  the fix has broken the passing case.
* The Inventory's `CREDITS` reads 600 at the same moment.

⚠ **And the third reader is the one to watch.** A fix applied to the
Inventory alone would turn my TEST 132 reading green and leave this bed red,
which is exactly why it exists. I will grep every reader of
`equipment['credits']` rather than re-running one comparison.

## Fixture

`~/.local/share/kotor-rpg/packages/tester-purse/` — package, one area, one
merchant blueprint, `stores/purse.shp`, `dialogue/purse.toml`, and a copy of
`store-bed`'s vibroblade blueprint (item paths resolve inside the SELECTED
package).

`mk131.py` gains **`purse`** — 500 credits, two vibroblades, level 4.

⚠ **One harness note for my own future runs.** `pkg.sh`'s fixed scroll count
put me on the wrong card once the library grew to 39 packages, and a
premature Continue fell through to New Game and chargen. The library's
horizontal position is not stable across package counts; scroll, screenshot,
and read the card before clicking it.
