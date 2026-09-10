# 27 · Aurora pressed — the Builder rebuild foundation

**From `Tester`.** Successor to `STUDY/26-aurora-observed`, which looked at the
toolset. This one **uses** it: every wizard run to its last step, all five
editors I had not opened, every instance verb, and a 1280×720 pass.

**The bar for this document is "could somebody rebuild this from these notes?"**
so it is written as findings with the screen that proves each one, not as a tour.

---

## How it was run, and what that limits

Aurora Toolset **v89.8193.37-17** under plain Wine, throwaway `WINEPREFIX`,
module **`To Heir is Human.mod`** (stock). Main window 1500×1008 for most of the
pass, then 1280×720 for §9.

**⚠ NOTHING WAS SAVED.** The module title carried `*` for the whole session and
the process was killed rather than closed. The NWN install was read, never
written. Blueprints I created live only in the dead process's memory.

**⚠ What I did NOT look at, so the next person knows where to go:**

- **File > New Module / the Module Wizard.** Not run. Everything here is inside
  an existing module. Making a package from nothing is still unmapped.
- **The Creature, Item, Door and Conversation editors.** Covered in `STUDY/26`;
  not re-opened here.
- **The `Inventory`, `Conversation` and `Properties` instance verbs.** Named in
  §8 because the menu shows them; not exercised.
- **`Build`, `Tools`, `Environment`, `View`, `Edit` menus.** Only `Wizards` was
  opened.
- **Tile painting itself.** I created an area through the Area Wizard and read
  its properties; I never painted a tile.
- **What the blue-vs-olive colour code in §7 means.** Observed, not explained.
- **Whether `Update Instances` and `Update instances in current area` differ in
  behaviour.** Only the labels differ; I did not test either.

---

## 1 · The seven rules worth stealing

These are the transferable answers, stated as rules. Everything below is
evidence for one of them.

1. **A wizard is the editor's own tabs put in order — not a second code path.**
   The Encounter wizard's "Creature List" step and the Encounter editor's
   "Creature List" tab are the same control.
   → `15`, `20`
2. **Gate the step whose emptiness makes the object meaningless; let the
   cosmetic step pass.** `Next` is greyed on "pick a creature to spawn" and on
   "pick a wave file"; it is *not* greyed on "choose a palette category".
   → `15`, `29`, `14`
3. **A required either/or is a radio group with a sentence under each option,
   not a dropdown.** Aurora proves this against itself: the Sound wizard
   explains looping vs single-shot in two sentences; the Encounter editor
   expresses the same concept as a bare `Spawn Option` dropdown.
   → `27`, `28` vs `19`
4. **Explain the consequence, not the field.** The Levelup Wizard spends three
   paragraphs on what a class *does to the creature*, not on what to type.
   → `47`
5. **Ask in the domain's language and prefill with working content.** The Store
   wizard asks *"What does the shopkeeper say when the conversation begins?"*
   and has already filled in *"Welcome to my shop…"*. Press Finish and you have
   a working store.
   → `48`
6. **Say the count, the consequence, and whether it can be undone — before it
   starts.** *"This object contains 3 modified inventory items… There is no way
   to cancel this operation if you start."*
   → `51`
7. **Show the thing, and say where the cursor is.** Every placeable editor has a
   live 3D preview; the status bar continuously names the grid row/column and
   the tile resref under the pointer.
   → `36`, `44`

---

## 2 · The shell

`01`, `02`

Three tree roots — **Areas**, **Conversations**, **Scripts**. An area expands
into **nine content kinds**: Creatures, Doors, Encounters, Items, Merchants,
Placeables, Sounds, Triggers, Waypoints. Those are the same nine the palette
offers, so the tree and the palette agree on the vocabulary.

**⚠ The palette does not exist until an area viewer is open.** With no area
open, the right-hand third of the window is empty grey. The palette is a
property of the open area, not of the module.

**⚠ Expanding `Scripts` scrolled `Areas` and `Conversations` off the top.** The
tree is one flat scroll region; opening a large root evicts the others from
view. `03` shows the result: ~50 scripts, **flat, alphabetical, no folders and
no visible search box**.

> **Correction I had to make mid-run.** I first recorded "no search". There
> **is** a search — `Find Text` / `Ctrl+F` and `Find Next` / `F3`, hidden in the
> right-click context menu (`10`). It is undiscoverable, not absent. **We do
> better by showing the box.**

