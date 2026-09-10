# BUILD 87 — `PT-1559`: a conversation wizard. The idea is Aurora's; the questions are ours.

**909 green** — Lodestar 395 · Lens 7 · Loom 176 · app 331.

Lodestar `61e2849` · Lens `6b55219` · Loom `f72a36c` · app `f453601`.

⚠ **Loom only. No reader, no writer, no format, no runtime.**

---

## ⚠⚠ WHAT `PT-1552` ACTUALLY FOUND

Aurora's Store Wizard asks **in the domain's language** — *"what does the
shopkeeper say when the conversation begins?"* — with **working prefilled
answers**, and generates a conversation and a script.

**Ours asked for the schema.** The evidence is one file over, and it is exact:

    the editor's verbs     + line · + reply · link · effect · tag
    the editor's fields    "id or kind" · "dc"

> **That is the right tool for the tenth minute and the wrong one for the
> first.**

## ⚠ NOTHING IN THE FORMAT OR THE RUNTIME CHANGES

`DIALOGUE-FORMAT-01` was designed against `TRACE-112`'s reading of a real
`.dlg`; `PT-1435` measured the runtime at **4,000 commits per rank**.

`wizard.dart` assembles a **`ConversationDraft`** and nothing else — the same
immutable types the reader produces, rendered by `ConversationWriter`, **read
back by `parseConversation` like any other file.** The one assertion that counts
in the suite is exactly that: *render, read back, validate.*

## ⚠ IT SITS ON TOP OF THE EDITOR, LITERALLY

The tree opens on a **filled** draft instead of an empty one. **`start from an
empty tree` is one tap away**, and the label says what it does rather than
`cancel` — `PT-1376` gives the editor create/save/close and this does not take
that away.

⚠ **The name and the owner stay on the create screen.** They are what the FILE
needs (`§1`); the wizard asks about the **content**, and a wizard that re-asks a
question the author has answered is a form.

---

# ⚠⚠ THE QUESTIONS AURORA COULD NOT HAVE ASKED

## 1 · *"Does this line have replies, or does it continue?"*

**`PT-1432` and `PT-1434` as one sentence an author can answer**, offered as
*the player answers* / *they keep talking*.

Aurora has **no two-kinds-of-link-list rule and no NPC-to-NPC continuation**, so
its wizard cannot ask this and would not know to. **And the validator already
refuses a line carrying both**, so this is not a convenience — it is the choice
the format requires, moved to the moment the author is thinking about it.

## 2 · *"When can they say it?"* — A LIST, NOT A BOX

**`PT-1430` closed the vocabulary as a REFUSAL, and it is also a menu.** There
is no `script`, `call`, `expr` or resref; every term reads a projection, so the
question has a finite set of answers.

    only if they pass a check          skill (+ dc)
    only once something has happened   flag
    only at a point in a quest         quest (+ status)
    only if they feel a certain way    attitude
    only if they can pay               payment
    only if a companion is with you    party
    only for a species / background    species · background
    only at an alignment               alignment

⚠⚠ **AND THE GUARD IS THE PAIR, NOT THE LIST.** `askableGates` plus
`gatesNotAsked` **must be exactly `gateKeys`** — a key added to the reader and to
neither fails the suite. Each excuse carries its reason: `dc` and `status` are
**companions, not gates** (`§4` pairs them), `opposed` is a **form** of a check,
and `all_of` / `any_of` / `not` are **composers a wizard cannot compose**.

## 3 · *"And then what happens?"* — THREE ANSWERS, NOT FORTY

    a fight starts            encounter.began    (the kind alone)
    something is remembered   quest.flag-set     flag
    a quest reaches an end    quest.concluded    quest, conclusion

`EVENT-KINDS-01` declares ~40 kinds and `PLAY-STATE-01 §6` leaves every payload
**deliberately unspecified**. **Three have a shape a consumer reads**, and the
fields come from `effectPayloadFields`, which is derived from `flagsFrom` and
`questsFrom` rather than from what a field name suggests.

> **A pick-list of three is a wizard question. Forty would have been a text box
> wearing a menu.**

⚠ **And `startsFight` is DERIVED — `PT-1437`.** The wizard writes the effect and
the fact follows. A second signal an author could set separately could disagree
with the first.

⚠ **An effect missing its field is not written at all.** `flagsFrom` matches on
`flag`, so an effect without one is a gate that will never open — better absent
than present and unreadable, and the author never sees the validator refuse a
thing the wizard could have not written.

---

