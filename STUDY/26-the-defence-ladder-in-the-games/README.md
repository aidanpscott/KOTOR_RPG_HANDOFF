# STUDY 26 — the class Defence ladder, read from the games

**Files only. The third source for `CLASS-TABLES-JEDI §5A`'s empty column.**

**⚠ The Extractor's Jedi Guardian read at RCR f.60 is its work and is not touched
here.** This study reads KOTOR 1 and KOTOR 2 only.

---

## 1 · ⚠⚠ THE GAMES DO HAVE IT — AND `TRACE-85`'s "class 4" IS THIS

**`classes.2da` carries a column called `armorclasscolumn`, in both games.** It is
a *reference*, exactly like `attackbonustable` — but it names a **column**, not a
table:

| class | `attackbonustable` | `armorclasscolumn` |
|---|---|---|
| Soldier | `CLS_ATK_1` | `SOL` |
| Scoundrel | `CLS_ATK_2` | `SCD` |
| JediGuardian | `CLS_ATK_1` | `JDG` |

**Those codes are the column headers of `acbonus.2da`**, which ships in both
games. **`TRACE-85`'s *"18 = base 10 + dex mod 4 + class 4"* is a lookup into
this table** — the "class 4" is `acbonus[level][class column]`.

### ⚠ And the structure is the OPPOSITE of the attack axis

| | attack | defence |
|---|---|---|
| shape | **three tables**, `cls_atk_1/2/3` | **one table**, `acbonus` |
| selector | table **name** on the class | column **name** on the class |
| classes sharing | by pointing at the same table | by pointing at the same column |

**⚠ There is no `cls_def_*` table.** Scoped: the complete `cls_*` list is
`cls_atk_1/2/3`, `cls_spgn_jedi`, and eleven (K1) / eighteen (K2) `cls_st_*` save
tables. **Nothing else.** *(`caarmorclass.2da` is unrelated — 8 rows of armour
**body-part** codes, `NK CL FP PP SC CH ST LE`.)*

---

## 2 · ⚠⚠ K2 FLATTENED ATTACK AND DID NOT FLATTEN DEFENCE

**This inverts the expectation the brief carried, and it matters.**

`PT-72` records that **K2 gives every one of its seventeen classes `CLS_ATK_1`** —
the attack axis carries no information there. **The brief reasonably expected the
defence table to be flattened the same way.**

**It is not.** K2's seventeen classes carry **13 distinct `armorclasscolumn`
codes** — `SOL SCT SCD JDC JDS JDG SAS SLD SMA JWA JMA JWM TEC`.

> **K2 threw away the attack distinction and kept — and elaborated — the defence
> one.** K1's table is 21 rows × 6 columns; K2's is **51 rows × 13 columns.**

**So a K2 defence fact is a real fact, and this is the one axis where K2 is the
richer source.**

---

## 3 · THE LADDERS, BOTH GAMES

### K1 — 21 levels, 6 columns, **2 distinct tracks**

| columns | ladder |
|---|---|
| `scd · jdc · jds · jdg` | **+2** at L0 · **+4** at L6 · **+6** at L12 · flat to L20 |
| **`sol · sct`** | ⚠ **0 at every level** |

### K2 — 51 levels, 13 columns, **6 distinct tracks** (levels 0–49)

| columns | at L49 | cadence |
|---|---|---|
| `sas · sma · jwa · jwm` | **+20** | +2 every **5** levels |
| `scd` | **+18** | +2 every 5–6 |
| `jdc · jdg · jds` | **+18** | +2 every **6** |
| `sol` | **+16** | +2 every 5–6, ⚠ **starts at 0 and does not move until L5** |
| `jma · sld` | **+14** | +2 every **8** |
| **`sct · tec`** | ⚠ **0** | never |

### ⚠ A SHIPPED DATA DEFECT — two columns transposed in the final row

Rows 41–49 are clean. **Row 50 is not:**

```
L48-49   sld=14   sma=20
L50      sld=22   sma=14        ⚠ swapped
```

`sld` steps every 8 (next due L56) and `sma` steps every 5 (next due L50 → 22).
**`sma`'s value landed in `sld`'s column and `sld`'s in `sma`'s.** They are
**adjacent columns** (indices 7 and 8).

**⚠ Controlled:** a monotonicity sweep of all 13 columns × 51 rows finds **exactly
one decrease in the entire table** — `sma`, 20 → 14, at row 50, and nowhere else.
**A defence bonus that goes down at maximum level is not a design.**

*(Counting tracks over all 51 rows gives **8**; over 0–49 it gives **6**. The
extra two are artefacts of this one row, which is why the count above excludes
it.)*

---

## 4 · WHAT IT SETTLES, IN THE ORDER ASKED

### 1 · ⚠ Two shapes are NOT the whole system — and the reason generalises

**The games carry six distinct tracks across thirteen class columns.** So a
defence axis keyed per class does not collapse to two.

**⚠ But the transferable finding is sharper than that, and it is about sample
size:**

| roster | classes | distinct tracks |
|---|---|---|
| K1 | 6 | **2** |
| K2 | 17 | **6** |

**The same mechanism produced two tracks from six classes and six from
seventeen.** **A small roster under-counts tracks**, because tracks only become
visible when a class needs one that does not exist yet.

