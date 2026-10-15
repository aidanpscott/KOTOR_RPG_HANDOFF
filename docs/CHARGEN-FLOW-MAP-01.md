# CHARGEN-FLOW-MAP-01 — how character creation connects

**Purpose.** A build-facing map of every screen, every transition, and every conditional in character creation and level-up. Written for whoever implements this. Rulings are cited so the reasoning is one lookup away; this document does not restate it.

**Read the arrows as "leads to". Read `⇢` as "conditional — see the gate".**

---

## 1 · The spine — `PT-2752` (2026-10-15), chargen rebuilt 1:1 with K2

```
Campaign package selected
  ↓
NEW GAME
  ↓
ENTRY SCREEN (K2's qorcpnl_p) ──────────── PT-1221, PT-2752 R-a/R-e
  ├─ Quick Character   →  PRE-HUB → hub: Gender, Portrait, Name, Play   (built after Recommended works, Y5)
  ├─ Custom Character  →  PRE-HUB → the full hub
  └─ Premade           →  PREMADE ROSTER  →  PLAY
  ↓
PRE-HUB (no step strip drawn) ─────────── PT-1220
  1. SPECIES                              PT-1233, PT-1235
       ⇢ subrace/chassis picker, 7 species  PT-1182
  2. MODEL   ⇢ droids only                PT-1222
  3. CLASS   "Choose your class" (32160)  PT-1240 — class only, no gender pairs (PT-2752 R-b)
  ↓  straight in: no SPECIES AND CLASS screen (PT-2752 R-d)
HUB — K2's maincg_p + custpnl_p ───────── PT-1215, PT-1216, PT-2752 Y1
  ↓
  the steps below, then PLAY.  Back → Class (species kept) · Cancel → Entry
```

**Why the pre-hub exists.** The strip cannot render honestly until it knows two facts: whether the character is a droid, and whether the class grants Force powers. Both change which steps exist. Choosing them first means the strip is correct on its first draw rather than reshaping under the player. `PT-1220`.

---

## 2 · The hub steps, and what gates each — `PT-2752`'s order

