/// ⚠ PROVENANCE WARNING. The brief says "design/ENGINE-INTERFACE-01.md is now
/// written — read it". THAT FILE DOES NOT EXIST in the repo (searched by name
/// and by content, and for PT-1326 and "resolve(check)"). Everything below is
/// RECONSTRUCTED from the brief's single sentence:
///
///   resolve(check) "must return the whole derivation, not a total, because
///    PT-1326 renders 'rolled 17 — d20 11 + rank 4 + aptitude 2 · needed 14'"
///
/// The shape is inferred from that ONE rendered string. Treat as provisional.
library;

import 'dart:math';

class Term {
  final String label;   // "d20", "rank", "aptitude"
  final int value;
  const Term(this.label, this.value);
}

class Check {
  final String skill;
  final int rank, aptitude, dc;
  const Check({required this.skill, required this.rank, required this.aptitude, required this.dc});
}

/// The WHOLE derivation. Not a total, not a bool — every term the UI must name.
class Derivation {
  final Check check;
  final List<Term> terms;
  final int total, needed;
  bool get success => total >= needed;
  const Derivation(this.check, this.terms, this.total, this.needed);

  /// Reproduces PT-1326's string exactly:
  /// "rolled 17 — d20 11 + rank 4 + aptitude 2 · needed 14"
  String render() {
    final b = StringBuffer('rolled $total — ');
    for (var i = 0; i < terms.length; i++) {
      if (i > 0) b.write(terms[i].value < 0 ? ' - ' : ' + ');
      b.write('${terms[i].label} ${terms[i].value.abs()}');
    }
    b.write(' · needed $needed');
    return b.toString();
  }
}

final _rng = Random();

Derivation resolve(Check c, {int? forcedRoll}) {
  final d20 = forcedRoll ?? (_rng.nextInt(20) + 1);
  final terms = <Term>[Term('d20', d20), Term('rank', c.rank), Term('aptitude', c.aptitude)];
  return Derivation(c, terms, terms.fold(0, (a, t) => a + t.value), c.dc);
}
