# SPIKE — FAIL CONDITIONS, WRITTEN BEFORE ANY CODE

**Committed before the first line of Dart.** If the spike is judged against
criteria invented afterwards, it is not evidence.

**The question:** does Flutter fight us when the acceptance criterion is
"identical to KOTOR"?

---

## ⚠ Hard fails — any one of these and I say Flutter is the wrong choice

**F1 · Nine-slice cannot be drawn with the border thickness decoupled from the
source texture.** KOTOR's `DIMENSION` is independent of the CORNER/EDGE texture
size — a 16-pixel border drawn from an 8-pixel corner is normal in the shipped
panels. If Flutter can only slice at the texture's own dimensions, every panel
in the game is unreproducible.

**F2 · Runtime tinting of a greyscale source is not possible without writing a
shader.** The whole UI is greyscale masks multiplied by a per-control colour.
If this needs a custom fragment shader in Flutter, the cost of every control
goes up by an order of magnitude.

**F3 · Bitmap-font glyphs cannot be placed at exact integer pixel positions.**
If the text renderer insists on subpixel positioning, hinting or its own
metrics, "identical" is off the table for every label in the game.

**F4 · Text input cannot be styled to match.** If Flutter's editable text drags
in platform chrome — a native caret, a selection colour, a context menu — that
cannot be restyled, then the one control we must invent looks foreign beside the
eight we are copying.

**F5 · The Linux desktop build does not work.** Not "is fiddly" — does not
produce a running window on this machine with a reasonable amount of effort.

---

## ⚠ Soft fails — two or more of these and the recommendation is in doubt

**S1** A required capability exists only in an unmaintained third-party package
(no release in ~12 months, or a single maintainer with open critical issues).

**S2** Any of the four builds takes more than about half a day of fighting, as
opposed to half a day of typing.

**S3** The engine interface has to be contorted to be callable from a widget —
if "ask, don't compute" forces async plumbing, global state, or a rebuild storm
just to show a derivation.

**S4** Pixel output is close but not exact, with no route to exact.

**S5** Native file dialogs, menus or a second window on Linux need a workaround
rather than a package call.

---

## What would NOT count as a fail

- **Verbosity.** Flutter is wordy. Wordy is not fighting.
- **Writing the nine-slice painter by hand.** Expected, and correct — a
  `CustomPainter` is the supported way to do custom drawing, not a workaround.
- **No built-in game loop or netcode.** Already known and priced in.
- **Having to build a bitmap-font renderer.** Also expected; the games use an
  atlas format nothing supports natively.
- **Toolchain friction in *this sandbox*.** I have no root here. If I must
  hand-assemble clang/cmake/ninja, that is a fact about this container, **not**
  about Flutter on the owner's Linux box — and I will say which is which.

---

## ⚠ Two blockers found before starting, reported not worked around

**B1 · `design/ENGINE-INTERFACE-01.md` does not exist in this repository.**
Searched the whole tree by filename and by content; also searched for `PT-1326`
and `resolve(check)`. Nothing. `STUDY/_reference/` holds thirteen documents and
this is not among them. **Same pattern as the `SKILLS-01` episode** — believed
pushed, not present.

I am not blocking on it. The brief itself specifies the essential contract in
one sentence — *`resolve(check)` must return the whole derivation, not a total,
because `PT-1326` renders "rolled 17 — d20 11 + rank 4 + aptitude 2 · needed
14"* — and that is enough to test the shape. **What I build for item 4 is
therefore my reconstruction from that sentence, not an implementation of the
spec, and every finding about it is provisional until the real document is
readable.**

**B2 · This sandbox has no root and no C toolchain.** `gcc`, `pkg-config` and
GTK 3.24.49 are present; `clang`, `cmake` and `ninja` are not, and `sudo`
requires a password. Flutter's Linux desktop target needs all three. I am
fetching them as unprivileged tarballs. **Per the exclusion above, difficulty
here is a property of the container and will be reported separately from any
property of Flutter.**
