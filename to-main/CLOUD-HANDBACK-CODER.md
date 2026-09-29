# CLOUD-HANDBACK-CODER — the cloud Coder hands back to the PC

Written 2026-09-29 by the cloud Coder, on Main's wrap-up order. No PT filed.
**Nothing is left only in the cloud container**: every repo below is clean,
has no stash, and has no commit missing from `origin/main`.

## 1. `main` head in every repo I touched

| Repo | `main` head |
|---|---|
| KOTOR-RPG-APP | `c85719e` Mines set at their own tier; starting consumables usable; one item resolver; companion sheets; a dice seed per campaign — PT-2709 (3)(5)(6)(8)(9) |
| Shelf | `c9f64b6` base-rules regenerated: mines carry their tier (set_dc), Marksman/Sniper Rifle carry the rifle wield class, Scavenger's grant is Components compont_00001 — PT-2709 (3)(6)(7) |
| Lodestar | `d0741c8` One item resolver: the starting-weapon check looks where play looks — PT-2709 (5) |
| Loom | `1d1fa74` Verify passes base-rules as the item fallback; Lodestar pin d0741c8 — PT-2709 (5) |
| KOTOR_RPG_MAIN_WORK | `01773f3` Agenda: PT-2709 progress — items 1–10 done, 11 in the report, 12 next |
| KOTOR_RPG_HANDOFF | this note's commit (after `8c0fbef` Mirror the agenda: PT-2709 progress) |
| Lens | `2bad745` — untouched by me this session beyond its tests |

KOTOR_RPG_Library and kotor-engine were cloned but never touched.

**Pins at hand-back:** the app's `pubspec.lock` resolves Lodestar to
`d0741c8`; Loom's resolves Lodestar to `d0741c8`.

## 2. `cloud-wip-*` branches

**None.** Nothing was mid-change at the wrap-up order: PT-2709 items 1–11 are on
`main`, verified (app 1818 pass, 2 loud skips; Lodestar 1862; Loom 430; analyzer
app 89 / Loom 41 / Lodestar 3 / Lens 0, 0 errors — the PT-2707 baseline).

⚠ **Stale session branches the owner must delete by hand:**
`claude/zen-wright-89pbv4` on **KOTOR-RPG-APP, Shelf, Loom, KOTOR_RPG_MAIN_WORK**.
PT-2709 item 1 ordered them deleted; the cloud's git proxy refuses branch
deletion (HTTP 403, policy). Every change on them is on `main` (checked by
reverse-applying each branch's own patch onto `main`). They hold superseded WIP
only. The old coder's `rescue/pc-2026-09-28` branches (app `8b7411d`, HANDOFF,
Shelf) are untouched and still to be folded — see §3.

## 3. Where I stopped

**PT-2709 is done through item 11. Item 12 was not started:**
- the rest of PT-2707 — the `linux/` proposal and the setup-script text (both
  answered in §5 and §6 below, as Main asked);
- then the PT-2705 list (7 items), with the old coder's rescue branch folded
  into its item 1. The app rescue commit `8b7411d` (9 files) carries a
  `defence_agrees_across_screens_test.dart`, a second-weapon change that
  OVERLAPS mine (`ledger_writer.dart`, `starting_weapon.dart` — the second
  weapon is now in Config 2 by PT-2709 item 4) and `tool/author_test142_save.dart`.
  Fold it by hand; do not merge it blind.

The full PT-2709 report (items, commits, flags, owner proposals) was given to
Main in the session; its substance is in `CODING-AGENDA-01`'s PT-2709
PROGRESS line and repeated in §4 so nothing depends on the chat.

## 4. Things known that are not written down elsewhere

### Owner questions / proposals still open (PT-2709 item 11 — nothing built)
- **Boots:** all 25 `ITEMS-08` pairs ARE in the catalogue; authored rows have no
  `baseitems` row, so no base type makes them items. Proposal: a `boots`
  worn-slot base modelled on `belt` (slot `boots`, no numbers of its own).
