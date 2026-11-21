#!/usr/bin/env python3
"""Session49: exact first/second augmentation Bockstein on G2=U2:C11.

An ACTUAL global first correction is not constructed; this finite canonical
model checks source-matched cochain signs, a genuine nonzero H^2 class,
and information loss under projection/local-cone forgetting.
"""
from itertools import product

P = 11


def choose2plus(e):
    return (e * (e + 1) // 2) % P


def mult2(s, t):
    e, u, v = s
    f, x, y = t
    return ((e + f) % P, (u + x) % P, (v + y - e * x) % P)


def inv2(s):
    e, u, v = s
    return ((-e) % P, (-u) % P, (-v - e * u) % P)


def mult3(s, t):
    e, u, v, z = s
    f, x, y, w = t
    return ((e + f) % P, (u + x) % P, (v + y - e * x) % P,
            (z + w - e * y + choose2plus(e) * x) % P)


def inv3(s):
    e, u, v, z = s
    return ((-e) % P, (-u) % P, (-v - e * u) % P,
            (-z - e * v - (e * (e - 1) // 2) * u) % P)


def comm3(a, b):
    return mult3(mult3(mult3(a, b), inv3(a)), inv3(b))


def first_lift_cocycle(g, h):
    # d c1(s,t) = chi(s) * c0(t).
    e, u, v = g
    f, x, y = h
    gh = mult2(g, h)
    return (v + y - gh[2]) % P == e * x % P


def second_bockstein(g, h):
    # d c2(s,t) = chi(s)c1(t) - binom(chi(s)+1,2)c0(t).
    e, u, v = g
    f, x, y = h
    return (e * y - choose2plus(e) * x) % P


def boundary2(g, h):
    # The central extension 0->T²V->G3->G2->1 has this cocycle.
    e, u, v = g
    f, x, y = h
    return (-e * y + choose2plus(e) * x) % P


def check_cocycle(g, h, k):
    return ((second_bockstein(h, k)
             - second_bockstein(mult2(g, h), k)
             + second_bockstein(g, mult2(h, k))
             - second_bockstein(g, h)) % P) == 0


def commutator_second_order_controls():
    # The relator [h,[h,w]]=1 in G2 cannot be lifted to G3, independent
    # of ALL four free first/second coordinates for the two generators.
    def comm(a, b, f, inv):
        return f(f(f(a, b), inv(a)), inv(b))

    h0 = (2, 0, 0)
    w0 = (0, 1, 0)
    assert comm(h0, comm(h0, w0, mult2, inv2), mult2, inv2) == (0, 0, 0)
    for h1, h2, w1, w2 in product(range(P), repeat=4):
        h = (2, 0, h1, h2)
        w = (0, 1, w1, w2)
        c = comm3(h, w)
        d = comm3(h, c)
        assert d == (0, 0, 0, 4)

    assert comm3((0, 0, 0, 0),
                 comm3((0, 0, 0, 0), (0, 1, 0, 0))) == (0, 0, 0, 0)
    assert comm3((2, 0, 0, 0),
                 comm3((2, 0, 0, 0), (0, 0, 0, 0))) == (0, 0, 0, 0)


def local_cone_forgetting_control():
    # An exactly-solvable finite linear model of the distinction:
    # global Frobenius x+y=9, two ordinary local equations x=0,y=0.
    # Any pair is solvable, all three simultaneously are not.
    allvars = list(product(range(P), repeat=2))
    equations = (
        lambda x, y: (x + y) % P == 9,
        lambda x, y: x == 0,
        lambda x, y: y == 0,
    )
    assert all(any(a(x, y) and b(x, y) for x, y in allvars)
               for a, b in ((equations[0], equations[1]),
                            (equations[0], equations[2]),
                            (equations[1], equations[2])))
    assert not any(all(f(x, y) for f in equations) for x, y in allvars)
    # The exact left-kernel/syndrome of A=[[1,1],[1,0],[0,1]]:
    # row0 - row1 - row2 = 0, yet rhs0-rhs1-rhs2=9.
    assert (9 - 0 - 0) % P == 9
    assert (9 - 0 - 9) % P == 0  # deliberate consistent mutation
    # Projection of V=F11^2 onto its 2nd coordinate kills a nonzero
    # first-coordinate Bockstein, so projection can hide obstructions.
    witnesses = [((e, 0, 0), (0, 1, 0)) for e in range(P)]
    assert any(second_bockstein(g, h) != 0 for g, h in witnesses)
    assert all((0 * second_bockstein(g, h)) % P == 0
               for g, h in witnesses)


def main():
    e0 = (0, 0, 0)
    identity3 = (0, 0, 0, 0)
    for e in range(P):
        for f in range(P):
            assert choose2plus(e + f) == (
                choose2plus(e) + choose2plus(f) + e * f) % P
    for g, h in product([(e, u, v) for e in range(P)
                         for u in (0, 1, 3, 10) for v in (0, 2, 5)],
                        repeat=2):
        assert first_lift_cocycle(g, h)
        assert second_bockstein(g, h) == -boundary2(g, h) % P
    for e in range(P):
        for f in range(P):
            for u, v, x, y in product((0, 1, 7), repeat=4):
                g = (e, u, v)
                h = (f, x, y)
                assert check_cocycle(g, h, (3, 8, 2))
                assert check_cocycle(g, h, (9, 1, 10))
    for g in [(0, 0, 0, 0), (2, 0, 1, 3), (7, 4, 9, 10),
              (10, 5, 0, 6)]:
        assert mult3(g, inv3(g)) == identity3
    assert mult2((2, 0, 0), (0, 1, 0)) != mult2((0, 1, 0), (2, 0, 0))
    commutator_second_order_controls()
    local_cone_forgetting_control()

    print("PASS: exact inverse-character d c1 and d c2 coefficients")
    print("PASS: canonical second H2 cocycle = negative central-extension cocycle")
    print("PASS: exhaustive 11^4 generator lifts force double bracket 4*T^2")
    print("PASS: group extension is non-split; second H2 class is nonzero")
    print("PASS: projected vanishing and individually soluble local cones can hide defect")
    print("NONCLAIM: no actual arithmetic second Bockstein, local Greenberg or BSD implication")


if __name__ == "__main__":
    main()
