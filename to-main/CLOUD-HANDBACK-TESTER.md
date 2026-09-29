# CLOUD HANDBACK — TESTER (2026-09-29)

The cloud Tester ran from 2026-09-29 to hand-back and filed TEST 142 and TEST 144. This note holds
everything that lived only in that container.

## Repo heads at hand-back

| repo | `main` head | what the cloud Tester did there |
|---|---|---|
| `KOTOR_RPG_HANDOFF` | the commit carrying this note (on top of `8c0fbef`) | TEST 142, TEST 144, `TEST/fixtures/*`, `BUILD/screens/test-142/`, `BUILD/screens/test-144/`, this note |
| `KOTOR-RPG-APP` | `b34f45b` (read only; TEST 144 built from it) | nothing committed |
| `Shelf` | `be87ee9` (read only) | nothing committed; Coder committed my fixtures |
| `KOTOR_RPG_MAIN_WORK` | `69e1634` (read only) | nothing committed |
| `Lodestar` / `Lens` | `7b6c97f` / `2bad745` (the lock's pins, read only) | nothing committed |

**`cloud-wip-*` branches:** none, because nothing was left unfinished.

**One stale branch:** `KOTOR_RPG_HANDOFF` `claude/stoic-mccarthy-ti193p` still exists on the remote.
- Everything on it is on `main`: TEST 142 is `08ca96e`, the fixtures and addendum are `ac96c69`.
- The session's git proxy drops branch deletions ("remote end hung up") every time, and the GitHub tools
  have no delete call.
- **Aaron: please delete it by hand.**

## Where I stopped

TEST 144 is filed (`fe29eed`, then this hand-back). **Nothing is mid-flight.** The last live state was
characters in a throwaway data directory; they matter only as the evidence already in the report.

**Still open from TEST 144, all for Main to route:**
1. **FAILED:** a player Brawler at L2 never receives `unarmed_specialist_i`, on either Auto or manual
   Level Up.
   - The manual summary promises it ("feat — Unarmed Specialist I, granted by Brawler").
   - A companion's level-up does write grants.
   - Not traced in code. My guess, unverified: the PT-2708 subject convention in the player's branch of
     `_commitLevelUp` / `_newlyGrantedFeats`, or the Auto path (`_autoLevelFromSheet`) never calling the
     grant step. Compare the two paths against Mate's.
2. **Boots (`a_boots_01`) and Sparring Gloves (`a_gloves_00`) never arrive.**
   - The save says "the catalogue gives it no base type".
   - It's likely a base-rules/catalogue gap, not app code. Check `items.toml` for a `base` on those resrefs.
3. **Every unlock attempt spends a spike.** With a 2-spike kit, one failed roll leaves the terminal
   unusable. Is that a rule question?
4. **Persuade adds Cha but not the origin's "Persuade +2"** (SKILLS-01 §10.0 says homeworld bonuses stack).
5. **Minor:**
   - Inventory has no stack counts.
   - A dark inset sits across the Store readout's Credits/In Stock rows.
   - The initiative status line still shows the tag `dummy.room.02`.
   - At level 2 the skill rows say "cap 4".
   - The level-up Feats footer says "0 feats are granted" while the summary lists two.
   - After a door, Mate is drawn like an enemy token.
   - The attack footer text collides with the character name.

## Things not written down anywhere else

**Environment (cloud):**
- **Flutter** is at `/opt/flutter`, and the Linux toolchain, Xvfb, xdotool and ImageMagick are present.
- **Git deps resolved without trouble**, so `dependency_overrides` was never needed. `flutter create
  --platforms=linux .` is needed on every `git archive` snapshot because `linux/` is gitignored.
- **No rsync.** Seed a data directory with `git -C shelf archive HEAD | tar -x -C <dir>/packages`.
- **The rm guard:** the harness refuses `rm -rf $VAR` when the variable could be HOME. Use `mktemp -d` and
  literal paths.
- **Skills:**
  - `claude plugins install mattpocock-skills` fails because no marketplace is configured. Working lines:
    `claude plugin marketplace add mattpocock/skills` and
    `claude plugin install mattpocock-skills@mattpocock`.
  - Superpowers' `verification-before-completion` is copied alone into `~/.claude/skills/` from commit
    `8ca22db`. The Superpowers plugin is NOT installed, because its SessionStart hook injects the
    whole-workflow skill.

**Driving the app under Xvfb (the window is 1280×720 at 0,0):**
- **Input:** position with `xdotool mousemove --window <wid> X Y`, then `click`/`key` without `--window`.
  This worked for every input in both passes. The helper I used:

  ```bash
  export DISPLAY=:2
  W=$(xdotool search --name '^kotor_rpg_app$' | head -1)
  # click:  xdotool mousemove --window $W X Y; xdotool click 1     (right-click: click 3)
  # key:    xdotool mousemove --window $W 5 5; xdotool key <Key>
  # shot:   import -window root -crop 1280x720+0+0 +repage out.png
  ```
- **Library:** one horizontal wheel click (button 7) moves roughly 53 px, and card order is alphabetical,
  so scroll, screenshot, then click. The Load Game list's clickable part is the **name text**; a click to
  its right misses.
- **Options** (Esc) has a different layout with a party, and again in combat: Leave Session sits at y≈398
  with a party, 378 solo, and 350 in combat, with the confirm button beside it. `q` typed into an open
  conversation goes into its text box, so close dialogue first.
- **Sheets:**
  - A companion's sheet opens by **right-clicking its sidebar row twice**: the first makes it active, the
    second opens the sheet.
  - On the player's sheet, **Auto Level Up sits directly above Level Up**. I hit Auto by accident once.
- **Fights:** the trooper in Endar Spire opens with a natural 20 more often than not (the first d20 of a
  session was 20 in most runs). An 8-HP character dies before acting, so use `tester-xp-bed-arena` for
  anything that needs several rounds.

**Save decoding** (the `.sav` is a `KRSV` header plus a gzip of JSON lines, one event per line):

```python
import sys, zlib
b = open(sys.argv[1], 'rb').read()
print(zlib.decompressobj(31).decompress(b[b.find(b'\x1f\x8b'):]).decode())
```

**Validating a fixture without the app:** make a scratch pub project with
`dependencies: lodestar: path: ~/.pub-cache/git/Lodestar-<sha>`, then call `open(dir)` →
`validatePackage(pkg)`, plus `openConversation` and `openStore` for dialogue and stores. I mutation-checked
it: it reports a short map row and a missing blueprint. Without the base-rules inputs (`weaponSections`
and the rest), four checks are disabled.

**Fixtures:** all four packages are in `HANDOFF/TEST/fixtures/`, and the README says what each is for. The
new `tester-xp-bed-arena` is not on the Shelf yet. Coder should commit it next to `tester-xp-bed`.

**Nothing is left only in the container.** The data directories (`~/tester-data*`) held only throwaway
characters and the arena fixture, and the arena is now in HANDOFF.
