# STATE — every repository, branch and worktree, as found on disk

**REBUILT FROM FILES, 2026-11-20 (about 21:15), by CODER, on MAIN's order (`PT-2752`, 2026-11-20, "your handover note is stale").
Heads updated at the TEST 274 hash's push sitting, 2026-11-20 (about 22:00).**
The file before this one was last changed 2026-10-03 (HANDOFF b4f56a2) and is not trusted: nothing in it was carried over unchecked.
Every line below comes from `git` on this machine (fetched at the time of writing), the MAIN_WORK ledger (`playtest/PLAYTEST-RULINGS-01.md`,
PT-2752 entries from 2026-11-17 on), or a file named beside it. Rewritten in full each time, never appended.

## Heads — the shared clones in KOTOR_APP_PROJECT

All shared clones are clean and at their origin/main once this push sitting lands (app, MAIN_WORK, Shelf and HANDOFF pushed together).

| Repository | Shared head | origin/main | Notes |
|---|---|---|---|
| `KOTOR-RPG-APP` | `c5b65a3` | `c5b65a3` | the TEST 274 hash (on the 1c hash 6aaa63e): 8e85567, 86bd3cb, c9c058d, c5b65a3. FULL 6103 passed, 0 failed, 22m07s |
| `KOTOR_RPG_MAIN_WORK` | `747ad21f` | `747ad21f` | 11 commits on 6efe93f0: the rulings' rows, the ledger lines, and the gate's app-root fix |
| `Shelf` | `af7a8e1` | `af7a8e1` | 3 commits on d4caf41: df17d58, dc6c04a, af7a8e1 (the folder is a symlink to ~/.local/share/kotor-rpg/packages) |
| `Lodestar` | `a554b93` | `a554b93` | |
| `Loom` | `9a1c3ef` | `9a1c3ef` | |
| `Lens` | `e449221` | `e449221` | |
| `Atlas` | `0b7cc47` | `0b7cc47` | |
| `HANDOFF` | this commit | `0f2e6e2` before it | |

KOTOR-RPG-APP-owner (the owner's clone) is at fcf7d0c, 282 commits behind app origin/main and clean. It's the owner's, not CODER's, and was not touched.

## The TEST 274 hash — pushed in this sitting

CODER's three branches (app `coder-t274` in ~/.cache/kotor-coder/app-t272, MAIN_WORK `coder-wip` in ~/.cache/kotor-coder/mainwork,
Shelf `coder-wip` in ~/.cache/kotor-coder/xdg/kotor-rpg/packages) were fast-forwarded into the shared trees, gated there with
PUSH_SITTING=1, and pushed. Each branch is now level with origin/main; nothing is unpushed.

- FULL at c5b65a3: 6103 passed, 0 failed, 22m07s, -j 3, peak 2278 MB, run 2026-11-20 20:43. The FULL before it, at c9c058d, failed 1 (species_equip_test); c5b65a3 is that test's change.
- A gate run from the private worktree reads DO NOT SEND by location alone: two icon checks resolve the mods folder only from the shared MAIN_WORK, and two shelf checks read the shared Shelf. The verdict that counts is the shared-tree gate.
- 747ad21f: gate.py now hands its generators (KOTOR_APP_ROOT) the app checkout whose HEAD is the hash it gates, or a folder that does not exist, so gen_icons_to_create.py refuses rather than rewrite ICONS-TO-CREATE.md from the shared clone. Bed scripts/test_app_tree.py, in the gate; 5 of 5 mutants killed; end-to-end control: with the wiring removed, `gate.py --at c5b65a3` from the worktree rewrites ICONS-TO-CREATE.md again.
- 7d083c5f (MAIN_WORK, "Hardened Chassis says organics cannot take this chain…", 06:05) is on no branch. git range-diff shows it identical to ceeb359f, its rebased copy on coder-wip (08:12). Superseded; nothing lost.
- df17d58 (Shelf, the same Hardened Chassis change) is on Shelf coder-wip.

## The next hash against the ledger

From MAIN's three 2026-11-20 rulings after the 1c acceptance:

