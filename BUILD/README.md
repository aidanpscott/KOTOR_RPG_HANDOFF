# BUILD — what shipped, for a reader who cannot see the code repositories

**⚠ Four of the five product repositories are invisible to the owner's token.**
`Lodestar`, `Lens`, `Loom` and `KOTOR-RPG-APP` are private and unreadable from
here; `base-rules` is not a repository at all, it is a package folder on a
shelf. So a build slice can run, pass and push and **leave no trace anywhere the
owner can look.**

That happened five times in seven reports before this directory existed.

> **⚠ STANDING: every build slice writes a report here, in the same act as the
> push.** Same habit `STUDY/` already has for studies, applied to builds. A
> report that only exists in a chat message is a report that can be lost.

---

## Read this first

| File | What it is |
|---|---|
| **`STATE.md`** | ⚠ **The current state of every repository and package.** Always rewritten, never appended — it answers "what exists right now". |
| `NN-name.md` | One slice, as it was reported. Appended, never rewritten. |

---

## The slices

| | Slice | Repo | Head |
|---|---|---|---|
| `00a` | [The Lens split — why a fourth package exists](00a-lens-split.md) | `Lens` | `d532c0a` |
| `00b` | [The extraction batches — and the limit that matters most](00b-extraction-batches.md) | `MAIN_WORK` | `869e13a` |
| `00c` | [`base-rules` — audit trail versus rule](00c-base-rules.md) | shelf | — |
| `01` | [Chargen step 2 — the hub opens](01-chargen-hub.md) | `KOTOR-RPG-APP` | `592ec4b` |
| `50` | [`PT-1464` — the bar at the class step, the notes out of the cells](50-the-bar-at-the-class-step.md) | app · `MAIN_WORK` | `edaf92d` |
| `49` | [`extract_feats.py`, and what the disambiguation leaves](49-extract-feats.md) | `MAIN_WORK` | `890db53` |
| `48` | [Data nothing examined — the sweep, and two corrections](48-data-nothing-examined.md) | `MAIN_WORK` | `a46f6e9` |
| `47` | [`PT-1461` — the Builder refuses, the bed answers, and the field was there](47-the-builder-refuses.md) | `Loom` · app · `MAIN_WORK` | `5571dd7` |
| `46` | [Three slices — the droid loads, the wire is connected, `PT-1459`](46-three-slices.md) | all three | `4eb7d28` |
| `45` | [`PT-1458`, and two diagnoses before any fixing](45-the-droid-and-two-diagnoses.md) | `Lodestar` · app | `d95ad2c` |
| `44` | [`PT-1453` — more than one, and the class underneath it](44-more-than-one.md) | `Lodestar` · `Loom` · app | `a42f9b3` |
| `43` | [`PT-1452` — the item blueprint, and the trooper fires its rifle](43-the-item-blueprint.md) | all four | `1407b4e` |
| `42` | [⚠ STOP — the equipped weapon cannot be read](42-the-equipment-stop.md) | none — nothing built | — |
| `41` | [The runner faked a pass, and the wound survives a quit](41-the-runner-and-the-wound.md) | `KOTOR-RPG-APP` | `4f8a242` |
| `40` | [`PT-1447` — the side panel, and the room doubles](40-the-side-panel.md) | `KOTOR-RPG-APP` | `f924efb` |
| `39` | [The other half of the sandbox, and the `Tester` protocol](39-the-other-half-of-the-sandbox.md) | `Loom` | `b2308e1` |
| `38` | [`PT-1445`, and the suite stops writing to real data](38-the-id-and-the-sandbox.md) | `KOTOR-RPG-APP` | `3d97d52` |
| `37` | [The tree moves to the Steam library](37-the-move.md) | all six | `14b02f5` |
| `36` | [On the machine, and runnable](36-on-the-machine.md) | — | — |
| `35` | [The doctrine format, and a check instead of an errand](35-the-doctrine-format.md) | `Lodestar` · `Loom` | `f7fe50d` · `387fcf1` |
| `34` | [Four of the five closed, one stop, and a sixth found](34-four-of-five.md) | `Loom` | — |
| `33` | [The audit, and Loom authors a conversation](33-the-audit-and-the-create-path.md) | `Loom` · app | — |
| `32` | [The viewport pass — `§7` re-derived](32-the-viewport-pass.md) | app · `Lens` | `04e4061` |
| `31` | [A fight from a conversation, and the Builder's editor](31-a-fight-and-an-editor.md) | `Loom` · app | — |
| `30` | [The dialogue screen](30-the-dialogue-screen.md) | `KOTOR-RPG-APP` | — |
| `29` | [`PT-1434` measured, and the dialogue runtime](29-npc-continuation-and-the-runtime.md) | `Lodestar` | — |
| `28` | [The empty `say` refused, and the converter folds](28-refuse-the-empty-say-and-fold.md) | `Lodestar` | — |
| `27` | [The dialogue reader, and a real `.dlg` converted](27-the-dialogue-reader.md) | `Lodestar` | — |
| `26` | [`PLAY-STATE-01` — the second projection](26-play-state-the-second-projection.md) | `Lodestar` · app | — |
| `25` | [The enemy takes a turn](25-the-enemy-takes-a-turn.md) | `KOTOR-RPG-APP` | `e8fba9b` |
| `24` | [A creature in the bed, and the seam reachable](24-a-creature-in-the-bed.md) | `Loom` · app | `9d06456` |
| `23` | [Three rulings, and the seam](23-rulings-and-the-seam.md) | `Lodestar` · app | `ae4a87f` · `3edf2b7` |
| `22` | [Combat slice 4 — enemy decisions](22-combat-slice-4.md) | `Lodestar` | `44b8eb9` |
| `21` | [Combat slice 3 — the round](21-combat-slice-3.md) | `Lodestar` | `16b5593` |
| `20` | [Combat slice 2 — the check fix, pools and damage](20-combat-slice-2.md) | `Lodestar` · app | `8c281e8` · `508f741` |
| `19` | [Combat slice 1 — `resolve()` and one attack](19-combat-slice-1.md) | `Lodestar` | `442b600` |
| `18` | [The two checks — emitted, declared, handled](18-vocabulary-checks.md) | all three | `3d0be11` · `d08c2f` · `5510cbf` |
| `17` | [Ledger batch 3 — Continue and Load Game light up](17-ledger-batch-3.md) | app · `Lodestar` | `d1a2c05` · `fc4fb3` |
| `16` | [Ledger batch 2 — to disk and back](16-ledger-batch-2.md) | `Lodestar` · app | `244fce8` · `d3a46f` |
| `15` | [Ledger batch 1 — events and replay](15-ledger-batch-1.md) | `Lodestar` · app | `172963b` · `e9483fb` |
| `14` | [Identity — the last step, and what Play owes](14-identity-and-what-play-owes.md) | `KOTOR-RPG-APP` | `fd48d5c` |
| `13` | [Batch 6, and Equipment — `PT-1200` resolves](13-batch6-and-equipment.md) | both | `c85a9c4` · `c827da5` |
| `12` | [Import, the import question answered, and the Equipment stop](12-import-and-the-equipment-stop.md) | `KOTOR-RPG-APP` | `251fb66` |
| `11` | [`PT-1407`, the attack gap surveyed, and Powers](11-pt1407-and-powers.md) | both | `73b5324` · `43f2840` |
| `10` | [Batch 5a, three rulings, and the Sith stop searched](10-batch5a-and-the-sith-stop.md) | both | `a271f73` · `45a58a1` |
| `09` | [Batch 5, a droid completes Skills, and Feats](09-droid-skills-and-feats.md) | both | `61d05ea` · `81ab9ec` |
| `08` | [The droid Abilities close, and Skills](08-skills.md) | both | `4ffbe26` · `8668390` |
| `07` | [Backstory collapses, and Abilities](07-abilities.md) | `KOTOR-RPG-APP` | `b1e57ae` |
| `06` | [Backstory, and the re-lock warning](06-backstory.md) | `KOTOR-RPG-APP` | `7db8fa5` |
| `05` | [Two fixes, and what the stale citations said](05-open-01-and-the-check.md) | `MAIN_WORK` | — |
| `04` | [check_decisions.py — the boundary nothing watched](04-check-decisions.md) | `MAIN_WORK` | — |
| `03` | [Reconciling the two decision records](03-decision-records.md) | recon | — |
| `02` | [The world menus exported, and Origin completes](02-worlds-and-origin.md) | both | `e5d68ab` · `addeb81` |

**⚠ The `00` slices are BACKFILLED** — three where someone reading the code would
ask *why* and find nothing. **Deliberately not everything:** a backfill that
reconstructs every slice is a second history, and the ruling record already holds
the decisions.

## Reconnaissance

| File | What it is |
|---|---|
| [`RECON-worlds.md`](RECON-worlds.md) | ⚠ Where the world roster and its menus actually are, and why the Origin stop is not a staging fix |
