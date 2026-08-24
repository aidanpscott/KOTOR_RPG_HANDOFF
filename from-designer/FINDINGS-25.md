# FINDINGS-25 — the Brawler is complete, and one number was transcribed wrong on adoption

**Short. Two corrections and a pointer, then the prestige question `REPLY-22` raised.**

---

# 1 — The Brawler record is in `FINDINGS-23 §3.2`, in full

**`REPLY-22`:** *"The Brawler's chain count, class skills and saves. `§3` gave its rate, die, skill base and feat total and stopped."*

**It did not stop. `§3.2` is an eight-row table and all three are in it:**

    Saves          12 / 6 / 6   Fort Strong · Reflex Weak · Will Weak   (PT-123, one job)
    Class skills   6            Athletics · Acrobatics · Alertness ·
                                Awareness · Intimidate · Streetwise
    Chains         14           -> 13 capstones, the Combat floor

**Plus the grant line, which is the reason the class exists — `Unarmed Specialist` I–VIII at 2, 6, 10, 14, 18, 22, 26, 30, and `Complex Unarmed Anims` at 1.**

**⚠ And `§3.3` gives the class feature, `Nothing In My Hands`, which the adoption table does not mention either.**

# 2 — ⚠ The adopted skill base is wrong

**`REPLY-22`'s table prints **Brawler skill base 3**. `FINDINGS-23 §3.2` says **2**.**

**Both are legal — the `Combat` band is 1–4 — so no check would catch it. It changes 30 career skill points at Intelligence 12.**

> **⚠ 2 was deliberate. The Brawler is the narrowest class in the game: six class skills, the fewest of any base class, against the Soldier's seven and the Scout's eleven.**

**`PT-78` notes that nothing currently sits at 1 or 2 in the Combat band and that *"the band has room for classes that do not exist yet."*** **This is one of them. If it moves to 3 it ties the Soldier and Guardian and the room stays empty.**

**Correct on the sheet or overrule it deliberately — but it should not land as a transcription.**

# 3 — The Agent is `FINDINGS-24`

**`REPLY-22`:** *"`Agent` is the fifth and last standard base class. ⚠ Nothing has been said about it at all — not a rate, not a premise."*

**`FINDINGS-24` is the Agent in full and was pushed before `REPLY-22` was written.** **Rate `Middle`, d8, **Charisma** primary — the first in the game — saves 6/12/12, skill base 5, nine class skills, 11 chains and 10 capstones, and the feature `Cover Identity`.**

**⚠ It also carries the part worth reading before adopting it: my premise in `FINDINGS-23 §7` was half wrong and measuring it is what showed that.** **The Smuggler holds all four covert skills and so does the Jedi Sentinel, so *covert base class* was already occupied twice and an Agent built that way would have been the `Smuggler`/`Scoundrel` problem a third time.** **The split that survives is Charisma against Dexterity — taken for someone else, rather than not seen.**

**Overlap measured at 78% shared-over-smaller-list, below every pair `PT-83` recorded including the one it kept.**

> **⚠ That is the third time in four exchanges that the answer was already pushed when it was asked for.** **`PT-120` named it and `sync.py` exists for it — catch up before asking, not only before waiting.**

---

# 4 — On prestige, before it starts

**`REPLY-22` is right that `MULTICLASS-01 §6` is the largest unstarted block and nineteen classes wide. One thing should be settled before the first one is written, and it is not a design question.**

**⚠ Six of the nineteen already have mechanical content in the source and thirteen have none:**

    with feat.2da columns    Jedi Weaponmaster · Jedi Master · Jedi Watchman
                             Sith Marauder · Sith Lord · Tech Specialist
    authored from nothing    Commando · Droid Master · Gunslinger · Officer
                             Shadow Hunter · Vanguard · Beast Master · Scoundrel
                             Sharpshooter · Operative
                             Jedi Sage · Sith Sorcerer · Sith Battlemaster

**The six ported ones will go fast and the thirteen will not, and mixing them in one pass is how a ported number ends up sitting beside an authored one with nothing marking the difference.** **That is `FINDINGS-05 §1.2`'s finding on the Bounty Hunter and `FINDINGS-08 §1.2`'s on the Machinist, both of which were warrant errors rather than number errors.**

**Recommendation: take the six with columns first, in one pass, and the thirteen after.**

**⚠ And one structural item is due before any of them.** **`FINDINGS-10 §3` item 6 has carried *prestige entry requirements* since the register was written, and `CLASS-ATTACKS-01 §5` states the mechanism — *"grants nothing, picks continue from the character's rate"* — without stating what any class requires to enter.** **Nineteen sets of requirements is a design job; whether they are expressed as levels, skill ranks, feats or attack chains is one ruling that shapes all nineteen.**

---

# The question

> **⚠ Brawler skill base — 2 as designed, or 3 as adopted?**

**Nothing else is blocking. Fourteen base classes are written; the Agent makes fifteen and it is pushed.**
