# STUDY 24 — one file deeper, the GIT half, and the log line

**Files only. Nothing launched.**

---

## 1 · ⚠⚠ `k_ai_master` DOES NOTHING ABOUT THE BODY — AND THAT IS THE ANSWER

`STUDY 23` stopped at `k_def_death01`, which delegates every death:

```c
ExecuteScript("k_ai_master", OBJECT_SELF, KOTOR_DEFAULT_EVENT_ON_DEATH);
```

**`k_ai_master.nss` is 41,456 bytes, 858 lines. `SetIsDestroyable` appears in it
ZERO times.** So does `DestroyObject`. So does `Corpse`.

The default enemy death case, entire:

```c
case 1007: //KOTOR_DEFAULT_EVENT_ON_DEATH
{
    if(!GN_GetSpawnInCondition(SW_FLAG_AI_OFF))
    {
        SpeakString("GEN_I_AM_DEAD", TALKVOLUME_SILENT_TALK);
        //Shout Attack my target, only works with the On Spawn In setup
        SpeakString("GEN_ATTACK_MY_TARGET", TALKVOLUME_SILENT_TALK);
    }
    if(GN_GetSpawnInCondition(SW_FLAG_EVENT_ON_DEATH))
    {
        SignalEvent(OBJECT_SELF, EventUserDefined(1007));
    }
}
```

**Two silent shouts to its allies, and an optional hook. Nothing about the body.**

⚠ **And the henchman death case is completely empty:**

```c
case 2007: //KOTOR_HENCH_EVENT_ON_DEATH
{

}
```

> **A party member's death runs no script at all.**

### How often live enemies get `SetIsDestroyable` — counted, not guessed

`STUDY 23` named this unchecked. It is now measured **twice**, because module
scripts ship as **compiled `.ncs`, not source** — grepping them is impossible.

**Source (`.nss`, `chitin.key`):** 1,774 files, **4 textual matches — and one is
commented out** (`k_pman_comp04`) and one is the declaration in `nwscript`. **Two
real call sites in source.**

**Bytecode (`.ncs`):** `SetIsDestroyable` is engine routine **323**, so the
`ACTION` opcode `05 00 01 43` locates it without a disassembler.

| population | `.ncs` scanned | routine 323 | control: `GetIsObjectValid` (42) |
|---|---|---|---|
| `chitin.key` | 1,784 | **4** | 347 |
| modules (274 archives) | **14,368** | **25** | 4,051 |

⚠ **The control is why the small number is believable** — the same scan finds a
common routine 4,398 times, so it is reading bytecode correctly.

**29 call sites in 16,152 compiled scripts. 0.18%.** And they are named
set-pieces — `k_pdan_nemo01`, `k_pdan_guard_9` (Dantooine), `k36_spn_destrdth`,
`k_pman_water01…11` (Manaan) — plus the three base scripts.

### ⚠⚠ AND THE THREE BASE SITES REVERSE THE EXPECTATION

| script | call | who |
|---|---|---|
| `k_def_spawndead` | `SetIsDestroyable(FALSE,FALSE,FALSE)` | spawn-in-dead **scenery** |
| **`k_hen_spawn01`** | **`SetIsDestroyable(TRUE,TRUE,TRUE)`** | **every henchman** |
| `k_hen_candspwn` | `SetIsDestroyable(TRUE,TRUE,TRUE)` | Canderous |