- HARDENED CHASSIS 1, line 196 matches the JSON: done (FEATS-LIBRARY-01:196, MAIN_WORK ceeb359f, Shelf df17d58).
- HARDENED CHASSIS 2 and 3: answered by the feats_core ruling (option A); check_feat_text_gates passes in the gate.
- FEATS_CORE OPTION A, audit_skillfeats reads the extract: done (3637e5a6).
- FEATS_CORE OPTION A, a header on feats_core.json saying its text columns are not maintained and not to be cited: NOT DONE. The file (and its twin scripts/feats_core.json) is still a bare JSON array; its last change is S15c. A header inside the array would break audit_sheets, audit_featsplit and audit_featsync, which load it as a list.
- PT-616 "or earlier by class" on Droid Upgrade 2 and 3 and Plating Proficiency: Medium and Heavy: present (lines 93, 94, 186, 187).
- PT-577 "Closed to Astromech and Remote" on Droid Upgrade 3: present (line 187). The ladder-cap bed: app 8e85567.
- PT-621 Empathy's Protocol line: present (line 493). App 8e85567 "pins Empathy's unreachable premise"; what that premise is needs reading from the test before it's reported.
- TEST 274's 1, a level-gated chain red with its level: 86bd3cb.
- TEST 274's 2, Plating Proficiency: Light's "Droids only" as data: 86bd3cb, c9c058d, c5b65a3, MAIN_WORK 7e0d1e01, Shelf af7a8e1. MAIN's question about PT-1462 and the row's placement: no answer found in any file.
- TEST 274's 3, the 1-2 px border at 1920: 86bd3cb names the designation refusal clearing Random Name; its pixel bed needs confirming.
- TEST 274's 4, droid Bounty Hunters holding organic-armour proficiencies: no source lines found in any file. Open.
- TEST 274's 5, "Closed to Astromech" on Improved Close Combat: 86bd3cb ("every red cell gives its reason").
- TEST 274's 6, Skill Focus's real reason: the mutant list m274b.json names "the pane drops Skill Focus's reason", so a reason is drawn; the reason itself needs stating in the report.
- TEST 274's 7, a portrait per chassis: 86bd3cb; the Battle droid is on ICONS-TO-CREATE (7e0d1e01).
- MUTANTS for TEST 274: ~/.cache/kotor-coder/m274b.json lists them (08:25, before c5b65a3). No result file was found. They must be run (or their results found) before the hash is reported.

## Every worktree under ~/.cache/kotor-coder (a symlink to /mnt/games2/ai-work/kotor-coder)

Nothing was discarded or pruned.

| Worktree | Repository | Branch | Last commit | Ahead / behind origin | Uncommitted |
|---|---|---|---|---|---|
| app-t272 | app | coder-t274 | c5b65a3 11-20 09:16 | 0 / 0 (pushed) | none |
| app-arrows | app | coder-arrows | bdbf45d 11-19 14:43 | 0 / 6 (merged) | none |
| app-icons | app | coder-icons | 0e383ee 11-19 19:23 | 0 / 4 (merged) | none |
| app-t271 | app | coder-t271 | fb449fe 11-19 17:33 | 0 / 5 (merged) | none |
| mainwork | MAIN_WORK | coder-wip | 747ad21f 11-20 | 0 / 0 (pushed) | none |
| xdg/kotor-rpg/packages | Shelf | coder-wip | af7a8e1 11-20 08:26 | 0 / 0 (pushed) | none |
| loom-warn | Loom | coder-warn | 9a1c3ef 11-18 22:07 | 0 / 0 (merged) | none |
| t263-state/a | a throwaway clone of Atlas (the "behind origin" bed) | main | 4636ddb 11-18 07:34 "t" | 1 / 0 against its local origin | none |
| wt-111-merge | the-uninvited (not KOTOR) | detached | b0f493f 11-19 11:42 | on origin/feature/SCRUM-111-terminal-ui | build-config.log (untracked) |

Also in the folder, not git: full-*.log (FULL stamps), gate-*.txt, m27x*.json (mutant lists), mut/ (the mutant runner), and the probe, worldscale and biomeshot scratch folders.
Elsewhere: Lodestar's worktree list still names a prunable coder-wip worktree in the old session's /tmp scratchpad (1b24e7e). Lodestar's coder-wip branch is fully on origin/main. The worktree entry was left, not pruned.
Other local branches, all old and not CODER's current work: app backup/pre-reinstall-local-2026-10-01 (45 ahead), app rescue/pc-2026-09-28 (1), HANDOFF rescue/pc-2026-09-28 (1), MAIN_WORK in-game-batch-4 (1).

## DEFERRED (`PT-1608`)

The old file's deferral table (HANDOFF b4f56a2:BUILD/STATE.md) was not carried over: it is from 2026-10-03 and was not checked against the ledger.
These are open now:

- The feats_core.json header (above): not in the TEST 274 hash. It goes to MAIN as a question (the file is a bare array that three audits load as a list).
- The TEST 274 mutants (above): to run on c5b65a3 and report.
- TEST 274's PT-1462 placement question and the droid Bounty Hunter source lines (above): to research and report.
- CODER's seed lives in the claude.ai project, not on this machine (MAIN, 2026-11-20). Its section 0 is the paste-block rule, logged under PT-2752.
