import 'dart:io';
import 'dart:ui' as ui;
import 'package:flutter/rendering.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:file_selector/file_selector.dart';
import 'panel.dart';
import 'text_input.dart';
import 'engine.dart';
import 'bitmap_font.dart';

const kTextures = [
  'dialogfont16x16','pnl_pause_pc','uibit_arrow_l','uibit_arrow_r',
  'uibit_brdr_16bct','uibit_brdr_16bet','uibit_brdr_16gc','uibit_brdr_16ge',
  'uibit_brdr_16wc','uibit_brdr_16wct','uibit_brdr_16we','uibit_brdr_16wet',
  'uibit_eqp_cnfg_p','uibit_eqp_shld_p','uibit_fill_2bt','uibit_fill_2wt','uibit_stf_1_p',
];

void main() => runApp(const Spike());

class Spike extends StatefulWidget {
  const Spike({super.key});
  @override
  State<Spike> createState() => _S();
}

class _S extends State<Spike> {
  final GlobalKey _cap = GlobalKey();
  Art? art;
  Derivation? last;
  String typed = '';
  String? openedPath;

  @override
  void initState() {
    super.initState();
    Art.load(kTextures).then((a) {
      setState(() => art = a);
      // Capture our OWN pixels at exactly 1.0 device ratio. No X11 grab, no
      // window manager, no overlapping windows — this is what we drew.
      _shoot('/home/aidan/spike/cap_idle.png', const Duration(milliseconds: 900));
      // captured mid-gesture while xdotool holds the button down over a row
      _shoot('/home/aidan/spike/cap_press.png', const Duration(seconds: 9));
    });
  }

  Future<void> _shoot(String path, Duration wait) async {
    await Future.delayed(wait);
    final b = _cap.currentContext?.findRenderObject() as RenderRepaintBoundary?;
    if (b == null) { stderr.writeln('CAPTURE: no boundary'); return; }
    final im = await b.toImage(pixelRatio: 1.0);
    final d = await im.toByteData(format: ui.ImageByteFormat.png);
    if (d != null) File(path).writeAsBytesSync(d.buffer.asUint8List());
    stderr.writeln('CAPTURED $path  ${im.width}x${im.height}');
  }

  // ---- 3: the Builder's desktop spine -----------------------------------
  Future<void> _open() async {
    final f = await openFile(acceptedTypeGroups: const [
      XTypeGroup(label: 'campaign package', extensions: ['json', 'zip'])
    ]);
    setState(() => openedPath = f?.path ?? '(cancelled)');
    _shoot('/home/aidan/spike/cap_open.png', const Duration(milliseconds: 300));
  }
  Future<void> _saveAs() async {
    final loc = await getSaveLocation(suggestedName: 'package.json');
    setState(() => openedPath = loc?.path ?? '(cancelled)');
  }
  void _second() {
    // ⚠ SECOND WINDOW. Flutter's stable channel exposes NO API for a second
    // native window on Linux. Reported honestly rather than faked — see report.
    setState(() => openedPath = 'second window: NOT AVAILABLE on stable');
  }

  @override
  Widget build(BuildContext c) {
    final a = art;
    return MaterialApp(
      title: 'KOTOR fidelity spike',
      home: CallbackShortcuts(
        bindings: <ShortcutActivator, VoidCallback>{
          const SingleActivator(LogicalKeyboardKey.keyO, control: true): _open,
          const SingleActivator(LogicalKeyboardKey.keyS, control: true): _saveAs,
          const SingleActivator(LogicalKeyboardKey.keyN, control: true): _second,
        },
        child: Focus(
        autofocus: true,
        child: PlatformMenuBar(
        menus: [
          PlatformMenu(label: 'File', menus: [
            PlatformMenuItem(label: 'Open Package…', onSelected: _open),
            PlatformMenuItem(label: 'Save As…', onSelected: _saveAs),
            PlatformMenuItem(label: 'New Window', onSelected: _second),
          ]),
        ],
        child: Scaffold(
          backgroundColor: const Color(0xFF000000),
          // ⚠ PlatformMenuBar above is a NO-OP on Linux (macOS only, per the
          // framework's own docs). This drawn MenuBar is what actually works.
          appBar: PreferredSize(
            preferredSize: const Size.fromHeight(34),
            child: MenuBar(children: [
              SubmenuButton(menuChildren: [
                MenuItemButton(onPressed: _open, child: const Text('Open Package…')),
                MenuItemButton(onPressed: _saveAs, child: const Text('Save As…')),
                MenuItemButton(onPressed: _second, child: const Text('New Window')),
              ], child: const Text('File')),
              SubmenuButton(menuChildren: [
                MenuItemButton(onPressed: () {}, child: const Text('Undo')),
              ], child: const Text('Edit')),
            ]),
          ),
          body: a == null
              ? const SizedBox()
              // ⚠ NO FittedBox. Scaling by a non-integer factor destroys exact
              // pixel placement (F3). The panel renders 1:1 at its authored size.
              : Center(
                  child: RepaintBoundary(
                    key: _cap,
                    child: SizedBox(
                      width: 800, height: 620,
                      child: Stack(children: [
                        EquipPanel(a, onCheck: (d) {
                          setState(() => last = d);
                          _shoot('/home/aidan/spike/cap_engine.png',
                              const Duration(milliseconds: 250));
                        }),
                        // ---- 4: the engine call, rendered as a derivation
                        Positioned(
                          left: 78, top: 508, width: 640, height: 22,
                          child: BitmapText(last?.render() ?? 'pick a skill',
                              font: a.font,
                              color: last == null
                                  ? const Color(0xFF1AB28C)
                                  : (last!.success ? const Color(0xFF6FE0A8) : const Color(0xFFE06F6F)),
                              alignment: 1 | 16),
                        ),
                        // ---- 2: the text input
                        Positioned(
                          left: 78, top: 534, width: 640, height: 40,
                          child: KotorTextInput(
                            font: a.font,
                            corner: a['uibit_brdr_16wct'], edge: a['uibit_brdr_16wet'],
                            fill: a['uibit_fill_2wt'],
                            tint: const Color(0xFF0D593F), textColor: const Color(0xFF1AB28C),
                            dimension: 16,
                            onSubmit: (v) {
                              setState(() => typed = v);
                              _shoot('/home/aidan/spike/cap_typed.png',
                                  const Duration(milliseconds: 250));
                            },
                          ),
                        ),
                        Positioned(
                          left: 78, top: 578, width: 640, height: 20,
                          child: BitmapText(
                              openedPath != null ? 'path: $openedPath'
                                  : (typed.isEmpty ? '' : 'said: $typed'),
                              font: a.font, color: const Color(0xFF8899AA), alignment: 1 | 16),
                        ),
                      ]),
                    ),
                  ),
                ),
        ),
      ),
      ),
      ),
    );
  }
}
