# CLASS-DEFENCE-01 — all 39 classes, ruled

**`PT-2717`, corrected at `PT-2718`. Every one of our 39 classes now has a wired Class Defence ladder, built in `Lodestar/lib/src/combat.dart`. This file replaces `CLASS-DEFENCE-PROPOSAL-01.md` (renamed, not deleted from history), whose "27 proposed / 6 open" summary was itself wrong — the rows it actually carried were closer to 17 proposed / 9 open — and whose whole "proposal, not built" frame no longer applies now that the owner has ruled every row.**

**The owner's own logic, stated once and applied class by class: the less armour a class may wear, the faster its class Defence grows — KOTOR's own logic (`PT-1544`), for variety. Offsets live on the class pointer (`defenceTrackOf`), never as copied numbers, and any offset result below 0 is floored at 0.**

---

## The two corrections `PT-2717` made to what `PT-2716` built

- **The three Jedi move to K2.** `jedi_consular`/`jedi_guardian`/`jedi_sentinel` all read K2's own `jdc`/`jdg`/`jds` column (byte-identical in `k2_acbonus.2da`, confirmed via `scripts/parse2da.py`) as one named shape, `k2-jedi-step`. The RCR-derived `hold-three-then-two` (Noble/Consular) ladder is **retired for this mechanic** — nothing else in `defenceTrackOf` pointed at it, so it was removed from `defenceTracks` rather than kept unread.
- **The Smuggler reads K2 above L21, not a clamp.** K1's own `scd` column (the class Smuggler absorbed) covers L1-21; K2's own `scd` column — real data, not an extrapolation — covers L22-30. The step at L22 (+6 → +8) is the seam between two real sources, not a discontinuity in either one.

---

## The seven shapes

| Shape | Source | L1 | Steps | L30 |
|---|---|---|---|---|
| `k2-soldier-step` | K2 `sol` | 0 | +2 at 6/12/18/24/30 | +10 |
| `k2-scoundrel-step` | K2 `scd` | +2 | +2 at 6/12/18/24/30 | +12 |
| `smuggler-composite` | K1 `scd` 1–21, K2 `scd` 22–30 | +2 | +2 at 7, 13; then K2's own column | +12 |
| `k2-jedi-step` | K2 `jdc`/`jdg`/`jds` | +2 | +2 at 7/13/19/25 | +10 |
| `k2-prestige-step-five` | K2 `jwm`/`jwa`/`sas`/`sma` | +2 | +2 at 6/11/16/21/26 | +12 |
| `k2-prestige-step-eight` | K2 `jma`/`sld`/`tec` | +2 (0 for `tec`) | +2 at 9/17/25 | +8 (0 for `tec`) |
| `flat-zero` | K2 `tec` | 0 | none | 0 |

`step-every-two` (RCR's own Soldier shape) and `k1-scoundrel-step` (K1's own `scd`, the first half of `smuggler-composite`) remain defined in `Lodestar` for the record; nothing points at `step-every-two` and `k1-scoundrel-step` is read only through `smuggler-composite`.

---

## Base classes (19)

| Class | Role / armour | Ladder | Reason on record |
|---|---|---|---|
| Soldier | Full armour, any weapon | `k2-soldier-step`, offset 0 | K2's own column — K1 gives flat 0 |
| Smuggler | Light armour, covert | `smuggler-composite`, offset 0 | K1's own `scd` (the class it absorbed) for L1-21, K2's own `scd` for L22-30 |
| Scout | Light/medium armour | `k2-soldier-step`, offset -1 | RCR Table 3-5 f.48 / 3-6 f.50: exactly the Soldier's own column minus 1, on KOTOR's scale (`FROM-EXTRACTOR-RCR-SCOUT-DEFENCE.md`). K1 and K2 both give flat 0 |
| Jedi Consular | Light/no armour, Force | `k2-jedi-step`, offset 0 | Owner: K2 for all three Jedi |
| Jedi Guardian | Light/no armour, Force | `k2-jedi-step`, offset 0 | Owner: K2 for all three Jedi |
| Jedi Sentinel | Light/no armour, Force | `k2-jedi-step`, offset 0 | Owner: K2 for all three Jedi |
| Bounty Hunter | Light AND medium armour, all weapons | `k2-soldier-step`, offset -1 | Owner's own row (`ACTION-ECONOMY-01 §18.2`, `PT-107`) |
| Agent | Covert, lightly armoured | `k2-scoundrel-step`, offset 0 | K2's own Scoundrel column |
| Treasure Hunter | Light armour, agility | `smuggler-composite`, offset 0 | The Smuggler's own composite |
| Saboteur | Light armour | `smuggler-composite`, offset 0 | Already bound (`PT-1545`: "points at the twins ladder rather than carrying a copy") |
| Duelist | Light armour, footwork | `k2-jedi-step`, offset 0 | A fencer's footwork without the Force |
| Brawler | No armour, unarmed | `k2-prestige-step-five`, offset 0 | Fights close with no armour |
| Machinist | Protected by gear | `k2-prestige-step-eight`, offset 0 | Protection from gear, not training |
| Medic | Works from cover | `k2-prestige-step-eight`, offset -2 | Support, not a front-line archetype |
| Engineer | Droid-chassis class | `flat-zero`, offset 0 | Droid Defence comes from plating earned by level (`PT-577`); a class ladder would double-count |
| Marksman | Droid-chassis class | `flat-zero`, offset 0 | Same reason as Engineer |
| Sith Warrior | Mirrors Jedi Guardian | `k2-jedi-step`, offset 0 | `PT-124`/`PT-125` |
| Sith Assassin | Mirrors a Jedi | `k2-jedi-step`, offset 0 | `PT-124`/`PT-125` — all three Jedi share one shape, so every mirror resolves the same |
| Sith Inquisitor | Mirrors Jedi Consular | `k2-jedi-step`, offset 0 | `PT-124`/`PT-125` |

