# TEST 177 — recheck of the TEST 176 fixes, class kits and the Motivator slot

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 launched. Text only; screenshots in `KOTOR_RPG_MAIN_WORK/media/screens/test-177/` (MAIN_WORK `25bcb965`). Read first: Coder's TEST 176 fixes entry and the Motivator research.

## Build

App `d69382ff22fe3d81a0cae44cb508280ff54d12c2` (git archive, lock unchanged after build). Lodestar `be1319a5020337e561e6094bd7d2784e866d0045` = lock. Lens `bfc9bff8daeac99c39da6a38283f41dd1551faa2` = lock. Shelf `6f74e54` (my data dir). `tool/env.sh` sourced. check_shelf clean (31 rules, 112 blueprints). Fresh fixtures. `KOTOR_ENEMY_TURN_PAUSE_MS=4000`.

## Summary: two pass, three fail or are partial

| # | Check | Result |
|---|---|---|
| 1 | Off-turn | **PASS** for what I could reach (Precognition Ambush, off my turn): **Switch Weapons** changes nothing, and the board's status line reads "switching weapons — not on the enemies' turn; wait for your own" (`1c`, `1d`). A **weapon slot** pick is refused in a box: "putting your weapon away — not on the enemies' turn; wait for your own" (`1b`). Armour is refused too (`1a`). **Door / conversation off-turn: not reached**: this room has no door, and the seer wasn't reachable during the fight. Note: these lines say "enemies' turn" even when it's Kael's turn |
| 2 | Class kits | **FAIL (Config 2)**: Soldier, Bounty Hunter, Smuggler, Medic, Sith Warrior and the droid Engineer each take body armour, boots and the Config 1 right-hand weapon off and back on with nothing refused (`2-*-lists`, `2-*-ons`, `2y` droid Ion Blaster). But **a weapon taken off Config 2 isn't offered back in Config 2**: the Soldier's Short Sword and the Medic's Short Sword go to the bag, unequipped, and the Config 2 list then offers only "None" (`2x-*`). The Config 1 list does offer the same sword. Left-hand slots refuse a second weapon beside a two-handed or "incompatible" one, which is the correct pairing rule |
| 3 | Slicing and repair | **FAIL**: the Quartermaster works: "Three spikes and a part", and the bag shows "Security spike ×3" and "Repair part" (`3a`–`3c`). But (a) **the console still counts 0 spikes** ("slicing in costs 3 spikes … you have 0") until a save and reload (`3d`). (b) After the reload, slicing in **spends all 3 spikes**, so both **[Slicing]** replies show but are dimmed: "(3 spikes) — you have 0 spikes" (`3e`). (c) **The console has no [Repair] reply at all** (dialogue/console.toml has only the two [Slicing] replies). The only Repair offer I found is the right-click Repair on a droid |
| 4 | Motivator slot | **PASS** as far as testable: a droid's Equip draws a "Motivator" square where an organic has Boots (`4a`). Its list offers only "None", and the droid's kit has no boots (`4b`). The label wraps mid-word ("MOTIVATO / R") in the square. No motivator item is in any fixture or store, so "an organic can't fit a motivator" and equip/unequip/sell of one are untested |
| 5 | Quick regression | **PASS**: Auto Save row in play shows Kael's face (`5a`); zoom out stops with the room in view, in about 3× (`5b`); own-turn Switch Weapons ×3: free, then Action, then "you have spent your interaction and your Action" (`5c`, `5d`); party bar faces Off Tun + Kael (`5e`); boots off/on on every kit; Escape+F4 ×3: one quick.mark each |

## Notes (not failures)

- The Sith Warrior's robe reads "Robe 1" in Equip (TEST 172 showed "Dark Padawan Robe").
- A Soldier's Inventory lists the Config 2 Short Sword as "(Equipped)" while it's worn in Config 2. That's correct, but two weapons both show "(Equipped)".
- My chargen script no longer completes the Equipment step without a manual "Standard Gear" click, so each class was finished by hand (Tester-side).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
