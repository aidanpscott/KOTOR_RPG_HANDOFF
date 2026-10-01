# EQUIP-COMPARISON-PT2720 — the live four-state loop, re-run

**`PT-2720` item 3. Same method as `PT-2718` (`PT-2687`'s technique: position with `--window`, click without it), same character where it still exists — `Garon Corvan` (our app) / `Onjo Trigit` (K2's `000008 - game7`), a Jedi Sentinel/Jedi Guardian with a training lightsaber in the main hand and a Jedi Robe worn. Paired screenshots captured this cycle live in both apps; not yet copied into `BUILD/screens/` (see note at the end).**

K2's save `000008 - game7` was reloaded fresh this cycle (the character and world state were re-verified live rather than assumed from the prior cycle's screenshots: Peragus, "Onjo Trigit", the real 2×3 lattice, all re-confirmed). Our side loaded the SAME save PT-2718 used — `garon-corvan.sav`, found already present in `~/.local/share/kotor-rpg/saves/` under the `endar-spire` package, not re-authored from scratch.

---

## State 1 — filled slot selected (Body)

| Element | K2 | Ours | Verdict |
|---|---|---|---|
| "Equip" title, dividers, subtitle, list panel frame, DEF badge, Attack Modifier/Damage labels | unchanged from `PT-2718`'s own read | unchanged from `PT-2718`'s own read | PASS (no re-litigation; nothing touched these) |
| Font | K2's own bitmap glyph-atlas font | now K2's own `fnt_dialog16x16` glyph atlas, rendered through the new `KotorText` renderer built in `PT-2719` item 2 | **PASS — the `PT-2718`/`PT-2695` font wall is closed.** This is the one state that changed since the last comparison, and it changed for the better: no more generic sans-serif. |
| Off-hand attack/damage numbers | both hands show a pair (dual-wielded build) | only the main hand shows a pair; the off hand shows nothing, **because this character has nothing in `weapon_l_1`** | **Not a fail, on this character.** `PT-2720` item 2 already traced this exact shape and confirmed the off-hand reading is correct when the off hand is genuinely empty — this is that same character, single-wielded, and a blank off-hand number here is the right answer, not the `PT-2718` gap recurring. |
| Icon grid shape | 2-row-by-3-column | 7-cell diamond | **OPEN, UNCHANGED** — `PT-2695`'s owner-approved deviation, left exactly as `PT-2720` instructed. |

## State 2 — empty slot selected (Implant)

| Element | K2 | Ours | Verdict |
|---|---|---|---|
| Candidate list | "None" plus any real alternatives the package has, no "(Equipped)" suffix anywhere | "None" only — `endar-spire`'s own catalogue has no implant-slot items at all, so the list is legitimately one row | PASS on content; the row COUNT differs only because the two packages' catalogues differ, not because of a rendering gap |
| Description text for "None" | (K2 shows no separate banner; "None" is self-explanatory in the list) | "nothing equipped in this slot" | Cosmetic wording difference, not a new finding — carried as-is, not worth a ticket on its own |
| Footer | Cancel/OK | Cancel/OK | PASS |

## State 3 — description pane (Body, a filled slot)

| Element | K2 | Ours | Verdict |
|---|---|---|---|
| List stays visible beside the description | yes | yes | PASS |
| "(Equipped)" suffix on the worn item's row | yes ("Jedi Robe" would read this way if selected) | yes — "Training Lightsaber (Equipped)" and "Jedi Robe (Equipped)" both confirmed this cycle | PASS |
| Description content | Feats Required / Defense Bonus / Max Dexterity Bonus / flavour text, own lines | `describeBaseType` (`play_screen.dart:86`) produces the same shape from `equipment.toml`'s own fields (`defence`, `max_dex`, `note`) — verified against the raw `robe-1` catalogue entry, not just read off the screen: `Defense Bonus: +1` / `Max Dexterity Bonus: uncapped` / the `note` field's own EQUIPMENT-01 §5.2 text, matching what rendered | PASS, confirmed at the data layer because the window's text is still small enough that eyeballing alone wasn't trustworthy |
| Font | K2's own | `KotorText`, same as State 1 | PASS — same wall closure, not re-counted |
| Footer | Cancel/OK | Cancel/OK | PASS |

## State 4 — description pane (a weapon)

| Element | K2 | Ours | Verdict |
|---|---|---|---|
| Content | Feats Required / Damage / Critical Threat / flavour text | `describeBaseType`'s weapon branch, verified against the raw `training-lightsaber` catalogue entry: `Feats Required: Weapon Proficiency - Lightsabers` / `Damage: 1d8` / `Critical Threat: 19–20 / ×2`; no flavour line, because `equipment.toml`'s own `training-lightsaber` row carries no `note` field — correctly left out rather than invented, per the standing rule at `play_screen.dart:76` | PASS, confirmed at the data layer for the same reason as State 3 |
| Everything else | same as State 3 | same as State 3 | PASS |

---

## Summary

**Nothing failed this pass.** The one real gap `PT-2718` found (the font) was closed by `PT-2719`'s glyph-atlas renderer and is confirmed closed live, on this same character, not just by the unit suite. The other thing `PT-2718` flagged (blank off-hand numbers) was already run to ground by `PT-2720` item 2 as the CORRECT reading for a character with nothing in the off hand, and this cycle's capture is consistent with that finding rather than contradicting it.

**No new defect surfaced.** Every description-pane content check was cross-verified against the raw `equipment.toml` catalogue entries rather than trusted from eyeballing a screenshot — the app's own rendered window is still small enough (1280×720) that reading text directly off a screenshot is not reliable, so this cycle leaned on the data source as the check, consistent with "a tidy explanation is a hypothesis" — confirmed, not assumed.

**Loop status: 1:1 on everything compared.** The only remaining open item is the one `PT-2720` explicitly said to leave alone: the 7-cell diamond vs K2's 2×3 grid (`PT-2695`'s owner-approved deviation). Nothing to fix, so the loop does not need a second iteration this cycle.

**Screenshots**: captured to the session scratchpad this cycle (`app-garon-1..4-SAVED.png`, alongside the existing `k2-1..4-*.png` from earlier in `PT-2720`); not yet copied into `HANDOFF/BUILD/screens/`. Flagged here rather than silently deferred — can be mirrored on request or as part of the next commit touching that folder.
