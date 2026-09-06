// Probe: does the experimental windowing API actually make a second native
// window on the STABLE channel, if the compile-time flag is set?
// Enabled with --dart-define=FLUTTER_ENABLED_FEATURE_FLAGS=windowing
import 'dart:io';
import 'package:flutter/widgets.dart';
// ignore: implementation_imports
import 'package:flutter/src/widgets/_window.dart';
// ignore: implementation_imports
import 'package:flutter/src/foundation/_features.dart';

void main() {
  stderr.writeln('isWindowingEnabled = $isWindowingEnabled');
  try {
    final c = RegularWindowController(
      delegate: RegularWindowControllerDelegate(),
      size: const Size(420, 300),
      title: 'Builder — second window',
    );
    stderr.writeln('PROBE: controller created OK, rootView=${c.rootView.viewId}');
    runWidget(ViewCollection(views: <Widget>[
      RegularWindow(
        controller: c,
        child: const Center(
          child: Text('second window', textDirection: TextDirection.ltr,
              style: TextStyle(fontSize: 22, color: Color(0xFF00FF88))),
        ),
      ),
    ]));
    stderr.writeln('PROBE: runWidget returned');
  } catch (e) {
    stderr.writeln('PROBE FAILED: $e');
    exit(3);
  }
}