```c
void main()
{
   //added march 10,03 by Aidan
   SetIsDestroyable(TRUE,TRUE,TRUE);
```
*(the comment is BioWare's, in the shipped file)*

**The party is explicitly made `destroyable=TRUE, raiseable=TRUE,
selectableWhenDead=TRUE`. Ordinary enemies receive no call whatsoever.**

> ### ⚠⚠ The answer to `PT-1525`'s open question
>
> **KOTOR does not script corpse persistence for enemies. It never touches the
> flag.** An enemy's body is **pure engine default** — behaviour BioWare never
> had to express, because not-deleting-something is free.
>
> **The only creatures whose death is explicitly configured are the party**, and
> what they are given is the *opposite* of a persistent corpse: raiseable, and
> **selectable while dead** — which is how you click a downed companion.

### PT-1496

1. **What did they do?** Nothing, deliberately. The death script talks to the
   AI and leaves the body to the engine; the party gets three flags set on spawn.
2. **Why?** Because the corpse is not a feature — it is **the absence of a
   deletion**. There is nothing to implement, so there is nothing in the script.
   `SetIsDestroyable` exists to *override* that in the 0.18% of cases that need
   scenery or a raiseable companion.
3. **Does the reason still hold for us?** ⚠ **It holds exactly, and it is the
   sharpest thing in this study.** `PT-1525` frames leaving the combatant as
   *available*. **KOTOR shows it is not a feature to add but a removal to not
   perform** — and our engine already keeps combatants in `PLAY-STATE-01`.
4. **What is the modern form?** **Do not delete the combatant, and do not write a
   rule that says so.** The rule to write is the *exception* — KOTOR's shape is a
   per-creature flag for the few who behave differently, and
   `selectableWhenDead` as its own third decision.

---

## 2 · THE GIT HALF — my own negative, closed

`STUDY 23` said: *"a corpse instantiated only in a GIT would not appear in my
count… the 2,940 figure is a floor."*

**157 GIT files across every K1 module: 2,234 creature instances, 4,845 placeable
instances.**

| | fields an instance carries |
|---|---|
| creature | `TemplateResRef` · `XPosition` · `YPosition` · `ZPosition` · `XOrientation` · `YOrientation` — **and nothing else, on all 2,234** |
| placeable | `TemplateResRef` · `X` · `Y` · `Z` · `Bearing` (+ `UseTweakColor`/`TweakColor` on 65) — **and nothing else, on all 4,845** |

> **⚠⚠ A KOTOR GIT IS A PURE PLACEMENT LIST. It carries no gameplay fields at
> all.** Every gameplay property — `BodyBag`, `Appearance`, `Min1HP`,
> `NoPermDeath` — lives on the blueprint and **cannot be overridden per
> instance.**

**Creature instances with `BodyBag ≠ 0`: 0. Placeable instances with a body-bag
appearance: 0** — and both are *necessarily* zero, because the field is not
expressible there.

⚠ **So `STUDY 23`'s figure was not a floor after all — it was the whole
population, and I under-claimed.** The blueprint survey is complete by
construction. **The correct caveat was not "instances might add more" but "check
whether instances can override at all"** — a different question, and the cheaper
one.

*(This also confirms `AREA-FORMAT-01`'s shape from outside: placement and
definition are separate, and the placement layer is deliberately thin.)*

---

## 3 · ⚠⚠ THE LOG LINE — IT IS IN THE FILES. THREE STUDIES WRONG.

`STUDY 21`, `22` and `23` all recorded this as unanswered because
`CombatLog.xaml` carries only `Combat Log` and `Latest`.

**That was the wrong place to look, not a real negative.** The entries are
assembled by code **from loca templates**, and `loca.py` finds them.

### One grammar, three verbs, for every d20 roll in the game

```
[1] needs [3] to hit.     They rolled [2].
[1] needs [3] to save.    They rolled [2].
[1] needs [3] to succeed. They rolled [2].
```

with critical variants:

```
[1] needs [2] to hit.  They rolled [3] (Critical Hit).
[1] needs [2] to hit.  [1] rolled [3] (Critical Miss).
[1] needs [2] to save. They rolled [3] (Critical Success).
[1] needs [2] to save. They rolled [3] (Critical Failure).
```

> **⚠⚠ THAT IS `PT-1326`'S LINE, AND IT IS IN THE LOG RATHER THAN A TOOLTIP.**
> Target number, then the roll, then the verdict. **The derivation is the
> sentence.**

⚠ **And the crit vocabulary splits by roll type** — an attack gets *Critical
Hit/Miss*, a save gets *Critical Success/Failure*. **Two vocabularies over one
grammar**, which is a decision, not an accident.

### The rest of the log's sentence stock

```
[1] hit [2] for [3].            [1] was hit for [2].
[1] absorbed [2] damage from [3].    [1] was hit for [2] by a surface
[1] used [2].                   [1] used [2] on [3].
[1] used [3] as a reaction to [2]'s action.
[1] gained [2].                 [1] gained [2] experience.
[1] downed [2].                 [1] was killed while Downed.
[1] died.                       Round [1]
```

* ⚠ **`[1] used [3] as a reaction to [2]'s action.`** — a reaction line **names
  what it reacted to.** `ATTACHMENT-01 §3`'s `on:` made visible to the player.
* ⚠ **`[1] downed [2].` and `[1] was killed while Downed.`** — the DOWNED band
  is its own logged event, distinct from death. `STUDY 23 §3`'s two statuses,
  surfacing in the log.
* **`Round [1]`** — the round boundary in the log is a **numbered header**, not a
  banner and not a per-combatant mark. That is a *third* treatment alongside the
  grey wash and the hourglass.

### ⚠ Three inconsistencies in shipped player text

Worth recording because this project hunts exactly this shape:

| | |
|---|---|
| `They rolled [3] (Critical Hit)` **vs** `[1] rolled [3] (Critical Miss)` | sibling strings, one uses a pronoun and one repeats the name |
| `[1] died.` **vs** `[1] has died` | two forms, and only one has a full stop |
| `[1] used [2] on themselves.` **vs** `[1] used [2] on self.` | **two phrasings for the same event** |

**A keyed string table does not prevent this** — it only makes it findable. Our
`check_player_strings` is the instrument that would.

### PT-1496

1. **What does it do?** Keeps every log line as an authored template with
   numbered holes, uses **one sentence shape for all three d20 rolls**, and logs
   the derivation rather than hiding it in a tooltip.
2. **Why?** Because a log is read after the fact, when the tooltip is gone. **A
   line that says only the outcome cannot be audited**; one that says *needs 14,
   rolled 11* can.
3. **Does the reason still hold for us?** **Yes, and it is `PT-1326` almost word
   for word.** ⚠ **Where it does not transfer:** BG3 has *two* surfaces and we
   have one line doing both jobs — so adopting the wording without the split
   makes our unbounded working line longer, not better. **The grammar is safe to
   take; the volume is not.**
4. **What is the modern form?** **One sentence shape for every check** —
   *needs N to VERB, rolled M* — with the verb naming the kind of roll, and the
   critical case appended in parentheses rather than given its own sentence. And
   ⚠ **log the round as a numbered header**: cheap, unambiguous, and it needs no
   portrait, no strip and no icon.

---

## 4 · Correction filed against `STUDY 20`

**Done in that file, at the owner's instruction.** `STUDY 20 §5` recorded
`libssl.so.1.1` as *the* blocker. **It is the first of at least two.**

`Tester` cleared the loader half — sniper's `libssl.so.1.1` and
`libcrypto.so.1.1` copied to a scratch dir with `LD_LIBRARY_PATH` pointed at it
**removes the loader error entirely.** The game still does not open a window:
**`bg3` spawns `steam.sh` to relaunch itself and parks as a single sleeping
thread**, and Steam's console shows it failing twice before `Tester` arrived.

⚠ **The shape of my error is the same one this series keeps producing: a correct
finding mistaken for a complete one.** Not attempted again, per the brief.

---

## 5 · What was NOT checked — scoped

* **Nothing was launched.**
* **The `.ncs` scan is a byte-pattern match, not a disassembly.** `05 00 01 43`
  is `ACTION` + routine 323; **a call built some other way would be missed**, and
  the pattern could in principle occur inside a string constant. The control
  (routine 42, 4,398 hits) shows the method works; it does not prove
  completeness.
* **The 25 module hits were not read** — they are identified by name only.
  `k36_spn_destrdth` and `k_pdan_nemo01` are the interesting ones and were not
  decompiled.
* **K2 was not re-run for any of `§1` or `§2`** — the `SetIsDestroyable` survey,
  the GIT scan and the bytecode scan are **K1 only**.
* **`k_inc_generic` was not read.** `k_hen_spawn01` includes it, and
  `k_ai_master` is built on it; **a body-related call could live there** and
  would have been caught by the bytecode scan only if compiled into a script that
  ships.
* **Whether the engine default is "persist" or "fade" was not established from
  files.** The evidence is indirect: `k_def_spawndead` sets `FALSE` explicitly
  for scenery, and enemies are lootable in play — **but "enemies are lootable" is
  a memory of playing, not a file, and is not relied on above.**
* **No BG3 log line was seen rendered** — the templates are read, their
  assembly order and which fill which `[n]` is not.
* **`english.loca` was searched by regex over values**, so a template phrased
  unusually would be missed. 232,878 strings; the searches in `§3` are the ones
  named and no more.
