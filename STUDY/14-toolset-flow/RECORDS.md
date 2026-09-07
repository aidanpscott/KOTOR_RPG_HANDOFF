# STUDY 14 — Aurora's flow, launch to a placed creature: records

**Description only.** Judgement is in `FLAWS.md`.

## ⚠ Evidence classes, and the limit that matters most

Three kinds of statement appear below and are labelled at every point:

- **DFM** — read out of the 105 parsed binary form streams in `nwtoolset.exe`
  (Beamdog EE `1.5.0.5`, the same binary as `STUDY/12-toolset-ui`). Strong for
  structure, captions, and **design-time defaults**.
- **DOC** — the shipped changelogs in `lang/en/docs/`.
- **⚠ COULD NOT DETERMINE** — lives in compiled Object Pascal. **Not disassembled.**

**⚠ The limit that shapes this whole study:** a DFM records the value a property
has *when the form is loaded*, not what it has *after the form's code runs*. So
"enabled at design time" is **not** "enabled at launch", and every enable rule,
every list population, every "Next is blocked until you type a name" is code I
cannot read. **The toolset was not run.** Where that bites, it is marked.

---

## R14.01 · Launch does not open on the main window — it opens on a question

**DFM.** `TdlgWelcome`, `bsDialog`, `poScreenCenter`, captioned
*"Aurora Neverwinter Nights Toolset"*:

```
TLabel        lWelcomeTitle     "Welcome!"
TLabel        lWelcomeMessage   "Create your own Neverwinter Nights modules using the Aurora …"
TLabel        lWelcomePrompt    "What would you like to do?"
TRadioButton  rbCreateNew       "Create a new Module"
TRadioButton  rbOpenExisting    "Open an existing Module:"
TListBox      lbModuleFiles     (empty at design time)
TRadioButton  rbDoNothing       "Start normally"
TCheckBox     xbShowAtStartup   "Show this screen at startup"
TButton       bOK / bCancel
```

**Three options, and the third is "Start normally"** — which is itself the
admission that the other two are the expected ones.

**⚠ COULD NOT DETERMINE:** which radio is pre-selected (none carries
`Checked = True` at design time), whether `xbShowAtStartup` is on by default at
runtime (it is off at design time but is obviously read from a setting), and
whether the dialog is modal.

## R14.02 · What "no module" looks like: everything is present, almost nothing is off

**DFM.** `TfrmFrame`'s caption is `NeverWinter ToolSet - No Module`, so it opens
empty. Every pane is present and visible at design time — **there is no
"nothing loaded" layout**:

```
ctlbFrame   (toolbars)   Visible default true
fraInventory (tree)      Visible default true
pArea       (canvas)     Visible default true
fraPalettes (palette)    Visible default true
pBottom     (log+status) Visible default true
all five toolbar panels  Visible default true
all three splitters      Visible default true
```

Of the **59 `TAction`s**, exactly **7 carry `Enabled = False`** at design time:

```
actClose · actSave · actSaveAs · actCopy · actCut · actPaste · actWizardCreature
```

**⚠ Six of those seven are obvious** — you cannot close, save or paste with
nothing loaded. **`actWizardCreature` is the odd one**, since `actWizardDoor`,
`actWizardItem`, `actWizardPlaceable`, `actWizardStore`, `actWizardSound`,
`actWizardTrigger`, `actWizardWaypoint`, `actWizardArea` and `actWizardModule`
are all left enabled at design time.

**⚠ COULD NOT DETERMINE, and it is the important one:** the other 52 are almost
certainly disabled at runtime when no module is loaded — an `OnUpdate` handler
is the normal VCL mechanism and it is code. **The DFM proves only what the
designer set as the starting value.** It does not prove what the user sees.

## R14.03 · The two trees are empty by design; the palette's shape is not

**DFM.** `fraInventory.tvMain` has **zero design-time nodes**. So does every
palette tree. The palette's *structure*, though, is fully authored:

```
pcMain      tabs: Standard · Custom
pcStandard  tabs: Creatures · Doors · Encounters · Items · Placeables ·
                  Sounds · Stores · Triggers · Waypoints · Terrain   (10)
pcCustom    tabs: the same nine, WITHOUT Terrain                      (9)
```