# ⚠⚠ THE VALIDATOR CAUGHT THE GENERATOR WRITING A FREE CHECK

**On its first run.** The message was the ruling:

> *`stand-aside` is offered as a `Persuade` check and its `then` carries no
> check, so `_pick` takes the first link before any dice are touched. `§9` puts
> the check on the OUTBOUND link, where a pass and a fail are different nodes
> (`PT-1501`).*

**A `skill` gate on the OFFER link renders the option amber and never rolls.**
That is `PT-1501` exactly — *twelve passes out of twelve at a nominal 55%* —
reached from a new direction, **by a generator, in the shape every author would
have copied.**

### So a check asks a second question

**"And what do they say if it fails?"** — and the wizard generates:

    the offer link      gated with the check          §4c renders it amber
    the outbound pass   gated with the SAME check     the roll happens HERE
    the outbound fail   ungated, and it comes SECOND  the fallback
    the failure node    TERMINAL — nothing links out

⚠ **THE ORDER IS MEANING.** `_pick` returns on the first ungated link, so a fail
link sitting ahead of the check would take every pass with it — which is
`unlink`'s whole reason for existing rather than a `setGate`.

⚠⚠ **AND THE FAILURE NODE IS TERMINAL.** `§9`'s own worked example **re-offers
the check from its failure node**, *"and that makes it free"*. The bed authored a
terminal one; **this generates that, so the shape an author copies is the right
one.**

⚠ **And a check is the ONE gate that needs a second answer** — the only one that
can fail **after being offered**. Every other term decides whether the option is
SHOWN (`§4c` hides what fails), and a thing you were never offered needs no
reply. The suite asserts a `payment` gate produces **no** outbound gate.

---

## ⚠ AND `PT-1433` MAKES OURS SMALLER RATHER THAN LARGER

**59% of their player nodes are blank**, because K2's `Logic` joins exactly two
conditions and a compound question means a chain of blank routing nodes.

**Their wizard must generate nodes a player never sees. Every line ours writes is
a line somebody says.** There is no invisible half to design.

---

# ⚠⚠ WHAT IT CANNOT ASK — and it is on the screen, not only in a comment

**A wizard that covers everything is the editor again.** The last step lists
these under *"the editor opens on this, and it is what these are for"*:

    a compound condition        `all_of`/`any_of`/`not` nest arbitrarily deep
                                (§4b.1), and PT-1431 makes `not` a missing
                                TENSE. §4's own example nests an any_of inside
                                an all_of; no sentence asks for that shorter
                                than the tree does
    more than one beat          an opening line, its branch, and each branch's
                                answer. DEPTH TWO. STUDY 12 calls a
                                conversation a DAG, and linking back to an
                                existing id is how a DAG is expressed — there
                                is no wizard question for "and this one
                                rejoins that one"
    which of the eight skills   ⚠⚠ A GAP RATHER THAN A CHOICE. §4c names THE
                                EIGHT and NOTHING IN LODESTAR DECLARES THEM, so
                                the check question takes a typed skill name
                                where every other closed vocabulary is a list.
                                PT-1430 closed the gate KEYS; the eight skills
                                were never written down anywhere the Builder
                                can read
    a second speaker            §6's `by` — a companion interjecting, a second
                                guard answering for the first. Their writers
                                used it a quarter of the time. It is a SCENE
                                rather than a beat
    a pinned line               §4b's `pinned` is an instruction to a later
                                pass, not a decision made while writing a first
                                draft
    an effect nothing reads     ⚠ DELIBERATE. §9's own example writes
                                `item.lost` and nothing in this project reads
                                it. The tree can write any kind, and the
                                validator says what it cannot check

---

## ⚠ TWO MORE DUPLICATED VOCABULARIES, FOUND AND NOT FIXED

Both are in the **tree editor**, which this slice was told not to rebuild.
Neither can produce a wrong file — they can only offer a smaller menu — so they
are reported rather than taken.

    conversation_tab.dart:128   `_effectFields` is a HAND COPY of the reader's
                                `effectPayloadFields`, plus `encounter.began`.
                                The wizard derives from the reader; the editor
                                beside it does not
    conversation_tab.dart:~375  the gate row offers FIVE of fifteen keys —
                                skill, payment, species, flag, not — with
                                nothing saying why those five. `askableGates`
                                and `gatesNotAsked` are now the answer to that
                                question, and the editor does not read them

⚠ **`not` is in the editor's five and is a COMPOSER**, so the editor offers a
composer the wizard correctly refuses to compose — which is right for the editor
and worth saying out loud.
