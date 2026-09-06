# STUDY 08 — THE CONTENT CENSUS

*Focused census, out of batch order. Counts what a shipped KOTOR campaign
actually contains, and how it is named — to put a number under the one
judgement in the naming spec that had none: how deep a path should be.*

---

## 0 · ⚠ Method — what was counted, and how

**A number without its method is not evidence, so here is the boundary.**

**IN the sample**
- the BIF layer of each game, via `chitin.key`
- `modules/*.rim` and `modules/*_s.rim` (all 234 K1, 164 K2)
- `modules/*_dlg.erf` (82 K2; K1 has none — batch 1)

**OUT of the sample, and why**
- **`modules/*.mod` — all 40 in K1.** Batch 4 proved these are written by the
  running game, not shipped. Including them would mix one playthrough's
  artifacts into the corpus.
- **K1's `rims/` and `patch.erf`** — duplicate and patch layers (batch 1). Their
  contents overlap the BIF and would double-count.
- saves, `gameinprogress/`, `currentgame/` — runtime state.
- `streamwaves`/`streamvoice`, `streammusic`, `streamsounds`, `movies` — loose
  audio and video, counted separately in batch 6 and not blueprints.

**Counting rule.** Everything below counts **distinct `(resref, restype)`
pairs**, lower-cased, deduplicated across layers. Where a resource exists in both
the BIF and a module, it counts once. Occurrence counts (the same resref in
several archives) are reported separately in §4 because they are a different
finding.

**Readable names** come from resolving each blueprint's `LocalizedName`,
`FirstName`, `LocName` or `Name` through that game's TLK. **7,255 of 8,299 K1
blueprints and 4,816 of 5,797 K2 blueprints resolved**; the rest carry no name
field or an unset StrRef and are excluded from name-based analysis. That
exclusion is stated wherever it matters.

---

## 1 · The count per kind

Distinct resrefs, by layer.

```
kind                 K1 BIF   K1 mod   K1 all   K2 BIF   K2 mod   K2 all
---------------------------------------------------------------------------
UTI item                557      267      810      994      127     1114
UTC creature            205     1504     1709      284      932     1215
UTP placeable           317      821     1138      383      463      842
UTW waypoint              9     1730     1736        9      400      409
UTT trigger              21      811      832       34      312      345
UTD door                 50      423      473      104      256      360
UTS sound                 0      395      395        0      417      417
UTE encounter            65       60      125       65       40      105
UTM store                 0       38       38        0       17       17
DLG conversation         32     1016     1043       30      945      973
ARE area                  0      106      106        0       74       74
GIT instances             0      106      106        0       74       74
NCS script             1784     7254     8927      612     3006     3516
NSS source             1774        0     1774      638        0      638
2DA table               209        0      209      424        0      424
JRL journal               1        1        2        1        0        1
MDL model              2832        0     2832     3237        0     3237
WOK walkmesh           1202        0     1202     1236        0     1236
WAV audio (in BIF)     1928        0     1928     2265        0     2265
GUI panel                84        0       84      159        0      159
---------------------------------------------------------------------------
TOTAL distinct                          25,470                      17,422
```

**The direct answer to "40 weapons or 400": neither — about 250.**

```
                    K1                       K2
weapons        234  (28.9%)  31 classes   263  (23.6%)  31 classes
armour          89  (11.0%)  11 classes   102  ( 9.2%)  14 classes
other equipable 185 (22.8%)  21 classes   254  (22.8%)  17 classes
not equipable  302  (37.3%)  29 classes   495  (44.4%)  28 classes
                --------                   --------
                810                        1,114
```

*Method for that split: an item is a **weapon** if its `baseitems` row has a
non-blank `weapontype`, **armour** if it has a non-blank `armortype`, **other
equipable** if `equipableslots` is non-zero, otherwise **not equipable**.*

So the largest single category a builder would ever browse is roughly **250
weapons across 31 classes — about 8 per class.** Not 40, not 400.

---

## 2 · ⚠ How lopsided is it — much less than expected

