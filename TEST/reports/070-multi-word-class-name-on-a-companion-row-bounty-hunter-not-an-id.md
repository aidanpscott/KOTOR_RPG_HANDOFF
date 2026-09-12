# TEST 070 — PT-1810's fix confirmed live: a multi-word class
# ("Bounty Hunter") now reads correctly on a companion's sidebar row,
# not the raw blueprint id it used to carry

**Built against:** `run-app.sh` (always rebuilds). Local HEAD at build
time: `24ade3d` (09:28:29, *Pin to Lodestar 1e17025 -- PT-1123's
exploration catalogue*) — the tip of the branch at the moment I built, so
this includes `11d4783` (09:21:39, *PT-1810: a class reads the same on
every row -- and it was not casing*), the exact fix this task asked me to
confirm. `pubspec.lock`'s `lodestar` entry uses a floating `ref: main`;
its `resolved-ref` at my build was `3b7e03892664796b7649b42e9d2cf70c1f3eb6e6`
(not the `1e17025` short hash named in the pin commit's message — expected
for a floating ref, since `main` had moved again by the time my build's
own `pub get` ran) — confirmed present as an actual checkout at
`~/.pub-cache/git/Lodestar-3b7e03892664796b7649b42e9d2cf70c1f3eb6e6`.
`check_shelf.py` run first, per standing practice — despite the heads-up
about recent ranged-weapon corrections (Blaster Carbine threat range,
crit multipliers), it came back clean: `✓ 25 rules files, all identical
to what the extracts generate`. No re-ship needed.

App PID `133098`, killed by PID at the end, confirmed gone. Coder's Loom
(`12445`/`12443`) checked running, untouched, before and after.

---

## Multi-word class on a companion's row — CONFIRMED

TEST 069 found `Mate`'s row reading `soldier · 1` (lowercase) against the
player's `Soldier · 1`, and read it as a casing bug. PT-1810's own commit
message corrects that: it wasn't casing, it was two different *kinds* of
value — the player's row held the class's display name, a companion's
held the blueprint's class **id** — and they only looked like a casing
difference because every class tested so far happened to be one word,
where id-capitalized and true-display-name coincide by accident.
`bounty_hunter` capitalized is `Bounty_hunter`; the real display name is
`Bounty Hunter` — no capitalization of the id produces that, which is
exactly why this needed a multi-word class to catch.

Temporarily changed `companion-fixture`'s `mate.toml` from
`class = "soldier"` to `class = "bounty_hunter"` (a valid id — checked
`base-rules/rules/classes.toml`'s `[[classes]] id = "bounty_hunter" /
name = "Bounty Hunter"` — and reverted immediately after this test, back
to `soldier`, so the fixture is unchanged from prior sessions). Loaded
back into the existing "Sura Sarn" save from TEST 069 (Continue, not a
fresh chargen — this exercises the same live-resolution path either way,
since the sidebar reads the companion's *current* blueprint class id at
render time rather than anything baked into the save). Mate's row in
`a02-second-room`'s exploration sidebar read:

**`Mate` / `Bounty Hunter · 1` / `57 of 60`**

— the full two-word display name, correctly capitalized, matching
`classes.toml`'s `name` field exactly. Not `bounty_hunter`, not
`Bounty_hunter`, not `Bounty hunter` — confirming the fix resolves the id
through the real `classes` map (the same one `baseAttackAt` already used)
rather than string-transforming the id itself.

## An aside, not investigated further

The status bar under "Sura Sarn" (the player) read **"1 rule about this
character not checked"** — text I hadn't seen on this save in TEST 069.
Didn't chase it: this save's Sura Sarn still carries the pre-existing,
already-reported `equips items/weapons/blaster-rifle, which will not
open` gap from `companion-fixture` missing that item blueprint (visible
in the same status line, unchanged since TEST 069), and my own ad hoc
edit to Mate's class outside of chargen is exactly the kind of change
that could trip a validator not meant for hand-edited fixtures. Flagging
only so it isn't mistaken for something PT-1810 touched — not part of
this task's ask, not claimed as a finding.

## State

- `companion-fixture` (mine) — `mate.toml`'s `class` field was changed to
  `bounty_hunter` for this test and reverted to `soldier` immediately
  after; confirmed back to baseline. No other file touched.
- No other package touched — confirmed by mtime (only `companion-fixture`
  newer than `base-rules`, same five weapon-item blueprints and `mate.toml`
  as prior sessions).
- Reused the existing "Sura Sarn" save from TEST 069 rather than creating
  a new one — no new save artifact this session.
- App PID `133098` killed by PID, confirmed gone. Coder's Loom
  (`12445`/`12443`) checked running, untouched, before and after.
