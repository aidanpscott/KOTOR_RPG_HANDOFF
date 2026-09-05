# CHARACTER-RECORD-01 — what a character is, as data

**Purpose.** The contract every creation screen writes into and every later system reads from. Written because nothing specified it: eleven screens produce a character and no document said what that character *is*.

**⚠ FIRST, WHAT THIS IS NOT — reconciled with the ledger at `PT-1265`.**

`ENGINE-SPEC-01-LEDGER` rules that **state is derived by replay of an append-only event log, and state is never the primary artifact.** This document describes a character as an object with fields, which reads like the opposite. It is not.

**This record is a PROJECTION of the event log, not the store.** Creation writes *events* — a species chosen, a point spent, a feat taken. The record is what you get by replaying them. It is the shape every screen reads and every rule computes against, and it is worth specifying precisely because so much depends on its shape — but **the log is what persists.**

**Three consequences, and they are not optional:**

- **"Validate on load" means validate the projection**, after replay, not a file on disk.
- **A correction is a new event, not an edit.** Nothing rewrites history to fix a bad record.
- **Multiplayer falls out of the log's visibility sets**, not out of this document — which is why `§5` says nothing here addresses it.

**Two principles govern the whole shape.**

**Store the choice, derive the consequence.** A record holds `species: "aqualish"`, `subrace: "quara"` — it does not hold the resulting `+2 Strength`, because that is a lookup. Storing derived values means two sources of truth and one of them going stale. `SKILLS-01`'s aptitude rule changing should change every character, not none of them.

**Absent, not zeroed.** A droid has no `upbringing` key at all — not `null`, not `""`. This mirrors how every screen in the flow renders (`PT-1099`), and it makes an unset field distinguishable from a field set to nothing.

---

## 1 · The record

```json
{
  "schema": "CHARACTER-RECORD-01",
  "id": "uuid",
  "package": "the-sith-lords",

  "identity": {
    "name": "Vash Corrin",
    "portrait": { "kind": "preset", "ref": "bith_04" },
    "story": "Vash Corrin came up on Coruscant…",
    "story_origin": "generated | edited | authored"
  },

  "species": {
    "id": "bith",
    "subrace": null,
    "chassis": null,
    "model": null
  },

  "gender": "male",

  "origin": {
    "world": "coruscant",
    "world_open": null,
    "aptitude_skill": "persuade",
    "upbringing": "orphan"
  },

  "backstory": {
    "profession": "acolyte",
    "programming": null,
    "lifestyle": "destitute",
    "grant_taken": "aptitude"
  },

  "classes": [
    { "id": "jedi_sentinel", "levels": 1 }
  ],

  "abilities": { "str": 12, "dex": 14, "con": 12, "int": 13, "wis": 15, "cha": 13 },

  "skills": { "awareness": 4, "mysticism": 4, "persuade": 3, "security": 2 },

  "feats": [
    { "id": "weapon_prof_lightsaber", "source": "granted", "at_level": 1 },
    { "id": "conditioning",           "source": "chosen",  "at_level": 1 }
  ],

  "powers": [
    { "id": "force_push", "at_level": 1 }
  ],

  "equipment": {
    "route": "standard",
    "items": ["padawan_robe", "training_lightsaber", "medpac", "medpac"],
    "credits": 100
  },

  "progress": { "level": 1, "xp": 0 }
}
```

---

## 2 · Field rules

**`species`** — exactly one of `subrace` or `chassis` is non-null, and only for the species that carry them (`PT-1182`). `model` is non-null **only** when `chassis` is, and is validated against that chassis (`PT-1222` — `DROID-MODELS-01` is keyed by chassis).

**`gender`** — for a droid this holds the **voice** (`masculine`/`feminine`/`neither`). **Absent entirely** for Astromech and Remote (`PT-1190`). One field, three behaviours; the chassis tells you which.

**`origin`** — **absent entirely for droids** (`PT-1222`): the model replaced homeworld and moved pre-hub, and upbringing does not apply. For organics, `world_open` carries a free-text world when the player took the open option (`PT-1183`), in which case `world` is null and `aptitude_skill` must also be null.

**`backstory.grant_taken`** — `"item"` or `"aptitude"`, and **written by the Equipment screen, not Backstory** (`PT-1217`, `PT-1223`). Backstory shows the offer; Equipment resolves it.

**`classes`** — ordered, first entry is the class taken at level 1. **Maximum three** (`PT-723`). `levels` sums to `progress.level`.

**`abilities`** — the **final** scores, not the point-buy spend. Floor 8, ceiling 18 at level 1 (`PT-1227`).

**`skills`** — ranks only, and **only skills with a rank above zero appear**. An absent skill is rank 0. Aptitude is *not* stored — it is derived, and §3 says how.

**`feats`** — `source` distinguishes `granted` (automatic, from the class schedule) from `chosen` (spent a slot). This matters: a granted feat cannot be removed, and the distinction is what the grant popup reports (`PT-1228`, `TRACE-76`).

---

## 3 · Derived, never stored

**Recompute these. Do not persist them.**

| Value | Derived from |
|---|---|
| ability adjustments | species + subrace/chassis |
| species skill bonuses, senses, traits | species + subrace/chassis (`PT-1237`) |
| **aptitude set** | class skills + species + origin world + profession-if-taken + Skill Focus feats (`SKILLS-01 §11.2`) |
| skill rank caps | aptitude, level (`PT-1227`) |
| vitality, defence, saves, attack bonus | classes + abilities + feats |
| Force points | class + abilities |
| languages | species + programming |
| credits remaining | equipment route + lifestyle |

**⚠ The aptitude set is the one to get right.** Five sources contribute and they **stack** (`PT-1201`) — a skill can hold aptitude from class *and* species *and* homeworld. The UI names which sources granted it, so the derivation must return the **set of sources**, not a boolean.

**⚠ And it is mutable mid-campaign.** A Skill Focus feat taken at level 8 adds aptitude the character did not have at level 1 (`TRACE-68`). Any cached aptitude set invalidates on feat gain.

---

## 4 · Validation

A record is legal when all hold:

```
species exists, and subrace/chassis is present iff that species requires one
model present iff chassis present, and valid for that chassis
gender absent iff chassis is Astromech or Remote
origin absent iff droid
classes non-empty, ≤ 3 entries, levels sum to progress.level
no droid holds a Force class                                    PT-92, PT-569
abilities 8..18 at level 1
skill ranks ≤ cap for their derived aptitude
every feat with source=granted appears in that class's schedule at ≤ level
every chosen feat's prerequisites are met
powers present only if a held class grants them
backstory.grant_taken set iff a profession or programming is set
```

**⚠ Validate on load, not only on save.** A record can become illegal without being edited — a rules change to `SKILLS-01`'s caps invalidates existing characters, and silent breakage is worse than a refusal.

---

## 5 · Open

- **`story_origin`** is proposed here, not ruled. It records whether the prose was generated, edited or written from scratch, which the engine may want when mining it for hooks (`PT-1243`).
- ~~Ability generation is unruled~~ **Closed at `PT-1260`:** 30-point buy from a base of 8, ceiling 18. No rolls to store. `abilities` holds the **bought** scores; the species modifier is applied on read, per `§3`.
- **`package`** assumes campaign packages scope characters. Whether a character is portable between packages is not decided.
- **Multiplayer** — nothing here addresses whose record this is or how it syncs.