---

## 3 · The palette is a nine-way mode selector, and that holds for all nine

`04`, `05`, `06` — every mode, with its tooltip and its root categories.

| mode | root categories |
|---|---|
| Paint Creatures | Monsters · NPCs · Tutorial |
| Paint Doors | Tileset Specific · Universal |
| **Paint Encounters** | **Hard · Impossible · Moderate · Normal · Very Easy** |
| Paint Items | Armor · Creature Items · Miscellaneous · Plot Item · Tutorial · Weapons |
| Paint Merchants | Merchants |
| Paint Placeable Objects | 12 categories, Battlefield → Visual Effects |
| Paint Sounds | Animals · Civilization · Magical · Nature · People · Weather |
| Paint Triggers | Area Transition · Generic Trigger · Secret Object Trigger · Traps |
| Paint Waypoints | Waypoints |

**Every mode has `Standard` and `Custom` tabs.** The shape is identical across
all nine — mode selector → Standard/Custom → category tree → blueprints — while
the depth varies from one root (Merchants, Waypoints) to twelve (Placeables).

**⚠ Encounters are filed by difficulty, not by content.** That is a filing
decision with a consequence; see §5.

---

## 4 · The Custom tab, and how a thing gets into it

`07`, `08`, `09`

**The Custom tab is not empty.** It ships the *same category skeleton as
Standard, plus a `Special` category Standard does not have* — and in this module
every one of those categories is empty. `Monsters` → `Animals` → `Bear` is five
levels deep and holds nothing.

**⚠ The only signal that a category is empty is the absence of a `+` expander.
There is no sentence anywhere.** You can drill five levels and find nothing,
with the UI never saying so. **Do not copy this.** The *answer* — give authors a
taxonomy to file into — transfers; the *presentation* is a silent empty state of
exactly the kind this project has ruled against.

**Two ways a blueprint gets there:**

- **Right-click a category → `New`** (`10`). The category menu is `New` ·
  `Find Text` · `Find Next` · `Refresh Palette`. A blueprint's own menu is
  richer: `Edit` · **`Edit Copy`** · `New` · `Delete` · `Update Instances` ·
  `Export` · the three above. `Edit Copy` — *open this, but don't touch the
  original* — is a verb we do not have.
- **⚠ Place an instance, tune it, then right-click it → `Add To Palette`**
  (`45`, `51`). **Instance → blueprint**, not only blueprint → instance. This is
  the more interesting direction and we have no equivalent.

---

## 5 · The wizards

**Every kind's wizard opens with the same step: "Assign Palette Category".**
`14`, `23`, `26`, `35`, `39`.

**⚠ The wizard already knows the answer and shows no sign of knowing it.** I
right-clicked `Hard` and the category list came up with **nothing highlighted**,
and `Next >` enabled anyway — no refusal for an unselected required field. Two
steps later the Name field is prefilled **`Hard 001`**, which proves the
selection was carried the whole time. It was never displayed. Same for
`Area Transition 001`, `Animals 001`, `Battlefield 001`, `Merchants 001`.

**A wizard has exactly as many steps as the kind has required fields:**

| kind | steps |
|---|---|
| Trigger | Category → Name |
| Placeable | Category → Name |
| Merchant | Category → Name |
| Encounter | Category → **Creature List** → Name |
| Sound | Category → **Timing** → **Positioning** → **Wave List** → Name |

**Every wizard ends by asking where you want to be**: ☐ `Launch Properties
Dialog`. The Area Wizard's last step is the same idea (☐ Launch Area Properties,
☑ Open in Area Viewer). *A wizard that ends by asking where you want to be* is a
convention worth taking.

> **⚠ Recorded as observed, not as a rule.** That checkbox appeared unticked,
> then ticked without my ticking it, then unticked again across four wizards. I
> could not derive the rule and am not claiming one.

**⚠ The wizards are not one shared shell.** They are 326–605px wide, and the
Placeable one is narrow enough that the identical header sentence **wraps to two
lines** (`35`). In that same dialog the category list's height is not a multiple
of its row height, so **`Trades & Academic & Farm` is sliced in half** by the
list's bottom edge — a PT-1439-family defect, in the shipped product.

**⚠ Cancel in the editor does not undo the wizard's creation.** I cancelled out
of `Battlefield 001`'s property dialog; the blueprint was still in the palette.
Cancel discarded my *field edits* only. A builder who backs out still has an
object.

