# 28 · The empty `say` refused, and the converter folds

**236 Lodestar tests · 198 app · 101 Loom.** All three analyze clean.
**42 of the Lodestar tests are dialogue; 4 are new.**

---

## 1 · `PT-1433` — an empty `say` is a load failure

**On both node kinds**, and the player one is the case that matters —
**59% of K1's player nodes are blank.** The reason is worth keeping written
down, because refusing it looked like a loss and is not one:

> **Their blank nodes exist to work around something we fixed.** K2's `Logic`
> joins **exactly two** conditions with one operator, so asking a compound
> question meant **chaining blank nodes**, each testing one piece and pointing
> at the next.

**`§4`'s `all_of`/`any_of` nest arbitrarily deep, `PT-1431` added `not`, and
`PT-1432` made a reply list show ALL that pass.** A compound test is one gate,
a not-yet is a negation, and an if-this-else-that is two replies with two
gates. **The node has nothing left to do.**

## 2 · `PT-1432` — the ordering check is now correct rather than provisional

Nothing changed in the code. **The narrowing was already right** and the
comment that called it *"reported, not resolved"* now cites the ruling.

---

## 3 · ⚠⚠ The converter folds — and here is the number nobody had

    source          26 NPC nodes · 35 player nodes · 58 links · 11 ways in
    after the fold  23 NPC nodes · 15 player nodes · 29 links · 11 ways in

> **⚠ 23 of 26 NPC nodes survive. 15 of 35 player nodes do. Half the links go.**

**⚠ The NPC side barely moves and the player side collapses**, which is the
shape of the finding: **the player half of a KOTOR conversation is mostly not
the player.** Of the 20 blank nodes here, **11 were the NPC line simply
ending**, 3 merged the line below into the line above, and **6 would not fold.**

**⚠ AND NOT ONE INVENTED LINE IS LEFT.** The old fixture padded a real tree
with 20 pieces of fake dialogue. Every node in it now is a node the source had
text for; two of them say `(+1 folded in)`.

**⚠ It folds to fixpoint**, because a chain of blank nodes is exactly the shape
the source used for a compound question and one pass would take only the first
hop.

---

## 4 · ⚠ Is the fold always unambiguous? **No — and not for the expected reason**

Measured over **every blank player node in both shipped games** — 15,023 in K1
and 11,196 in K2:

```
                                                   K1       K2
terminal — the NPC line simply ends             20.8%    20.6%
merges into the NPC line above                  34.1%    41.7%
── FOLDS CLEANLY ─────────────────────────      54.9%    62.3%

a SWITCH — 2+ outgoing links, not one test       7.6%     8.1%
⚠ the SPEAKER changes across the fold           12.8%    13.7%
shared by several NPC nodes                      0.3%     3.5%
the parent also offers real replies              0.3%     0.1%
── GENUINELY AMBIGUOUS ───────────────────      21.1%    25.4%

the target NPC has other parents                24.1%    12.4%
── UNEXPRESSIBLE, NOT AMBIGUOUS ──────────      24.1%    12.4%
```

**⚠ The switch case is real and is the one that was named** — a blank node with
two outgoing links is *"route to A if X, else B"*, and it cannot become one
gate.

**⚠ But the larger ambiguity is one nobody named: the speaker changing across
the fold, 12.8% and 13.7%.** Two NPC lines merge into one line **only if the
same character says both**, and often a different one does. **Four of this
conversation's own six unfoldable nodes are that** — Carth answering inside
Bastila's conversation. **Without that check the converter would have merged
two characters' lines into one and nothing would have complained.**

**⚠ And the last row is not ambiguity at all — it is a gap.** When the NPC line
below has other parents it cannot be merged away, and **an NPC line continuing
to another NPC line with no player input has no form in this format.** A
quarter of K1's blank nodes are that. **Recorded in `§11`.**

---

## 5 · What the drop cost, and the validator said it

**The 6 unfoldable nodes were dropped rather than invented around** — a branch
we cannot express is a branch that does not survive, the same category as the
conditions. **That orphaned a five-node sub-conversation, and the validator
reports all five.**

**⚠ And the two checks fire for entirely different reasons on this one file:**
**five nodes nothing links to**, and **eleven openings of which ten can never
be chosen.** Neither check would have found the other's problem.

---

## 6 · Not built

Still no editor, no screen, no runtime. Nothing renders a conversation and
nothing plays one.
