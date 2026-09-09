# BUILD 53 — `PT-1471`: the content half, and the arithmetic that shrank again

**Content first. The bed had one item blueprint and now has nine, and the two
it does not have are a rules gap rather than an oversight.**

---

## ⚠ What is left, now that the notes are out

You asked what remains after `PT-1467` moved 98 cells. Measured against the
**weapon slot** — the only slot `weapon_r_1` needs:

| | pieces | resolves |
|---|---|---|
| `droid_arrays.weapon` | 9 | **9 — all of them** (7 via disambiguation, 2 outright) |
| `class_arrays.weapon` | 28 | 21 outright or via disambiguation |

Of the seven that did not:

- **1 is `NONE`** — the Brawler starts with their hands. A value, not a gap.
- **5 are `Training Lightsaber`**, which has *exactly one* catalogue row
  (`a_w_trnsbr01`, 150cr). ⚠ It failed only because the array cell reads
  `Training Lightsaber  blue` — **the separator was never an em dash.** The
  source is `**Training Lightsaber** ⚠ *blue*` and `_tables.clean()` strips the
  `⚠`, leaving two spaces. The qualifier is fused into the name by a glyph the
  extractor removes. `PT-1467`'s class, one layer along.
- **1 is `Blaster Rifle`** — genuinely ambiguous, two catalogue rows, **both at
  300cr**, and not among the 14 disambiguation entries.

**So one name is genuinely unresolved, and it is ambiguous on resref only —
not on price and not on base type.** Not 23.

## ⚠ Eleven distinct weapons, not forty-one

That is the whole content half. Nine have a base type in `EQUIPMENT-01`; two do
not.

## The answer you asked for: content first

**A reference with nothing to resolve is not worse than the fist on screen** —
`PT-1452` built every link to fail out loud, so it would read *"equips
items/weapons/ion-blaster, which will not open"* instead of *"your record
carries no [equipment]"*. Both are true sentences and neither arms anybody.

**It is worse in the record.** A record is a log and the reference is
permanent. Landing the producer first fixes a path shape into every save
written before anything can resolve it, and the first thing that ever resolves
one is also the first thing that could have told us the shape was wrong. Content
first means the first reference written is validated the moment it is written —
and the content is nine blueprints, so there is nothing to gain by waiting.

## ⚠⚠ And a third need, underneath both

**The Ion Blaster is authored and still arms nobody.** `EQUIPMENT-01` gives it
`1d4 + 1d10 vs droid`; `weaponFromBase` refuses a conditional expression rather
than truncating it to `1d4`. Verified:

    Ion Blaster  REFUSED: has damage `1d4 + 1d10 vs droid`, which is not a
                 single die expression

The blueprint is right. **The engine has no model for damage that depends on
the target** — and this is the exact case `TEST 007` opened with, an Engineer
carrying an Ion Blaster. Asserted in a test so it cannot look solved.

## The two that are not authored

- **`Marksman Rifle`** — `EQUIPMENT-01` carries blaster-, ion-, sonic- and
  disruptor-rifle and **no `marksman-rifle`**. The droid Marksman array names
  it; the rules do not have it.
- **`Training Lightsaber`** — the catalogue has one, `EQUIPMENT-01` has no base
  type. Mapping it to `lightsaber` gives a padawan's practice weapon **2d10**,
  the war blade's dice. ⚠ That is a ruling, not a mapping.

## ⚠ And the table has to move when the producer lands

It is keyed by the **array's** spelling, because that is the string the
producer will look up — `Hold Out Blaster` against `EQUIPMENT-01`'s
`Hold-Out Blaster` is one hyphen and was the only reason that name failed. But
a name→path mapping is **data**, and it currently sits in a Dart file in
`Loom/tool` that the app cannot read. `item_disambiguation.toml` is the shape
it should take. Recorded, not solved.

## Tests

**657 green** — Lodestar 297 · Lens 4 · Loom 119 · app 237.

The drift test runs both directions — a weapon the arrays name with no entry,
**and** an entry no array names — and was verified red with one entry removed.
Authored through `ItemWriter` per `PT-1346`; the pre-existing rifle came back
byte-identical.

## Still open

- **The producer** — `PT-1468`'s first NEED, now unblocked. Nine of eleven
  weapons resolve the day chargen writes the reference.
- Conditional damage (`1d4 + 1d10 vs droid`) is unmodelled.
- `Marksman Rifle` and `Training Lightsaber` need a base type ruled.
- `PT-1467`'s two: `equipment.section` as a key, and `powers.effect`'s
  `targets` column.
