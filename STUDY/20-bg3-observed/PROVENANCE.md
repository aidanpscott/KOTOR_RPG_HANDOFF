# Provenance — every asset in this study, and the archive it came from
All paths are inside `Baldurs Gate 3/Data/`. Read with `STUDY/19-input-and-combat/tools/lspk.py`.

## Images in `shots/`
| image | built from |
|---|---|
| `bg3_resource_states.png` | `Game.pak` → `Public/Game/GUI/Assets/ActionResources_c/Icons/{,Highlight/,Missing/,Used/}{ActionPoint,BonusActionPoint,ReactionActionPoint}.DDS` — 12 files, 56×56 each |
| `bg3_movement_states.png` | same tree, `…/Icons/{,Highlight/,Missing/,Used/}Movement.DDS` — 4 files |

## XAML read

| file | bytes | archive |
|---|---|---|
| `Mods/MainUI/GUI/Pages/ActiveRoll.xaml` | 160,303 | `Game.pak` |
| `Mods/MainUI/GUI/Pages/PassiveRoll.xaml` | 6,589 | `Game.pak` |
| `Public/Game/GUI/Library/DiceAnimation.xaml` | 241,767 | `Game.pak` |
| `Public/Game/GUI/Library/TurnOrderLib.xaml` | 58,068 | `Game.pak` |
| `Mods/MainUI/GUI/Pages/TurnModeInfo.xaml` | 79,021 | `Game.pak` |
| `Mods/MainUI/GUI/Pages/ActionResources_c.xaml` | 57,324 | `Game.pak` |
| `Public/Game/GUI/Library/ActionResourceTemplates_c.xaml` | 69,455 | `Game.pak` |
| `Mods/MainUI/GUI/Pages/HotBar.xaml` | 483,748 | `Game.pak` |
| `Mods/MainUI/GUI/Pages/CombatantsOverlay.xaml` | 35,664 | `Game.pak` |
| `Mods/MainUI/GUI/Pages/CombatLog.xaml` | 42,560 | `Game.pak` |

`gui/PassiveRoll.xaml` is committed verbatim — it is small enough to read whole and it carries the finding.
