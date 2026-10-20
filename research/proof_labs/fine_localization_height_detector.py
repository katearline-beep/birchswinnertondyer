#!/usr/bin/env python3
"""Actual local Kummer data and a conditional supported-obstruction detector.

Arithmetic inputs are recomputed; the Selmer/compact-support naturality
statement is a source/derivation obligation, not certified by these tests.
"""
import contextlib
import io
import itertools
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parents[2]
P = 11
NAMES = ('P1', 'P2', 'P3', 'P4', 'R')


def need(ok, message):
    if not ok:
        raise AssertionError(message)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b)) % P


def mv(a, x):
    return [dot(row, x) for row in a]


def rank(a):
    if not a:
        return 0
    a = [[x % P for x in row] for row in a]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        u = pow(a[r][j], -1, P)
        a[r] = [u * x % P for x in a[r]]
        for i in range(len(a)):
            if i != r:
                u = a[i][j]
                a[i] = [(x - u * y) % P for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def actual_local_columns():
    # Existing independent guarded projective implementation: no height data.
    with contextlib.redirect_stdout(io.StringIO()):
        m = runpy.run_path(str(ROOT / 'research/split11/independent_jacobian_all_columns.py'))
    columns = {name: list(m['result'][name]) for name in NAMES}
    return columns, [[columns[name][v] % P for name in NAMES] for v in (0, 1)]


def compare_pari(columns, text):
    need('***' not in text, 'PARI interpreter error')
    rows = {}
    for line in text.splitlines():
        if line.startswith('LOCAL '):
            fields = line.split()
            need(len(fields) == 4 and fields[1] in NAMES, 'bad PARI local row')
            need(fields[1] not in rows, 'duplicate PARI local row')
            rows[fields[1]] = [int(fields[2]), int(fields[3])]
    need(set(rows) == set(NAMES), 'incomplete PARI local columns')
    expected = {name: [x % 121 for x in columns[name]] for name in NAMES}
    need(rows == expected, 'PARI/minimal-model local mismatch')
    need('PASS PARI fine-localization inputs' in text, 'missing PARI completion')
    aux = [line.split() for line in text.splitlines() if line.startswith('AUX ')]
    need(aux == [['AUX', '3389', '154', '3498', '668', '1888',
                  '1', '10', '5', '4', '8']], 'PARI auxiliary-prime mismatch')


def actual_height_p2_r():
    # Recompute this one decisive complete first height by the existing
    # direct-coordinate denominator-ideal oracle, not by a local-log proxy.
    m = runpy.run_path(str(ROOT / 'research/anticyclotomic_11/direct_coordinate_height_mod11.py'))
    F, K, Curve = m['F'], m['Quadratic'], m['Curve']
    k = K(2)
    e = Curve(k, (1, -1, 0, -79, 289))
    p2 = (k.elt(5), k.elt(-2))
    sx = k.elt(F(-3355, 63))
    sy = k.elt(F(-128780, 1323), F(257560, 1323))
    r = (k.div(k.add(sx, k.elt(1)), k.elt(4)),
         k.div(k.sub(sy, k.add(sx, k.elt(1))), k.elt(8)))
    value, ratio = m['self_height'](e, e.add(p2, r), 11, 18, 7)
    need(value == 2 and pow(ratio, 4, 121) == 34,
         'decisive global first-height input changed')
    return value, ratio


def character_unit_control():
    # r is the ratio at sqrt(-7)=+2 used for the BCLMN orientation.
    # C0033 chooses the opposite embedding, so r_artin = r^(-1).
    count = 0
    for r in range(1, 121):
        if r % P == 0:
            continue
        rho = -((pow(r, 10, 121) - 1) // P) * pow(10, -1, P) % P
        ell = (pow(pow(r, -1, 121), 10, 121) - 1) // P % P
        need(ell == 10 * rho % P, 'character unit calibration failed')
        count += 1
    need(count == 110, 'incomplete unit calibration')
    need(10 % P != 0 and pow(10, -1, P) != 0, 'character factor is not a unit')
    print('PASS: all110 unit ratios calibrate Artin ell=10*rho mod11')


def auxiliary_support_controls(fine):
    m = runpy.run_path(str(ROOT / 'research/proof_labs/kummer_reduction_11_certificate.py'))
    primes = [(127, 45), (743, 109), (907, 30), (1087, 373), (1117, 542)]
    restrictions = []
    for q, root in primes:
        c = m['row_at'](q, root)
        cc = m['row_at'](q, q - root)
        need(c['order'] % P == 0 and c['order'] % (P * P) != 0,
             'auxiliary prime fails torsion-direction criterion')
        # Positive fine MW points have identical reductions at the two
        # conjugate places. The selected cyclic generators also agree here.
        need(c['row'][:4] == cc['row'][:4], 'conjugate positive rows differ')
        restrictions.append([dot(c['row'], y) for y in fine])
    target = [2, 5, 10]
    passes = []
    fails = []
    for size in range(6):
        for subset in itertools.combinations(range(5), size):
            rows = [restrictions[i] for i in subset]
            span_contains = rank(rows + [target]) == rank(rows)
            # Independent dual-certificate search, rather than the same
            # row reduction twice: find a surviving fine-class witness.
            witness = next((x for x in itertools.product(range(P), repeat=3)
                            if all(dot(row, x) == 0 for row in rows)
                            and dot(target, x) != 0), None)
            need(span_contains == (witness is None),
                 'support row-span test disagrees with dual witness search')
            record = tuple(primes[i][0] for i in subset)
            (passes if span_contains else fails).append(record)
    need(len(passes) + len(fails) == 32, 'support search incomplete')
    minimum = min(map(len, passes))
    need(minimum >= 2, 'a single candidate unexpectedly kills the known detector')
    explicit = [1, 0, 1]
    need(dot(restrictions[0], explicit) == 0 and dot(target, explicit) == 1,
         'explicit q127 obstruction witness failed')
    print('ACTUAL auxiliary-prime rows on fine basis:',
          {q: row for (q, _), row in zip(primes, restrictions)})
    print('NECESSARY support test: minimum candidate pairs:', minimum,
          'minimal passing supports:', [s for s in passes if len(s) == minimum])
    print('PASS: all32 supports checked by row spans and independent dual witnesses')
    print('PASS q127 still fails: P2+P4-9P1 is locally divisible and pairs to1')
    print('NONCLAIM: passing the known-MW support test does not eliminate unknown fine classes')

    # A targeted bounded search, not enumeration of a Galois closure.
    found = None
    eligible = 0
    for q in range(5, 20001):
        if q in (7, 11, 117223) or not m['prime'](q) or pow(-7 % q, (q - 1) // 2, q) != 1:
            continue
        n = m['count'](q)
        if n % P or n % (P * P) == 0:
            continue
        eligible += 1
        root = next(x for x in range(q) if (x * x + 7) % q == 0)
        c = m['row_at'](q, root)
        if c is None:
            continue
        row = [dot(c['row'], y) for y in fine]
        if any(row) and all(row[j] * target[0] % P == row[0] * target[j] % P
                            for j in range(3)):
            found = c, row
            break
    need(found is not None, 'bounded prime search found no hit; not a nonexistence result')
    c, row = found
    need((c['q'], c['root'], c['order'], c['generator'], c['row'], row) ==
         (3389, 154, 3498, [668, 1888], [1, 10, 5, 4, 8], [10, 3, 6]),
         'targeted auxiliary-prime certificate changed')
    need(row == [5 * x % P for x in target], 'auxiliary row is not aligned')
    conjugate = m['row_at'](3389, 3389 - 154)
    need(conjugate['row'][:4] == c['row'][:4], 'targeted conjugate row differs')
    print('ACTUAL targeted auxiliary-prime hit:', c, 'fine row:', row,
          'eligible primes tested:', eligible)
    print('NONCLAIM: q3389 removes the known-MW detector only; full fine coverage is unknown')


def prescribed_functional_controls():
    # Synthetic finite-representation control for the auxiliary-prime lemma:
    # A=diag(1,2), quotient V/(A-1)V is the first coordinate. A full
    # translation subgroup lets each independent cocycle realize any value.
    targets = set()
    for values in itertools.product(range(P), repeat=3):
        translations = [(values[i], i + 1) for i in range(3)]
        projected = tuple(v[0] for v in translations)
        need(projected == values, 'prescribed functional not realized')
        # Changing a cocycle representative adds (A-1)*b=(0,b2),
        # so its unramified quotient class does not change.
        for offset in range(P):
            changed = [(v[0], (v[1] + offset) % P) for v in translations]
            need(tuple(v[0] for v in changed) == values,
                 'coboundary changed the quotient functional')
        targets.add(projected)
    need(len(targets) == P ** 3, 'not every functional is realized')
    # A proper diagonal translation image cannot realize values (1,0).
    diagonal_values = {(x, x) for x in range(P)}
    need((1, 0) not in diagonal_values,
         'independence/isotypic hypothesis was incorrectly omitted')
    print('PASS: prescribed finite-module functionals; proper-image countercontrol')


def main():
    columns, loc = actual_local_columns()
    need(loc == [[4, 0, 8, 3, 9], [4, 0, 8, 3, 2]], 'local Kummer inputs changed')
    need(rank(loc) == 2, 'known MW localization rank changed')
    fine = [[0, 1, 0, 0, 0], [9, 0, 1, 0, 0], [2, 0, 0, 1, 0]]
    need(rank(fine) == 3 and all(mv(loc, y) == [0, 0] for y in fine),
         'proposed fine MW frame is not a basis')
    count = sum(mv(loc, x) == [0, 0] for x in itertools.product(range(P), repeat=5))
    need(count == P ** 3, 'finite localization kernel count changed')
    print('ACTUAL local Kummer matrix mod11:', loc)
    print('PASS: known MW fine kernel has dimension3; basis P2,P3-2P1,P4-9P1')

    if len(sys.argv) == 2:
        text = Path(sys.argv[1]).read_text(encoding='utf8')
        compare_pari(columns, text)
        # This mutation exercises the very same oracle comparator.
        changed = text.replace('LOCAL P2 33 33', 'LOCAL P2 34 33')
        need(changed != text, 'mutation target missing')
        try:
            compare_pari(columns, changed)
        except AssertionError:
            pass
        else:
            raise AssertionError('mutated PARI column accepted')
        print('PASS: independent PARI minimal-model columns; mutation rejected')
    else:
        need(len(sys.argv) == 1, 'usage: script [PARI-output]')

    value, ratio = actual_height_p2_r()
    print('ACTUAL direct-coordinate q(P2+R) mod11:', value, 'squared ratio mod121:', ratio)
    # The full old row has separate direct-coordinate and prior global-ideal
    # CI checks. Only its decisive P2 entry is recomputed here.
    a = [1, value, 7, 8]
    b = [[0] * 5 for _ in range(5)]
    for i, x in enumerate(a):
        b[i][4] = b[4][i] = x
    detected = [[dot(y, [b[i][j] for i in range(5)])
                 for j in range(5)] for y in fine]
    need(detected == [[0, 0, 0, 0, 2], [0, 0, 0, 0, 5], [0, 0, 0, 0, 10]],
         'conditional fine-class detector changed')
    need(rank(detected) == 1, 'detected rank changed')
    print('CONDITIONAL height detector in rho-normalization:', detected)

    # Synthetic exact-sequence controls: im(loc^t) is annihilated by fine.
    # Conversely non-fine P1 may see a local boundary whose global image is0.
    boundaries = {tuple((u * loc[0][j] + v * loc[1][j]) % P for j in range(5))
                  for u, v in itertools.product(range(P), repeat=2)}
    need(len(boundaries) == P ** 2, 'local-boundary rank changed')
    need(all(dot(y, z) == 0 for y in fine for z in boundaries),
         'fine annihilator identity failed')
    e1 = [1, 0, 0, 0, 0]
    need(mv(loc, e1) != [0, 0] and dot(e1, loc[0]) == 4,
         'non-fine false-positive control failed')
    need(tuple([1, 2, 7, 8, 0]) not in boundaries,
         'R detector incorrectly factors through local boundary')
    need([P * x % P for x in a] == [0] * 4,
         'nonunit scaling control failed')
    # Unknown extra fine-minus classes can obstruct a positive MW class
    # while vanishing on every known positive fine test. Do not infer
    # positive-lift existence from the detector's positive zero columns.
    hidden_global_obstruction = [0, 0, 0, 1]
    known_fine_tests = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0]]
    need(all(dot(y, hidden_global_obstruction) == 0 for y in known_fine_tests)
         and hidden_global_obstruction != [0] * 4,
         'incomplete fine-test countermodel failed')
    character_unit_control()
    auxiliary_support_controls(fine)
    prescribed_functional_controls()
    print('PASS: local-boundary, non-fine, nonunit and hidden-fine-class controls')
    print('NONCLAIM: no cochain presentation, complete fine Selmer group, h2 or complex BSD computed')


if __name__ == '__main__':
    main()