> **Three RCR classes yielding two curves is exactly what K1's six classes did.**
> **It is consistent with two, and equally consistent with six.** The read of a
> fourth and fifth class is what distinguishes them — which is the Extractor's
> Guardian folio, and it is the right next read.

**d20's good/average/poor convention predicts three. The games show a system of
this kind reaching six.** ⚠ **Neither number is evidence about RCR** — different
system, different increments — **but it retires the assumption that the answer is
small.**

### 2 · ⚠⚠ The `+1` offset — KOTOR CANNOT EXPRESS IT

**The Extractor found Noble `+2 → +10` and Consular `+3 → +11`: the same curve,
offset by exactly 1, and flagged its own two-instance evidence density.**

**The games settle their own half of this decisively:**

> **Every value in `acbonus.2da`, in both games, is EVEN.**
> **K1 distinct values: `0 2 4 6`. K2: `0 2 4 6 8 10 12 14 16 18 20 22`.**
> **Odd values present: NONE.**

**KOTOR's defence bonus moves in steps of 2 and never lands on an odd number**,
so a `+1` class offset is **unrepresentable** in it. Classes in KOTOR share a
column *exactly* (`jdc`, `jds` and `jdg` are byte-identical) or sit on a
different track — **there is no "same shape, one higher".**

**⚠ So the games give no support for the `+1` offset, and they are not neutral:
they positively exclude the mechanism.** If RCR's `+1` is real, **KOTOR did not
carry it across** — which is `§4.3`.

### 3 · ⚠⚠ KOTOR DID NOT ADOPT RCR'S LADDERS — AND ON ONE CLASS IT INVERTED THEM

| | RCR (per the Extractor) | KOTOR |
|---|---|---|
| Noble | `+2 → +10`, irregular, 3-then-2 hold | — no counterpart |
| **Soldier** | **`+3 → +12`, linear, +1 per 2 levels** | ⚠ **K1: ZERO at every level** |
| Jedi Consular | `+3 → +11` | K1: `+2/+4/+6`, shared with three others |
| increments | **+1** | **+2** |
| classes at zero | none | ⚠ **Soldier and Scout (K1); Scout and Tech Specialist (K2)** |

> **⚠ RCR gives the Soldier the strongest defence progression in the three read.
> K1 gives the Soldier nothing at all.** Same class, opposite treatment.

**And what KOTOR's table actually is, is legible from who gets it:** in K1 the
bonus goes to the **Scoundrel** and the three **Jedi** — the classes that fight
in light armour or none — and is denied to the **Soldier** and **Scout**.
**It reads as a light-armour compensation, not a universal defence track.** RCR's
is the opposite kind of thing: a ladder every class has some version of.

**⚠ And K2 changed its mind about the Soldier:** 0 at every level in K1, a real
track reaching **+16** in K2. **The Scout stayed at zero in both.**

---

## 5 · PT-1496 — the four questions

1. **What did they do?** Put one wide table behind a per-class *column* pointer,
   moving in steps of +2 at fixed level intervals, with **two classes given
   nothing at all** and several classes sharing a column byte-for-byte.
2. **Why?** Because in KOTOR the defence bonus is not a universal progression —
   it is **the light-armour classes' answer to armour**. A Soldier gets defence
   by wearing plating; a Scoundrel and a Jedi get it by not being hit. **Zero is
   a statement, not an omission**, which is why two columns of zeroes ship.
3. **Does the reason still hold for us?** ⚠ **The mechanism does; the assignment
   is a rules question that is not mine.** But two things transfer regardless:
   **a shared column is cheaper than a per-class ladder** — K2 expresses 17
   classes in 6 tracks — and **zero must be expressible as a value**, or a class
   that deliberately receives nothing is indistinguishable from a class nobody
   filled in. **That is this project's absence-versus-blank problem, and KOTOR
   solves it by making the column explicit rather than absent.**
4. **What is the modern form?** **A defence track is a named ladder that classes
   point at**, not a column of numbers copied per class — so two classes sharing
   a curve share it by reference and cannot drift. And **an explicit zero
   track**, so *"this class gets none"* is authored rather than missing.

---

## 6 · What was NOT checked — scoped

* **RCR was not read.** Every RCR figure here is the Extractor's, quoted. **The
  Guardian folio is theirs and was not touched.**
* **`acbonus.2da` was read for values only.** What consumes it at runtime — where
  the engine adds it, whether armour suppresses it, whether it stacks with
  Dexterity — **was not traced.** `TRACE-85`'s sum is the only attestation of use,
  and it is one observed total.
* **The column codes were mapped to classes via `classes.2da` only.** No `.utc`
  or save file was checked to confirm a character's actual bonus matches the
  table.
* **Modules and `override/` were not searched for a patched `acbonus.2da`.** K1
  ships one in `Override/` — ⚠ **`spells.2da` is loose in `swkotor/Override/`
  and `acbonus.2da` is not**, but the general precedence question was not
  re-verified for this file.
* **Rows beyond the playable cap were kept in the data and excluded from the
  track count.** K2's table runs to level 50; whether the game ever reads row 50
  was not established — **which is likely why the transposition survived.**
* **Only `acbonus` and `caarmorclass` were examined.** A defence contribution
  living in `feat.2da`, a class feature, or `k_inc_*` script was **not** searched
  for, so *"the class ladder is `acbonus`"* is a statement about the class axis,
  **not a claim that nothing else adds defence.**
