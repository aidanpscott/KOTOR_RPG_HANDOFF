# SAVE-LOAD-01 — the save is the log

**The last piece of architecture with a genuine open question in it.** `PLAY-STATE-01` made state a projection of an append-only log. **That settles what a save *is* and leaves two problems: it grows, and replaying it is slow.**

---

## 1 · What a save is

> **The save is the log. Loading is replay.**

**There is no separate save format**, no state dump, no world snapshot. `TRACE-85` found KOTOR doing the opposite deliberately — **a save there is a replacement copy of every visited module**, 112 fields inline per creature. **They had no replay, so they had no choice.** We do.

---

## 2 · ⚠ Size — compress, do not discard

**`PT-1271` bound the growth problem to this work.** `ENGINE-SPEC-01 §5`: *"if generated content writes into the fact ledger without bound, the ledger stops being the flat 58 KB file and becomes the 13.6 MB one."*

**⚠ The answer is compression, not compaction — and the distinction is everything.**

| | Does what | Reversible |
|---|---|---|
| **Compression** | makes the same events smaller | **yes — decompress and they are all there** |
| **Compaction** | replaces events with a checkpoint | **no — the events are gone** |

**An event log is close to a best case for a general compressor.** The same ~30 event kinds, the same handful of character ids, the same structure, thousands of times over. **A 13.6 MB log compresses to well under a megabyte**, which removes the problem `TRACE-04` raised.

### ⚠ Measured, not assumed — `PT-1328`

**Tested on a synthetic 120,000-event log, 16.3 MB raw — larger than `TRACE-04`'s 13.6 MB worst case.** Round-trip verified by SHA-256 against the original in every case.

| | size | ratio | compress | decompress | round-trip |
|---|---|---|---|---|---|
| **gzip-6** | 1.41 MB | 11.6× | 0.29 s | **0.04 s** | **identical** |
| **zstd-10** | 1.32 MB | 12.4× | 0.35 s | **0.01 s** | **identical** |
| bzip2-9 | **0.78 MB** | **21.0×** | 2.21 s | 0.33 s | identical |
| xz-6 | 1.10 MB | 14.8× | 9.72 s | 0.08 s | identical |
| zstd-19 | 1.08 MB | 15.1× | **24.57 s** | 0.01 s | identical |

**⚠ EVERY ONE IS BYTE-IDENTICAL ON ROUND-TRIP. Nothing is lost, by any of them** — that was the requirement and it is met by all five.

**Recommended: `zstd` at a middle level, `gzip` as the fallback.** 16.3 MB to ~1.3 MB, **a hundredth of a second to load**, and no dependency worth arguing about. **`bzip2` buys 0.5 MB for a two-second save** — a bad trade on a file saved often. **`xz` and `zstd-19` are unusable at 10 and 25 seconds.**

**⚠ And do not write a custom compressor.** A standard one gets 12× here with nobody designing anything. **The effort belongs upstream.**

### The real lever is what gets logged

**`EVENT-KINDS-01` already carries the tool: lifetimes.** A `transient` event declares its own expiry condition — **and once that condition has fired, the event need never have been written at all.**

**Ten thousand events compressed 15× beat a hundred thousand compressed 20×.** Design the vocabulary so most combat chatter never persists, and compress what survives.

### The file is `.sav` — `PT-1329`

**Owner ruling. The extension is `.sav` whatever compressor sits inside.**

**⚠ And the source games already did this.** `TRACE-81`: **`SAVEGAME.sav` opens with the `MOD` signature, not `SAV`** — KOTOR's save is an ERF archive wearing a `.sav` extension. **The name was never the format.**

**⚠ So the file must say what it is in its first bytes**, because the extension does not. A short header before the compressed payload:

```
magic          identifies the file as ours
format version so a future change is detectable
compressor     which one, so it can change without breaking old saves
rules version  PT-1270's OF07 pin — what this log was played under
⚠ PT-1518 — format = 2:
saved at       UTC milliseconds. A fact about the PLAY SESSION
package        which package — so listing need not replay every log
character      the player's name for them
class, level   what a save row shows beside a name
area           where they were standing
```

**⚠⚠ `format = 2` SINCE `PT-1518`, AND THE BUMP IS LOAD-BEARING RATHER THAN CEREMONIAL.** The header is **positional** and its length is **derived from the fields a reader knows**. New fields sit before the payload, so a `format = 1` build reading a `format = 2` save computes the payload offset short, hands header bytes to the decompressor, and reports **"Damaged save: the contents could not be unpacked."** **That is a wrong reason for a perfectly good file** — `PT-1366`'s motivating case exactly: *an old file must be distinguishable from a broken one.* The machinery to say the true thing already existed (`formatFromTheFuture`, *refused rather than read optimistically*) **and it only fires if the number moves.**

