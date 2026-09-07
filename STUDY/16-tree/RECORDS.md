# STUDY 16 — Aurora's module tree: records

**Description only.** Judgement is in `FLAWS.md`. Same binary as `STUDY 12`,
`14` and `15` — Beamdog EE `1.5.0.5`. **The toolset was not run.**

**Evidence classes:** **DFM** (parsed form streams), **PE** (resource sections),
**⚠ COULD NOT DETERMINE** (compiled Object Pascal, not disassembled).

---

## R16.01 · The tree is empty at design time, and lazily filled

**DFM.** `TfraMainInventory` holds exactly one `TTreeView tvMain`, `alClient`,
**zero design-time nodes**, plus a popup menu and a 14-action list.

Its full property set is small and every interesting entry is a handler:

```
OnExpanding · OnChange · OnDblClick=actGotoExecute · OnEditing · OnEdited
OnKeyDown · OnMouseDown · OnMouseMove
OnCustomDrawItem · OnAdvancedCustomDrawItem
Indent=19 · HideSelection=False · RightClickSelect=True · ToolTips=False
```

**⚠ `OnExpanding` is the load-bearing one.** It is the handler for "a node is
about to open" and exists to fill children on demand. **A flat list does not
need it.**

**⚠ No `Images` property.** No ImageList is bound at design time, so the icon
indices the brief asked about **are assigned in code and their order cannot be
read from the DFM.**

## R16.02 · The tree's own verbs

**DFM.** `alMain`, fourteen actions, and the popup that exposes them:

```
actGoto            "Go To"            — shown as "View Area" AND "Focus on Object"
actLocationAdjust  "Adjust Location"
actRescanInstances "Refresh Area"
actAreaExport      "Export Area"
actEdit            "Edit" / "Properties"
actNew             "New"
actRemove          "Delete"
actCopy · actCut · actCopyResource "Create Copy"
actAddToPalette    "Add to Palette"
actVariables       "Variables"
actBuild           "Build"
actRefreshConversations
```

**⚠ Two different captions share `actGoto`: "View Area" and "Focus on Object".**
One action, two node kinds. **And "Adjust Location" only means anything on a
placed instance.**

## R16.03 · ⚠ The string table does NOT name the categories — scoped negative

**PE.** The binary carries **27 `RT_STRING` blocks, 428 entries**. I read all of
them. **Every one is a VCL runtime string** — ids 65104 and up, the Delphi
framework's own messages: *"%d is an invalid PageIndex value"*, *"JPEG error
#%d"*, *"Failed to delete tab at index %d"*.

**Not one toolset category name is in the string table.** Category names are
compiled literals.

## R16.04 · ⚠ The category vocabulary, from the one form that enumerates it

**DFM.** `TdlgVerifyModule` ("Verify Module") checks a module category by
category, and its checkboxes carry **stable `Tag` numbers** — the same tag on
every checkbox for the same category across three independent columns.

| Tag | Category |
|---|---|
| 5 | **Scripts** |
| 6 | Encounters |
| 8 | **Blueprints** |
| 14 | **Conversations** |
| 16 | Creatures |
| 17 | Doors |
| 18 | Items |
| 19 | Placeables |
| 20 | Sounds |
| 21 | Stores |
| 22 | Triggers |
| 23 | Waypoints |
| 24 | Creature CR |
| 25 | Palettes |
| 28 | **Areas** |
| 29 | Blueprints *(spell-check column)* |

**⚠ And the Spell Check column is laid out as a hierarchy.** Read down by `Top`:

```
Areas            Top 30
Conversations    Top 50
Blueprints       Top 70
  Creatures      Top 98      ← indented under Blueprints, Left 16, 28px gap
  Doors          Top 118
  Encounters     Top 138
  Items          Top 158
  Placeables     Top 178
  Sounds         Top 198
  Stores         Top 218
  Triggers       Top 238
  Waypoints      Top 258
```

**Areas, Conversations and Blueprints are peers; the nine object types are
children of Blueprints.**

**⚠ THIS IS THE VERIFY DIALOG'S VOCABULARY, NOT PROVEN TO BE THE TREE'S.** It is
the only place in the binary that enumerates a module's contents as a structure,
and the tree is populated from the same module — but **nothing in the DFM ties
this list to `tvMain`.** Stated as the strongest available evidence, not as the
tree's node list.

## R16.05 · Scripts are a first-class module category

**DFM.** `xbUnusedScripts` (Tag 5) and `xbCompileScripts` (Tag 5) both exist —
**Scripts appear under "Unused" and under "Compile"**, alongside Areas,
Conversations and Blueprints.

**⚠ COULD NOT DETERMINE whether Scripts are a BRANCH OF THE TREE.** `STUDY 12`
established the Script Editor is the one genuine second window and is reached
from `Tools`. That it is *also* a tree branch is not shown by any DFM.

## R16.06 · The palette's categories, exactly

**DFM.** `TfraMainPalette`:

```
pcMain      Standard · Custom
pcStandard  Creatures · Doors · Encounters · Items · Placeables ·
            Sounds · Stores · Triggers · Waypoints · Terrain     (10)
pcCustom    the same nine, WITHOUT Terrain                        (9)
```

And the switcher's nine buttons, hinted:

```
Paint Creatures · Paint Doors · Paint Encounters · Paint Items ·
Paint Merchants · Paint Placeable Objects · Paint Sound Objects ·
Paint Triggers · Paint Waypoints
```

**⚠ The palette's nine are EXACTLY the nine children of `Blueprints` in
`R16.04`.** Same names, same set, no additions, no omissions.

**Terrain is the only palette entry that is not a blueprint category, and it is
Standard-only.**

## R16.07 · Instances are area-scoped, and there is a tool for finding them

**DFM.** `TdlgFindInstance`, `fsStayOnTop`:

```
Search For        (what)
In Area           TComboBox cbArea       ← a list of AREAS
From Blueprint    (which template)
With Tag          (which instance)
```

**⚠ "In Area" is a filter.** An instance is looked up *within* an area, and the
existence of a dedicated always-on-top search dialog says **browsing to an
instance through the tree was not considered sufficient.**

## R16.08 · How big an Aurora area is

**DFM, re-confirmed from `STUDY 14`.** The Area Wizard:

```
udWidth   Min=2  Max=32  Position=2
udHeight  Min=2  Max=32  Position=2
```

**2 to 32 tiles a side — up to 1,024 tiles in one area.** An NWN tile is a
room-or-corridor-sized chunk of geometry, not a square a token stands on.

**⚠ So an Aurora area is not a room. It is a building, a dungeon level, or a
stretch of countryside**, and its contents are many.

## R16.09 · ⚠ Haks and the custom TLK are in PROPERTIES, not the tree

**DFM.** `TfrmIFOProp` ("Module Properties") has five tabs:

```
Basic · Events · Advanced · Description · Custom Content
```

and the **Custom Content** tab is:

```
TLabel     "This is a list of Hak Paks used by this module"
TListBox   lbHakFiles
TButton    Add · Remove · Move Up · Move Down      ⚠ AN ORDERED LIST
TButton    "Check for Conflicts..."
TLabel     "Custom Tlk File"
TComboBox  cbCustomTlkFile
```

**⚠ Move Up and Move Down.** The hak list is **ordered, by hand, in a properties
dialog** — and `TdlgHakPak` ("Hak Pak Conflict Analysis") exists to tell you
what that order collided with.

**Nothing about custom content appears in the module tree.**
