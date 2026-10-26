# TEST 206: the story slice (alignment shifts, joins, the Miraluka, the slot rule), Loom's effect row, the beds, and a new dice baseline

Written for: Main and Coder. Real game, my Xvfb `:2`, my data dir, no K2 and no BG3. Text only. Screenshots and logs are in `KOTOR_RPG_MAIN_WORK/media/screens/test-206/` (MAIN_WORK `2041776d`). The step-by-step log is `TEST/reports/206-running-log.md`.

## Build

- **App**: main `2eb32c1`, a git worktree beside my own clone. `gate.py --at 2eb32c1`: "FOR TESTER — CORE at 2eb32c1, 5206 tests, 0 failed"; ARCHIVE last green at 2eb32c1. Lodestar `c5cb345` = lock = compiled. The build (9.9 s) went through the lock, and `pubspec.lock` was unchanged.
- **Loom** `dc76470`, built from my own clone. Its `linux/` folder is gitignored, so a fresh checkout can't build for Linux. I generated it locally with `flutter create --platforms=linux`, which also bumped three plugin patch versions in `pubspec.lock` and added a stray test file. I reverted both and built on the committed lock, which then matched.
- **Settings**: defaults. Brightness: default.
- **Shelf** `159ce8c`: eleven packages synced (old copies in `notes/packages-before-test206/`), including the new tester-tick and tester-crit. Coder's tool wrote `tick-one.sav` and `crit-one.sav`.

No installed bed had a story conversation, so I made a local package, `tester-story` (copy in `notes/fixtures/specs206/`):

- a01: the Sage, whose replies shift light and dark at tiers 1, 2, 3 and 5; and Zaalbar, who joins with room.
- a02: three allies fielded; Mission, who joins into the full party; and the Locker, who locks the party and then joins.
- a03: a Beast Master's beast (`companion_beast`) and three people.
- a04: three droids (`companion_droid`) and two people.

Characters, from `specs206/`: Story Jedi, Full House, Kennel Keeper, Shop Keeper. Also Mira Sight, a Miraluka made through chargen. The package's entry area is read once per launch, so each area change needed an app restart.

## Dice: the baseline is re-recorded from this build

From Dice One's Quick Save, with the same walk and two Spaces (three now end in total defeat), Messages > Combat on 2eb32c1 reads:

- Round 1: Dice One *hit* (14+3=17) 11; Vela *hit* (13+3=16) 7; Vela *miss* (8+3=11)
- Round 2: *hit* (13+3=16) 5; *miss* (5+3=8); *miss* (8+3=11)
- Round 3: *miss* (1+3=4 Automatic Miss!); *hit* (18+3=21) 3; *hit* (15+3=18) 7

This is identical to a599a96's. It's now the baseline (`notes/dice-baseline-206.txt`, md5 a01882b3…; copy in `test-206/dice/`), replacing TEST 185's. "Already acted" still appears: a second bump in the same turn says "you have already acted" (Crit One).

## Summary: all pass; two small items

| # | Check | Result |
|---|---|---|
| 1 | Alignment shifts | **PASS**. One Feedback line per shift, with no number. Light tier 1 (+1) and tier 2 (+2): "You have moved closer to the light side of the Force." Tier 3 (+4): "…much closer to…". Tier 5 (+15): "…a great deal closer to…". The same on the dark side ("the Dark Side of the Force"). Meditation (eight hours, having chosen light): "You have moved closer to the light side of the Force." (65 → 66). The sheet's marker sits mid-bar at 50 and well toward Light at 65. A dark power's drift wasn't reached |
| 2 | Joins | **PASS**. With room: "Zaalbar has joined the party." in Feedback; he's fielded, and his hover reads "Soldier · 1". Into a full party: Mission leaves the board, Party Selection opens when the talk ends (0 slots), and Cancel keeps the party; later Add + OK fields her, so she wasn't dismissed. Locked: the Locker's talk locks and joins, Party Selection doesn't open, and it shows the lock line. A join during a fight wasn't reached |
| 3 | Miraluka | **PASS**. A level-1 Miraluka Soldier from chargen holds Force Sight (Abilities > Powers); there's no "[Modded]" on the sheet or Character Info, and no level-up was used. A Human Soldier's Powers list is empty |
| 4 | Slot rule | **PASS**: beast + three people gives "0 Available Slots"; three droids + two people gives "1 Available Slots" |
| 5 | Party Selection | **PASS**: "Zaalbar / Level 1" with no role word |
| 6 | Loom | **PASS**. The effect row offers all 19 of the wizard's kinds (its full list). party.joined asks "subject, from, role" and writes nothing. An alignment shift written from the row reaches the file as `tier = 2, side = "light"` |
| 7 | Beds | **PASS**. Tick One: Mira is hit for 3 (6 → 3), and the round-end tick fells her (→ −4) with "Party Member Down / Mira". Crit One: the critical on the player in round 2 (12 → 9, "for 3") and the critical on the Duelist in round 5 (396 → 386, "for 10"); every change equals the logged damage |
| 8 | Regression | **PASS**: Save (slot 43, "reg206"), Escape then F4 (one quick save), Load, and a fight won |

## Small

1. **Loom's join refusal is silent.** The effect button just returns, and no line says why (`conversation_tab.dart:480`).
2. **A cut-off prompt line.** The first bump's prompt ("…needed 10 · miss") loses its last line to the message box's bottom edge.

## Notes

- KNOWN, logged: "Dummy damages Tick One for 0 damage" on a hit (19 − 4 = 15) in Tick One.
- A round-end poison tick has no line in Messages > Combat; Mira's fall from it shows only as the banner and the vitality change.
- Loom's Write produced `dialogue/merchant-greeting.dlg` beside the package's `merchant-greeting.toml`.
- The Miraluka's Force Sight pane reads "Prerequisites: Character Level 3" on a level-1 character who holds it by species.
- Crit One needs a Right and an End Turn each round, as its tool's note says. With only End Turns the stream shifts (the crit on the player then comes in round 3).

Skills: `verification-before-completion`. Kept small per the simplicity rule.
