# TO MAIN — from AUTHOR. ⚠ STOP on Chapter Three's catalogue. The base ranged-weapon dice do not match K1's raw data, and two of my own approved chapters are implicated.

**`PT-1349` stop: recording the finding and handing back a prompt rather than resolving it.
This touches owner rulings and two approved chapters, so it is not mine to decide.**

**I did not write the catalogue.** Its families are defined by exactly the stat lines in
question, so drafting 172 rows now would propagate whatever is wrong at scale.

---

## What I was doing

Starting Chapter Three's family catalogue — 94 pistols, 78 rifles — organised Base versus
Advanced by tier, matching Chapter Two's eleven families.

**First step was grouping the 172 rows into families.** Because *"resref stem is not a
reliable proxy for base weapon type in either direction"* is already established here, I
grouped by the stat line instead, then checked the resulting families against the base
table. **The stat lines partition perfectly** — 94 and 78, no leftovers:

| Pistols | n | Rifles | n |
|---|---|---|---|
| `1d8, 20 ×2` → Blaster Pistol | 36 | `1d12, 19–20 ×2` → Blaster Rifle | 21 |
| `1d10, 20 ×2` → Heavy Blaster | 20 | `1d12, 20 ×2` → Blaster Carbine | 18 |
| `1d4, 19–20 ×2` → Hold Out Blaster | 12 | `1d10, 20 ×3` → Ion Rifle | 13 |
| `1d4, 20 ×2` → Sonic Pistol | 10 | `1d10, 20 ×2` → Sonic Rifle | 10 |
| `1d6, 18–20 ×2` → Disruptor Pistol | 9 | `1d10, 19–20 ×3` → Bowcaster | 8 |
| `1d6, 20 ×3` → Ion Blaster | 7 | `1d10, 18–20 ×2` → Disruptor Rifle | 7 |
| | | `1d10, 19–20 ×2` → Marksman Rifle | 1 |

**The structure is ready to write.** Then I checked the families against the raw `.2da`, as
Chapter Four's method requires, and stopped.

---

## ⚠⚠ FINDING 1 — K1's raw `baseitems.2da` disagrees with the base table on most ranged weapons

**Read directly from `data/2da/k1/k1_baseitems.2da`, which is plain text**, with the column
mapping validated against weapons whose values are already settled (Quarterstaff `1d6`
threat-20 ×2 — matches Chapter Two exactly).

| Weapon | **K1 raw `.2da`** | `EQUIPMENT-01` / Chapter Three | Agrees? |
|---|---|---|---|
| Hold Out Blaster | **1d4**, 19–20, ×2 | 1d4, 19–20 | ✔ |
| Sonic Pistol | **1d4**, 20, ×2 | 1d4, 20 | ✔ |
| Bowcaster | **1d10**, 19–20, ×2 | 1d10, 19–20 | ✔ |
| **Blaster Pistol** | **1d6**, 20, ×2 | **1d8**, 20 | **✗ one die step** |
| **Heavy Blaster** | **1d8**, 20, ×2 | **1d10**, 20 | **✗ one die step** |
| **Ion Blaster** | **1d4**, 20, **×2** | **1d6** +1d10 vs droid, 20 · **×3** | **✗ die and multiplier** |
| **Ion Rifle** | **1d6**, 20, **×2** | **1d10**, 20 · **×3** | **✗ two die steps and multiplier** |
| **Sonic Rifle** | **1d6**, 20, ×2 | **1d10**, 20 | **✗ two die steps** |
| **Blaster Carbine** | **1d8**, **19–20**, ×2 | **1d12**, **20** | **✗ die and threat** |
| **Blaster Rifle** | **1d8**, 19–20, ×2 | **1d12**, 19–20 | **✗ two die steps** |

**The three that agree are the three nobody bumped.** Every disagreement runs the same
direction — the table is higher than K1's data, by one or two die steps.

### ⚠ This is Chapter Four's lightsaber finding, at ten times the scale

Chapter Four established, and MAIN approved, that `EQUIPMENT-01 §4b`'s stated K1 lightsaber
die was wrong against the raw `.2da`, and that **`ITEMS-01`'s `K2+K1` tag does not mean the
two games share a value** — it can mean only one game's number was recorded.

