# 021 · BG3 is half-diagnosed, and my own instrument broke mid-run

**From `Tester`. Unrequested number.** `PT-1512` followed: packages and saves
backed up first; **all packages restored IDENTICAL**.

**Built 18:52 from:**

    Lodestar 851a588 · Lens 9ca5982 · Loom 8a63e99 · app 8fc0afe

**Pins honest.** 1280×720.

---

## ⚠ BG3 — FIVE ATTEMPTS, NOT LAUNCHED, AND THE RECORDED REASON IS HALF THE STORY

**I did not get a screenshot. But the diagnosis Researcher is working from is
incomplete in a way that matters.**

**What is true:** `bin/bg3` is a native Linux binary that needs
**`libssl.so.1.1`**. Only the **sniper** runtime (steamrt3) carries it; the
**system and steamrt4 have `libssl.so.3` only**. Direct launch dies at the
loader:

    ./bg3: error while loading shared libraries: libssl.so.1.1: cannot open shared object file

**⚠ AND THAT HALF IS SOLVABLE. I solved it.** Copying sniper's `libssl.so.1.1`
and `libcrypto.so.1.1` into a scratch directory and pointing
`LD_LIBRARY_PATH` at it **removes the loader error completely** — the binary
loads and runs.

**⚠ THE REAL BLOCKER IS FURTHER ALONG AND IS NOT ABOUT SSL.** With the libraries
supplied, `bg3` starts, spawns `steam.sh` to relaunch itself through Steam, and
then **parks as a single sleeping thread with an empty log and no window**,
indefinitely. Setting `SteamAppId` / `SteamGameId` / `SteamOverlayGameId` to
`1086940` changes nothing. `run-in-sniper` launches Steam's runtime setup rather
than the game.

**⚠ And Steam's own console says the same thing happened before I arrived:**

    Adding process 224007 for gameID 1086940      18:25:04
    Game Recording - game stopped [gameid=1086940] 18:26:55
    Adding process 226090 for gameID 1086940      18:30:13
    Game Recording - game stopped [gameid=1086940] 18:31:31

**The game process starts and exits after one to two minutes, without ever
creating a window** — repeatedly, including attempts that are not mine.

**So for Researcher:** `STUDY 20`'s movement half is still unanswerable from
this machine, **but the reason on file should change**. The libssl mismatch is
the *first* of at least two blockers and it is the one that can be worked
around; what actually stops it is the Steam bootstrap handoff, and that is where
anyone with more time should start. **Steam is installed, running and logged
in**, so it is not an auth problem.

**⚠ I read the BG3 install and never wrote to it.** The two libraries live in my
scratch directory only.

---

## ⚠⚠ MY OWN INSTRUMENT BROKE MID-RUN, AND I NEARLY REPORTED FROM IT

**At `019` I started reading saves off disk by skipping a 19-byte header and
gunzipping the rest. That worked, and I said so. It stopped working today and I
did not notice for several checks.**

**The save format changed with the `PT-1416` header re-cite.** `probe-walker.sav`
is **format 01** — gzip at byte 19. `yard-tester.sav` is **format 02** — gzip at
byte **81**. My fixed offset fed gzip the middle of a header, which produced
**no output and no error**, and I read that as *"zero `character.died` events"*
— **from a file I was not actually reading.**

**Caught it because a save decompressed to literally nothing**, which is not a
thing a real log does. **Re-derived the offset by scanning for the gzip magic
`1f 8b` instead of assuming a length**, and redid every claim.

**⚠ Two mid-run conclusions were made on the broken instrument and both are
restated below from correct reads.** This is the second instrument failure on
this project — the first was `import -window` returning a frozen buffer at
`003`. **Both had the same signature: a plausible answer produced by an
instrument that had silently stopped measuring.**

---

## ⚠⚠ THE SAVE HEADER NOW CARRIES WHAT REQUEST 001 SAID IT LACKED

**Request `001`:** *"The header carries **no name, no time, no character and no
package**."* **Format 02 carries all four**, readable straight out of the bytes:

    KRSV · fmt 02 · "gzip" · "0.1.0" · <timestamp> · "tester-probe"
         · "Yard Tester" · "soldier" · "a01-probe-room"

**A time, the package, the character, the class, and the area.**

**And the screen tells the truth about the ones that predate it:** `Load Game`
now reads **`when not recorded`** where it used to read `rules 0.1.0`. **That is
the honest form** — a version number was never an answer to *when*, and a file
written before the field existed cannot have one.

**⚠ THE SHELF IS MIXED AND BOTH FORMATS WORK: 15 saves at format 01, 2 at format
02.** Both list, both load, and nothing warned me the format had moved. **I only
noticed because my own reader broke on it.**

**⚠ This should retire `020`'s `listFor` filing.** I filed that a save's package
is discoverable only by replaying its whole log — **the package is in the header
now**. **I did not verify that `listFor` was changed to read it rather than
replaying anyway**, and that is worth one check by someone.

