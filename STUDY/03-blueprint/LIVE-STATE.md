# STUDY — KOTOR'S LIVE CHARACTER STATE

*Focused study, out of batch order. Filed with the blueprint work because it is
the other half of the same question: `RECORDS.md` describes what a creature
**declares**; this describes what one **becomes**.*

**Why this exists.** `CHARACTER-RECORD-01` is a creation-time contract and has
nothing for a character in play (`FLAWS.md` OF01). KOTOR shipped that half. This
is what it looks like.

**Method.** Read from four real K1 save directories and the exploded live
working set in `gameinprogress/`, with the GFF reader from batch 3. Coverage:
**184 saved creature records across 21 module snapshots, 321 effects, 21 copies
of the player, and every top-level save file.** Inferences are marked; negatives
name what was searched.

**⚠ K1 only.** This install has **no K2 save data of any kind** — searched the
whole K2 tree for `*.sav`, `savenfo.res`, `PARTYTABLE.res`, `GLOBALVARS.res`,
`AVAILNPC*`, and for `saves`/`currentgame`/`gameinprogress` directories. All
negative. §7 says what can and cannot be concluded about K2 from the script API
alone.

---

## 1 · ⚠ Where live state actually lives

**It lives in six places, and the player lives in a seventh that surprised me.**

Batch 1 established the save's outer shape: `SAVEGAME.sav` holds companion
`UTC`s, `INVENTORY`, `REPUTE`, and one nested `{ARE, GIT, IFO}` archive per
**visited** module. Following the state properly changes the picture.

```
Saves/<NNNNNN - Name>/
  SAVEGAME.sav               MOD-signature archive
    AVAILNPC0/1/2/6/7/8      companions, as full creature records
    INVENTORY                party inventory
    REPUTE                   faction standings
    <module>.sav  x21        one per visited module, each holding:
        <module>.GIT           ⚠ full live creature records, not placements
        <module>.ARE           area state
        Module.IFO             ⚠ Mod_PlayerList — THE PLAYER
  PARTYTABLE.res             party-level state, journal, message logs
  GLOBALVARS.res             every global variable's value
  pifo.ifo                   a further copy of the player (autosave only)
  savenfo.res                load-screen metadata
  Screen.tga                 save thumbnail (non-autosave only)
```

### The GIT stops being a placement file

This is the crux. A **shipped** GIT `Creature List` entry carries six fields —
template name plus five floats (`README.md` §4). A **saved** GIT entry carries
**112 fields**: the whole creature, inline, with its current hit points, its
effects, its action queue and its position.

So the save does not reference blueprints at all. **It replaces them.** Once a
module has been visited, its creatures exist only as saved records; the
blueprint is never consulted again for that module.

### The player is in `Mod_PlayerList`, inside every module snapshot

I looked for the player in the saved creature lists and found nothing —
**0 of 184 saved creatures have `IsPC = 1`**. The player is not in the GIT.

The player is in the module snapshot's **IFO**, under `Mod_PlayerList`, and it
is there in **all 21** of them.

**And the 21 copies are not duplicates — they differ.** Sampled across one save:

```
tar_m02aa   HP 10/22   XP 28,310   GoodEvil 70   7 effects   X  92.6
tar_m02ab   HP 10/22   XP 33,205   GoodEvil 72   7 effects   X 130.3
tar_m02ac   HP  6/22   XP 29,420   GoodEvil 69  10 effects   X 188.9
tar_m02ad   HP 10/22   XP  5,045   GoodEvil 66   3 effects   X 113.7
tar_m03ab   HP  0/22   XP 18,285   GoodEvil 77   3 effects   X 113.2
…
distinct values across the 21:  HP 4 · XP 15 · GoodEvil 7 · effects 8 · X 21
```

