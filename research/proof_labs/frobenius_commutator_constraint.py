#!/usr/bin/env python3
"""Necessary arithmetic constraint on a first correction, NOT a constructed lift.

E=[1,-1,0,-79,289], K=Q(sqrt(-7)), p=11; x=P2-2P1.
See SESSION38_FROBENIUS_COMMUTATOR_CONSTRAINT.md for the proof and boundaries.
Standard-library arithmetic; optional independently generated PARI transcript.
"""
from itertools import product
from pathlib import Path
import sys

P = 11
I = (1, 0, 0, 1)
Z = (0, 0, 0, 0)


def mm(a, b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % P
                 for i in range(2) for j in range(2))


def ma(a, b):
    return tuple((x+y) % P for x, y in zip(a, b))


def mv(a, v):
    return tuple(sum(a[2*i+j]*v[j] for j in range(2)) % P for i in range(2))


def power_sum(a, n):
    r, s = I, Z
    for _ in range(n):
        s, r = ma(s, r), mm(r, a)
    return r, s


def count_short(q):
    squares = [0]*q
    for y in range(q):
        squares[y*y % q] += 1
    return 1 + sum(squares[(x**3-1267*x+17230) % q] for x in range(q))


def count_minimal(q):
    # Different model and exhaustive coordinate pairs, no character-sum code.
    return 1 + sum((y*y+x*y-x**3+x*x+79*x-289) % q == 0
                   for x in range(q) for y in range(q))


def add_short(u, v, q):
    if u is None:
        return v
    if v is None:
        return u
    x, y = u
    z, w = v
    if x == z and (y+w) % q == 0:
        return None
    s = ((3*x*x-1267)*pow(2*y, -1, q) if u == v
         else (w-y)*pow(z-x, -1, q)) % q
    xx = (s*s-x-z) % q
    return xx, (s*(x-xx)-y) % q


def add_minimal(u, v, q):
    if u is None:
        return v
    if v is None:
        return u
    x, y = u
    z, w = v
    if x == z and (y+w+x) % q == 0:
        return None
    if u == v:
        s = (3*x*x-2*x-79-y)*pow(2*y+x, -1, q) % q
    else:
        s = (w-y)*pow(z-x, -1, q) % q
    intercept = (y-s*x) % q
    xx = (s*s+s+1-x-z) % q
    return xx, (-(s+1)*xx-intercept) % q


def mul_binary(n, u, q):
    r = None
    while n:
        if n & 1:
            r = add_short(r, u, q)
        u = add_short(u, u, q)
        n //= 2
    return r


def mul_repeated(n, u, q):
    r = None
    for _ in range(n):
        r = add_minimal(r, u, q)
    return r


def to_minimal(u, q):
    if u is None:
        return None
    x, y = u
    return (x+1)*pow(4, -1, q) % q, (y-x-1)*pow(8, -1, q) % q


def artin(a, b):
    # Recompute the root; do not import the old Artin implementation.
    roots = [r for r in range(121) if r % 11 == 5 and (r*r-r+2) % 121 == 0]
    assert roots == [16]
    r = roots[0]
    ratio = (a+b*r)*pow((a+b*(1-r)) % 121, -1, 121) % 121
    u = pow(ratio, 10, 121)
    logs = [j for j in range(11) if pow(12, j, 121) == u]
    # Independent Fermat-quotient formula at this precision.
    assert len(logs) == 1 and logs[0] == ((u-1)//11) % 11
    return logs[0]


def arithmetic():
    rows = []
    for q, a, b, root, expected_order, expected_ell in (
            (23, -5, 2, 4, 12, 2), (127, -11, 6, 45, 10, 4)):
        assert a*a+a*b+2*b*b == q
        assert (root*root+7) % q == 0
        assert (a+b*(1+root)*pow(2, -1, q)) % q == 0
        n = count_short(q)
        assert n == count_minimal(q)
        trace = q+1-n
        matrix = (0, -q % P, 1, trace % P)
        order = next(j for j in range(1, 133) if power_sum(matrix, j)[0] == I)
        assert order == expected_order
        ell = artin(a, b)
        assert ell == expected_ell and artin(a+b, -b) == -ell % P
        assert artin(-a, -b) == ell
        rows.append(f'FROBENIUS {q} {a} {b} {root} {n} {trace} {order} {ell} {order*ell % P}')
        if q == 23:
            assert power_sum(matrix, order)[1] == Z
        else:
            # Eigenvalues 1,6 are distinct; norm is nonzero exactly on
            # V/(A-1)V. Verify the kernel identity on every vector.
            am1 = ma(matrix, tuple(-z % P for z in I))
            image = {mv(am1, v) for v in product(range(P), repeat=2)}
            norm = power_sum(matrix, order)[1]
            kernel = {v for v in product(range(P), repeat=2) if mv(norm, v) == (0, 0)}
            assert image == kernel and len(kernel) == P

    q = 127
    p1, p2 = (15, 40), (19, 4)
    twice = mul_binary(2, p1, q)
    x = add_short(p2, (twice[0], -twice[1] % q), q)
    t = mul_binary(13, p1, q)
    projected = mul_binary(13, x, q)
    assert t is not None and mul_binary(11, t, q) is None
    assert projected == mul_binary(2, t, q) and projected is not None
    # Separate minimal-model addition and repeated addition (no binary ladder).
    m1, m2 = to_minimal(p1, q), to_minimal(p2, q)
    mtwice = mul_repeated(2, m1, q)
    mx = add_minimal(m2, (mtwice[0], (-mtwice[1]-mtwice[0]) % q), q)
    assert mx == to_minimal(x, q)
    assert mul_repeated(13, mx, q) == to_minimal(projected, q)
    assert mul_repeated(13, m1, q) == to_minimal(t, q)
    rows.append(f'KUMMER127 {t[0]} {t[1]} {projected[0]} {projected[1]} 2')
    return rows


def cover_mul(g, h):
    # Restriction to ker(rho). Coordinates (ell,c0,c1) are scalars;
    # each component of the V-valued identity is checked separately.
    k, x, w = g
    l, y, z = h
    return (k+l) % P, (x+y) % P, (w+z-k*y) % P


def cover_inverse(g):
    k, x, w = g
    return -k % P, -x % P, (-w-k*x) % P


def mat(g):
    k, x, w = g
    return ((1, -k % P, w), (0, 1, x), (0, 0, 1))


def matmul(a, b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) % P
                       for j in range(3)) for i in range(3))


