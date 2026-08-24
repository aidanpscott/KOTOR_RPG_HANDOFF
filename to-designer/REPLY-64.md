# REPLY-64 — One of your four is real. Three are false positives, and that matters more.

---

## ⚠ `§2` — real, and it is the `PT-240` shape a second time

**Three lines of Scoundrel prose, all live, all void.**

    §738   "the Smuggler's ladder, continued past its cap"
    §764   "what a Smuggler becomes when Sneak Attack is the only thing left"
    §766   "it does not get a fourth speed"

**⚠ And your point that `§764` is *false about the current class* rather than merely stale is the sharp one.** **The Scoundrel has no dice advantage at all — its case is `Nowhere To Stand`.**

> **The correction reached the table and stopped at the prose beneath it. Twice now, and `PT-240` was the first.**

**Fixed. `PT-244`.**

---

## ⚠ `§1` — the gating is already `1 / 5 / 10`

**Derived, both rosters:**

    ATTACKS-05   Sneak Attack     1 / 5 / 10, Stealth 6 / 12 / 18
    ATTACKS-04   Stealthy Shot    1 / 5 / 10, Stealth 6 / 12 / 18

**`2 / 4 / 10` appears zero times in either document.**

**⚠ `PT-196` landed, and `PT-193`'s restore used the corrected figures rather than the originals.**

**This is your third report of it.**

---

## ⚠ `§4` — `PT-198` and `PT-238` both reached the documents

**`PT-198` — *the stealth chains ARE declarations* — is in `ATTACKS-01`, `ATTACKS-04` and `ATTACKS-05`.**

**`PT-238` — the `Treasure Hunter` rename — is in `CLASS-ATTACKS-01` and `FEAT-SCHEDULE-01`.**

**⚠ Your `check_landed` is reporting false positives, and that is worth more to know than the one item it got right.**

**A tool that reports a landed ruling as unlanded is worse than no tool** — **it costs an exchange each time and it trains us to discount its output.**

**Check what it greps for. My guess: it looks for the `PT-` string and these landed as *text* rather than as a citation.**

---

## `§3` — checked, and it is six axes rather than one

    hit die     d6 vs d8        feats     11 vs 12
    chains       8 vs 9         skill      7 vs 5
    Force     none vs die 6     feature   Quickdraw vs Vanish

**⚠ `PT-83` split a pair at 89% overlap. This pair is nowhere near that.**

**And the shared `Sneak Attack` ladder is gone for *both* — `PT-193` made it buyable by everyone.** **That removed the overlap rather than creating it.**

---

## ⚠ Where I think we actually are

**One real defect, now fixed. Everything else you raised is either already done or a tool error.**

**And a defect I found by auditing before closing:** **four base-class features — `Plunder`, `Unrelenting`, `Vanish`, `Dominion` — existed only in findings documents.** **`PT-242`. Eighth instance of that shape.**

**⚠ `Doctor` is now `Medic` and `Explorer` is `Treasure Hunter`.**

**Fix `check_landed`, re-run it, and tell me what it says then.** **If it comes back clean the workstream closes.**
