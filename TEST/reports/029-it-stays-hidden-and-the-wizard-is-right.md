# 029 · It stays hidden — the negative case passes; and what the wizard gets right

**From `Tester`. Unrequested number.** `PT-1512` followed; packages and saves
backed up to `BK6/` first.

**⚠⚠ TWO BUILDS, AND EACH FINDING BELONGS TO ONE OF THEM.**

    §1  hidden / PT-1576     app 355f370 · Lodestar 9ef2fd2 (pinned, matched HEAD) · Lens 6b55219
    §2–§6  Loom              Loom 07e70ed · same Lodestar line

**⚠ I checked the pin before building.** `KOTOR-RPG-APP/pubspec.lock` carried
`resolved-ref: 9ef2fd2…`, which matched `Lodestar` HEAD exactly, and the source
is `git` — so the build took the committed ref, **not** the working tree, which
was 2 files dirty at the time. *(What was dirty was `package_validate.dart` —
Coder acting on `027`/`028`.)*

**⚠ And the tree moved four more times while I worked.** As I write: `Loom
07e70ed` · app **`f636082`** · `Lodestar` **`c832b1c` (2 dirty)`**. **Nothing
here is a finding against those.**

---

# ⚠⚠ 1 · `PT-1576` PASSES, AND THE CASE THAT MUST NOT WORK DOES NOT WORK

**You said a find test alone proves nothing. So the bed is a matrix, and two of
its three rows are negatives.**

## The fixture, in `a04-probe-slit` — 64×2, arrival `west-end` at `0,0`

    probe-warden.probe-slit.02     at 4,1    stealth 5     range default 10
    probe-sentinel.probe-slit.03   at 6,1    stealth 35    range default 10
    probe-anvil.probe-slit.04      at 40,1   stealth 5     range default 10

**Chosen so no single condition explains the result.** `.03` is **in range** and
must stay hidden **on stealth**; `.04` would be found **on stealth** and must
stay hidden **on range**.

## What happened, walking in through the door rather than loading inside

| case | expected | observed |
|---|---|---|
| `.02` — in range, low stealth | found | ✅ **"you notice probe-warden — 10 against 5"** |
| `.03` — in range, stealth 35 | **hidden** | ✅ **not drawn** |
| `.04` — distance 40, stealth 5 | **hidden** | ✅ **not drawn** |

> **⚠⚠ THE NEGATIVE HOLDS: a creature a passive 10 had just beaten at distance
> 4 is NOT found at distance 40. Range gates it.**

**⚠ And `.02` was found ON ARRIVAL, without a step taken in that area.** I came
through the door from `a01`, landed at `west-end`, and the notice fired. That is
the half `PT-1573` exists for — *"you walk into a room already standing
somewhere."*

## ⚠ Settled once — proved by closing the distance and getting nothing

**I walked from ~6 squares to 1 square of `.03`** — standing directly above it at
`6,0` — **and it was never re-evaluated.** No second message, no second chance.
The contract's own warning (*"what a caller must still not do is re-ask as the
finder walks closer"*) is obeyed.

## ⚠ `PT-1550`'s floor holds, and it is worded differently on purpose

Pressing `Down` from `6,0` into the hidden square:

> **"something was waiting there — probe-sentinel"**

**A creature with `stealth 35` against a passive `10`, which had FAILED the
notice check and was invisible at distance 1, is found by contact.** The roll is
irrelevant to walking into it.

**⚠ And the two findings say different sentences** — *"you notice X — 10 against
5"* against *"something was waiting there — X"*. **You can tell whether you
spotted it or blundered into it.** Keep that.

**⚠ It held its square.** I remained at `6,0`; the sentinel occupies `6,1`.
`hidden` is not absent.

## ⚠⚠ AND THE RANGE BOUNDARY, MEASURED TO THE SQUARE

Walking east toward `.04` at `40,1`, one step at a time:

    at 29,0   distance 11   ⚠ nothing
    at 30,0   distance 10   ✅ "you notice probe-anvil — 10 against 5"

**So `.04` — hidden at 40 — is found the moment the finder is within 10.**
`range` is a live distance, not a permanent flag.

> **⚠ And the metric is CHEBYSHEV, not Euclidean.** `30,0` → `40,1` is
> `max(10,1) = 10` and it fired; Euclidean would be `√101 ≈ 10.05` and would
> have needed `x = 31`. **`<=` includes the boundary square.**

## ⚠ One thing the matrix caught that I had shipped myself

On loading into `a01-probe-room` the first message was:

> **"you notice probe-warden — 10 against 0"**

**That is my own `026` fixture — `hidden = true` with NO `stealth`.** Its total
is **0**; a passive **10** beats it always. **That is the flawed-fixture shape
you warned about, and my own bed had it.** It is left in place on purpose: it is
the shortest demonstration that a find test alone proves nothing.

**⚠ And the message shows the arithmetic** — `total against stealth` — which is
`PT-1543`'s components-and-total, and is why the flaw was visible at a glance.

---

# ✅ 2 · `PT-1575` IS FIXED, AND MY ZOO IS THE PROOF

**`028 §1` filed it; `Loom 07e70ed` closes it.** The six fixtures now read:

    probe-anvil · probe-doubled · probe-sentinel · probe-warden      (fine)
    ⚠ zoo-comment-only   The file has no [character] section.
      zoo-deep-equip                                                  (fine)
    ⚠ zoo-empty          The file has no [character] section.
    ⚠ zoo-no-name        [character].name is missing or is not text.
    ⚠ zoo-unparseable    The character file is not valid TOML:
                         TOML parse error: end of input expected at 3:27
    ⚠ zoo-wrong-kind     The file has no [character] section.

**Four distinct, accurate reasons across five broken files** — and
`zoo-unparseable` carries **the reader's own error with a line and column**,
which is the shape `027 §2` asked for.

**⚠ And the sharp end of `028` is closed too: they cannot be armed and cannot be
placed.** Clicking `zoo-empty` does not highlight it; clicking the board
afterwards **writes nothing**. The problem count moved **5 → 7**.

**`zoo-directory.toml` is still correctly excluded.**

---

# ⚠⚠ 3 · WHAT THE CONVERSATION WIZARD GETS RIGHT — in detail, because a control is about to be built into it

**You asked for this at the same weight as the fault. It deserves it: this is
the best surface in the Builder.**

## 3a · It asks in the domain's language and never shows a field name

    What do they say when the conversation begins?
    Does this line have replies, or does it continue?
    What can the player say?
    when can they say it?
    and what do they say back?
    and then what happens?

**Not one of `replies`, `then`, `gate`, `effect`, `say` or `id` appears.** The
options are in player terms too — **"the player answers" / "they keep talking"**,
not `replies`/`then`.

## 3b · Every field arrives prefilled with content that works

    the first line   "You are not supposed to be here."
    they say         "I was told to come this way."
    the answer       "Were you. Go on, then."
    they say         "Stand aside."          (gated)
    the answer       "Fine. Be quick about it."
    the failure      "My orders say otherwise. Last warning."
    they say         "Then stop me."
    the answer       "Gladly."               (a fight starts)

**Press through and you have a working three-option conversation with a check, a
failure branch and a fight.** Nothing must be typed.

## 3c · ⚠⚠ THREE CLOSED VOCABULARIES ARE RENDERED AS LISTS

| vocabulary | how it is shown |
|---|---|
| **the ten gates** (`§4`) | `always` · `only if they pass a check` · `only once something has happened` · `only at a point in a quest` · `only if they feel a certain way about you` · `only if they can pay` · `only if a companion is with you` · `only for a species` · `only for a background` · `only at an alignment` |
| **the skills** | the full roster as buttons — `Persuade` selected and mirrored into the field. **⚠ This is `PT-1571` built.** |
| **the effects** (`§5`) | `nothing in particular` · `a fight starts` · `something is remembered` · `a quest reaches an end` |

**Each has a sensible default preselected** (`always`, `nothing in particular`)
so the next control is always live.

## 3d · ⚠⚠ IT EXPLAINS THE CONSEQUENCE, NOT THE FIELD

> *"replies are SHOWN ALL AT ONCE and the player picks; a continuation hands
> straight on to another line they say. **A line carries one or the other — the
> reader refuses both.**"*

> *"the kind alone is the whole effect — **nothing to fill in**."*

**The first names what the READER does. The second answers the payload question
`PT-1516` was about, at the point of use.**

## 3e · ⚠⚠ IT CARRIES MY OWN `PT-1326` FINDING AS A WARNING TO THE AUTHOR

Under the failure line:

> **"⚠ and the failure line is an ending. §9's own example sends a failure back
> to the same check, which makes it free — twelve passes out of twelve at a
> nominal 55%."**

**That is `TEST 016`'s measurement, quoted at the exact place an author could
repeat the mistake.**

## 3f · ⚠⚠ AND IT GENERATES THE `§9` SHAPE CORRECTLY, WHICH I HAD TO FIX BY HAND

**The written file — I pressed `Write` and it validated:**

    replies = ["i-was-told",
               { to = "stand-aside", gate = { skill = "Persuade", dc = 14 } },
               "then-stop-me"]

    [[player]] id = "stand-aside"
    then = [{ to = "fine-be-quick", gate = { skill = "Persuade", dc = 14 } },
            "my-orders-say"]

**The check is in BOTH correct places** — **inbound** on `replies`, gating
whether the option is *offered*; **outbound** on `then`, gating which *answer*
you get, with `my-orders-say` as the **ungated fall-through**.

> **⚠ That is exactly the fix `026 §8` made me apply by hand to
> `sentinel-challenge` after Loom refused it. The wizard writes it right by
> default. It does NOT reproduce `PT-1326`.**

**Also generated without being asked:** `tag = "lie"` on *"I was told to come
this way."* (`§3`'s manner tag), `effect = [{ kind = "encounter.began" }]` with
no payload, and **ids slugged from the text** — `you-are-not`, `fine-be-quick`,
`then-stop-me`. Readable, derived, unnumbered.

## 3g · ⚠ It names its own limits and hands off

    the editor opens on this, and it is what these are for
      · a compound condition
      · more than one beat
      · a second speaker
      · a line that must not be rephrased
      · an effect nothing reads

**And it does hand off** — `Generate` opened the editor on the tree rather than
writing blind, so you see what you made before it exists.

> **⚠ In `STUDY 27 §6` I filed against Aurora's Sound Wizard that *"the wizard
> cannot reach every valid state"* — I chose `Single-shot(s)` and `Once` was
> reachable only from the editor, with nothing saying so. THIS WIZARD SAYS SO,
> AND LISTS THE CASES.**

## 3h · Two smaller things it gets right

**`start from an empty tree` is offered at EVERY step**, beside `next`. **The
wizard is never a trap.**

**The verb is `Generate`, not `Create`** — it says it produces content rather
than recording what you typed.

---

# ⚠ 4 · What it still gets wrong — unchanged from `028`

**⚠⚠ `owner` IS THE ONLY FREE-TEXT FIELD LEFT IN IT.** And `§3c` above is why
that now reads as an oversight rather than a gap: **the same wizard renders three
closed vocabularies as lists**, including one (`skills`) that `PT-1571` converted
from a typed name *for this exact reason*. **`owner`'s vocabulary is enumerable
from the module tree three inches to the left of the field.**

**`028 §4` established the consequence** — a typed owner is how
`endar-spire/dialogue/trooper-challenge.toml` came to name
`sith-trooper.command-deck.07` against an area holding only `.39`.

**⚠ "There is no conversation here." is still drawn in ALERT RED on the CREATE
surface.** Nothing is wrong when you press `+` to make one.

---

# ⚠ 5 · The two you asked me to press again — both still true

**⚠ The item dialog's refusal is still below forty base types.** `016`,
re-confirmed in `028 §2` on `84f49ec`: `Create` does nothing, and *"An item needs
a path — where it lives IS what it is"* renders at the bottom of the scrolling
body, below ~40 base types and a `description` field, while `Create` is pinned in
the action row.

> **⚠ The conversation wizard's own action row is NOT below the fold** — `back` ·
> `Generate` · `start from an empty tree` sit at the end of the pane and the
> outer scroll reaches them. **So the two dialogs disagree about this, in the
> same program.**

**⚠ `doors` and `waypoints` still carry both lines** on `07e70ed` — the correct
sentence and *"cannot list — no folder is specified for this kind yet"*, which is
false for those two because `§4a` makes them a way permanently.

---

# 6 · Scoped negatives

- **`PT-1578`'s continuation control** — not built when I looked; **not chased,
  as instructed.** When it lands the test is to sit through a conversation at
  reading pace, which I cannot assert from a screenshot.
- **Whether `.02`'s find persists across a reload** — I re-entered once and it
  re-fired on arrival; **I did not test whether a find is remembered.**
- **A hidden thing with an explicit non-default `range`** — all three fixtures
  used the default 10. **The `range` override is untested in play.**
- **`stealth` between tiers** — I used 5 and 35, both on the ladder. **An
  off-ladder number is untested.**
- **A finder with a non-zero Awareness/Alertness** — Yard Tester's passive was
  10 throughout, so **the `max(awareness, alertness)` half never varied.**
- **The app at `f636082`** — landed as I wrote; not built.
- **Painting tiles in Loom** — still not done, five sessions running.

---

# 7 · What I left behind

**`a04-probe-slit` is now the `PT-1576` bed** and is worth keeping:

    tag_seq 4
    probe-warden.probe-slit.02     4,1    hidden, stealth 5     ⚠ the positive
    probe-sentinel.probe-slit.03   6,1    hidden, stealth 35    ⚠ in range, stays hidden
    probe-anvil.probe-slit.04     40,1    hidden, stealth 5     ⚠ out of range, stays hidden

**⚠ I removed `probe-anvil.probe-slit.01` (at `3,0`, never hidden)** — with it
and `.02` on adjacent columns in opposite rows, the 2-row corridor was
impassable without combat. **Declared because it changed the fixture mid-run;
the three matrix results above were all obtained before and after that removal
and did not change.**

**`a01-probe-room` keeps `probe-warden.probe-room.10`** — `hidden` with **no
stealth**, total 0. **The flawed-fixture demonstration, on purpose.**

**`dialogue/wizard-doc.toml` is the wizard's own output**, written and
validating. Kept as the reference for `§3f`.

**Backups: `BK3/`–`BK6/`.**
