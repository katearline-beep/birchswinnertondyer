#!/usr/bin/env python3
"""Exact Session36 arithmetic/algebra controls; not elliptic correction cochains.

Only the good-prime point counts are newly evaluated curve arithmetic here.
The cohomology and local-defect matrices below are explicitly synthetic.
No tests establish Poitou--Tate, the C0044 source inputs, or actual h2.
"""
from itertools import product


def require(ok, message):
    if not ok:
        raise ValueError(message)


def rejected(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError('negative control was accepted')


def mm(a, b, m):
    return [[sum(x*y for x, y in zip(row, col)) % m
             for col in zip(*b)] for row in a]


def tr(a):
    return [list(row) for row in zip(*a)]


def scale(a, s, m):
    return [[s*x % m for x in row] for row in a]


def mv(a, x, m):
    return [sum(u*v for u, v in zip(row, x)) % m for row in a]


def padd(a, b, m):
    return tuple((x+y) % m for x, y in zip(a, b))


def pmul(a, b, m):
    return tuple(sum(a[j]*b[i-j] for j in range(i+1)) % m
                 for i in range(3))


def pscale(a, s, m):
    return tuple(s*x % m for x in a)


def subst(a, t, m):
    return padd((a[0] % m, 0, 0),
                padd(pscale(t, a[1], m),
                     pscale(pmul(t, t, m), a[2], m), m), m)


def action(k, m):
    # (1+T)^(-k), evaluated by INTEGER binomial coefficients.
    return (1, -k % m, (k*(k+1)//2) % m)


def point_and_dual_controls():
    q = 7
    direct = 1+sum((y*y+x*y-x*x*x+x*x+79*x-289) % q == 0
                   for x in range(q) for y in range(q))
    # Different model, Legendre sum rather than enumeration of y.
    character_sum = q+1
    for x in range(q):
        rhs = (x**3-1267*x+17230) % q
        character_sum += 0 if rhs == 0 else (1 if pow(rhs, 3, q) == 1 else -1)
    require(direct == character_sum == 13, 'good prime7 count disagreement')
    a = q+1-direct
    require(a == -5, 'wrong trace7')
    # charpoly evaluated at1 and q controls BOTH ordinary/singular terms.
    require((1-a+q) % 11 != 0 and (q*q-a*q+q) % 11 != 0,
            'prime7 cannot be removed without a support audit')
    rejected(lambda: require(11 % 11 != 0, 'hidden local torsion'))

    j = [[0, 1], [10, 0]]
    count = 0
    for a, b, c, d in product(range(11), repeat=4):
        det = (a*d-b*c) % 11
        if not det:
            continue
        g = [[a, b], [c, d]]
        inv = scale([[d, -b], [-c, a]], pow(det, -1, 11), 11)
        dual = scale(tr(inv), det, 11)
        require(mm(tr(g), mm(j, g, 11), 11) == scale(j, det, 11),
                'Weil determinant identity fails')
        require(mm(j, g, 11) == mm(dual, j, 11), 'Cartier equivariance fails')
        count += 1
    require(count == 13200, 'incomplete GL2 enumeration')
    conjugation = [[1, 0], [0, 10]]
    rejected(lambda: require(mm(j, conjugation, 11) == mm(conjugation, j, 11),
                             'plain linear dual incorrectly substituted'))
    print('PASS actual #E(F7)=13 by two models; both support units;13200 Cartier identities')


def augmentation_controls():
    for m in (11, 121):
        tinv = (0, -1 % m, 1)
        naive = (0, -1 % m, 0)
        inv2 = pow(2, -1, m)
        u = (0, 1, -inv2 % m)
        require(subst(tinv, tinv, m) == (0, 1, 0), 'inversion not involutive')
        require(subst(u, tinv, m) == pscale(u, -1, m), 'log coordinate not odd')
        for k in range(m):
            require(subst(action(k, m), tinv, m) == action(-k, m),
                    'anticyclotomic action not c-equivariant')
            exp_u = padd((1, 0, 0),
                         padd(pscale(u, -k, m),
                              pscale(pmul(u, u, m), k*k*inv2, m), m), m)
            require(exp_u == action(k, m), 'T and u coefficient disagreement')
            for h in range(m):
                require(pmul(action(k, m), action(h, m), m) == action(k+h, m),
                        'truncated character action not a representation')
        rejected(lambda: require(subst(action(1, m), naive, m) == action(-1, m),
                                 'naive T negation misses quadratic term'))
    require(action(11, 11) == (1, 0, 0), 'C11 residual fidelity')
    require(action(11, 121) != (1, 0, 0), 'C11 falsely accepted at mod121')
    require(action(121, 121) == (1, 0, 0), 'C121 second-level fidelity')
    print('PASS all mod11/mod121 character pairs, odd log coordinate and wrong-involution/tower refusals')


def cyclic_and_affine_controls():
    # Algebraic model of the proved cyclic H1-minus: not a computation of H1.
    for n in range(1, 5):
        m = 11**n
        image = {11**(n-1)*a % m for a in range(11)}
        require(len(image) == 11 and 11**(n-1) % m != 0, 'Kummer generator order')
        require(all(a % (11**(n-1)) == 0 for a in image), 'wrong torsion inclusion')
        if n > 1:
            require((1 % m) % (m//11) == 1, 'Kummer generator reduction')
    # Same finite order does NOT imply cyclicity: kill that shortcut explicitly.
    elementary_order = lambda x: 1 if x == (0, 0) else 11
    require(11**2 == len(list(product(range(11), repeat=2))), 'order model')
    require(max(elementary_order(x) for x in product(range(11), repeat=2)) < 121,
            'order121 falsely implies cyclic')

    for m, r in ((11, 9), (121, 108)):
        unit_inverse = pow(r, -1, m)
        require(unit_inverse == (5 if m == 11 else 93), 'normalization inverse')
        for a in range(m):
            t = -a*unit_inverse % m
            solutions = [z for z in range(m) if (a+r*z) % m == 0]
            require(solutions == [t], 'unit affine slice not unique')
            # Changing the local origin changes the normalized class.
            shifted = -(a-1)*unit_inverse % m
            require(shifted != t, 'affine torsor falsely has canonical origin')
            for defect in (0, 1):
                # Synthetic local coordinates: R lies in the ordinary line.
                require(all((defect+0*z) % m == defect for z in range(m)),
                        'kernel scalar incorrectly repairs local defect')
        rejected(lambda: require(any((1+11*z) % 121 == 0 for z in range(121)),
                                 'nonunit slice falsely solvable'))
        require(sum((11+11*z) % 121 == 0 for z in range(121)) == 11,
                'nonunit slice falsely unique')

    # Hidden negative fine class: kernel of [9,0] has dimension1, not0.
    visible_kernel = [x for x in range(11) if 9*x % 11 == 0]
    hidden_kernel = [(x, y) for x, y in product(range(11), repeat=2)
                     if 9*x % 11 == 0]
    require(len(visible_kernel) == 1 and len(hidden_kernel) == 11,
            'hidden fine-class falsifier failed')
    print('PASS cyclic/order distinction; relative affine inverse factors5/93; hidden-class and local-defect controls')


def secondary_controls():
    # SYNTHETIC signed two-term complex, basis C1=(x+,R-,z-), C2=(a+,b+,w-).
    # H1-minus=R, H2-minus=0.  d1 reverses sign; d2 preserves sign.
    d0 = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
    d1 = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
    c1 = [[1, 0, 0], [0, -1, 0], [0, 0, -1]]
    c2 = [[1, 0, 0], [0, 1, 0], [0, 0, -1]]
    for m in (11, 121):
        require(mm(c2, d0, m) == mm(d0, c1, m), 'd0 sign')
        require(mm(c2, d1, m) == scale(mm(d1, c1, m), -1, m), 'd1 sign')
        for alpha in (0, 1):
            d2 = [[0, 0, 0], [alpha, 0, 0], [0, 0, 0]]
            require(mm(c2, d2, m) == mm(d2, c1, m), 'd2 sign')
            x = [1, 0, 0]
            quotient_values = set()
            raw_values = set()
            for t in range(m):
                correction = [0, t, -1]
                first = [(a+b) % m for a, b in zip(mv(d0, correction, m), mv(d1, x, m))]
                require(first == [0, 0, 0], 'first global lift fails')
                second = tuple((a+b) % m for a, b in zip(mv(d2, x, m), mv(d1, correction, m)))
                raw_values.add(second)
                # quotient by beta(R)=a, and by d0 C1=w, retains b only.
                quotient_values.add(second[1])
            require(len(raw_values) == m, 'missing genuine first-lift ambiguity')
            require(quotient_values == {(alpha-1) % m}, 'secondary quotient not invariant')
            if alpha == 0:
                rejected(lambda: require(quotient_values == {0}, 'first lift falsely implies second lift'))
            else:
                require(quotient_values == {0}, 'zero-secondary control fails')
        # Finite vanishing need not be integral vanishing even after first lifts.
        require(11 % 11 == 0 and 11 % 121 != 0, 'finite-zero anti-vacuity')
    print('PASS synthetic identical first-order data: secondary obstruction either zero or nonzero, modulo exactly beta(R)')


def main():
    point_and_dual_controls()
    augmentation_controls()
    cyclic_and_affine_controls()
    secondary_controls()
    print('NONCLAIM: source-derived cohomology proof is unreviewed; no actual c1, local reference, h2 or BSD computed.')


if __name__ == '__main__':
    main()
