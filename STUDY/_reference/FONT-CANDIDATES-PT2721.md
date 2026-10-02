# FONT-CANDIDATES-PT2721 — identifying K2's real typeface

**`PT-2721`'s first owner ruling: identify the real font, or the closest real one, bring three candidates with sourcing and a side-by-side, then stop and wait for the file. This is that report. No font has been downloaded for bundling, and nothing in the app has changed — the atlas renderer (`lib/play/kotor_font.dart`) still draws the Equip screen until the owner's file arrives.**

Side-by-side image: `HANDOFF/STUDY/_reference/pt2721-font-candidates/side-by-side.png`. Individual specimens in the same folder.

---

## The reference: K2's own glyphs, rendered clean

`k2-own-render.png` — our own renderer (`KotorText`, `PT-2719`), drawing `fnt_dialog16x16`'s real atlas at 3× scale, no Flutter font engine involved. This is the real asset, not a guess: "EQUIP", "LIGHT COMBAT SUIT (EQUIPPED)", "ATTACK MODIFIER", "0123456789".

**One honest caveat up front**: `fnt_dialog16x16` is a 16-pixel-tall bitmap. At that resolution, what looks like a flared or serifed capital "I" could be a genuine design feature OR pixel-grid rounding at a small size — I can't fully separate the two from a bitmap alone, and the one directly-game-derived outside source I could check (see "Old Republic," below) points the other way. Flagged rather than trusted.

## Candidate 1 — Galahad (Adobe Originals, 1995, Alan Blackman)

**Evidence it's the real one**: the file-naming convention. K2/NWN's own Aurora-engine asset set ships a font literally named `fnt_galahad14` — confirmed via the KOTOR Font Tool / NWN Font Maker documentation on Deadlystream, whose own generated-output convention is to name a font `fnt_galahad14.tga`/`.txi` when it's built from the real Galahad typeface. That strongly suggests BioWare's own original toolchain used the same convention: `fnt_galahad14` is Galahad. What it does NOT confirm is that `fnt_dialog16x16` specifically — the font actually in use on the Equip screen — is the same face; K2 ships several distinct `fnt_*` assets for different UI purposes, and this is naming evidence for the FAMILY, not a slot-for-slot proof for this one asset.

