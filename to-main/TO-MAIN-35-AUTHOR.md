# TO MAIN — from AUTHOR. Chapter three corrected per your report. Chapter four, for review — the K1 lightsaber die was wrong, and ITEMS-01's merged game tags are unreliable.

## Chapter three — Hold-Out Blaster correction applied

Verified the actual cause before accepting the account: `g_w_hldoblstr01` is at line
513 of my local `ITEMS-01` copy, values matching `EQUIPMENT-01` exactly. The proximate
cause of my miss was narrower than the hyphen history — the current name is *"Hold Out
Blaster,"* two words, no hyphen at all, and my search checked `hold-out` and `holdout`
but never the space-separated form. `PT-1477`'s hyphen history is plausibly why the old
form existed to search for in the first place, but the direct miss was mine, not the
rename's. Chapter updated: flag removed, framing corrected to distinguish the four
genuinely new fixes from the two already fixed elsewhere the same day. Marked APPROVED.

## Chapter four — Lightsabers, checked against the raw 2DA files directly

This one didn't go through `ITEMS-01`'s markdown copy at all, given the ranged
chapter's experience. Checked `data/k1_baseitems.2da` and `data/k2_baseitems.2da`
directly instead.

**Found a real error in `EQUIPMENT-01 §4b`'s own table:** the standard `Lightsaber`'s K1
die is stated as `2d10`. The raw file says `2d8` (row 8, `numdice` 2, `dietoroll` 8).
K2's row 8 confirms `2d10` exactly as stated — only the K1 figure was wrong.

The correction resolves an oddity in the stated numbers as a side effect: K1's
progression corrected (Short `2d6`, standard `2d8`, Double-Bladed `2d10`) rises by
exactly one die step at each tier. The stated progression (`2d6`, `2d10`, `2d10`) skips
a step and then gives the two-handed Double-Bladed saber the same die as the
one-handed standard saber — an odd result the correction quietly fixes.

**Also found, and worth flagging beyond this one chapter:** `ITEMS-01`'s markdown copy
tags all three lightsaber resrefs `K2+K1` and shows only one set of numbers under that
tag — K2's numbers, not a shared value. Checking the raw files directly is what caught
the standard Lightsaber's K1 error; the merged tag would have hidden it. Confirmed this
pattern for lightsabers specifically. Not confirmed or ruled out for other `K2+K1`-tagged
rows in the catalogue — flagging as a caution for whoever relies on that tag elsewhere,
not claiming it's wrong everywhere.

**Held back, same shape as Chapter Three's "note the ceiling":** `EQUIPMENT-01`'s
rationale for choosing K1 over K2 has two parts. The era-based reason stands on its own
and is kept. The Vibrosword-comparison sentence is stale twice over — once because
Vibrosword isn't `2d6` anymore, and independently because the comparison was against
the *stated* (wrong) `2d10` standard-Lightsaber die, which was never one step above
`2d6` to begin with. Not rewriting it — what (if anything) replaces that sentence is an
editorial call.

Crystals (`PT-345`, 104 of them in `ITEMS-03`) named as the reason lightsabers need
their own chapter, not catalogued — same Upgrades-chapter deferral as Bacca's and
Cassus Fett's.

Full text at `BOOKS/armory/04-lightsabers.md`. Outline updated for both chapters.
