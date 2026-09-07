# 08 · The droid Abilities close, and Skills

**`KOTOR-RPG-APP` `4ffbe26` · `MAIN_WORK` `8668390`.** 105 tests pass, analyze
clean. **One stop, and it is droids again — a different one.**

---

## `PT-1403` — the chassis spread ships, and its source is a design document

`chassis.json` → `chassis.toml`. **Seven chassis, every one totalling 72.**

| | |
|---|---|
| Derived | 4 — a chassis adjustment is authored, so the spread follows from it |
| Inferred | 3 — Labor, Protocol, Probe carry no adjustment; the spread follows from what the chassis is *for* |
| Total | 72 on all seven, matching the organic point-buy total |

> **⚠ ITS SOURCE IS A DESIGN DOCUMENT, NOT A RULES CHAPTER.** The spread was
> ruled into `design/CHARGEN-DATA-01.md`. `SPECIES-CHAPTER-v2` carries the
> chassis *records* and not the spread. So this is **its own kind** —
> `extract_chassis.py`, one source, one digest — rather than a field welded onto
> `species.json` whose fingerprint would then cover two files.

`gen_base_rules.py` now writes **12 kinds, 979 records** (up from 11 / 972).
`check_extracts.py`: **current 22, stale 0.**

> **⚠ `models.json`'s ability block is NOT this and stays an NPC statblock.**
> Those records carry CR; Labor reaches CON 22 and Battle STR 20, and an organic
> PC cannot exceed 18. Reading the model row as a PC spread would have shipped a
> droid nobody could match. They are different numbers for different purposes and
> both are correct.

---

## The droid Abilities stop is closed

A droid completes Abilities. The screen shows the chassis spread as **final
scores with no spend controls at all** — no plus, no minus, no pool.

> **⚠ THE CHASSIS ADJUSTMENT DOES NOT APPLY ON TOP.** It already shaped the
> spread. Battle's `+2 Str` is *visible in the 14*; applying it again would show
> 16. The droid's `AbilityChoice` therefore carries an empty adjustment, and that
> emptiness is the ruling, not an omission.

**I chose to say on screen which three are inferred.** The brief left it to me
and asked which I picked. Labor, Protocol and Probe carry a line naming the
spread as inferred — a player looking at 16 Charisma on a protocol droid can see
where it came from rather than assuming it was authored.

---

## Step 5 — Skills

`SKILLS-01 §9.1` and `§11.1`, `PT-1227`, `PT-1230`.

| Rule | In the screen |
|---|---|
| Budget | `(class base + Int modifier) × 4` at first level |
| Cost | **1** point per rank with aptitude, **2** without |
| Cap | **4** with aptitude, **2** without, at level 1 |
| Roster | **25**, alphabetical |

> **⚠ 25, NOT 26.** `skills.json` has 26. Fly is beast-only — `PT-554` — and is
> not on a character list. The extract is complete and the screen filters it;
> those are two different facts and both hold.

The minus renders only above zero and the plus **vanishes** at the cap rather
than greying — `PT-1227`. OK is refused until the budget is spent.

### ⚠ Aptitude is marked with its sources NAMED — `PT-1201`

Class, homeworld and profession can all land on the same skill. A tick would say
*this is cheap* and not *why*, and a player who later changes profession needs to
know whether the discount survives. So the mark reads `class · homeworld ·
profession` — every source that granted it, listed.

The chain is assembled in the hub from the three places that own it: the class
record's `classSkills`, Origin's four-skill menu (`PT-1396`), and the
profession's `teaches` column (`PT-1401`).

---

## ⚠ WHAT STOPPED — a droid cannot complete Skills

**`rules/DROID-SKILLS-01.md` is authored in `MAIN_WORK` and is not extracted.**

- **`§2.2`** closes Mysticism, Streetwise and one other to **every** chassis.
- **`§2.4`** says what each chassis ends up with — a per-chassis gate.

**The need:** the chassis skill gate does not exist as data. Nothing in the 22
extracts carries it.

**Why I did not offer the organic list meanwhile.** It would let a droid take
Mysticism, which `§2.2` closes outright — a wrong character the player would
have to be told to unbuild later. The screen refuses for droids and names the
document.

**What was NOT done:** I did not extract `DROID-SKILLS-01`, did not read past
what the stop needed, and did not build steps 6–9. No character record, no save.

---

## Scope of the negatives

- **"Fly is not on a character list"** — checked `skills.json` (26 records) and
  `PT-554`. Not checked: whether any *beast* screen will need it, since no beast
  screen exists.
- **"The chassis gate is not extracted"** — checked all 22 files in
  `data/extracted/`, `gen_base_rules.py`'s 12 kinds, and the shipped
  `base-rules` shelf. Not checked: `ATLAS/decisions/`, the 34 files `MAIN_WORK`
  has never read.
