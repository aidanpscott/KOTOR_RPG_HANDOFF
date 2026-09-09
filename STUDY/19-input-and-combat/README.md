# STUDY 19 — Input and combat interaction, across three games

**Method: `PT-1496`, four questions — what did they do · why · does that reason
still hold · what is the modern form of it.** The anchor is **KOTOR**. NWN is
read as the ancestor and BG3 as the modern contrast, neither as a thing to copy
over it.

**⚠ Files only. Nothing was played.** Where a question could only be answered
by watching the game, it is marked and left unanswered rather than inferred
from data.

---

## 0 · What was read, and with what

| Game | Read from | Container |
|---|---|---|
| KOTOR 1 | `/mnt/ga/SteamLibrary/steamapps/common/swkotor` | `chitin.key` → 26 BIFs, **25,836 resources**, 209 `.2da` |
| KOTOR 2 | `…/Knights of the Old Republic II/steamassets` | `chitin.key` → 11 BIFs, **18,439 resources**, 424 `.2da` |
| NWN:EE | `…/Neverwinter Nights/data` | `nwn_base.key` → 60 BIFs, **113,483 resources**, 597 `.2da` |
| BG3 | `…/Baldurs Gate 3/Data` | 49 `.pak` (LSPK v18); `Shared.pak` = **11,147 entries** |

### ⚠ The brief's premise was wrong about the machinery

The brief says *"previous studies read them with our own readers — chitin.key,
BIF, GFF, 2DA. That machinery exists."*

**The BIF half does not exist.** `MAIN_WORK/scripts` has `gff.py`, `gffparse.py`,
`parse2da.py`, `archive.py`/`container.py` (ERF/RIM/MOD) and `tlk.py`. It has
**no KEY reader and no BIF reader**, and neither does any other repo — scoped:
grepped all six repos for `BIFF`, `chitin`, `KEY V1` across `*.py` and `*.dart`,
zero hits. Prior studies worked from **25 loose `.2da` files in `HANDOFF/data/`**
extracted by some route that left no script, with `HolocronToolset` present in
the Steam library as the likely tool.

So `tools/keybif.py` was written for this study. It is a reader, not product code.

### ⚠ Two 2DA formats, not one

KOTOR ships **`2DA V2.b`** (binary — `parse2da.py`). **NWN:EE ships `2DA V2.0`**
(plain text, shlex-quoted). Detected from the magic, not from the game.
`tools/d2.py` handles both.

---

## 1 · ⚠ THE BG3 EXTRACTOR — reported before it was used

**Reported first, as ordered.** BG3 stores stats as plain text inside LSPK v18
archives. Reaching them takes three steps:

1. **Header** — `LSPK`, version, `FileListOffset`, `FileListSize`. No dependencies.
2. **File list** — LZ4-**block**-decompress `Shared.pak`'s 385,188 bytes into
   `11,147 × 272` entry records.
3. **Per file** — seek, then decompress by a per-entry flag: `0` stored ·
   `1` zlib · `2` lz4 · `3` zstd.

**What this machine had:**

| need | status |
|---|---|
| zlib | ✓ stdlib |
| zstd | ✓ `/usr/bin/zstd` |
| **LZ4 block** | ✗ no `lz4` module, no `lz4` CLI |
| LSLib / `divine` | ✗ absent, and no `mono`/`dotnet` — `wine` alone cannot run it |

**One piece was missing and finishing the download would not supply it.** The
owner was asked and chose a **pure-Python LZ4 block decoder** (`tools/lz4block.py`,
stdlib only, nothing installed) over `pip install lz4`. That matches the project's
own practice: `archive.py`, `parse2da.py` and `gff.py` are all hand-written
readers rather than dependencies.

