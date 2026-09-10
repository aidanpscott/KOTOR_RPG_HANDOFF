# STUDY 27 — `PerceptionRange`, the last source

**Files only. Both games. `.utc` blueprints, palette and modules, 4,397 creatures.**

---

## ⚠⚠ IT IS NOT A THIRD NEGATIVE. THE GAMES MODEL BOTH SIGHT AND HEARING, IN METRES.

**RCR has no sight range, no hearing range, no droid perception rule, and no
`Spot` or `Listen` skill. The games have all four.**

> **A creature in KOTOR has a sight distance and a separate hearing distance,
> both in metres, both authored per blueprint.**
> **The default is 20 m sight / 20 m hearing.**

**So the owner is not ruling into silence.** Every number below is attested.

---

## 1 · IT IS AN INDEX, AND THE TABLE IS `ranges.2da`

**`PerceptionRange` holds a small integer — 8, 9, 10 or 11 — not a distance.**
Those are **row indices into `ranges.2da`**, the same table weapon and spell
ranges use. `acbonus` answered defence by naming a *column*; this names a *row*.

| row | label | primary | secondary |
|---|---|---|---|
| 8 | `PercepRngShrt` | **10** | **10** |
| 9 | `PercepRngMed` | **20** | **20** |
| 10 | `PercepRngLng` | **35** | **20** |
| 11 | `PercepRngDefault` | **20** | **20** |
| 12 | `PercepRngPlayer` | **250** | 20 |
| 13 | `PercepRngMonster` | 28 | 15 |

**⚠ Byte-identical between K1 and K2.**

### ⚠⚠ primary = SIGHT, secondary = HEARING — established three ways

1. **The Percep rows are the ONLY rows in `ranges.2da` with a second value.**
   Every `SpellRng*` and `WeaponRng*` row has `secondaryrange` empty — in **NWN**,
   literally `****`. A perception range is the only kind that needs two numbers.
2. **The engine has separate states for them**, in *both* games' `nwscript.nss`:
   `PERCEPTION_SEEN_AND_HEARD` · `PERCEPTION_HEARD_AND_NOT_SEEN` ·
   `PERCEPTION_SEEN_AND_NOT_HEARD` · `PERCEPTION_NOT_HEARD` — 8 constants.
3. **KOTOR ships the query functions:** `GetObjectSeen`, **`GetObjectHeard`**,
   `GetLastPerceptionSeen`, **`GetLastPerceptionHeard`**, `GetLastPerceived`.

**And the values corroborate the reading:** `Lng` is **35 sight / 20 hearing** —
sharpened eyes, ordinary ears. `Shrt` is 10/10. **Nothing has hearing greater
than sight.**

---

## 2 · HOW MANY VALUES SHIP — AND TWO ROWS NOTHING SELECTS

**4,397 creature blueprints parsed** (palette + every module archive, both games).

| | K1 (2,656) | K2 (1,741) |
|---|---|---|
| `11` default — **20 m** | **2,599** | **1,713** |
| `10` long — **35 m** | 32 | 22 |
| `9` medium — 20 m | 19 | **0** |
| `8` short — **10 m** | 3 | 6 |
| field absent | 2 | 0 |
| `12` player · `13` monster | **0** | **0** |

**⚠ `PercepRngPlayer` (250 m) and `PercepRngMonster` (28/15) are referenced by
NO creature in either game.** Same shape as `CLS_ATK_3` and the RancorCorpse
rows: **populated table rows nothing selects.** *(The player's 250 m is presumably
applied by the engine to the PC, not through a blueprint — not verified.)*

**⚠ And row 9 is mechanically identical to row 11 — both `20/20`.** The 19 K1
creatures set to "Medium" get exactly the default. **A distinct authored value
that changes nothing.**

> **So there are FOUR selectable rows and THREE effective distances: 10 m, 20 m,
> 35 m — and 97.8% (K1) / 98.4% (K2) of all creatures sit on 20 m.**

---

## 3 · ⚠⚠ IT CLUSTERS BY NEITHER SPECIES NOR ROLE-AS-A-RULE — IT IS SET DRESSING

**KOTOR has exactly two races** — `racialtypes.2da` rows 5 `Droid` and 6 `Human`,
**rows 0–4 blank**. So the owner's organic/droid question maps precisely onto this
field.

| | non-default | total | rate |
|---|---|---|---|
| **K1 Droid** | 9 | 379 | **2.4%** |
| **K1 Human** | 45 | 2,098 | **2.1%** |
| **K2 Droid** | 6 | 286 | **2.1%** |
| **K2 Human** | 22 | 1,455 | **1.5%** |

> **⚠ Droids and organics are statistically indistinguishable, in both games.**
> **There is no droid perception rule in KOTOR, exactly as there is none in RCR.**

**And what the 2% actually are, named:** the 35 m creatures are the **Taris duel
ring** — `Bendakstar021`, `DeadeyeDun021`, `GerlonTwof021`, `Ice021` — plus
**Darth Malak**, the **Korriban bridge guards** (`kor37_bridge1–4`), and a
**gizka**. The 10 m creatures are `kor33_yuthura`, `tar02_larrim`, and
`kor38b_tuksleep` — *a sleeping Tusken*.

**⚠ That is per-encounter authoring, not a rule.** A duellist in a ring notices
you sooner; a sleeping man notices you later. **Both races appear at both
non-default values** — `kor37_bridge1–4` are Droids on 35 m, `ldr_asndrd` is a
Droid on 20 m, the duellists are Human on 35 m.

---

## 4 · ⚠ THE GAMES ANSWER THE OWNER'S EXPECTATION — AGAINST IT

