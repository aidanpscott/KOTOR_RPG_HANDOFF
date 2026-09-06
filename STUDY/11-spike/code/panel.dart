import 'dart:convert';
import 'dart:ui' as ui;
import 'package:flutter/widgets.dart';
import 'package:flutter/services.dart';
import 'package:flutter/gestures.dart';
import 'bitmap_font.dart';
import 'nine_slice.dart';
import 'engine.dart';
import 'panel_data.dart';

// ---------------------------------------------------------------- model
class St {
  final String corner, edge, fill;
  final double dim, inner;
  final Color color;
  final int fillstyle;
  St(Map m)
      : corner = m['corner'] ?? '', edge = m['edge'] ?? '', fill = m['fill'] ?? '',
        dim = (m['dim'] as num).toDouble(), inner = (m['inner'] as num).toDouble(),
        color = _c(m['color']), fillstyle = m['fillstyle'] ?? 2;
  static Color _c(List? v) => v == null
      ? const Color(0xFFFFFFFF)
      : Color.fromARGB(255, (v[0] * 255).round(), (v[1] * 255).round(), (v[2] * 255).round());
}

class Ctl {
  final String tag, type, parent, font, text;
  final double l, t, w, h;
  final int? align;
  final Color? tcolor;
  final Map<String, St> states;
  Ctl(Map m)
      : tag = m['tag'], type = m['type'], parent = m['parent'] ?? '',
        font = m['font'] ?? '', text = m['text'] ?? '',
        l = (m['l'] as num).toDouble(), t = (m['t'] as num).toDouble(),
        w = (m['w'] as num).toDouble(), h = (m['h'] as num).toDouble(),
        align = m['align'], tcolor = m['tcolor'] == null ? null : St._c(m['tcolor']),
        states = {for (final e in (m['states'] as Map).entries) e.key: St(e.value)};
}

// ---------------------------------------------------------------- assets
class Art {
  final Map<String, ui.Image> img;
  final BitmapFont? font;
  Art(this.img, this.font);
  ui.Image? operator [](String n) => n.isEmpty ? null : img[n];

  static Future<Art> load(List<String> names) async {
    final m = <String, ui.Image>{};
    for (final n in names) {
      try {
        final d = await rootBundle.load('assets/$n.png');
        m[n] = (await (await ui.instantiateImageCodec(d.buffer.asUint8List())).getNextFrame()).image;
      } catch (_) {/* absent asset stays absent — never a placeholder */}
    }
    final f = m['dialogfont16x16'];
    return Art(m, f == null ? null : BitmapFont(f));
  }
}

// ---------------------------------------------------------------- states
/// KOTOR ships BORDER / HILIGHT / SELECTED / HILIGHTSELECTED. equip_p uses
/// only BORDER (54 controls) and HILIGHT (17). There is NO PRESSED state
/// anywhere in the format — PT-1113 asks for one, so it is SYNTHESISED here
/// and marked as ours. It is not read from the game.
enum Vis { normal, hilight, pressed, selected }

St pick(Ctl c, Vis v) {
  final b = c.states['BORDER'] ?? c.states.values.first;
  switch (v) {
    case Vis.normal:
      return b;
    case Vis.hilight:
      return c.states['HILIGHT'] ?? b;
    case Vis.selected:
      return c.states['SELECTED'] ?? c.states['HILIGHT'] ?? b;
    case Vis.pressed:
      return b;   // tint is darkened at the call site — see _tintFor
  }
}

Color _tintFor(Ctl c, Vis v) {
  final s = pick(c, v);
  if (v != Vis.pressed) return s.color;
  // OURS, not a copy: pressed = the HILIGHT hue driven down in value, so the
  // control reads as recessed rather than merely un-highlighted.
  final h = (c.states['HILIGHT'] ?? s).color;
  return Color.fromARGB(255, (h.red * 0.45).round(), (h.green * 0.45).round(), (h.blue * 0.45).round());
}

// ---------------------------------------------------------------- control
class ControlView extends StatelessWidget {
  final Ctl c; final Art art; final Vis vis; final String? label;
  const ControlView(this.c, this.art, {super.key, this.vis = Vis.normal, this.label});
  @override
  Widget build(BuildContext ctx) {
    final s = pick(c, vis);
    final txt = label ?? c.text;
    return NineSlice(
      corner: art[s.corner], edge: art[s.edge], fill: art[s.fill],
      dimension: s.dim, tint: _tintFor(c, vis), fillStyle: s.fillstyle,
      child: txt.isEmpty
          ? null
          : Padding(
              padding: EdgeInsets.all(s.inner),
              child: BitmapText(txt, font: art.font,
                  color: c.tcolor ?? const Color(0xFFFFFFFF), alignment: c.align ?? 17),
            ),
    );
  }
}

// ---------------------------------------------------------------- panel
class EquipPanel extends StatefulWidget {
  final Art art;
  final ValueChanged<Derivation>? onCheck;
  const EquipPanel(this.art, {super.key, this.onCheck});
  @override
  State<EquipPanel> createState() => _EP();
}

