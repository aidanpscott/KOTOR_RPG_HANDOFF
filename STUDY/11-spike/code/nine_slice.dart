import 'dart:ui' as ui;
import 'package:flutter/widgets.dart';

/// KOTOR's border model: three greyscale masks (CORNER, EDGE, FILL) composed as
/// a nine-slice at an arbitrary DIMENSION and tinted at runtime.
///
/// ⚠ F1: the source textures are 32x32 and equip_p draws them at DIMENSION 16.
/// Border thickness is DECOUPLED from texture size — and edges and fills TILE
/// along the run rather than stretching. Stretching was my first attempt and it
/// smeared; the tile size is the DIMENSION, not the texture size.
class NineSlice extends StatelessWidget {
  final ui.Image? corner, edge, fill;
  final double dimension;
  final Color tint;
  final int fillStyle;
  final Widget? child;
  const NineSlice({super.key, this.corner, this.edge, this.fill,
      required this.dimension, required this.tint, this.fillStyle = 2, this.child});
  @override
  Widget build(BuildContext c) => CustomPaint(
        painter: _NinePainter(corner, edge, fill, dimension, tint, fillStyle),
        child: child,
      );
}

class _NinePainter extends CustomPainter {
  final ui.Image? corner, edge, fill;
  final double d;
  final Color tint;
  final int fillStyle;
  _NinePainter(this.corner, this.edge, this.fill, this.d, this.tint, this.fillStyle);

  /// ⚠ FILTER QUALITY IS PER-DRAW, NOT GLOBAL.
  /// A 32x32 mask drawn at DIMENSION 16 is a 2:1 downscale and needs filtering;
  /// a mask drawn at its own size must be nearest-neighbour or the edge softens
  /// and exact placement (F3) fails. Same painter, opposite answers.
  Paint _paint(Rect src, Rect dst) => Paint()
    ..colorFilter = ColorFilter.mode(tint, BlendMode.modulate)
    ..filterQuality = (dst.width < src.width || dst.height < src.height)
        ? FilterQuality.medium
        : FilterQuality.none
    ..isAntiAlias = false;

  /// Tile [img] across [dst] in [tile]-sized steps, clipped to dst.
  void _tile(Canvas cv, ui.Image img, Rect dst, double tw, double th,
      {int quarterTurns = 0}) {
    if (dst.width <= 0 || dst.height <= 0 || tw <= 0 || th <= 0) return;
    final src = Rect.fromLTWH(0, 0, img.width.toDouble(), img.height.toDouble());
    final p = _paint(src, Rect.fromLTWH(0, 0, tw, th));
    cv.save();
    cv.clipRect(dst);
    for (double y = dst.top; y < dst.bottom; y += th) {
      for (double x = dst.left; x < dst.right; x += tw) {
        final cell = Rect.fromLTWH(x, y, tw, th);
        if (quarterTurns == 0) {
          cv.drawImageRect(img, src, cell, p);
        } else {
          cv.save();
          cv.translate(cell.center.dx, cell.center.dy);
          cv.rotate(quarterTurns * 1.5707963267948966);
          cv.drawImageRect(img, src,
              Rect.fromCenter(center: Offset.zero, width: tw, height: th), p);
          cv.restore();
        }
      }
    }
    cv.restore();
  }

  void _one(Canvas cv, ui.Image img, Rect dst, {int quarterTurns = 0}) {
    if (dst.width <= 0 || dst.height <= 0) return;
    final src = Rect.fromLTWH(0, 0, img.width.toDouble(), img.height.toDouble());
    final p = _paint(src, dst);
    if (quarterTurns == 0) { cv.drawImageRect(img, src, dst, p); return; }
    cv.save();
    cv.translate(dst.center.dx, dst.center.dy);
    cv.rotate(quarterTurns * 1.5707963267948966);
    cv.drawImageRect(img, src,
        Rect.fromCenter(center: Offset.zero, width: dst.width, height: dst.height), p);
    cv.restore();
  }

  @override
  void paint(Canvas cv, Size s) {
    final w = s.width, h = s.height;
    // FILL: tiled at the texture's own size when there is a DIMENSION to scale
    // by, otherwise stretched (the 1024x1024 backdrop is a stretch, not a tile).
    if (fill != null && fillStyle != 0) {
      final dst = Rect.fromLTWH(d, d, w - 2 * d, h - 2 * d);
      if (fill!.width >= 256) {
        _one(cv, fill!, dst);                       // full-panel art: stretch
      } else {
        _tile(cv, fill!, dst, fill!.width.toDouble(), fill!.height.toDouble());
      }
    }
    if (d > 0) {
      if (edge != null) {
        _tile(cv, edge!, Rect.fromLTWH(d, 0, w - 2 * d, d), d, d);
        _tile(cv, edge!, Rect.fromLTWH(d, h - d, w - 2 * d, d), d, d, quarterTurns: 2);
        _tile(cv, edge!, Rect.fromLTWH(0, d, d, h - 2 * d), d, d, quarterTurns: 3);
        _tile(cv, edge!, Rect.fromLTWH(w - d, d, d, h - 2 * d), d, d, quarterTurns: 1);
      }
      if (corner != null) {
        _one(cv, corner!, Rect.fromLTWH(0, 0, d, d));
        _one(cv, corner!, Rect.fromLTWH(w - d, 0, d, d), quarterTurns: 1);
        _one(cv, corner!, Rect.fromLTWH(w - d, h - d, d, d), quarterTurns: 2);
        _one(cv, corner!, Rect.fromLTWH(0, h - d, d, d), quarterTurns: 3);
      }
    }
  }

  @override
  bool shouldRepaint(_NinePainter o) =>
      o.tint != tint || o.d != d || o.corner != corner || o.edge != edge || o.fill != fill;
}