**⚠ The install state was a red herring, and was measured rather than assumed.**
At the time of asking, Steam reported 93% and the final `Data/` directory was
empty — but every archive needed was **already complete** in
`steamapps/downloading/1086940/Data/`, proved by `FileListOffset + FileListSize
== filesize` **exactly** on `Shared.pak`, `Gustav.pak`, `GustavX.pak`,
`Engine.pak` and `Patch8_HotFix9.pak`. Steam committed the move mid-study; the
read would have worked either way.

---

## 2 · QUESTION 1 — HOW YOU SAY "HIT THAT ONE"

**⚠ The differences are the finding, and they are large.** All three ship a
`keymap` table, and the table itself is the evidence.

| | NWN `keymap.2da` | KOTOR 1 `keymap.2da` | KOTOR 2 | BG3 `inputconfig.json` |
|---|---|---|---|---|
| shape | **4 columns**, 72 rows | **22 columns**, 79 rows | **23 columns**, 81 rows | JSON dict, ~120 events |
| columns | `ActionStrRef · Language0 · Page · Name` | + `remappable`, `forcedisplay`, six `ic*` context flags, `repeatable/repeatwait/repeatrate`, `scale/scalemag/scaleexp`, `character`, `sortpos`, `disabled` | K1 + `eventtype` | binding → list of chords |

### The three answers

**NWN — targeting is a MODE, opened per object.** Nine of its 72 rows are the
radial menu: `RadialSW · RadialS · RadialSE · RadialW · RadialCancel · RadialE ·
RadialNW · RadialN · RadialNE`, plus `ActivateOwnRadial`. You point at a thing,
open a radial on it, and pick a compass direction. **The verb list is built from
the object you opened it on.** Also present and **entirely unbound**:
`CombatStepLeft/Right/Front/Back` — modelled, never given a key.

**KOTOR — targeting is persistent SELECTION plus a three-slot verb bar.**
`SelectPrev` (Q) and `SelectNext` (E) cycle the target; `TargetLeftAct` (1),
`TargetMiddleAct` (2) and `TargetRightAct` (3) fire one of three actions **at
whatever is currently selected**. Alongside sit four *personal* slots —
`PersonalPowerAct` (4), `PersonalMedicalAct` (5), `PersonalOtherAct` (6),
`PersonalMinesAct` (7) — which need no target. Plus `DefaultAction` (R),
`CancleCombat` (F — misspelled in shipped data), `ClearOneAction` (Y),
`Flourish` (X).

**BG3 — one context-resolved verb, or verb-first from a hotbar.** There is **no
"attack" binding at all**. `Action1` is bound to `mouse:left` and resolves
against whatever is under the cursor. The alternative is verb-first:
`UISelectSlot1`…`UISelectSlot12` pick the action, then you click the target.
`CycleCharactersNext/Prev` cycle the *actor*, not the target — the inverse of
KOTOR's Q/E.

**So: NWN is noun→menu→verb. KOTOR is noun→verb, verb pinned to a slot. BG3 is
either verb→noun or one click that means whatever the target implies.**

### ⚠ KOTOR's input CONTEXTS are data, and this is the transferable part

K1's six `ic*` columns declare, per binding, where it is live: `icpc` (normal
play) · `icminigame` · `icpcgui` · `icdialog` · `icfreelook` · `icmovie`. A
binding is not global — it is **scoped to a mode, in the table, per row**. The
nine `Dialog1`–`Dialog9` rows are `icdialog=1` and nothing else.

### PT-1496 — the four questions

1. **What did they do?** Selection is a persistent noun (Q/E), the verb is one
   of three target-slots or four personal slots, and every binding declares
   which input contexts it is live in.
