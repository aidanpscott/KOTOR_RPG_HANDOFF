# TEST 178 — the TEST 177 fixes, motivators in play, boots Defence, droid speed and the implant names

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 or BG3 launched. Text only; screenshots in `KOTOR_RPG_MAIN_WORK/media/screens/test-178/` (MAIN_WORK `8e146bce`). Read first: Coder's TEST 177 fixes and motivator entries.

## Build

App `42cc86c262e4a8922799c6c0f097de80f4f06d58` (git archive, lock unchanged after build). Lodestar `c6f4db0ce7184e8148caec28fe4dda7900070f24` = lock. Lens `bfc9bff8daeac99c39da6a38283f41dd1551faa2` = lock. Loom: the app's lock has no Loom entry. Shelf `83b5bec` (my data dir). `tool/env.sh` sourced. check_shelf clean (31 rules, 114 blueprints). Fresh fixtures.

**Machine notes (Tester side):** the OS is now Ubuntu 26.04. `libgtk-3-dev` was missing; the owner installed it. GTK then aborted on a GNOME xsettings schema key, so I run `xsettingsd` on `:2` with a private schema dir. My shell now carries `WAYLAND_DISPLAY`, and the first launch opened on the owner's desktop; I killed it by PID and now launch with `GDK_BACKEND=x11`, without `WAYLAND_DISPLAY`. None of this is an app fault.

## Summary: six pass, two partial, one not reachable

| # | Check | Result |
|---|---|---|
| 1 | Config 2 | **PASS**: Soldier: Config 2 Short Sword off, then offered back and on; Config 1 Blaster Rifle off and back on (`1a`, `1b`). Medic: same with Short Sword / Hold Out Blaster (`1c`, `1d`). While the sword is worn in Config 2, the Config 1 list offers only the rifle |
| 2 | Spikes and repair | **PASS**: Quartermaster "Four spikes and a part" (`2a`). The console opens free and reads Spikes 4 at once, with no reload (`2b`). "[Slicing] Cycle the corridor lights. (1 spike)" spent 1 (`2c`). Reopened free at Spikes 3; "[Slicing] Unseal the vault door. (3 spikes)" spent 3 (`2d`). Damaged Power Panel: "Repair (Repair)" opens "[Repair] Reroute the power coupling. (1 part)"; picked, "1 part spent"; reopened, it shows dimmed "— you have 0 parts" (`2e`–`2g`) |
| 3 | Turn lines | **PASS**: on Kael's turn: "switching weapons — it is Kael's turn; wait for your own" (`3a`). On an enemy's turn, a slot pick: "putting your weapon away — it is Sentry Droid's turn; wait for your own" (`3b`). The Switch Weapons button on an enemy's turn wasn't caught: each droid's 4 s turn ended before my clicks, and its attack line overwrote mine |
| 4 | Names | **PASS** with a note: the Sith Warrior's robe reads **"Jedi Robe"**, not "Robe 1" (`4b`); TEST 172 showed "Dark Padawan Robe" for a Sith Warrior, so check which is ruled. Soldier and Marksman starting items read their own names, with no lost apostrophes ("Dockworker's Treads") (`4a`, `4d`). The Marksman Rifle comes off and goes back on (`4c`). No "Training Blade" item exists in base-rules, so I couldn't check that example |
| 5 | Motivators | **PASS** except rough ground: Quick-Fix stocks Treaded (75) and Silenced (400) Motivators (`5a`). The droid bought both (`5d`). "MOTIVATOR" fits on one line (`5e`). The droid's Motivator list offers both motivators but not its Dockworker's Treads (`5f`). An organic Medic who bought a Treaded Motivator sees only the Treads in Boots (`5b`, `5c`). Silenced: Stealth Bonus 0 → +2, total 2 (`5g`, `5h`). Treaded: an Astromech moves **3** instead of 4 (`5i`). **Rough ground: not reached** (below). The refusals are "not offered" rather than a line, because neither list contains the other kind |
| 6 | Droid speed | **PASS** (speed); **rough ground not reached**: Astromech 4, Assassin 5, Battle 5, Remote 6 squares on its own turn (`6a`–`6d`). The Remote crossing rough ground free wasn't checked (below) |
| 7 | Boots Defence | **NOT REACHABLE**: no fixture or store holds Sith Trooper, Mandalorian, Krath or Vanguard boots (grep of every package; none stock them) |
| 8 | Implants | **PARTIAL**: items read Cybernetic Implant, Advanced Cybernetic Implant and Master Cybernetic Implant (`8a`). Each pane's "Feats Required" names its own tier (`8b`). Abilities > Feats shows "Cybernetic Implantation", with "Surgical grounding for cybernetic hardware… Allows Cybernetic Implants." (`8e`). My fixture held only the first tier, so the Advanced and Master feat entries weren't seen. The Cybernetic Implant equips (`8d`). An Advanced one is refused with K2's generic line, **"You cannot equip this item. You don't have the prerequisites. Please see the item description."** (`8c`). The pane names the feat; the refusal line itself does not |
| 9 | Quick regression | **PASS**: Auto Save row in play shows Kael's face (`9a`); boots off/on (`9b`); own-turn Switch Weapons: free, then Action, then "you have spent your interaction and your Action" (`9c`, `9d`); party bar faces (`9e`); Escape+F4 ×3, one quick.mark each |

## Not reached

- **Rough ground (items 5 and 6):** the only difficult squares in any fixture are in Tester Probe's Probe Yard (a03). A save authored there still starts in the probe package's first room (the save's area header doesn't place the player), behind a room of probe creatures. A small room with difficult squares beside the arrival would make this testable.
- **Boots Defence (item 7):** no source for those boots.

## Notes (not failures)

- The Auto Save row in play shows Kael, but its time reads 21:09:35 yesterday, while the Quick Save from minutes ago reads the same. The faces are refreshed; the time may not be.
- The Marksman Rifle and the Cybernetic Implantation feat draw no icon (empty cell).
- My fixtures (in the snapshot only): `tool/tester_author_droidbuyer.dart` (Bolt Buyer, astromech Engineer in Store Bed, 1000 credits, Treads in bag); `tool/tester_author_chassis.dart` (env CHASSIS/SEED/NAME/CARRY/BOOTS/GENDER, droids in Precognition Ambush; Assassin and Battle need GENDER); `tool/tester_author_implant.dart` (Ivy Plant, Store Bed, Cybernetic Implantation, three implant items); `tool/tester_author_probe.dart`. I also copied the two motivator blueprints into my local precognition-ambush package for the chassis fixtures.
- For TEST 179 (four-way movement): none of my routes here used a diagonal step; I move with arrow keys only.

Skills: `verification-before-completion`. Kept small per the simplicity rule.
