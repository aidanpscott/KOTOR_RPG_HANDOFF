# STUDY 32 — does BG3 need a combat roster?

**Files only. `Game.pak` GUI layouts, `Shared.pak` stats, `english.loca`.
The companion to `STUDY 31`, which found KOTOR has none.**

> **Answer: YES, and it is explicit. The two games are opposite shapes on every
> one of the four questions.**

---

## 1 · ⚠⚠ BG3 HAS A COMBAT SESSION OBJECT WITH A PARTICIPANT LIST

`Mods/MainUI/GUI/Pages/CombatantsOverlay.xaml`:

| line | binding | what it proves |
|---|---|---|
| **391** | `CurrentPlayer.SelectedCharacter.Combat.Participants.Count` | ⚠⚠ **a `Combat` object, with a `Participants` collection** |
| 392 | `CombatParticipantsChangedCommand` | membership change is **an event** |
| 35 | `<ListBox ItemsSource="{Binding Combatants}">` | the panel reads a **collection** |
| 289 | `DataTrigger Binding="{Binding CurrentCombat, Converter=NullToBoolFalseConverter}"` | **the overlay exists iff `CurrentCombat` is non-null** |
| 319–374 | `IsSharedCombat` (×6) | ⚠ **combats can be *shared*, so there can be more than one** |

**`SelectedCharacter.Combat` — combat hangs off the character, and characters can
be in *different* ones.** `IsSharedCombat` is the flag for when they are not.
**KOTOR cannot express any of this**; `GetIsInCombat` is one boolean and there is
nothing to be a participant *of*.

### The stats layer says the same thing, in a closed vocabulary

`Public/Shared/Stats/Generated/Structure/Base/ValueLists.txt:1219`,
`valuelist "StatusPropertyFlags"` — 39 values, four of which are membership:

```
value "InitiateCombat"               : 2
value "BringIntoCombat"              : 3
value "AllowLeaveCombat"             : 11
value "AllowLeaveDisallowJoinCombat" : 36
```

> **⚠⚠ `BringIntoCombat` is the decisive word. You cannot *bring into* something
> that is not a container.** And `AllowLeaveDisallowJoinCombat` is a **third**
> membership state — out, and barred from returning — which is unthinkable
> without a roster.

### And the single cleanest proof, from the string table

`english.loca` carries, verbatim:

```
Flee failed: not in combat
```

**The game can tell you, as a binary fact, that you are not in combat.** That is
a membership test with a user-visible failure message.

> **Answer to the load-bearing question: this is NOT a second confirmation of
> KOTOR's shape. It is the counter-example.** One engine derives membership, the
> other stores it.

---

## 2 · THE PANEL SHOWS THE ROSTER, NOT WHAT IS VISIBLE

**`ItemsSource="{Binding Combatants}"`** — the list binds to the collection, and
nothing else.

**Scoped negative, and it is a clean one:** searched all three combat UI files —
`CombatantsOverlay.xaml`, `TurnOrderLib.xaml`, `TurnModeInfo.xaml` — for
`IsVisible`, `Seen`, `Sight`, `Hidden`, `Invisible`, `Detect`, `LineOfSight`,
`Obscur`, `Sneak`, `Stealth`.

**No visibility filter exists in any of them.** The only `Hidden` hits are
`LeftHiddenCounter` / `RightHiddenCounter` — the **overflow counters** from
`STUDY 21 §4`, which count combatants that do not fit *on screen*, not ones you
cannot *see*. The only `Visibility=` bindings are to `ConcentrationSpell` and
`StatusEffects.Count`.

> **⚠ So in BG3 you absolutely can be "fighting" an enemy you cannot currently
> see, and the panel keeps showing it.** Membership persists through cover,
> corners and darkness. **This is the exact opposite of `STUDY 31 §3`**, where
> KOTOR's party disengages the moment `GetNearestCreature(…, PERCEPTION_SEEN)`
> returns nothing.

