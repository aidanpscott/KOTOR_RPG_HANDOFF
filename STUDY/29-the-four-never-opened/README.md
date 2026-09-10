# 29 · The four never opened — and two corrections to my own studies

**From `Tester`.** Closes every hole named in `STUDY/28`'s appendix, plus the
owner's new question. **The Aurora work is done after this.**

**⚠ NOTHING WAS SAVED.** The NWN install held **8298 files** before and after,
newest mtime **2026-02-05**, unchanged. `Build Module` and `Test Module` stay
un-run. Every save prompt was answered *No*; the module title carried no
asterisk at the end. `Export` was opened and **cancelled before writing**.
`Resize Area` was opened and **cancelled before applying**. Nothing was
compiled.

---

## ⚠⚠ TWO CORRECTIONS TO STUDIES 26–28. Read these first

### 1 · **Aurora CAN resize an area. Our limit is a real gap.**

`24`, `25`. I wrote this **three times** — in `STUDY/26`, `27` and `28`:

> *"Tileset, Length and Width are disabled after creation — Aurora cannot resize
> an area either, so our same limit is not a gap we invented."*

**That is wrong.** Those fields are disabled *in Area Properties* because
resizing is **`Edit > Resize Area`**, a separate command with its own dialog —
Rows/Columns spinners, a live green preview, and the same Tiny/Small/Medium/Large
defaults as the Area Wizard (**one control, two entry points**). There is
**`Edit > Rotate Area`** beside it.

**⚠ So we were taking comfort we had not earned.** Our inability to resize an
area is a gap, Aurora closed it in 2002, and the control to copy is one we have
already documented.

