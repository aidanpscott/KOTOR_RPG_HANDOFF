# AUTHORED-CHARACTER-01 — everyone a player did not make

**Cluster B of `RECORD-GAPS-01`.** `CHARACTER-RECORD-01` describes a character built by a player through eleven creation screens. **A campaign is mostly people nobody built that way** — a guard, a merchant, a companion, a Sith lord who has to survive act two.

**⚠ This is less new than it looked.** `BEASTS-ENTRIES-01` already specifies authored creatures and does it well. Most of this document generalises that model rather than inventing one.

---

## 1 · What we already have, and it is good

A beast entry looks like this:

```
Cannok — Scavenger · Medium · pack · paired

    Str 10  Dex 16  Con 6  Int 3  Wis 3  Cha 6
    skills     2 points per level
    attacks    bite 1d6 · claw 1d4
    strikes    2 per round
    speed      10 m
    Defence    15
    vitality   1d8 per level
    saves      Fortitude and Reflex strong · Will weak
```

**⚠ Three things it gets right that the player record does not.**

**It is a template, and templating is the point.** One `Cannok` entry, many cannoks. `TRACE-83` found KOTOR's blueprint system collapsing under exactly the pressure this avoids — **1,589 distinct blueprints for 1,619 placements**, roughly one template per instance, because an instance could override nothing.

**Vitality is a die per level, not a number.** So a creature scales without anyone authoring a value, and two of the same kind at different levels need one entry.

**It carries `senses` as a first-class line** — which `PT-1237` had to add to the player record afterwards, and `PT-1238` then had to propagate across five surfaces.

**So the model exists. It is scoped to beasts and needs generalising to people.**

---

## 2 · What an authored character adds

**Beyond the beast shape, a person needs:**

```
identity      a NAME, and a HANDLE a package can author against
class         beasts have none; people take our real classes
equipment     what they carry and wear, per the locked lattice
faction       who they belong to
protection    whether the story can afford to lose them
behaviour     what they do when nobody is scripting them
```

### ⚠ Protection — take KOTOR's three booleans exactly

`TRACE-85` found `Plot`, `Min1HP` and `IsRaiseable` on live creature records. **Three booleans that solve the story-NPC problem**, and twenty years of shipped content needed all three:

| Flag | Means |
|---|---|
| **`plot`** | cannot be harmed at all |
| **`min_1_hp`** | can be hurt, cannot be killed |
| **`raiseable`** | can be killed, comes back |

**They are not the same flag at different strengths.** A quest-giver mid-conversation is `plot`. A companion in a fight they must survive is `min_1_hp`. A character who *should* die and return is `raiseable`. **Copy them as-is.**

### Identity, and the handle

**`PT-1268`'s handle principle applies directly.** A uuid is identity; it is not a name a package can author against. An authored character carries a **stable handle** — `guard.peragus.dock_02` — that dialogue, quests and scripts reference, and which survives the character being edited.

---

## ⚠ 2a · THE FILE — `PT-1374`

**`4d` stopped on this: `AREA-FORMAT-01 §3` says `from = "characters/sith-trooper"`, and no such file could exist.** This document described **what an authored character contains and never what one IS.** Content without shape.

**Nothing below is new.** Every field comes from `§1`, `§2`, `§3` or `§4` — **this is those sections written as a file.**

```toml
# blueprints/characters/sith-trooper.toml   ⚠ PT-1377

[character]
name       = "Sith Trooper"
handle     = "sith-trooper"          # §2 — a package authors against this
class      = "soldier"               # §2 — people take our real classes
level      = 3
faction     = "sith"                 # §2

[abilities]
str = 14
dex = 12
con = 13
int = 10
wis = 10
cha = 8

[vitality]
die = "d10"                          # §1 — a die per level, from the beast model
override   = 0                       # ⚠ §3's escape hatch. 0 = derive normally

[protection]                         # ⚠ §2 — KOTOR's three, copied as-is
plot       = false                   # cannot be harmed at all
min_1_hp   = false                   # can be hurt, cannot be killed
raiseable  = false                   # can be killed, comes back

[equipment]                          # §2 — the locked lattice, PT-1252
body       = "items/armor/sith-armor"
weapon_r_1 = "items/weapons/blaster-rifle"

[attachments]                        # ATTACHMENT-01 §2
doctrine   = "blueprints/doctrines/sith-line"   # ⚠ PT-1441 — a PATH
reaction   = [                                  # ⚠ PT-1441 — INLINE, no file
  { on = "alarm_raised", then = "doctrine.rally" },
]
```

### ⚠ A CHARACTER BLUEPRINT NAMES ITS SPECIES — `PT-1490`

