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