```
                                          K1        K2
top  1 base class holds                 10.7%     14.2%
top  3                                  21.6%     27.2%
top  5                                  29.4%     ~33%
top 10                                  42.6%       —
top 20                                  59.6%       —
median items per used class                 5         —
largest single class                       87       158
base classes used exactly once        13 of 92        —
base classes with ZERO items           0 of 92   0 of 104
```

**This is a long tail, not a spike.** No category dominates: the biggest is
`Plot_Useable_Items` at 10.7% / 14.2%, and that is a catch-all rather than a
real kind. It takes **twenty** classes to reach 60% of items.

**And every base class is used.** Zero of 92 K1 rows and zero of 104 K2 rows have
no items — the categorisation BioWare defined is fully populated, with a median
of five items per class.

**By equipable slot the spread is similar:**

```
K1   (none) 37.3% · either hand 14.4% · body 12.5% · right hand 10.4%
     head 5.9% · arms 4.7% · creature wpn 4.1% · implant 2.7% · belt 2.5% …
K2   (none) 44.4% · either hand 12.5% · body 10.6% · right hand 9.3% …
```

**What this means for the spec.** A two-level path is not straining. The worst
single folder would hold 87 (K1) or 158 (K2) items, and the median folder holds
five. The failure mode a deep path guards against — a wall of 400 files in one
directory — does not occur in a shipped campaign of this size.

---

## 3 · Naming patterns in the shipped data

**⚠ Correcting the premise.** The brief said resrefs cap around 15 characters
against readable labels running to 28. Measured:

```
                       K1                    K2
resref length     min 1, max 16          min 2, max 16
                  mean 13.2              mean 11.0
at the 16 cap     2,172 blueprints       461 blueprints
readable name     min 2, max 68          min 2, max 68
                  mean 13.6              mean 17.0
```

The resref field is **16 bytes** (batch 1), not 15, and **2,172 K1 blueprints sit
exactly at the cap** — 26% of them. Readable names run to **68 characters**, not
28. So the pressure is worse than the premise assumed in both directions: the
identifier is more saturated and the names are longer.

### The prefix convention is real, weak, and inconsistent

```
share of blueprints carrying ANY  x_  prefix:    K1  28.2%    K2  58.1%
```

**K1 is not following a prefix convention** — 72% of its blueprints have none.
K2 more than doubled the adoption but still leaves 42% unprefixed.

Prefixes that do appear, K1: `g_` 10.9%, `plc_` 3.3%, `k_` 2.4%, `wp_` 2.3%,
`sta_` 1.7%, `sw_` 1.4%, `end_` 1.3%, `n_` 1.1%, `c_` 0.7%. K2 adds `u_`, `tr_`,
`a_`, `w_`, `d_`, `npc_` and reaches **113 distinct prefixes** against K1's 29.

**Consistency varies wildly by kind**, which is the more useful finding:

```
kind            K1 dominant prefix        K2 dominant prefix
item            g_        68%             (none)    21%,  g_ 20%
creature        (none)    71%             g_        27%,  n_ 22%
encounter       g_        58%             g_        63%
placeable       (none)    62%             (none)    45%,  plc_ 39%
trigger         (none)    87%             tr_       58%
waypoint        (none)    80%             wp_       63%
door            (none)    73%             (none)    57%,  sw_ 35%
conversation    (none)    87%             (none)    85%
sound           (none)    98%             (none)    94%
```

**Not one kind reaches 90% adherence in either game.** The best is K1's
encounters at 58% `g_` and K2's waypoints at 63% `wp_`. The convention exists in
the sense that a reader can see it; it does not exist in the sense that anything
could rely on it.

*Note the reversal on items: K1 was 68% `g_`, K2 dropped to 20%. The convention
got weaker for the kind that has the most instances.*

---

## 4 · ⚠ What would have collided — the number that matters

**Method.** Every blueprint whose readable name resolved. Name slugified
(lower-case, runs of non-alphanumerics to `-`, `<Token>` markup stripped). Paths
built at three depths and duplicates counted.

