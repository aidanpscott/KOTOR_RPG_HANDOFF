# BUILD 120 — interrupt: a third link list, priced in reactions

`PT-1664`. Three answers first, then the build.

---

## 1 · ⚠⚠ WHAT TRIGGERS ONE — THE AUTHOR MARKS THE LINE

**A third link list on an NPC line, beside `replies` and `then`**, naming player
lines and gated exactly as a reply is.

```toml
[[npc]]
id  = "n1"
say = "You are not cleared for this deck, and I have a list."
then      = ["n2"]
interrupt = [{ to = "cut", gate = { skill = "persuade", dc = 14 } }]
```

⚠ **NOT A SKILL THRESHOLD ON ITS OWN.** A gate says **who** may cut in; the
author says **where** that is possible at all. **An interrupt that fired
wherever a skill was high enough would put words in the author's mouth at a
place they never wrote** — and this project refuses to infer authorial intent
everywhere else: `PT-1433` refuses an empty `say`, `PT-1432` makes list
semantics explicit.

⚠ **NOT A DOCTRINE FLAG.** `DOCTRINE-FORMAT-01` is combat behaviour; using it to
drive conversation would be a category error.

⚠ **AND IT IS NOT A FOURTH VOCABULARY.** Same `Link`, same `Gate`, same reader,
**and the same function builds the `Option`s** — `_offers` now serves both the
show-all list and the interrupt list, because two copies would be two places for
`§4c`'s colours to drift apart.

### ⚠⚠ Its home is a CONTINUING line, and that is what makes it not a reply

`PT-1578` built `Continue` for exactly the moment a player has no choice —
*"a continuation has no such pause, so either it advances on a control or the
player is reading against a timer."*

> **An interrupt is the one option you get at a moment you would otherwise only
> be able to watch.**

**The reader refuses `interrupt` on a line that shows replies.** A line that
already asks has nothing to cut into, and offering both would put two ways to
say something in front of a player at once.

⚠ **AND IT IS NOT `replies`-AND-`then` IN DISGUISE.** `PT-1432` bars those
because they race two list semantics for the **same** moment. These do not race:
`then` says where the conversation goes when nobody cuts in, this says where it
goes when somebody does. **Different moments, nothing to arbitrate.**

## 2 · ⚠⚠ WHAT IT COSTS — ONE REACTION

`PT-1373`: *a trigger PRODUCES an event and a reaction CONSUMES one.* BG3 prices
**all 122** of its `InterruptData` entries — `Cost "ReactionActionPoint:1"` —
and `STUDY 19` called that one of *"the two fields we would otherwise have
discovered late."*

**Reduced to the pool we already have**: `Budgets.reactionsLeft`, computed by
`reactionPool`, drawn in the strip since `PT-1517`.

⚠ **IF IT WERE FREE, EVERY LINE WOULD BE INTERRUPTIBLE AND `Continue` WOULD HAVE
NO POINT.** Deliberate pacing shipped this week; an unpriced interrupt turns
every continuation into a reply list with extra steps.

⚠ **A FAILED ONE STILL COSTS.** `PT-1501` resolves a check *when the player
commits*, and cutting in IS the commitment. **A failed interruption still cost
you the chance to make it**, which is what makes the pool mean anything.

⚠ **SUPPLIED, NOT COMPUTED IN THE ENGINE.** A conversation is not a turn — `§1`
gives a **turn** five counters and nothing else in a conversation spends — so
where the number comes from and when it refreshes is the app's, the seam `speed`
and `SkillFacts` use. **Today: one pool per conversation**, because a
conversation has no rounds to refresh on, so the conversation IS the window.

⚠ **AND ZERO IS A REAL ANSWER.** `PT-1517`: *a reaction pool of zero is ABSENT,
not grey.* The runtime returns **no offers** when nothing can be spent, so there
is no greyed row and no refusal behind a click.

## 3 · ⚠ WHO — THE PLAYER, AND IT IS STRUCTURAL

Not a preference. **An NPC cutting into the player's line needs a moment during
which that line is being read, and there is none** — a player line is picked and
resolves in one gesture. `Continue` is the only place where time passes without
the player acting, **and only the player is waiting there.**

So `interrupt` hangs on an NPC line and names player lines, exactly as `replies`
does. The day a player line is also read on a `Continue`, the mirror is the same
shape — and there is a case saying so rather than a silence.

## 4 · On the screen

    [Cut in] Check it again.
      ⟩ costs a reaction — you have one
    [Continue]
      ⟩ enter, when you are ready

⚠ **ABOVE `Continue`, NOT UNDER IT.** This is the moment they exist for; a
control listed under the thing that ends the moment is a control found too late.
**Asserted by position**, and the case fails when the two are swapped.

⚠ **THE PRICE IS ON SCREEN BEFORE IT IS PAID** — `PT-1315`'s discipline on the
payment bracket: a cost a player discovers by spending it is not a choice.

⚠ **AND IT ROUTES THROUGH `choose`.** An interrupt's target is a player line
like any other, so the roll, the effects and `dialogue.choice-made` are the
existing path. **One resolution, reached two ways.**

### What was found on the way

⚠ **`begin` AND `choose` REBUILD THE `Beat` FIELD BY FIELD**, so a field added to
`Beat` and not added at both copy sites is silently dropped. It cost the first
run of the engine cases and is now named at both.

---

## Tests

`Lodestar` 511 · `Lens` 7 · `Loom` 244 · `KOTOR-RPG-APP` — see the push.
Every new case checked by mutation: offers not drawn **fails**, drawn below
`Continue` **fails**, ordering restored **passes**.