*(And it gives no warning about tiles or instances outside the new bounds — in
the same program that says* **"There is no way to cancel this operation if you
start"** *on `Add To Palette`. The genuinely destructive one is silent.)*

### 2 · **Aurora has all three of our `[protection]` booleans, not one.**

`36`. `STUDY/28 §B3` said:

> *"Aurora's creature sheet has `Plot` (a single checkbox) and no other two."*

**Wrong — I had never opened the creature's `Advanced` tab.** It carries:

| Aurora | ours (`AUTHORED-CHARACTER-01 §2`) |
|---|---|
| `Plot` | `plot` — cannot be harmed at all |
| **`Immortal`** | `min_1_hp` — can be hurt, cannot be killed |
| **`No Permanent Death`** | `raiseable` — can be killed, comes back |

**This strengthens our position rather than weakening it.** We took the three
from KOTOR; **NWN has the same three**, so it is a convergent answer across both
source engines, not a KOTOR quirk.

---

# 1 · The Journal Editor — quests, which we have never built

`01`–`05`. **This is the only evidence we will get, so it is written as a
specification.**

## The model, complete

```
Category  (= a quest)                        ⚠ the API calls this a PLOT
  Name        player-facing title            localised (…)
  Tag         identity, used by scripts      ⚠ "Kill the Mistress" — WITH SPACES
  Priority    Highest|High|Medium|Low|Lowest journal sort order
  XP          500                            ⚠ awarded on COMPLETION, not per stage
  Comments    author note

  Entry  (= a stage)  ×N                     ⚠ the API calls this a STATE
    ID              10, 20, …                ⚠ NUMBERED IN TENS
    Finish Category ☐                        ⚠ this stage ends the quest
    Text            the whole player paragraph, localised (…)
```

**Seven fields for an entire quest system.** That is the whole editor.

## ⚠⚠ The four findings that matter

**⚠ Stages are numbered in TENS — `[0010]`, `[0020]`** — so `[0015]` can be
inserted later without renumbering. An old convention and a good one.

**⚠⚠ A STAGE IS NOT A DELTA. It restates the whole entry.** `02` shows stage
`[0020]` beginning with `[0010]`'s text **verbatim** and then appending more.
The author copies forward and adds.

> **Our instinct would be an append-only list of entries. That would be wrong.
> Each stage is a complete replacement of the visible journal text.**

**⚠ `Finish Category` is the only mechanic in the editor.** One checkbox says
"this stage completes the quest".

**⚠⚠ THERE IS NO CONDITION, NO TRIGGER, AND NOTHING THAT SAYS WHAT ADVANCES A
STAGE.** The Journal Editor is purely text and numbering. **Advancement lives
entirely outside it** — see §2.

**And by `PT-1376`'s own test it is a DIALOG, not an editor**: `Apply / OK /
Cancel`, no New/Open/Save/Close. **The form census predicted this exactly.**

## ⚠ Three vocabularies for one concept, in one product

| where | word for a quest | word for a stage |
|---|---|---|
| the menu | **Journal** | — |
| the editor UI | **Category** | **Entry**, with an `ID` |
| the scripting API (`20`) | **Plot** (`szPlotID`) | **State** (`nState`) |
| the export type list (`23`) | **Plot Blueprint File** | — |

**Four names, two concepts.** Do not inherit this.

---

# 2 · ⚠⚠ THE JOIN — how a conversation sets a quest

**This is the thing `PT-1516` found we cannot do, and Aurora's answer is better
than "a script".**

A conversation node's property pane has **five tabs** (`06`, and the strip
scrolls — `Current File` is hidden until you press `›`):

| tab | what it holds |
|---|---|
| `Text Appears When …` | **the gate** — a script named `int StartingConditional()` (`08`) |
| `Actions Taken` | **the effect** — an arbitrary script (`09`) |
| **`Other Actions`** | ⚠⚠ **structured pickers: Play Animation · Play Sound · JOURNAL** (`10`) |
| `Comments` | author note |
| `Current File` | ⚠ conversation-scoped, not node-scoped — see below |

## The Journal control, exactly

`10`, `11`, `12`. **Two dropdowns and an `Edit` button.**

- **Dropdown 1** lists the module's quest Categories — `Kill the Mistress`,
  `Rescue the Heir`, plus a blank meaning *no journal action*.
- **Dropdown 2** fills with **that quest's stage IDs** — `10`, `20`.
- **`Edit`** jumps straight into the Journal Editor.

> **⚠⚠ You cannot type an arbitrary quest name. The vocabulary is closed by
> construction — it is whatever the Journal Editor contains.**

**That is our principle, applied by Aurora, in 2002** — and it is the shape
`DIALOGUE-FORMAT-01 §5`'s effect payload needs:

```toml
effect = [ { kind = "quest.flag-set", flag = "spire.codes-surrendered" } ]
```

**`PT-1516` found a flag cannot be set by anyone because Loom cannot write the
payload. Aurora's answer is that the payload is a PICKER whose contents come
from the quest definition.** Not a text box. Not a script.

## ⚠⚠ And the same node is inconsistent in the way that proves our rule

On one property pane:

- the **journal action** is a closed picker — **safe, checkable, un-typoable**
- the **gate** is `int StartingConditional()` — **arbitrary compiled code**

**Same dialog, two philosophies.** `DIALOGUE-FORMAT-01 §4` refuses the second
and builds a closed vocabulary instead. **Aurora itself demonstrates that the
closed one is the better half of its own design.**

## What else the conversation editor has

- **`Script Preview`** (`08`) — the condition's source shown **inline**, so the
  author reads it without opening the script editor. ⚠ **The transferable germ
  even though the mechanism is refused**: whatever a gate *is*, show what it says
  where it is used.
- **A `Name`/`Value` parameter table** beside each script — so a script call is
  parameterised, not just named. *(Empty on every node I opened.)*
- **`Current File` → `Normal` and `Aborted` end-scripts** (`13`). ⚠ **We have no
  concept of an ABORTED conversation** — `DIALOGUE-FORMAT-01` ends on an absent
  `then` and does not distinguish *ended* from *abandoned*.
- **`Module Word Count : 4458`** in the status bar (`06`) — a **writer's** tool,
  for localisation and VO budgeting. We have nothing like it.
- **`Scrap` tab** — a scratch area to park nodes.
- `Data | Bookmarks | Search` beneath the text box.
- **`[OWNER]`** as a speaker placeholder and **`<master/mistress>`** as runtime
  gender substitution inside a line (`07`). Our `by` covers the first; **we have
  no token substitution.**

**⚠ And it is TAB-PER-OPEN-THING** (`Scrap | untitled000 | berdel`) — exactly
what `PT-1375` rejected, and exactly the thin spot `PT-1376` recorded.

---

# 3 · The Faction Editor — the standing track we declined

`14`, `15`, `16`. **`FACTIONS-01 §4b` gives one handle and explicitly not a
standing track. This is what declining costs.**

**Nine factions** in this module: `PC`, `Hostile`, `Commoner`, `Merchant`,
`Defender` (stock) plus `Rangers`, `Drow`, `Animals`, `Uninvolved`
(module-added). **`Add Faction` / `Remove Faction`** — a module defines its own,
and **`Remove Faction` is greyed for the stock five.**

## What an author actually sets

**⚠⚠ A pairwise reputation matrix, 0–100** (`16`), colour-coded by band —
**red at 0, grey at 50, blue at 100**. Read directly off the grid:

| | PC | Hostile | Commoner | Merchant | Defender |
|---|---|---|---|---|---|
| **Hostile** | **0** | 100 | **0** | **0** | **0** |
| **Commoner** | 50 | **0** | 100 | 50 | 50 |
| **Merchant** | 50 | **0** | 50 | 100 | 100 |
| **Defender** | 50 | **0** | 100 | 100 | 100 |

**Three structural details worth copying:**

1. **The matrix shows only the factions ticked in the list** — four of nine
   here. **That is how an N×N grid stays readable.**
2. ⚠ **There is a PC column but no PC row.** Others have an attitude toward the
   player; **the player has none toward them.** Asymmetric on purpose.
3. `15` — the `Basic` tab draws the **0–100 scale with its bands** as a picture,
   so you can see where Friendly and Hostile begin without reading a number.

## ⚠ Where ours stands

`FACTIONS-01 §4b` gives a creature **one handle** and no number, and `PT-1526`
found **`character.faction-changed` folded and written by nothing.**

> **So we have the event and not the model.** Aurora has the model and no event —
> its reputation is mutable current state, not history.

**This does not automatically transfer.** A 0–100 track per faction pair is
`O(n²)` for the author to maintain, and `§4b` declined it deliberately. **But
the decision should now be made against this evidence rather than in the
abstract**, and if we ever want *"the Sith remember what you did"*, this is the
shape that supports it.

**⚠ AND FACTIONS DO NOT EXPORT** — see §5. A creature can travel between
modules; **its faction cannot.**

---

# 4 · The Script Editor — does `PT-1341` survive?

`17`–`20`. Measured **752×506** client area; `PT-1341` read **760×540** from the
binary. **The binary reading is confirmed.**

## ⚠ But the characterisation was incomplete

`PT-1341` called it *"not an IDE, it is a text area over a compile-output pane.
It fits in a tab."* **It is three panes, not two:**

1. **code** — line numbers, syntax highlighting, prefilled `void main() { }`
2. ⚠ **an API reference browser docked right** — a **`Filter` box** over
   `Functions | Variables | Constants | Templates`
3. **output** — `Compiler | Help | Bookmarks | Search Results`

## ⚠⚠ The ruling survives, and this is *why* it survives

**Everything the right-hand pane does is LSP functionality.** Filter for
`Journal` and you get the three-function quest API (`19`); select one and the
bottom pane shows **the source's own doc comment** (`20`):

```
// Add a journal quest entry to oCreature.
// - szPlotID: the plot identifier used in the toolset's Journal Editor
// - nState: the state of the plot as seen in the toolset's Journal Editor
```

**Symbol list, filter, signature-and-doc on selection — that is hover and
completion.** Aurora built it *in-window* because 2002 had no language server.
**Putting LSP outside gets the same capability and gives the pane's real estate
back to the code**, which at 752×506 is only ~500×360.

**⚠ The two things LSP does NOT give:** **`Templates`** (snippets — `18`, and
**empty with no message**, another silent empty state) and **`Bookmarks`**. Both
are per-author conveniences; neither is load-bearing.

**⚠ Not tested: compiling.** The `Compiler` tab was never exercised because
compiling writes. **So whether the compile-error surface is usable is unknown.**

---

# 5 · Import / Export — what travels, and what does not

`21`–`23`. **Directly relevant to building our system from the game files.**

**⚠ Export is a BASKET, not a per-object action** (`21`): *"Click the 'Add
Resources…' button to select the resources that you wish to export."* You
assemble a bundle and export it together. *(And note that empty state **has an
instruction sentence** — where `Templates` was blank and the resource picker's
was a bare `0`. **Three qualities of empty state in one program.**)*

**⚠ The picker is locked to your own content** (`22`): `Resources to Show` has
all three radios **greyed** with `Module Resources Only` selected. **You cannot
re-export base-game or hak resources.** The same `Select Resource` dialog as
everywhere else, with the button relabelled `Export`.

## ⚠⚠ The thirteen exportable types

Enumerated one at a time by keyboard, because the dropdown would not paint under
Wine (`23`):

    Conversation File
    NWScript Source              ⚠ SOURCE, not compiled .ncs
    Blueprint for Creatures
    Blueprint for Doors
    Blueprint for Encounters
    Blueprint for Items
    Blueprint for Placeables
    Blueprint for Sounds
    Blueprint for Market/Merchants (Stores)
    Blueprint for Triggers
    Blueprint for Waypoints
    Plot Blueprint File          ⚠ A QUEST CAN TRAVEL
    Area File                    ⚠ A WHOLE AREA CAN TRAVEL

**⚠ The exchange unit is SOURCE you can read.** `NWScript Source`, not the
compiled binary. **`PACKAGE-FORMAT-01 §2`'s *"git diff works. A modder can
look"* is a rule Aurora already agreed with.**

## ⚠⚠ What does NOT travel

- **FACTIONS.** There is no faction type in the list. Export a creature that
  belongs to `Drow` and **the faction does not go with it** — the faction table
  is module-global. **A creature arrives in a new module pointing at a faction
  that may not exist.**
- **The module's own properties** — start area, time, XP scale, hak list.
- **The 2DA rules tables** (they are hak content, not module content).

> **For `PT-1334`'s exchange this is the lesson: the unit of travel is a
> BLUEPRINT, and anything module-global that a blueprint REFERS TO is left
> behind.** Our `faction` field on `AUTHORED-CHARACTER-01` has exactly this
> shape, and exactly this hazard.

---

# 6 · ⚠⚠ Can a module restrict character generation? **NO.**

**The owner's new question, and the answer is a clean negative that goes
straight into column three.**

I checked **every** Module Properties tab (`26`, `27`, `28`):

| tab | contents | any chargen restriction? |
|---|---|---|
| **Basic** | Name, Tag `MODULE`, Start Area, **Starting X/Y/Z** | no |
| **Events** | 21 module hooks | no — but see below |
| **Advanced** | Minutes/Hour, Dawn/Dusk, calendar, **XP Scale**, Starting Movie, Variables | no |
| **Description** | one free-text blob | no |
| **Custom Content** | the hak-pak list | no |

**⚠ There is no module property that limits what a player may be.** Not races,
not classes, not alignments, not level.

**The two workarounds Aurora leaves you, both of which are not properties:**

1. **`OnPlayerLevelUp` / `OnClientEnter` scripts** (`27`, right). You can
   **detect an illegal character after it already exists** and kick or rewrite
   it. Reactive, not preventive.
2. **A hak pak overriding `classes.2da` / `racialtypes.2da`** — you replace the
   **rules tables wholesale** so the class does not exist at all. All-or-nothing,
   affects every module using that hak.

> **⚠⚠ So `PT-1412`'s `[creation] species_closed / classes_closed` has NO Aurora
> equivalent, and that is the answer.** Ours is a **declarative subtractive list
> against a shared table** — neither a reactive script nor a wholesale
> replacement. **Column three, with evidence.**

**⚠ And the shape it wants is now clear from what Aurora got wrong:** the
restriction must be **visible to the player at the point of choice** (a greyed
row in the picker that says *why*), not discovered after they have built a
character. `base-rules`' hub already does this for us; **the chargen picker must
do the same.**

## Two other findings from Module Properties

**⚠ `[entry]` — Aurora's is richer than ours.** Basic names a **Start Area AND
an exact Starting X/Y/Z**. Our `[entry] area = "…"` names only the area. *(And
note the inconsistency in theirs: cross-area connections land on named
waypoints, but the module's own start uses bare coordinates.)*

**⚠⚠ `Custom Content` is our `[requires]`, and we independently got it right.**
*"a list of Hak Paks used by this module, sorted in order of highest to lowest
priority. Resources in the top Hak Paks override resources in the lower ones."*
— **ordered, and the order IS the precedence**, exactly `PACKAGE-FORMAT-01
§4·1`.

- ⚠ **`Check for Conflicts…`** — a button that reports when two dependencies
  provide the same resource. **We have nothing like it and a package system with
  overriding dependencies needs it.**
- ⚠ **No version constraint and no digest.** A hak is named, not versioned.
  **Our `version = ">=2.0"` and `digest` have no counterpart.** Aurora's
  ordering is right and its identity is weak.

**⚠ And `Description` shows what happens without structured fields** (`28`):

```
Recommended Levels: 5 - 15
Number of Players: 1 - 4
```

**Typed into prose, by convention, because there is no field for either.** We
structured `summary`/`authors`/`cover` in `§4·1`'s library tile — **but we have
no level-range or party-size field either. Aurora's evidence is that authors
will type it into the description if you do not give them one.**

---

# 7 · The small ones

## ⚠⚠ The red overlay lines — ANSWERED, by experiment

`32`, `33`, `34`. Two steps, both decisive:

1. **`View > Object Filters > Show None`** removed the purple trigger polygon,
   the yellow waypoint arrows and the placeables — **and the red and green lines
   survived.** So they are **not object markers.**
2. **`Environment > Display Grid`** (checked by default) — unticking it
   **removed the red lines**, and the green rectangle remained.

> **RED = the tile grid overlay. GREEN = the current tile selection / brush
> footprint.** The apparent irregularity is a rendering matter I did not chase.

## ⚠ `View > Object Filters` — per-kind visibility

`30`. `Show All` · `Show None` · then one toggle per kind — Creatures, Doors,
Encounters, Items, Merchants, Placeables, Sounds, Triggers, (Waypoints).

**Hide everything but creatures while you place creatures.** ⚠ **We have nothing
like it, and `Lens` draws `area.contents` wholesale** — the same code where a
marker outlives the creature.

## `Environment` menu

`31`. Refresh (F5), **Display Grid**, Display Shadows, Fog, Use Area Lighting,
Fade Geometry ▸, Render AABB Nodes, and **Play Ambient Sound / Music / Placed
Sounds** — the area's audio auditioned in the editor, consistent with the
audition-everywhere pattern from `STUDY/27`.

## `Edit` menu

`24`. Undo (Ctrl+Z), Redo, Copy/Cut/Paste, **Resize Area**, **Rotate Area**,
**Find Instance**, **Module Properties**, Area Properties.

⚠ **`Find Instance`** — locate a placed instance across the module. Enabled with
no area open, so it is module-scoped.

## `Tools` menu

All four "editors" live here, not under File: Conversation (Ctrl+Alt+V), Faction
(Ctrl+Alt+F), Script (Ctrl+Alt+S), Journal (Ctrl+Alt+J), plus `Options`.
**⚠ Four things named "Editor"; by `PT-1376`'s test only two own a lifecycle.**

## ⚠ `Update Instances` — the labels differ by kind, behaviour still untested

| kind | label |
|---|---|
| Encounter, Merchant | `Update Instances` |
| **Placeable** | **`Update instances in current area`** |
| Creature | **neither — it is only in the palette context menu** |

**Placeable is the odd one out.** ⚠ **I still did not test whether the behaviour
differs** — that needs one blueprint placed in two areas and a change propagated,
and I judged it not worth the writes. **The labels promise different scopes and
only one states its scope.**

## ⚠ The blue-vs-olive list colour — hypothesis EXCLUDED, still unexplained

`STUDY/27` saw the Store wizard's list colour-coded blue vs olive with no legend.
**Tested: the module's `Custom > Merchants` category is EMPTY** (no expander), so
the module has **zero custom merchants**.

> **Therefore the split is NOT module-local vs stock.** That hypothesis is dead.
> **I did not establish what the colours mean.** The same list renders uniform
> black in the main palette, so the colouring is specific to that picker.

## ⚠ Four save/discard prompts, four phrasings, and one inverted

`37`, `38`, `39`, and the module guard from `STUDY/28`:

| where | text | icon | `Yes` means |
|---|---|---|---|
| Module | *"Would you like to save your changes to the module?"* | ⚠ warning | **save** |
| Conversation | *"Save conversation file berdel?"* | ? | **save** |
| Script | *"Save changes to untitled000?"* | ⚠ warning | **save** |
| **Journal** | **"Discard changes"** | ? | **⚠ DISCARD** |

**Two of four name the object. Two of four use the right icon. And the one that
inverts the button meaning is the destructive one.** A user who learns *"Yes
keeps my work"* loses it in the Journal Editor.

---

# 8 · Creature Properties — the biggest editor, and a gift

`35`, `36`. Opened incidentally while chasing `Update Instances`; too useful to
leave out.

**⚠ Eleven tabs on TWO ROWS**: `Advanced | Feats | Spells | Special Abilities |
Comments` over `Basic | Statistics | Appearance | Classes | Skills | Scripts`.

> **⚠⚠ AND CLICKING A BACK-ROW TAB SWAPS THE ROWS.** I aimed at `Statistics` and
> landed on `Feats`, because clicking `Advanced` moved every other tab. **That is
> `PT-1439`'s hazard, live, in the most-used editor in the toolset.** A two-row
> tab bar is a moving target. **Do not build one.**

## What maps to `AUTHORED-CHARACTER-01`

**⚠ `Race` and `Appearance` are separate fields** — `Animal` vs `Bear, Black`.
**That is our `character.species-set` / `character.model-set` split**, already in
`EVENT-KINDS-01`. And **`Phenotype`** is a *third* axis (body build) where we
have two.

**⚠ `Subrace` is a FREE TEXT FIELD** on Advanced, with `Deity` beside it. **No
records, no mechanical effect — a label.** Our subraces are **records the picker
filters, carrying mechanical values** (`PT-1391`). **We are strictly richer and
should not read Aurora's field as precedent.**

**⚠⚠ `Challenge Rating: Calculated 2.19 · Adjustment 0 · Challenge Rating 2`.**

> **This is the derive-and-override pattern with all three numbers on screen at
> once — and it is BETTER than ours.**

`AUTHORED-CHARACTER-01 §3`'s HP escape hatch is `override = 0` meaning *derive
normally*. **You cannot see what the derived value would have been.** Aurora
shows **derived**, **adjustment**, and **result** side by side. **Copy this
shape for `override`, and for every other derived-with-escape-hatch field.**

**Also present:** `Faction` + an **`Edit Factions`** button that jumps to the
Faction Editor; **`Apply Template`**; `Sound Set`; `Perception Range`;
`Treasure Model`; `Corpse Decay Time (s)`; `Leaves Lootable Corpse`;
`Disarmable`; a live 3D preview; a real portrait (`po_bearblck_` — a **stem**,
as `STUDY/27` found for placeables); an `Inventory …` button; and a
`Conversation` slot with `Edit`.

**The `Feats` tab** pairs a filterable master list (`Filter: All Feats`, plus a
`?` help button) with a **`Feats Selection Summary`** tree grouping what is
actually assigned. ⚠ **A master list plus a grouped summary of the chosen
subset** is the right shape for any long pick-many list, and our feats surface
does not exist yet.

---

# 9 · Updated column three — what this study adds

**New entries for `STUDY/28 §B`:**

| our thing | Aurora answer | shape it wants |
|---|---|---|
| `QUEST-MODEL-01` | ⚠ **exists** — Category/Entry, 7 fields, §1 | copy the model; **fix the vocabulary** |
| `quest.flag-set` payload (`PT-1516`) | ⚠ **exists** — two closed pickers, §2 | **a picker, never a text box** |
| an ABORTED conversation | `Current File > Aborted` | we have no concept — decide |
| `[creation]` (`PT-1412`) | ⚠⚠ **NONE**, §6 | declarative subtractive list; **greyed rows that say why** |
| `[requires]` version + digest | ⚠ **NONE** — haks are named, not versioned | keep ours; **add `Check for Conflicts`** |
| level range / party size | ⚠ **NONE** — typed into prose | give it a field |
| faction standing track | ⚠ **exists** — N×N 0–100 matrix, §3 | decide against evidence, not in the abstract |
| per-kind viewer visibility | `View > Object Filters` | **take it** |
| `override` visibility | ⚠ **better than ours** — derived/adjustment/result | **take it** |
| word count / VO budget | status bar | consider |

**And two things `STUDY/28` recorded that must be edited:**

- *"Aurora cannot resize an area either"* → **false, see Corrections §1**
- *"Aurora has `Plot` and no other two"* → **false, see Corrections §2**

---

## Appendix · What is STILL not looked at

- **Compiling a script.** The `Compiler` output tab is unexercised — it writes.
- **`Build Module` and `Test Module`.** Still deliberately un-run.
- **`Tools > Options`.** Never opened.
- **Creature tabs `Statistics`, `Appearance`, `Classes`, `Skills`, `Scripts`,
  `Spells`, `Special Abilities`.** Only `Basic`, `Advanced` and `Feats` seen.
- **`Import…`.** Only `Export…` was opened; the import side is unknown, including
  what happens when an imported blueprint names a faction that does not exist.
- **`Edit > Find Instance`** and **`Edit > Rotate Area`** — seen in the menu,
  never opened.
- **Whether `Update Instances` and `Update instances in current area` differ in
  BEHAVIOUR.** Labels compared; behaviour untested.
- **What the blue/olive list colouring means.** One hypothesis excluded.
- **The `Name`/`Value` script-parameter table.** Empty on every node I opened, so
  I never saw a parameter passed.