**Subkind honesty:** only **items** carry a categorisation field the data
supports (`baseitems` class). No other blueprint kind has one — creatures,
placeables, doors and the rest have `PaletteID`, which is a browser folder id,
not a semantic subkind. So depth 3 is meaningful for items and degenerate
elsewhere, and that is reported rather than papered over.

```
K1 — 7,255 named blueprints
  depth 1  name                  4,775 paths   2,480 collide   34.2%
  depth 2  kind/name             4,833 paths   2,422 collide   33.4%
  depth 3  kind/subkind/name     4,844 paths   2,411 collide   33.2%

K2 — 4,816 named blueprints
  depth 1  name                  4,235 paths     581 collide   12.1%
  depth 2  kind/name             4,275 paths     541 collide   11.2%
  depth 3  kind/subkind/name     4,275 paths     541 collide   11.2%
```

### ⚠ Depth is not the lever

**Going from a flat name to a three-level path removes 2.8% of K1's collisions
and 6.9% of K2's.** In K2, depth 3 removes *nothing at all* over depth 2 —
identical path count, identical collisions.

**Because the collisions are inside the leaf, not across categories:**

```
K1   door / door                        x145
     item / credits                      x49
     creature / dark-jedi                x45
     creature / sith-soldier             x38
     placeable / footlocker              x35
     waypoint / waypoint                 x29

K2   door / door                         x20
     item / credits                       x19
     item / double-bladed-lightsaber      x13
     placeable / skeletal-corpse          x13
     item / lightsaber                    x12
```

145 doors named "Door" are all doors. No amount of hierarchy separates them,
because they are genuinely the same name for genuinely different objects.

**Items alone, where a real subkind exists:**

```
K1   810 items:  flat 226 collide (27.9%)  →  class/name 215 (26.5%)
K2 1,114 items:  flat  71 collide ( 6.4%)  →  class/name  71 ( 6.4%)
```

Even with a real semantic category, adding it removes **eleven collisions out of
226** in K1 and **zero** in K2.

### The other direction — resrefs already collide, heavily

```
(resref, restype) pairs appearing in more than one module archive:
  K1  2,078      worst: "module" x117 · "invisible001" x59 · "invisible002" x31
  K2  1,658      worst: "module" x82  · "low_rumb_04_a" x65 · "newgeneric001" x59
```

**Every module's manifest is named `module`.** 117 files share that resref in K1.
The flat 16-character namespace is already saturated, and BioWare resolved it by
scoping to the archive — which is batch 3's F33 (scope is decided by file
location, not declaration).

### What this says for the spec

**Two levels is enough, and the third is not worth its cost.** The evidence:

- depth 3 buys 0.2 percentage points in K1 and **nothing** in K2;
- the residual collisions are same-name-different-thing, which needs a
  **discriminator on the leaf**, not more hierarchy;
- the median category holds five items and the worst holds 158, so no folder
  becomes unnavigable at two levels.

**The lever is a stable leaf identifier, not path depth.** A `kind/name` path
plus a short discriminator resolves the 145 doors; a `kind/subkind/name` path
without one does not.

---

## 5 · Did BioWare want more categorisation? — traces of the answer

**Yes for authoring, no for addressing, and they built it in a separate place.**

**`PaletteID` is live on every blueprint and items are by far the most
sub-categorised kind:**

```
kind          K1 distinct PaletteID    K2 distinct PaletteID
item                   16                      30
placeable              10                      11
creature                6                       7
trigger                 6                       7
encounter               5                       5
waypoint                5                       2
door                    2                       2
store         (field absent)            (field absent)
```

So the authoring tool's folder count for items **doubled between games** — 16 to
30 — while the item count grew 810 to 1,114. They wanted more buckets and added
them, **in the palette, not in the name.**

**But the shipped palette tree is shallow.** K1 ships 16 game-global `ITP` files
and K2 ships 18 — `creaturepal`/`creaturepalstd`, `itempal`/`itempalstd` and so
on, a "custom" and a "standard" tree per kind. Parsing one: **maximum nesting
depth 2, with 8–10 nodes total.**

