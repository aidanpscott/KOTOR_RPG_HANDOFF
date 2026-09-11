# STUDY 31 — how enemies enter combat in KOTOR

**Files only. K1's scripts, GUI layouts and script API. Feeds the HUD's
enemy-visibility question (`PT-1584`/`PT-1640`).**

---

## 1 · COMBAT START IS PERCEPTION-DRIVEN AND AUTOMATIC. IT IS NOT CONTACT.

**`STUDY 27` already established the range**: every creature carries a
`PerceptionRange` indexing `ranges.2da`, and **97.8% sit on the default — 20 m
sight, 20 m hearing.** This is what fires on it.

`k_def_percept01.nss` delegates to `k_ai_master`, case `1002`. The live path:

```c
object oPerceived = GetLastPerceived();
if (GetCommandable() && !AI_OFF)
  if (!GetIsObjectValid(GetAttemptedAttackTarget()) && … && !GetAttackTarget())   // not already fighting
    if (GetLastPerceptionSeen())                                                   // ⚠ SEEN, not heard
      if (GetIsEnemy(oPerceived))
      {
          float fDelay = GetDistanceBetween(OBJECT_SELF, oPerceived) / 10.0;
          DelayCommand(fDelay/2.0, SetFacingPoint(GetPosition(oPerceived)));
          if (GN_GetSpawnInCondition(SW_FLAG_STATE_AGITATED)) fDelay = 0.0;
          SpeakString("GEN_I_WAS_ATTACKED", TALKVOLUME_SILENT_TALK);
          DelayCommand(fDelay, GN_DetermineCombatRound());
          if (fDelay > 0.0) GN_SetSpawnInCondition(SW_FLAG_STATE_AGITATED);
      }
```

**Four things worth having:**

* **⚠ The gate is `GetLastPerceptionSeen()` — sight specifically.** Hearing fires
  the same event and **does not start a fight** on this path.
* **⚠⚠ THE REACTION DELAY IS PROPORTIONAL TO DISTANCE — `distance / 10` seconds.**
  At the default 20 m that is **2.0 s**; at 5 m, **0.5 s**. And the creature
  **turns to face at half the delay**, so it visibly notices before it acts.
  *A distant enemy is slower to react than a near one, and that falls out of one
  division.*
* **⚠ `SW_FLAG_STATE_AGITATED` removes the delay on re-encounter** — BioWare's
  own comment: *"Put in the agitation flag so that re-encountered monsters do not
  delay."* (Preston Watamaniuk, April 10 2003.) **You get the slow notice once.**
* **`SpeakString(…, TALKVOLUME_SILENT_TALK)` is an AI broadcast, not dialogue.**
  One creature noticing you propagates to its allies, which is how a room engages
  together without any group object existing.

**And a second branch handles losing sight mid-fight** —
`GetLastPerceptionVanished()` → `ClearAllActions(); ActionMoveToObject(oPerceived,
TRUE); ActionAttack(oPerceived)`. **It walks to where it last saw you and attacks
there.**

> **Answer: distance-based, per-creature, engine-driven. No trigger, no script,
> no contact required.** Scripts *can* start fights (and many do), but the default
> is automatic.

---

## 2 · ⚠⚠ THERE IS NO COMBAT ROSTER. THERE IS NO "IN" TO BE IN.

**`GN_DetermineCombatRound` is per-creature AI, not a combat manager.** It reads
the creature's own AI style, and picks a target with:

```c
GetNearestCreature(CREATURE_TYPE_REPUTATION, REPUTATION_TYPE_ENEMY)
```

**Then `ActionAttack`. That is all.** It never enumerates participants, never
writes a list, never notifies anything.

**The script API confirms it.** Scanned K1's `nwscript.nss` for combat-state
functions:

| function | what it is |
|---|---|
| `int GetIsInCombat(object oCreature)` | ⚠ **a per-creature boolean** |
| `void CancelCombat(object oidCreature)` | per-creature |
| `object GetLastHostileActor(object oVictim)` | per-creature memory |
| `GetFirstObjectInShape(…)` | a **spatial query** |

> **⚠ Nothing returns the set of combatants. There is no encounter object, no
> participant list, and no moment at which a roster is locked.**

