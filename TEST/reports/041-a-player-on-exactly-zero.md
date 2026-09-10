# 041 · A player on exactly zero — watched at last, and the event still does not reach the save

**From `Tester`. Unrequested number.** `PT-1512` and `PT-1617` followed;
`BK17/`, `SV-T040/`.

**⚠⚠ BUILT AND MEASURED AGAINST — both pins read from the commits I BUILT, and
they are the same pin:**

    Loom 323c3b5  →  Lodestar 2b75092      built 15:33
    app  a74750f  →  Lodestar 2b75092      built 15:41

**⚠⚠ AND `PT-1622`'s CLAMP IS ONE COMMIT PAST THAT PIN.** The clamp lives in
`combat.dart` at `Lodestar 9aa7382`; both artifacts pin `2b75092`. **So the fix
for `040 §4` is in no build that exists yet, and I did not re-run the bug it
fixes** — `PT-1623`, applied on its first outing.

**As I write: app `660134a` · `Lodestar 9aa7382` · `Loom 802dec5` ·
`HANDOFF e29e3d2`. Nothing here is against those.**

---

# ⚠⚠ 1 · A PLAYER ON EXACTLY ZERO. WATCHED, FINALLY — AND THE EVENT DOES NOT REACH THE SAVE

**My own first negative, standing since `039`. It took six fall-and-re-engage
cycles.**

    YOU FALL. The fight ends and you stand at 1 — anyone left down stands at 1
    when combat ends. — probe-sentinel.probe-slit.03: unarmed · rolled 18 —
    d20 17 + attack 1 + Strength 0 · needed 12 — hit · ⚠⚠ 1 damage · 0 left

    Blade Tester: 1 of 11 — in your campaign, a04-probe-slit ⚠⚠ left you at 0
      · revived at 1 · you were struck down here

> **✅ `0 left`, and the campaign line records `left you at 0`. That is
> `VitalityState.down`, on a board, for the first time.**

**⚠ And the method is the finding as much as the frame.** A player who falls
stands at 1, so **re-engaging at 1 vitality is the only reliable way to reach
the knife-edge** — the next landed blow must roll exactly 1. **Observed damage
was 1, 3 and 4**, so roughly one landed blow in three qualifies, and I needed
six cycles.

## ⚠⚠ AND `character.downed` IS STILL ZERO IN THE SAVE

**On `a74750f` — the commit whose message is *"PT-1618 — the crossing reaches
the save, on both sides"*.**

    character.downed   0        ⚠⚠ after a watched standing → down crossing
    character.dying    0        ✅ correct — declared transient at 15:01
    character.died     3
    character.revived  7

## ⚠ I ran the discriminating experiment rather than guessing

**`_persist` filters by `widget.campaignKinds`, and both the dialogue path and
the crossing path go through it. So: talk on the same build, in the same save.**

    dialogue.choice-made   1      ✅ written, through _persist, this build
    character.downed       0      ⚠⚠ same _persist, same save, same session

> **⚠⚠ SO THE FILTER IS NOT THE CAUSE. `campaignKinds` is populated,
> `character.downed` is declared `campaign` in the shipped `event_kinds.toml`,
> and `_persist` demonstrably wrote a campaign kind minutes earlier.**

**⚠ What I ruled out, by reading `a74750f`:**

    _enemyTurns  1845:  if (r != null) _persistCrossing(r, r.target);
                 1847:  if (f.over) return _endFight('it is over');

**The persist happens BEFORE the fight-over return**, so the ending blow is not
skipped by ordering.

    _persistCrossing 1007:  if (r.ledgerKinds.isEmpty) return;

> **⚠ NARROWED TO: `r.ledgerKinds` did not contain `downed` for that blow. ⚠ I
> DID NOT DETERMINE WHY, and I say so rather than guessing.**

**⚠ And one structural fact that bounds where it can ever come from.**
`pools.dart:115` — an enemy is `current > 0 ? standing : dead` and **never
`down`** — so the player's swing can never produce a `downed` at all. **The
enemy-side call site hitting the player at exactly zero is the ONLY producer in
the product**, which is the path that just failed.

---

# ✅ 2 · THE REBUILT PALETTE — USED, NOT READ. AND THE DISARM HOLDS BOTH WAYS

**`Loom 323c3b5`. The palette is a mode selector: kinds at the top, the selected
kind's varieties below.**

## ⚠⚠ The disarm, with a positive control

| | | |
|---|---|---|
| arm `wall` in **terrain** → switch to **creatures** → click board | **nothing written** | ✅ disarmed |
| arm `probe-feeble` in **creatures** → switch to **terrain** → click board | **nothing written** | ✅ disarmed |
| arm `wall` in **terrain** → click board | `..:!` → `..:#` | ✅ **the instrument works** |

