# TEST 057 — two enemies confirmed, and a dead player still moves

**Built against:** `run-app.sh` / `run-loom.sh` (always rebuild). ⚠⚠ **The app moved
under me mid-session and I am correcting my own build declaration rather than
report against a stale one.** My relaunch produced PID `705138`, and its
`/proc/.../exe` mtime is `11:06:35` — **after** `KOTOR-RPG-APP` HEAD advanced to
`ee501ed` (*BUILD 125 — turn order on screen, and striking reveals you*, committed
`11:01:50`), not the `509f86e` (*PT-1678*) I expected going in. `strings … |
grep -c "PT-1422"` → 13, confirming the binary actually carries it. Loom tree/bundle
unchanged at `f3ba09d` (*PT-1678 — a square holds one way, and Loom refuses the
second*), PID `700935`. `pubspec.lock`'s `resolved-ref` for Lodestar is
`f1bf0de5f9d1f60b09240be25535056188272c7e`, cached and present at
`~/.pub-cache/git/Lodestar-f1bf0de5f9…`.

**Instrument:** PID-scoped via `run-app.sh`/`run-loom.sh`'s `exec`. App `705138`,
Loom `700935`; both killed by PID. Coder's Loom `517968` confirmed untouched
before and after.

**Task:** the new `two-enemies` fixture — walk into the first droid and confirm
the HUD's multi-combatant behaviour: all three join the roster (hidden one marked,
not absent); killing one leaves the fight running; the corpse-strikeable bug is
gone; the two droids don't attack each other. Also a quick, not-urgent confirm on
`PT-1681`'s Loom fix.

---

## 1. All three join the roster — confirmed, twice, with two different builds

Built two disposable characters (`Roster Tester`, then `Kill Tester`) and walked
each into `droid.probe-pair.01` at (1,0). Both times, the moment the fight opened:

    turn order          in this fight
    ▶/› probe-pair.03    20
      probe-pair.02      16
      probe-pair.01       8
      <player>          5–6

    lurker.probe-pair.03   24 of 24
    droid.probe-pair.02    24 of 24
    droid.probe-pair.01    24 of 24

**Confirmed: all three joined**, including the hidden lurker, matching
`_alsoInContact`'s one-hop contact-join. Board-side, the lurker at (1,1) was
correctly **absent** before combat (`t057-play.png`) and correctly **present**
once the fight opened — but not marked hidden by the time I could screenshot it,
in either fight. I traced this before assuming a defect, and it isn't one.

### ⚠ The concealed-in-roster frame — confirmed unreachable in THIS fixture, not a gap in my search

`BUILD 125`'s own note says why, and I confirmed it against the actual behaviour
rather than taking the note on faith: *"`_begin` runs the enemy turns itself when
the player loses initiative, the dice are seeded, and in the `two-enemies` bed a
droid wins — so the lurker strikes and reveals inside the same synchronous call
that starts the fight. There is no frame in that fixture where it is both in the
fight and concealed."* Both my characters lost initiative to the lurker (20 beats
5 and 6 every time — the dice are seeded, not merely unlucky twice), so the reveal
fires before Flutter ever paints a frame with the fight open. **I did not get to
see "hidden, not absent" on a living row in the roster** — I looked for it
specifically, twice, with two characters, and the fixture as built cannot show it.

**What I confirmed instead, on the identical code path**: `_concealed` unions
`_fallen` with the stealth-concealed set, so the SAME `hidden` flag the brief
asked about is exercisable on a dead row (§2 below) — and it renders exactly as
`roster_panel.dart` says it should. This is the same mechanism, observed from the
other side of it, not a substitute confirmation for a different one.

## 2. Killing one leaves the fight running, and the dead row persists exactly as promised

Built `Kill Tester` (STR 18, CON 17, Close Combat feat) specifically because
`Roster Tester` (all 13s, unarmed like every character in this build) could not
put a dent in a 24-vitality droid before dying first. With real damage output,
landed the killing blow on `droid.probe-pair.01`:

    unarmed · rolled 14 — d20 13 + attack 1 + Strength 4 · needed 13 —
    hit · damage 6 — 1d3 2 + Strength 4 · -1 left · character.died