2. **Why?** KOTOR is real-time-with-pause on a gamepad-shaped control budget.
   A radial menu (NWN's answer) needs a mouse and a pause; three fixed slots
   need neither. The `ic*` columns exist because the same physical key had to
   mean different things in dialogue, minigames and movies.
3. **Does the reason still hold?** **Partly.** The context-scoping reason holds
   completely and is stronger for us — we already have area, dialogue and combat
   as distinct surfaces. The three-slot limit was a 2003 screen-space and
   gamepad constraint; `PT-1340` already ruled we are not bound by Aurora's
   constraints, only its answers.
4. **What is the modern form?** **A binding carries the mode it is live in**,
   the way `icpc/icdialog/icminigame` do. And **selection is state, not a
   gesture** — KOTOR's Q/E survive because the selected target persists across
   actions, which is exactly what `PT-1443`'s click-to-move-with-keys needs.

---

## 3 · QUESTION 2 — WHAT A COMBAT ACTION IS AS DATA

### ⚠ In KOTOR and NWN, an "action" carries nothing mechanical at all

`actions.2da` has **three columns in both games**: `label · string_ref · iconresref`.

* NWN: **44 rows**
* KOTOR 1: **39 rows**

**Rows 0–38 are label-for-label identical**, including four D&D concepts with no
Star Wars meaning that KOTOR shipped anyway — `AnimalEmpathy`, `SmiteEvil`,
`QuiveringPalm`, `StunningFist` — and **including the same two blank holes at
rows 24 and 27**. KOTOR inherited NWN's action enum verbatim. KOTOR 2 has no
`actions.2da` at all.

**No cost. No target type. No range. No interrupt. `actions.2da` is a display
table and an engine enum, and nothing else.** It answers the owner's question
directly: *what did they carry per action?* — **nothing.**

### Where the cost actually lives — the control on the above

Cost is on the **ability**, not the action. K1 `spells.2da` is 53 columns; the
load-bearing ones are:

| field | what it carries | K1 spread over 132 rows |
|---|---|---|
| `forcepoints` | the **one** pool cost | **4 price points** — 10, 15, 20, 25 (87 rows are 0) |
| `range` | a single letter into `ranges.2da` | `T` 52 · `M` 28 · `P` 14 · `S` 13 · `L` 12 · `W` 2 |
| `category` | AI targeting class, **a hex bitmask** — `0x1808`, `0x2441` | — |
| `conjtime`/`casttime`/`catchtime` | milliseconds | see the control below |
| `forcehostile`/`forcefriendly` | AI priority integers | — |
| `pips` | UI tier dots | 1–3 |

`feat.2da` (60 columns) carries the melee side: `usesperday`, `targetself`,
`hostilefeat`, `usetype`, `category`, plus 24 per-class grant columns.

### ⚠⚠ CONTROL — a field modelled per-action that 97% of actions never vary

`casttime` looked uniform by eye across the first 42 rows, so it was counted
across all of them rather than trusted:

| | K1 (132 powers) | K2 (282 powers) |
|---|---|---|
| `casttime` | **128 × `1330`**, then 1940, 1500, 0 | **216 × `1330`**, 5 others |
| `conjtime` | **125 × `170`**, then 0, 560 | 214 × `170` |
| `catchtime` | **130 × `0`**, 2 × 500 | 280 × `0` |

**KOTOR modelled per-action timing and then gave essentially every action the
same value.** The only real outliers are Lightsaber Throw (560/1940/**500** —
the sole non-zero `catchtime`, because the sabre has to come back) and Force
Jump. **The interruptible window exists as a field and not as a design.**

### BG3 — the same question answered with 136 fields

**1,764 spell entries** across nine `Spell_*.txt` files, **136 distinct data
fields**. An action is a record with a prototype chain.

**⚠ CONTROL — inheritance made the first count wrong by a quarter.** 1,533 of
1,764 entries declare `using "<parent>"` and inherit every field they do not
restate. Counting raw `data` lines gave **1,079** entries with `UseCosts`;
resolving the chain gives **1,346** (+267), and `ActionPoint` moved 854 → **1,066**.
A further **32** entries set `UseCosts ""` explicitly — *free* stated as a value,
distinct from unset. (That is this project's absence-versus-blank distinction,
made by the source.)

**Four cost fields, because price depends on circumstance:**

| field | entries | what it means |
|---|---|---|
| `UseCosts` | 1,314 | paid to start |
| `HitCosts` | 53 | paid **only on a hit** — Bardic Inspiration, Superiority Die |
| `RitualCosts` | 8 | a different price **out of combat** |
| `DualWieldingUseCosts` | 2 | a different price **while dual-wielding** |

**16 distinct resources**, and the shape of the distribution matters more than
the list: `ActionPoint` 1,066 · `SpellSlotsGroup` 909 · `BonusActionPoint` 256 ·
`KiPoint` 44 · `ReactionActionPoint` 28 · `Movement` 14 · `WildShape` 14 ·
`ChannelDivinity` 10 · `SuperiorityDie` 9 · `BardicInspiration` 6 ·
`ChannelOath` 4 · `SorceryPoint` 3 · `ArcaneRecoveryPoint` 2 ·
`NaturalRecoveryPoint` 2 · `Rage` 1 · `FungalInfestationCharge` 1.

**Three resources carry 96% of the traffic and thirteen are long-tail.** Cost is
written as a string expression — `"ActionPoint:1;SpellSlotsGroup:1:1:4"`,
`"Movement:Distance*0.5"` — not as numeric columns.

### ⚠⚠ What can interrupt an action — and this answers an OPEN BLOCKER

`STATE.md` carries: *"⚠⚠ **A reaction has no home and no format** —
`ATTACHMENT-01 §3` specifies `on: <kind> then: <response>` and nothing says
where one is declared. `BUILD 34`'s stop."*

**BG3 declares reactions as their own top-level record type.**
`Public/Shared/Stats/Generated/Data/Interrupt.txt` — **122 entries**, `type "InterruptData"`.
A worked example, verbatim:

```
new entry "Interrupt_ControlledChaos"
type "InterruptData"
data "InterruptContext"      "OnSpellCast"
data "InterruptContextScope" "Nearby"
data "Container"             "YesNoDecision"
data "Conditions"            "IsAbleToReact(context.Observer) and not Self(...) and Enemy(...) and IsSpell() and not Uninterruptible()"
data "Properties"            "TriggerRandomCast(OBSERVER_SOURCE,1,0,WildMagicEvil);UseSpell(...)"
data "Cost"                  "ReactionActionPoint:1"
data "InterruptDefaultValue" "Ask;Enabled"
data "EnableCondition"       "not HasStatus('SG_Polymorph') or ..."
data "EnableContext"         "OnStatusApplied;OnStatusRemoved"
```

**The trigger vocabulary is a closed set of seven**, and it is small:
`OnCastHit` 16 · `OnPostRoll` 14 · `OnSpellCast` 8 · `OnPreDamage` 4 ·
`OnPostRoll;OnPreDamage` 1 · `OnEnterAttackRange` 1 · `OnLeaveAttackRange` 1.
**Scope is two values** — `Self` 33, `Nearby` 14.

**⚠ `ATTACHMENT-01 §3`'s `on:`/`then:` is two of BG3's fields. BG3 carries five more:**

* **`InterruptContextScope`** — whose event am I watching, mine or a neighbour's
* **`Cost`** — a reaction is **paid for** (`ReactionActionPoint:1`, sometimes plus a spell slot)
* **`InterruptDefaultValue`** — `Ask;Enabled` (37) vs `Enabled` (9): **whether the game stops and asks the player, or fires it silently, is authored per reaction**
* **`Container`** — how the prompt is presented; **all 45 are `YesNoDecision`**
* **`EnableCondition`/`EnableContext`** — when the reaction is even *eligible to be listed*, separate from when it fires

**KOTOR and NWN have no equivalent.** Scoped: no `interrupt`/`reaction` table in
K1's 209, K2's 424 or NWN's 597 `.2da` names; the concept lives in hardcoded
attack-of-opportunity behaviour, not in data.

### PT-1496 — the four questions

1. **What did they do?** KOTOR made the action table an icon-and-label enum and
   put every mechanical fact on the *ability* — one pool (`forcepoints`), four
   price points, a letter range, a hex targeting bitmask, and three timing
   fields it then held constant.
2. **Why?** Because in real-time-with-pause **the round is the budget and the
   clock is the cost.** There is no action economy to model: you queue, the
   round ticks, the animation takes the time it takes. Cost is only ever *"can I
   afford the points"*, so one pool is enough.
3. **Does the reason still hold?** **No, and this is the sharpest divergence in
   the study.** `PT-1423` gives us a **turn with five budgets**. The moment
   spending is discrete and plural, KOTOR's answer stops transferring — a
   three-column action table cannot say which of five budgets a thing costs.
   **KOTOR is the anchor for feel and is the wrong model for this one field.**
4. **What is the modern form?** BG3's, reduced. **Cost belongs on the action, as
   a named-resource expression rather than numeric columns** — `ActionPoint:1`
   scales to five budgets where a column per budget does not. Two of BG3's four
   cost fields are worth having (`UseCosts`, and the *circumstance* idea behind
   `HitCosts`/`RitualCosts`); `DualWieldingUseCosts` at 2 entries is not a
   pattern. And **`InterruptData` is the format `ATTACHMENT-01 §3` is missing** —
   with `Cost` and `Ask`-vs-`Enabled` the two fields we would otherwise have
   discovered late.

---

## 4 · QUESTION 3 — MOVEMENT

### ⚠⚠ Neither KOTOR nor NWN prices ground. At all.

`surfacemat.2da` — the table that describes every walkable surface:

| | KOTOR 1 | NWN |
|---|---|---|
| rows | 31 | 31 |
| columns | `label · walk · walkcheck · lineofsight · grass · sound · name` | `Label · Walk · WalkCheck · LineOfSight · Sound · Name · IsWater · Visual · Act1_Strref · Act1_Icon` |

**`walk` and `walkcheck` are booleans, and there is no cost column in either
game.** Read the rows that ought to be expensive:

```
 3  Grass    walk=1     9  Carpet   walk=1
 4  Stone    walk=1    12  Swamp    walk=1
11  Puddles  walk=1    13  Mud      walk=1
14  Leaves   walk=1     6  Water    walk=1
```

**Swamp, Mud, Puddles, Leaves and Water carry values identical to Stone and
Carpet.** The only distinctions a surface can make are *can you walk on it*,
*does it block sight*, and *what sound does a footstep make*. NWN adds `IsWater`
and a footstep `Visual` and still prices nothing.

Speed is a property of the **creature**, in metres per second — `creaturespeed.2da`:

| | walkrate | runrate |
|---|---|---|
| KOTOR `PC_Movement` | 3.20 | 5.40 |
| NWN `PC_Movement` | 2.00 | 4.00 |

**Movement is continuous distance over time, never a per-square charge.**
`ranges.2da` is metres too — `SpellRngShrt` 10, `Med` 15, `Lng` 28;
`WeaponRngShrt` 10, `Med` 30, `Lng` 50.

*(Aside for `FLAWS`: K1 replaced NWN's `Snow`, `Sand`, `Barebones` and
`StoneBridge` with ten placeholder rows literally labelled `CRAP`, shipped at
retail. NWN's equivalent placeholders are labelled `Temp`.)*

### BG3 — movement is a spendable resource, and difficult ground is a STATUS

Movement is one of the 16 resources, spent in **metres**:

```
"Movement:Distance"        pay what you actually travelled
"Movement:Distance*0.5"    travel at half price
"Movement:3"  "Movement:5"  "Movement:9"  "Movement:15"    flat charges
"ActionPoint:1;Movement:15"    an action that costs BOTH
```

**Difficult ground is not a property of the tile.** It is a status applied to
the creature standing in it, carrying a multiplier on the Movement resource:

```
new entry "PLANT_GROWTH"
type "StatusData"
data "Boosts"       "ActionResourceConsumeMultiplier(Movement, 4,0)"
data "StatusGroups" "SG_DifficultTerrain"
```

The named instances are `DIFFICULT_TERRAIN_MUD`, `_WEB`, `_VINES`,
`_OVERGROWTH`, `_DEEPWATER`. **They are all filed under one status group**, so
Freedom of Movement does not enumerate five terrain types — it says
`StatusImmunity(SG_DifficultTerrain)` once. A second, separate axis,
`PathInfluence`, sits on the **character** and weights 33 surfaces for
pathfinding — `Lava,700`, `Mud,30`, `Web,30`, `SpikeGrowth,40`.

**⚠ Not asserted:** whether `PathInfluence` also charges movement or only steers
the pathfinder. The name says influence, the values look like avoidance weights,
and **that distinction cannot be settled from these files.**

### PT-1496 — the four questions, and this one answers the owner directly

The owner asked: *"Ours currently spends a flat 1 per square and difficult
ground costs nothing though its own doc says otherwise. What did theirs cost,
and what did it cost to SAY so?"*

1. **What did they do?** KOTOR charged **nothing per square**, because it has no
   squares — movement is metres per second and terrain is a walkability bit.
   **The cost to SAY difficult ground exists was: they never said it. There is
   no field.** BG3 charges metres from a per-turn pool and expresses difficult
   ground as a status carrying `ActionResourceConsumeMultiplier(Movement, N)`.
2. **Why?** KOTOR is continuous and real-time; a per-square price is
   unrepresentable and terrain variety was spent on footstep sounds instead —
   the `sound` column is the one thing `surfacemat` genuinely varies. BG3 is
   discrete and turn-based, so a cost multiplier is both meaningful and cheap.
3. **Does the reason still hold?** **For us, no.** We are grid-and-turn, which
   is BG3's shape, not KOTOR's. **KOTOR's silence here is not an answer we can
   inherit** — and it is worth naming that **our current behaviour matches
   KOTOR exactly** (flat cost, free difficult ground). **The document is the
   outlier, not the code.** Whether the doc or the code is wrong is the owner's
   call and is not decided here.
4. **What is the modern form?** **Do not put the cost on the tile.** BG3's move
   is that the multiplier rides on the *creature*, grouped, so one immunity
   clears every source at once — which is exactly the shape that makes
   Force Speed, a swamp and a web compose instead of fight. A `cost` column on a
   tile type cannot do that.

---

## 5 · QUESTION 4 — KEY BINDINGS AS A SURFACE

### ⚠⚠ KOTOR refuses in TWO places, and they are different refusals

This is the finding. KOTOR models the verb side and the key side as separate
tables, each with its own veto.

**`keymap.2da.remappable` — this ACTION may not be reassigned.**
Refused in K1: `MoveForward`, `MoveBack`, `StrafeLeft`, `StrafeRight`,
`RightLookabout`, `AlternateActions` (LeftShift), `AlternateActions2`
(RightShift), `GUI` (Escape), `Pause`, **`Dialog1`–`Dialog9`**, and the four
minigame arrows.

**`bindablekeys.2da.bindable` — this KEY may not be assigned to anything.**
85 rows in K1 (103 in K2). **Nine are refused**, and they are precisely the keys
the interface needs unconditionally:

```
KEYBOARD_RETURN        KEYBOARD_LEFT_ARROW    KEYBOARD_RIGHT_ARROW
KEYBOARD_UP_ARROW      KEYBOARD_DOWN_ARROW    KEYBOARD_LEFTSHIFT
KEYBOARD_RIGHTSHIFT    KEYBOARD_ESC           KEYBOARD_PAUSE
```

**Everything else — all 26 letters, all digits, F1–F12, the numpad, Tab, Home,
End, Insert, Delete, PrintScreen, CapsLock, Space, both Alts, both Ctrls — is
open.** The refusal is small, specific, and justified by the UI needing those
keys to still work while you are rebinding.

### ⚠ `forcedisplay` — the good idea

`Escape` (`GUI`) and `Pause` are `remappable=0` **and** `forcedisplay=1`: shown
in the options screen precisely *because* they cannot be changed. **The list is
teaching the controls, not just editing them.** An un-rebindable key that is
hidden is a key nobody learns.

### ⚠ `disabled=1` — shipped and switched off

Nineteen K1 rows are disabled, and they are a cut feature visible in data: the
whole **`ActionMenu*` family** (`Left`, `Right`, `Up`, `Down`, `Queue`,
`RemoveQ`, `ShowMenu`) — a keyboard-driven action menu — and six `*Chg` rows on
F1–F6 (`DEFAULTChg`, `FEATSSKILLChg`, `HOSTILEPOWERChg`, `HOSTILEITEMChg`,
`FRIENDLYPOWERChg`, `minesMenuChg`) for re-assigning what a slot holds.

**⚠ Not asserted:** these rows are `disabled=1` in the shipped table, and the
four `MoveForward/Back/StrafeLeft/Right` rows are too. **Whether `disabled`
means "feature absent" or "not offered in the options list" cannot be settled
from the table alone**, and `swkotor.ini`'s `[Keymapping]` block uses a
different numbering (`Action204`–`Action286`, with `A`/`B` primary/secondary
pairs) that was **not** reconciled to these row indices. Flagged, not concluded.

### NWN — no refusal mechanism at all

NWN's `keymap.2da` is `ActionStrRef · Language0 · Page · Name`. **There is no
`remappable` column and no `bindablekeys.2da` in its 597 tables.** The only
grouping is `Page` (0–3). **KOTOR added the entire refusal apparatus.**

### BG3 — the refusal is expressed as a separate file

`Engine.pak/PlayerProfiles/Default/inputconfig.json` holds ~120 bindings.
`inputorder.json` holds **six categories** — camera, photo mode, world
interaction, combat/party actions, panels, and UI/system — listing ~95 events.

**A binding is rebindable if and only if it appears in `inputorder.json`.**
Everything in `inputconfig.json` but absent from `inputorder.json` is
unreachable: every `Widget*` and `UI*` internal, and the developer keys
`ForceKillApp`, `ReloadInputConfig`, `WidgetToggleDebugConsole`, `ToggleIK`.
**Same decision as KOTOR's `remappable` column, taken with file membership
instead of a flag** — and the *ordering* file doubles as the *grouping* and the
*permission*.

### PT-1496 — the four questions

1. **What did they do?** KOTOR vetoed twice — the action (`remappable`) and the
   key (`bindable`) — refusing nine keys of 85 and a short list of actions, and
   **displayed the un-rebindable ones anyway** (`forcedisplay`). NWN had no veto.
   BG3 replaced the flag with membership of an ordering file.
2. **Why?** Because the options screen is itself operated by keyboard. Enter,
   Escape and the arrows must keep working *while you rebind*, or the screen can
   lock the player out of their own game. Shift is refused for a different
   reason — it is the `AlternateActions` **modifier**, so binding it would
   collide with every chord.
3. **Does the reason still hold?** **Yes, entirely, and it is the one answer in
   this study that transfers with no modernisation at all.** We have no
   bindings and no settings screen (`PT-1443`), so the failure it prevents is
   still ahead of us, not behind us.
4. **What is the modern form?** **Two vetoes, not one** — a key can be reserved
   even where no action claims it, and an action can be fixed even where its key
   is free. Keep `forcedisplay`: show what cannot be changed. And take KOTOR's
   `ic*` columns with it — **a binding declares the contexts it is live in**,
   which is what makes `PT-1425`'s open problem tractable: walking-into-something
   as the attack affordance is a *combat-context* binding, and saying so in data
   is how that gesture gets re-answered without re-arguing it.

---

## 6 · Controls run against results that looked too strong

**`TRACE-112`'s rule applied three times, and it changed two answers.**

| result | why it looked wrong | what re-derivation showed |
|---|---|---|
| *"five BG3 archives are truncated"* | all five short by **exactly 8 bytes** — five identical coincidences is a reader bug, not five broken files | `FileListSize` **includes** the 8-byte count prefix. All five are **complete**; the check is `offset + size == filesize` exactly. **Reversed the answer.** |
| *"1,079 BG3 spells cost something"* | 685 of 1,764 costing nothing is implausible for a combat game | **1,533 entries inherit via `using`.** Resolved: **1,346** (+267); `ActionPoint` 854 → **1,066**. **Wrong by a quarter.** |
| *"KOTOR cast times are all 1330"* | eyeballed over 42 of 132 rows | Counted over all: **128 of 132**. **Confirmed, and sharpened into the finding** — the field is modelled and never varied. |

---

## 7 · ⚠ WHAT WAS NOT CHECKED — every negative scoped

**Read, not inferred** — every claim above comes from a file opened by
`tools/`. These are the gaps:

* **Nothing was played.** No claim about what the screen shows, how targeting
  *feels*, or what a cursor does on hover. `cursors.2da` (11 rows: Walk,
  XWalk, Attack, Magic, Talk, Examine, Use, NoUse, Trap, Transition) names ten
  cursor states but **what triggers each is engine behaviour and was not read**.
* **`swkotor.ini`'s `[Keymapping]` was not reconciled to `keymap.2da`.** The ini
  uses `Action204`–`Action286` with `A`/`B` suffixes; the 2DA uses row indices
  0–78. The mapping between them was not derived. **Every statement about
  default keys above comes from `keymap.2da`'s `language0`/`character`
  columns, not from the ini.**
* **KOTOR 2's ini carries no `[Keymapping]` section**, because this install has
  never been configured. Checked: `steamassets/swkotor2.ini` and
  `swplayer.ini`. **Not checked:** any per-user Aspyr config outside the install
  directory. K2's `keymap.2da` (81 rows, 23 columns) **was** read.
* **`disabled=1` was not resolved** — see §5. Whether those 19 rows are cut
  features or merely hidden from the options list is unsettled.
* **BG3 `PathInfluence`** — whether it charges movement or only weights
  pathfinding is **not determinable from these files**.
* **The `DIFFICULT_TERRAIN_*` status bodies were not located.** They are
  *referenced* in `Shared.pak` (`Character.txt` immunities, `Passive.txt`,
  `Status_BOOST.txt`) and **searched for in `Shared.pak` and `Gustav.pak`'s 21
  status files without a hit.** `PLANT_GROWTH` is a *different* status in the
  same group and is the source of the `×4` figure quoted. **Not checked:**
  `GustavX.pak`, `Patch8_HotFix9.pak`, `Engine.pak`, or the 44 other paks.
* **BG3's UI XML was not read.** `KeybindingOptions.xaml` and
  `KeybindingOptions_c.xaml` were located in `Game.pak` and **not opened** — so
  nothing here describes how BG3 *presents* rebinding, only which events it
  permits.
* **NWN's `nwnplayer.ini` was not read** — only `keymap.2da`. NWN:EE's runtime
  keybinding file lives in the user profile, not the install, and was not
  located.
* **`combatanimations.2da` (58 rows × 31 columns of parry/dodge/damage
  variants) was read for its shape only**, not analysed. It is the largest
  unexamined combat table in K1.
* **Modules were not opened.** No `.rim`/`.mod`/`.erf` was read in this study —
  all KOTOR/NWN findings come from `chitin.key`/`nwn_base.key` BIF resources.
  `archive.py` exists for that and was not needed.
* **K2 has no `actions.2da` and no `categories.2da`** — confirmed absent from
  its 424-table index, not merely unlooked-for.