> **✅ IT DISARMS IN BOTH DIRECTIONS.** The failure Coder built against — *"the
> board paints a creature while the pane displays items"* — **cannot happen on
> this build**, and the third row is there because two silent negatives are not
> a finding until something proves the click can still paint.

**✅ And the `standard | custom` split is live.** Selecting `creatures` revealed
it with a `+`; `custom` carries my six creatures and the zoo in red with reasons.
**`tester-probe` supplies no standard content, so `custom` is the populated
side** — the split I have never been able to see both halves of.

## ⚠ The right pane collapses. THE LEFT PANE DOES NOT

**Right pane: ✅ only the selected mode expands; every other kind is a bare
row.**

**⚠ Left pane: it opens FULLY EXPANDED** — `▼ areas` → `a01-probe-room` → `▼
creatures` with every placement listed, and the same for `a02`, `a03`, `a04`.
**Clicking the `▼ areas` triangle did not collapse it either.**

> **⚠ The ruling you quoted is *"it collapses on open — left pane areas and
> conversations only"*. On `323c3b5` the KINDS are right and the COLLAPSE is
> not.** If a later slice carries it, this is the build it was not in.

## ✅ And `PT-1619` landed, which was my `039 §4`

**The tree now marks what it CAN file, with the reason inline:**

    probe-warden.pro…  4,1   ⚠ RED
      "…equips items/weapons/no-such-blaster in slot weapon_r_1, and there is
       no item there."
    zoo-empty.probe-…  2,4   ⚠ RED
      "…that blueprint cannot be read: The file has no [character] section."
    a03-probe-yard           ⚠ RED — AN AREA ROW
      "a03-probe-yard declares no connections, so a character who walks into
       it from another area can never leave."

**✅ Placements and AREAS both, in the pane where the author is working.**

## ⚠ A third normalisation in the tile writer

**Painting a wall over the last `!` dropped `hazard` from the legend:**

    legend = { "." = "floor", "#" = "wall", "~" = "water", ":" = "difficult", "!" = "hazard" }
    legend = { "." = "floor", "#" = "wall", "~" = "water", ":" = "difficult" }

**So the writer expands `default` into a map on the first paint (`035`),
collapses back to `default` when every square is one kind (`037`), and now
PRUNES a glyph when its last square goes.** Three directions, all correct.

---

# ✅ 3 · `connectionUnreachable`'s WALL BRANCH — THE LAST UNEXERCISED BRANCH IN THE FAMILY

    a02-probe-hall   door.probe-hall.01
    "door.probe-hall.01" is at 1,0 in "a02-probe-hall", and no walkable route
    joins it to anywhere a character can arrive. ⚠⚠ The square is wall.

**Against `039`'s floor form — *"The square is floor and it is cut off."*
Two tails, both now seen.** With `areaHasNoWayOut`'s second branch beside it.

> **⚠ The position family is finished: four members, every branch, all seen.**

---

# 4 · Scoped negatives

- **⚠⚠ WHY `ledgerKinds` LACKED `downed` — NOT DETERMINED.** I ruled out the
  filter, `campaignKinds`, the declared lifetime and the call ordering, and
  stopped there. **It needs an instrumented run or a unit test, and neither is
  mine to write.**
- **⚠ `PT-1622`'s clamp — NOT TESTED.** One commit past both pins; **no build
  exists that contains it.** And per `PT-1623` I did **not** re-run the healing
  bug it fixes — `040 §4` stands as measured, on `661405c`.
- **⚠ I did not check whether a HENCHMAN reaches `down`.** `partyStandsAtOne` is
  TRUE for a henchman on Normal, so a henchman goes `down` on any value ≤ 0
  rather than only at zero — **a much wider target, and there are no henchmen in
  the bed.**
- **⚠ The left-pane collapse** — I clicked the `▼ areas` triangle once and it
  did not collapse. **I did not test whether any node collapses**, so "does not
  collapse on open" is what I saw and not a claim that collapsing is broken.
- **⚠ The `standard` half of the split** — still never seen populated. I looked
  at `custom` only, because `tester-probe` has no standard content.
- **⚠ I painted from `terrain` only.** The other ten modes were selected but
  never painted from, and I did not open the `+` on `creatures`.
- **Painting tiles with a TILESET** — still never; every area says `no tileset`.

## What I left behind — nothing

    packages   diff -rq against BK17/  →  no differences
    all 20 saves                       →  byte-identical to SV-T040/

**`a02-probe-hall` was rewritten four times and restored; `blade-tester.sav` was
rewritten twice and restored.**

**Backups: `BK3/`–`BK17/`, `SV-T031/`–`SV-T040/`.**
