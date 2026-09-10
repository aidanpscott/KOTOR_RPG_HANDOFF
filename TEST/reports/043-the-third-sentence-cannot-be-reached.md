# TEST 043 — the third sentence cannot be reached, and the four inert kinds are one kind

**Built against:** app `660134a` (*Engine pin: PT-1622's clamp and the deduplicated
didYouMean*) → Lodestar `9aa73822c5022024b841b017445e978ad80c9227`, bundle
`kernel_blob.bin` built **16:11**. Loom bundle built **16:39** at Loom HEAD
`908a412` (*PT-1629 — scripts returns as a third root*).

⚠ **`4b66395` (PT-1626) IS NOT IN MY BINARY.** `strings kernel_blob.bin | grep -c
"PT-1626"` → **0**; `PT-1622` → 5, `not enough to hurt` → 2. Everything below is a
measurement of `660134a`. **I did not test PT-1626's fix.**

**Instrument:** PID-scoped throughout. App PID `513413`, window `142606339`; my own
Loom PID `520365`, window `144703491`, launched from the existing bundle — I did
**not** run `flutter build`, because that writes into Coder's tree. Both killed by
PID at the end; Coder's Loom `517968` survived, which is the control.

---

## 0. The third sentence does not exist in the app

The brief asked me to confirm `grazed`, `miss` and **out of reach** read differently.
Two of the three I captured. The third **cannot be captured, and the reason is
structural rather than a matter of my not finding the fixture.**

`AttackReport.line` has three branches (`attack.dart:435–466`):

    if (outOfReach != null) return '$w out of reach — $outOfReach';
    if (!outcome.hit)       return '$w${outcome.toHit.line}… — miss';
    …                       return '$w${outcome.toHit.line}$far — hit ·$dmg …';

`outOfReach` is set in exactly one place, `attack.dart:520`, inside `strike` when
`distanceSquares > reach`. **`strike` has two callers and neither can reach it.**

- **`play_screen.dart:1687` (the player).** Coder's own comment on the line above
  it: *"Walking into something is always one square away, so this cannot refuse
  today."* Confirmed by use — an attack is only ever produced by walking into an
  adjacent square.
