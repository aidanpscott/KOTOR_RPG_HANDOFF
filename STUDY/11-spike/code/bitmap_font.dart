import 'dart:ui' as ui;
import 'package:flutter/widgets.dart';

/// KOTOR's dialogfont16x16: a 256x256 atlas, 16x16 grid of 16x16 cells,
/// cell index = codepoint. Fixed advance, no kerning, no shaping.
///
/// ⚠ F3 tests whether Flutter will place a glyph at an EXACT integer pixel.
/// Flutter's own text stack will not — it shapes, hints and subpixel-positions.
/// So this bypasses it entirely and blits cells from the atlas.
class BitmapFont {
  final ui.Image atlas;
  final int cell, cols;
  const BitmapFont(this.atlas, {this.cell = 16, this.cols = 16});
  double get lineHeight => cell.toDouble();
  double measure(String s) => s.length * cell.toDouble();
}

class BitmapText extends StatelessWidget {
  final String text;
  final BitmapFont? font;
  final Color color;
  final int alignment;    // KOTOR bitfield: 1 L, 2 HC, 4 R, 8 T, 16 VC, 32 B
  const BitmapText(this.text, {super.key, this.font, required this.color, this.alignment = 17});
  @override
  Widget build(BuildContext c) =>
      CustomPaint(painter: font == null ? null : _TextPainter(text, font!, color, alignment));
}

class _TextPainter extends CustomPainter {
  final String text; final BitmapFont f; final Color color; final int align;
  _TextPainter(this.text, this.f, this.color, this.align);

  @override
  void paint(Canvas cv, Size s) {
    if (text.isEmpty) return;
    final w = f.measure(text), h = f.lineHeight;
    double x, y;
    if (align & 4 != 0) { x = s.width - w; }
    else if (align & 2 != 0) { x = (s.width - w) / 2; }
    else { x = 0; }
    if (align & 32 != 0) { y = s.height - h; }
    else if (align & 16 != 0) { y = (s.height - h) / 2; }
    else { y = 0; }
    // ⚠ EXACT INTEGER PLACEMENT. Round once, here, then never fractional again.
    x = x.roundToDouble(); y = y.roundToDouble();

    final p = Paint()
      ..colorFilter = ColorFilter.mode(color, BlendMode.modulate)
      ..filterQuality = FilterQuality.none
      ..isAntiAlias = false;

    // One atlas -> drawAtlas is the right call: a single draw for the whole run.
    final tf = <RSTransform>[]; final rc = <Rect>[];
    for (var i = 0; i < text.length; i++) {
      final cp = text.codeUnitAt(i);
      if (cp == 32) continue;
      if (cp > 255) continue;                     // atlas is 256 cells; no fallback
      final cx = (cp % f.cols) * f.cell, cy = (cp ~/ f.cols) * f.cell;
      rc.add(Rect.fromLTWH(cx.toDouble(), cy.toDouble(), f.cell.toDouble(), f.cell.toDouble()));
      tf.add(RSTransform(1, 0, x + i * f.cell, y));
    }
    if (tf.isEmpty) return;
    cv.drawAtlas(f.atlas, tf, rc, null, null, null, p);
  }

  @override
  bool shouldRepaint(_TextPainter o) => o.text != text || o.color != color || o.align != align;
}