Each snapshot holds **the player as they were when they last left that module** —
including one at 0 hit points. The save therefore contains a partial history of
the character, at module granularity, as a side effect of how modules are
frozen. Nothing reads it back as history; it is 20 stale copies and one live
one. The highest XP (33,310) matches `PARTYTABLE`'s `PT_XP_POOL`, which is how
you tell which is current.

`pifo.ifo` at the save's top level is the same structure again — one
`Mod_PlayerList` with one 112-field record. **It is present only in the
autosave**; the three ordinary saves have no `pifo.ifo` and no top-level IFO
inside `SAVEGAME.sav`. Why the autosave carries an extra copy was not
determined.

### Companions are outside the world

`AVAILNPC0…8` are full creature records with live values — Bastila at 24/27 hit
points, alignment 70, 29,596 XP, one active effect — but **`ObjectId` is
absent** on all of them, where every in-world creature has one. A companion not
in the active party has no world identity; it is a record in a drawer.

---

## 2 · The field set

Diffing every saved creature field against every field on every K1 blueprint:
**49 live-only, 63 shared, 23 blueprint-only.**

### ⚠ Live-only — 49 fields, present in a save, on no blueprint

| group | fields | persists across save | across area transition |
|---|---|---|---|
| **identity** | `ObjectId`, `AreaId` | yes | ⚠ reassigned — see below |
| **vitals (derived, frozen)** | `ArmorClass`, `FortSaveThrow`, `RefSaveThrow`, `WillSaveThrow`, `MaxForcePoints` | yes | yes |
| **progression** | `Experience`, `Gold`, `SkillPoints`, `JoiningXP`, `MClassLevUpIn`, `StartingPackage`, `PregameCurrent` | yes | yes |
| **position** | `XPosition`, `YPosition`, `ZPosition`, `XOrientation`, `YOrientation`, `ZOrientation` | yes | ⚠ per-module — see below |
| **effects** | `EffectList` | ⚠ per-effect flag — §3 | yes |
| **AI / senses** | `PerceptionList`, `ExpressionList`, `AIState`, `DetectMode`, `Listening`, `Commandable` | yes | frozen with the module |
| **action queue** | `ActionList` | yes | frozen with the module |
| **combat** | `CombatInfo`, `CombatRoundData` | yes | yes |
| **script variables** | `SWVarTable` (`BitArray`+`ByteArray`), `VarTable` | yes | yes |
| **presentation** | `Animation`, `AmbientAnimState`, `Color_Skin`, `Color_Hair`, `Color_Tattoo1`, `Color_Tattoo2`, `CreatureSize`, `MovementRate`, `Age`, `UseBackupHead`, `DuplicatingHead` | yes | yes |
| **flags** | `StealthMode`, `PM_IsDisguised`, `IsDestroyable`, `IsRaiseable`, `DeadSelectable`, `CreatnScrptFird` | yes | yes |

**Two things do not survive an area transition.** `ObjectId` is a runtime handle
scoped to the loaded module — the same creature in two modules has two ids, and
companions out of the party have none at all. And position is stored **inside
the module snapshot**, so a creature has one position per module and no global
one. Both are inferences from the storage layout, not observed behaviour.

### Blueprint-only — 23 fields dropped the moment a creature exists

`TemplateResRef`, `Comment`, `PaletteID`, `TemplateList`, `BodyVariation`,
`TextureVar`, `WalkRate`, `PerceptionRange`, `CRAdjust`, `NoPermDeath`,
`LawfulChaotic`, `Morale`, `MoraleBreakpoint`, `MoraleRecovery`,
`SaveFortitude`, `SaveReflex`, `SaveWill`, `FortBonus`, `RefBonus`,
`WillBonus`, `SubRace`, `Portrait`, `SoundSet`.

Three groups: **authoring metadata** (`Comment`, `PaletteID`,
`TemplateResRef`), **the dead NWN residue** batch 3 F30 catalogued, and — the
interesting one — **`WalkRate` and `PerceptionRange` become `MovementRate` and
`PerceptionList`**. A declared parameter is replaced by live state derived from
it.

