# 29 · `PT-1434` measured, and the dialogue runtime

**256 Lodestar tests · 199 app · 101 Loom.** All three analyze clean.
**62 of the Lodestar tests are dialogue; 20 are new.**

---

## 1 · `PT-1434` — and the ruling took it from 54.9% to 99.5%

**The field is `then`, and the pair reads as one rule:**

    replies   SHOW ALL   options, to PLAYER lines
    then      PICK ONE   a continuation, to NPC lines

**⚠ One or the other, never both.** `PT-1432` makes them different kinds of
list, and carrying both would race two semantics with nothing to say which won.
**After a line the player either chooses or the conversation continues.**
`then` is now the pick-one name everywhere — a player line's and an NPC line's
are the same field doing the same job.

**⚠ And the narrowed guarantee is enforced rather than described.** The reader
still refuses a player line linking to a player line, and there is a test whose
name is the invariant.

### The conversion, re-run — both numbers

    BEFORE PT-1434   23 of 26 NPC nodes · 15 player · 6 validator problems
    AFTER            26 of 26 NPC nodes · 15 player · 1 validator problem

**⚠ All 26 survive, and the five-node orphan reattached.** Nine of the twenty
blank nodes became a `then`; eleven were the NPC line simply ending; **none was
dropped and none was merged.**

**⚠ The converter now folds to a LINK rather than a MERGE**, which is what a
routing node always was. Merging two NPC lines into one was lossy and was only
ever justified by having no alternative.

### Corpus-wide, both games

```
                                                 K1        K2
terminal — the NPC line simply ends           20.8%     20.6%
became a `then` — an NPC line continuing      78.7%     79.0%
── EXPRESSIBLE ───────────────────────        99.5%     99.6%
the parent also offers real replies            0.5%      0.5%
```

**The two shapes that could not be expressed are gone** — the target NPC having
other parents (24.1%) and **the speaker changing across the fold (12.8%)**,
which is exactly what `by` was for. **77 nodes in K1 and 56 in K2 are left**,
and they are the one shape `§3` forbids: options and a silent continuation at
once.

---

## 2 · The runtime — it walks, and renders nothing

`DialogueRun.begin` · `.choose` · `.advance`. It answers **what the NPC says**
and **what to put in front of the player**, and `PT-1432`'s two list kinds are
the whole of its traversal.

**⚠ AND THE NO-WRITE RULE STOPS BEING THEORETICAL.** Every gate term reads a
`DialogueView` built from **`CharacterRecord`** (`PT-1415`) and **`PlayState`**
(`PT-1427`) — both folds. **A gate cannot write because there is nothing
writable in reach.** It is not enforced; it is unreachable.

**⚠ A skill term COLOURS an option; it does not hide one.** `§4c` makes amber
*"a real check"* and `PT-1307` rules *"players should just roll and see if it
fails or not."* So a Persuade option is shown, in amber, and **rolls when the
player commits** — through combat's own `resolve()`, not a second idea of what
a check is. On a **pick-one** link there is nothing to show, so it rolls there
and then.

**⚠ And what nothing projects is SAID rather than read as false.** `alignment`
and `attitude` are in `§4`'s vocabulary and **`PLAY-STATE-01` projects
neither.** A gate nothing can answer hides its option **and reports why** — a
term that read as a failed gate would be a silent wrong answer.

**⚠ Effects come back as events the CALLER appends.** The runtime never writes.
`dialogue.node-reached` and `dialogue.choice-made` are engine-written — the two
kinds `§5` forbids an author from naming — and a beat is built once per
arrival, so a node's effects are produced once.

---

## 3 · ⚠ Check A held, and one of its rules was never about this

**`PT-1418`'s checks bind, and the two new kinds pass all of them** —
`dialogue.node-reached` is `session`, `dialogue.choice-made` is `campaign`,
neither is folded by replay, and the lifetime rule is satisfied because neither
is permanent.

**⚠ But one rule had to be narrowed, and it is worth saying why rather than
just doing it.** *"Every emitted kind is declared `permanent`"* **held only
while chargen was the only thing that wrote.** Both dialogue kinds are
correctly not permanent and **would have failed a rule that was never about
them.** Narrowed to the chargen kinds, with the two dialogue lifetimes asserted
directly so the coverage does not shrink.

**⚠ AND A GAP TO REPORT RATHER THAN CLOSE.** Check A's `emitted` set is *"every
kind THIS BUILD can write"*, listed by hand. **Dialogue introduces
data-driven emission:** a package's `effect` may name any declared kind —
`quest.flag-set` is permanent and replay does not fold it. **That is fine**,
because `quest.flag-set` is world state and the character record is not the
only projection any more. **But check A cannot see it, and the lifetime rule's
reasoning — *"a character that came back missing something would look exactly
like this"* — was written when it could.** The validator checks package effects
against `EVENT-KINDS-01`; **nothing checks their lifetimes.**

---

## 4 · Not built

No screen, no editor, no AI. Nothing renders a beat.
