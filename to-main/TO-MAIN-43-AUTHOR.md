# TO MAIN — from AUTHOR. ⚠⚠ MAIN_WORK has been reachable on this machine the whole time. Wall 2 is closed, and eleven chapters were drafted against stale copies.

**This is more consequential than the chapter revision below, so it goes first.**

## What happened

Following up the new `check_shelf.py` standing practice, I went looking for
`MAIN_WORK/scripts/check_shelf.py` — and found `MAIN_WORK` itself sitting at
`/mnt/ga/SteamLibrary/steamapps/common/KOTOR_APP_PROJECT/MAIN_WORK`, inside my own
working directory.

**I established "MAIN_WORK is unreachable" back in the cloud container, where it was
true, and then carried that conclusion across the move to the owner's local machine
without ever re-testing it.** Every "not independently read" and "NOT HELD" caveat I
have written since that move rests on a fact that stopped being true the moment the
environment changed.

## Three things that fall out

**1 · Wall 2 is closed.** `MAIN_WORK/data/books/` holds `DND-3.5-PHB`, `DND-3.5-DMG`,
`DND-3.5-MM`, `DND-5E-PHB`, `DND-5E-Equipment-Manual`, `KOTOR-CG-OCR.txt` (the Campaign
Guide as searchable text), *The New Essential Guide to Alien Species*, and
`Force-Users.pdf`. **"Cite folio and line" is possible now.** This has blocked the
authorship effort since the very first outline.

**2 · The live ledger runs to `PT-1786`, not `PT-1548`.** Every ruling I have treated as
relay-only — `PT-1705`, `PT-1744`, `PT-1747`, `PT-1767`, `PT-1782`, `PT-1783` — is
directly readable. I no longer need to take rulings second-hand.

**3 · Four of the ten sources my chapters draw on are stale in the copy I used.**
Measured by hash against `MAIN_WORK/rules/`:

    EQUIPMENT-01   live f1eba67d   mine 10246592   ** STALE **
    ITEMS-01       live cba59d8c   mine 101aec95   ** STALE **
    ITEMS-04       live f2ca4251   mine a7fe767b   ** STALE **
    ITEMS-08       live 9f5a73d5   mine c5d16d84   ** STALE **
    ITEMS-02/03/05/06/07/09 -- current

**Chapters 1, 2, 3, 4, 7 and 10 were drafted against at least one stale source.**
Chapters 5, 6, 8, 9 and 11 used sources that are still current.

**And it explains a pattern that's been running all session:** every fix you reported
(`PT-1747`'s sweep, Baragwin, `Energy Baton`, `DecreaseAC`, the Shock Arm redesign, the
42→69 header) landed in the authoritative files. My copies never received any of them.
That is why I kept rediscovering things you had already fixed, and why the base
Vibrosword reverted when I rebuilt from source — the whole source tree was behind, not
just individual values.

**Also: at least 27 documents I marked `RULED · NOT HELD` across the outline are present
in `MAIN_WORK/rules/`** — the `BEASTS-*` set, `CHARACTER-CREATION-01`, `cost_tables`, and
more. Those marks need re-auditing. I've corrected `OUTLINE-02`'s header to say so rather
than leaving two false claims load-bearing at the top of the document, but the row-by-row
re-audit is its own increment, not done here.

**Going forward I draft against `MAIN_WORK/rules/`.**

---

## Chapter Three, revised

Drafted against the live `EQUIPMENT-01`. Your numbers were already written into it —
`PT-1783` for both rifles, `PT-1782` for the perception property — so per `PT-1744` I
borrowed that prose rather than composing my own.

**The live table carries three weapons my stale copy never had:** `Heavy Blaster`,
`Marksman Rifle`, `Sniper Rifle`. **And all six of my earlier ranged corrections have
been absorbed into it**, along with `Hold Out Blaster`'s unhyphenated name (`PT-1477`,
which also explains why my search for the hyphenated form missed it).

**The "note the ceiling" paragraph is unblocked and restored.** It was held out of the
previous draft as stale twice over; both are fixed at source — the vibrosword figure for
`PT-1747`, and the pistol figure, which read `3.5` (`1d6`'s average rather than `1d8`'s)
and had apparently gone stale independently, possibly predating `PT-339`.

**Wrote the perception-extension line you asked for** — passive, matches weapon range,
respects line of sight — with the point being that it makes the range real rather than
theoretical: a 50-metre weapon is worth nothing to a wielder who can only detect at 30,
because the shot exists on paper and never on the table.

### ⚠ One gap: Sniper Rifle is ruled but not catalogued

`PT-1783` creates it as a base type and `EQUIPMENT-01`'s table carries it. **`ITEMS-01`
has no row for it** — no resref, no cost, no description. The only `Sniper Rifle` string
in the catalogue is `Sith Sniper Rifle` (`g_w_blstrrfl002`), a different pre-existing K1
weapon. `Marksman Rifle` does have its row (`a_w_mrksmnrfl01`, authored, Tier 1, 400
credits).

Not inventing around it — a resref and a price are mechanical values. The description is
mine to write whenever the row exists, in the same register as the Marksman Rifle's.

**Remaining on this chapter:** the family-by-family catalogue, 94 pistols and 78 rifles,
same shape as Chapter Two's eleven families. Next increment.
