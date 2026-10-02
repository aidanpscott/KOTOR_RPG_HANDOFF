# EQUIP COMPARISON — PASS 3 (PT-2725) — FRESH K2 CAPTURES, ONE ROW LEFT FAILING SHORT OF SIGN-OFF

K2 was started by CODER (`steam steam://rungameid/208580`, recipe in `HANDOFF/BUILD/STATE.md`), `000008 - game7` loaded and Equip opened, read-only; a second load of the stocked save (`000003`'s row) for the weapon lists; left through Options → Exit Game. **No slot was written** (slot mtimes unchanged; the only new slot is the owner's `000009 - game8`). Captures: `HANDOFF/BUILD/screens/pt2721-equip-loop/pass-3/` (`k2-*` fresh, `app-*` ours on the rebuilt app).

Status: **PASS** (compared fresh in this pass) · **FAIL** · **EXCUSED** (named ruling).

| Row | K2 (fresh) | Ours | Status |
|---|---|---|---|
| 1 frame | photographed bronze | recreated | EXCUSED — `ASSET-REPLACEMENT-01` / `PT-1309` |
| 13 grid shape | 3×3+ | 7-cell diamond | EXCUSED — owner, `PT-2721` |
| 14 slot cell size | 130×97 | diamond scaled to fit, text at K2 size | EXCUSED — owner, `PT-2725` (DECISION A) |
| 8b Inventory icon | (39,156,131) when sampled; five earlier captures (36,142,119)–(43,174,147); others (49,196,165) | pulses 72–100 % of tint (sampled (34,141,119)); others (47,196,165) | **PASS** — same band, same cause (`HILIGHT PULSING=1`); phase differs by nature |
| Config 1/2 labels | (49,196,165), 71 px | (47,196,165), 71 px | **PASS** |
| weapon readout layout | damage over attack beside each hand, no captions | same, no captions | **PASS** (the numbers differ with the character: K2 3-17/−6, 5-23/0; ours 4-14/−2, 4-18/−2) |
| DEF figure | 17 | 17 | **PASS** (was 18; 36b) |
| pane — Light Combat Suit | `Armor Proficiency -  Light` · Defense Bonus 3 · Max Dex +5 · prose | identical | **PASS** |
| pane — Jedi Robe | `Jedi Defense` · Defense 1 · Regenerate Force Points: 1 · prose | identical | **PASS** |
| pane — Reinforced Fiber Armor | `Armor Proficiency -  Light` · Defense **7** · Max Dex +4 | identical (was 5: the item's own `Armor 2` was not added) | **PASS** after fix |
| pane — Jamoh Hogra's (two-feat base) | **only the first feat** (`-  Medium`) · Defense **11** · Max Dex +2 · `Immunity: Critical Hits` · `Strength: +1` · prose | identical (was two feat lines, 7, no property lines) | **PASS** after fix — settles the two-feat format and the colon→dash rule on a fourth item |
| pane — Short Lightsaber | `Damage: Energy, 2-16` · `Critical Threat:` / `19-20,x2` · **`Balanced: +2/+0 vs. two-weapon penalty if used in the off hand`** · prose | no Balanced line | **FAIL** — `balanced` is null for lightsabers in our data; the game's source for the line is not found |
| pane — Blaster Pistol: Null | `Damage: Energy, 1-8` · **`Range: 23m`** · `Critical Threat:` / **`20-20,x2`** · Balanced line · `No Description Set` | no Range line; threat prints `20`; no Balanced | **FAIL** — Range (K2 23 m; our data 24 m, `baseitems.2da` maxrange 50), the single-number threat form and its ×2 are not in our data |
| pane — non-energy weapon | not observable: `000008` and the stocked save hold only the lightsabers and the blaster | `Damage: Piercing, 1-10` is our extrapolation | **FAIL** until a K2 save carries a vibroblade |
| row border colours | **Owner's reading (2026-10-02):** the last row's red-orange (204,51,0) is K2's **can't-use marker** — the character lacks the feat (Jamoh Hogra's armour; the popup and greyed OK say so). **Pointer hover is WHITE**, as is every control. A *different* orange marks an item that is **new / not yet hovered** in the inventory lists, and it reverts to green or white once the cursor has passed over it (try Down on the stocked save's inventory) | ours paints (204,51,0) under the **pointer** (wrong: should be white) and has neither the can't-use marker, the refusal popup, the greyed OK, nor the new-item marker | **FAIL** — four things unbuilt/wrong: hover colour, can't-use marker + refusal, greyed OK, new-item marker. K2's white hover was not pixel-measured (K2 was closed); measure before changing the constant |
| belts list (empty slot) | None · Adrenaline Amplifier · Cardio-Regulator · Stealth Field Generator · Frozian Scout Belt | the same five (the two Stealth belts are new) | **PASS** |
| Light Combat Suit / sheet / fight | — | `wornAt` +3, +7, +11 feed the sheet and fights | covered by tests, not a K2 row |

## New findings from this pass

1. **Defence is the class plus the item's own `Armor N`** (7, 11) and K2 prints `Immunity:` and an ability line. `EQUIPMENT-01 §5.1/§5.2` reads `Armor N` as selecting a robe's grade; for armour classes K2 adds it. Built (`gen_base_rules.py` writes the finished number on the blueprint, `PT-2144`'s mechanism). **This changes fight Defence for every shipped armour with an `Armor N`** — Main to confirm the rule.
2. **K2's can't-use state** (red-orange row, popup, greyed OK) when the character lacks a required feat, and the separate **new-item** orange: unbuilt. Our pointer hover is painted with the can't-use colour by mistake — hover is white.
3. **Weapon pane lines** K2 prints that our data cannot yet source: `Range`, `Balanced`, the single-number threat's `20-20,x2`.
4. **Droid Equip reference** (owner's `000009 - game8`, T3-M4, Expert Droid 3): `Plating` list holds only None, DEF 14, droid slot icons, droid weapon cells reading `1-4 / +3` — `k2-droid-equip.png`.

NOT READY FOR SIGN-OFF: rows above marked FAIL. Closing suites are for a pass with none, and were not run.