**⚠ Terrain is Standard-only.** There is no custom-terrain tab.

## R14.04 · ⚠ The palette switcher says the verb out loud

**DFM.** `pPaletteSwitcher` holds nine `TToolButton`s whose `Hint` values are:

```
Paint Creatures · Paint Doors · Paint Encounters · Paint Items ·
Paint Merchants · Paint Placeable Objects · Paint Sound Objects ·
Paint Triggers · Paint Waypoints
```

**Nine buttons, one verb.** Terrain is switched separately, by `sbTerrain` in
the palette's own header rather than by the switcher.

## R14.05 · The Module Wizard has four pages and asks ONE question

**DFM.** `TdlgModuleWizard`, `TPageControl pcSteps`, four `TTabSheet`s:

| Page | Contains | Asks |
|---|---|---|
| `tsStart` | three labels, no input | **nothing** |
| `tsModuleCreation` | `TEdit eModuleName` + `TButton bModuleName` captioned `...` | **the module name** |
| `tsAreaCreation` | `TListBox lbAreas` + `TButton bNewArea` "New Area" | **nothing directly** — it launches the Area Wizard |
| `tsFinish` | four labels, no input | **nothing** |

The wizard's own words:

> `tsStart` — *"This wizard will take you step by step through the creation of a
> basic module with things like areas, creatures, treasure and more."*
>
> `tsAreaCreation` — *"Every module needs at least one area. Areas are easily
> created using the area wizard. Use the area wizard now to create as many areas
> as you would like. You can always create more areas later by accessing the
> wizard in the main menu."*
>
> `tsFinish` — *"You now have a playable module that you can adventure on your
> own, give to friends or explore in a group."* and *"The terrain and game object
> palettes contain all kinds of interesting things like creatures and items,
> which you can place in your area."*

**⚠ `eModuleName` has no design-time `Text`.** There is **no default module
name.** The `...` button beside it is the localised-string editor
(`TdlgLocString` exists as its own form).

**⚠ The area list is a display, not a question.** The wizard's second input
control is a listbox you never type into.

**⚠ COULD NOT DETERMINE:** whether `Next` is blocked on an empty name, and
whether `Next` is blocked on an empty area list despite the page insisting
every module needs one.

## R14.06 · The Area Wizard has three pages and asks four things, three of which have defaults

**DFM.** `TdlgAreaWizard`, captioned `Area Wizard`:

| Page | Control | Default |
|---|---|---|
| `tsNameAndTileSet` | `TEdit eName` | **none — empty** |
| | `TListBox lbTileSets` | **empty at design time**, filled at runtime |
| `tsSize` | `TListBox lbSize` (presets) | **empty at design time** |
| | `TEdit eWidth` / `TUpDown udWidth` | **`Text = 2`, `Min 2 Max 32 Position 2`** |
| | `TEdit eHeight` / `TUpDown udHeight` | **`Text = 2`, `Min 2 Max 32 Position 2`** |
| `tsFinish` | `TCheckBox xbLaunchAreaDialog` "Launch Area Properties Dialog" | **unchecked** |
| | `TCheckBox xbOpenNewArea` "Open Area in the Area Viewer" | **`Checked = True`** |

Its own words: *"Please enter a name for the new area and select a tileset."*,
*"Please choose a size for the new area."*, *"This area is now ready to be
created. Click Finish to add the area to your module."*

**⚠ The size floor is 2×2 and it is also the default.** An author who presses
through gets the smallest legal area, not a middling one.

**⚠ `Open Area in the Area Viewer` defaults ON.** Finishing the wizard puts you
in front of the thing you just made without asking again.

**DOC, corroborating:** *"Increased height of Area Wizard dialog so that all
tilesets are visible without having to scroll the listbox."* — confirms
`lbTileSets` is runtime-filled and long enough to have been a usability problem.

**⚠ COULD NOT DETERMINE:** whether a tileset is pre-selected, and what the
`lbSize` presets are.

## R14.07 · The wizards share a base, and this one overrides its captions

**DFM.** `TdlgWizard` is a base form carrying exactly the furniture:

```
TBevel bvDivider · TButton bHelp "&Help" · bFinish "&Finish"
TButton bNext "&Next" · bBack "&Back" · bCancel "&Cancel"
TPageControl pcSteps
```