**Visual check**: `candidate-galahad.png`, a real 1995 specimen (Luc Devroye's type-design reference page, sourced from Alan Blackman's own foundry images). Described by its own foundry page as "a cross between Optima and the flat-pen writing of Friedrich Neugebauer" — and the specimen shows it: visibly rough-edged, hand-calligraphic, flared serif-like terminals (the capital "I" does carry a flare, which lines up with the K2 render's own "I" — the one real visual echo found). But the overall character is a hand-lettered DISPLAY face, not a clean geometric technical face, and that's a real mismatch against how uniform and blocky K2's own render looks. **Said plainly: the naming evidence is strong, the visual match is not — this is a candidate on documentation, not on sight.**

**Source/licence**: Adobe Fonts (bundled with a Creative Cloud subscription), or standalone "Galahad Std" from Fontspring (~$29, Adobe-licensed).

## Candidate 2 — Bank Gothic (Morris Fuller Benton, 1930s; several digital revivals)

**Evidence**: a KOTOR-modding community thread (Deadlystream's KOTOR Font Tool discussion) names Bank Gothic directly as the closest real substitute for the dialogue/HUD font when a modder needed something Fontmaker-compatible and the fan "Old Republic" font (below) lacked lowercase glyphs. Wikipedia's own description — "rectilinear geometric sans-serif," "capitals-only" in its original release, became genre-standard for "a science-fiction, military, corporate … aesthetic" — matches the GENRE K2's UI is going for.

**Visual check**: `candidate-bankgothic.png` (Wikipedia's own specimen, `File:BankGothicsp.svg`). This is, by eye, the closer visual match of the two real commercial candidates: clean, squared, geometric letterforms, a rounded-rectangle "0" in a similar proportion to K2's own, no stray serifs. The capital "I" is a plain stroke — not a match for the flare in K2's own render, which is the one point against it.

**Source/licence**: GroupType's revival (MyFonts, paid) or ParaType's `BankGothicC TT` family (MyFonts, paid). No free/OFL version exists under the original name.

## Candidate 3 — Aldrich (Google Fonts, SIL Open Font License)

**Evidence**: same geometric-techno-sans genre as Bank Gothic — included here specifically because it is FREE and fully redistributable (OFL), with a ready Flutter package (`google_fonts`), so if Bank Gothic's licence is unwanted this is a same-genre fallback with zero friction to actually bundle.

**Visual check**: not obtained this pass — Google Fonts' specimen page is JavaScript-rendered and didn't return a usable static image or description through the tools available this cycle. Named on genre and licence, not on a side-by-side; flagged honestly rather than illustrated with something I didn't actually look at.

**Source/licence**: fonts.google.com/specimen/Aldrich, free, OFL.

## Not a numbered candidate, but worth having: "Old Republic" (DaFont, Trollax Kinora)

A fan font built BY tracing K2's own screenshots — the creator's own note: "reproduces lettering from the Lucas Arts game… made my own from screens of the game." `fallback-old-republic.png` is its real specimen. Visually it is the closest of everything checked this pass to K2's own geometric, clean, no-flourish look — unsurprising, since it was built the same way our own glyph-atlas renderer was: by copying the pixels rather than sourcing the original design. **This is exactly the kind of recreation the owner asked to move away from**, so it isn't the recommendation — but it's the most direct visual anchor available, and if neither real candidate above satisfies on sight, it's the fallback that's already free (check its licence terms for anything beyond personal use before shipping it).

---

## Recommendation

**Bank Gothic first, Aldrich as its free-licence twin, Galahad third.** The visual evidence favours Bank Gothic over Galahad even though Galahad has the stronger paper trail (the literal filename in K2's own asset family) — reported as a real disagreement between two kinds of evidence rather than smoothed into one answer. If the owner wants to spend nothing, Aldrich is the same genre as Bank Gothic under a free licence. Galahad stays a real candidate on the strength of the naming evidence alone, worth trying if the other two don't look right once rendered at full size — a 16-pixel bitmap and a handful of static specimen images are not a substitute for the owner's own eye on the actual file.

**Stopping here, as instructed.** No font downloaded for bundling. Once the owner hands over a file (`~/kotor-repos/books/fonts/` or wherever they say), the swap is: bundle it as the app's font, move every Equip text site off `KotorText` to it, pull size/letter-spacing/colour from `equip_p.gui`'s own controls, retire the atlas renderer, and keep the semantics-always-present fix (`PT-2720` item 1) alive in whatever replaces it.

---

## ⚠ CHOSEN — BankGothic Md BT (owner ruling, `PT-2721`)

The owner chose **Candidate 2, Bank Gothic**, in Bitstream's "BankGothic Md BT" cut: `BankGothicMediumBT.ttf`, **v4.4 (1998)**. It is bundled in the **private** app repository (`assets/fonts/`) and **nowhere else — never in this public repo**; the font file itself is not here, only pictures made with it.

**Picture:** `STUDY/_reference/pt2721-font-candidates/equip-font-side-by-side.png` — K2's own text on top (the real `fnt_dialog16x16` atlas at 3×), the same four strings in the Equip screen's font below, at the same cell (48 = 3 × 16), colours and row pitch.

**How it is sized.** K2's capitals fill 8 px of the 16 px cell (measured off the extracted atlas, rows 3–10); BankGothic's capitals are 0.52 em (measured by rendering "H": 104 px at 200 px). The Equip call sites speak in K2's cell, so the font size is scaled by 0.50 / 0.52 in one place (`EquipText`, `kEquipFontScale`) so the **capitals are K2's height**. K2's `spacingR` is 0, so no spacing is added. A test re-measures the capitals by rendering the real file.

**⚠ WHAT THE PICTURE SHOWS, AND IT IS NOT SMALL.** At K2's capital height Bank Gothic is **much wider** than K2's face: "LIGHT COMBAT SUIT (EQUIPPED)" runs about 880 px against K2's 490 px at 3× — roughly **1.8×**. It is an extended typeface; K2's bitmap font is narrow. It fits the Equip screen's fixed boxes at 1920×1080 (the list rows, the description pane, the buttons and the portrait block were rendered and checked), but every string will read visibly wider than K2's. Bank Gothic also draws lowercase as small capitals, so "Light Combat Suit" reads as "LIGHT COMBAT SUIT" with larger first letters. If the width is not wanted, the options are a narrower face, or the same face at a smaller size (capitals then shorter than K2's) — the owner's call, with this picture.

**⚠⚠⚠ THE LICENCE IS NOT SETTLED.** The zip carried no licence text and its source site listed the licence as "Unknown"; it is a commercial Bitstream typeface. Settle it before the app is shared with anyone.

The atlas renderer (`KotorText`, `fnt_dialog16x16`'s extracted texture and glyph table) is retired; `scripts/extract_equip_font.py` goes with it.
