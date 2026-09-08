# 12 · Import, the import question answered, and the Equipment stop

**`KOTOR-RPG-APP` `251fb66`.** 134 tests pass, analyze clean. **Step 8 stopped.
Nothing was extracted from either game.**

---

## ⚠ 1 · EQUIPMENT — STOPPED, and the brief is aimed at the wrong file

**`equipment.json` is not the equipment step's source.** It reads
`rules/EQUIPMENT-01.md` and is the **weapon and armour rules table** — its own
`_notes` say so: *"This is NOT an item catalogue… Item instances live in
ITEMS-01..09."* Its 34 rows carry `values[]` as an **unnamed ordered list**
because the five sections have different column sets, and **three of the 34 are
the source's own placeholders** (`Droid plating — named placeholder values`).

### The document step 8 actually needs is `STARTING-EQUIPMENT-01`

**709 lines. Status `⚠⚠ CLOSED — PT-724 – PT-779`.** It holds:

    18 ORGANIC ARRAYS · 9 DROID ARRAYS · 28 PROFESSION GRANTS
    18 Two-Weapon Fighting rows · the upgrade rule · the random rule
    THREE ROUTES — the Assortment, the Purse, and the GM decides

**⚠ It is the source of no extract.** Sixteen extract files; not one reads it.
Nor does any read `ITEMS-01..09`.

### Why the `PT-1200` boxes still cannot be clicked

`PT-1200` resolves the profession's offer at Equipment **"once the item's worth
is visible beside the rest of your gear."** Neither half exists as data:

| | |
|---|---|
| **the item's worth** | Costs live in `ITEMS-01..09`'s `Cost` column — **unextracted** |
| **the rest of your gear** | The arrays live in `STARTING-EQUIPMENT-01` — **unextracted** |
| **the item itself** | ⚠ The grant is a **category**, not an item: *robe · gauntlets · melee weapon · a tier above*. Resolving it needs the catalogue |

> **Making the boxes clickable now would defeat the ruling's own reason for
> putting them here.** A player would choose between an unnamed item of unknown
> worth and an aptitude — which is exactly the choice `PT-1200` moved *out* of
> Backstory.

**The need:** `STARTING-EQUIPMENT-01` extracted (the arrays, the three routes,
the 28 grants) and `ITEMS-01..09`'s cost column, so an offer can be priced.

**What was NOT done:** no Equipment screen, no partial screen, and the Backstory
boxes are untouched. Step 9 is unbuilt. No character record, no save.

---

## ⚠ 2 · THE IMPORT QUESTION — the owner means ART, and the corpus says so

**The stats import already happened, and it was a conversion.**
`ITEMS-01` – `ITEMS-09` hold **1,425 distinct resrefs** across 1,251+ stated
items — `418 weapons · 173 armour · 164 upgrades · 135 droid · 241 worn · 58
usable · 20 quest · 42 other`, plus a 118-row upgrade tree — each row carrying
`Name · Resref · Src (K1/K2) · Tier · Cost · Weapon · Upgradeable · Properties`.

Every one of those files heads its conversions by ruling:

    PT-339 dice · PT-341 Massive Criticals · PT-308 tiers
    PT-327 unique · PT-345 crystals · PT-349 Upgradeable · PT-384 the feat remap

> **⚠ SO A STATS IMPORT WOULD NOT ADD THE CATALOGUE. IT WOULD OVERWRITE A
> CONVERTED ONE WITH THE GAME'S OWN BALANCE**, undoing seven named rulings. The
> owner cannot have meant that, and the evidence is in the corpus rather than in
> my judgement.

### What KOTOR's item data actually contains

Both games are installed here. Their tables of contents (`chitin.key`) read:

| | K1 | K2 |
|---|---|---|
| keyed resources | 25,836 | 18,439 |
| **`.uti` item blueprints** | **557** | **994** |

A `.uti` is a GFF record. Field by field, **almost all of it is rules**:

| Field | What it is |
|---|---|
| `BaseItem` | index into `baseitems.2da` — **weapon class, damage dice, crit, range**. Rule |
| `PropertiesList` | `itempropdef.2da` + cost tables — **the whole bonus system**. Rule |
| `Cost`, `AdditionalCost` | **economy**. Rule |
| `LocalizedName`, `DescIdentified` | `StrRef` into `dialog.tlk` — **text**, theirs |
| `ModelVariation`, `TextureVar`, `BodyVariation` | ⚠ **the only art pointers** |

**So the art is a handful of variation indices naming a texture; everything else
in the file is mechanics.** `ITEMS-01..09` is what those mechanics look like
once converted, and it is already ours.

### ⚠ And the pairing `PT-1369` demands is not one-to-one with items

**Icons are per class + variation, not per item.** K1's GUI texture pack holds
**183 `ii_*` icons across 38 classes** — `ii_belt`, `ii_mask`, `ii_datapad`,
`ii_pazcard` — against 557 blueprints. Many items share one picture.

> **So `PT-1369`'s one-to-one must be defined against ICONS, not items:** 183
> extracted pictures, 183 counterparts we made or 183 notes saying one is owed.
> Defined against items it can never balance, and a build that checks the wrong
> side would pass while owing 374 drawings.

**⚠ Scoped negative:** I found **no `ii_*` resources in K2's `chitin.key` at
all**, and this Steam Linux build's `TexturePacks/` holds only controller
overlays. **K2's item icons are not where K1's are, and I did not locate them.**
An art import's K2 coverage is unverified. Not checked: the module `.rim`/`.erf`
files, and `override/` (60 files).

### The recommendation

**Import art. Do not import stats.** `PACKAGE-FORMAT-01`'s `blueprints/items/`
lets a *package* add a sword, and that stays true — **but `base-rules` carrying
KOTOR's balance is the other thing, and it would overwrite work already done.**

---

## 3 · Import on Console Home, and as the first run

**The explanation leads with what happens if you do nothing.**

- First line: *"Everything here works right now. Nothing needs importing."*
- *"if you do not — Everything still works and looks plainer. A picture that is
  not there is drawn as a labelled placeholder, and no rule, screen or character
  depends on one."* — `PT-1368`
- *"It reads pictures only… Importing changes how things look and never what
  they do."* — `PT-1361`
- *"The artwork stays on your disk… never packaged, shared, or shipped with
  anything you make."* — `PT-1350`
- **⚠ The second button is "Continue without it", not "Skip".** Skipping implies
  something was owed.

The folder button **renders and says it is not built** rather than being hidden.
**Nothing is extracted.**

### Two choices that are mine, not a document's

| | |
|---|---|
| **A fourth corner icon** | `PT-1146` names **three** — Characters, Profile, Settings. The owner asked for Import on Console Home, and it is the only light-weight place `§0` leaves; the friends strip and the library are both spoken for |
| **Where first-run is remembered** | `Locations` names `packages/` and `saves/` and nothing else. `console/first-run.json` sits beside them because it belongs to the console, not to a package or a save |

The two acceptance walks now **mark the run seen** rather than the app bypassing
the welcome — they are the returning user's walk, and the first run is covered
on its own.