**⚠ In `TdlgModuleWizard` and `TdlgAreaWizard` those five buttons have EMPTY
captions.** They are image buttons in the concrete wizards.

**DOC, corroborating:** *"Fixed BadStrRef hint when mousing over area listbox
and Finish image in Module Wizard."* — *"Finish image"*, in Beamdog's own words.

## R14.08 · Every wizard, measured the same way

**DFM.** Pages are `TTabSheet` count; inputs are the eleven interactive classes;
"w/default" counts a non-empty `Text`, a `Checked = True`, a set `ItemIndex`, or
a `TUpDown` (which always carries a `Position`).

```
WIZARD                        pages  inputs  w/default
TDLGMODULEWIZARD                  4       2          0
TDLGAREAWIZARD                    3       9          5
TDLGPLACEABLEWIZARD               2       2          0
TDLGSTOREWIZARD                   2       3          0
TDLGBLUEPRINTWIZARD               2       2          0
TDLGDOORWIZARD                    4       2          0
TDLGENCOUNTERWIZARD               3       2          0
TDLGTRIGGERWIZARD                 3       4          0
TDLGWAYPOINTWIZARD                3       5          0
TDLGITEMWIZARD                    4       6          1
TDLGSOUNDWIZARD                   5       8          1
TDLGSTORESETUPWIZARD              4       9          3
TDLGPLOTWIZARD                    7       7          0
TDLGCREATUREWIZARD                0      35         16
TDLGPLOTNODEWIZARD               10      53          3
TDLGSCRIPTWIZARD                 19     107         26
TFRMCREATURELEVELUPWIZARD         0      25         16
```

**⚠ The two wizards on the shortest path are the two smallest.** Module and Area
are 4 pages / 2 inputs and 3 pages / 9 inputs. The Script Wizard is 19 pages and
107 inputs, and **nothing on the path to a placed creature touches it.**

**⚠ `TDLGCREATUREWIZARD` reports 0 pages** — it has no `TPageControl`. It is a
single-page form wearing the word "wizard".

## R14.09 · The minimum sequence

**DFM, assembled from the forms above.** Launch to one creature standing in one
area, taking every default that exists:

```
 1  TdlgWelcome            choose "Create a new Module"          → OK
 2  Module Wizard  tsStart          (nothing to do)              → Next
 3  Module Wizard  tsModuleCreation TYPE the module name         → Next
 4  Module Wizard  tsAreaCreation   click "New Area"             → Area Wizard
 5    Area Wizard  tsNameAndTileSet TYPE a name, PICK a tileset  → Next
 6    Area Wizard  tsSize           (2 × 2 already filled)       → Next
 7    Area Wizard  tsFinish         (open-in-viewer already on)  → Finish
 8  Module Wizard  tsAreaCreation   the area is now in the list  → Next
 9  Module Wizard  tsFinish         (nothing to do)              → Finish
10  Main window, area already open in the viewer
11  Palette → Creatures → place one
```

**Four windows** — welcome dialog, module wizard, area wizard, main window.
**Nine page-views** before the main window. **Eleven steps to a placed creature.**

**⚠ COULD NOT DETERMINE:** whether step 11 needs the Select Mode toggled to
Objects first. `sbModeObject`'s hint is *"Select Objects (Hit F10 to toggle)"*
and which mode is active at launch is runtime state.

## R14.10 · The decision points, counted

**DFM.** Every point on `R14.09` at which the software waits for a person:

| # | Decision | Default in the DFM? |
|---|---|---|
| 1 | Welcome: create / open / start normally | **⚠ undetermined** |
| 2 | Module name | **NO — empty** |
| 3 | Area name | **NO — empty** |
| 4 | Tileset | **⚠ undetermined** (runtime-filled) |
| 5 | Area width | **yes — 2** |
| 6 | Area height | **yes — 2** |
| 7 | Launch Area Properties Dialog | **yes — off** |
| 8 | Open Area in the Area Viewer | **yes — on** |

**Eight decision points. Four have a default you can press past. Two have no
default and cannot be defaulted — they are names. Two are undetermined.**

**⚠ So the irreducible count is two pieces of typing** — a module name and an
area name — **plus one list selection**, if the tileset is not pre-selected.
Everything else on the shortest path is `Next`.