### The player carries one thing nobody else does

`LvlStatList` — a per-level record, on the PC only:

```
[{ LvlStatClass, LvlStatHitDie, LvlStatForce, SkillPoints,
   SkillList[8], FeatList[…] }, …]        one entry per character level
```

**This is a level-up history**: what class was taken, what hit die rolled, what
skills and feats were gained, at each level. It is the closest thing in KOTOR to
our event log — and it exists only for the player, only for level-ups, and is
append-only in practice.

---

## 3 · ⚠ Effects and conditions

**A list on the creature.** `EffectList` is present on **184 of 184** saved
creatures. Lengths 1–9; 321 effects in the sampled snapshots.

**Entry shape — one shape, universal across all 321:**

```
Type            what kind of effect          e.g. 36 = EFFECT_TYPE_HASTE
SubType         observed 1, 3, 4, 9, 10
Duration        FLOAT, seconds
ExpireDay       game-calendar day
ExpireTime      time within that day
CreatorId       who applied it
SpellId         the power that caused it, or 0xFFFFFFFF for none
Id              a unique effect instance id
IsExposed       whether the UI shows it
SkipOnLoad      whether it survives a reload
NumIntegers     how many of IntList are meaningful
IntList  FloatList  ObjectList  StringList     the typed payload
```

**Types decoded** against `EFFECT_TYPE_*` in `nwscript.nss` (79 constants in K1,
82 in K2). Observed in this save:

```
 2 ABILITY_BONUS   10 DAMAGE_IMMUNITY   13 DEAF   22 FORCE_RESISTANCE
30 SLEEP           36 HASTE             48 MOVEMENT_SPEED_INCREASE
68 SPELLLEVELABSORPTION                107 (no constant with this value)
```

The payload is generic: an effect carries four typed arrays and a count, and
what those slots mean depends on `Type`. **The effect system is a tagged union
with an untyped body** — the same shape problem batch 3 §1 found in GFF, one
level further in.

**Durations are real-time seconds.** Only two values appear across all 321:
`0.0` (312 effects) and `5000.0` (9). Combined with `ExpireDay`/`ExpireTime`, an
effect expires at a wall-clock instant on a game calendar, not after a number of
rounds. `DURATION_TYPE_INSTANT/TEMPORARY/PERMANENT` exist as script constants
(0/1/2) but are not the stored duration — the stored duration is a float.

**Across a save: it is per-effect and explicit.** `SkipOnLoad` is **1 on 190
effects and 0 on 131**. Some effects are deliberately dropped on reload and
others deliberately kept, decided when the effect is created. That is a real
mechanism and a good one — it is the answer to "what happens to a buff when you
reload", and KOTOR answers it per effect rather than by blanket rule.

**And some are hidden.** `IsExposed` is 0 on **6 of 321**. The engine
distinguishes effects the player can see from effects it does not surface —
relevant to §6.

**What is *not* here.** No condition names, no stacking rules, no source
description, no "who can dispel this". An effect is a type id and a bag of
numbers.

---

## 4 · Alignment

**One field. `GoodEvil`, an integer 0–100.** It sits on the blueprint *and* on
the live record, so it is both an authored default and a live value.

Observed: player 72 (and 66–77 across the 21 historical copies); Bastila 70,
Carth 75, Mission 75, Zaalbar 60, T3-M4 50, Canderous 30; ordinary NPCs 50 in
181 of 184 cases.

**Nothing else exists.** Scope of that negative: searched every field of all 184
saved creatures, the 112-field player record, `PARTYTABLE.res`,
`GLOBALVARS.res`, and both games' blueprint field sets. There is **no band, no
direction of travel, no history, no hysteresis state, no drift rate, no
per-source accounting**. `LawfulChaotic` exists on blueprints, is dead
(batch 3 F30), and is dropped entirely from live records.

