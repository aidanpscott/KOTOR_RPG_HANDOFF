# KOTOR-RPG-APP — OLD → NEW COMMIT HASHES (PT-2722, 2026-10-02)

**Why this file exists.** On 2026-10-02 the private `KOTOR-RPG-APP` history was rewritten with `git filter-repo` to purge two Bank Gothic paths (`assets/fonts/BankGothicMediumBT.ttf`, `assets/fonts/BANKGOTHIC-NOTES.md`) from every commit, then force-pushed (owner-approved). Every commit that touched or followed those paths got a new hash. **The ledger, agenda and `STATE.md` are history and are NOT rewritten: an app hash cited there before this date is the OLD hash — look it up here. Use the new hash from now on.** The six other repos were not rewritten.

- **Result:** old head `ca16ef4331af1b17f4e9a3192c92144a1ae5fef0` → new head `60898dc6b1f59cd3c6994da320665e6d28edda92`. The tree is byte-identical (`99bf00bd6ce154e4969bc09f140839f0f8de3e80` before and after).
- **631 commits in the map; 69 changed hash, 562 are unchanged** (everything before the first Bank Gothic commit, plus the `rescue/pc-2026-09-28` branch, whose head `8b7411d` is unchanged).
- Source: `.git/filter-repo/commit-map` from the rewrite. Subjects are from the new commits.

