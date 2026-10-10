// frames.dart VIDEO PTS_FILE FIRST_INDEX COUNT — per-frame metrics for a window of a 1920x1080 capture.
// Reads ffmpeg rgb24 frames and the packet pts (wall clock, -copyts) and prints one CSV row per frame:
//   pts, hp (mean abs change of the HP card text vs the previous frame), flash (red excess in the
//   bottom edge band), num (pixels of the damage colour over Onjo), miss (pixels of the miss colour
//   over Onjo), ring (Onjo's ring centre x,y found in the frame).
import 'dart:io';
import 'dart:math';
import 'dart:typed_data';

const w = 1920, h = 1080;

Future<void> main(List<String> a) async {
  final video = a[0];
  final all = File(a[1]).readAsLinesSync().where((l) => l.isNotEmpty).map(double.parse).toList();
  final k0 = int.parse(a[2]), count = int.parse(a[3]);
  final pts = all.sublist(k0, min(all.length, k0 + count));
  final first = pts.first;
  final rel = (all[k0] - all[0]).toStringAsFixed(4);
  final p = await Process.start('ffmpeg', ['-loglevel', 'error', '-ss', rel, '-i', video, '-frames:v', '$count', '-fps_mode', 'passthrough', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']);
  final n = w * h * 3;
  final buf = BytesBuilder(copy: false);
  Uint8List? prev;
  var i = 0;
  stdout.writeln('i,pts,hp,flash,num,miss,ringx,ringy');
  void frame(Uint8List f) {
    int px(int x, int y, int c) => f[(y * w + x) * 3 + c];
    // HP card text "N of 103"
    var hp = 0.0;
    if (prev != null) {
      var s = 0;
      // ⚠ BOTH PLACES ONJO'S CARD CAN BE: initiative is re-rolled every take and the turn order puts the first actor's card on
      // top, so "N of 103" is at y~294 (Onjo first) or y~388 (trooper first). The trooper's own card never changes here (Onjo
      // never attacks), so watching both rows reads Onjo's alone.
      for (final y0 in const [284, 378]) {
        for (var y = y0; y < y0 + 20; y++) {
          for (var x = 300; x < 400; x++) {
            for (var c = 0; c < 3; c++) {
              s += (f[(y * w + x) * 3 + c] - prev![(y * w + x) * 3 + c]).abs();
            }
          }
        }
      }
      hp = s / (20 * 100 * 3);
    }
    // the play pane's bottom edge band (over black, below the board), red excess
    var fl = 0.0;
    for (var y = 735; y < 793; y += 2) {
      for (var x = 500; x < 1780; x += 4) {
        fl += px(x, y, 0) - (px(x, y, 1) + px(x, y, 2)) / 2;
      }
    }
    fl /= (29 * 320);
    // Onjo's ring: cream pixels in the board, left of the trooper
    var sx = 0, sy = 0, cnt = 0;
    for (var y = 150; y < 740; y += 2) {
      for (var x = 700; x < 1560; x += 2) {
        final r = px(x, y, 0), g = px(x, y, 1), b = px(x, y, 2);
        if (r > 190 && g > 185 && b > 150 && (r - b) < 60 && (r - g).abs() < 20) {
          sx += x; sy += y; cnt++;
        }
      }
    }
    final cx = cnt == 0 ? 1096 : sx ~/ cnt, cy = cnt == 0 ? 476 : sy ~/ cnt;
    var num = 0, miss = 0;
    for (var y = max(0, cy - 62); y < cy - 27; y++) {
      for (var x = cx - 40; x < cx + 40; x++) {
        final r = px(x, y, 0), g = px(x, y, 1), b = px(x, y, 2);
        if ((r - 185).abs() < 45 && g < 90 && b < 60) num++;
        if (r > 170 && g > 170 && b > 140 && (r - b) < 50) miss++;
      }
    }
    final t = i < pts.length ? pts[i] : first + i / 60;
    stdout.writeln('$i,${t.toStringAsFixed(3)},${hp.toStringAsFixed(3)},${fl.toStringAsFixed(2)},$num,$miss,$cx,$cy');
    prev = f;
    i++;
  }

  await for (final chunk in p.stdout) {
    buf.add(chunk);
    while (buf.length >= n) {
      final all = buf.takeBytes();
      frame(Uint8List.sublistView(all, 0, n));
      if (all.length > n) buf.add(Uint8List.sublistView(all, n));
    }
  }
  await p.exitCode;
}
