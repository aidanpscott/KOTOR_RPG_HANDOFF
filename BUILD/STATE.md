# STATE — every repository, branch and worktree, as found on disk

**REBUILT FROM FILES, 2026-11-20 (about 21:15), by CODER, on MAIN's order (`PT-2752`, 2026-11-20, "your handover note is stale").
Heads updated at the TEST 274 hash's push sitting, 2026-11-20 (about 22:00), at the next hash's, 2026-11-21 (about 08:00), the gen_feats hash's, 2026-11-21 (about 12:40), the Hardened Chassis hash's, 2026-11-21 (about 14:00), the asides hash's, 2026-11-21 (about 16:30), the lines and droid tiers hash's, 2026-11-21 (about 19:20), the spacing and Navigation lock hashes', 2026-11-22, and the TEST 278 hash's, 2026-11-23.**
The file before this one was last changed 2026-10-03 (HANDOFF b4f56a2) and is not trusted: nothing in it was carried over unchecked.
Every line below comes from `git` on this machine (fetched at the time of writing), the MAIN_WORK ledger (`playtest/PLAYTEST-RULINGS-01.md`,
PT-2752 entries from 2026-11-17 on), or a file named beside it. Rewritten in full each time, never appended.

## Heads — the shared clones in KOTOR_APP_PROJECT

All shared clones are clean and at their origin/main once this push sitting lands (app, MAIN_WORK, Shelf and HANDOFF pushed together).

| Repository | Shared head | origin/main | Notes |
|---|---|---|---|
| `KOTOR-RPG-APP` | `b63ea9c` | `b63ea9c` | the TEST 278 hash (on a5a2cfd): Equipment gives the item outright where the aptitude is closed, no note on the Upbringing pane, the granted list after a reset. FULL 6126 passed, 0 failed, 22m08s |
| `KOTOR_RPG_MAIN_WORK` | `f64283b2` | `f64283b2` | on Tester's f4c89265 (TEST 278 media): the ledger lines for TEST 278 and its rulings (b3df66e1, f64283b2) |
| `Shelf` | `b9bc862` | `b9bc862` | unchanged in this sitting: 7cb3965 (nine effects and ten notes lose a double space), b9bc862 (Droid Upgrade 4 granted, the Navigation lock) (the folder is a symlink to ~/.local/share/kotor-rpg/packages) |
| `Lodestar` | `a554b93` | `a554b93` | |
| `Loom` | `9a1c3ef` | `9a1c3ef` | |
| `Lens` | `e449221` | `e449221` | |
| `Atlas` | `0b7cc47` | `0b7cc47` | |
| `HANDOFF` | this commit | `db9e91c` before it | |