Writes come from `SetGoodEvilValue` and `AdjustAlignment` in the script API —
so alignment moves only when content says so, never as a computed consequence.

**Against ours:** `ALIGNMENT-01-v2` specifies seven bands, directional
hysteresis, dark-power drift, four atonement routes and Wisdom resistance.
KOTOR carries the *value* and derives the band on read. Everything our system
needs to remember **between** changes — which direction you were last moving,
how deep the hysteresis is — has no home in KOTOR because KOTOR has no such
rule. So this is one place where our record genuinely needs a field KOTOR never
had, rather than a field KOTOR has and we lack.

---

## 5 · ⚠ Which of this is real-time, and which is being a character

The distinction the study was asked for. **Roughly a third of live state exists
only because time flows continuously, and copying it into a turn-based game
would be actively wrong.**

### Artefacts of the clock — do not port

| what | why it exists | what turn-based needs instead |
|---|---|---|
| `Duration` as **float seconds** + `ExpireDay`/`ExpireTime` | effects expire at a wall-clock instant | **rounds remaining**, or a named end condition ("until you rest", "end of your next turn") |
| `ActionList` — the queued-action stack, with a **suspended script VM** (`CodeSize`, `InstructionPtr`, 106 KB of bytecode mid-execution) | the engine interrupts and resumes behaviour between frames | nothing. A turn ends cleanly; there is no mid-action to resume |
| `CombatRoundData` | tracks where you are *inside* a 3-second round | nothing. The round boundary is the unit |
| `Animation`, `AmbientAnimState` | which frame of which animation is playing | nothing |
| `MovementRate`, `PerceptionList`, `DetectMode`, `Listening`, `AIState` | continuous sensing and pathing | perception is a check, not a standing list |
| `ExpressionList` (`gen_i_was_attacked`) | AI mood that decays over time | a condition with a stated end |
| `PT_PLAYEDSECONDS` | a wall clock | session count, or nothing |

The action queue is the clearest case. KOTOR persists a **half-executed script**
— program counter and all — because a save can land anywhere in continuous
time. A turn-based game has natural quiescent points and needs none of this. If
our design ever grows an action queue, that is a signal something has gone
wrong.

### Genuinely about being a character — port these

| what | why it is not about the clock |
|---|---|
| `CurrentHitPoints` vs `MaxHitPoints` | damage taken is state regardless of how time flows |
| `CurrentForce` vs `MaxForcePoints` | same, and ours needs it more — `FORCE-POOL-01` has regeneration, fatigue and degradation, all of which need a current value to act on |
| `EffectList` **as a list on the creature** | conditions are things a character has. Only the *duration unit* is real-time |
| `IsExposed` per effect | "the player can see this one" is a presentation decision, not a timing one |
| `SkipOnLoad` per effect | persistence is a property of the effect, and deciding it per effect is right in any model |
| `Experience`, `Gold`, `SkillPoints` | unspent resources |
| `GoodEvil` | a value that drifts |
| `LvlStatList` | what happened at each level |
| `SWVarTable` per creature | arbitrary per-character state that content can write |
| `IsDestroyable`, `IsRaiseable`, `Plot`, `Min1HP` | narrative protection |
| `ArmorClass`, save throws, `CombatInfo` **as a cache** | see below |

### The one that is genuinely arguable

`CombatInfo` is a **fully derived block frozen onto the record** — `NumAttacks`,
`OnHandAttackMod`, `OnHandDamageMod`, off-hand equivalents, `ForceResistance`,
`ArmorCheckPen`, crit range and multiplier, unarmed damage dice, both equipped
weapon handles. Every value is computable from class, abilities, feats and
equipment.

For a real-time engine recomputing per frame, caching is obviously right. For a
turn-based game it is not obviously wrong either — a cached, *visible*
derivation is what a character sheet **is**, and a player reading "Defence 18"
wants a number, not a promise that one could be computed.