| # | Screen | Renders when | Ruling |
|---|---|---|---|
| 1 | **Gender** / **Voice** | organic → `GENDER` (Male 358 / Female 359); Assassin/Battle → `VOICE` (Masculine / Feminine / Neither, `PT-1190`); Astromech/Remote → **absent**. First, so the portrait filter has the gender | `PT-1236`, `PT-2752` R-b |
| 2 | **Portrait** | always — K2's `portcust_p`; chosen once, never changed later | `PT-2751` (R4) |
| 3 | **Origin** | organic only — world (Aptitude) → upbringing | `PT-1234`, `PT-1222`, `PT-2752` |
| 4 | **Background** | always; droids get **Programming** in place of Profession and no Lifestyle | `PT-1239`, `PT-1206`, `PT-1848` |
| 5 | **Attributes** | always (K2's 209; it read Abilities) | `PT-1227`, `PT-1229`, `PT-2752` |
| 6 | **Skills** | always — K2's rows with a Description pane | `PT-1227`, `PT-1230`, `PT-2752` |
| 7 | **Feats** | always | `PT-1228` |
| 8 | **Powers** | **only if the class grants Force powers**; after Feats until the K2 capture says where K2 asks (R-g) | `PT-1232`, `PT-1099`, `PT-2752` R-g |
| 9 | **Equipment** | always | `PT-1241` |
| 10 | **Name** | always — K2's `name_p` popup over the hub, Random Name; Story is its second panel | `PT-2752` R-c, R-h (supersedes `PT-1732`) |
| — | **Play** | unlocked only when every step is complete | `PT-1216` |

---

## 3 · Multi-stage steps

**The panel transitions in place; it is not a new screen.**

```
ORIGIN        world (Aptitude)  →  [Upbringing ▸]  →  upbringing        PT-1212
NAME          name  →  [Story ▸]  →  story   (inside the name_p popup)   PT-1243, PT-2752 R-h
BACKGROUND    profession — ONE tab, not two ⚠ PT-1401                    PT-1239
```

Origin and Name carry a **back control inside the step** — `◂ change world`, `BACK` — which returns to the earlier stage without leaving the step or losing state. Their labels wait on the owner's names list (`PT-2752` item 3).

---

## ⚠ 4a · THE SECOND BACKWARDS DEPENDENCY — `PT-1405`

**`§4` draws `FEATS → aptitude`, calls `SKILLS` terminal in the same block, and names ONE backwards dependency.** **⚠ `Skill Focus` is a second, and nothing ruled it.**

**It grants aptitude — *"1 point per rank instead of 2"* — which is a SKILLS input arriving at step 6, after Skills was priced at step 5.**

> **⚠ RULED THE SAME WAY `PT-1200` RULED THE FIRST: forward-looking. The aptitude applies from level 2. Skills are NOT repriced.**

**Why that rather than a reprice:** `§5`'s unlock is sequential and re-opening a completed step **re-locks everything after it and discards it.** A feat that repriced Skills would **force a step to re-open itself from a later step** — and `PT-1200` already refused that shape once, on `Equipment` reaching back to `Backstory`.

**⚠ And a second reason `Skill Focus` cannot be offered at all today:** `SKILLS-01 §12` says **twenty-three exist, one per skill**, and the library holds **ONE generic record with no skill on it.** **There is nothing to name.** The dependency ruling stands for when there is.

---

## ⚠ 3a · LIFESTYLE AND PROFESSION ARE ONE FIELD — `PT-1401`

**`§3` said Backstory was `profession ⇄ lifestyle`, two tabs. `PT-1400`'s successor stop found there is no lifestyle roster, and `PROFESSIONS-01` states the question outright as unsettled.**

**⚠ Checked, and the data answers it. Each of the 28 records carries BOTH:**

| | `grant` | `teaches` |
|---|---|---|
| **Merchant** | *a tier above* | `Appraise` |
| **Hermit** | *one item, NO CREDITS* | `Botany` |
| **Courtesan** | *credits* | `Persuade` |

**`CHARACTER-CREATION-01`: *"lifestyle touches starting credits, not aptitude."* That is the `grant` column. The `teaches` column is the aptitude.** **⚠ Both are on the same record, so the two words name two HALVES OF ONE CHOICE, not two choices.**

> **Backstory is ONE tab for an organic and one for a droid. There is no second roster and there never was.**

**⚠ And `PROFESSIONS-01` headed its own 28 rows "Lifestyle" while the file is called professions** — which is why this read as two things. **One field, two names, and the vocabulary collision is the whole of it.** Same shape as `PT-1331`'s role-versus-tag.

**A droid gets `programming` in the same single tab**, and `PT-692`'s *"NOT SOME. NOT CHASSIS-DEPENDENT. NONE."* is now a statement about a tab that does not exist for anyone.

---

## 4 · The dependency graph — what feeds what

This is the part that matters most for implementation. **An arrow means the source must resolve before the target can render correctly.**

```
SPECIES ──┬─→ subrace/chassis      resolves ability, skills, senses, trait
          ├─→ MODEL menu            droid only; DROID-MODELS-01 is keyed by chassis
          ├─→ ORIGIN world list     cardinality band, D-CARD-01
          ├─→ GENDER branch         vocabulator or not
          └─→ ability starting values

CLASS ────┬─→ POWERS step exists?   Force-granting or not
          ├─→ skill point budget
          ├─→ aptitude set          which skills are class skills
          ├─→ feat availability     <cls>_list = 1
          ├─→ recommendation order  <cls>_recom, ranked
          └─→ priority abilities    shown on the Attributes screen

ORIGIN ───→ aptitude #1             the world's four-skill menu ⚠ `PT-1396`

BACKSTORY ┬─→ aptitude #2           conditional, PT-695
          └─→ starting item offer   resolved at EQUIPMENT, not here

ABILITIES ─→ skill point total      Int modifier

SKILLS ────→ nothing downstream     terminal

FEATS ─────→ aptitude               Skill Focus feats, SKILLS-01 §11.2

EQUIPMENT ─→ resolves BACKSTORY's item-or-aptitude trade   PT-1217, PT-1223

NAME (Story) ──→ story text becomes engine input   PT-1243
```

**⚠ The one backwards dependency.** Backstory offers an item *or* an aptitude, and the choice resolves at Equipment — after skill points are spent. Ruled **forward-looking** at `PT-1200`: the aptitude applies from level 2, and the Equipment screen must say so. Do not reprice skills.

---

## 5 · Progressive unlock

**The strip is a hub, not a wizard.** `PT-1100`, `PT-1215`.

```
completed   grey disc, tick        revisitable
next        teal disc, PULSING     the encouraged step
current     bone disc              being viewed
locked      padlock                name still readable
PLAY        amber disc             pulses when every step is done
```

**Re-opening a completed step re-locks everything after it**, and **must warn first, naming what will be discarded.** `PT-1215`. NWN discards silently; we do not.

---

## 6 · Popups — three kinds, do not conflate

| Kind | Fires | Content | Ruling |
|---|---|---|---|
| **Explanatory** | first entry to a screen, **once ever** | teaches the mechanic; own glyph per screen | `PT-1230`, `PT-1235` |
| **Grant** | any level that grants something | *"You have been granted the following feat(s) this level"* | `PT-1228`, `TRACE-79` |
| **Recommendation** | `RECOMMENDED` pressed | *"The following feat(s) have been recommended"* | `PT-1228` |

**Glyphs so far:** `?` figure = attributes · hand = skills · globe = origin · standing figure = species.

**⚠ `RECOMMENDED` splits.** Attributes and skills apply **silently**; feats and powers **announce**. Not arbitrary — the strings exist for feats and powers only. **The rule: a popup announces what you might not otherwise notice.** `TRACE-79`.

---

## 7 · Level-up — same screens, different budgets

```
CHARACTER SHEET
  portrait carries a level-up arrow badge when a level is available   TRACE-78
  ↓  [Level Up]  or  [Auto Level Up]
CLASS  ← ours, not the source's; MULTICLASS-01 allows any class at any level-up
  ↓
LEVEL-UP HUB  =  leveluppnl_p overlaid on maincg_p                    TRACE-78
  portrait · name · class · level · eleven-row stat table · 3D model
  ↓
  Attributes ⇢ every 4th level
  Skills     always
  Feats      ⇢ class's featgain schedule — wildly non-uniform
  Powers     ⇢ Force class only
  Accept     locked until the rest are done
  ↓
GRANT SUMMARY popup  →  next level
```

**No new screens.** Attributes, Skills and Feats reuse the chargen panels exactly; only Powers has a level-up-specific panel, because KOTOR has no Force class at level 1. `TRACE-77`.

---

## 8 · The frame — applied by fit, not by rule

**Governing test: the frame fits when a screen is list-plus-detail with no dominant visual.** `PT-1242`.

| Treatment | Screens |
|---|---|
| **Full frame** | Attributes, Skills, Feats, Powers, Class, Equipment |
| **Hybrid** | Species, Origin — frame crowded the visual element |
| **Header bars only** | Gender — too little content to frame |
| **Popup over the hub** | Name — K2's `name_p` (`PT-2752` R-c) |

**House constants across all of them:** two stacked header bars · **rounded option boxes for every selectable entry** (`PT-1239`) · dim olive lowercase section labels · **amber marks the privileged member of a set** — aptitude, priority ability, granted item · `CANCEL` / `OK` footer.

---

## 9 · Open items a builder will hit

- **Feat and power icon cells are unmeasured.** Real geometry is 85.7×56 in a 257×56 row, 4px padding. Mockups use square cells. `PT-1202`.
- ~~Ability generation is unruled~~ **Closed at `PT-1260`:** all six start at **8**, **30-point** budget, ladder 1/2/3 per step, ceiling **18**. Droids are excluded — their scores come from chassis and model.
- **The organic Scavenger's component count does not exist** in the corpus. `PT-1219`.
- **Whether all 47 species carry a senses line is unestablished.** Four confirmed. Blocks five surfaces. `PT-1238`.
- ~~`dialog.tlk` is not held~~ **It is now** (`scripts/tlk.py`, K2 and K1): `PT-2752` read every chargen strref from it.
- **Authored `.gui` colour is intent, not output** — the engine repaints at runtime. Do not trust parsed colour values. `TRACE-69`, `TRACE-70`.
