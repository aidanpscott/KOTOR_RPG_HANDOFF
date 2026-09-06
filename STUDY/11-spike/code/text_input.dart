import 'package:flutter/widgets.dart';
import 'package:flutter/services.dart';
import 'bitmap_font.dart';
import 'nine_slice.dart';
import 'dart:ui' as ui;

/// F4: a text input that keeps the KOTOR frame and the bitmap font.
/// KOTOR has NO text entry control — the nine GUI control types include none.
/// So this is OURS, and the test is whether Flutter lets a caret and an IME
/// live inside a painter we control, rather than inside its own Material box.
class KotorTextInput extends StatefulWidget {
  final BitmapFont? font;
  final ui.Image? corner, edge, fill;
  final Color tint, textColor;
  final double dimension;
  final ValueChanged<String>? onSubmit;
  const KotorTextInput({super.key, this.font, this.corner, this.edge, this.fill,
      required this.tint, required this.textColor, this.dimension = 16, this.onSubmit});
  @override
  State<KotorTextInput> createState() => _S();
}

class _S extends State<KotorTextInput> {
  final _c = TextEditingController();
  final _f = FocusNode();
  int _caretPhase = 0;

  @override
  void initState() {
    super.initState();
    _c.addListener(() => setState(() {}));
    _f.addListener(() => setState(() {}));
    _tick();
  }
  void _tick() async {
    while (mounted) {
      await Future.delayed(const Duration(milliseconds: 450));
      if (mounted) setState(() => _caretPhase ^= 1);
    }
  }
  @override
  void dispose() { _c.dispose(); _f.dispose(); super.dispose(); }

  @override
  Widget build(BuildContext ctx) {
    final txt = _c.text;
    return GestureDetector(
      onTap: () => _f.requestFocus(),
      child: NineSlice(
        corner: widget.corner, edge: widget.edge, fill: widget.fill,
        dimension: widget.dimension,
        tint: _f.hasFocus ? widget.tint : widget.tint.withOpacity(0.55),
        child: Stack(children: [
          // The real editing machinery, made invisible. Flutter still owns the
          // IME, the selection, the platform key handling — we own every pixel.
          Opacity(
            opacity: 0.0,
            child: EditableText(
              controller: _c, focusNode: _f,
              style: const TextStyle(fontSize: 16, color: Color(0xFFFFFFFF)),
              cursorColor: const Color(0xFFFFFFFF),
              backgroundCursorColor: const Color(0x00000000),
              onSubmitted: (v) { widget.onSubmit?.call(v); _c.clear(); },
              inputFormatters: [LengthLimitingTextInputFormatter(64)],
            ),
          ),
          Padding(
            padding: EdgeInsets.symmetric(horizontal: widget.dimension + 4),
            child: BitmapText(
              txt + (_f.hasFocus && _caretPhase == 1 ? '_' : ''),
              font: widget.font, color: widget.textColor, alignment: 1 | 16,
            ),
          ),
        ]),
      ),
    );
  }
}