The honest position: **cache it, but treat the cache as a projection with a
stated invalidation rule**, not as stored truth. KOTOR does not distinguish
these, which is why `ArcaneSpellFail` — a D&D field with no KOTOR meaning — sits
in `CombatInfo` on every creature in the game.

---

## 6 · ⚠ What it feels like

The state is not the interesting part. **What KOTOR surfaces is.**

### It shows the player the entire arithmetic

`PARTYTABLE.res` carries `PT_FB_MSG_LIST` — a **64-entry ring buffer of feedback
messages**, persisted in the save. Real entries from this one:

```
Gail Dakari succeeds with attack on Sith Governor. Power Attack used.
Attack Breakdown: Mainhand 25 = roll 20 Automatic Hit!
Threat Breakdown: Roll 20 vs. required 19 - 20, threat success with A…
Defense Breakdown: 18 = base 10 + dex mod 4 + class 4
```

**KOTOR shows the dice.** Not a result — the roll, the modifiers, each named,
and the total. "Defense Breakdown: 18 = base 10 + dex mod 4 + class 4" is a
sentence explaining a derived value in terms of its sources, printed to the
player during play.

For a system whose record derives vitality, defence and saves rather than
storing them, this is the strongest single argument in the study for
**derivation being a feature you can show rather than a cost you hide**. Our
locked character sheet has the same information and, unlike KOTOR, is not
fighting a 3-second combat round for the player's attention.

Two colours are used (`PT_FB_MSG_COLOR` 0 on 53 entries, 1 on 11) — plain and
emphasised. One type (`128`) across all 64. `feedbacktext.2da` is a separate and
much smaller thing: **3 rows** in both games — `Resisted`, `Immune`, `Saved` —
so the breakdown text is engine-generated, not table-driven.

### It keeps a parallel record of what was said

`PT_DLG_MSG_LIST`, also 64 entries, `{PT_DLG_MSG_SPKR, PT_DLG_MSG_MSG}` —
speaker and line. Terminal output appears here too
(`Security Terminal` / `[SUCCESS] ELEVATOR OPEN`), so the log is "things that
addressed you", not only conversation.

### It remembers the interface

`PT_LAST_GUI_PNL` records which panel was last open. `PT_TUT_WND_SHOWN` is a
6-byte bitmask of which tutorial windows have been seen. `PT_SOLOMODE`,
`PT_FOLLOWSTATE`, `PT_CONTROLLED_NP` persist party-control mode. The interface
state is part of the save, not rebuilt from defaults.

### And it hides some things deliberately

`IsExposed = 0` on 6 of 321 effects. The engine carries effects it does not
surface — the player is affected and not told. Whether that is per-effect
authorial choice or a category rule was not determined.

### What it does *not* show

No effect names anywhere in the data — an effect is a type id. Whatever the
player sees for a buff comes from the icon layer, not from anything stored on
the effect. Nothing records how long an effect has left in player-facing terms;
the expiry is an absolute timestamp.

---

## 7 · K1 vs K2

**⚠ Scope first.** There is **no K2 save data in this install** — searched the
whole K2 tree for save-shaped files and directories, all negative. Everything
below is either from the script API, which both games ship, or is explicitly
unverified.

**What can be said.** K2's `nwscript.nss` carries the same live-state accessors:
`GetCurrentHitPoints`, `GetMaxHitPoints`, `GetGoodEvilValue`,
`SetGoodEvilValue`, `GetFirstEffect`/`GetNextEffect`, `GetEffectType`,
`GetEffectSubType`, `GetEffectDurationType`, `GetEffectCreator`,
`GetEffectSpellId`, `RemoveEffect`, `GetXP`/`SetXP`, `GetGold`,
`GetStealthMode`, `GetDetectMode`. So the same state exists and is reachable.

`DURATION_TYPE_INSTANT/TEMPORARY/PERMANENT` are 0/1/2 in both games.