class _EP extends State<EquipPanel> {
  late final List<Ctl> all = (jsonDecode(panelJson) as List).map((m) => Ctl(m)).toList();
  String? _hover, _down;
  int _sel = -1;
  double _scroll = 0;

  // Rows for the list. Skills, so the engine call has something real to run on.
  static const _rows = [
    ('Repair', 4, 2, 14), ('Persuade', 6, 1, 18), ('Awareness', 2, 3, 12),
    ('Demolitions', 5, 0, 15), ('Security', 7, 2, 20), ('Treat Injury', 3, 1, 13),
    ('Computer Use', 4, 4, 16), ('Stealth', 1, 2, 11), ('Athletics', 3, 3, 14),
    ('Archaeology', 5, 1, 17), ('Xenology', 2, 2, 12), ('Mysticism', 6, 3, 19),
  ];

  Ctl? byTag(String t) { for (final c in all) { if (c.tag == t) return c; } return null; }

  @override
  Widget build(BuildContext ctx) {
    final proto = byTag('PROTOITEM');
    final lb = byTag('LB_ITEMS');
    final sb = all.firstWhere((c) => c.tag == 'SCROLLBAR', orElse: () => all.first);

    final children = <Widget>[];
    for (final c in all) {
      if (c.tag == 'PROTOITEM') continue;                 // a template, never drawn as itself
      if (c.parent == 'LB_ITEMS' && c.tag != 'SCROLLBAR') continue;
      final v = _down == c.tag
          ? Vis.pressed
          : (_hover == c.tag && c.states.containsKey('HILIGHT') ? Vis.hilight : Vis.normal);
      children.add(Positioned(
        left: c.l, top: c.t, width: c.w, height: c.h,
        child: MouseRegion(
          onEnter: (_) => setState(() => _hover = c.tag),
          onExit: (_) => setState(() => _hover = null),
          child: Listener(
            onPointerDown: (_) => setState(() => _down = c.tag),
            onPointerUp: (_) => setState(() => _down = null),
            child: ControlView(c, widget.art, vis: v),
          ),
        ),
      ));
    }

    // ---- the ProtoItem list, stamped from the template, clipped and scrolled
    if (proto != null && lb != null) {
      final rowH = proto.h + 2;
      final viewH = lb.h - 2 * (lb.states['BORDER']?.inner ?? 8);
      final maxScroll = (_rows.length * rowH - viewH).clamp(0.0, double.infinity);
      final inner = lb.states['BORDER']?.inner ?? 8;
      children.add(Positioned(
        left: lb.l + inner, top: lb.t + inner, width: lb.w - 2 * inner, height: viewH,
        child: ClipRect(
          child: Listener(
            onPointerSignal: (e) {
              if (e is PointerScrollEvent) {
                setState(() => _scroll = (_scroll + e.scrollDelta.dy).clamp(0.0, maxScroll));
              }
            },
            child: Stack(children: [
              for (var i = 0; i < _rows.length; i++)
                Positioned(
                  left: 0, top: i * rowH - _scroll, width: proto.w, height: proto.h,
                  child: MouseRegion(
                    onEnter: (_) => setState(() => _hover = 'row$i'),
                    onExit: (_) => setState(() => _hover = null),
                    child: Listener(
                      onPointerDown: (_) => setState(() { _down = 'row$i'; _sel = i; }),
                      onPointerUp: (_) {
                        setState(() => _down = null);
                        final r = _rows[i];
                        widget.onCheck?.call(resolve(
                            Check(skill: r.$1, rank: r.$2, aptitude: r.$3, dc: r.$4)));
                      },
                      child: ControlView(proto, widget.art,
                          label: '${_rows[i].$1}  ${_rows[i].$2}',
                          vis: _down == 'row$i'
                              ? Vis.pressed
                              : (_sel == i ? Vis.selected
                                 : (_hover == 'row$i' ? Vis.hilight : Vis.normal))),
                    ),
                  ),
                ),
            ]),
          ),
        ),
      ));
      // ---- the scrollbar thumb, sized to the visible fraction
      final frac = (viewH / (_rows.length * rowH)).clamp(0.1, 1.0);
      final track = sb.h - 2 * sb.states['BORDER']!.dim;
      children.add(Positioned(
        left: sb.l, width: sb.w,
        top: sb.t + sb.states['BORDER']!.dim +
            (maxScroll == 0 ? 0 : (_scroll / maxScroll) * track * (1 - frac)),
        height: track * frac,
        child: GestureDetector(
          onVerticalDragUpdate: (d) => setState(() => _scroll =
              (_scroll + d.delta.dy * (maxScroll / (track * (1 - frac)).clamp(1, track)))
                  .clamp(0.0, maxScroll)),
          child: ControlView(sb, widget.art, vis: Vis.hilight),
        ),
      ));
    }
    return SizedBox(width: 800, height: 600, child: Stack(children: children));
  }
}