- **Sparring Gloves** `a_gloves_00` → base `gauntlets` (hands).
- **Glow Rod, Recording Rod** → a carried inert base, or drop from the kits.
- **Armorply Plating Mark I** `u_a_over_02`, **Components** `compont_00001` →
  carried inert upgrade/material bases until workbench crafting exists.
- **Tier-1 saber upgrade:** PT-755 already names three (Deflection Emitter
  `u_l_emit_01`, Synthesized Kunda Lens `u_l_lens_01`, Discharge Energy Cell
  `u_l_cell_01`), chosen or rolled — the array row should name them. Initiate:
  the same three or a (chosen) colour crystal. Augmented: determined (PT-716).
  Dancer: determined, else chosen.
- **Reload-and-retry dice (PT-2709 item 9):** the stream restarts from the
  campaign seed every time the play screen opens, so a reload replays the same
  rolls for the same moves. Unchanged; the owner's call.

### Flags raised, not ruled
- Mine **notice** DC is set to the tier (SKILL-RESOLUTION-01 §2.1 states none).
- `ITEMS-06`: Deadly Gas Mine save **DC 30**, Devastating Gas **DC 100** — used as stated.
- K2-only STRONG / DEVASTATING mines take K2's own `setdc` (20/30); STRONG ties AVERAGE at 20.
- Set mines cannot be recovered (a set mine carries no `recovers`).
- Catalogue warts: "Components  UNIQUE" (a ⚠ UNIQUE marker leaked into the
  name); `u_l_cell_01` catalogued `ranged-cell` though `u_l_` is lightsaber.
- `droidHoldsMelee` (Lodestar `package_validate.dart`) still looks up equipment
  in the story package only — the same "second formula" shape item 5 fixed for
  the starting-weapon check, not asked about, left alone.
- Store's `_StoreRule` divider sits half a texel above its y since the tpc.py
  flip (4px); not the footer defect, not changed.
- Equip's Switch Weapons button is below the fold in combat (tests use
  `ensureVisible`).

### The tests: things that will bite
- **Seeded-stream tests.** Many board tests depend on the play screen's dice
  stream (seed 1). Anything that adds or removes a d20 (the confirmation roll
  did) moves them; PT-2709 item 2's commit shows how each was re-read, and each
  says why. Tests that play through real chargen pass `App(campaignSeed: 1, …)`
  — that IS the old stream; without it chargen draws a random seed and those
  tests become non-deterministic.
- **Start square.** New games start on the one declared arrival. Tests that
  script moves from (0,0) pass `startAt: const Point(0, 0)` or, when driving the
  whole app, call `pinStartAtCorner(where, package, area)` (test/sandbox.dart).
- **Fast triage:** temporarily set `pumpUntil`'s default timeout
  (test/sandbox.dart) from 60s to 8s, run the suite, then run the same files
  with the change under test switched off — anything failing only with it on is
  real. **Restore 60s** before a real run.
- Full app suite ≈ 11 minutes; test runs rewrite `HANDOFF/BUILD/screens/*.png`
  through the `HANDOFF` symlink — revert them (`git checkout BUILD/screens`)
  before committing HANDOFF.

### Environment gotchas (cloud)
- Set `XDG_DATA_HOME` before every test run (`$HOME/coder-data`); the app adds
  `kotor-rpg/`. Without it Lodestar tests fail with "base-rules is not installed".
- After changing the Shelf, reseed the data dir's copy of that package.
- `pkill -f <pattern>` kills its own shell (exit 144); kill by PID or `pkill -x`.
- Background tasks die on a container restart; the working tree survives.
- The git proxy **refuses remote branch deletion** (403) — don't retry it.
- Force-with-lease against this proxy needs the explicit form
  (`--force-with-lease=<branch>:<sha>`); the bare form reports stale info.