---

## 6 · The five editors

### Encounters — `19`, `20`, `21`, `22`

Tabs: Basic | Creature List | Scripts | Advanced | Comments.

**⚠ The sharpest contradiction in the program.** I filed the blueprint under
palette category **Hard**; it is named **Hard 001**; its `Category` field reads
**Hard**; and its **`Difficulty` field reads `Easy`**. Three things on one
screen say Hard and the mechanical field says Easy. **The palette category is a
filing label with no connection to the difficulty.** A builder who files under
"Hard" gets an Easy encounter and nothing warns them.

`Tag` is silently derived from `Name` by stripping spaces (`Hard 001` →
`Hard001`).

**What an encounter asks that painting cannot supply:** a spawn *table*
(`CR | Creature | Tag | Blueprint ResRef | Unique`), a difficulty, min/max
creature counts, and a spawn option. No amount of placing creatures on squares
expresses "pick from this list, respawning, on a 60-second timer".

**⚠ A two-level dependency cascade, one level of it across a tab boundary.**
Proved, not guessed:

1. `Spawn Option = Single Shot` on **Basic** greys `Encounter Respawns` on
   **Advanced**. Nothing on either tab says so.
2. Setting it to `Continuous` enables the checkbox but its three sub-fields stay
   greyed until the checkbox itself is ticked (`21` → `22`).

**⚠ And the default after enabling is self-cancelling:** `Number of Times To
Respawn = 0` with `Infinite Respawn` unticked. Respawns on, set to never
respawn.

`Update Instances` on Advanced answers a question our system has: **changing a
blueprint propagates to already-placed instances only when you press the
button.** Explicit, not automatic. Good answer.

### Triggers — `24`, `25`

Tabs: Basic | Scripts | Advanced | Comments.

**⚠ `Trigger Type` reads `Area Transition` and is greyed — immutable, set by the
palette category I right-clicked.**

**⚠ So the same "palette category" concept means two opposite things for two
kinds — mechanically binding for Triggers, purely decorative for Encounters —
and nothing in the UI distinguishes them.** This is the single most important
"do not inherit" finding in the document. If our Builder has a filing category,
it must be *consistently* one or the other, and it must say which.

**⚠ ResRefs are silently truncated to 16 characters.** `Area Transition 001` →
`areatransition001` (17) → **`areatransitio001`**. It dropped a letter from the
*stem* and preserved the numeric suffix. A hard format limit, applied
invisibly.

Advanced carries a **Portrait and a Cursor on a trigger**, and a greyed
`Faction` with no reason given.

### Sounds — `27`, `28`, `29`, `33`, `34`

Tabs: Basic | Positioning | Advanced. **No `Scripts` tab** — a sound has no
event hooks.

**The wizard is the best-explained UI in the program.** `Timing` and
`Positioning` are radio groups where **every option carries a full sentence**,
nothing is preselected, and `Next` is greyed until you choose:

> ○ **Seamlessly looping** — One wave that seamlessly repeats over and over
> again with no breaks
> ○ **Single-shot(s)** — One or more waves that are played separately with a
> random delay between each

**⚠ Those sentences exist only in the wizard.** The `Positioning` tab shows the
same three options as bare one-liners (`34`). Create via wizard and you are
taught; edit later and you are not.

**⚠ The wizard cannot reach every valid state.** I chose **Single-shot(s)**; the
editor's `Play Style` reads **Repeating**, and **`Once` is reachable only from
the editor**. The wizard's two options map onto three.

**Diagrams that explain numbers by drawing them** (`34`) — `Volume Distances`
draws Cutoff 10.0m and Max Volume 1.0m as two concentric circles; `Height` draws
a ground plane and a vertical. Directly transferable.

Advanced holds a **24-checkbox AM/PM schedule grid** for `Specific Hours`, and
`Play Order: Random` greyed **because the list holds one sound** — a correct and
thoughtful disable, still with no reason stated.

**⚠ `Area-wide` positioning means a thing you place on a square whose square
then does not matter.** Worth deciding deliberately for our format.

### Placeables — `36`, `37`, `38`

**⚠ A live 3D preview pane, full height of the dialog, showing the actual
model** (`36`). The editor shows you the thing. **This is where we most clearly
do not do better** — Loom shows a name in a tree.