## Prestige classes (20)

| Class | Role / armour | Ladder | Reason on record |
|---|---|---|---|
| Jedi Weaponmaster | K2 Force prestige | `k2-prestige-step-five`, offset 0 | K2's own `jwm` column |
| Jedi Watchman | K2 Force prestige | `k2-prestige-step-five`, offset 0 | K2's own `jwa` column |
| Jedi Sage | K2 Force prestige | `k2-prestige-step-eight`, offset 0 | K2's own `jma` column |
| Sith Battlemaster | K2 Force prestige | `k2-prestige-step-five`, offset 0 | K2's own `sma` column |
| Sith Marauder | K2 Force prestige | `k2-prestige-step-five`, offset 0 | K2's own `sas` column (`PT-216`'s reassignment) |
| Sith Sorcerer | K2 Force prestige | `k2-prestige-step-eight`, offset 0 | K2's own `sld` column |
| Blademaster | Non-Force, heavy melee | `k2-prestige-step-five`, offset 0 | The non-Force Weaponmaster |
| Gunslinger | Quick, covert | `k2-scoundrel-step`, offset 0 | K2's own Scoundrel column |
| Operative | Quick, covert | `k2-scoundrel-step`, offset 0 | K2's own Scoundrel column |
| Scoundrel (prestige) | Direct Smuggler descendant | `smuggler-composite`, offset 0 | Direct line from the Smuggler's own composite |
| Shadow Hunter | Direct Smuggler descendant | `smuggler-composite`, offset 0 | Direct line from the Smuggler's own composite |
| Shock Trooper | Mobile, medium kit | `k2-soldier-step`, offset +1 | Above the Soldier's own column |
| Pirate | Mobile, medium kit | `k2-soldier-step`, offset +1 | Above the Soldier's own column |
| Commando | Soldier continuation | `k2-soldier-step`, offset 0 | Direct Soldier continuation, no offset |
| Officer | Leads from behind | `k2-prestige-step-eight`, offset 0 | Commands rather than fights directly |
| Beast Master | The beast takes the hits | `k2-prestige-step-eight`, offset 0 | Owner's own reasoning (same shape as Officer) |
| Tech Specialist | K2-only, `tec` column real | `flat-zero`, offset 0 | K2's own `tec` column — the strongest possible source, IS the class the column names |
| Sharpshooter | Scout/Marksman/Bounty Hunter lineage | `k2-soldier-step`, offset -1 | "Follows" the Scout (owner's own wording, `PT-2717`) |
| Juggernaut | Heavy armour, the only class besides Soldier granted it | `k2-prestige-step-eight`, offset -2 | Owner-ruled, `PT-2718` |
| Droid Master | Commands droids, does not fight through them | `k2-prestige-step-eight`, offset -2 | Owner-ruled, `PT-2718`, same row as Juggernaut |

---

## Juggernaut and Droid Master — corrected at PT-2718

`PT-2717`'s own message was cut off mid-table at this exact row on Main's side — the text ran `"Juggernaut, **Droid**"` directly into an unrelated paragraph about the Scout's extractor marker, with no ladder or reason visible for either class. That was Main's own truncation, not an owner gap: flagged rather than silently guessed, and the flag caught it.

The reconstruction built then — Juggernaut on `k2-soldier-step` at offset 0 (the Soldier's own column, unmodified), Droid Master on `k2-prestige-step-eight` at offset 0 (Officer/Beast Master's own exact numbers) — was a reasoned guess and was wrong. **The owner's real row for both, delivered at `PT-2718`: `k2-prestige-step-eight`, offset -2, floored at 0** (0 at L1-8, +2 at L9-16, +4 at L17-24, +6 at L25-30). Neither class shares a ladder with Soldier or Officer any more.

---

## Summary

**All 39 classes have a wired, owner-ruled ladder.** 19 base + 20 prestige, including the six K2 Force-prestige classes (unchanged from `PT-2716`) and Juggernaut/Droid Master (corrected at `PT-2718`, above). **Nothing in this file is a proposal or a reconstruction any more.**
