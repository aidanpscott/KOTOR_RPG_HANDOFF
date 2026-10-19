# CODER-STATE — what a fresh Coder session needs; MAIN carries it into the project's Coder seed

**Made 2026-10-19 (MAIN, `PT-2752` ruling 6): there was no Coder seed file in the repos.** Kept short; update it when a standing rule changes.

## Running the tests

- **Test worktrees go BESIDE the main clone, in `KOTOR_APP_PROJECT`** (app 75b1eac). A worktree anywhere else cannot see the sibling packages (Lodestar, Lens, Shelf) by relative path: one ran 1997 of 4058 tests and stamped a false failure. `tool/test_tier.sh` now refuses before running or stamping (exit 4, "put test worktrees beside the main clone").
- `source tool/env.sh`, then every Flutter run goes through `tool/one_at_a_time.sh` (one Dart compile machine-wide). Tiers: `tool/test_tier.sh quick|core|archive|full`. Never `flutter run`.
- An app push needs a passing CORE stamp at HEAD. Read a commit's stamps with `python3 scripts/gate.py --at <hash>` (from MAIN_WORK). Report CORE's time and count every run.

## Pushing

- Shelf, Lodestar and Loom are unguarded. The app, MAIN_WORK and HANDOFF need the gate SENDABLE: commit, run `python3 scripts/gate.py` from MAIN_WORK, then push. Fetch and rebase MAIN_WORK and HANDOFF first (others push there); rerun the gate after a rebase.
- Mirror changed docs to `HANDOFF/docs` (only those that exist there), then `scripts/refresh_handoff_ledger.py` and `scripts/check_docs_mirror.py`. HANDOFF is text only.

## Data

- Documents → extractors (`scripts/extract_*.py`) → `data/extracted/*.json` → `scripts/gen_base_rules.py <scratch>` → diff → copy into `Shelf/base-rules`. Run `scripts/check_shelf.py` before confirming.
- `scripts/attacks.json` and `data/attacks.json` are twins (`audit_duplicates`): change both.