**`BUILD 64` found that a placement has no KIND.** This document gives a blueprint a name, class, level, faction, abilities, vitality and protection — **and no species and no chassis.** The Sith Trooper's file names none, Loom's writer offers none, `OpenedCharacter` has no field for one.

**⚠ So `kindOf` returns null for every creature in the bed, and `excludes` has nothing to refuse.** The gate is correct and **permanently silent about placements** until a blueprint can say what it is.

**⚠ And it corrects `PT-1424`, which was half right.** I ruled that **speed is DERIVED rather than missing — it lives on the species, and a blueprint carrying one would be a second source for a fact the species already owns.** True — **and there is no species to own it.** `combatantsIn` hardcodes `speed` for exactly that reason.

> **One absent field, two symptoms. A character blueprint names its species.**

**⚠ `PT-1424`'s principle survives and its conclusion does not.** Speed is still derived, `base attack bonus` and `reaction tier` are still derived from class — **but a derivation needs something to derive FROM, and I checked that the species OWNED speed without checking that the blueprint NAMED a species.**

### ⚠ EVERY LIGHTSABER CARRIES A COLOUR CRYSTAL — `PT-1472`

**Owner ruling.** **The colour is the CRYSTAL, and the crystal is part of the upgrade suite.** **⚠ Every lightsaber starts with one attached.**

**So `Training Lightsaber blue` is not a name with a qualifier fused into it — it is a weapon and a fitted crystal**, and `Coder`'s extractor diagnosis was right about the mechanism (`clean()` strips the `⚠`, leaving two spaces) **and incomplete about the meaning.** The second word was never part of the name.

**⚠ And the structure already exists and nobody had joined it:** the catalogue holds **97 crystals**, and every lightsaber row carries *"properties come from the fitted crystals — `PT-345`"* — **one of the annotations `PT-1467` moved out of `items.properties`.** A lightsaber's base dice are its own; **everything else comes from what is fitted.**

> **⚠ STILL OPEN, AND IT IS NOT THE CRYSTAL: `Training Lightsaber` has no base type.** `lightsaber` is **2d10** — a war blade — and `Coder` is right that **giving a padawan's practice weapon a master's dice is a ruling, not a mapping.**
>
> **Either `Training Lightsaber` is its own base type in `EQUIPMENT-01`, or "training" is flavour on the array and it IS a lightsaber with a cheap crystal.** The crystal ruling does not decide this.

**And `Marksman Rifle` is the same shape:** `EQUIPMENT-01` has `blaster-`, `ion-`, `sonic-` and `disruptor-rifle` **and no `marksman-rifle`.** **Two names, both needing a base type rather than a mapping.**

### ⚠ A doctrine is a FILE; a reaction is INLINE — `PT-1441`

**`BUILD/34` stopped here and the line it drew is right: `items/` exists and `doctrines/` did not.** Three things ruled.

**⚠ 1 · `doctrines/` goes in `blueprints/`**, beside `characters/`. A doctrine is **authored content a package supplies and many creatures share** — which is what `blueprints/` is for.

**⚠ 2 · A creature names a PATH, not a handle.** `AUTHORED-CHARACTER-01` said path, `ATTACHMENT-01 §2` said `czerka_security`. **The path wins:** `PACKAGE-NAMING-01` makes **the path identity**, and every other cross-reference in the format is one — `from`, `tileset`, a conversation's `owner`. **A handle needs a lookup table and nothing declares one.**

**⚠ 3 · A REACTION IS INLINE AND HAS NO FILE.** `ATTACHMENT-01 §3` makes it **two fields — `on` and `then`** — and **a file per two-field record is worse than the record.** A doctrine earns a file because it carries preferences, exclusions and a break-off rule; **a reaction does not.**

**And that removes the dangling half:** `§2`'s bare list `[ alarm_raised, ally_downed ]` **pointed at nothing declared anywhere.** Written out, it points at itself.

### ⚠ Three things this file does NOT have

**No `id` separate from the file path.** `PACKAGE-NAMING-01`: **the path IS the identity.** `characters/sith-trooper.toml` is the id.

**⚠ No `tag`.** A tag names a **placed instance** (`PT-1331`) and lives in `[[contents]]`. **A template is placed many times; it has no instance identity.**

**⚠ No current state.** No hit points now, no position, no conditions. `PLAY-STATE-01`: **state is a projection of the log.** `vitality.die` is what it derives *from*.

**⚠ AND NO SPEED, NO BASE ATTACK BONUS, NO REACTION TIER — `PT-1424`.** The seam asked for all three and **invented none.**

**Speed is DERIVED, not missing:** it lives on the **species**, where **49 of 57 records carry it.** A character's speed is its species' — **so the blueprint carrying one would be a second source for a fact the species already owns**, and `PT-1391` made the subrace what resolves the mechanical values.

