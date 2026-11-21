#!/usr/bin/env python3
"""Session44: exact relative 121-kernel tower algebra, NOT Galois existence.

The conditional existence of an arithmetic first field uses signed global
duality (C-0047), NOT this code.  See SESSION44_SIGNED_FIRST_LIFT_121_TOWER.md.
"""
from itertools import product

P = 11


def action(e, v, r):
    """(1+T)^(-e) on V[T]/T^r, V=F11^2, for r=1,2,3."""
    assert r in (1, 2, 3) and len(v) == 2*r
    coeff = (1, (-e) % P, (e*(e+1)//2) % P)
    result = [0]*(2*r)
    for j in range(r):
        for k in range(j+1):
            for c in range(2):
                result[2*j+c] += coeff[k]*v[2*(j-k)+c]
    return tuple(v % P for v in result)


def diff(e, v, r):
    return tuple((a-b) % P for a, b in zip(action(e, v, r), v))


def rank_mod_p(rows, ncols):
    a = [list(row) for row in rows]
    rank = 0
    for j in range(ncols):
        pivot = next((i for i in range(rank, len(a)) if a[i][j] % P), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = pow(a[rank][j], -1, P)
        a[rank] = [int(x*scale % P) for x in a[rank]]
        for i in range(len(a)):
            if i == rank:
                continue
            k = a[i][j]
            a[i] = [int((x-k*y) % P) for x, y in zip(a[i], a[rank])]
        rank += 1
    return rank


def lower_central_dimensions(r):
    n = 2*r
    basis = [tuple(1 if j == k else 0 for j in range(n))
             for k in range(n)]
    d1 = [diff(2, v, r) for v in basis]
    d2 = [diff(2, x, r) for x in d1]
    d3 = [diff(2, x, r) for x in d2]
    ranks = [n, rank_mod_p(d1, n), rank_mod_p(d2, n),
             rank_mod_p(d3, n)]
    return [ranks[i]-ranks[i+1] for i in range(3) if ranks[i] > ranks[i+1]]


def scalar_action(e, p, r):
    coeff = (1, (-e) % P, (e*(e+1)//2) % P)
    return tuple(sum(coeff[k]*p[j-k] for k in range(j+1)) % P
                 for j in range(r))


def multiply(a, b, r):
    e, x = a
    f, y = b
    ay = scalar_action(e, y, r)
    return ((e+f) % P, tuple((x[i]+ay[i]) % P for i in range(r)))


def inverse(a, r):
    e, x = a
    y = scalar_action(-e, x, r)
    return (-e % P, tuple(-v % P for v in y))


def comm(a, b, r):
    return multiply(multiply(multiply(a, b, r), inverse(a, r), r),
                    inverse(b, r), r)


def nonsplitting():
    # First stage: base is abelian V x C11; its central 121-cover G2 is
    # nonsplit, since no lift of these commuting base elements can commute.
    for h1, g1 in product(range(P), repeat=2):
        h2 = (2, (0, h1))
        g2 = (7, (1, g1))
        k = comm(h2, g2, 2)
        assert k == (0, (0, 9))
        assert comm((2, (0,)), (7, (1,)), 1) == (0, (0,))
    # Second stage: the double commutator is a defining relation in
    # G2, but EVERY lift of the selected generators to G3 violates it.
    for h1, g1, h2, g2 in product(range(P), repeat=4):
        h = (2, (0, h1, h2))
        g = (7, (1, g1, g2))
        c = comm(h, comm(h, g, 3), 3)
        assert c == (0, (0, 0, 4))
        assert comm((2, (0, h1)), comm((2, (0, h1)),
                                (7, (1, g1)), 2), 2) == (0, (0, 0))
    assert comm((0, (0, 0, 0)), comm((0, (0, 0, 0)),
                                      (0, (1, 0, 0)), 3), 3) == (0, (0, 0, 0))
    assert comm((2, (0, 0, 0)), comm((2, (0, 0, 0)),
                                      (7, (0, 0, 0)), 3), 3) == (0, (0, 0, 0))


def unramified_local_cohomology():
    """H^1_unr = coker(Frob-1) at q23/q127 for r=1,2,3."""
    A23 = ((0, 10), (1, 5))  # irreducible x^2+6x+1
    A127 = ((0, 5), (1, 7))  # (x-1)(x-6)

    def matvec(A, v):
        return tuple(sum(A[i][j]*v[j] for j in range(2)) % P
                     for i in range(2))

    def frobenius(A, e, v, r):
        w = action(e, v, r)
        out = []
        for j in range(r):
            out.extend(matvec(A, w[2*j:2*j+2]))
        return tuple(out)

    def image_matrix(A, e, r):
        n = 2*r
        basis = [tuple(1 if j == i else 0 for j in range(n))
                 for i in range(n)]
        return [tuple((a-b) % P for a, b in zip(frobenius(A,e,v,r),v))
                for v in basis]

    for r in (1, 2, 3):
        n = 2*r
        image23 = image_matrix(A23, 2, r)
        image127 = image_matrix(A127, 4, r)
        assert rank_mod_p(image23, n) == n
        assert rank_mod_p(image127, n) == n-1
        # If the character vanishes at q127, the first/second jet
        # unramified cohomology has extra dimensions, so the uniqueness
        # is a genuine consequence of actual ell(Frob127)=4.
        assert rank_mod_p(image_matrix(A127, 0, r), n) == r
        u0 = (5, 1) + (0,)*(n-2)
        assert rank_mod_p(image127+[u0], n) == n
        # Surjective projection to the residual cokernel + equal dimension
        # gives canonical H1_unr(A_r) -> H1_unr(V) isomorphism.
    return True


def main():
    assert unramified_local_cohomology()
    dims = [lower_central_dimensions(r) for r in (1, 2, 3)]
    assert dims == [[3], [3, 2], [3, 2, 2]], dims
    orders = [P**sum(v) for v in dims]
    assert orders == [1331, 161051, 19487171]
    assert [orders[i]//orders[i-1] for i in (1, 2)] == [121, 121]
    assert 13200*orders[0] == 17569200
    assert 13200*orders[1] == 2125873200
    assert 13200*orders[2] == 257230657200
    # The top filtered coefficient group T^(r-1)V is central
    # for the relative C11 action (not for the full rho group).
    for r in (2, 3):
        for i in range(2):
            v = [0]*(2*r)
            v[-2+i] = 1
            assert diff(2, tuple(v), r) == tuple(0 for _ in v)
    # Without the nontrivial anticyclotomic action the derived group
    # disappears; a direct-product quotient is insufficient.
    for r in (2, 3):
        for j in range(2*r):
            v = tuple(1 if i == j else 0 for i in range(2*r))
            assert diff(0, v, r) == tuple(0 for _ in v)
    nonsplitting()
    print("PASS: q23/q127 unramified H1 dimensions 0/1 across three truncation depths")
    print("PASS: q127 residual projection is an isomorphism, fails if character ell=0")
    print("PASS: exact lower-central graded F11 dimensions (3), (3,2), (3,2,2)")
    print("PASS: 11^3 -> 11^5 -> 11^7 and successive 121-kernel tower")
    print("PASS: separate GL2-dependent total-degree arithmetic")
    print("PASS: 121-extension nonsplitting at both stages via Frobenius commutators")
    print("PASS: 11^4 exhaustive second-stage scalar controls; zero-input tests")
    print("CONDITIONAL ARITHMETIC: first field exists only subject to C0044/C0047 source assumptions")
    print("NONCLAIM: code proves neither first global existence nor second lift, Greenberg or BSD")


if __name__ == "__main__":
    main()
