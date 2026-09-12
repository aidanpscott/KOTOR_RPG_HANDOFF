# Armory — Editorial Notes

**⚠ NOT PART OF THE BOOK. Internal record, for MAIN, Coder and the owner.**

**This file exists because of `PT-1844`**, and mirrors `BOOKS/timeline/EDITORIAL-NOTES.md`.
The chapters used to carry their findings in an *"Open items, carried from review"* section
citing internal documents and ruling numbers a reader cannot look up. **Those sections are
moved here as each chapter is passed — preserved, not deleted.**

---

# Chapter One — Weapon Damage and the Defence Formula

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED by MAIN**, checked against `EQUIPMENT-01` and
`ACTION-ECONOMY-01` directly. **Sources it stood on:** `EQUIPMENT-01 §1` (melee damage),
`EQUIPMENT-01` with `PT-340` (ranged adds Dexterity), `PT-1` (the provisional lightsaber
line), `PT-341` (the Massive Criticals cap), `PT-339`.

**`ATTACKS-01`'s ranged-damage line is stale against `EQUIPMENT-01`'s own `PT-340`
amendment** — reported at `TO-MAIN-30-AUTHOR.md`, not fixed here. This chapter draws its
ranged-damage value from `EQUIPMENT-01` directly, which already has it right.

**The lightsaber-damage-ability line is provisional in its own source (`PT-1`).** Carried
through as a flag rather than smoothed into a stated fact.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 8 internal citations**, including the whole *Source* column of the damage
table.

**⚠ The damage table's source column could not be handled by the approved rule alone**, and
this is the first Armory exception worth recording. **The rule is "attribute to the game's
own data rather than the internal ruling" — but the four rows are not the same kind of
claim:**

- **Melee one- and two-handed** are straightforward extracted values.
- **Ranged adding Dexterity** is a d20 convention rather than something the games state.
- **The lightsaber line is explicitly provisional** — a reading of an ambiguous source.
- **The Massive Criticals cap is a deliberate departure** from the games, which leave it
  uncapped.

**Blanket-attributing all four to "the game's own data" would have been false for three of
them.** So the column was dropped and **provenance is now stated in prose exactly where it
differs from the games** — which is the `⚠ AUTHORED` discipline the Armory already uses,
turned reader-facing.

**The lightsaber warning is stated more strongly than before, not less.** It now says
plainly that this is **this game's reading of an ambiguous source**, that the source calls
lightsabers *"not melee weapons"* about upgrades and criticals rather than damage, and that
**being wrong is worth roughly ±3 damage on every hit a Jedi lands.**

**The Massive Criticals cap now says outright that it is a departure** — *"one of the few
places where this book knowingly differs from its source rather than reporting it"* — which
the old text conveyed only through a ruling number.

**⚠ And a self-caught over-removal.** My first pass at the armour restrictions dropped the
names **`Soresu`** and **`Well Guarded`**, treating them as internal jargon. **They are not
— they are a lightsaber form and a class feature, both real in-game things a reader can look
up in the Player's Handbook.** The audio rendition of this chapter still named them, which
is how the loss was spotted. **Restored, and the passage is now stronger than either
version:** the restriction decides what kind of defence a character can build.

**✔ The audio rendition needed no pass.** `01-weapon-damage-and-defence-formula-audio.md`
was written as continuous prose for a text-to-speech reader and **carries zero internal
citations already** — checked, not assumed. It remains substantively consistent with the
revised chapter.

**⚠ Deliberately NOT loosened.** Every value survives: the three damage formulas, the six
wield classes and their pairing rules, threat ranges and multipliers, the `2d6` cap, the
sum-of-9 armour rule with both organic exceptions, the uncapped-robe rule and the Jedi
Defence-12 example, and both droid plating tables with K2's uncapped sentinel.

---

# Chapter Two — Melee Weapons

*`PT-1844` pass. This chapter had no "Open items" section of the usual shape; what it
carried instead was a work-tracking section on an incomplete sweep, reproduced here.*

**Chapter status: DRAFT, full-catalogue standard applied.** Eleven families, 62 entries.
**Scope rule:** `PT-342`'s K1-overrides-on-shared-items applied where a genuine difference
appears.

## ⚠ Four weapons still carrying the pre-`PT-1747` Vibrosword die

`PT-1747` moved Vibrosword from `2d6` to `1d12`. The sweep covered the nine
`vbroswrd`-stemmed resrefs. **Four more melee weapons still read `2d6, 19–20 ×2` — the
exact pre-ruling Vibrosword signature — and none of them carry that stem, which is why a
stem-matched sweep would pass over them:**