- MAIN_WORK's extractors need **python3.12** (`python3` is 3.11).
  `extract_starting_equipment.py` and `extract_item_effects.py` write only when
  given the destination path as an argument; `extract_equipment.py` writes by
  default.
- xdotool under Xvfb: move with `--window`, click without it.

## 5. PT-2707 — the `linux/` proposal

**Keep `linux/` ignored; generate it, don't commit it. Recommendation below.**

What the cloud session established:
- `linux/` (with `android/ ios/ macos/ windows/`) has been in the app's
  `.gitignore` since the repo's first commit (`a70de67`, 2026-09-06, "README,
  gitignore, licence placeholder" — "no scaffolding"). It has never been committed.
- What `flutter create --platforms=linux .` generates here is the **stock
  template, unmodified**: `BINARY_NAME kotor_rpg_app`, `APPLICATION_ID
  com.example.kotor_rpg_app`, a GTK runner at 1280×720. Nothing in it is ours.
- Regenerating it costs one command and touches two tracked files
  (`.metadata`, `test/widget_test.dart`), which must be reverted afterwards.

**Proposal:** keep the ignore rule. Add one line to the README / setup: *"the
desktop runner is generated: `flutter create --platforms=linux .` then
`git checkout -- .metadata test/widget_test.dart`"* — done in the setup script
below. **Commit `linux/` only on the day we change it** (a real application id,
window title, icon, or size); from then on it is ours and belongs in the repo,
and the ignore line comes out in the same commit.

## 6. PT-2707 — the final setup-script text (if the cloud is needed again)

```bash
#!/usr/bin/env bash
# KOTOR RPG — cloud container setup for Coder / Tester.
# Repos are cloned by the environment into /home/user:
#   kotor-rpg-app shelf Lodestar Lens Loom kotor_rpg_main_work KOTOR_RPG_HANDOFF
set -euo pipefail
cd /home/user

# 1. Tooling (skip what the image already has). Flutter 3.47.5 / Dart 3.13.4.
sudo apt-get update -qq
sudo apt-get install -y -qq clang cmake ninja-build pkg-config libgtk-3-dev \
  xvfb xdotool python3.12
# (Flutter itself: install to /usr/local/flutter if `flutter` is missing.)

# 2. The data directory the app reads packages from — tests need it too.
echo 'export XDG_DATA_HOME=$HOME/coder-data' >> ~/.bashrc
export XDG_DATA_HOME=$HOME/coder-data
mkdir -p "$XDG_DATA_HOME/kotor-rpg/packages"
for p in /home/user/shelf/*/; do
  [ -f "$p/package.toml" ] && cp -r "$p" "$XDG_DATA_HOME/kotor-rpg/packages/"
done

# 3. The HANDOFF symlink the screenshot-writing tests expect.
ln -sfn /home/user/KOTOR_RPG_HANDOFF /home/user/HANDOFF

# 4. Dependencies. Lodestar and Lens are private git deps — the proxy fetches them.
(cd Lodestar && dart pub get)
(cd Lens && flutter pub get)
(cd Loom && flutter pub get)
(cd kotor-rpg-app && flutter pub get)

# 5. The generated desktop runner (PT-2707 §5: ignored, never committed).
(cd kotor-rpg-app && flutter create --platforms=linux . >/dev/null \
  && git checkout -- .metadata test/widget_test.dart)

# 6. Skills (user level only — never into a KOTOR repo without the owner's OK):
#    Matt Pocock's skills via the plugin marketplace, plus superpowers'
#    `verification-before-completion` copied alone into ~/.claude/skills.
#    Do NOT install the Superpowers plugin; do NOT run /setup-matt-pocock-skills
#    in a KOTOR repo.

echo "ready — remember: XDG_DATA_HOME, python3.12 for extractors, revert HANDOFF/BUILD/screens after tests"
```

Every Coder change from this session is on `main` in the repos above.
