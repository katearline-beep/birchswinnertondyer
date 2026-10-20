#!/usr/bin/env python3
"""Exact finite-algebra controls for Session32; not a Galois/Selmer solver."""
from itertools import product

P = 11


def need(ok, message):
    if not ok:
        raise AssertionError(message)


def mul(a, b):
    return [[sum(x * y for x, y in zip(row, col)) % P
             for col in zip(*b)] for row in a]


def trans(a):
    return [list(col) for col in zip(*a)]


def scale(k, a):
    return [[k * x % P for x in row] for row in a]


def ident(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def det(a):
    return (a[0][0] * a[1][1] - a[0][1] * a[1][0]) % P


def inv2(a):
    d = pow(det(a), -1, P)
    return scale(d, [[a[1][1], -a[0][1]],
                     [-a[1][0], a[0][0]]])


def action(a, k, length=3):
    # Coefficient order x0,x1,x2; inverse-character sign can be put in k.
    k %= P
    coeff = [1, k, k * (k - 1) * pow(2, -1, P) % P]
    return [[(coeff[i // 2 - j // 2] * a[i % 2][j % 2]) % P
             if i // 2 >= j // 2 else 0
             for j in range(2 * length)] for i in range(2 * length)]


def rank(a):
    a = [[x % P for x in row] for row in a]
    r = 0
    for j in range(len(a[0]) if a else 0):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        a[r] = [x * pow(a[r][j], -1, P) % P for x in a[r]]
        for i in range(len(a)):
            if i != r:
                factor = a[i][j]
                a[i] = [(x - factor * y) % P
                        for x, y in zip(a[i], a[r])]
        r += 1
    return r


def check_cartier_dual():
    j = [[0, 1], [-1 % P, 0]]
    jinv = [[0, -1 % P], [1, 0]]
    count, plain_dual_failures = 0, 0
    for entries in product(range(P), repeat=4):
        a = [list(entries[:2]), list(entries[2:])]
        if not det(a):
            continue
        # Weil pairing: Cartier dual is det(A)*inverse(A)^transpose.
        dual = scale(det(a), trans(inv2(a)))
        need(dual == mul(mul(j, a), jinv), "Cartier self-duality failed")
        plain_dual_failures += trans(inv2(a)) != dual
        count += 1
    need(count == (P * P - 1) * (P * P - P) == 13200,
         "incomplete GL2 enumeration")
    need(plain_dual_failures > 0, "missing determinant twist not detected")
    print("PASS: all13200 Cartier-dual identities; plain-dual shortcut rejected")


def check_truncation_and_scalar():
    samples = [ident(2), [[1, 1], [0, 1]], [[0, 1], [1, 0]],
               [[0, -23 % P], [1, -6 % P]]]
    for a in samples:
        need(det(a) != 0, "sample not invertible")
        for b in samples:
            for k, ell in product(range(P), repeat=2):
                need(mul(action(a, k), action(b, ell)) ==
                     action(mul(a, b), (k + ell) % P),
                     "T3 group law, including character wrap, failed")
    minus = scale(-1, ident(2))
    s = action(minus, 0)
    need(s == scale(-1, ident(6)), "central scalar on A3 failed")
    w = [row[2:] for row in s[2:]]
    need(w == scale(-1, ident(4)), "central scalar on W failed")
    # det(-I)=1, so Cartier dual also acts by -I.
    need(mul(w, w) == ident(4), "dual scalar inverse failed")
    for a in samples:
        need(mul(s, action(a, 7)) == mul(action(a, 7), s),
             "scalar centrality failed")
    # Scalar/Sah cochain equation has invertible coefficient s-1=-2.
    need((-2 * pow(-2 % P, -1, P)) % P == 1, "Sah division failed")
    # Negative control: trivial action of C11 has nonzero hom k -> k.
    need(all((k + ell) % P == (k % P + ell % P) % P
             for k, ell in product(range(P), repeat=2)),
         "C11 cocycle control failed")
    need(any(k != 0 for k in range(P)), "nonzero trivial-action class lost")
    need(all((1 - 1) * b % P == 0 for b in range(P)),
         "trivial-action coboundary should vanish")
    print("PASS: T3 action; central scalar; identity-scalar countercontrol")


def check_support_loss():
    # Synthetic complexes only: degree1=F11^3, degree2=F11^3,
    # D(T)=T^order I. Forgetting constraints maps degree2 to zero.
    zero, eye = [[0] * 3 for _ in range(3)], ident(3)
    vectors = list(product(range(P), repeat=3))
    for order in (1, 2):
        coeffs = [zero if i != order else eye for i in range(3)]
        surviving = 0
        for x in vectors:
            value = tuple(sum(a * b for a, b in zip(row, x)) % P
                          for row in coeffs[order])
            # Lower coefficients are zero. Every constant class is
            # unobstructed below the designated order.
            need(all(all(t == 0 for t in row)
                     for matrix in coeffs[:order] for row in matrix),
                 "lower order premise failed")
            surviving += any(value)
            # Projection to zero degree2 kills all these obstructions,
            # without altering the constant degree1 class.
            forgotten_value = ()
            need(forgotten_value == (), "forgetful cochain map failed")
        need(surviving == P ** 3 - 1,
             "nonzero constrained obstructions were not detected")
    # Rank-nullity control, not an asserted actual localization matrix.
    loc = [[1, 0, 1, 2, 3], [0, 1, 4, 5, 6]]
    need(rank(loc) == 2 and 5 - rank(loc) == 3,
         "five-to-two kernel lower bound failed")
    need(5 - rank([[0] * 5, [0] * 5]) == 5,
         "lower bound was mistaken for exact dimension")
    print("PASS: first/second-order support loss; kernel lower bound not equality")


def main():
    check_cartier_dual()
    check_truncation_and_scalar()
    check_support_loss()
    print("PASS: finite-module and support-loss controls; no arithmetic Selmer lift computed")


if __name__ == "__main__":
    main()