**⚠ And moving it is what keeps old saves readable, not what breaks them.** A `format = 1` save still parses and still yields its log; it carries none of the new fields, and **absent means *older than the field*** — never a value invented from the filesystem.

**⚠ The compressor field is what makes the choice reversible.** `PT-1328` recommends `zstd` with `gzip` as fallback; **recording which one was used means switching later does not orphan existing saves.** Without it, the choice is permanent by accident.

---

## 3 · ⚠ Speed — snapshots, and why they are not a violation

**A hundred hours of replay on every load is unacceptable.** The fix is a snapshot: the projected state at a point, stored, so a load replays only the events after it.

**⚠ And `CHARACTER-RECORD-01 §3` says derived values are never stored.** That looks like a contradiction. It is not, and the reason matters:

> **The rule exists to prevent DRIFT — a stored value disagreeing with what it should compute to. A cache that can always be regenerated cannot drift; it can only be stale, and a stale cache is discarded.**

**The test, and it is the whole distinction:**

> **Can you delete every snapshot and lose nothing? If yes it is a cache. If no it is a store, and it violates the rule.**

**A snapshot must pass that test.** It is never the source of truth, never edited, and **always regenerable from the log.**

### When

**At session end.** A natural boundary, it is when a save happens anyway, and it bounds replay to one session's events.

**⚠ And a snapshot is invalidated by a rules change**, not just by new events — `PT-1270`'s `OF07`. If the version the log is pinned to changes, **every snapshot is stale and is thrown away.** That is cheap precisely because they are caches.

---

## 4 · ⚠ So compaction is WITHDRAWN

**`PT-1272` ruled compaction lawful and restated `PT-1265`'s replay guarantee around it: *"compaction produces a different log with the same end state."***

**Compaction existed to solve SIZE. Compression solves size losslessly. Snapshots solve SPEED. Compaction has no remaining job.**

**⚠ So the guarantee returns to its unconditional form:**

> **Replay of a log is bit-identical, always. No operation produces a log that cannot be replayed to any point in it.**

**That is a real simplification.** It removes: the four-lifetime *compactability* distinction as a storage concern, the checkpoint event kind, the question of when compaction is offered, and `PT-1272`'s caveat that a compacted log cannot replay past its checkpoint.

**⚠ Lifetimes SURVIVE and change job.** They no longer decide what may be destroyed. **They decide what is written in the first place**, which is `§2`'s lever and a better use for them.

**Kept as a last resort, unruled:** if a log is ever pathological *after* compression, discarding is the fallback. **Nothing suggests that will happen, and no mechanism is specified for it.**

---

## 5 · Loading

```
1  read the manifest, resolve packages       PACKAGE-FORMAT-01 §6
2  take the latest valid snapshot            or none, if the rules version moved
3  replay events after it
4  validate the projection                   PLAY-STATE-01 §2
5  open
```

**⚠ Failure is loud at every step**, per `F35`. **A missing package, a snapshot pinned to a version that no longer exists, an event referencing a handle that does not resolve** — all refuse, none degrade quietly.

---

## ⚠ WHICH LOG AN `encounter.ended` BELONGS TO — `PT-1427`

**The second projection asked it and its own `b3` mostly answers it: ONE EVENT PER COMBATANT, not one listing everyone**, because *the fold keys on subject and a party member's outcome may need to travel alone.*

> **⚠ An event goes in the log of the SUBJECT it describes.**

**A player character's outcome goes in that character's log** — `PT-1415`'s one-log-per-character-per-campaign, unchanged.

### ⚠ And an NPC has no log — CLOSED at `PT-1510`, not deferred

**A wounded trooper's state is not a fact about any player.** It is **a fact about the campaign** — and `PT-1415` already makes a save **one log per character per CAMPAIGN**, so the character's log *is* the campaign's log for a solo campaign. **That is the design, not a stand-in for one.**

> **⚠⚠ RULED AT `PT-1510`: A PACKAGE IS A MODULE, NOT A WORLD.** Two characters in one package are **two campaigns of the same module** — *"two groups running the same book do not share a dead ogre"* — and it is what KOTOR and NWN both did.

