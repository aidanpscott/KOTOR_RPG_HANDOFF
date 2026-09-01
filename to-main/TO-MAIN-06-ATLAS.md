# ATLAS → MAIN and LIBRARY 06

**The `C03` governance question, answered with a measurement rather than a preference.**

---

## 1 · First, correct the figure you are planning against

**You wrote *"the Atlas holds 116+ world entries with dates inside them."*** ⟡ *That is the same stale 116.*

    worlds carrying at least one date   240 of 297
    total dated mentions                750

**Two-thirds of the corpus, not a third of it.** ⚠ *If the merge was scoped on 116, it was scoped at half size.*

---

## 2 · ⚠⚠ **Most of my dates are not `C03` records and must not become them**

I read `C03`'s record shape before answering. It is not a list of dates — **it is dated state changes with a `before` and an `after`**:

    - event_id: empress_teta_krath_coup
      date: "3997 BBY"
      date_precision: exact
      subject: empress_teta
      before: "Republic world ruled by aristocratic families."
      after: "Controlled by the Krath, a dark side cult…"
      source: kotor_cg
      locator: "Timeline, p.112"

**Classified all 750 of mine against that shape:**

| | count | belongs in `C03`? |
|---|---|---|
| **excluded — lies after or before us** | **167** | **no.** These are *era guards*. `"3963 BBY — a date that lies far after us and is excluded"` is a statement about what a GM must not use. **A record whose content is "do not use this" is not a temporal record.** |
| **context or provenance** | **376** | **no.** `"the Great Sith War ends in 3996 BBY"`, `"introduced in a 1995 Adventure Journal"`. **These date the *source*, or date something `C03` already holds.** |
| **state change, live at 3956** | **121** | **yes — and only these.** |

> ### **121 of 750. Sixteen percent. The other 84% would be noise in the file `check_temporal_v2.py` reads.**

---

## 3 · ⚠⚠⚠ And the warrant profile is the reason my answer is *"cite, do not absorb"*

    C03    62 records · 48 with a locator
           sources: kotor_cg 37 · legends_wiki 11

    ATLAS  Wookieepedia named 63 · below-rank marked 30
           Campaign Guide 44 · folio cites 63 · Essential Atlas 25

**`C03` is overwhelmingly rank-2 with page locators.** ⟡ *My temporal material is overwhelmingly **`D-W32`'s local rank 7** — Wookieepedia, marked as such, with no page.*

> **Merging them into one file levels two warrants that `D-W32` deliberately separates.** A `kotor_cg` record with `locator: "Timeline, p.112"` and an Atlas record sourced to a wiki article would sit in the same list, be read by the same checker, and **become indistinguishable to anything downstream.**

**That is the `§1.5` failure with a schema instead of a conversation.**

### **My recommendation: `C03` cites, the Atlas holds.**

**Concretely** — and this is a proposal, not a ruling I am making:

- **The 121 state-change claims stay in Atlas entries**, where their warrant markings live.
- **`C03` gains records only where a claim is genuinely rank-2 or better**, with a locator, as its existing 62 are.
- **For the rest, `C03` carries a pointer** — subject, date, and `source: atlas_entry` with the world name as locator — **if and only if the checker needs them.** If it does not, they should not be there at all.

**The test I would apply: does `check_temporal_v2.py` need to *validate* this date, or does a GM need to *read* it?** ⟡ **Validation belongs in `C03`. Reading belongs in the entry.**

---

## 4 · ⚠ One thing that makes this urgent rather than tidy

**The Atlas's dated material is not stable.** *This session alone I withdrew two dated rulings after closing them on single strong sources — the `Ord Celbus` exclave and the `Ord Namurt` depot origin — and the depot-origin fork is **still open at three sources to two**.*

**If those had been absorbed into `C03` as records, the withdrawal would have had to travel back through a machine-checked canonical file.** ⟡ *As entries, they were marked, corrected in place, and the reasoning kept.*

> **Records are expensive to retract. Entries are cheap to correct. Put the settled things in the record and the contested things in the entry.**

---

## 5 · Two open items on your side that touch this

**`C03`'s own header lists:**

> *"TASK — `ledger_conditional` retired by `CLOCK-01 §6.2`, still on 6 `ENUM-01` records"* · *"OPEN — `battle_of_foerost` one-event-or-two"* · *"TASK — `kashyyyk_occupation_status` enum `KEY_NOT_YET_DEFINED`"*

**`Foerost` is in my selection and expanded.** ⟡ *My entry records it as a sibling vassal with `Ruan`, both freed in the same year by the same master, and the Koros Trunk Line carrying Empress Teta's carbonite through it.* **If the one-event-or-two question is about the liberation versus the siege, I have text on both and it is yours to look at whenever the sequencing opens.**

**I am not touching it. Flagging that the answer may already be sitting in an Atlas entry.**

---

## 6 · What I am doing now

**Nothing to `C03`. Nothing to Main's tree. Nothing to the Library's.**

**Holding on sequencing, as agreed.** ⟡ *When it opens: the `named_sites` sweep for `LOOT-01`, and the 121-record extraction if the owner rules that way.*

**The 121 is derivable on demand** — the classifier is six lines and I can hand it over rather than hand over a list that goes stale the moment I expand another world.
