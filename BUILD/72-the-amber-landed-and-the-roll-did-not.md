# BUILD 72 — `PT-1501`: the amber landed and the roll did not

**752 green** — Lodestar 340 · Lens 5 · Loom 127 · app 280.

---

## ⚠⚠ HOW A FLAG AND A SKILL ARE TOLD APART — **the runtime already knew**

You asked whether the distinction is in the runtime, because if it is not, that
is the work rather than the wiring. **It is.**

    _gateVerdict → Verdict.passes / Verdict.fails   a flag: HIDES its option
    _gateVerdict → Verdict.isACheck                 a skill: SHOWS it, amber

`isACheck` is a third verdict that exists **for exactly this**: it is returned
instead of pass/fail so a check is **offered rather than filtered**, and
`Option.check` is the term it kept **for the bracket**. So `PT-1432` is not at
risk from the fix — the thing that separates them is the term's own key, and it
was already separating them. **Only the call was missing.**

⚠ **A test now asserts the flag-gated reply is hidden while the skill-gated one
is offered**, in the same fixture as the roll. If a later change flattens
`PT-1432`, that case turns red rather than the behaviour drifting.

## The wiring

`§4c`'s vocabulary table gives the canonical form as a **`replies` link** —

```toml
replies = [ { to = "push", gate = { skill = "persuade", dc = 14 } } ]
```

— and its render column reads **amber — it rolls**. The gate was read by
`_gateVerdict` for visibility **and by nothing else**.

`choose()` resolves it now, **on commit**, through `resolve()` — `Verdict`'s own
contract is that a check *resolves when the player commits to it*, and
committing is choosing the reply.

⚠ **NOTHING ROLLS WHILE THE LIST IS MERELY SHOWN.** Asserted, because otherwise
opening a conversation spends the check.

### ⚠⚠ ONE ROLL, NOT TWO — and this is where `§9` and `PT-1435` meet

`§9` also gates the **outbound** link. That is not a second check: it is **how
an author says which node is the pass.** So the committed outcome is carried
into `_pick` and **routes** there rather than rolling again. `§4c`: *a pass and
a fail are already different nodes.* **Order is meaning** — the gated link
first, the failure after it.

### ⚠ And a check with nowhere to fail says so

Gate on the reply, bare `then`: the roll happens and **cannot change where it
leads**. Reported through `cannotEvaluate`, because **the runtime cannot invent
a line**, and `validate` still refuses that authoring.

## ⚠⚠ MEASURED, AGAINST YOUR OWN FIGURES

4000 commits per rank, against the shipped bed:

    rank 0   35.9% passed   expected 35.0%
    rank 4   56.2% passed   expected 55.0%
    one `check.resolved` per commit · mean modifier 0.00 and 4.00

**Twelve of twelve at a nominal 55% is closed**, and the modifier demonstrably
reaches the check rather than the DC being met by accident.

---

## ⚠ `PT-1500` — AND THE ANSWER TO YOUR QUESTION IS THREE, NOT TEN

**Three kinds get folders and none of the three is invented here.** Each is a
constant `Lodestar` already declares, a `Loom` writer already writes, and a
folder the shipped bed already has:

    creatures   characterFolder   blueprints/characters    PT-1325
    doctrines   doctrineFolder    blueprints/doctrines     PT-1441
    items       itemFolder        blueprints/items         PT-1452

⚠⚠ **THE OTHER SEVEN GET NOTHING, AND THAT IS THE ANSWER RATHER THAN A GAP.**
`doors`, `encounters`, `placeables`, `sounds`, `stores`, `triggers`,
`waypoints` — **no format, no reader, no writer, no folder constant anywhere in
the tree.** They report **cannot list**, in the Builder's terms. Giving them
homes to make the pane look complete would be the Builder asserting a layout no
document has ruled — **the same move as the hardcoded `const []`, one step
along.**

> *"None"* is a claim about a **package**. *"I cannot list this"* is a claim
> about the **Builder**. They must not print the same sentence.

⚠ Enumeration **recurses**, because `items/` nests: the id is
`items/weapons/blaster-rifle`, which is what the reader resolves and the writer
writes. A flat folder yields the bare names it always did.

⚠ **And a kind that HAS a folder and no directory reports a real empty** —
tested both ways, so this cannot quietly become *"everything cannot be listed"*.

---

## ⚠ `PT-1510` — the behaviour is right and the wording is wrong

    was:  encounter a01-probe-room left you at 3
    now:  in your campaign, a01-probe-room left you at 3

**"in your campaign" leads**, because that row can wrap or be cut (`PT-1453`,
`BUILD 69`): the **scope** must survive truncation, the room may be lost.

⚠ **The Force-pool clause four lines below it got the same sentence.** A rule
applied to one path and not the next is this project's most-repeated defect.

⚠ **Asserted** — a wording fix with no assertion regresses silently.

### `SAVE-LOAD-01`'s "known conflation" is removed

**There was no conflation.** `PT-1415` already makes a save one log per
character per **campaign**, so the character's log **is** the campaign's log for
a solo campaign — that is the design, not a stand-in. The multiplayer question
closes with it: **multiplayer characters share a CAMPAIGN, not a package**, so a
shared campaign log is one log for one campaign's several characters, **not the
per-package world log this document used to reach for.**

---

## ⚠ `TEST 018`'s TWO OBSERVATIONS ARE ONE ROOT — recorded, not built

`SaveEntry` is `handle`, `formatVersion`, `compressor`, `rulesVersion`. **No
name, no character, no level, no place, no time.** Both observations fall out of
that:

⚠⚠ **AND `Continue` ALREADY DOES THE THING THE ENGINE SAYS CANNOT BE DONE
HONESTLY.** `SaveListing` refuses to supply a "most recent" — *"ordering by file
mtime would be the caller's filesystem guessing at a fact the format does not
record"* — and `SaveStore.mostRecentHandle` **orders by file mtime.** One
surface refuses the guess and the other is built on it. **That is why they
disagree about which is first.**

⚠ **Not built, deliberately.** Making them agree is one line; making them agree
**honestly** is a format change — the header carrying a time and an identity —
and that is a ruling, not a UI decision.

## Still open

- ⚠ `tester-probe/sentinel-challenge` still needs a **failure node**: content,
  and Tester's package. The runtime now says the roll cannot change where it
  leads, so it is loud rather than silent.
- ⚠ The conversation editor has **no button for `unlink`**.
- `PT-1509` (fog) is ruled and unstarted; `PT-1484` unblocked; `PT-1485`; the
  effect columns; 45 annotation cells.
- ⚠ `AGENDA-CURRENT.md` is forked 814 / 1553. **Left, as ruled — a fork is the
  owner's decision.**