| Weapon | Resref | Confidence |
|---|---|---|
| **Vibrosword** (K2's own) | `w_melee_06` | **Certain** — same weapon, same name, same 120-credit price as K1's |
| **Echani Vibrosword** | `w_melee_21` | **Certain** — names the family |
| **Sith Tremor Sword** (K2's) | `w_melee_22` | **Certain** — direct counterpart of K1's `g_w_vbroswrd03` |
| **GenoHaradan Poison Blade** | `geno_blade` | **⚠ Suspected only** — die and threat match exactly, but the name doesn't say Vibrosword and `BaseItem` could not be read from this copy |

**⚠ UPDATE — three of these four are now fixed at source.** `w_melee_06`, `w_melee_21` and
`w_melee_22` all read `1d12` in the live `ITEMS-01`. **`GenoHaradan Poison Blade` was not
changed and still reads `2d6`** — so either it genuinely isn't a Vibrosword-family weapon,
or it is a fifth miss. **Settling it needs a `BaseItem` read rather than a die-signature
match.**

**Two resref-versus-base-type disagreements worth noting for whoever runs that check:**
`Raito's Gaderffii` sits at `g_w_qtrstaff03` while carrying the Gaffi Stick's `1d8` die,
and `Baragwin Assault Blade` sits at `g1_w_vbroswrd01` with a `g1_` prefix no other weapon
in the family uses. **Resref stem is not a reliable proxy for base weapon type in either
direction** — the same lesson the `Energy Baton` resolution taught from the opposite side.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 5 internal citations**, and one whole section.

**⚠ The proper-noun check was run deliberately this time, and it changed the outcome.**
Following the `Soresu` lesson from Chapter One, every code-formatted term was checked
rather than pattern-matched. **The resrefs stayed** — all 92 of them. **They are the games'
own item identifiers, not internal project references, and a reader can look them up in the
game files.** Stripping them would have destroyed the catalogue's usefulness.

**The Vibrosword sweep section moved here in full.** It was work-tracking — a ruling
number, a sweep's coverage, confidence ratings and what has since been fixed at source.
**None of it is reader content.**

**⚠ But it left a real residue, and that stayed in the chapter.** The `GenoHaradan Poison
Blade`'s die is genuinely unsettled, and a reader using that weapon needs to know. **The
note is now self-contained rather than pointing at a section that no longer exists:** it
reads `2d6` where its family reads `1d12`, it may belong to a different family than its
damage suggests, **and a Gamemaster is told to treat `1d12` as the working value with `2d6`
as a defensible reading.** That is more useful than the cross-reference was.

**⚠ And a dangling reference caught mid-pass.** Removing the sweep section orphaned the
GenoHaradan entry's *"see the note at the top of this chapter"* — **the same failure mode
caught in the Timeline's Chapter Three.** Found by re-reading the entry after the removal
rather than by trusting the edit.

**The tail section became a caution on item codes**, which is the reader-facing half of the
resref finding: **the code is the games' own identifier and is not a reliable guide to what
kind of weapon something is. Read the family heading, not the code.**

**⚠ Deliberately NOT loosened.** All 11 families, all 62 entries, every die, threat range,
price and property line survives. **The K1-over-K2 rule is stated in reader terms rather
than by ruling number, and the one place a genuine divergence is called out — the Sith
Tremor Sword's sonic value — still names both figures.**

---

# Chapter Three — Ranged Weapons

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: catalogue complete, 122 items across 14 families.** Base table drafted
against `MAIN_WORK/rules/`. **Rulings it stood on:** `PT-1783` (the two long rifles),
`PT-1782` (the perception extension), `PT-1477` (the Hold Out Blaster name), `PT-1473`,
`PT-345` (crystals), `PT-1747`/`PT-339`/`PT-340` (the ceiling comparison), `PT-1825` /
commit `f408708` (the ×3 revert).

**✔ The family catalogue is complete** — 122 items across fourteen families, replacing the
placeholder this section previously carried.

**✔ Flag 1 — the ruled corrections have landed, and this catalogue matches the corrected
file exactly.** The owner ruled that **K2's dice stand**, with two exceptions: **Blaster
Carbine's threat moves to 19–20** (die stays `1d12`) and **Ion Blaster and Ion Rifle revert
from ×3 to ×2**. `EQUIPMENT-01` now carries all three.

**Re-verified after the sync:** of this catalogue's 122 entries, **zero are absent from the
corrected file, zero changed stat line, and zero real rows are missing from the
catalogue.** The membership capture held.

**✔ The ×3 revert is now complete** (`PT-1825`, commit `f408708`) — **all nine ion variant
rows and all six Bowcaster rows corrected to ×2.** Verified by reading the file at that
commit directly: **the only ×3 rows remaining are the seven nameless `prop*` placeholders**,
which this catalogue already excludes. **The Bowcaster was extended into scope on the
reasoning that ×3 is unsupported by either game's raw data** — K1's `Bowcaster` base row
carries `crithitmult` 2 — **which is the same reasoning the ion revert rested on.**

*Recorded for the history, since the flag-resolution convention keeps what was raised:* the
nine ion variants were —

    Ion Blaster   w_blaste_10   Aratech Droid Oxidizer
                  w_blaste_21   Aratech Ionmaster
    Ion Rifle     g_w_ionrfl02  Bothan Droid Disruptor
                  g_w_ionrfl03  Verpine Droid Disruptor
                  w_brifle_02   Ion Carbine
                  w_brifle_15   Bothan Droid Disruptor
                  w_brifle_20   Verpine Droid Disruptor
                  w_brifle_29   Verpine Droid Disintegrator
                  g1_w_ionrfl01 (the corrupted-name row, Flag 4)

— **all now ×2**, along with the six Bowcaster rows.

**The family headings above state ×2 throughout and always did**, so nothing in this
catalogue changed when the fix landed.

**⚠ Flag 2 — `ITEMS-01`'s ion rows are internally inconsistent, which is how this was
caught.** Two base Ion Rifles (`g_w_ionrfl01`, `w_brifle_07`) already read ×2 while their
own variants read ×3. **That inconsistency is corroboration for the ruled ×2**, and it is
why Ion and Sonic rifles cannot be separated by stat line alone once the fix lands — both
become `1d10, 20 ×2`. **Damage type is the discriminator, and it is recorded per entry.**

**⚠ Flag 3 — 30 of 122 descriptions are truncated mid-sentence in `ITEMS-01`**, several at
identical points — the disruptor description cuts at *"disruptors igno"* in three separate
items. **This is an extraction defect, not a source one:** a character limit applied during
extraction. **Each affected entry is marked in place** rather than completed by invention.
**A re-extraction would fix all thirty at once.**

**⚠ Flag 4 — a fourth instance of the corrupted Name-field pattern.** `g1_w_ionrfl01` is an
ion rifle whose Name field reads **`Mastercraft: Armor II`** — an armour upgrade's name on
a weapon's resref. **Left unnamed in the catalogue rather than given an invented one.**
Same shape as the Baragwin, Weapon Master and spike-mount cases.

**⚠ Flag 5 — `Sniper Rifle` and `Marksman Rifle` have one entry each**, both `⚠ AUTHORED`
(`a_w_snprrfl01`, `a_w_mrksmnrfl01`). **They are the only families here with no extracted
members**, which is expected — both were added by ruling (`PT-1473`, `PT-1783`) and no game
item carries them.

**Closed from the earlier draft:** `Hold Out Blaster`'s naming flag (`PT-1477`) and the
Sniper Rifle catalogue gap, both resolved above.

`Hold Out Blaster`'s earlier "could not be confirmed" flag is closed; `PT-1477` explains
both why it existed and why searching for the hyphenated form missed it.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 10 internal citations from the body**, plus the five-flag section. **The
catalogue itself was almost untouched:** 124 entries, 14 family headings and all 29
truncation markers survive unchanged.

**⚠ The `⚠ AUTHORED` marking became the chapter's most important rewrite.** The Sniper
Rifle and Marksman Rifle section was headed *"Sniper Rifle — ruled, and now catalogued"*
and described a gap being closed. **A reader does not know there was a gap.** The section is
now headed **"The two rifles this game added"** and opens by saying plainly that **neither
weapon exists in either game** and both were written for this book. **That is the
ours-versus-extracted discipline stated where a reader meets it**, rather than signalled by
a ruling number.

**The price caveat became advice rather than a note to ourselves.** It read *"open to a
second look if it doesn't sit right in play."* It now says the 800 credits is **"the kind
of number a table should feel free to adjust."**

**⚠ The ceiling paragraph lost a stale-value confession it should never have carried.** Two
sentences explained that the figures had previously been wrong, why, and which rulings
fixed them. **A reader needs the comparison, not its repair history.** What replaced it is
a fact the old paragraph only implied: **ranged weapons add Dexterity, so the gap closes
for a character built that way — but it closes by the shooter's ability, not the weapon's.**

**The corrupted-name entry now warns a reader rather than counting instances.** It said
*"fourth instance of the corrupted-Name pattern."* It now says **this item has no usable
name**, its name field holds an armour upgrade's name, **the weapon is real and the name is
not.**

**✔ Resrefs kept throughout**, per Chapter Two's finding, and the families note now points
at Chapter Two's caution rather than restating the resref lesson.

**✔ The standing orphan check was run** after every removal — the new step adopted in
Chapter Two. **Zero dangling cross-references.** The `KillBlaster`'s crystal note was the
one at risk; it cited a crystal ruling and now points at Chapter Six, which is where
crystals are actually catalogued.

**⚠ Deliberately NOT loosened.** All 14 base weapons keep their dice, threat ranges and
ranges; both long rifles keep their full treatment including the perception extension's
three properties; the 122-item catalogue is untouched; and **the 50 excluded entries are
still listed with the reason for each exclusion.**

---

# Chapter Four — Lightsabers

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: DRAFT.** Split from the combined melee/ranged/lightsabers chapter per
MAIN's ruling. **Base table checked against the raw `.2da` files directly** —
`data/k1_baseitems.2da`, `data/k2_baseitems.2da` — **not `ITEMS-01`'s markdown copy**,
whose merged `K2+K1` tag masks the two games' different values for these three weapons.
**Rulings:** `PT-1472` (training sabers take crystals), `PT-345` (the crystal subsystem),
`PT-1747` (the stale Vibrosword comparison).

**⚠ The `K2+K1` tagging finding, in its internal form:** `ITEMS-01` tags all three
lightsaber resrefs `K2+K1` and shows **only K2's numbers** under that combined tag
(`2d8`/`2d10`/`2d12`). **A `K2+K1` tag in that catalogue does not mean the two games share
a value — it can mean the extraction recorded only one game's number for a resref present
in both.** Confirmed for lightsabers against the raw `.2da`; **not confirmed or ruled out
for anything else tagged the same way.**

**⚠ The stale rationale, recorded because it was deliberately not rewritten in the
chapter:** `EQUIPMENT-01 §4b`'s reason for preferring K1's dice had two parts. *"Our
campaign is 3956 BBY and K1 is the era"* stands. *"A Vibrosword is `2d6`, so a K1
lightsaber sits exactly one die step above it"* **is stale twice over** — Vibrosword is
`1d12` since `PT-1747`, and even before that the comparison ran against the *wrong*
standard-Lightsaber die of `2d10`, which was never one step above `2d6`. **The `PT-1844`
pass removed the sentence from the chapter entirely rather than repairing it**, since the
era reason carries the choice alone.

The lightsaber-damage-ability flag from Chapters One through Three — genuinely this
chapter's own subject now, not just carried for continuity. `EQUIPMENT-01 §4b` itself
raises the same caveat independently: *"lightsabers are not melee weapons,"* a
statement the source makes about upgrades and criticals rather than damage, which is
exactly why treating lightsabers as melee-for-damage is a working assumption rather
than a confirmed rule. Two independent paths to the same open question, not two
separate ones.

New this chapter: the K1/K2 rationale paragraph (editorial), and the `K2+K1` tagging
caution above, which isn't this chapter's to resolve but felt worth surfacing where it
was found.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 12 internal citations from 103 lines**, the densest concentration in the Armory
so far.

**⚠ The raw-file citation survived, exactly as predicted, and it reads well.** The die
correction is the chapter's centrepiece, and the approved method says a citation to the
games' own data stays. **It does — but the framing changed from a document-versus-document
dispute into a warning a reader can use:**

> **You will find the standard Lightsaber's K1 die quoted elsewhere as `2d10`. It is
> `2d8`.** The figure above was read out of KOTOR 1's own weapon table — row 8, label
> `Lightsaber`, two dice of eight — **not from any summary of it.**

**The internal document that had it wrong is gone; the game table that has it right
stayed.** That is the method working as intended.

**⚠ The `K2+K1` methodological note became a reader caution**, and this is the pass's best
gain here. It was a warning to whoever next reads the item catalogue. **It is now a warning
to whoever next builds a character:** where a weapon appears in both games it is easy to
assume both give it the same numbers, these three prove otherwise, and **a summary listing
a weapon once without saying which game it quotes will silently give you one game's value
for both.** Ending with: **if a weapon matters to your table and appears in both games,
check both.**

**⚠ The Training Lightsaber got the authored-marking treatment** approved at Chapter Three.
It read *"a fourth entry, authored rather than extracted"* — accurate and meaningless to a
reader. **It now opens: this weapon does not exist in either game; it was written for this
book.**

**And its unsettled threat range became advice.** The old text named the two documents that
disagreed and declined to choose. **The chapter still declines — but now tells a Gamemaster
that `20` is the safer ruling**, which is what the old note's own reasoning implied and
never said.

**⚠ Deliberately NOT loosened.** Both games' dice for all three lightsabers survive, the
K1-versus-K2 table is intact, the die-progression argument is unchanged, all three training
sabers keep their dice, and the crystal subsystem still points at Chapter Six with Rubat and
the 104-crystal count.

---

# Chapter Five — Armour

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED.** Source is `ITEMS-02` — **already the primary-source
catalogue**, converted from the game files under `PT-339` (dice), `PT-341` (Massive
Criticals), `PT-308` (tiers), `PT-327` (unique), `PT-345` (crystals), `PT-349`
(Upgradeable) and `PT-384` (the feat remap). **It did not need the cross-check against a
more primary source that caught real errors in Chapters Two through Four — it largely *is*
that source.** `PT-980` priced the Dark Padawan Robe down from 900 to 700.

Same lightsaber-damage flag, unaffected by this chapter. `DecreaseAC` closed above —
confirmed, not a real gap. Still worth stating plainly: this chapter samples five of
173 items rather than auditing the full catalogue line by line, the way
the eleven-row weapon tables in Chapters Two through Four could be. A category count
and a representative sample is the right grain for a browsable-reference chapter; a
full 173-item transcription would belong to `ITEMS-02` itself, not to prose built on
top of it.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 11 internal citations from 71 lines**, almost all of them in a single opening
paragraph that existed to explain this chapter's provenance to a colleague.

**⚠ That paragraph is the clearest example yet of a citation load with a real point buried
in it.** It listed seven ruling numbers and two document names to say that this chapter's
source *"largely is"* the primary source rather than a summary of one. **A reader cannot
use any of that — but the conclusion matters to them, because it tells them how far to
trust the numbers.** It now reads:

> **One difference worth knowing, because it affects how much to trust these numbers.** The
> armour figures in this chapter were converted straight from the games' own item files.
> **They did not pass through a summary first**, which is where the errors corrected in
> Chapters Two, Three and Four came from.

**Same claim, and it now earns its place** by telling a reader why this chapter is less
likely to be wrong than the three before it.

**⚠ The `DecreaseAC` explanation kept its game-data citations and lost its method
narration.** The two `.2da` file names stayed on the approved rule — they are the games'
own tables — **but the passage no longer walks through the resolution as a procedure.** It
gives the worked example (`Light Combat Suit`: base armour 4, cap +5, penalty applies to the
armour component, **true protection `+3` with the full `+5` cap kept**) and then states the
general rule in one sentence.

**⚠ The Dark Padawan Robe repricing got the authored-marking treatment.** It read *"an owner
ruling rather than an oversight… by ruling."* **A reader does not know what an owner ruling
is.** It now says plainly: **one price in this chapter is deliberately not the games' own**,
because two items that do exactly the same thing now cost the same. **That is this game
changing something on purpose, and a reader is told so.**

**⚠⚠ A content gap noticed during the pass and NOT addressed by it.** **This chapter
samples five of 173 items** where Chapters Two and Three carry full catalogues.

**✔ RULED — `PT-1770` already required this, retroactively.** MAIN checked: the
full-catalogue standard was not a convention Chapter Five was written before, it was **an
explicitly retroactive rule that already governed this chapter and was never enforced on
it.** So this is compliance, not a new decision.

**⚠⚠ OUTSTANDING TASK — expand Chapter Five to the full 173-item catalogue**, matching
Chapters Two and Three: six categories, Base/Advanced where it applies, ordered by tier.

**Sequenced AFTER the `PT-1844` sweep completes, by AUTHOR's call, for a practical
reason:** writing the 173 entries fresh means **they are born compliant with both standards
at once.** Expanding first would produce 173 entries that then need a de-jargoning pass of
their own — the same work twice. **Recorded here so it cannot be lost between tasks.**

**⚠ Deliberately NOT loosened.** All six category counts, the 173 total, the nine
both-games items, every representative entry with its armour value, the Dark Padawan Robe's
two prices, and the `DecreaseAC` worked example's exact figures all survive.

---

# Chapter Six — Upgrades and the Upgrade Tree

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: DRAFT.** Sources `ITEMS-03` (164 items) and `ITEMS-09` (118 rows, *"the
upgrade tree"*, refiled at `PT-781` from material originally scattered across the `plot`,
`device`, `sensor`, `clothing` and `creature` categories). `PT-345` governs crystals.

Same lightsaber-damage flag as every chapter so far. New here: the deferred
unique-weapon mechanic is explained rather than mechanically resolved, and how common
its four-resref shape is across the rest of the catalogue is an open, unscoped
question rather than a closed one.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 7 internal citations from 96 lines.** Four were section headings that carried a
source document's name as a subtitle, which told a reader nothing and made the contents page
unreadable.

**The unique-weapon survey question became a reader-facing caveat.** It read as a scoping
note about what *"hasn't been budgeted for."* It now tells a reader what to do with the
uncertainty: **treat the pattern as demonstrated for the two weapons named and unproven
elsewhere.**

**⚠ And the pass caught an inaccuracy I introduced myself, two chapters ago.** Chapter
Four's crystal pointer — written during this task's Chapter Four pass — said **"Chapter Six
catalogues 104 crystals."** **It does not catalogue them. It describes them.** Corrected to
*"covers"*. **The forward-reference check exists for exactly this, and it caught a false
claim of my own making rather than an inherited one.**

## ⚠⚠ And the pass measured the real scope of the `PT-1770` gap

**Chapter Five is not an isolated case.** Counting catalogue entries against claimed item
totals across every item chapter:

| Chapter | Entries present | Items claimed |
|---|---|---|
| Two — melee weapons | **62** | complete |
| Three — ranged weapons | **124** | complete |
| **Five — armour** | **0** | **173** |
| **Six — upgrades** | **0** | **164** + 118 rows |
| **Seven — droid equipment** | **0** | **135** |
| **Eight — worn gear** | **0** | **241** |
| **Nine — usable items** | **0** | **58** |
| **Ten — quest and miscellaneous** | **0** | **20** |

**Six chapters carry a category table and a handful of representative entries instead of a
catalogue. Roughly 791 items are uncatalogued.**

**Verified by inspection, not by pattern-match** — Chapters Eight and Nine were opened
directly to confirm they use the same category-table-plus-sample shape as Chapter Five
rather than a format the entry count was failing to recognise.

### ✔ RULED — the catalogue-completion task, scoped and sequenced

**All six chapters get full catalogues. No exceptions carved out for the smaller ones**,
and none for the larger. `PT-1770` was already decided; the size of the gap is a
sequencing question, not a reason to revisit whether the rule applies.

**Sequenced after `PT-1844` completes across all sixteen chapters**, not interleaved — so
every new entry is born compliant with both standards and nothing is written twice.

**Order within the task: smallest first**, for momentum, the same shape the original
sixteen chapters were written in:

    1.  Ten — quest and miscellaneous        20 items
    2.  Nine — usable items                  58 items
    3.  Seven — droid equipment             135 items
    4.  Six — upgrades                      164 items + 118 rows
    5.  Five — armour                       173 items
    6.  Eight — worn gear                   241 items

**~791 items total.** Comparable in size to writing the Armory's sixteen chapters in the
first place.

---

# Chapter Seven — Droid Equipment

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED.** Source `ITEMS-04`, a primary-source catalogue on the same
footing as `ITEMS-02` and `ITEMS-03` — no cross-check against a more-primary source needed,
unlike Chapters Two through Four.

Same lightsaber-damage flag, unaffected. The four-way split proposal above was
approved and the other three chapters are drafted.

**The `spike-mount` corrupted-Name row is resolved.** It is `Advanced Droid Interface`
(`g1_i_drdcomspk01`, Tier 3, 9,000 credits), gated behind `Droid Upgrade 3` and granting
skill 7 in Awareness, Computer Use, Demolitions and Security — *"a self-contained
artificial intelligence system... to provide them with additional resources useful in
the bypassing of computer and conventional"* security. The four skill bonuses, which had
also been showing as unmapped subtypes, resolve cleanly and match the item's own flavour
text. Third instance of that corruption pattern, and the third to resolve the same
way — by reading the raw file rather than the markdown copy.

## ⚠ The stale scoping proposal, removed from the chapter

**This section sat in the chapter as an open question when it had already been answered.**
It proposed splitting a combined outline row into four chapters and closed with *"not
drafting the other three until this is confirmed"* — while the flags directly beneath it
recorded **"the four-way split proposal above was approved and the other three chapters are
drafted."**

**That is `PT-961`'s shape in this project's own book**: a resolved proposal left standing
as though still pending, with its own resolution sitting twenty lines below it. **The fifth
instance of that pattern found during this work, and the first in something I wrote.**

Preserved in full:

## A scoping proposal, not yet decided

**The outline currently bundles `ITEMS-04` through `08` — droid equipment, worn gear,
usable items, and quest/miscellaneous items — into one chapter.** Having looked at all
five, they aren't one category the way Armour's sub-categories were:

- **Droid equipment** (this chapter) — its own coherent, thematically distinct set.
- **Worn gear** (`ITEMS-05`, 241 items — belts, forearms, gauntlets, implants, masks) —
  the single largest catalogue after weapons, and mechanically its own thing: passive
  body-slot gear, not weapons or armour.
- **Usable items** (`ITEMS-06`, 58 — adrenals, medical, trap kits) — active consumables,
  a different kind of object entirely from anything worn or equipped.
- **Quest and miscellaneous items** (`ITEMS-07` + `ITEMS-08`, roughly 60 combined) —
  both small enough to share one chapter, and both are genuinely miscellaneous rather
  than a coherent category in their own right.

**Proposing four chapters rather than one**, same reasoning as the Melee/Ranged/
Lightsabers split — different mechanical shapes, and a single chapter covering all
five `ITEMS` files' combined ~500 items would strain this book's own browsable-
reference identity. Not drafting the other three until this is confirmed.

---

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 6 internal citations, and the stale proposal section above**, which was a third
of the chapter's length.

**The opening now says what the chapter is for rather than how it came to exist.** It
explained its own split from an outline row and named three source documents. It now opens:
**droids do not wear armour and cannot use most of what Chapters Two through Six catalogue,
and this chapter is what they get instead.**

**⚠ Removing the flags orphaned a live cross-reference, caught by the standing check.** The
category table's Spike-mount row pointed *"see below"* at a detail that lived only in the
flags. **That detail is genuinely reader-facing** — the best item in the category is
effectively unfindable by name.

**So it was restored into the chapter as its own section** rather than moved out: the
**Advanced Droid Interface**, `g1_i_drdcomspk01`, Tier 3, 9,000 credits, `Droid Upgrade 3`,
granting skill 7 in Awareness, Computer Use, Demolitions and Security — **with the practical
warning a reader needs: if you search the game files for this item by name you will not
find it, so search by code.**

**What stayed in the notes is the part that was never reader-facing:** that this is the
third instance of the corrupted-Name pattern, and that it resolved the same way as the
others — by reading the raw file rather than a markdown copy.

**⚠ Deliberately NOT loosened.** All eight categories and their counts survive, both
representative-entry tables are intact including the `Droid Desh Plating` `DecreaseAC`
cross-reference to Chapter Five, and the Advanced Droid Interface's full specification is
now in the book rather than in a footnote about it.

---

# Chapter Eight — Worn Gear

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED.** One of four chapters split out from a combined outline row.
Source `ITEMS-05`, a primary-source catalogue on the same footing as Chapters Five through
Seven.

Same lightsaber-damage flag, unaffected. Same unmapped-subtype question as above,
explicitly deferred rather than picked at piecemeal. Two categories (Belt beyond the
one sample, Gauntlets and Implant beyond their authored examples) not deeply sampled —
the same browsable-reference grain as Chapter Five's five-of-173, applied here to a
larger catalogue.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 6 internal citations from 62 lines.**

**⚠ The authored-item section got the Chapter Three treatment, and it was the most
important change here** — this is one of only two chapters that mix invented items in with
extracted ones.

It was headed *"Two of these categories mix original content in with the games' own items"*
and explained the `⚠ AUTHORED` mark by describing **the provenance discipline** — *"every
asset declares whether it's ours or extracted, and nothing ships without that
declaration."* **That is a statement about how this project works, offered to someone who
does not know this project exists.**

It is now headed **"Two items in this chapter do not exist in either game"** and says what
the mark means in use: **an invented item should never sit beside an extracted one as though
the two came from the same place**, and where you see the mark, **the item is this game's
own work rather than BioWare's or Obsidian's.**

**⚠ The unmapped-skill-subtype section was rewritten from a scoping note into a table
ruling.** It previously explained why the author was *not* resolving these — that it belongs
to a commissioned pass, and that duplicating effort would waste a slice. **All true, and all
addressed to a colleague.**

**A reader needs something else entirely: what to do when they meet one.** The section now
explains that the entry records a bonus and its size **but not which skill**, that it is a
known and separately-tracked problem, and that **until it is fixed a Gamemaster should
assign the bonus to whichever skill the item's description and slot most plausibly
support** — with `Safety Harness` named as the clearest example.

**⚠ Two directional errors caught by the standing checks**, one inherited and one mine.
The Forearm category compared itself to `ITEMS-04`'s droid shields; **it now points at
Chapter Seven**, where a reader can actually look. And my own rewrite said `Safety Harness`
was *"in the sample below"* **when the table sits above that section** — the same class of
error as the Timeline's Chapter Three *"Ossus below"*. **Third time a directional reference
has gone wrong in this task, and the third time the check caught it rather than luck.**

**⚠ Deliberately NOT loosened.** All five categories and their counts survive, both authored
items keep their full specifications, and the representative-entry table is unchanged.

---

# Chapter Nine — Usable Items

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED.** Second of four chapters split from a combined outline row.
Source `ITEMS-06`. **Medpac values are `PT-1` B3's deliberate replacement of the source
game's WIS/skill-scaled mechanic.**

Same lightsaber-damage flag, unaffected. Same unmapped-subtype deferral as Chapter
Eight — none of this chapter's own categories happened to carry one, but the
commissioned pass (once run) may still touch entries here.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 6 internal citations from 59 lines.**

**⚠ The medical section got the Chapter One treatment**, as the second of only two places
in the Armory where a value is knowingly not the source's own.

It was headed *"Medical — where a ruling deliberately replaces the source mechanic"* and
opened by explaining that this is *"not a contradiction to resolve"* — **which is an answer
to a question only someone auditing the corpus would ask.** A reader meeting different
numbers in the games does not think *contradiction*; they think **which one is right.**

It is now headed **"Medical items — where this game knowingly differs from the games"** and
opens by telling them directly: **you will find different numbers in the games, and the
difference is on purpose.** The comparison table's columns changed from *"Source game's own
mechanic / This game's ruling"* to **"What the games do / What this game does"**, which is
the same distinction without the word *ruling*.

**⚠ And the proportionality argument was kept in full, because it is the part that
justifies the change.** The games triple both base healing and the skill multiplier from
Medpac to Life Support Pack; **this game triples the average healing across the same three
items.** Different mechanic, same shape. **That reasoning is why the replacement is
defensible rather than arbitrary, and a reader deserves it.**

**Closed with the line the section was always making and never said:** *a medpac is a
medpac — in this game, who hands it to you does not change what it does.*

**Two smaller fixes.** The `Components` row pointed at the crafting rules by document name;
**it now points at Chapter Twelve**, where those rules actually live in this book. And the
`Antidote Kit` / `Squad Recovery Stim` paragraph described them by reference to *"the
earlier medpac ruling"* — **it now simply says they sit outside the three tiers**, with the
Squad Recovery Stim correctly characterised as **a different kind of thing rather than a
stronger medpac.**

**⚠ Deliberately NOT loosened.** All six categories and counts survive, the 30-item
cross-game overlap is kept, all three medpac tiers keep both the games' formula and this
game's dice, and the tripling argument is unchanged.

---

# Chapter Ten — Quest and Miscellaneous Items

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

**Chapter status: APPROVED.** Last of four chapters split from a combined outline row.
Sources `ITEMS-07` (quest) and `ITEMS-08` (other). **Authored content:** `Shock-arm`
(`PT-713`, `PT-712`, `PT-714`) and `Boots` (`PT-690`).

Same lightsaber-damage flag, unaffected. The category-count question and the
Shock-arm design are both closed above. Still open: the cross-reference worth someone
picking up later — Pazaak's cards exist here while its rules chapter is still
unplaced in Book Five.

## ⚠ The two count-correction histories, removed from the chapter

**Both were internal and both are preserved here.**

**Quest items:** the header once read **"154 items"**. `PT-781` moved 134 upgrade rows out
of the `plot` category into `ITEMS-09` — dropping `plot` from 147 to 13 — **and the header
was not updated until `PT-871` caught it.** True count: **20.**

**Miscellaneous items:** the file stated **42 items against a five-category sum of 69**.
**The header was wrong, not the arithmetic** — corrected to 69, matching the sum exactly.
**The same stale-header shape the quest catalogue had already shown**, in the same file
family.

**Also removed: the shock arm's redesign history** — that a free, auto-upgrading
T3-M4-unique version existed and was deleted, leaving one purchasable line at two price
points. **A reader needs the design that exists, not the one that did not survive.**

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 9 internal citations and two correction histories**, the heaviest combination
in the Armory.

**⚠ The authored section is the strongest ours-versus-extracted case in the book, and it
now reads like it.** It was headed *"Two of these five categories are original content, not
extracted from either game"* — accurate, and phrased in the project's internal vocabulary.

It is now **"Two categories here do not exist in either game"**, opening: **this is the
furthest this book goes beyond its source.**

**⚠ And the Boots justification became checkable rather than asserted.** It cited the ruling
and named the game's equipment table. **The table is game data and stayed** — but the claim
is now framed as something a reader can verify: **"That is not an oversight on this book's
part — it is verifiable in the games' own equipment table, which covers implant, head,
armour, hands, arms, weapons and belt, and nothing below the waist."**

**The shock arm's three consequences were pulled out of a citation-dense paragraph into
plain statements:** it occupies no weapon slot, cannot be disarmed, dropped or sold, and a
droid may still carry a blaster. **And the reason that matters — it is chassis hardware, the
same category a beast's claws belong to, so it never passes through the wield classes —
now also explains why droids being barred from melee weapons does not bar them from this.**
**That last connection was implicit in a ruling number and is now stated.**

**The pazaak note became a Gamemaster's instruction.** It described a rules chapter as
`UNPLACED` in another book. **It now says the cards are catalogued regardless, and a
Gamemaster who wants to run a hand has the props and will need to supply the game.**

**⚠ Deliberately NOT loosened.** Both authored categories keep their full specifications
including prices, dice and gating; all five miscellaneous categories and their counts
survive; and the quest-item categories are unchanged.

---

# Chapter Eleven — Tiers, Pricing, and Availability

*`PT-1844` pass. **This chapter was rewritten rather than edited**, because more of it was
addressed to the project than to a reader. The removed material is preserved below.*

**Chapter status: DRAFT.** Rulings: `PT-308` (loot tiers), `PT-327` (unique items),
`PT-384` (the feat remap, confirming `PT-352` was applied). Currency is
`STARTING-EQUIPMENT-01`, **not** `D-CURRENCY-01`.

## ⚠ The `D-CURRENCY-01` miscitation — removed from the chapter, still outstanding at the outline level

## ⚠ `D-CURRENCY-01` was miscited from the start — not this chapter's fault to fix quietly

**The outline's own row for this chapter, and separately Book Seven's Planetary Atlas
row for "currency and trade," both cite `D-CURRENCY-01` as the source. It isn't.**
Read the actual document: 217 lines, entirely about *which Atlas world-record source
governs* — a corpus-authority ruling for the Planetary Atlas's own data, unrelated to
in-game currency. The word "currency" appears exactly once, in a single aside about
*"the currency question"* being asked in the same letter as the actual subject —
incidental, not the topic.

**This isn't a gap, just a wrong pointer.** The real currency mechanic — credits as
the sole medium of exchange, starting purses, item costs — is already `RULED` and
held, in `STARTING-EQUIPMENT-01`: the Purse/Array choice (`PT-728`, *"the array may
contain what the purse could not afford... a player who takes the purse gets freedom,
a player who takes the array gets value"*), per-class starting credits, and the cost
columns already running through every `ITEMS` file in this book. **Both outline rows
citing `D-CURRENCY-01` should point to `STARTING-EQUIPMENT-01` instead — flagging this
for correction at the outline level, not just inside this one chapter.**

Same lightsaber-damage flag, unaffected. New here: the `D-CURRENCY-01` miscitation,
which needs fixing at the outline level in both Book Four's and Book Seven's rows —
not something one chapter file can close on its own. The loot-tier character-vs-area
question is named as undecided rather than resolved.

## ⚠⚠ A contradiction between two chapters, found and fixed by this pass

**Chapter Eleven said the loot-tier gate was undecided. Chapter Thirteen answers it.**

The old text read: *"What's still undecided: whether the tier gate keys off character level
or area danger. Area is the recommended direction… but that's a recommendation, not a
ruling."*

**`LOOT-01` resolved this, and Chapter Thirteen states it in full** — a character-level
table (1–5 → tier 1, through 21–30 → tier 4), **and** an area tier derived as
`max(encounter level, container difficulty)`, **and** world danger capping both. **The
answer turned out to be *both*, not one or the other.**

**So Chapter Eleven was carrying an open question that a later chapter in the same book had
already closed** — a reader consulting Eleven would have been told the system was unsettled
while Thirteen described it working. **Chapter Eleven now defers to Chapter Thirteen
instead.**

**That is the sixth instance of the self-description pattern found in this work, and the
second in a chapter I wrote.**

## ⚠ What the `PT-1844` pass changed in this chapter

**This was the heaviest rewrite of the task.** The chapter opened with a section about a
miscitation in the project's own outline, and three of its four remaining sections were
organised around ruling numbers.

**What survived, because it is genuinely reader-facing:** the unique-item rule in both its
halves, the 85-item count and — the best thing in the chapter — **how the 29 unflagged ones
were found.** *"There was one Nomi Sunrider, and she had one robe"* is now supported by the
rule it demonstrates: **if an item is named after a person, there was only ever one of it.**

**What was added, because the chapter's title promised it and the text never delivered it:**
**a section on currency.** The chapter was called *Tiers, Pricing and Availability* and said
nothing about money except inside the miscitation report. **It now states that credits are
the only medium of exchange, and that a character chooses between a purse and an array at
creation** — with the purse-versus-array line kept, since it explains the trade in one
sentence.

**What was reframed:** the feat remap. It was a confirmation that a data pass had been
applied. **A reader needs the consequence instead** — that where this book says an item
gates or grants something, **that came from the item itself** — with the four counts kept as
evidence.

**⚠ Deliberately NOT loosened.** Every figure survives: 85 unique items split 56 and 29, the
feat-property counts of 84, 120 and 9, and the purse-versus-array choice. **The one thing
genuinely removed is an open question that was no longer open.**

---

# Chapter Twelve — The Weapon Matrix and Crafting

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

*Sources: `WEAPON-MATRIX-01` (⚠ a derived view — `STARTING-EQUIPMENT-01 §2`, `§4a`, `§5`
are the record) for Part One, with `PT-760`, `PT-763`–`PT-767`, `PT-692`, `PT-702`,
`PT-714`, `PT-109`, `PT-567`. `CRAFTING-01` for Part Two, with `PT-203`, `PT-225`,
`PT-482`; `SKILL-RESOLUTION-01` for take-10 and `REST-AND-MEDITATION-01` for the downtime
period. Source tables `k2_itemcreate.2da`, `k2_chemicalcreate.2da`, `k2_upgrade.2da`.*

**⚠ Flag 1 — Part One restates a document that is itself a restatement, and I have said so
rather than hidden it.** `WEAPON-MATRIX-01` declares itself `DERIVED` and names
`STARTING-EQUIPMENT-01 §2`/`§4a`/`§5` as the record. **This chapter is therefore a third
copy**, and `D-W32`'s reasoning applies — *cite, do not restate, because copies drift.*
**The table is reproduced here because a player-facing book cannot send a reader to a rules
document for their own starting kit**, but the pointer is stated at the top of Part One and
the source governs on conflict. **A future sweep should check this table against
`STARTING-EQUIPMENT-01` directly, not against `WEAPON-MATRIX-01`.**

**⚠ Flag 2 — fifteen item names in this table resolve to more than one item.**
`WEAPON-MATRIX-01 §4` records it: *"which row each item name means — `§2c`, because fifteen
of these names resolve to more than one item."* **Chapter Three proves the point** — thirty
separate items are called some variety of Blaster Pistol. **A GM handing out a "Blaster
Pistol" at character creation should take the base row**, `g_w_blstrpstl001`, not whichever
variant a search returns first.

**⚠ Flag 3 — the crafting item catalogue is deliberately deferred and stays deferred.**
994 blueprints are extracted and joined; **turning them into readable entries is a separate
job** and is not attempted here. Also deferred at source: `k2_itemcreatemira`'s 214
character-specific recipes (companion content, and there is no companion system yet) and
the 99 upgrade rows whose blueprints live in module archives rather than `templates.bif`.
**This chapter documents the system, not the recipe list.**

**⚠ Flag 4 — the recipe count in circulation is 73 and the true figure is 68.**
`CRAFTING-01` corrects it in place, but **73 is the number printed on the source table** and
will keep resurfacing. **The five removed are the HK parts above**, which are a droid rather
than recipes.

**Not a flag, but worth stating: nothing in this chapter needed the base weapon dice.**
Part One names weapons; it does not restate their stat lines, which Chapters One through
Four already carry. **That insulates it entirely from the ranged-dice question** that
stopped Chapter Three's catalogue.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 17 internal citations from 379 lines**, plus the four-flag section. **The
highest raw count of any chapter in the task**, though most were single ruling numbers
attached to otherwise clean sentences rather than dense passages.

**⚠ The derived-view warning was the important one.** Part One opened by quoting
`WEAPON-MATRIX-01`'s own status line — *"THIS DOCUMENT RESTATES `STARTING-EQUIPMENT-01`…
THOSE ARE THE SOURCE; THIS IS THE VIEW"* — and explaining that this chapter is therefore a
third copy.

**All true, all internal, and the reader-facing half is one sentence:** **the Player's
Handbook is the authority on starting equipment, this is a summary of it, and where the two
differ the Player's Handbook is right.** A reader does not need to know how many copies
deep the summary is; they need to know which one wins.

**⚠ The feat-versus-profession correction was re-pointed at the reader.** It read *"`PT-764`
corrects a mistake worth understanding"* — a mistake *this project* made. **The reader's
version of that mistake is different and more likely:** it is tempting to read *"two Heavy
Blasters"* as something the feat alone provides. **It is not.** Same correction, aimed at
the person who will actually make it.

**The `hkpart` entries now point at Chapter Fourteen** rather than at the ruling that
deferred droid construction — **which is where a reader can actually follow them.**

**The take-10 rule, the DC ladder, the downtime period and the droid-construction
permissions all lost their citations and kept their content**, including the Machinist's
exclusive right to build *for another character*, which was corrected during this same task
at Chapter Fourteen.

**⚠ Deliberately NOT loosened.** All thirteen standard classes, six Force classes and nine
droid arrays keep their full four-column entries; the `Brawler`'s empty row keeps its
explanation; the ceiling ruling keeps both weapons and both prices; every crafting DC,
skill reassignment and implant split survives; and **the five `hkpart` entries are still
named individually.**

---

# Chapter Thirteen — Loot

*Moved here from the chapter's foot, `PT-1844` pass, unchanged in substance.*

*Sources: `LOOT-01`, with `PT-307` (the bands, ported), `PT-308`/`PT-309` (the tier gate,
authored), `PT-323` (party composition), `PT-327` (unique items), `PT-404` (world danger),
`PT-651` (every item carries a tier), `PT-655` (party level), `PT-666` (authored versus
generated), `PT-912`/`PT-922` (named sites). `SKILL-RESOLUTION-01` for take-10;
`PARTY-01 §2` for party level; `ITEMS-01`–`08` for the tier data.*

**⚠⚠ Flag 1 — the band-to-table mapping is an inference, and the source document says so.**
This is the largest open item in the chapter. `PT-307` **read the constants out of
`a_give_treas`, not the control flow** — so the band *thresholds* (60/70/80/90) are
verified, but **which band draws from which list is unverified** until someone disassembles
the script properly.

**Everything above is written as though band 5 draws the best item on the table**, which is
the natural reading and matches observed play. **It is not confirmed.** If the mapping turns
out to be different, the bands table stands and only the interpretation moves.

**⚠ Flag 2 — every item carries a tier, and the count in circulation is stale.** `PT-651`
closed this: **1,385 rows across `ITEMS-01`–`08`, zero blanks** — tier 1: 634, tier 2: 427,
tier 3: 213, tier 4: 111. **The figure of 994 still appears in places** and is the blueprint
count, not the item count. `LOOT-01` notes the drift against itself: *"the corpus grew past
it and the paragraph did not."*

**⚠ Flag 3 — `LOOT-01` carries a duplicated paragraph with a broken cross-reference.** Its
`§7b` states *"Procedurally generated areas are not covered by ."* — the reference is
missing entirely — and then repeats the same paragraph immediately with the reference
filled in as *"section 4"*. **The first copy should be deleted.** Same shape as the
`EVENTS-01` heading defect from the Galactic Timeline: an edit that added a corrected
version without removing the broken one. **Reported, not fixed — `LOOT-01` is a rules
document.**

**⚠ Flag 4 — the named-site count appears twice with different values.** `PT-912` records
**45 sites across 31 worlds**; `PT-922` records **47 across 32**, hand-curated, delivered.
**Both sit in the document.** The later supersedes under `§3b`'s later-wins rule and this
chapter uses **47 / 32** — but a reader meeting 45 first has no way to know it is
superseded. **Same class as the Timeline's stale `"ranking fifth"` numeral.**

**⚠ Flag 5 — the world count does not match the Atlas's.** `LOOT-01` reports **288 worlds**
carrying a `danger` value; `PT-1705` establishes that `data/extracted/worlds.json` holds
**301 world entries** — a figure it explicitly corrected from 290 *"before it became the
working number."* **Thirteen worlds are unaccounted for.** They may simply lack a danger
value, in which case the fallback is party level and nothing breaks — **but the chapter
cannot say so, because no held source states it.** Worth one check by whoever owns the
Atlas.

**Not a flag: `§7` and `§7b` state `PT-651` twice in near-identical terms.** Harmless
duplication rather than contradiction, but it is the same edit pattern as Flag 3 and the
two were probably introduced together.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — only 4 internal citations from 308 lines**, the lightest body load of any Armory
chapter. **This chapter was written late and already spoke to a reader.**

**⚠ But Flag 1's reader-facing half was promoted into the chapter, and that is the
important change.** The band-to-table mapping being an inference is **not a project
housekeeping note** — it affects how every loot roll in a campaign resolves, and a
Gamemaster is entitled to know which part of the system is certain and which is inferred.

The chapter now carries it directly, immediately after the bands table:

> **One honest caveat about the bands.** The roll thresholds above — 60, 70, 80, 90 — were
> read directly out of the game's own script and are certain. **Which band draws from which
> list is an inference**… **If that turns out to be wrong, the bands stand and only their
> mapping moves.**

**The project-facing half stayed here:** that the reading came from constants rather than
control flow, and that settling it means disassembling the script properly.

**That is the split-by-audience default doing exactly what it was adopted for — and this is
the case where burying the caveat would have mattered most**, because Chapter Eleven now
defers to this chapter for the whole tier system.

**⚠ And the authority Chapter Eleven handed over was preserved rather than weakened.** The
sources section states plainly which half of this system is KOTOR 2's and which is this
game's addition: **the roll and its bands are ported unchanged; the tier gate, the
`Security`-DC ladder, the world-danger ceiling and the named-site override are all new.**
The `376 sampled` evidence for KOTOR having no lock difficulty at all is kept, because it is
what makes the authored half defensible.

**Three smaller fixes.** The `Atlas` references now name the **Planetary Atlas** as a book in
this set rather than a data source; the `danger` **field** became a **rating**; and the
take-10 and party-level rules lost their document citations while keeping their content
exactly.

**⚠ Deliberately NOT loosened.** Every threshold, tier boundary, DC band, formula and count
survives — including `area tier = min( max(encounter, container), world danger + 1 )`, the
180-of-288 constraint, the 47 named sites, and both unique-item halves.

---

# Chapter Fourteen — Droid Construction and Upgrade

*Original source line, as it stood before the `PT-1844` pass:*

> *Sources: `DROID-CONSTRUCTION-01` (`PT-572`, `PT-607`–`PT-613`, `PT-225`, `PT-558`,
> `PT-594`, `PT-598`, `PT-599`, `PT-609`, `PT-953`) and `DROIDS-UPGRADE-01` (`PT-274`,
> `PT-316`, `PT-323`, `PT-577`, `PT-616`, `PT-654`). `CLASS-ROSTER-01` for the
> prestige-class check. `DEATH-AND-DIFFICULTY-01 §5b` for rebuild by difficulty mode.*

## Flags, carried from review

**⚠⚠ Flag 1 — this chapter contradicts Chapter Twelve, and Chapter Twelve has the weaker
source.** `CRAFTING-01` states the `Machinist` *"is the **only class** that can build a
droid — `PT-225`"*, and **Chapter Twelve repeats that.** `DROID-CONSTRUCTION-01 §4` says
otherwise: **Machinist, Droid Master and Engineer may all build**, and explains the
relationship — *"`PT-225` is explicit that construction belongs to the Machinist, and
`PT-572` does not take it away — it **extends** it to the two classes whose premise is
droids."*

**`PT-572` is the later and more specific ruling, and it is the one this chapter follows.**
`CRAFTING-01`'s sentence was true when written and was not updated when `PT-572` extended
it — **`PT-961`'s shape again.**

**✔ Fixed.** Chapter Twelve now reads that the Machinist is **the only class that can build
a droid *for someone else***, and states that `PT-572` extended building itself to
`Droid Master` and `Engineer`. **Both citations were verified against `PT-225`'s own
heading and `DROID-CONSTRUCTION-01`'s reconciling text before the edit.**

**⚠ Flag 2 — `DROID-CONSTRUCTION-01 §6` uses part names that `PT-612` retired.** The
rebuild section reads *"the **Motivator**, **Processor Core** and **Power Cell** are
destroyed"*. But `PT-612` **renamed `Motivator` to `Control Cluster`**, uses **`Droid
Processor`** rather than *Processor Core*, and **withdrew `Power Cell` entirely** — *"the
droid quest has no power component and we should not invent one."*

**So §6 lists a part that no longer exists.** This chapter states the three current parts
instead. **Reported, not fixed.**

**⚠ Flag 3 — and the same section carries a figure from the superseded flat-cost model.**
§6 gives the rebuild cost as **2,800 credits** and *"one day, regardless of chassis"*. But
`PT-608` replaced the flat 2,800 with the tiered ladder — **700 / 1,400 / 2,800.** 2,800 is
now the **heavy-tier** figure only; **rebuilding a Remote should cost 700, not 2,800.**
This chapter states it as *"its parts bill"* rather than repeating the stale number.
**Same edit-lag as Flag 2 and probably the same moment.**

**⚠ Flag 4 — the Armory references a class the Player's Handbook does not contain.**
`Droid Master` appears in this chapter's build permissions and in the bay-grant ladder, and
`CLASS-ROSTER-01` lists it among the **prestige** classes. **`PT-1705` moved prestige
classes to the Advanced Player's Guide**, so a reader of the Armory and the PHB together
will not find it. **Not an error — a cross-book reference that wants a pointer** when Book
Eight exists.

**⚠ Flag 5 — `DROIDS-UPGRADE-01` documents its own staleness and leaves it.** Its closing
paragraph reads: *"`LOOT-01` answered this in the same words as the worry — 'a party with no
droid gets nothing' — **and this paragraph never moved.**"* The document knows the text is
superseded, says so, and keeps it. **Harmless here because the two agree**, but it is the
third instance in two chapters of a rules document carrying a retracted or superseded
passage alongside its replacement.

## ⚠ What the `PT-1844` pass changed in this chapter

**Removed — 13 internal citations from 407 lines**, plus the `Status: DRAFT, for review`
header and its *"third of the Armory's four remaining chapters"* build-state claim, which
told a reader nothing and would have been wrong within the week.

**⚠ Flag 3's reader-facing half was promoted, and it is the change that matters most.** The
rebuild section said a destroyed droid *"costs its parts bill"* — true, and useless at a
table, because a Gamemaster mid-session needs a number. **The chapter now states all three:
700 light, 1,400 medium, 2,800 heavy**, with the two worked cases the flag itself supplied —
**an Assassin rebuilds for 2,800 against 6,900 to build fresh; a Remote rebuilds for 700.**

**That was the flag's whole point.** The stale figure in `DROID-CONSTRUCTION-01 §6` is a flat
2,800 for every chassis, which over-charges a Remote fourfold. **Stating the ladder in the
chapter closes the reader's exposure to it regardless of when the rules document is fixed.**
The project-facing half — that §6 is still stale — stayed here.

**⚠ Flag 4's reader-facing half was promoted too.** `Droid Master` is used twice in this
chapter and does not appear in the Player's Handbook. The chapter said *"see Flag 4"* — a
pointer to a note that has now moved out of the book entirely. **It now says plainly that
prestige classes live in the Advanced Player's Guide and that a reader with only the
Player's Handbook will not find the class there.** The project-facing half — that this wants
a real cross-book pointer once Book Eight exists — stayed here.

**⚠⚠ A real content find, reported rather than papered over: the fifth crafting-bench
entry.** Chapter Twelve identifies **five** entries that are not recipes, `hkpart01` through
`hkpart05`, and says all five belong in Chapter Fourteen. **This chapter built from four.**
The opening paragraph named four and called them five.

**`hkpart05` — the HK Protocol Pacifist Package — has no ruling anywhere in the corpus.** A
search of the rules documents and the ledger returns nothing but Chapter Twelve's own
listing. **So there is no crunch to borrow and none was invented.** The chapter now names the
part, says it belongs to KOTOR 2's rebuild of one particular droid rather than to general
construction, and states plainly that it has no cost, no tier and no place in a build.

**⚠ This is a gap, not a fix.** If the owner wants the Protocol Pacifist Package to be a
buildable part, it needs a ruling; the chapter's current sentence is honest about its absence
and nothing more. **Raised for a decision.**

**⚠ One precision fix inside a rule, changing no rule.** The chassis-cap section read *"a
light chassis caps at six bays"* while the parts ladder four sections earlier sorts
`Astromech` as **medium**. **The cap applies to `Astromech` and `Remote` specifically**, so
the line now reads *"those two chassis cap at six bays, permanently."* **Same gate, same two
chassis, no longer contradicting the tier table on the same page.**

**Smaller rewrites.** The Vocabulator passage stated two rulings-made-from-lore and now
states the two facts themselves; the `LB-series` quote is kept and attributed to the setting
rather than to a ruling number. The three-tier parts shape is now attributed to the game's
own plating items, by resref — **`g_i_drdltplat001`–`003`, `g_i_drdmdplat001`–`003`,
`g_i_drdhvplat001`–`003`** — which is a stronger justification than the ruling number was,
because a reader can check it.

**Three passages lost their development history and kept their content.** The flat-2,800
problem is now stated as what a flat price *would* do rather than as what an earlier draft
did; the brain-first build order no longer mentions that a draft had it backwards; the
six-socket count no longer records that it was first read as four. **The corrections
themselves all survive, stated directly — which is the standing method for rulings that exist
because something is commonly got wrong.**

**⚠ Deliberately NOT loosened.** Every price, tier, DC, bay count, class grant, cap and
formula survives unchanged: the 700 / 1,400 / 2,800 ladder and its per-part breakdown, all
seven build-or-buy rows, the `Repair` DC ladder 15–30, one day per 1,000 credits, the junk
droid's half price / DC +5 / `−2` / natural-1 / `Droid Upgrade 1` ceiling, the six sockets,
the 3 / 6 / 9 bays, the whole class-grant table, the `Astromech`/`Remote` cap, and
`Juggernaut`'s exclusion by it.