| old | new | subject |
|---|---|---|
| `00f0a3b14e42` | `79047c315d91` | PT-2716: an equipped Equip-screen cell shows its own slot glyph, not the item's name as te |
| `01294e0f8f2b` | `f2f1a88e73b9` | PT-2713 (3): disarming a mine spending Computer Spikes — not reproduced |
| `03ba4e805fda` | `9ca1724d3e4e` | Grey out what chargen cannot deliver, with the real reason — PT-2710 (9) |
| `043087a59aeb` | `7949cde747ea` | Store and Terminal borders frame outward; the footer labels show -- PT-2708 (9) |
| `075df96a2e59` | `f2e0d150767b` | PT-2716: migrate three test fixtures off the retired Soldier RCR ladder |
| `0da942e3c9c7` | `5f046aa32c63` | PT-2721: tool/env.sh, versioned, aware of the host and the flatpak sandbox |
| `106950c8c236` | `1421f48d8754` | PT-2722 D4: never render an item's developer note to a player |
| `15669f540319` | `fcf3731e239f` | A dismissed henchman is out of the party, the fight and the XP split -- PT-2708 (7) |
| `1c0fc5c98803` | `49e5658dbb55` | run.sh without env.sh; machine-bound tests read Locations or skip loudly -- PT-2707 |
| `1c2de7b20110` | `67fe92a5e266` | PT-2711 (3): route the two real id-collision feats and the three availability-fixed feats  |
| `1ea24a0e876c` | `3fb2057058dd` | PT-2713 (4): mine tier table proven at all three real Frag Mine models |
| `294bd5303906` | `0ac159edae55` | PT-2711 (6): root-cause whole_loop_test.dart's flake, skip the test it lives in |
| `2d8a76f11baa` | `822be35f3f1f` | PT-2718: bump Lodestar to df81340 (Juggernaut/Droid Master corrected) |
| `2de7b5f3c7c8` | `01e2afb6ec42` | PT-2721: the item list reads names, draws item art, and shows K2's none-glyph |
| `383e68a3d620` | `17d8273d5e5b` | One-fold Defence across all three readers -- PT-2710 (12), reopening PT-2688/PT-2705 |
| `5041e30cd4c8` | `918dc49638ad` | PT-2720: the suite is green at the cause; the off-hand reads agree |
| `51af2cd5919c` | `03a5fba18901` | PT-2721: the portrait block, and the menu screens drop the play view's chrome |
| `551a9b849599` | `93853213504f` | On main: pre-freeze working tree from /mnt/ga, 2026-10-01 |
| `5705d4167de9` | `8d869bdcad77` | PT-2721: the size guard - the list and description boxes are fixed, and scroll inside |
| `5b92aba04475` | `7cf2706c59fa` | PT-2718: fix the dex-18 fight-start bug at its real cause |
| `5cc3d551927a` | `6c0e23c200dd` | Test: read endar-spire from the sandbox's shelf, not /home/aidan |
| `606491307492` | `b91631f8048d` | PT-2713 (5): Auto Level Up never silently skips a choice, the interim guard |
| `631063e6d920` | `83e1cff198e2` | PT-2722 fix 1(a): items built from a starting blueprint are named by their catalogue row a |
| `64ea0e41e7e3` | `4f71ae9c03e5` | PT-2722: the Equip screen draws in K2's two faces - Bank Gothic for the UI, Liberation San |
| `64ec66fa3fa7` | `3410415e41e4` | PT-2721: a capture test for K2's own font sample |
| `652e7f5dd6d5` | `25de3c0f4077` | index on main: 3410415 PT-2721: a capture test for K2's own font sample |
| `69aa5712ac11` | `3e19f77d949b` | PT-2717: bump Lodestar to bef3b0a, one-fold Defence test for 3 newly-wired classes |
| `6aaea1699aab` | `368448e524c4` | PT-2721: the Equip screen is on BankGothic Md BT; the atlas renderer is retired |
| `6bf511f2e0a5` | `f5544fcf9bd1` | The dice stream resumes from the log's own position -- PT-2710 (2) |
| `70193e439a59` | `abea491c4e41` | PT-2721: the HANDOFF guard fails on writes, not on a read |
| `7545695c5b32` | `11b7973fb96b` | PT-2721 partial: fixed boxes, chrome art, top-bar icons |
| `758dada11356` | `287f58fb534f` | untracked files on main: 3410415 PT-2721: a capture test for K2's own font sample |
| `7d63a406b3e4` | `f8005c523a5c` | PT-2721: whole_loop_test's Load Game case loses a real fight, on its own shelf |
| `7e5bf8885be0` | `5033e17909bc` | Starting inventory arrives: every array item, kit, medpac and grant; the second weapon --  |
| `8264e41d29dc` | `36002948deb5` | Equipping, built: free out of combat, refused in combat, the pairing rule -- PT-2708 (3) |
| `89c79e285e84` | `fcc6657b1fd7` | Whose event is it: one convention, and the player keeps their kills -- PT-2708 (1)(2) |
| `9d7479ff235a` | `e84f7982cff5` | PT-2722: D3 and D6 candidates - K2's fonts by use, and a correction to PT-2721 |
| `a1279d94aa3c` | `22eb377f3960` | PT-2722: capture tool for the Bank Gothic replacement candidates |
| `a136e3e53038` | `0f6bea1c44bd` | PARKED, needs Main's pick: a new game begins on a declared start -- PT-2708 (10c) |
| `a54fca2b0757` | `8920f9abc14b` | Build the Credits route in chargen — PT-2710 (5), PT-1217/PT-728 |
| `af55038deb78` | `2c4cdac49293` | Granted feats are shown as granted: the sheet marks each feat's source, Level Up names the |
| `b0a17a97edd0` | `c0697a9a0830` | Homeworld and species skill bonuses stack -- PT-931, SKILLS-01 §10.0, PT-2710 (4) |
| `b18bb08020b6` | `00bb41c0d88c` | PT-2711 (5): enemy and companion parity for §7 dual-wield and unarmed strikes |
| `b34f45b9fc17` | `d8300908572b` | The turn order says names; level-up Skills and Feats state the level's own arithmetic -- P |
| `b901794243e6` | `9008a6990c06` | Player-side granted feats on level-up, both routes -- PT-2710 (1) |
| `bf4ebabe7e45` | `b895194e122d` | PT-2717: recalibrate the Force Body fixture's DEX past the new class term |
| `c03909fef6f5` | `9db4c08655ac` | PT-2721: un-skip whole_loop_test's Load Game case by forcing the death in the log |
| `c7ef0d107544` | `f0f1445cd340` | PT-2721: Equip opens on Body when Body is worn; the matched-gear character for the loop |
| `c85719e4fca3` | `afec7ebba278` | Mines set at their own tier; starting consumables usable; one item resolver; companion she |
| `c93efe3f81ba` | `6fb230e1dd78` | PT-2721: the top bar has K2's eight icons, in K2's order; Map is drawn and disabled |
| `ca16ef4331af` | `60898dc6b1f5` | PT-2722: the Equip UI face is Orbitron (SIL OFL 1.1), Bank Gothic removed |
| `cb82d15cd437` | `54071707e2c3` | The level-up skill cap label reads the real cap, not a stale "cap 4" — PT-2710 (7) |
| `cea9da2f76bc` | `8dea527b73a4` | PT-2717: raise the distraction fixture's DC past the trooper's Will save cap |
| `cf157a44d1a8` | `cf34366fc25d` | PT-2722 fix 1(b): no menu screen draws the play view's status row |
| `cf443c1556af` | `f0305993ab68` | PT-2719: off-hand readout proven correct; the real K2 font, drawn |
| `d213d18e04b0` | `cf1230971ea8` | tool/author_tester_purse_save.dart: the tester-purse player -- PT-2708 (12) |
| `d246521c88c6` | `a7921de9d916` | PT-2722: word gap set from K2's space glyph, separate from letter-spacing |
| `d6306e8aa484` | `b64f981bd161` | PT-2712 (1): fix Equip's DEF badge, the third Defence reader missing classBonus |
| `d92eb087906b` | `858e0e8c5b67` | Regression guard: a companion keeps its side across a door — PT-2710 (6) |
| `dc98ec3f5f86` | `e065aad3185e` | PT-2721: two tests that failed for reasons outside the code under test |
| `de4f77e3654a` | `699b25e91dbe` | The attack line says whether a threat was confirmed; Lodestar pin ec6c30e -- PT-2709 (2) |
| `e10ecbcf66b8` | `02ebc45b11fe` | Skill checks add the key ability everywhere; criticals multiply the whole blow -- PT-2708  |
| `e78076a28df1` | `0d09392f9a28` | Minor batch — PT-2710 (8): stack counts, the readout plate, initiative names, the feats fo |
| `e85d9c524c72` | `4cc9e54d6b18` | PT-2713 (2): the Credits route now prices all 19 base classes, not 6 |
| `e8f72bf4b3f7` | `9270cc1c5f25` | Slicing and Security spend spikes per SKILL-RESOLUTION-01 §5 -- PT-2710 (3) |
| `eb992da08c3f` | `246a0d0affc8` | PT-2713 (1): a companion keeps its ally ring across a door |
| `ee11c6262ba4` | `f44d707c27d3` | PT-2721: a test run can no longer dirty the public repo |
| `f232b6c14bc4` | `b89c21950242` | Switch Weapons: the two configurations trade places, as ACTION-ECONOMY-01 §5's free intera |
| `f74aeb7f15ac` | `22d1d6f15b26` | Pin the walk-scripted tests to the old corner; the start rule is on main -- PT-2709 (1) |
