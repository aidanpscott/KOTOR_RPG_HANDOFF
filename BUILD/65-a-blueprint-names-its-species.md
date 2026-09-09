# BUILD 65 — `PT-1490`, and four things the worked row was missing

**700 green** — Lodestar 306 · Lens 4 · Loom 120 · app 270.

---

## ⚠ First, before you author: the worked row was missing four things

Filed as an amendment to `TEST/POWER-COLUMNS-SHAPE.md`, with counts. **A shape
corrected after 104 rows is 104 rows**, so I measured rather than guessed.

| | rows | |
|---|---|---|
| `save_effect` | **24 of 53** | ⚠ Without it a save is rolled and **nothing knows what passing means**. 17 *negate*, 5 *half*, 2 *"results in no effect"* — which is `negates` in other words, and is why it is a column and not a keyword match. |
| `area_squares` | **19 of 104** | ⚠ Nineteen powers **do not have "a target"**. In squares, because that is the board's unit — and the document already converts twice: *"a 10-metre radius — 5 squares"*. |
| `damage_per_round` | **6** | `Force Choke` deals damage *"each round, for the duration"*. Without it, **the same two numbers mean one hit or twelve.** |
| ⚠⚠ `affects` | 6 heal | **Not really a column — a gap in my own gate.** |

### ⚠⚠ `affects` is the one that matters

Six powers **heal**, and **three heal party members**: *"heals all party
members within 14 metres"*. `Dark Healing` heals **self**. `Death Field` and
`Drain Life` damage an enemy **and** heal the caster.

**`targets` and `excludes` say what KIND may be affected. Nothing says whether
a power is aimed at a friend or an enemy** — so `PT-1488`'s gate would let you
Force Push an ally and Heal a trooper with equal confidence. **That is mine to
fix and I cannot fix it without this column.**

Seventeen columns now, and I am not proposing an eighteenth.

---

## `PT-1490` — the blueprint names its species

`CharacterWriter` gains `species` and `chassis`, and the bed's trooper was
**re-authored through it rather than edited** — `PT-1480`. The diff is **exactly
one line**; everything else is byte-identical.

⚠ **The tool uses `render()` rather than `write()`**, and the distinction
matters: `write` **refuses to overwrite an existing creature**, which is right
for the New Creature dialog and wrong for a deliberate re-authoring. That guard
protects a user from clobbering, not a corpus from being regenerated — and the
content still comes from the writer, which is all `PT-1346` asks.

### ⚠⚠ And `loom_can_write_test` caught the writer before it had them

The reader gained two fields and the guard went red on **exactly those two** —
*"anything the Builder cannot write, the Builder eventually destroys."* ⚠ **The
first time that guard has fired on a field added the same day**, which is the
difference between a guard and a monument.

## The two symptoms, both closed

**A placement has a kind**, so `PT-1486`'s `excludes` finally has something to
refuse: `Force Static Field` is aimed at droids and the trooper is a human, and
the gate says so.

**`combatantsIn` stops hardcoding `speed: 10`.** The species owns it, per
`AUTHORED-CHARACTER-01` line 144, read out of `species.toml`'s own prose —
`"10 metres."` for 49 of 57 records. ⚠ **It happens to BE 10 for a human, which
is exactly why the hardcoding survived every slice.**

⚠ Where a species supplies no speed the default is used **and `speedNote` says
so**. A fallback that says nothing is how `speed: 10` sat there in the first
place.

## Still open

- The effect columns — yours, and the amendment is filed.
- ⚠ `affects` — my gate cannot tell a friend from an enemy until it exists.
- `PT-1484` unblocked; `PT-1485`; 45 annotation cells; conditional damage.
