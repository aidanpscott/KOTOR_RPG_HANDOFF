# STATE — every repository, branch and worktree, as found on disk

**REBUILT FROM FILES, 2026-11-20 (about 21:15), by CODER, on MAIN's order (`PT-2752`, 2026-11-20, "your handover note is stale").
Heads updated at the TEST 274 hash's push sitting, 2026-11-20 (about 22:00), at the next hash's, 2026-11-21 (about 08:00), the gen_feats hash's, 2026-11-21 (about 12:40), the Hardened Chassis hash's, 2026-11-21 (about 14:00), the asides hash's, 2026-11-21 (about 16:30), and the lines and droid tiers hash's, 2026-11-21 (about 19:20).**
The file before this one was last changed 2026-10-03 (HANDOFF b4f56a2) and is not trusted: nothing in it was carried over unchecked.
Every line below comes from `git` on this machine (fetched at the time of writing), the MAIN_WORK ledger (`playtest/PLAYTEST-RULINGS-01.md`,
PT-2752 entries from 2026-11-17 on), or a file named beside it. Rewritten in full each time, never appended.

## Heads — the shared clones in KOTOR_APP_PROJECT

All shared clones are clean and at their origin/main once this push sitting lands (app, MAIN_WORK, Shelf and HANDOFF pushed together).

| Repository | Shared head | origin/main | Notes |
|---|---|---|---|
| `KOTOR-RPG-APP` | `ee3a63b` | `ee3a63b` | the lines and droid tiers hash (on 6d12a75): _droidTierRows removed, the beds. FULL 6117 passed, 0 failed, 21m44s |
| `KOTOR_RPG_MAIN_WORK` | `1265c4fd` | `1265c4fd` | on Docs' e701d84e (row 22 corrected), itself on a0971724: the ruled lines, the earlier-by-class words and their PT-616 citation struck from four rows, the ledger lines |
| `Shelf` | `ab30306` | `ab30306` | on 485c89e: feats.toml, the ruled lines and the four droid tier rows (the folder is a symlink to ~/.local/share/kotor-rpg/packages) |
| `Lodestar` | `a554b93` | `a554b93` | |
| `Loom` | `9a1c3ef` | `9a1c3ef` | |
| `Lens` | `e449221` | `e449221` | |
| `Atlas` | `0b7cc47` | `0b7cc47` | |
| `HANDOFF` | this commit | `a9f1b67` before it | |

KOTOR-RPG-APP-owner (the owner's clone) is at fcf7d0c, 282 commits behind app origin/main and clean. It's the owner's, not CODER's, and was not touched.

## The lines and droid tiers hash — pushed in this sitting (accepted by MAIN, `PT-2752`, 2026-11-21)

- Master Killer's Instinct, Boresight and Integrated Toolkit carry MAIN's ruled lines in their effect; Personal Cloaking Shield's aside is corrected (MAIN_WORK 75e582c2; Shelf e45d08e). Bed: each on its pane, once (app ee3a63b).
- K2's droid tiers (the owner, 2026-11-21): every droid class gets plating and Droid Upgrade at 1, 7 and 13; PT-616's 4/9 and 5/11 rows are gone from the app (_droidTierRows, ee3a63b) and DROIDS-UPGRADE-01 (Docs, 304a1ab3). The four library rows lost "or earlier by class (PT-616)" (MAIN_WORK 75e582c2, 127f4b27; Shelf ab30306). Mutants 7 of 7 killed.
- The hash before it (app 6d12a75, Shelf 485c89e, HANDOFF a9f1b67) is accepted and pushed: the asides. Its MAIN_WORK head is a0971724, the same commits rebased onto Docs' 304a1ab3 at push time; this file named the pre-rebase 8933f49c until this sitting.

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

- The extractor's spacing (MAIN, 2026-11-21), its own small hash, next: collapse runs of spaces in every effect, regenerate, show the nine Shelf rows that change (whitespace only), and bed it.
- TEST 277 for Tester, after this push (MAIN, 2026-11-21).
- audit_source gets a test of its own (MAIN, 2026-11-21): a header without HAND-MAINTAINED fails, one saying "Generated by scripts/" fails. A later hash.
- The K2 session list: MAIN_WORK playtest/K2-SESSION-LIST.md, kept current by CODER (MAIN, 2026-11-21). Every K2-session item goes there.
- CODER's seed lives in the claude.ai project, not on this machine (MAIN, 2026-11-20). Its section 0 is the paste-block rule, logged under PT-2752.