A placeable carries **Hardness, Hit Points and three saving throws**: furniture
is a combatant-shaped object. Plus a Conversation, faction, portrait
(`po_plc_a01_` — a *stem*, with the size suffix appended at runtime), initial
state, treasure model, and variables.

**⚠⚠ A checkbox on one tab grows the tab bar.** Ticking `Useable` on **Basic**:

- enables `Has Inventory`,
- **greys `Static`** — mutual exclusion enforced by disabling, not by an error,
- and **inserts two new tabs, `Lock` and `Trap`, between `Basic` and `Scripts`**
  (`37`). Five tabs became seven and **every tab to the right shifted**.

A click aimed at `Scripts` a moment earlier now lands on `Trap`. The *idea* —
don't show a Lock tab on something that cannot be locked — is right and worth
taking. **The execution is a live PT-1439 hazard.** If we do this, new sections
append at the end or the bar reserves its positions.

> I tested this properly rather than asserting it: my first hypothesis was that
> `Static` gated `Has Inventory`. I unticked `Static`, `Has Inventory` stayed
> greyed, and only then did I try `Useable`.

**The `Trap` tab is the good version of the same idiom** (`38`): `Is Trapped ☐`
sits **directly above** a titled `Trap Settings` group box that greys as one
unit. Same program, same pattern as the Encounter's respawn group — one done
right, one done across a tab boundary. Note also that disabled checkboxes render
**greyed-but-ticked**: disabled ≠ hidden.

### Merchants — `41`, `42`

Tabs: Basic | Advanced | Restrictions | Comments.

**⚠ `Scripts` is a *group box* on Advanced here, a *whole tab* on Encounters and
Triggers, and *absent* on Sounds.** The placement scales with the number of
hooks (2 / 5 / 0), which is sensible — but it means **a builder cannot learn
"scripts are on the Scripts tab."**

**⚠ `Sell Mark Up 100` / `Buy Mark Down 65` are percentages with no unit shown.**

**⚠ The disabled fields hold `-1` sentinels.** Tick `Has Maximum Buy Price` and
your starting max buy price is −1. Same class of problem as the encounter's
"respawn 0 times".

**⚠ There is a `Restrictions` tab and a `Restrictions` group box on the Basic
tab.** Same name, two different things, one dialog.

**The `Restrictions` tab is the most elegant control on the tour** (`42`): two
radios — *"Store will **NOT** buy the following items"* / *"Store will **ONLY**
buy the following items"* — over **one** shuttle list. One list, blacklist or
whitelist, chosen explicitly. **That is the same shape as our doctrine
exclusions/preferences** and it is a better presentation of it.

---

## 7 · Lists, pickers and empty states

**The `Select Resource` picker (`30`) is the single most transferable screen in
this document.** It carries, all at once:

- a **live count** — `185 resource(s)`, updating with the filters;
- a **provenance filter** — All Resources / **Module Resources Only** / **Hak
  Pak Resources Only**. This is exactly what a package that `requires` another
  needs: *show me only what I authored*;
- a **name search**;
- **`Resources of Type: Wave sounds` greyed** — correctly disabled, because the
  caller fixed it;
- **`Name Filter: as_Animals` prefilled from the palette category I chose**, so
  the category does real work here;
- and **`Play` / `Stop`** — **you can audition the resource inside the picker.**
  The right answer for any media picker, and the buttons appear again in the
  editor (`33`).

**Layout:** hundreds of entries in **newspaper columns that scroll
horizontally**, ~4 × 29 visible. Unusual; dense; worth considering.

> **Correction.** I first wrote that this dialog had no search or filter. I had
> cropped above the filter panel. It has three filters and a count. Recorded
> because the mistake is instructive: **a scoped negative taken from a partial
> view is worth nothing.**

**⚠ Where we already do better.** Switching to `Module Resources Only` gives
`0 resource(s)` and a **blank white rectangle** (`31`). The numeral in the
corner is the *entire* empty state — nothing distinguishes "your filter matched
nothing" from "the dialog broke". Our `folderFor` ruling produced an honest
*sentence*. Keep the live count; keep the sentence too.

**⚠ Two list defects that recur:** entries clipped by a too-narrow pane with a
**horizontal scrollbar** as the answer (`16`, `42` — "Ancient Dire Bea…",
"Basic Crafting Compon…"), and **rows sliced in half** by list heights that are
not multiples of the row height (`35`, `43`).

