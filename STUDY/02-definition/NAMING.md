# STUDY 02 — DEFINITION LAYER — NAMING

*KOTOR's name · what it actually is · a clearer name.*

Batch-2 additions. Merges with `01-container/NAMING.md`.

---

## Formats

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **2DA** | A rules table: rows of things, columns of properties, every cell an untyped string. The name means "2-dimensional array", which describes the storage and not the purpose. | **rules table** |
| **`2DA V2.b`** | The compiled binary form. The only form that ships. | **compiled table** |
| **TLK** | Every display string in the game, in one numbered array. "Talk table" is a conversation-era name for something that also holds item names, GUI labels and journal text. | **string table** |

## Identifiers and reference mechanisms

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **StrRef** | An index into the one global string array. Not a reference to a string — a *position* in a file. | **string index** |
| **row index** | The primary way anything points at a table row. Carries no type, no bounds, no name. | **table position** |
| **`label`** | A human-readable name for a row that the engine mostly does not use for lookup. | **row name** — and it is documentation, not a key |
| **row label** (the stored one) | A second name field, usually just the decimal index, occasionally meaningful, never unique-checked. | **row tag** — see `FLAWS.md` F20 |
| **`****`** | A text-source convention for "deliberately blank" that does not survive compilation. | **(nothing — it does not exist in shipped data)** |
| **class prefix** (`sol_`, `jgd_`, `drx_`) | The real identifier of a class in five tables, declared nowhere. | **undeclared class key** — see `FLAWS.md` F15 |

## Tables worth renaming

| KOTOR's name | What it actually is | A clearer name |
|---|---|---|
| **`classes.2da`** | The class list — but the *properties* of a class are spread across column families in five other tables. | **class roster** — it is a roster, not a definition |
| **`skills.2da`** | Eight skills, plus a per-class availability and recommendation matrix bolted on as columns. | **skill roster + class-skill matrix** (two things in one file) |
| **`feat.2da`** | Every feat, plus a per-class availability / grant-level / recommendation-rank matrix as columns. | **feat roster + class-feat matrix** |
| **`featgain.2da`** | 97% per-class columns indexed by level. It is a class × level table, not a feat table. | **feats-per-level by class** |
| **`spells.2da`** | Force powers. Named `spells` from the D&D ancestor; the game never says "spell". | **force power roster** |
| **`acbonus.2da`** | Defence bonus by class by level. Rows are levels, columns are classes; neither axis is named in the file. | **defence-by-level table** |
| **`cls_atk_1/2/3`** | Attack progression. A single `bab` column where the row index *is* the level. Three tables because there are three progression rates. | **attack progression (fast / medium / slow)** |
| **`cls_st_*`** | Saving-throw progression, one table per class. | **save progression** |
| **`repute.2da`** | A square faction-versus-faction matrix, positional on both axes. | **faction relationship matrix** |
| **`globalcat.2da`** | The declaration list for every global variable a script may use. Not a category table. | **global variable declarations** |
| **`pack*` tables** (155 in K2) | One table per class per variant, holding starting equipment or feat lists. | **class package** |
| **`appearance.2da`** | Every creature body — models, textures, movement, sounds. The largest table in either game. | **creature body catalogue** |
| **`baseitems.2da`** | The item *kinds* (blaster, robe, grenade), not the items themselves. | **item category table** |

## Terms worth *not* carrying forward

**"2DA."** It names the storage shape, not the role. Everything in the layer is
a rules table; calling them all "two-dimensional arrays" told nobody anything
and made 633 files look interchangeable when they are not.

**"StrRef."** It implies a reference to a string. It is an index into one
game-global array, and that is exactly the property that makes it a problem
(`FLAWS.md` F23). Naming it `string index` keeps the coupling visible.

**"label" as a key.** In KOTOR a `label` is documentation — the engine addresses
rows by position. Any format we write should not have a name field that looks
like a key and is not one.

**Treating the class prefix as a naming convention.** `sol_`, `jgd_`, `drx_` are
load-bearing identifiers with no declaration. If our format has per-class data,
it should be rows keyed on a class id, not columns keyed on a substring.