**⚠ One honest limit:** the XAML proves the panel reads a collection named
`Combatants` on a combat object. **It cannot prove that collection is
unfiltered** — the view-model could filter it before binding. **What is proved is
that no filtering happens in the UI layer**, and that the vocabulary the UI uses
is membership, not sight.

---

## 3 · WHAT STARTS COMBAT — ⚠ THE MAIN TRIGGER IS NOT IN THE FILES

**Stated plainly rather than guessed, as asked.**

**`STUDY 31` could answer this for KOTOR because KOTOR's combat start is in a
SCRIPT** — `k_ai_master` case 1002, readable line by line. **BG3's equivalent is
engine code.** There is no `.txt`, `.lsx` or `.xaml` in anything opened that
contains the "I see an enemy, begin combat" decision.

**What IS in the files is a second, effect-driven path:**

| flag | statuses carrying it | what they are |
|---|---|---|
| **`InitiateCombat`** | **28** | `BLADE_BARRIER` · `HARM` · `INSECT_PLAGUE_AURA` · `SUNBEAM` · `PHANTASMAL_KILLER` · `TERRIFIED` · `EYEBITE_SICKENED` … |
| **`BringIntoCombat`** | **19** | `WALLOFFIRE` · `WALLOFTHORN` · `VORTEX_AURA` · `BLADE_BARRIER_AURA` · `SPREADING_SPORES` … |

**⚠ Read the second list: they are almost all AURAS AND WALLS.** Persistent area
effects. **Walking into one pulls you into the combat that already exists** —
which is precisely the operation a roster makes possible and KOTOR has no way to
express.

**And `STUDY 19` found the range-aware hooks**: `Interrupt.txt` carries
`OnEnterAttackRange` and `OnLeaveAttackRange` as interrupt contexts — **but those
fire reactions, not combat start.**

> **⚠ So: comparable to KOTOR's perception trigger? Unknown, and not answerable
> from files.** What can be said is that **BG3 has at least one combat-start path
> KOTOR structurally cannot have** — a status that adds a creature to an existing
> fight.

**⚠ Turn-based does not appear to change the *trigger*, only the presentation.**
`inputorder.json` (`STUDY 19 §4`) binds `UIEnterTurnBased`, `UILeaveTurnBased` and
`ToggleCombatMode` as **player-facing keys**, and `english.loca` has
**`Leave Turn-Based Mode`** — so **turn-based mode is a display/pacing state the
player can toggle, distinct from combat membership.** You can be in turn-based
mode outside combat.

---

## 4 · LEAVING WITHOUT DYING IS AN EXPLICIT, GATED PLAYER ACTION

`english.loca`, verbatim:

```
Flee from Combat
Flee Combat
Flee failed: not in combat
Flee failed: enemies too close
Flee failed: no safe waypoint shrines
Flee to your camp.
```

**Three named failure conditions**, and they are the design:

* **`not in combat`** — ⚠ the membership precondition, `§1`.
* **`enemies too close`** — ⚠ **a distance gate.** You cannot flee from an
  adjacent enemy.
* **`no safe waypoint shrines`** — ⚠⚠ **fleeing is an EXTRACTION TO A
  DESTINATION, not a walk-away.** It needs somewhere to put you.

**Compare `STUDY 31 §4`:** KOTOR's disengage is
`CancelCombat(); ClearAllActions(); ActionFollowLeader()` — **no cost, no gate,
no destination, and mostly triggered by a conversation starting.**

> **That is what a roster costs.** KOTOR can drop a creature out of "combat"
> because combat was never a thing to be in. **BG3 must define an exit, gate it,
> and give it somewhere to go.**

**⚠ Scoped negative:** `AllowLeaveCombat` and `AllowLeaveDisallowJoinCombat`
appear in the `StatusPropertyFlags` vocabulary and are carried by **zero statuses
in `Shared.pak`** — searched all 68 extracted stat files. They may be used in
`Gustav.pak` or engine-side; **not found where it was looked.**

---

