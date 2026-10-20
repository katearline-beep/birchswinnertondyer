#!/usr/bin/env python3
"""Exact arithmetic prerequisites and falsifiers; does NOT compute focal delta3389.

Published theorem applicability and finite Selmer-complex duality remain
source obligations. Decimal diagnostics are deliberately absent from proofs.
"""
from fractions import Fraction as F
from pathlib import Path
import sys

P = 11


def need(ok, message):
    if not ok:
        raise AssertionError(message)


def card(a, b, q):
    squares = [0] * q
    for y in range(q):
        squares[y*y % q] += 1
    return 1 + sum(squares[(x*x*x+a*x+b) % q] for x in range(q))


def valuation(n):
    need(n != 0, 'zero valuation is not finite')
    v = 0
    while n % P == 0:
        n //= P
        v += 1
    return v


def vp(x):
    return valuation(x.numerator) - valuation(x.denominator)


def prerequisites():
    a, b = -1267, 17230
    at, bt = a*49, b*(-343)
    need((at, bt) == (-62083, -5909890), 'wrong -7 twist')
    x, y = F(3355, 9), F(128780, 27)
    need(y*y == x*x*x+at*x+bt, 'twist point is off curve')
    # Both short models use u=2 to their displayed minimal models.
    xm, ym = (x+1)/4, (y-x-1)/8
    need((xm, ym) == (F(841,9), F(14836,27)), 'wrong minimal change')
    need(ym*ym+xm*ym == xm**3-xm*xm-3880*xm-91372,
         'minimal twist equation fails')
    need(2*49*117223 == 11487854, 'wrong conductor factorization')
    need(all(q % P not in (1, P-1) for q in (2,117223)),
         'Zhang multiplicative congruence obligation not vacuous')
    need(2 % 2 == 0 and 1 % P != 0, 'even multiplicative count / I1 ramification')
    n = card(at, bt, P)
    need(n == 18 and (P+1-n) % P != 0, 'ordinary/nonanomalous input changed')
    need(2 % P != 0, 'Tamagawa product is not a unit')
    q = 3389
    need((154*154+7) % q == 0 and (q-1) % P == 0, 'q not split/eligible')
    nt = card(at, bt, q)
    need(nt == card(a,b,q) == 3498 and nt % P == 0 and nt % (P*P) != 0,
         'q is not in P_1,0')
    need(q+1-nt == -108, 'wrong trace')
    # Complete discrete-log table: primitive root is checked, not assumed.
    h = next(g for g in range(2,q) if len({pow(g,j,q) for j in range(q-1)}) == q-1)
    logs = {pow(h,j,q): j % P for j in range(q-1)}
    need(len(logs) == q-1 and logs[1] == 0, 'incomplete log table')
    need(all(logs[pow(h,j,q)] == j % P for j in range(q-1)), 'log mismatch')
    need(all(logs[(-a) % q] == logs[a] for a in logs), 'unexpected odd log')
    print('PASS exact twist point/minimal change; #Et(F11)=18; q3389 order3498, trace-108')
    print('PASS complete mod11 discrete logs at q3389; primitive generator', h)
    print('SOURCE INPUTS, NOT CODE PROOFS: minimal conductor/Tamagawas, residual GL2, Zhang and Sakamoto theorems')


def valuation_falsifiers():
    need(vp(F(4)) == 0, 'unit baseline failed')
    for digits in (6,12,30,60):
        b = 10**digits+1
        need(b % P != 0, 'bad denominator')
        k = (4*b)//121
        if k % P == 0:
            k += 1
        x = F(121*k,b)
        need(vp(x) == 2 and abs(x-4) <= F(121,b),
             'near-four nonunit counterexample failed')
    # Q = Sha_order / index^2 only under a FULL suitable leading-term identity.
    # Known point's 11-primitivity removes index valuation, not real-rational ambiguity.
    need(F(121,121) == 1 and valuation(121) == 2, 'nonprimitive index control failed')
    print('PASS arbitrarily close-to-four rational values with v11=2 versus v11(4)=0')
    print('PASS nonunit point-index square and finite Sha=(Z/11)^2 controls')


def conditional_first_kernel():
    # Conditional on FULL negative residual Selmer line R and finite first-height
    # duality/comparison, the only possible tests of a positive vector use R.
    row = [1,2,7,8]
    frame = [[9,1,0,0],[4,0,1,0],[3,0,0,1]]
    need(all(sum(a*b for a,b in zip(row,x)) % P == 0 for x in frame), 'wrong kernel')
    need([x[1:] for x in frame] == [[1,0,0],[0,1,0],[0,0,1]], 'dependent frame')
    # Hidden negative Sha direction adds a new independent first-height test.
    hidden = [0,1,0,0]
    need(sum(a*b for a,b in zip(hidden,frame[0])) % P != 0,
         'hidden-Sha false upper bound was not detected')
    # This checks linear algebra, not existence of the Selmer duality identification.
    print('CONDITIONAL kernel frame: P2-2P1, P3-7P1, P4-8P1; no positive upper bound used')
    print('PASS hidden negative residual class defeats an unwarranted three-survivor inference')


def compare_pari(text):
    need('***' not in text, 'PARI interpreter error')
    controls = [line.split() for line in text.splitlines() if line.startswith('TWISTCONTROL ')]
    expected = [(1,1,1,-2),(2,1,1,-2),(3,1,1,-2),(4,-2,-2,1),(5,1,1,-2),(6,-2,-2,-1)]
    need(controls == [['TWISTCONTROL', *map(str,row)] for row in expected], 'twist-symbol control mismatch')
    need('TWISTINPUT 11487854 2 18 3498' in text.splitlines(), 'missing twist local inputs')
    need('PASS PARI Session34 exact small-curve symbol control' in text.splitlines(), 'missing completion')


def main():
    prerequisites()
    valuation_falsifiers()
    conditional_first_kernel()
    if len(sys.argv) == 3 and sys.argv[1] == '--pari':
        text = Path(sys.argv[2]).read_text()
        compare_pari(text)
        for bad in (text+'\n*** synthetic error', text.replace('TWISTCONTROL 1 1 1 -2','TWISTCONTROL 1 2 1 -2')):
            try:
                compare_pari(bad)
            except AssertionError:
                pass
            else:
                raise AssertionError('mutated PARI oracle accepted')
        print('PASS independent PARI exact twist inputs and six small-curve symbols; mutations rejected')
    else:
        need(len(sys.argv) == 1, 'usage: script [--pari output-file]')
    print('NONCLAIM: delta3389 is UNCOMPUTED; no twist Sha11 bound, actual h2 or original complex BSD')


if __name__ == '__main__':
    main()