**And `019`'s ordering finding is fixed:** `Load Game` is now **alphabetical** —
`bran-vex, dax-roon, hk-nine, ig-seven, ilyana-sorr, kaeda-vos, kesh-alaan,
rell-vantt, second-fight, sero-kade, t3-k9, t3-m4-probe, vekk-nal, vess-taran,
wren-ossik` — confirmed across all fifteen rows.

---

## ⚠⚠ `character.moved` IS DECLARED, READ, AND WRITTEN BY NOTHING

**Verified with correct offsets across all 17 saves: zero occurrences. In any
file. Ever.**

- **Declared** — `ledger.dart:89`, `campaign` lifetime, with the reason stated
  in the comment: *"`PT-1417` moved it up from `session` **because a save needed
  to know where a player was standing**."*
- **Read** — `play_state.dart:198` folds it into `Position(area, x, y)`.
- **Emitted** — **nowhere.** The only two hits for `CharacterEventKind.moved`
  in all three repos are the declaration and the reader.

**And it shows.** I walked Probe Walker out of the entry room, through a door
into `a03-probe-yard`, to `3, 0`; quit to the hub; pressed `Continue` — and
**arrived back in Probe Room.** The stated reason for the lifetime change does
not happen.

**⚠ This is the third instance of one shape**: `PT-1418` found fourteen emitted
kinds undeclared, `PT-1501` found `check.resolved` declared and never emitted,
and this is a kind that is declared **and read** and never written. **A complete
read path with nothing on the other end.**

---

## ⚠ `PT-1515` HAS LANDED, AND I STILL COULD NOT KILL ANYTHING — THE REASON IS THE FINDING

**It is in the code and it is right.** `Role.enemy` exists, `attack.dart:221`
gives every placed creature that role, revive is now guarded
`c.role != Role.enemy`, and `character.died` is written when `_isDead`.

**I attacked for roughly 35 exchanges across two packages and produced ZERO
`character.died` events in any save.** Not because the rule is wrong — because
of the numbers:

- **Death is at `−Constitution`** (`pools.dart`), superseding the flat −10.
- **Both creatures I fought have `con = 10`, so death is at −10.**
- **My characters are all at 1 vitality**, so every fight ends after one
  exchange, and **the enemy is revived to 1 when the fight ends** — it only
  dies if it passes −10 **within** a fight.
- The deepest I drove one was **−3**, and the log shows exactly that:
  `encounter.ended vitality:-3` followed by `character.revived`. **The next
  fight started it at 1 again.**

**⚠ So damage cannot accumulate across fights once it goes negative**, and a
character who falls every round can never reach −10. **The vacated square needs
a character healthy enough to deal `vitality + Constitution` — 18 here — in ONE
continuous fight.** Vekk Nal, level 1 and healthy, delivered **10** before
falling.

**That is not a defect and I am not filing it as one.** It is the setup the test
needs, stated exactly: **one fresh, tough character, one uninterrupted fight.**
The vacated square is now genuinely constructible and I did not construct it.

---

## Still queued, still blocked

**`PT-1516`'s flag experiment has not become runnable.** `conversation_tab.dart`
still reads `d.addEffect(sel, {'kind': _value.text.trim()})` — one key, no
payload — so a `quest.flag-set` still cannot carry the `flag` field. **The
moment that changes, the experiment is: set a flag on one character, load
another, see whether the gate opens.**

**And the status-bar step is now mine, not an observation.** Before I file
anything in Loom as inert I read the status bar first, then the file, then the
source. It has caught me twice and I have written it down so it does not need to
catch me a third time.

---

## ⚠ SCOPED NEGATIVES

- **No BG3 screenshot, and five attempts is all I spent**, as instructed.
- **I did not try Proton, a forced compatibility tool, or editing Steam launch
  options** — the last would have meant writing to the owner's Steam config.
- **I did not verify that `listFor` now reads the header** rather than replaying
  every log; I only established that the header has the field.
- **I did not test whether a format-02 save loads in an older build**, or what
  happens if the shelf is mixed in the other direction.
- **`character.moved`: I did not check whether `projectPlayState`'s `where` is
  consumed by anything** — only that nothing produces it.
- **I never produced a death**, so the vacated square, a body on a wall square,
  and everything downstream of `character.died` remain untested by me.
- **Everything I measured about death is from two creatures with `con = 10`.**
  I did not test a creature with a different Constitution.
- **Not touched:** the eight inert blueprint kinds, `NewItemDialog`, other
  window sizes.

---

## What this run changed

**Packages: nothing** — `diff -r` reports **IDENTICAL** against the pre-run
backup, including the test wall I painted and removed.

**Saves: `yard-tester.sav` and `vekk-nal.sav` were played and rewritten** — and
in doing so **both were migrated from format 01 to format 02**, which is how I
found the header change at all. **Fifteen format-01 saves remain.**
