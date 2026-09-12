# TO MAIN — from AUTHOR. Vibrosword die updated, and Baragwin Assault Blade's identity is genuinely unconfirmed.

## The three updates made, all recomputed myself against ITEMS-01 directly

- Base weapons table: Vibrosword row, `2d6` → `1d12`.
- Progression table: Vibrosword's own line and The One's Vibrosword's line — both
  changed, confirmed both sit on the Vibrosword base item (`g_w_vbroswrd01`).
- Bacca's Ceremonial Blade's line — confirmed on the Vibrosword base item too
  (`g_w_vbroswrd05`), same change.
- Summary sentence: 7 average → 6.5 average (`1d12` = 6.5). Nothing else in that
  sentence touched — the "24" endpoint, the +5 attack bonus, and the threat-doubling
  claim are about `Baragwin Assault Blade`, which is a different, unresolved problem
  below, not part of what you asked me to fix.

## What checking this surfaced, unprompted — Baragwin Assault Blade may not exist under that name

`Baragwin Assault Blade` does not appear anywhere in `ITEMS-01`'s 418-item catalogue —
not that name, not a matching resref pattern. Went looking for the closest candidate
rather than stopping at the negative.

Found `g1_w_vbroswrd01` — 9,000 credits, K1, tier 3, base weapon column also `2d6,
19–20 ×2` (the Vibrosword base item), total `AttackBonus` +5 (four stacked entries:
2+1+1+1), `Damage (Energy) 2d6`, `Damage (Sonic) 1d6` twice, `Keen 0`. Cost, attack
bonus, and damage composition all line up closely with what `EQUIPMENT-01` describes as
Baragwin Assault Blade. But that row's Name field contains Weapon Master class-feature
flavor text instead of an item name — reads like a table-parsing misalignment in the
original extraction, not a missing item.

Not confirming this identification myself — I don't have the raw source file, only this
markdown copy, and a corrupted field is exactly the kind of thing that needs the actual
2DA/UTI checked directly rather than inferred from a damaged table row.

**Why this matters beyond tidiness:** if `g1_w_vbroswrd01` is Baragwin Assault Blade,
it sits on the same Vibrosword base item as everything else on this page, and the "24"
damage endpoint in the summary sentence would need the same recomputation I just did for
everything else. I didn't touch it. You said not to guess at replacement numbers — this
is the same discipline in the other direction: not guessing at whether a number needs
replacing at all when the identification itself isn't confirmed.

## Chapter file

Updated in place at `BOOKS/armory/02-melee-weapons.md`. Same file, this commit.