**⚠ Six rows all labelled `Blackmarket Store`** with nothing to tell them apart
(`40`). In the Store wizard's embedded copy of the same list (`49`) they are
**colour-coded blue vs olive** — **a colour code with no legend anywhere**, and
the main palette renders the same list uniform black.

**Good empty states, for contrast:** the `Variables` editor (`12`) shows its
`Name | Type | Value` columns with zero rows, so you can see the shape of the
thing before you have one, and `Replace`/`Add`/`Delete` are greyed with the
reason visible beside them (the Name box is empty). Variables come in exactly
three types — **`int`, `float`, `string`** (`13`). No boolean, no object
reference.

---

## 8 · The instance verbs

`45` — right-clicking a placed creature gives **ten** verbs:

`Add To Palette` · `Adjust Location` · `Create Waypoint` · `Conversation` ·
`Inventory` · `Levelup Wizard` · `Setup Store` · `Delete` · `Variables` ·
`Properties`

**⚠ `Adjust Location` (`46`) shows the creature at X 38.31, Y 43.58, Z 0.00 —
fractional.** The creature is **not on a grid square**. Aurora's grid is for
*tiles only*; creatures, placeables and waypoints live in continuous metres on
top of it. **This is a fundamental architectural divergence from our
square-based placements** and the most important thing in this section.

The dialog separates **Position/Bearing** (game-meaningful, with a live bearing
preview swatch) from a group literally named **Visual Transforms** (scale,
rotation, translation — cosmetic). **Naming the cosmetic transform "visual" tells
you which one the engine respects.** Buttons are `Apply` / `OK` / `Cancel` —
commit without closing; ours offer only OK/Cancel.

**`Levelup Wizard` (`47`)** carries **three paragraphs** explaining what a class
does to the creature and what raising its level changes — the most prose in any
dialog here. Its class list puts **PC classes first, then creature types** in
deliberate blocks rather than one alphabetical run, and the Class/Level table
**pre-draws all eight empty rows**, so the maximum is visible in the layout
without reading the sentence.

**`Setup Store` (`48`) is a generator, not an editor** — see rule 5. Its second
step (`49`) embeds the merchant palette **with `New` and `Edit Copy` buttons in
it**: *the picker can create what it is picking*, without leaving the wizard.

**⚠ `Create Waypoint` (`50`) opened no dialog and printed no message.** It
dropped a waypoint at the creature's exact position and bearing. A builder who
missed the small yellow arrow would not know it had worked. **Our project
refuses loudly; this succeeds silently**, and silent success is its own hazard.

**⚠ The waypoint and the creature then occupy the identical position, and
right-click resolves to the creature with no disambiguation offered.**

**`Add To Palette` (`51`)** is the warning quoted as rule 6 — count, consequence,
and *"There is no way to cancel this operation if you start"*, before it starts.
Its title says `Warning` while its icon is a `?`; small, but the two disagree.

---

## 9 · 1280×720

`43`, `44`

**The three-pane layout survives intact.** Tree left (~200px), viewer centre,
palette right (~215px). Nothing overlaps, nothing is cut off, the nine-icon mode
selector still fits, and the toolbar has room. **Aurora's chrome is not the
thing that breaks at our build size.**

**⚠ The bottom tree row is sliced in half** by the pane edge — the same
non-quantised list height as §5.

**⚠ And at 1280 I finally read the status bar, which I had not looked at at
1500:**

> `Mouse(x:17 y:53)  Grid(row:5 col:1)  Tile(tde01_a10_01)`

It is **live and per-tile**. Four samples:

| screen | readout |
|---|---|
| (500,300) | `Mouse(x:28 y:45) Grid(row:4 col:2) Tile(tde01_a10_01)` |
| (630,330) | `Mouse(x:38 y:43) Grid(row:4 col:3) Tile(tde01_a01_04)` |
| (700,400) | `Mouse(x:43 y:37) Grid(row:3 col:4) Tile(tde01_a01_02)` |
| (900,500) | `Mouse(x:58 y:30) Grid(row:3 col:5) Tile(tde01_a10_01)` |

`Mouse(x,y)` is in **area units, not screen pixels**, and **y decreases as
screen y increases** — the area's y axis points up, opposite to the screen's.

**⚠ This is the direct answer to PT-1439's family.** A persistent readout naming
the square under the cursor *and the asset in it* makes an off-by-one placement
**visible instead of silent**. Our status bar is a place we have learned to read
for refusals; Aurora uses it for continuous positional truth. **Both, ideally.**