- **`fight.dart:226` (the enemy).** `fight.dart:213–219` computes the same
  `reachSquares(kind, incrementSquares: held.rangeSquares)` **before** the call and
  returns early:

      if (away > reach) {
        said = '$moved${me.handle} cannot reach ${d.target!.handle} — '
            '$away squares, reach $reach';

  So when the refusal is warranted, `strike` is never called, and the sentence a
  player would read is **fight.dart's, not PT-1593's.**

⚠ **So there are not three sentences. There are two from `AttackReport` — hit and
miss — and a third, differently worded one from `fight.dart` that is not the one
`PT-1593` wrote.** `AttackReport.outOfReach` and its
*"<weapon> reaches N squares and <target> is M away"* are dead in the app.

### And fight.dart's own refusal is not reachable by a player either

I tried to make an enemy end its move short. It cannot be done by moving, and I
measured why:

    probe-tusk.probe-yard.05 closes 5 squares — 6 to 1 · probe-tusk.probe-yard.05:
    unarmed · rolled 20 — d20 15 + attack 1 + Strength 2 + closed on a ranged
    weapon 2 · needed 16 · 1 square — hit · 5 damage · 7 left

My move budget is **5**; the enemy's is **at least 5**. A fight can only start by
contact, so the distance at the top of my turn is 1; the most I can open is
**1 + 5 = 6**; the enemy closes 6 → 1. `away` is never ≥ 2 at the moment
`fight.dart` tests it. Earlier, the same thing at shorter range:

    probe-sentinel.probe-room.04 closes 3 squares — 4 to 1 · … — miss

**Where I looked:** a02 (probe-feeble is sealed in the wall band, and the only
retreat square in its region is the doorway at 1,0, which transits and ends the
fight); a01 (6×5 open floor, max separation 5); a03 row 7 (ten squares of open
floor, the longest straight run in the bed, giving exactly 6). I did **not** try
authoring a new area with an impassable barrier to lengthen the enemy's path
beyond its budget — that is the one construction left, and it is the only way I
can see to put `fight.dart:215` on screen.

### grazed still does not read differently

`PT-1622`'s clamp works — captured earlier this run:

    probe-feeble.probe-hall.02: unarmed · rolled 17 — d20 20 + attack 1 −
    Strength 4 · needed 14 — hit · 0 damage · 1 left

Vitality held at 1 instead of rising. **But the derivation does not survive.** No
`1d3`, no damage-side Strength term, no *"not enough to hurt"*. The census stands:

    grep -rn "damage!.line\|damage\.line\|d\.line" KOTOR-RPG-APP/lib   → nothing
    grep -rn "toHit\.line"                                            → 2 hits

Lodestar's `combat.dart:299–310` builds the expected sentence and the app never
calls it. **A grazed hit is indistinguishable from an ordinary one.** The miss, for
comparison, captured on the same build:

    probe-feeble.probe-hall.02: unarmed · rolled 7 — d20 10 + attack 1 −
    Strength 4 · needed 14 — miss

---

## 1. `character.downed` is still not written — and the file shows the race

I landed a player on **exactly 0** and it was recorded:

    YOU FALL. The fight ends and you stand at 1 — anyone left down stands at 1
    when combat ends. — probe-anvil.probe-yard.04: unarmed · rolled 17 — d20 16 +
    attack 1 + Strength 0 · needed 14 — hit · 1 damage · 0 left

`probe-walker.sav`, decompressed, carries **three** falls and **the same three
lines every time**:

    encounter.ended {subject: <enemy>,      vitality: …}
    encounter.ended {subject: Probe Walker, vitality: -3 / -1 / 0}
    character.revived {subject: Probe Walker, encounter: …}

**No `character.downed`, three times out of three.**

⚠ **The `campaignKinds` filter is not the cause, and I checked rather than assumed.**
`base-rules/rules/event_kinds.toml:112` gives `character.downed`
`lifetime = "campaign"` — the same lifetime as `character.revived`, which **is** in
the file, written in the same tick. So `_persist`'s filter passes it and it is lost
after that.

This is independent confirmation of Coder's `PT-1626` diagnosis, arrived at from the
file rather than from the code: the surviving event is the one `_endFight` writes
last, and the lost one is `_persistCrossing`'s. **I am confirming the defect on
`660134a`, not the fix on `4b66395`.**

## 2. The ledger is not a movement trace

Same file. I walked eight squares inside a03 and **not one `character.moved` was
written.** The only `character.moved` entries are area arrivals:

    character.moved {area: a01-probe-room, x: 0, y: 0}
    character.moved {area: a02-probe-hall, x: 0, y: 0}
    character.moved {area: a03-probe-yard, x: 0, y: 0}

⚠ **And the header disagrees with the ledger.** `probe-walker.sav`'s header names
`a02-probe-hall` while the last `character.moved` in its body is `a03-probe-yard`.
I did **not** test which of the two Continue reads.

Also in `grave-digger.sav`: six consecutive `character.moved` with an **identical**
payload (`a03-probe-yard, x:6, y:6→2`), then six more identical at `7,5` — one per
fight round, at a square that did not change. I have not explained those and am not
filing them as a defect; they are noted because they are the same event kind
behaving differently on two paths.

## 3. Encounters, placeables, stores and triggers are one kind wearing four names

The brief said a difference between them would be the finding. **There is none —
and I measured it rather than eyeballing it.** Cropping the custom-tab body for all
four and diffing:

    encounters vs placeables   0 differing pixels
    encounters vs stores       0 differing pixels
    encounters vs triggers     0 differing pixels

The custom refusal, identical for all four:

    ⚠ cannot list — no folder is specified for this kind yet, so this list cannot
    be read — it is not a count
    a placement names a blueprint by path — §3 — and this kind has no format, so
    there is nothing a placement could name. Painting one would write a reference
    nothing can resolve.

⚠ **The difference is between the two halves, not between the four kinds.** The
standard half **names the kind**; the custom half does not:

    standard: base-rules ships rules/ and no blueprints/ at all, so there is no
              standard triggers — absent rather than empty
    custom:   …no folder is specified for this kind yet…     ← never says which kind

Four kinds refuse in wording that cannot be told apart. A builder who clicks
`triggers`, reads the panel, and clicks `stores` has no way to know the panel
changed.

**And the board is silent, correctly.** With `triggers` selected, clicking an empty
square does nothing at all — no paint, no status line. That is not a swallowed
refusal: `creatures` shows a list of blueprints **and a `+`**, and the four inert
kinds show **neither**, so no brush can be armed. `md5sum` on
`a01-probe-room.toml` before and after: unchanged.

## 4. Two confirmations in passing

- **`PT-1619`'s soft-lock warning is landed and correct.** The tree flags exactly
  the two rooms that trapped me: *"a03-probe-yard declares no connections, so a
  character who walks into it from another area can never leave."* I confirmed it by
  use, twice — Grave Digger and Reach Tester are both marooned in a03, and **every
  one of the five tester-probe saves now sits in a03 or a04.**
- **`PT-1629` is landed**: `scripts` renders as a third root with *"not built yet —
  PT-1341 gives them a tab inside Loom with an LSP outside it, so this is a root
  held open rather than a kind that is missing."*

## 5. The Gamorrean still swings at the wrong Strength — on a second creature

    probe-tusk.probe-yard.05: unarmed · … + attack 1 + Strength 2 …

`probe-tusk` has `str = 14` and `species = "gamorrean"`.
`base-rules/rules/species.toml:283` — *"+4 Strength, −2 Dexterity, −2 Intelligence,
−2 Charisma."* 14 + 4 = 18 → **+4**. The line says **+2**, which is the raw 14.
**`combatantFrom` still never reads species.** This was open from `probe-boar`; it is
now confirmed on a second creature, so it is not a property of one blueprint.

`+ closed on a ranged weapon 2` fired correctly against me both times, because I was
holding a Blaster Rifle.

---

## What I did not check

- **PT-1626's fix.** Not in my binary. Untested.
- **Whether Continue reads the save header's area or the ledger's last `moved`.**
- **The six identical `character.moved` rows** in `grave-digger.sav`.
- **`fight.dart:215`'s refusal on screen.** Proven unreachable by moving; not
  attempted by authoring a barrier area.
- **`sounds` and `items`** were not re-opened this run; the four assigned kinds were.
- **Click-to-move and diagonal keys.** Neither did anything in play on this build —
  clicks on the board only selected, and `KP_9`/`KP_Home` moved nothing. I did not
  chase it; flagging it because `PT-1443` is named in the code as the reason the
  player's reach check exists at all, and if click-to-move is inert then that
  justification has no path behind it yet.

## State

- Saves **restored** from `SV-T042` — `diff -rq` clean. My contamination
  (`probe-walker.sav`, `grave-digger.sav` changed; `reach-tester.sav` created) is
  snapshotted at `SV-T043-after/`.
- `tester-probe` package **unchanged** — `diff -rq` clean against a pre-run copy.
- `base-rules` **unchanged** — `diff -rq` clean against `BK19`. Nothing of Coder's
  moved under me this run.
- The NWN install was not read or written this run.
