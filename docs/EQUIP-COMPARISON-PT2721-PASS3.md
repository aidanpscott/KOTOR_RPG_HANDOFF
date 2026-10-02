# EQUIP COMPARISON — PASS 3 (PT-2725) — OUR SIDE CAPTURED, K2 SIDE PENDING

Status: **NOT READY FOR SIGN-OFF.** A row passes only when compared fresh against K2 in this pass; K2 is not running, and the owner loads K2 saves by hand. Our side is
captured below (`HANDOFF/BUILD/screens/pt2721-equip-loop/pass-3/`, 1920×1080, the loop's `000008` gear: 8 worn, 14 bagged). K2's side needs `000008 - game7` loaded and Equip opened.

Status: **PASS** (fresh K2 comparison) · **FAIL** · **EXCUSED** (a named ruling) · **PENDING-K2** (ours captured, K2 comparison not yet made).

| Row | Item | Ours (pass 3) | Status |
|---|---|---|---|
| 1 | frame | unchanged | EXCUSED — `ASSET-REPLACEMENT-01` / `PT-1309` ("reuse as reference, recreate close but ours"; `PT-1105`, `BUILDER-VISION-01 §7`) |
| 13 | grid shape | unchanged | EXCUSED — owner, `PT-2721` |
| 14 | slot cell size | diamond kept, scaled to fit, text at K2's size | **EXCUSED — owner, `PT-2725` (DECISION A)** |
| 8b | Inventory icon dim | pulses 72–100 % of its tint on the shared 1.6 s clock; cause: `HILIGHT PULSING=1` on every `top_p.gui` button, so the focused one breathes | PENDING-K2 (fresh K2 capture; K2's five earlier captures spanned (36,142,119)–(43,174,147), the others constant) |
| readout | weapon readout | no ATKL/ATKR; damage range over attack modifier beside each hand: `4-14 / -2` and `4-18 / -2` | PENDING-K2 (the numbers differ from K2's 3-17/−6 and 5-23/0 because the characters' stats differ, not the layout) |
| config | "Config 1/2" labels | (47,196,165), 71 px wide | PENDING-K2 (K2 measured (49,196,165), 71 px in pass 2) |
| hover | last-row hover | pointer on the last row with another row selected: border (204,51,0) | PENDING-K2 (K2's measured hover is (204,51,0)) |
| 36b | Light Combat Suit Defence | pane "Defense Bonus: 3"; **DEF 17** on the figure (was 18) | **FIXED, un-excused** (was a missing item property, not a ruling — `PT-2128`/`PT-2144`); PENDING-K2 fresh compare |
| pane/robe | Jedi Robe pane | `Feats Required:` / `Jedi Defense` / two blanks / `Defense Bonus: 1` / `Regenerate Force Points: 1` / prose, no Max Dexterity | PENDING-K2 |
| pane/light | Light Combat Suit pane | `Armor Proficiency -  Light`, `Defense Bonus: 3`, `Max Dexterity Bonus: +5`, prose | matches the K2 capture on file (`crop-k2-description-body.png`); PENDING fresh K2 |
| pane/medium | Jamoh Hogra's Battle Armor pane | two feat lines (`Armor Proficiency -  Medium`, `-  Light`), `Defense Bonus: 7`, `Max Dexterity Bonus: +2` | **FAIL until observed** — how K2 prints a base type that lists two feats has never been seen |
| pane/weapon | lightsaber pane | `Damage: Energy, 2-20`, `Critical Threat:` / `19-20,x2` | matches the K2 capture on file; PENDING fresh K2 |
| pane/non-energy | a non-energy weapon's "Damage:" line | `Damage: Piercing, 1-10` is our extrapolation | **FAIL until observed** — `000008` holds no non-energy weapon (blasters are energy); needs a K2 save that carries a vibroblade |
| feat names | source of the Feats Required text | installed TLK via `feat.2da` (`extract_base_feats.py`); id 43 is `WEAPON_PROF_LIGHTSABER`, its TLK name "Weapon Proficiency: Lightsaber"; `Heavy_Repeating_Blaster` is Heavy Weapons in K1, Blaster Rifle in K2 | data source settled; the colon→dash rule is a hypothesis from three K2 panes, PENDING more K2 panes |

## What K2 needs to show (owner action)

1. Load `000008 - game7`, open Equip → Body: capture the four armour panes (Light Combat Suit, Jedi Robe, Reinforced Fiber Armor, **Jamoh Hogra's Battle Armor** — the two-feat case), the pointer resting on the last row.
2. For the non-energy weapon: a K2 save with a vibroblade (or any non-energy weapon) in the right-hand list. `000003 - stocked` may hold one; the brief reserves that slot, so I have not opened it.