---

## 10 · Area Properties, completing STUDY 26

`11` — the two tabs `STUDY/26` captured but never read.

**Events** has **exactly four hooks** — OnEnter, OnExit, OnHeartbeat,
OnUserDefined — each a dropdown + `...` + `Edit`, plus **`Load Script Set` /
`Save Script Set`**: a set of hooks is a reusable named thing. The same pair
appears on the Encounter and Trigger script tabs.

**Advanced** is where what does not fit lives: Check Modifier Listen/Spot,
Loading Screen, No Rest, Player vs. Player, **`ResRef` greyed (`area001`) beside
an editable `Tag` (`Area001`)** — two identities, one immutable, differing only
in case — Terrain Type as **three independent radio pairs** (Interior/Exterior,
Natural/Artificial, Underground/Above ground), and `Variables ...`.

---

## 11 · Two corrections I made during this run

Recorded because the method matters more than either finding.

**⚠ Three times the instrument was broken, not the product.**

1. The Area Properties dialog was left open **behind** the main window while
   still holding X input focus. Every click I sent to the tree was swallowed. I
   was one step from filing *"the Scripts node does not expand"*.
2. I was detecting new dialogs with `xwininfo -root -children | grep nwtoolset`,
   which **does not list newly-mapped dialogs**. On that evidence I had written
   that `Edit` opened nothing for Merchants *or* Placeables — and I knew the
   Placeable editor worked, because I had had it open ten minutes earlier. That
   contradiction is what caught it. `xdotool getactivewindow` showed the dialog
   open and focused all along. **The whole line was withdrawn.**
3. The `Select Resource` "no search or filter" reading in §7, from a crop that
   cut off the filter panel.

**Each of those is the same failure**: a clean negative from an instrument that
had stopped measuring. Before reporting a negative, prove the instrument can
still produce a positive.

---

## 12 · Summary: transfers / does not transfer / we already do better

**Transfers**

- The wizard as an ordered walk through the editor's own tabs (rule 1).
- Gating the meaningful step and not the cosmetic one (rule 2).
- Radios with a sentence per option for a required either/or (rule 3).
- Explaining the consequence rather than the field (rule 4).
- Plain-language questions with working prefilled answers; a wizard that
  *generates* rather than edits (rule 5).
- A warning that names the count, the consequence, and the irreversibility
  before starting (rule 6).
- A live 3D preview in the editor; a live grid/tile readout in the status bar
  (rule 7).
- `Update Instances` as an explicit button rather than automatic propagation.
- A picker with a live count, a provenance filter, and in-place audition —
  and one that can `New` the thing it is picking.
- One list with an explicit NOT-buy / ONLY-buy radio, rather than two lists.
- `Edit Copy` and `Add To Palette` as verbs.
- Naming the cosmetic transform "Visual" so the meaningful one is unambiguous.
- Diagrams that explain paired numbers by drawing their relationship.

**Does not transfer**

- Continuous metre positions for instances over a tile grid — that is a whole
  different area format, and ours is square-based on purpose.
- Localised-string `...` buttons on every name field.
- A filing category that is binding for one kind and decorative for another.
- Inserting tabs into the middle of a tab bar at runtime.
- A deep empty taxonomy whose only empty-signal is a missing `+`.
- Sentinel values (`-1`) sitting behind disabled checkboxes.
- Disabled controls whose enabling control is on a different tab.
- Colour-coded list rows with no legend.
- Silent ResRef truncation.
- Horizontal scrollbars as the answer to a too-narrow tree.

**Where we already do better**

- **Our refusals say why.** Aurora greys `Plot Wizard`, `Faction`,
  `Has Inventory` and `Encounter Respawns` with no reason given anywhere; our
  `base-rules` hub says why a row is disabled.
- **Our empty states are sentences.** Aurora's is a `0` in a corner above a
  blank rectangle.
- **Our `Difficulty` cannot disagree with its own label** — Aurora ships a
  blueprint filed under Hard, named Hard, categorised Hard, and set to Easy.
- **We refuse loudly and do not succeed silently.** `Create Waypoint` changes
  the area with no message at all.
- **Aurora cannot resize an area after creation either** (`Tileset`, `Length`
  and `Width` are disabled on the Basic tab, `STUDY/26`). Our identical limit is
  not a gap we invented.