**⚠ SO THE EARLIER "KNOWN CONFLATION" FRAMING IS REMOVED: THERE WAS NO CONFLATION.** This section previously recorded the character's log carrying world state as a debt to be split later. It is not a debt. **The scope was right; only the wording was wrong** — `PT-1510`.

**⚠ And the multiplayer question is closed with it.** `PT-1330`'s *in-fiction shared, out-of-fiction private* still holds, and what it shares is a **campaign**: **multiplayer characters share a CAMPAIGN, not a package.** A shared campaign log is one log for one campaign's several characters — **not a per-package world log**, which is the thing this document used to be reaching for and which the ruling says does not exist.

**⚠ WHAT WAS ACTUALLY WRONG WAS A SENTENCE**, and `TEST 018` found it by making a second character: the same tagged creature stood at **3 for one and 2 for the other, at the same time**, which is correct — while the app said *"encounter `a01-probe-room` left you at 3"*, **phrased about the room.** A fact about your campaign must say so, or a player meets an untouched creature they personally beat and is told nothing.

> **⚠⚠ THE CONFLATION ARRIVED, AND IT IS NOT ONE — `PT-1510`.** `TEST 018` made a second character in one package and found **the same tagged creature at 3 for one and 2 for the other, at the same time.** Persistence works perfectly; **it is scoped to the character.**
>
> **⚠ AND NO CODE WOULD NEED TO BE WRONG FOR THIS TO HAPPEN — it falls out of the format.** An outcome is written into that character's own log, and a second character replays only its own.
>
> **RULED: A PACKAGE IS A MODULE, NOT A WORLD.** A campaign is the playthrough. **Two characters in one package are two campaigns of the same module** — exactly what `PT-1415` said: *one log per character per CAMPAIGN.*
>
> **⚠ That is what a published module IS.** Two groups running the same book do not share a dead ogre. **And it is what KOTOR and NWN both did** — a module is a scenario, not a place that remembers everyone who visited.
>
> **⚠ SO THE BEHAVIOUR IS CORRECT AND THE WORDING IS WRONG.** *"Encounter `a01-probe-room` left you at 3"* is **phrased about the room.** It is about **your campaign**, and the sentence must say so — otherwise a player meets an untouched creature they personally beat, **with no explanation anywhere.**
>
> **⚠ And the shared-log question is now CLOSED rather than deferred.** It was recorded as owed to multiplayer; **multiplayer characters share a CAMPAIGN, not a package**, so a shared campaign log is still the right home when it exists — **and this was never that case.**


---

## ⚠ POSITION IS CAMPAIGN LIFETIME — `PT-1417`

**Batch 3 found that a save cannot know where you were standing, and it was right about why:** `character.moved` and `area.entered` were both **session** lifetime, and `§4` gives lifetimes their job — *"they decide what is written in the first place."*

**⚠ So a player who walked to the second area, quit and continued arrived back at the first.** By the vocabulary's own rules.

**Both are now CAMPAIGN.** Owner ruling: *the state of everything was right when you ended it.*

### ⚠ And the cost is already measured

**A walk generates many events, which is the obvious objection — and `PT-1328` answers it.** **120,000 events compressed to 0.34 MB** and loaded in a hundredth of a second. **The batch's own real log was 26 events and 759 bytes.** **Volume is not the constraint it looks like.**

**⚠ And replaying 120,000 moves to learn where someone is standing is exactly what snapshots are for** — `PT-1327` made them a **cache**, taken at session end and invalidated by a rules-version change. **Delete every snapshot and lose nothing; the position is still in the log.**

**So the architecture already had the answer in two pieces and nobody had joined them:** the log makes it **true**, the snapshot makes it **fast.**

---

## ⚠ 5·0 HOW MANY, WHAT NAMES IT, AND WHAT `Continue` ORDERS BY — `PT-1416`

**Three questions, and two of them are already answered elsewhere.**

### ONE FILE PER CHARACTER PER CAMPAIGN

**`PT-1415` ruled the scope; this is the same ruling in the filesystem.** The log is append-only, so **"save" means flush the log you already have.** One file, rewritten.

**⚠ AND A SAVE SLOT IS A POINT IN THE LOG, NOT A COPY OF IT.** A player saving before a boss fight does not need a second file — **they need a bookmark.** Loading it means **replaying fewer events.**

**⚠ And playing forward from an earlier point writes a REWIND EVENT.** `PT-1415`'s `step-reopened` is exactly this shape one layer up: **the rewind names what it discards, replay honours it, and nothing leaves the log.** *A correction is a new event, not an edit* — **and so is a reload.**

