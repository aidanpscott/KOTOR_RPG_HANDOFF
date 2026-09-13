# BUILD 181 — the terminal needs one field, not a format

**A proposal. Nothing ruled, nothing built against it.** `BUILD 180` step
three: opening `TerminalPanel` from the `Slice` verb, which currently rolls and
says *"what a sliced terminal offers is not built yet."*

---

## 1 · ⚠⚠ THE ANSWER IS ONE WE ALREADY HAVE

I went looking for a terminal-options format. **KOTOR does not have one**, and
the reason is the finding:

> **A terminal's options are a CONVERSATION.** Same `.dlg` file, same replies,
> same gates — with a single field on the conversation choosing which screen
> draws it.

`200_info_term` is a dialogue. It carries `ConversationType = 1` and
`ComputerType = 0` beside `EntryList` and `ReplyList`, and **nothing else about
it is special.**

Measured across every conversation in both games — shared and module-local,
including the `_dlg.erf` archives the first pass missed:

| | conversations | ⚠ `ConversationType = 1` |
|---|---|---|
| K1 | 1,130 | **113** |
| K2 | 973 | **111** |

**About one conversation in ten is a computer**, and it is authored with the
same tool as every other one.

⚠ `ConversationType = 2` exists too — 132 and 59 — and **I do not know what it
is.** Not claimed, because I did not open one.

---

## 2 · ⚠ WHICH IS WHAT `PT-1149` ALREADY RULED, FROM THE OTHER END

`APP-UI-VISION-01 §4`: *"Computer Use and Repair are one shared screen in the
source, not two — the only real difference is which resource an option
consumes."* That ruling was made about the SCREEN. This is the same fact seen
from the content side: **one authoring format, and the renderer is chosen by a
flag.**

So the proposal is not a format. It is a field.

---

## 3 · ⚠⚠ THE PROPOSAL

### 3a · A conversation says which screen draws it

> **`[conversation] shown = "terminal"`, defaulting to `"dialogue"`.**
>
> The dialogue screen draws it unless it says otherwise. `TerminalPanel` draws
> it when it does.

⚠ **AND `absence-is-not-a-claim` APPLIES HERE**, which is why the default is
the permissive one: every conversation ever authored is a dialogue, said
nothing, and must keep working. **No cross-field check may ever fire on the
absence** — a conversation that does not say is not asserting *dialogue*, it is
declining to say, and the two must not be made to contradict anything later.

### 3b · The panel's four fields, and three are already there

`TerminalOption` wants `skill · sentence · cost · spends`:

    sentence   the reply's `say`                  ⚠ already there
    skill      the reply's GATE — `§4`'s data     ⚠ already there
    spends     the conversation's own kind        ⚠ derivable, see 3c
    cost       ⚠⚠ NOTHING AUTHORS THIS

**So one new field**, on a reply:

    [[player]]
    id    = "open-the-door"
    say   = "Open the blast door."
    costs = 3                # ⚠ the BASE, before the skill reduces it

⚠ **THE BASE, NOT THE COST.** `§5.1`'s reduction curve is already built —
`costFor({base, skillTotal})` with thresholds at 4, 9, 16, 25 and 36 — so what
an option actually costs is computed at display time from the character.
Authoring the final number would be a second copy of that curve.

### 3c · `spends` is the conversation's, not the option's

`§5.2` gives Slicing **computer spikes** and Repair **parts**, and `§4` says
the difference between the two screens *is* which resource an option consumes.
So it belongs to the conversation:

    [conversation] shown = "terminal"  spends = "spike"

⚠ **`Consumable` IS ALREADY THAT ENUM** — `terminal.dart`, `spike` and `part`,
and `Consumable.forCount()` already pluralises it live. Nothing new.

---

## 4 · ⚠ THE ONE REAL CONSTRAINT, NAMED RATHER THAN DISCOVERED LATER

**A terminal row is ONE LINE and a dialogue reply is not.** `§4` measured it:
*"a hard, one-line limit forced every option into skill tag, complete sentence,
cost, all on a single row, no subtitle possible."*

Nothing stops an author writing a 200-character reply. On the dialogue screen
it wraps; on the terminal it is **truncated or it overflows the row**, and
`PT-1501`'s ellipsis lesson says which failure that becomes — the part that
varies disappears.

**Two honest answers, and this is the one I would put to you:**

    A   `validate` refuses a reply over the row's width when its conversation
        is `shown = "terminal"`. Loud, at authoring time, and it is the same
        shape as refusing a connection that lands on an undeclared arrival.

    B   the panel wraps to two rows and the lifted geometry stops being lifted.

**I recommend A**, because `§4`'s row height is a measured value out of the
game's own `.gui` and `check_terminal_panel.py` exists to keep it that way.
**B quietly makes that check meaningless.**

---

## 5 · ⚠ WHAT THIS DOES NOT TOUCH

**`§4`'s no-write rule stands.** A terminal option is a reply and a reply's
gate is a declared predicate; nothing here adds an extension point, which is
the thing `§4` refuses on purpose.

**No `ComputerType`.** KOTOR has two computer looks. We have one screen, ruled
at `PT-1149`, and a second would need art nobody has briefed.

**Not the Repair half.** `§5.3`'s *"more vitality restored when a droid uses a
repair kit on itself"* is the same screen with `spends = "part"`, and it wants
its own slice — it is a droid-targeted verb, not a placeable one.

**Not what a sliced terminal DOES.** An option's `effect` is `§5`'s existing
node effect, naming declared event kinds. **Whether opening a door from a
terminal is expressible that way I have not checked**, and I would rather find
out in the build than assert it here.

---

## Tests

Nothing built. App **644** green, Lodestar **812**, gate **SENDABLE**.

## Still open

- ⚠ Everything above, and `§4`'s A-or-B in particular.
- `ConversationType = 2` — 191 conversations across the two games, unexamined.
- From `BUILD 180`: `[[hazards]]` is step four and is the largest.
- From `BUILD 179`: `charge` refuses all sixteen of its own items.
- `Examine`'s *what a total tells you* is unruled.
