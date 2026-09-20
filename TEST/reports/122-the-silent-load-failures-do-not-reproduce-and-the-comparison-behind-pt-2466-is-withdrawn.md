# TEST 122 — the silent load failures do not reproduce, and the comparison behind PT-2466 is withdrawn

**Build.** App **`bf2a9b2`**, the same binary TEST 121 was run on, built from
`git archive` of that sha; Lodestar **`d1fcab69`**, matching the committed
lock and the pub-cache checkout `package_config.json` compiles against.
Repo HEAD has since moved to `eebd977`; the greps below are against that,
the casts against `bf2a9b2`, and each is labelled.

**Verdict.** **Withdrawing my own contribution to PT-2466 and PT-2467.** The
trace MAIN approved was meant to find where an invalid record diverges from
`_loadRefusal`. It found instead that **the case does not exist**: neither of
the two "silent failure" observations I filed reproduces, and my stated
cause for each is wrong. What remains is one real, well-worded message and a
harness problem of my own making.

---

## What I claimed, and what is actually true

| claimed | measured now |
|---|---|
| TEST 120: Constitution 3 makes a save the menu counts as `1 unreadable` | **Loads.** `Whisper · Jedi Consular · 12 · 2 of 2 · force 159 of 159` |
| TEST 120: Constitution 8 loads silently into an empty party | **Loads.** `38 of 38 · force 159 of 159` |
| TEST 121: a content `tag` not matching its blueprint `handle` makes a package's saves unreadable | **Loads.** Board draws, every creature placed — *including the mis-tagged one* — party intact |

The third was tested by deliberately breaking the **entry** area's tag,
`frail.wp.01` → `frailwp.01`, which is the strongest form of the claim. The
mis-tagged creature still appears on the board.

So renaming the tag is not what fixed `m05-one`. **The reload was.**

## Why I got it wrong

All three observations were real — I have the screens — but each was taken
during a stretch where I was fighting the load path, and I attributed the
symptom to the variable I happened to be changing rather than to the
navigation. The actual mechanism is the one I eventually diagnosed properly
and wrote up in TEST 121:

> Continue and Load Game are **disabled for a second or two** after the menu
> opens while the saves are scanned. A click in that window does not miss —
> it falls through to **New Game** and opens Character Generation, which
> then absorbs every later click.

A greyed Continue is that window. I read it as a rejected save because I had
just changed Constitution, and again as a broken package because I had just
added an area. **The variable I was holding is not the variable that
moved** — and I checked neither against a control before filing.

The empty-party screen I cannot place. It happened; sampling the sidebar at
0.3, 1.1, 2.6, 5.6 and 11.6 seconds after clicking Continue shows it absent
and then populated, with no `nobody else` state captured in between. I am
not going to invent a mechanism for it. It is one unreproduced screen, and
it should not be carrying a routed work item.

## What this means for the routed item

**PT-2466's premise was three cases; there is one, and it already works.**

* Case 1 — invalid record loading into an empty party: **does not
  reproduce.** No divergence point to find, because nothing diverges.
* Case 2 — package/area problem greying Continue: **does not reproduce.**
  It was the scanning window.
* Case 3 — the damaged save: **real, and already well worded** —
  `1 save · 1 unreadable: Damaged save: it says it holds 569 bytes of
  contents and the file has 529. Part of another save may have been written
  over it.` Both numbers and a likely cause, in one sentence.

The one thing worth keeping from PT-2467 is the structural fact, which is
still true and which I did verify by reading `eebd977`:

* `validateRecord` failures already have a worded refusal —
  `main.dart` builds `'This save cannot be opened.\n\n' + v.problems.map((p) => '• ${p.reason}')`
  and `'This character cannot be played.\n\n' + …`.
* The library card carries **only** a count — `library_row.dart:30`,
  `final Map<String, int> problems`, keyed by package path, with no string.

That asymmetry is genuine. **But I have no observed failure that needs it
closed**, so it is a tidiness item at most, not the severe one it was filed
as. If Coder wants a reproduction to work against, I do not have one to give.

## What I should have done

A control, before filing either observation. Loading the *unchanged* save
after seeing a greyed Continue would have shown the same greyed Continue,
and neither item would exist. Both were single readings of a flaky path,
reported as findings because the cause was plausible — which is the failure
mode I have a standing note about and did not apply to an aside.

⚠ The two reports are amended in place rather than left standing: TEST 120
and TEST 121 each carry a RETRACTED note pointing here. Everything else in
both reports was measured against controls and is unaffected — the
five-round durations, the ten droid refusals with their sentient controls,
the Force Confusion battery, and the `Present.placed` classifier finding all
stand.