KOTOR-RPG-APP-owner (the owner's clone) is at fcf7d0c, 282 commits behind app origin/main and clean. It's the owner's, not CODER's, and was not touched.

## The TEST 278 hash — pushed in this sitting (accepted by MAIN, `PT-2752`, 2026-11-23)

- Equipment gives a bonus item outright where its aptitude is closed to the body, with no "Aptitude: —" row; the Upbringing pane draws no note (the only unfiltered note on any screen); a reset makes the Feats granted list show again (app b63ea9c). Mutants 4 of 4 killed.
- The two hashes before it (app a5a2cfd, MAIN_WORK 8523893a, Shelf b9bc862, HANDOFF 054bcbd) are pushed: the spacing and the Navigation lock.

## Two hashes — pushed 2026-11-22 (accepted by MAIN, `PT-2752`)

- The spacing hash: every feat effect is written with single spaces (MAIN_WORK 3eb1eaf2 with its gate test; Shelf 7cb3965; app 14e0f3b). A programming's aptitude is offered only where the chassis holds the skill, and the Feats help box comes before the granted list (app 5b2642d).
- The Navigation lock hash: Droid Upgrade 4 is granted only, by no class; the Navigation Droid is locked to the Astromech (PROGRAMMINGS-01 §1a), and every §1a lock is now applied on the Background page (it was read and never applied); a droid's level-up hub has no Homeworld or Upbringing row (MAIN_WORK 7720b671; Shelf b9bc862; app 01a9775, a5a2cfd). K2-SESSION-LIST.md item 11.
- The hash before them (app ee3a63b, MAIN_WORK 1265c4fd, Shelf ab30306, HANDOFF d720d15) is pushed: the lines and droid tiers.
- The first sitting for the spacing hash (2026-11-22) was refused by audit_paths on Tester's og277.py; the trees went back to origin until Tester's f319ca38.

## Every worktree under ~/.cache/kotor-coder (a symlink to /mnt/games2/ai-work/kotor-coder)

Nothing was discarded or pruned.

| Worktree | Repository | Branch | Last commit | Ahead / behind origin | Uncommitted |
|---|---|---|---|---|---|
| app-t272 | app | coder-t275 | ee3a63b 11-21 | 0 / 0 (pushed) | none |
| app-arrows | app | coder-arrows | bdbf45d 11-19 14:43 | 0 / 12 (merged) | none |
| app-icons | app | coder-icons | 0e383ee 11-19 19:23 | 0 / 10 (merged) | none |
| app-t271 | app | coder-t271 | fb449fe 11-19 17:33 | 0 / 11 (merged) | none |
| mainwork | MAIN_WORK | coder-wip | 1265c4fd 11-21 | 0 / 0 (pushed) | none |
| xdg/kotor-rpg/packages | Shelf | coder-wip | ab30306 11-21 | 0 / 0 (pushed) | none |
| loom-warn | Loom | coder-warn | 9a1c3ef 11-18 22:07 | 0 / 0 (merged) | none |
| t263-state/a | a throwaway clone of Atlas (the "behind origin" bed) | main | 4636ddb 11-18 07:34 "t" | 1 / 0 against its local origin | none |
| wt-111-merge | the-uninvited (not KOTOR) | detached | b0f493f 11-19 11:42 | on origin/feature/SCRUM-111-terminal-ui | build-config.log (untracked) |

Also in the folder, not git: full-*.log (FULL stamps), gate-*.txt, m27x*.json (mutant lists), mut/ (the mutant runner), and the probe, worldscale and biomeshot scratch folders.
Elsewhere: Lodestar's worktree list still names a prunable coder-wip worktree in the old session's /tmp scratchpad (1b24e7e). Lodestar's coder-wip branch is fully on origin/main. The worktree entry was left, not pruned.
Other local branches, all old and not CODER's current work: app backup/pre-reinstall-local-2026-10-01 (45 ahead), app rescue/pc-2026-09-28 (1), HANDOFF rescue/pc-2026-09-28 (1), MAIN_WORK in-game-batch-4 (1).

## DEFERRED (`PT-1608`)

The old file's deferral table (HANDOFF b4f56a2:BUILD/STATE.md) was not carried over: it is from 2026-10-03 and was not checked against the ledger.
These are open now:

- TEST 279 for Tester, after this push (MAIN, 2026-11-23).
- Recommended for Attributes and Skills (the owner, 2026-11-23): rules/recommended.toml per class (spread and ranked skills) from K2's rows, the documents, or derived with its reasoning; the table goes to MAIN before wiring to recommend.dart.
- Momentum's line (MAIN, 2026-11-23): "Another kill while it lasts doesn't raise it past +1." The next hash.
- Upbringing descriptions (the owner, 2026-11-23): Docs drafts, the owner approves, then into the upbringing rows (CODER).
- The double spaces that reach the screen (MAIN, 2026-11-23): with Evasion's note and the Salvage line; skip class_arrays.toml weapon (its colour separator); check the 16 item descriptions against K2's dialog.tlk.
- audit_source gets a test of its own (MAIN, 2026-11-21): a header without HAND-MAINTAINED fails, one saying "Generated by scripts/" fails. A later hash.
- The K2 session list: MAIN_WORK playtest/K2-SESSION-LIST.md, kept current by CODER (MAIN, 2026-11-21). Every K2-session item goes there.
- CODER's seed lives in the claude.ai project, not on this machine (MAIN, 2026-11-20). Its section 0 is the paste-block rule, logged under PT-2752.