**Confirmed, both halves of the ask:**

- **The fight did not end.** The panel stayed open, `lurker.probe-pair.03` and
  `droid.probe-pair.02` both still `24 of 24`, and combat continued for several
  more rounds afterward (I kept fighting to check §4). `standing.length <= 1` is
  false with two left standing — the `==0` case this fixture exists to rule out.
- **The dead row persists, marked, not vanished:**

      droid.probe-pair.01          hidden
      [dark, empty-coloured track]
      -1 of 24

  Amber `hidden` label, a track in the dead/empty colour rather than the teal
  fill the living rows use — exactly `_trackColour`'s "the track carries it when
  there is nothing left to fill," and exactly `_concealed`'s union of `_fallen`
  into the same set the lurker would have used. **One mechanism, two occasions to
  see it fire, and I caught it on this one.**

## 3. The corpse-strikeable bug — gone, and stronger than the brief's own phrasing

The brief: *"the body stays visible on the board for the rest of that round, then
clears at fight end."* ⚠ **That is not what I observed, and I want to say the
difference plainly rather than round it up to a match.** The corpse was gone from
the board in the **same frame** as the kill — no lingering token, not for the rest
of the round, not until fight end. This matches the source I read before testing
(`_theFallenLeaveTheBoard()` runs immediately after `_persistCrossing` inside
`_playerStrikes`, same tick as the kill), not the brief's description of the
timing. **The underlying ask — confirm the corpse-strikeable bug is actually gone
— is answered more strongly this way, not more weakly**: I walked the player
directly onto (1,0), the square droid.01 died on:

    a01-probe-pair · 1, 0        [move pips: 5 → 4, no attack roll, no combat log line]

Ordinary movement, not a strike. The square is fully vacated, not occupied by an
invisible corpse waiting to be hit again. **Confirmed gone, by direct
occupancy test, not just by the row looking right** — which is what the brief
specifically flagged as insufficient.

## 4. Two enemies do not attack each other — confirmed by absence

Across both fights (roughly nine enemy-turn cycles total), every attack roll
logged targeted the player. `lurker.probe-pair.03` and `droid.probe-pair.02`
finished at `24 of 24` in the second fight even after several rounds following
`droid.probe-pair.01`'s death — **not because they stood idle** (their turns
resolved every round; `droid.probe-pair.02` landed at least one hit on me, per
§6) but because neither ever appears as an attacker of the other in the log. No
allies-target-allies event observed anywhere in either fight.

---

## 5. ⚠⚠ Two of the brief's four "still open, not yours to chase" items are already closed

The brief named `hidden-after-striking` and `initiative order display` as open
and queued. **`BUILD 125` — the same commit my running binary is built from —
ships both**, landed between when the brief was written and when I sat down to
test it:

- **`hidden-after-striking`**: `_reveal(acting)` now fires whenever an enemy's
  turn returns a non-null result (a strike, hit or miss), which is precisely what
  I watched happen to the lurker in both fights.
- **`initiative order display`**: the `turn order` panel I quoted in §1 —
  `▶`/`›` markers, numbers, names — is `PT-1422`'s own new screen.