**⚠ Base attack bonus and reaction tier are derived from CLASS**, which the blueprint names. **A blueprint carries what an author CHOSE; everything computable from a choice stays computable.** `§1`'s own principle: **store the choice, derive the consequence.**

### ⚠ `override` is the escape hatch, and it defaults to OFF

**`§3` took this from `TRACE-84`: authored content sometimes needs an exact number the rules would not produce.** A boss with 200 HP.

**It is a field rather than a principle violation** — **`0` means derive normally**, and a non-zero value is **the author saying so explicitly and visibly in the file.**

### ⚠ And the format vs the editor — format first

**`BUILD-ORDER-01`'s rule asks *can the Builder make it?* Yes — a creature editor is what a Builder is for.** But **an editor writes a shape, so the shape comes first.** You cannot build an editor for a format that does not exist. **This is that shape; the editor is next.**

---

## 3 · ⚠ The HP escape hatch — `TRACE-84`'s sharpest finding

**The problem, stated plainly: in a derive-only model a designer cannot make one guard tougher.** Vitality derives from class, level and Constitution. To make *this* guard harder, you would have to invent a class or a feat for him. **That is absurd, and authored content needs an override.**

**The answer, and why it is not a hole in the principle.**

**Store-the-choice-derive-the-consequence is a rule about a PLAYER'S record.** A player's vitality is a consequence of choices they made. **An authored character has no choices — an author *declares* what is true about them.** A declaration *is* a choice; it is just the author's rather than the player's.

**So:**

```
vitality:  { die: d8 }                 derived, scales with level
vitality:  { die: d8, override: 40 }   declared — this one is tougher
```

**⚠ Both forms are choices. Neither violates the principle.** The override is authored data on a template, exactly as `Defence 15` already is on a Cannok.

**And the guard on it:** an override is **declared on the template**, never patched onto an instance. `TRACE-83` showed where instance-level overriding leads — KOTOR's waypoints can override seven fields while its creatures can override none, and the result is one blueprint per placement.

---

## 4 · Template and instance — the thing KOTOR got wrong

**⚠ `TRACE-83` is the whole argument.** Every KOTOR creature placement carries **six fields**: a template name and five position floats. 100% of 3,319 instances, both games. No inheritance, no partial override.

**The consequence is measurable.** Two guards differing only in hit points need **two complete blueprints**. K1's modules ship 1,589 distinct blueprints for 1,619 placements. **The template system stopped functioning as one.**

**Our rule:**

> **An instance is a template plus a named set of permitted overrides.** The template declares which fields an instance may override. Anything not declared overridable is fixed.

**Why the template declares it, rather than a global list:** a `plot` flag should be instance-overridable on a generic guard and *not* on a story character. **The template author knows; a global rule cannot.**

---

## 5 · `is_pc`, and what it actually distinguishes

**Not "is this a person" — `TRACE-85` found 0 of 184 saved KOTOR creatures carrying `IsPC=1`, because the player is stored somewhere else entirely.**

**What it distinguishes for us is which model a character uses:**

```
built     from CHARACTER-RECORD-01 — a log of choices, replayable
authored  from this document — a template, declared
```

**A companion is the interesting case.** Authored at first meeting, then levels up like a player. **Ruling: a companion is authored, and the log applies to it from the moment it joins.** One character can be declared *and then* accumulate a log; it cannot be built by creation and then re-declared.

---

## 6 · Open

- ~~Faction is named here and not specified~~ **Closed at `PT-1278`.** `FACTIONS-01 §4` rules a faction declaration does **three things and no more**: sets what a merchant will sell, sets **who starts hostile on sight**, and colours the backstories. `§5` says what it does **not** do, including that **it does not gate classes**. One handle on the character; no standing track.
- **Behaviour attachment** is named and deferred to **cluster C**, where the script handle lives.
- ~~Whether beasts and people share one document or two~~ ✅ **MERGE — `PT-1325`.** **The games used ONE type for everything alive.** `UTC` is *creature*, and there is no separate beast type among the nine blueprint types — **a Jedi, a rancor and an astromech droid are the same record shape.** One schema, one document; two documents describing one shape is a drift risk with no benefit.
- ~~Companion levelling~~ ✅ **RULED at `PT-1325`. The player levels them, and PLACE decides which player.**
  - **At the ship or headquarters, anyone present may level anyone.** That is where the party gathers, and it is how the games felt.
  - **In a party, the player tied to a companion levels them.**
  - **⚠ No locality lookup is needed.** An earlier proposal used `PT-1313`'s zone system; **the ship-or-party rule covers the same cases with no distance check** — a companion is either at the hub with everyone or in someone's party, and there is no third state.
