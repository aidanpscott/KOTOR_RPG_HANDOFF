# TO MAIN — from AUTHOR. Chapter one, audio rendition. Chapter three, for review — the base table itself was wrong on six rows.

## Chapter one, audio rendition

Requested for the owner's text-to-speech read-aloud. Plain continuous prose, no
tables, no markdown emphasis, no bracketed citations, no symbols — every number kept
exact, nothing rounded or dropped. At `BOOKS/armory/01-weapon-damage-and-defence-formula-audio.md`.
Doesn't replace the reference version; a second rendition for a different purpose.

## Chapter three — Ranged Weapons

Checking this one before borrowing it, per the amendment to `PT-1744` from Chapter
Two's Baragwin thread, found something bigger than a worked-example problem: **six of
`EQUIPMENT-01 §4`'s eleven base-table rows don't match `ITEMS-01`.** Not unique weapons
this time — the base weapons every reader will look up first.

    weapon            EQUIPMENT-01 said        ITEMS-01 confirms
    Disruptor Pistol  1d4, threat 20           1d6, threat 18-20
    Ion Blaster       1d4, threat 20           1d6, threat 20/x3
    Disruptor Rifle   1d6, threat 20           1d10, threat 18-20
    Ion Rifle         1d6, no threat given     1d10, threat 20/x3
    Sonic Rifle       1d6                      1d10
    Blaster Carbine   1d8, threat 19-20        1d12, threat 20/x2

Confirmed against both games' resrefs where both exist (Disruptor Pistol and Blaster
Carbine agree K1-to-K2). Every corrected row is one of the "exotic" ranged types --
disruptor, ion, sonic, carbine. Every row that was already right -- Sonic Pistol,
Blaster Pistol, Blaster Rifle -- is a standard blaster. `EQUIPMENT-01`'s own header
says range was cross-checked against `baseitems.2da`; the damage dice apparently
weren't checked with the same rigor.

Drafted the chapter with the corrected table rather than holding the whole thing --
these aren't identity-ambiguous the way Baragwin was, they're plainly-named resrefs
with a wrong die in the secondary source. Held back two things instead:

One -- `EQUIPMENT-01 §4`'s "note the ceiling" comparison paragraph (blaster-pistol
average vs. a Soldier's Vibrosword swing) is stale twice over: once for `PT-1747`'s die
change, and more significantly for `PT-340` -- the paragraph's whole argument assumes
ranged adds nothing to damage, which hasn't been true since that ruling. Fixing the
numbers without addressing the argument would leave a conclusion the document no
longer supports. That's an editorial call, not arithmetic -- didn't rewrite it
unilaterally.

Two -- `Hold-Out Blaster` doesn't appear under that name or a resref I could identify
anywhere in `ITEMS-01`. Flagged the same way Baragwin was before its identity resolved
-- kept at the stated value, not dropped, not guessed at.

Also noted: `Cassus Fett's Heavy Pistol` carries the same four-resref feat-conditional
structure Bacca's Ceremonial Blade did. Same treatment -- deferred to the Upgrades
chapter, not unpacked here.

Full text at `BOOKS/armory/03-ranged-weapons.md`. Outline updated.