I am not treating this as something I need to re-verify from scratch — `BUILD
125`'s own report already carries `fight_test`/`roster_panel_test` coverage for
both (tie-break ordering, the strip not re-sorting, the reveal-on-miss case) and
my job is to use the product, not re-run a closed test. I'm flagging it because
the brief's premise was accurate when written and stopped being accurate before
I got to it — worth saying plainly (`PT-1617`'s pattern) rather than silently
treating the brief as still current. The remaining two — detection at range,
faction-aware hostility — are still open per `BUILD 125`'s own "not done" list,
and I did not touch either.

## 6. ⚠⚠ Found next to the task: a dead player keeps moving, and the fight never resolves

Not something I went looking for — `Roster Tester` (11 HP, unarmed, no real
damage output) died to the three-droid pack while I was chasing §1's hidden-frame
question. What happened afterward is worth having on record.

    vitality -5 of 11        [bar fully red]
    turn order: ▶ probe-pair.01   8
                  Roster Tester   6
    droid.probe-pair.02 holds — none:no-target

The fight did not end. One enemy (`droid.probe-pair.02`) explicitly **held for
lack of a target** — consistent with the dead player no longer being a legal
target — but the encounter itself stayed open, `probe-pair.01` sitting marked as
the current turn indefinitely. Pressing arrow keys **moved the dead player around
the board** — position updated in the status line (`a01-probe-pair · 0, 1`, then
`· 0, 4` after two more presses), with no attack, no interruption, and the move
counter never decremented despite four separate steps. This is not ordinary
turn-based movement continuing correctly; it reads as a fallback input path with
no combat gate, running because there is nothing else defined to happen. Escape
cleanly returned to the pause menu — no hard lock, `BUILD STATE.md`'s own ruling
that *"a fight can always be left, and never lost by leaving"* held exactly as
documented.

**I checked `HANDOFF/BUILD/STATE.md` before writing this up, and I am reporting
a symptom of a named gap, not a surprise bug**: its "Rulings that are Claude's,
flagged not made" table already lists — as of `BUILD 125`, unresolved —
*"`down → dead` in one blow — writes only `character.died`. The last of the six
had-to-behave-somehows."* This is that gap's first concrete failure mode I've
seen: with no ruling for what a player's own death should do to an in-progress
multi-combatant encounter, the encounter simply doesn't resolve, and the input
layer falls through to something that looks like free movement. **Confirming,
not fixing** — the ruling is explicitly not mine or Coder's to make.

## 7. `PT-1681` (Loom) — quick-confirm, and stronger than "refused at the tap"

Re-opened `tester-probe`, armed `doors → doorway`, clicked `door.probe-room.05`'s
occupied square at (5,2) — the exact case `TEST 056` left open. `TEST 056` got a
placement dialog offering a duplicate. This time:

    There is already a way on 5, 2 — door.probe-room.05. A square holds one:
    the board can only select the last one placed and the game only uses the
    first, so a second here would be a door you cannot reach and a door you
    cannot see. Clear the palette to select it, or pick another square.

**No dialog opened at all** — stronger than "refused at the tap" suggests, since
there is no `Place` button to even consider pressing. Confirmed no write:
`a01-probe-room.toml`'s mtime was unchanged (`~1.85h` older than the click), and
`grep`ing the file back shows exactly one `[[connections]]` block at `(5, 2)`,
byte-identical to `TEST 056`'s baseline. Problems count held at 17. ⚠ `PT-1681`
still isn't a real commit in either repo (`git log | grep -i 1681` empty in both)
— same pattern as the `PT-1668`/`1669` mismatch noted in `TEST 054`; the actual
fix is `PT-1678` in `Loom` (`f3ba09d`), unchanged since `TEST 056`.

---

## What I did not check

- The literal timing the brief described ("stays till round end, clears at fight
  end") — I found immediate same-tick clearing instead. Flagged as a phrasing
  mismatch against a stronger guarantee, not chased further.
- Detection at range, faction-aware hostility — named not-mine, untouched.
- `creatures`/`placeables` armed on an occupied square in Loom — still untested,
  carried over from `TEST 056`.
- Whether the dead-player-moves state ever self-resolves given enough enemy turns
  (e.g. all three eventually holding with no target) — I did not sit and wait it
  out; Escape was the exit I used, consistent with fleeing always being available.

## State

- **`two-enemies` unchanged** except its own play — no edits, never opened in
  Loom this session. Two new saves: `roster-tester.sav` (11:36), `kill-tester.sav`
  (11:46) — both deliberate, the fixture had none before.
- **`tester-probe` unchanged** — `a01-probe-room.toml`'s connection at (5,2)
  verified byte-identical to `TEST 056`'s baseline; 17 problems, same as before.
- `endar-spire`, `base-rules`, `taris-undercity`: not opened this session.
- The NWN install was not read or written.
- Both my processes killed by PID; Coder's Loom `517968` untouched throughout —
  checked before and after.
- `KOTOR-RPG-APP` HEAD is `ee501ed` (`BUILD 125`), not `509f86e` — landed mid-idle,
  reported per `PT-1617`'s rule rather than assumed away. `Loom` unchanged at
  `f3ba09d`.