**That is BioWare's own answer to the depth question, from the tool they used
every day: two levels, roughly ten folders.**

**And the categorisation they did build is facets, not a tree.** `baseitems.2da`
carries eight category-ish columns, most of them heavily blank:

```
itemclass        88 of 92 distinct,  1 blank    ← effectively a second label
itemtype         43 distinct,        5 blank    ← a real ~43-bucket category
invsoundtype     28 distinct,        6 blank
ammunitiontype    6 distinct,       78 blank    ← weapons only
weaponmattype     5 distinct,       74 blank    ← weapons only
weapontype        4 distinct,       61 blank    ← weapons only
armortype         3 distinct,       81 blank    ← armour only
modeltype         3 distinct,        1 blank
```

Four of the eight apply only to a subset. **An item is not in one place in a
tree; it has several orthogonal properties, most of which do not apply.**

**Abandoned grouping machinery, as the brief predicted:**

- **`masterspell`** in `spells.2da` — **one distinct value, blank on all 132 K1
  and all 282 K2 rows.** Completely dead.
- **`masterfeat`** in `feat.2da` — 4 distinct values, blank on 104 of 125 K1 rows
  and 224 of 245 K2 rows. 83% and 91% unused.
- **`category`** on feats — 4 distinct, blank on 101/125 and 221/245.
- **`toolscategories`** on feats — 6 distinct, **0 blank in both games.** The one
  grouping column that is fully populated is the one named for the *toolset*.

That last contrast is the finding: **the categorisation BioWare maintained was
the one their authoring tool consumed. The categorisation meant for the rules
engine was left to rot.**

---

## 6 · The verdict on depth

Stating it plainly, since it is what the census was for.

**Two levels. The evidence does not support a third.**

1. **Depth 3 buys almost nothing.** 2.8% fewer collisions in K1, 0% in K2.
2. **Only one blueprint kind has a real subkind at all.** Items have
   `baseitems` class; nothing else has a semantic category, only a browser
   folder id.
3. **Volume does not require it.** Median category holds 5 items, worst holds
   158, largest whole kind is ~250 weapons across 31 classes.
4. **BioWare's own tool used two levels and ~10 folders**, across two games and
   ~2,000 items.
5. **The real pressure is on the leaf, not the path.** 26% of K1 resrefs are at
   the 16-character cap, names run to 68 characters, and 2,078 resrefs already
   collide across archives.

**Where the effort should go instead:** a stable, collision-proof leaf
identifier, and a *facet* layer beside the path rather than more path. KOTOR's
items have eight overlapping category columns because an item genuinely is
several things at once — a tree cannot express that at any depth, and BioWare
did not try.

---

## 7 · Scope — what was not checked

- **Audio, video and texture assets** are excluded from every count. They were
  censused in batch 6 and are not blueprints. Including K1's 13,860 voice files
  would swamp the content figures and answer a different question.
- **`.mod` files excluded** per batch 4. If the intent were "everything on
  disk", K1's totals would rise by roughly 700 UTC occurrences and 264 NCS —
  but they would not be shipped content.
- **1,044 K1 and 981 K2 blueprints have no resolvable name** and are excluded
  from §4 entirely. They are mostly waypoints, sounds and triggers, which are
  the kinds least likely to need a readable path — so the collision figures may
  be slightly pessimistic for the corpus as a whole and are accurate for the
  content a human would browse.
- **Subkind for non-item kinds was not synthesised.** I could have used the
  containing module, or `Appearance_Type`, as a pseudo-category and generated a
  better-looking depth-3 number. That would have measured my choice of
  categoriser, not KOTOR's data.
- **No running process.** Nothing here is observed behaviour; it is all read
  from shipped files.
- **`itemclass` was not cross-tabulated** against the item counts — with 88 of
  92 distinct values it behaves as a label rather than a category, and treating
  it as one would have produced a meaningless 88-bucket histogram.