**That is what `§6`'s *"a save that is a log may want showing differently from a save that is a slot"* was circling.** **It is a log, and a slot is a view of one.**

### THE FILE IS NAMED FOR THE CHARACTER'S id

**`PACKAGE-NAMING-01` answers this shape and the answer transfers:** the **path is identity**, a **name is what a player reads**, and **an id is derived from the name and stays correctable.** A character's name is free text and not unique; **`kaeda-vos.sav` is both readable and stable.**

### ~~⚠ `Continue` ORDERS BY FILESYSTEM TIME, and the header gains NOTHING~~ — ⚠⚠ OVERTURNED AT `PT-1518`

> **`PT-1416` ruled that and it was wrong.** The argument came from `PT-1358` — *"which tile sorts first is not a fact about the package"* — **and that holds for a SHELF, where nothing is being resumed. It does not hold here.**
>
> **⚠⚠ WHICH SAVE IS MOST RECENT IS A FACT ABOUT THE PLAY SESSION, not about the disk.** A copied folder or a restored backup **changes the answer without a player having played.**

**⚠ AND THE CODE HAD ALREADY SPLIT ON IT.** `save_listing.dart` refused to supply a *latest* — *"ordering by file mtime would be the caller's filesystem guessing at a fact the format does not record"* — while `SaveStore.mostRecentHandle` **ordered by file mtime**. **One surface refused the guess and the other was built on it**, which is why `Load Game` and `Continue` disagreed about which save was first.

**⚠ `TEST 018` measured the cost:** `Load Game` listed **fifteen saves in `Directory.list()` order** — arbitrary, stable, meaningless; not alphabetical, not most-recent — and **every row also read *"rules 0.1.0"***. A player looking for *the one I played yesterday* read fifteen filenames in scrambled order.

**RULED: the header gains a time and an identity.** The field set is above, and **every field is there for a named consumer** rather than for completeness:

| field | who needed it | what it was doing instead |
|---|---|---|
| `saved at` | `Load Game` order **and** `Continue` | guessing from file mtime |
| `package` | `listFor` | **decompressing and replaying every log** to learn the owner |
| `character`, `class`, `level` | the save row | showing a filename |
| `area` | the save row | nothing — *"no where"* |

**⚠ `package` is the sharpest of them.** `save_listing.dart`'s own contract is *"replaying one to answer 'is there a save?' would be the expensive answer to a cheap question"* — **and filtering by package was doing exactly that, fifteen times, to draw a menu.**

---

## ⚠ 5a · Where files live — `PT-1382`

**Needs D and E were one question and are one function.** `Locations(root)` yields `root/packages` and `root/saves`. **Both are *"where does this product keep its files"*, both must be identical across both programs, and both were placeholders.**

**⚠ It lives in Lodestar** — a shared answer in two places is what put the naming rules and `openCharacter` there. **Third time, same argument.**

**⚠ And the folder is named for the PRODUCT, not for either program**, with a test asserting the name contains neither `loom` nor `app`. **Loom writing to a Loom-scoped folder is precisely the failure being closed.**

### ⚠ The near-miss, which is the finding

**`path_provider`'s application-support directory is the obvious answer and is WRONG here.**

**On Linux it resolves to a directory derived from the RUNNING EXECUTABLE** — so Loom and the play client would **each get their own**, reintroducing the exact bug **in a form that looks like best practice.**

**Packages are shared between two applications, so the desktop root must be VENDOR-scoped rather than APP-scoped.**

**⚠ On mobile it returns null, deliberately.** Android and iOS have **no shared location and no environment variable naming one** — storage there is private to an installed application. **So the app supplies its own root and Loom throws with a reason, because a Builder does not run there.** A genuine platform constraint rather than something worked around.

**And it is not the engine browsing a disk.** `ENGINE-INTERFACE-01 §4` bars paths *"beyond open"* — **this answers WHERE, the way `PACKAGE-NAMING-01` answers what a name may be.** It enumerates nothing and reads nothing. **Listing stayed with the front-ends.**

---

## 6 · Open

- **Snapshot granularity.** Per character, per party, or one for the campaign. **Per campaign is simplest; nothing has tested whether it is fast enough.**
- **Whether the player ever sees any of this.** `PT-1255` kept `Save Game` and `Load Game` on the menu. **Compression and snapshots should be invisible** — but a save that is *a log* may want showing differently from a save that is a slot.
- **Multiplayer.** `ENGINE-SPEC-01` gives every event a visibility set. **Whose log is authoritative when four players share a campaign is not addressed here** — see `AGENDA-RECORD-01` item 6.
