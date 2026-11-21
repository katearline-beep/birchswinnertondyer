#!/usr/bin/env python3
"""Exact arithmetic at q743: pure Kummer Frobenius, local H1 and bracket gates.

AI-assisted; not a global correction, second Bockstein or BSD certificate.
Optional independently generated PARI oracle from minimal elliptic model.
"""
from itertools import product
from pathlib import Path
import sys

P = 11
Z = (0, 0, 0)
I = (1, 0, 0, 1)


def count_short(q):
    # Euler/Legendre sum: no point-law assumptions.
    out = q+1
    for x in range(q):
        z = (x*x*x-1267*x+17230) % q
        if z:
            out += 1 if pow(z, (q-1)//2, q) == 1 else -1
    return out


def count_minimal(q):
    # Completely separate count on y²+xy=x³-x²-79x+289.
    return 1+sum((y*y+x*y-x*x*x+x*x+79*x-289) % q == 0
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
    if u == v:
        t = (3*x*x-1267)*pow(2*y, -1, q) % q
    else:
        t = (w-y)*pow(z-x, -1, q) % q
    X = (t*t-x-z) % q
    return X, (t*(x-X)-y) % q


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
        t = (3*x*x-2*x-79-y)*pow(2*y+x, -1, q) % q
    else:
        t = (w-y)*pow(z-x, -1, q) % q
    b = (y-t*x) % q
    X = (t*t+t+1-x-z) % q
    return X, (-(t+1)*X-b) % q


def times(n, u, q, adder):
    out = None
    while n:
        if n & 1:
            out = adder(out, u, q)
        u = adder(u, u, q)
        n //= 2
    return out


def repeated(n, u, q):
    out = None
    for _ in range(n):
        out = add_minimal(out, u, q)
    return out


def to_minimal(u, q):
    if u is None:
        return None
    x, y = u
    return ((x+1)*pow(4, -1, q) % q,
            (y-x-1)*pow(8, -1, q) % q)


def artin(a, b):
    # Same C0033 orientation, independently rederived finite ratio.
    roots = [x for x in range(121) if x % 11 == 5 and
             (x*x-x+2) % 121 == 0]
    assert roots == [16]
    omega = roots[0]
    num = (a+b*omega) % 121
    den = (a+b*(1-omega)) % 121
    ratio = num*pow(den, -1, 121) % 121
    unit = pow(ratio, 10, 121)
    matches = [i for i in range(P) if pow(12, i, 121) == unit]
    assert len(matches) == 1
    return matches[0], ratio, unit


def mm(a, b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) % P
                 for i in range(2) for j in range(2))


def mv(a, v):
    return tuple(sum(a[2*i+j]*v[j] for j in range(2)) % P for i in range(2))


def matpower(a, n):
    out = I
    for _ in range(n):
        out = mm(out, a)
    return out


def rank_mod11(rows, n):
    a = [list(row) for row in rows]
    rank = 0
    for j in range(n):
        piv = next((i for i in range(rank, len(a)) if a[i][j] % P), None)
        if piv is None:
            continue
        a[piv], a[rank] = a[rank], a[piv]
        inv = pow(a[rank][j], -1, P)
        a[rank] = [x*inv % P for x in a[rank]]
        for i in range(len(a)):
            if i != rank:
                d = a[i][j]
                a[i] = [(x-d*y) % P for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def frob_matrix(q, n):
    tr = q+1-n
    return (0, -q % P, 1, tr % P)


def coefficient_action(rho, ell, r, v):
    # rho(Frob)*(1+T)^(-ell), where v has r coefficient vectors.
    coeff = (1, -ell % P, ell*(ell+1)//2 % P)
    out = [0]*(2*r)
    for degree in range(r):
        u = (0, 0)
        for j in range(degree+1):
            u = tuple((u[k] + coeff[j]*v[2*(degree-j)+k]) % P
                      for k in range(2))
        m = mv(rho, u)
        out[2*degree:2*degree+2] = m
    return tuple(out)


def local_dim(rho, ell, r):
    n = 2*r
    basis = [tuple(i == j for j in range(n)) for i in range(n)]
    col = []
    for v in basis:
        fv = coefficient_action(rho, ell, r, v)
        col.append(tuple((a-b) % P for a, b in zip(fv, v)))
    return n-rank_mod11(col, n)


def coboundary_group_prod(s, t):
    # On ker rho, scalar coordinate of V[T]/T³.
    e, (a, b, c) = s
    f, (u, v, w) = t
    return ((e+f) % P, ((a+u) % P,
                       (b+v-e*u) % P,
                       (c+w-e*v+(e*(e+1)//2)*u) % P))


def coboundary_inv(s):
    e, (a, b, c) = s
    x = -e
    au = (a, b-x*a, c-x*b+(x*(x+1)//2)*a)
    return (-e % P, tuple(-z % P for z in au))


def comm(s, t):
    return coboundary_group_prod(coboundary_group_prod(
        coboundary_group_prod(s,t),coboundary_inv(s)),coboundary_inv(t))


def arithmetic():
    q = 743
    a, b, root = 27, -14, 109
    assert a*a+a*b+2*b*b == q
    assert (root*root+7) % q == 0
    assert (a+b*(1+root)*pow(2, -1, q)) % q == 0

    ell, ratio, unit = artin(a, b)
    assert (ratio, unit, ell) == (112, 1, 0)
    ell127, _, _ = artin(-11, 6)
    assert ell127 == 4

    n = count_short(q)
    assert n == count_minimal(q) == 770
    assert n//11 == 70 and n % 121 != 0
    A743 = frob_matrix(q, n)
    A127 = frob_matrix(127, 143)
    assert A743 == A127 == (0, 5, 1, 7)
    assert matpower(A743, 10) == I
    assert all(matpower(A743, k) != I for k in range(1, 10))

    p1, p2 = (15, 40), (19, 4)
    negp1 = (p1[0], -p1[1] % q)
    x = add_short(add_short(p2, negp1, q), negp1, q)
    t = times(70, p1, q, add_short)
    w = times(70, x, q, add_short)
    assert t == (114, 527) and w == (185, 342)
    assert times(9, t, q, add_short) == w
    assert times(11, t, q, add_short) is None
    assert times(70, p2, q, add_short) is None

    # Independent affine group law, on the ORIGINAL minimal curve.
    m1, m2 = to_minimal(p1,q), to_minimal(p2,q)
    twice = add_minimal(m1,m1,q)
    mx = add_minimal(m2,(twice[0],(-twice[1]-twice[0])%q),q)
    assert mx == to_minimal(x,q)
    assert repeated(70,m1,q) == to_minimal(t,q)
    assert repeated(70,mx,q) == to_minimal(w,q)
    assert repeated(70,m2,q) is None

    rows = [
        f"FROBENIUS743 743 {a} {b} {root} {n} {q+1-n} 10 {ell} 0",
        f"FROBENIUS127 127 -11 6 45 143 -15 10 {ell127} 7",
        f"KUMMER743 {t[0]} {t[1]} {w[0]} {w[1]} 9",
    ]
    return rows, A743


def checks(A743):
    A23 = frob_matrix(23, 30)
    assert matpower(A23, 12) == I
    for r in (1,2,3):
        assert local_dim(A23,2,r) == 0
        assert local_dim(A743,0,r) == r
        assert local_dim(A743,4,r) == 1
    assert local_dim(A743,0,3) != local_dim(A743,4,3)

    # h=Frob23^12 and w=Frob743^10 are in ker rho; ell=2,0 and
    # c0(h)=0, c0(w) !=0 (its arbitrary scalar normalizes to one).
    # In EVERY hypothetical global T³ affine cocycle:
    for h1,h2,w1,w2 in product(range(P), repeat=4):
        h = (2, (0,h1,h2))
        w = (0, (1,w1,w2))
        c = comm(h,w)
        d = comm(h,c)
        assert c[0] == d[0] == 0
        assert c[1][0] == 0 and c[1][1] == 9
        assert d == (0, (0,0,4))
    # Wrong character (ell(h)=0) kills all brackets.
    assert comm((0,(0,0,0)),(0,(1,0,0))) == (0,Z)
    # Wrong residual input (c0(w)=0) kills the DOUBLE bracket.
    assert comm((2,(0,0,0)),comm((2,(0,0,0)),(0,(0,0,0)))) == (0,Z)


def compare(expected, given):
    if expected != given:
        raise ValueError("Changed/incomplete independent PARI transcript")


def main():
    expected,A743 = arithmetic()
    checks(A743)
    mutations = (expected[:-1], expected+[expected[0]],
                 ["*** PARI interpreter error"]+expected,
                 [expected[0].replace(" 10 0 0"," 10 1 10")]+expected[1:])
    for bad in mutations:
        try:
            compare(expected,bad)
        except ValueError:
            pass
        else:
            raise AssertionError("bad PARI transcript accepted")
    if len(sys.argv) == 2:
        compare(expected,Path(sys.argv[1]).read_text(encoding="utf8").splitlines())
        print("PASS independently generated PARI minimal-model/ray-class oracle")
    else:
        assert len(sys.argv) == 1
    for row in expected:
        print(row)
    print("PASS: two independently computed q743 point/group models and exact C0033 Artin=0")
    print("PASS: q127 and q743 share charpoly, but H1_unr dimensions differ (1 vs r)")
    print("PASS: all 14641 hypothetical correction coordinates force 23/743 brackets 9u,4u")
    print("NONCLAIM: no globally evaluated c1/c2, ordinary Greenberg, h² or BSD implication")


if __name__ == "__main__":
    main()