**K2 adds exactly three effect types** and removes none:
`EFFECT_TYPE_DROIDSCRAMBLE`, `EFFECT_TYPE_DROID_CONFUSED`,
`EFFECT_TYPE_MINDTRICK` — 79 constants to 82.

**What cannot be said.** Whether K2's save layout matches K1's; whether the
player still travels in `Mod_PlayerList`; whether `PT_FB_MSG_LIST` is still 64
entries; whether K2 added live fields to the creature record. **All unverified.**
K2's blueprint-side additions (batch 3: `BlindSpot`, `Hologram`,
`MultiplierSet`, `IgnoreCrePath`, `WillNotRender`) plausibly appear on live
records too, but that is an inference from the blueprint diff, not a reading.

---

## 8 · One discrepancy worth recording

**The save declares more globals than any shipped `globalcat.2da`.**

```
globalcat.2da   BIF / rims/global.rim / rims/miniglobal.rim   (all identical)
                809 Boolean · 369 Number · 5 Location · 2 String

GLOBALVARS.res (save)
                819 Boolean · 376 Number · 5 Location · 2 String
```

Ten more booleans and seven more numbers than the table batch 2 established as
the predeclaration list, and `patch.erf` does not contain a `globalcat`.

The structural point stands regardless, and it is a good one: **the save carries
its own name list** — `CatBoolean`, `CatNumber`, `CatLocation`, `CatString` are
lists of names inside `GLOBALVARS.res` — so a save does not depend on
`globalcat.2da` being unchanged in order to load. Values are packed tightly
against those lists: `ValBoolean` is a **103-byte VOID for 819 booleans**
(bit-packed), `ValNumber` is **376 bytes for 376 numbers** (one byte each, so
globals are 0–255), `ValLocation` is 2,400 bytes for 5 locations.

Why the counts differ was not determined — engine built-ins appended at runtime
is the obvious guess, and it is a guess.

---

## 9 · Scope — what was and was not checked

**Read in full:** four K1 save directories; all 21 module snapshots in
`gameinprogress/`; 184 saved creature records; all 321 of their effects; 21
player records; `pifo.ifo`; all six `AVAILNPC*.utc`; `PARTYTABLE.res`;
`GLOBALVARS.res`; `REPUTE.fac`; every shipped `globalcat.2da` copy; both games'
`nwscript.nss` for effect and state constants; `feedbacktext.2da` in both games.

**Searched, negative:** the whole K2 install for any save data (none); all 184
saved creatures for `IsPC = 1` (none); every field of every live record for any
alignment field beyond `GoodEvil` (none).

**Not checked — and some of this is engine-internal by nature:**

- **Any running process.** Nothing here is observed behaviour. Whether
  `ObjectId` is genuinely reassigned per module, whether `SkipOnLoad` does what
  its name says, and what `IsExposed` drives in the UI are all **inferences from
  storage layout**.
- **What `SubType` means.** Values 1, 3, 4, 9, 10 appear; `DURATION_TYPE_`
  constants are 0–2 and do not obviously map. Not resolved.
- **Effect type 107**, which has no `EFFECT_TYPE_*` constant in either game.
- **The `IntList`/`FloatList`/`ObjectList`/`StringList` payload semantics** —
  they are per-`Type` and would need the engine to decode.
- **`INVENTORY.res`** — opened only far enough to confirm it is a GFF with its
  own `INV ` magic. Its internals are inventory-layer work.
- **`CombatRoundData` populated** — every creature in these saves is idle, so
  the struct is empty in all 184. Its fields are unknown.
- **Regeneration.** No stored rate or tick was found on any record; if
  regeneration exists it is engine-internal. Scope: searched all live-record
  fields and both script APIs for `regen`-shaped names.
- **Why the autosave alone carries `pifo.ifo`.**
- **`Mod_Effect_NxtId`** on the module IFO — an effect-id allocator, noted but
  not traced.