> The owner expects organics and droids to differ. **RCR contradicts it by
> silence. The games contradict it with data.**

**KOTOR had the field, had the two races, had 4,397 chances, and used it to
distinguish droids from organics zero times.** That is stronger than RCR's
silence: **a system that could have said so and did not.**

**⚠ And it does not support RCR's direction either.** RCR's implication — that a
droid perceives *worse*, having no darkvision and no `Awareness` — is equally
absent. **KOTOR's droids see exactly as far as its humans.**

---

## 5 · KOTOR vs NWN — INHERITED VERBATIM EXCEPT TWO ROWS

**`TRACE-107`'s method, and it lands cleanly.**

| row | NWN | KOTOR |
|---|---|---|
| `PercepRngShrt` | 10 / 10 | 10 / 10 |
| `PercepRngMed` | 20 / 20 | 20 / 20 |
| `PercepRngLng` | 35 / 20 | 35 / 20 |
| **`PercepRngDefault`** | ⚠ **`****` / `****`** | ⚠ **20 / 20** |
| **`PercepRngPlayer`** | 35 / 20 | ⚠ **250 / 20** |
| `PercepRngMonster` | 28 / 15 | 28 / 15 |

**Two changes, and both are decisions:**

* **NWN's default row is EMPTY; KOTOR filled it with 20/20.** ⚠ **And KOTOR then
  put 97.8% of its creatures on that row.** The row NWN left blank is the one
  KOTOR runs on.
* **The player's sight went 35 m → 250 m — seven times.** Hearing stayed at 20.
  **A KOTOR player sees a very long way and hears no better than anyone.**

---

## 6 · K1 vs K2 — THEY AGREE, AND THAT IS WORTH STATING

`PT-1544` warned that *"K1 is the only fact"* has already been wrong once, on
defence. **Checked, and here it does not repeat.**

**The `ranges.2da` Percep rows are byte-identical.** The only difference is
usage: **K2 stopped using row 9 entirely** (19 → 0), which changes nothing
because row 9 equalled the default anyway. **No K2 elaboration, no K2
flattening.**

---

## 7 · Two anomalies in the race field

| | |
|---|---|
| **`Race = 2`, 178 creatures** | ⚠ **`racialtypes.2da` row 2 is BLANK.** Includes `c_drdg` and `c_sebulba` in the palette, and Admiral Saul Karath and the `stunt12_*` soldiers in cutscene modules. **A value used as a key that resolves to an empty row** — this project's recurring shape, in the source game. |
| **`Race = 8`, 1 creature** | ⚠ **Out of range — the table has 7 rows (0–6).** It is `partymember`, tag **`SWDWEEB`**, in the K1 palette. **A developer placeholder shipped at retail.** |

**Neither affects §3:** both were counted separately and neither sits at a
non-default perception value except 2 blueprints where the field is absent
altogether.

---

## 8 · PT-1496 — the four questions

1. **What did they do?** Gave every creature a pointer to one of six named
   perception rows, each carrying a **sight** distance and a **hearing** distance
   in metres — then put 97.8% of creatures on a single row and used the rest for
   about fifty hand-placed set-pieces.
2. **Why?** Because perception in a real-time game is an **AI trigger**, not a
   player-facing rule. It answers *"has this guard noticed you yet"*, which needs
   one good default and a per-encounter override for the handful of moments where
   the designer wants a duellist alert or a sentry asleep. **A per-species table
   would buy nothing an author could use.**
3. **Does the reason still hold for us?** ⚠ **Partly, and the divergence is
   sharp.** We are turn-based on a grid, so noticing is not a continuous AI poll —
   it is a thing that happens on someone's turn, at a countable distance. **The
   reason KOTOR needed only one number is that its check ran every frame; ours
   runs once per turn and can therefore afford to be read by a player.** But
   KOTOR's answer to *who differs* transfers exactly: **almost nobody.**
4. **What is the modern form?** **A named row, not a number on the creature** —
   `Alert` / `Default` / `Asleep`, pointing at a shared definition, so a hundred
   creatures share one and the author changes it once. **Carry sight and hearing
   separately**, because the engine already distinguishes them and because *heard
   but not seen* is the interesting state. ⚠ **And default nearly everything**:
   KOTOR's 2% is the evidence that per-creature perception is an authoring tool,
   not a stat.

---

## 9 · What was NOT checked — scoped

* **RCR was not read.** Its silence is the Extractor's finding, quoted.
* **⚠ The sight/hearing reading is INFERRED, not documented.** No file labels
  `primaryrange` as sight. The three supports in `§1` are strong and convergent
  but **BioWare never wrote it down in anything read here.** The alternative
  reading — primary is a "notice" radius and secondary a "lose track" radius —
  **was not excluded.**
* **What consumes `PerceptionRange` at runtime was not traced.** Whether the
  engine modifies it by Stealth, light, or `Awareness` is unexamined; `k_ai_master`
  and `k_inc_generic` were not searched for perception logic.
* **The 250 m player row is unattributed.** No `.utc` selects row 12, so *how* the
  PC gets it is unverified — it may be engine-hardcoded or set elsewhere.
* **GIT instances were not re-checked** — `STUDY 24` established a KOTOR GIT
  carries only `TemplateResRef` and position, so a placed creature cannot
  override `PerceptionRange`. **That finding is relied on here rather than
  repeated.**
* **K2 module coverage is lower than K1's** (1,741 vs 2,656 blueprints) because
  K2 ships fewer creature blueprints in its archives; **no K2 module was skipped
  deliberately**, but the totals are not comparable as populations.
* **`Awareness` as a skill was not cross-referenced** against perception in
  either game.