**⚠ And `Encounter*` is a false friend** — `GetEncounterActive`,
`GetEncounterSpawnsMax`, `GetIsEncounterCreature` (*"was spawned from an
encounter"*). **A KOTOR "encounter" is a SPAWNER**, not a fight.

**So combat in KOTOR is emergent, not a session.** It is the aggregate of
creatures independently deciding they have a visible enemy. *"Is this creature in
the fight"* is not a question the engine can be asked — only *"is this creature
in combat"*, of one creature at a time.

---

## 3 · ⚠⚠ VISIBILITY **IS** MEMBERSHIP — AND KOTOR HAS NO ENEMY PANEL AT ALL

### The mechanical half

`k_inc_generic.nss:289` — the disengage condition:

```c
else if (GetPartyMemberByIndex(0) != OBJECT_SELF &&
        !GetIsObjectValid(GetNearestCreature(CREATURE_TYPE_REPUTATION, REPUTATION_TYPE_ENEMY,
                          OBJECT_SELF, 1, CREATURE_TYPE_PERCEPTION, PERCEPTION_SEEN)) &&
        IsObjectPartyMember(OBJECT_SELF))
{
    if (!GetSoloMode()) { CancelCombat(OBJECT_SELF); ClearAllActions(); ActionFollowLeader(); }
}
```

**The query is for the nearest enemy `PERCEPTION_SEEN`.** Not the nearest enemy —
**the nearest enemy currently seen.**

> **⚠ So the answer to "can a player be fighting an enemy they can't see" is: not
> for long, and the engine drops them out of combat for exactly that reason.**
> Membership is not separate from visibility — **it is continuously re-derived
> from it**, per creature, every evaluation.

### The UI half — and this is the finding the HUD slice needs

**Parsed `mipc8x6` (the in-game HUD, 800×600) — 120 controls.** What is there:

| what | controls |
|---|---|
| **party, three slots** | `LBL_CHAR1/2/3` · `PB_VIT1/2/3` · `PB_FORCE1/2/3` · `LBL_DISABLE1/2/3` · `LBL_DEBILATATED1/2/3` |
| **the target — ONE** | ⚠ **`LBL_NAME` and `PB_HEALTH`** — *singular, no index, unlike `PB_VIT1/2/3`* |
| action queue | `LB_ACTIONS0–5` · `BTN_ACTION0–5` · `LBL_QUEUE0–3` · `BTN_CLEARALL` · `BTN_CLEARONE` |
| combat chrome | `LBL_COMBATBG1/2/3` · `LBL_CMBTMODEMSG` · `LBL_CMBTEFCTRED1-3` / `INC1-3` |
| world-space | `LBL_INDICATE` · `LBL_INDICATEBG` · `LBL_ARROW` |

> **⚠⚠ THERE IS NO ENEMY LIST. ONE NAME, ONE HEALTH BAR, FOR THE SELECTED TARGET.**

**The question *"how does the original game's sidebar handle an enemy you cannot
see"* has no answer because there is no sidebar.** KOTOR shows the *party* as a
list and the *enemy* as a singular selection. Enemy awareness lives in the world —
a reticle on the target, an arrow — not in a panel.

**⚠ So the "every visible enemy" panel has no KOTOR precedent.** The only
precedent in anything studied is **BG3's `CombatantsOverlay`** (`STUDY 21 §4`):
a scrolling strip with **a count at each end for what overflows**, and *acted this
round* drawn as a grey wash.

---

## 4 · LEAVING COMBAT IS NORMAL, AND IT IS MOSTLY NOT THE AI'S DOING

**`CancelCombat` is heavily used** — counted by bytecode routine (`ACTION` opcode,
routine 54), the method from `STUDY 24`:

| population | `CancelCombat` | *(for scale: `SetIsDestroyable`)* |
|---|---|---|
| `chitin.key` | **25** of 1,784 | 4 |
| modules | **842** of 14,368 | 25 |

**867 call sites. Thirty times more than `SetIsDestroyable`.** This is a
first-class operation, not an escape hatch.

**Two distinct exits:**

1. **The AI disengages when no *seen* enemy remains** — `§3`'s condition, then
   `ActionFollowLeader`. **Not death, not retreat: absence of a visible target.**
2. **⚠ Something else takes over.** The module call sites are overwhelmingly
   **dialogue, cutscene and trigger scripts** — `k_scene_start`, `k_pdan_bastdlg`,
   `k_pdan_zhar09`, `k_pdan_trig1303`. **Combat ends because a conversation
   starts.**

> **Answer: combat is not a one-way door, and the commonest way out is not
> mechanical at all — it is narrative.**

*(`GetLastHostileActor`'s own docs add a detail: **"This value will never be a
dead/destroyed creature."** The per-creature memory of who attacked you
self-clears on their death.)*

---

## 5 · ⚠ WHAT IS ENGINE-LEVEL AND NOT RECOVERABLE FROM FILES

**Stated plainly rather than guessed, as asked:**

* **What `GetIsInCombat` actually returns, and when the engine flips it.** The API
  and its callers are readable; **the state machine behind it is not in any file.**
  Whether it is set by having an attack target, by being attacked, or by a timer
  is **unknown from files.**
* **Whether the target's `PB_HEALTH` bar hides when the target leaves sight.** The
  layout says there is one bar; **what populates and clears it is engine code.**
  I can prove KOTOR has no enemy list; I cannot prove what it does with the one
  bar when line of sight breaks.
* **Whether `GetLastPerceptionSeen` accounts for walls or only distance.** The
  `bLineOfSight` parameter on `GetFirstObjectInShape` shows the engine *has*
  line-of-sight tests and that they are **opt-in there**; **whether the perception
  system uses one is not visible.**
* **The 2.0 s delay is arithmetic, not a measurement.** `distance/10` at the
  default 20 m. **Nobody timed it in the running game.**

---

## 6 · WHERE OUR CONTACT-ONLY MODEL IS A GAP, AND WHERE IT IS RIGHT

**A genuine gap, worth a ruling:**

* **⚠⚠ Nothing detects at range.** `_begin` has two call sites and both require
  walking into the creature. **KOTOR's default is automatic engagement at 20 m,
  and ours is 0 m.** That is not a simplification of KOTOR — it is the opposite
  behaviour. An enemy that lets you walk up to it is a different game.
* **⚠ The distance-scaled reaction delay is cheap and we have no analogue.**
  `distance/10` is one division, and it buys *"the guard at the far end notices
  you slower than the one beside you"* for free. ⚠ **On a turn-based grid it does
  not port as a timer** — but *"a distant enemy joins on a later round"* is the
  same idea in our units, and `STUDY 27`'s per-creature `PerceptionRange` is the
  field it would read.
* **`AGITATED` — noticing is once per encounter, not per sighting.** Worth having
  whatever the timing model is.

**Already the right simplification, and should stay:**

* **⚠ No roster is the correct model, and we should not build one.** KOTOR proves
  a fight needs no participant list — membership is re-derived from *is there a
  visible enemy*. Our `PLAY-STATE-01` is already a projection over the log;
  **"who is in this fight" can be a query, not a stored set.** ⚠ A locked roster
  would be *more* machinery than the anchor has, to answer a question the anchor
  never asks.
* **Visibility as membership transfers exactly.** On a grid it is cheaper than in
  3D — `STUDY 20 §3` records that BG3's hardest rendering problem is one a grid
  deletes, and the same applies here: **a grid can answer "is this square
  visible" exactly.**
* **⚠ Leaving combat via dialogue is already our shape.** `BUILD 31`/`PT-1437`
  has a conversation starting a fight; **KOTOR's commonest combat exit is the
  reverse of that same seam**, and `Fight.abandon()` already exists.

**⚠ And one thing to decide before the panel, not after:** KOTOR gives no
precedent for an enemy list, so **"every visible enemy" is our design, not an
inherited one.** The only worked example is BG3's, and `STUDY 21 §4` records what
it does when the list does not fit — **a count at each end** — which is
`STATE.md`'s own *"lead with the count"* rule, arrived at independently.

---

## 7 · What was NOT checked

* **K2 was not read for any of this.** All findings are K1. ⚠ `PT-1544`'s warning
  applies — K2 flattened attack and kept defence, so *"K1 is the only fact"* has
  been wrong once on exactly this kind of axis.
* **`k_ai_master`'s other cases were not read** — `ON_ATTACKED` (1005),
  `ON_DAMAGED`, `ON_DIALOGUE` (1004) and the whole `HENCH_*` (2000-series) block.
  **`ON_ATTACKED` is the other combat-start path and is unexamined.**
* **The 842 module `CancelCombat` sites were identified by name, not decompiled.**
  The dialogue/cutscene reading is from **script names and the base-script
  sources**, not from reading module bytecode.
* **`GN_RunDefaultAIRoutine` and the AI-style routines were not read** — target
  *selection* within a fight is unexamined; only target *acquisition* at combat
  start.
* **Only `mipc8x6` was parsed.** The other resolution variants and
  `maininterface` were not, though the control set is expected to match.
* **No `.git`/area data was read** for scripted-combat triggers, so *"many fights
  are script-started"* is an inference from call-site names.
