# TO MAIN — from AUTHOR. Armory is safe to work during the pause. Report on what was checked.

**Owner's amendment to the pause called at `TO-MAIN-28`: Armory doesn't depend on the
engine/playtest sequencing the way the other seven books do — its numbers are already
settled, not waiting on anything the playtest could change. Cleared to work on it now,
alongside the pause on everything else.**

---

## THE HEADLINE: THE BIG EXTRACTION IS ALREADY DONE

The owner's working assumption was that Armory would need a fresh pass extracting every
item from both games off the raw `.2da` files. **Checked rather than assumed — it
already happened.**

`EQUIPMENT-01 §7` records the owner asking this exact question earlier in the project —
*"every item in both games with effects, bonuses, penalties, and restrictions"* — and
being told it was *"a data-extraction job... the 2DA holder has the files."* **That job
was completed and is sitting in this repository:** `ITEMS-01` through `ITEMS-08`,
**1,251+ items**, each with resref, source game, tier, cost, upgrade-slot flag, and full
property text — weapons (418), armour (173), upgrades (164), droid (135), worn (241),
usable (58), quest (20), other (42) — under the same seven rulings `EQUIPMENT-01` itself
cites (`PT-339` dice, `PT-341` criticals, `PT-308` tiers, `PT-327` unique, `PT-345`
crystals, `PT-349` upgradeable, `PT-384` feat remap).

**Re-running that extraction now would duplicate finished, ruled work.** Flagging this so
nobody spends a Coder cycle re-deriving what's already sitting in `STUDY/_reference/`.

---

## ONE GENUINE GAP `EQUIPMENT-01` NAMED ITSELF, NOW CLOSED

`EQUIPMENT-01 §8` states plainly that droid plating's rows in `baseitems.2da` were never
extracted, and ships **authored placeholder values**, flagged everywhere they're used
(including droid pregens' Defence). `data/k1_baseitems.2da` and `data/k2_baseitems.2da`
are both sitting in this repository's `data/` — parsed them directly by header, rows
66–68 in both files:

    Plating    Placeholder (current)      Actual, from baseitems.2da
    Light K1   +4 / uncapped               +3 / +6
    Medium K1  +6 / uncapped                +4 / +3
    Heavy K1   +8 / +1                      +9 / +1
    Light K2   +4 / uncapped                +3 / uncapped
    Medium K2  +6 / uncapped                +4 / uncapped
    Heavy K2   +8 / +1                      +9 / +1

**The K1 sums (9, 7, 10) match what `§8` already asserted as attested** — only the split
between the two numbers was previously a guess. **Not applied — reporting the extracted
values rather than editing the ruled document myself.** Swapping a placeholder for a real
mechanical value is a ruling action; that's Coder's or the owner's to make, not AUTHOR's.

---

## WHAT'S ACTUALLY STILL OPEN — SHORT, AND IT'S STAGING NOT EXTRACTION

Thirteen of Armory's eighteen chapters are `RULED` and citable today. What remains is a
short list, all `NOT HELD` (indexed in the Library, not staged into `HANDOFF`) — the same
shape as Wall 2, not a new extraction need:

`PROPERTY-VOCAB-01`, `WEAPON-MATRIX-01`, `CRAFTING-01`, `LOOT-01`, `STARSHIPS-01`,
`SPACE-COMBAT-01` (derives from `MOUNTED-COMBAT-01`), `DROID-CONSTRUCTION-01`,
`DROIDS-UPGRADE-01`.

---

## NEXT

**Owner wants to review Armory's chapter list before any prose gets drafted** — same
discussion format as the identity pass, one book at a time. That's happening on our side
first; nothing further needed from you until that lands.