## 5 · WHAT THIS MEANS FOR US — AND THE OWNER'S INSTINCT IS RIGHT, WITH ONE TWIST

**Two engines, two shapes, and the difference is not arbitrary:**

| | KOTOR | BG3 |
|---|---|---|
| membership | **derived**, per creature, from `PERCEPTION_SEEN` | **stored**, `Combat.Participants` |
| panel shows | one target (`PB_HEALTH`) | the roster (`Combatants`) |
| out of sight | **drops out of combat** | **stays on the panel** |
| leaving | free, usually via dialogue | gated action with a destination |
| concurrent fights | meaningless | `IsSharedCombat` |

### ⚠⚠ Why BG3 needs one and KOTOR does not — and why it lands on us

**Turn order is the reason.** *"Whose turn is next"* is a question about an
**ordered sequence of participants**. KOTOR is real-time-with-pause and never has
to answer it; BG3 is turn-based and answers it every round.

> **⚠ We are turn-based. So we need something roster-shaped, and `STUDY 31`'s
> "no roster is the correct model" does NOT survive contact with turn order.**
> I should say that plainly, because `STUDY 31 §6` argued the other way from a
> real-time anchor.

### But the query-vs-store distinction survives, and it is the useful half

**A roster and a *stored mutable* roster are different things.** What turn order
needs is **an ordered list of participants at the current round** — and
`PLAY-STATE-01` is already a projection over the log.

* **Derive the roster**, the way `PLAY-STATE-01` derives everything else. Joining
  and leaving are **events**, and the participant list at any moment is a fold.
  ⚠ **BG3 agrees more than it looks**: `CombatParticipantsChangedCommand` fires
  on change — **membership is eventful there too**, and the collection is what the
  UI reads, not necessarily where the truth lives.
* **⚠ Do not make visibility the membership rule.** KOTOR's disengage-on-lost-sight
  is a *real-time* answer; on a turn-based grid it would let a player break combat
  by stepping behind a pillar. **BG3's separation is right for our shape** — you
  stay in the fight when you cannot be seen.
* **Which means our panel question has an answer**: show **who is in the fight**,
  and treat *visible* as a **display property of a row**, not a filter on the list.
  ⚠ Otherwise an enemy that steps out of sight vanishes from the panel and the
  player cannot tell "gone" from "hidden" — **which is this project's
  absence-versus-blank problem, in a new place.**
* **Steal the exit, not the flee.** BG3's three failure messages are worth more
  than its mechanism: **naming *why* you cannot leave** is the transferable part,
  and `STUDY 21 §2` found the same habit in `CapabilitiesErrors`/`Cause`.

---

## 6 · What was NOT checked

* **The combat-start decision is engine code and was not found.** `§3`. Nothing
  here claims to know BG3's detection range, its perception model, or whether it
  has a reaction delay. **`STUDY 31`'s KOTOR figures have no BG3 counterpart.**
* **Whether `Combatants` is filtered before binding** — `§2`. The UI does not
  filter; the view-model is not readable.
* **`Gustav.pak` was not searched** for `AllowLeaveCombat` users, nor for
  campaign-specific combat statuses. **`Shared.pak`'s 68 stat files only.**
* **No Osiris script was read.** BG3's story scripting (`.osi`/goal files) is where
  scripted combat starts would live, and **none was opened** — the analogue of
  `STUDY 31`'s inference from KOTOR module script *names*.
* **`TurnOrderLib`/`TurnModeInfo` were searched for visibility terms only**, not
  re-read in full; `STUDY 21 §4` covered their structure.
* **Nothing was played.** `STUDY 20 §5` records BG3 as unrunnable on this machine
  with no route, and that stands.
* ⚠ **`IsSharedCombat` is read as "more than one combat can exist".** That is the
  natural reading of a flag distinguishing shared from not-shared, **but no file
  states it**, and the alternative — shared between *players* in multiplayer — is
  not excluded. `Data.LocalPlayers` appears twice in the same file, which is
  evidence for the multiplayer reading.
