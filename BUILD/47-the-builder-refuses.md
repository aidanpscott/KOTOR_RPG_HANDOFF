# 47 · `PT-1461` — the Builder refuses, the bed answers, and the field was there

**637 green** — Lodestar 293 · Lens 4 · Loom 115 · app 225.
`Loom f5a5103` · `app 5571dd7` · `MAIN_WORK 4b67616`.

---

## 1 · Loom refuses to write what `validate` refuses

**⚠ The tab has been showing `validateConversation`'s problems the whole time
and wrote anyway.** That is why `PT-1459`'s new rule immediately made the bed's
own conversation invalid: **Loom wrote it.**

> **`PT-1379` — the Builder cannot create the fault it detects.** A tool that
> authors what `validate` refuses is a tool that manufactures work.

**⚠ AND IT REFUSES ON ANY PROBLEM, NOT ON THIS ONE.** The rule is about the
relationship between the writer and the reader, so **a check added later is
covered without anybody remembering to wire it.**

---

## 2 · The bed gets four answers, authored in Loom

**`tool/author_bed_answers.dart` loads the bed's conversation into
`ConversationDraft`, adds the trooper's answer to each approach, links them,
refuses if `validate` refuses, and writes with `ConversationWriter`.** Not
hand-written TOML — `PT-1346`.

**Minimal, because the bed is a fixture.** A gated reply's `then` is the NPC's
answer to that particular approach: **the trooper believes you, stands aside,
defers, or takes the money**, and each answer ends the conversation.

    command-sent-me   → "Nothing on my board about you. Nothing about a liar either. Go."
    you-are-one       → "...One man. Yes. Go on, then, before I think better of it."
    you-are-speaking  → "Sir. I did not see your rank in this light. Carry on."
    fifty-credits-says→ "Fifty says I saw nobody. Walk quickly, officer."

**The authoring test now authors an ANSWER rather than the fault**, so a green
write is itself the assertion that the conversation is sound — and a second
test pins the refusal, **including that the fix is an answer and not a looser
rule.**

---

## 3 · ⚠⚠ The feat eligibility field already existed

**`PT-1460` asked for a field. `section` IS it**, and `FEATS-LIBRARY-01`'s own
summary names the groups:

    1 · Everyone — organics and all droids        16   ✓ matches the extract
    2 · Organics and combat droids                 9   ✓
    3 · Organics only                             68   ✓
    4 · All droids — the chassis                  39
    5 · Restricted — class or chassis

**Nothing read it.** Every feat `TEST 004` saw offered to an organic —
`Droid Upgrade 1`, `Droid Interface`, `Droid Upgrade 4`, `Emergency Reboot` —
is **section 4, all droids**. And a droid was offered `Cybernetic
Implantation`, section 3. **The droid list was byte-identical to the organic
one because the eligibility was in the data and unconsulted.**

> **⚠ SAME SHAPE AS `droid_arrays.toml`, ONE SLICE APART: authored and then
> orphaned.** `FeatsScreen` was given `className` and no species, so it could
> not branch — **and the field it would have branched on was already there.**

**⚠ Only 3 and 4 are filtered.** Group 2 is *"organics and combat droids"* and
**nothing says which chassis is a combat droid**; group 5 is restricted by
class or chassis and the extract carries no field naming which. **Left offered
rather than guessed at, and a test asserts they still are** so the omission
cannot go quiet.

### ⚠ Two data defects found while checking, and NOT corrected

- **`Environmental Sealing` carries `availability = "selectable"`** while its
  own description reads *"Granted at 1st level to every droid."* `availability`
  already has a `granted` value — **188 feats use it** — so this is a wrong
  value, not a missing field. **Deriving it from the prose would be `TRACE-83`
  again**, so it is reported.
- **`Plating Proficiency: Light` is `section = "3"` — organics only —** while
  its description says *"DROID ONLY — PT-615."* ⚠ **And it is not in
  `FEATS-LIBRARY-01` at all**, so its section came from somewhere else.

**Those two are why a droid is still charged for a feat it already has.** The
organic side of `U2` is closed; **the droid side is a data correction and a
ruling, not code.**

---

## 4 · ⚠⚠ Can anything catch the CLASS — a front-end pinned behind an engine fix?

**Yes, and it is not a test.** `MAIN_WORK/scripts/check_engine_pin.py`.

**⚠ WHY A TEST CANNOT BE THE WHOLE ANSWER.** A test can only fail on behaviour
it already knows to look for — **`droid_loads_test` exists because somebody had
already been bitten by that exact rule.** The next engine fix will be a
different rule, and no test written today will cover it.

**This asks a question that needs no foresight: *is the lock behind the
engine?*** It reads each front-end's `pubspec.lock` and compares to the
engine's **`origin/main`**, and it catches every case at once — 4 comparisons,
two engines against two front-ends.

**⚠ `origin/main`, NOT the local HEAD.** A front-end can only resolve what has
been pushed, so an engine commit that exists only locally is **work in
progress, not a pin-behind.** Comparing against `HEAD` would cry wolf on every
commit before its push.

**Controlled all three ways**, `PT-1451`'s convention:

    clean                  4 compared · all level with origin/main       rc 0
    a real pin-behind      names the repo, both refs and the fix         rc 1
    an empty tree          "has NOT looked and is reporting nothing"     rc 2

**⚠ It has bitten twice and `BUILD/37` predicted it both times**, which is the
argument for a check rather than a memory: **the note was written down, read,
and did not stop it happening again.**