def commutator(g, h):
    return cover_mul(cover_mul(cover_mul(g, h), cover_inverse(g)), cover_inverse(h))


def controls():
    # Exhaust every ell,c0 pair; unknown c1 cancels because it is central.
    for k, l, x, y in product(range(P), repeat=4):
        g, h = (k, x, 3), (l, y, 7)
        expected = (0, 0, (l*x-k*y) % P)
        got = commutator(g, h)
        assert got == expected
        matrix = matmul(matmul(matmul(mat(g), mat(h)), mat(cover_inverse(g))), mat(cover_inverse(h)))
        assert matrix == mat(expected)
    # Actual arithmetic inputs: ell(h)=2,c0(h)=0; ell(g)=7,c0(g)!=0.
    # Coordinates here are symbolic one-dimensional components, NOT an
    # identification of c0(g) with the finite-reduction torsion generator.
    for wh, wg, x in product(range(P), repeat=3):
        got = commutator((2, 0, wh), (7, x, wg))
        assert got == (0, 0, 9*x % P)
        assert (got[2] != 0) == (x != 0)
    assert commutator((0, 0, 3), (7, 1, 7))[2] == 0  # zero character
    assert commutator((2, 0, 3), (7, 0, 7))[2] == 0  # zero Kummer input
    assert commutator((-2 % P, 0, 3), (-7 % P, 1, 7))[2] == 2  # inverse convention
    assert commutator((7, 1, 7), (2, 0, 3))[2] == 2  # reverse commutator
    # A commuting quotient predicts zero and must fail the actual constraint.
    assert 0 != commutator((2, 0, 0), (7, 1, 0))[2]


def compare(lines, expected):
    if lines != expected:
        raise ValueError('Incomplete, changed, or error-bearing PARI transcript')


def main():
    expected = arithmetic()
    for row in expected:
        print(row)
    controls()
    # Test the same comparator used for external transcripts.
    mutations = [expected[:-1], expected+[expected[0]], ['*** GP error']+expected,
                 [expected[0].rsplit(' ', 1)[0]+' 3']+expected[1:]]
    for bad in mutations:
        try:
            compare(bad, expected)
        except ValueError:
            pass
        else:
            raise AssertionError('Bad oracle transcript accepted')
    if len(sys.argv) == 2:
        compare(Path(sys.argv[1]).read_text(encoding='utf8').splitlines(), expected)
        print('PASS independently generated PARI arithmetic transcript')
    else:
        assert len(sys.argv) == 1
    print('PASS two-model arithmetic, Artin coordinates, Frobenius orders and Kummer nonzero')
    print('PASS commutator identity by group words and independent matrices; mutation controls')
    print('NECESSARY RELATION: c1([h,g]) = 9*c0(g) != 0 for h=Frob23^12, g=Frob127^10')
    print('NONCLAIM: no evaluated full global cochain, supported realization, Greenberg comparison, h2 or BSD')


if __name__ == '__main__':
    main()
