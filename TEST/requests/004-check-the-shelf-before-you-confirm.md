# 004 · Check the shelf before you confirm anything

**From `Coder`. `BUILD 149`, `PT-1772`, and the owner's ruling on top of it.**
Engine `30954f0`, app `7497018`.

---

## ⚠⚠ THE ONE COMMAND, AND IT TAKES A SECOND

    cd ~/kotor-repos/MAIN_WORK && python3 scripts/check_shelf.py

**Run it at the START of any confirmation session.** It exits `0` and prints
one line when your shelf is current. When it is not, it names the file, the
number of rows, and the rows themselves.

**If it comes back stale, re-ship before you test:**

    python3 scripts/gen_base_rules.py /tmp/br
    diff -rq /tmp/br ~/.local/share/kotor-rpg/packages/base-rules
    cp /tmp/br/rules/*.toml ~/.local/share/kotor-rpg/packages/base-rules/rules/

**⚠ DIFF BEFORE YOU COPY.** The check tells you *what* disagrees, never
*which side is right*. Twice now the generated side has been the correct one
and once — before `PT-1772` — regenerating blindly would have **deleted droid
plating from the shelf entirely** rather than correcting it, because an
extractor had gone blind to its own section. That specific hole is closed; the
habit is still the right one.

`python3 scripts/gate.py` runs it too, as a blocking check. The standalone
command is faster when the shelf is all you want to know about.

---

## ⚠ WHY YOU ARE BEING ASKED, AND IT IS NOT BUREAUCRACY

**Your shelf and mine are different installs.** If yours is behind, you are
testing different numbers than the ones I built against — and the report that
comes back is then about a difference neither of us can see from the other
side. The owner's ruling is that you **self-diagnose** rather than wait for me
to push to your machine.

**⚠⚠ THIS HAS ALREADY HAPPENED TWICE, BOTH SILENT, BOTH THROUGH A FULLY GREEN
SUITE:**

    PT-1763   Science and Survival were RULED open to droid characters months
              ago. The chapter was never edited, so the shelf went on shipping
              them "unruled" — and the Skills step printed "withheld —
              unruled for droids" over both, for every droid ever built here.

    PT-1767   EQUIPMENT-01 corrected eight weapon dice and all three droid
              plating grades. equipment.toml is where EVERY ATTACK'S DICE come
              from. It shipped the old numbers. Vibrosword rolled 2d6 for a
              ruled 1d12; droid plating gave +4/+6/+8 for a ruled +3/+4/+9.

**Either of those would have made a perfectly careful test report wrong about
the product** — and neither would have looked like anything from your side.

---

## ⚠ THREE STATES, NOT TWO — and one check per boundary

    the document      rules/*.md              what is RULED
    the extract       data/extracted/*.json   what was READ    ← check_extracts
    the shelf         base-rules/rules/*.toml what you RUN     ← check_shelf

**Neither check can see the other's gap.** `check_extracts` compares the first
pair by fingerprint; `check_shelf` compares the second. A document edited and
not extracted is invisible to `check_shelf` **and that is correct** — the
shelf and the extracts genuinely agree at that moment. If you want the whole
chain in one go, `gate.py` runs both.

**⚠ `check_shelf` passes when you have no `base-rules` installed**, and says
so. Absent is not stale, and you should not be blocked on somebody else's
install state.

---

## ⚠ WHAT CHANGED UNDER YOU SINCE YOUR LAST SESSION

Re-ship before confirming anything that touches these:

| | |
|---|---|
| **weapon dice** | eight base types corrected — Vibrosword `2d6`→`1d12`, Lightsaber `2d10`→`2d8`, Blaster Carbine, both Disruptors, both Ions, Sonic Rifle |
| **droid plating** | `+4 / +6 / +8` → **`+3 / +4 / +9`**, read from `baseitems.2da` rows 66–68 and confirmed by K1's own attested sums |
| **droid skills** | `Science` and `Survival` are now **selectable** for every droid chassis — 11 universal, not 9 |
| **droid designations** | a droid blueprint named `T3-M4`, `HK-47`, `HK-50`, `HK-51`, `T1-LB`, `3C-FD`, `G0-T0` or `B-4D4` is now a **`Verify` fault** in `Loom` |

**⚠ AND THE DESIGNATION VALIDATOR IS DELIBERATELY NARROW.** It refuses a
**reserved** name only. It does **not** enforce the shape rule — no spaces,
alphanumeric plus hyphen — because that is `PT-1726`'s rule for a **player
typing their own designation**, not for authored content. **Your own fixtures
`Droid Target`, `Melee Droid` and `OA Droid` are legal and will stay legal.**
If that reads wrong to you, say so — it is a scope decision, not an oversight,
and the owner has already said widening it is available if wanted.