**`§4b` itself says why this shape exists:** *"Confirmed from `baseitems.2da`. The games
differ — **K2 bumped every lightsaber one die step.**"* **`§4b` has separate K1 and K2
columns. The ranged-weapon table has one column and no K1/K2 split at all.**

**And `ITEMS-01` tags items `K1` while carrying the higher numbers** — `g_w_blstrpstl001`,
tagged `K1`, listed at `1d8` where K1's own base row says `1d6`.

### ⚠ `EQUIPMENT-01`'s own prose contains a corroborating fossil

Its ceiling note reads: *"A base blaster pistol averages 4.5 damage (`1d8`)… **⚠ The pistol
figure here read `3.5` before this correction — `1d6`'s average, not `1d8`'s** — and
appears to have gone stale independently."*

**`3.5` is `1d6`'s average, and `1d6` is exactly what K1's raw data says the Blaster Pistol
is.** The older prose figure agrees with K1's raw data; the "correction" moved it away.
**That does not prove the correction was wrong** — but it is the second independent sign
pointing the same way, and Chapter Three currently carries the corrected figure.

---

## ⚠⚠ FINDING 2 — `k2_baseitems.2da` cannot be read, and Chapter Four says it was

**`data/2da/k2/k2_baseitems.2da` has a plain-text header and a BINARY body.** Line 0 is
`2DA V2.b`, line 1 is a proper 166-column tab-separated header, and **every data row from
line 2 on is binary** — index-encoded bytes, not text. Verified with `od`; the file greps
clean for `Blaster_Pistol` because the string is not there to find.

**So no K2 base-item value can be read from that file without a 2da binary decoder.**

**⚠ Chapter Four states:** *"K2's row 8 in `k2_baseitems.2da` confirms `2d10`, matching
`EQUIPMENT-01`'s stated K2 value exactly."* **That check cannot have been run against this
file as it stands.** Either it was done against a copy that is no longer here, or the
claim is stronger than what was actually verified.

**That is a defect in my own approved chapter and I am reporting it as such.** The K1
correction Chapter Four makes is unaffected — `k1_baseitems.2da` is genuinely readable and
I re-read it today. **Only the K2 half of that chapter's claim is in question.**

---

## Why I stopped instead of writing the catalogue

**Every family in the catalogue is defined by the stat line in question.** Writing 172 rows
against `1d8` Blaster Pistols and `1d12` Blaster Rifles would either be right, or would
multiply a wrong base value across the largest table in the book.

**And it is entangled with owner rulings, which is the real reason this is yours:**

- **`PT-1783`** sets `Marksman Rifle` at `1d10` as *"Blaster Rifle's dice at longer
  range"*, revised down from `1d12`. **That reasoning depends on Blaster Rifle being
  `1d12`.** If the base table moves to K1's `1d8`, the ruling's own justification changes.
- **`PT-1782`**'s perception-extension ties to the range column of the same rows.
- **Chapter Three and Chapter One are both approved** and both state these values.

---

## What I need

**One ruling, and I do not think either answer is obvious:**

**Either — the ranged table is a deliberate conversion and K1's raw dice are not the
standard here.** Entirely legitimate: this is a d20 game, not a KOTOR emulator, and a
conversion may intentionally re-scale weapons. **If so I will write the catalogue exactly
as the families stand, and add a line to Chapter Three saying the ranged dice are converted
rather than extracted** — which it does not currently say, and which would stop the next
person repeating this check.

**Or — the table inherited K2's values the way `§4b` did, and K1 governs.** Then the base
table, the catalogue, and the affected rulings all need revising together, and **that is a
much bigger job than a chapter** — it touches `EQUIPMENT-01`, `ITEMS-01`'s 172 ranged rows,
and at least two owner rulings.

**Secondary, and smaller:** whether a readable K2 base-items source exists anywhere. If one
does, Chapter Four's K2 claim can be verified properly; if not, that claim should be
softened to what `EQUIPMENT-01` states rather than presented as a raw-file check.

**Nothing is blocked behind this except Chapter Three's catalogue.** I can move to the
Armory's four unblocked chapters or the PHB in the meantime — say which.
