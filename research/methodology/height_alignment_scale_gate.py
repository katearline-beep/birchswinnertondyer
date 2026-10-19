#!/usr/bin/env python3
"""Necessary finite-level test for speculative local/global height alignment.

Input height vectors here are FORMAL CONTROLS, not computed global heights.
No Sha, analytic vanishing, or anticyclotomic height is established.
"""
p = 11
n = 4
mod = p ** n
u = (7462, 14432, 1427, 7989)  # normalized local logs of P1..P4
assert u[0] % p == 4
assert tuple(x * pow(u[0], -1, p) % p for x in u) == (1, 0, 2, 9)


def primitive_test(a):
    """Return (precision remaining, normalized residues, wedge residues).

    Scalars a_i in Q_11 can always be scaled into Z_11; however a finite
    observation modulo 11^n cannot support a primitive conclusion if all
    entries vanish modulo 11^n. After removing a common factor 11^k,
    only n-k reliable digits remain.
    """
    assert len(a) == 4
    a = [int(x) % mod for x in a]
    if all(x == 0 for x in a):
        return None  # indeterminate rather than aligned
    k = min(next(i for i in range(n) if x % (p ** (i + 1))) for x in a if x)
    precision = n - k
    m = p ** precision
    primitive = tuple((x // (p ** k)) % m for x in a)
    wedge = tuple((u[0] * primitive[j] - u[j] * primitive[0]) % m
                  for j in (1, 2, 3))
    return precision, primitive, wedge


# Proposed alignment passes only when genuinely primitive data agree.
assert primitive_test(u)[2] == (0, 0, 0)
assert primitive_test(tuple(11 * x for x in u))[2] == (0, 0, 0)

# A symmetry-compatible rank-two *toy* height with cross vector e_2
# has a distinct radical from the local-log kernel.
bad = (0, 1, 0, 0)
assert primitive_test(bad)[2][0] == u[0] % mod

# Negative control: without primitive normalization these heights look
# perfectly aligned mod 11^3 (all zero), yet fail in the first reliable digit.
masked = tuple((11 ** 3) * x for x in bad)
assert all((u[0] * masked[j] - u[j] * masked[0]) % (11 ** 3) == 0
           for j in (1, 2, 3))
precision, normalized, wedge = primitive_test(masked)
assert precision == 1 and normalized == (0, 1, 0, 0)
assert wedge[0] % p == 4
assert primitive_test((0, 0, 0, 0)) is None

# The cheaply testable 11-adic projective obstruction, if L11 is true:
# after removing a common power of 11, a1 MUST be a unit and
# [a1:a2:a3:a4] ≡ [1:0:2:9] modulo 11.
for good in (u, tuple(11 * x for x in u)):
    _, v, _ = primitive_test(good)
    assert v[0] % p != 0
    assert tuple(x * pow(v[0], -1, p) % p for x in v) == (1, 0, 2, 9)

print('PASS projective local logarithm profile [1:0:2:9] mod 11')
print('PASS primitivity catches p^3-masked false-positive height data')
print('PASS zero finite-vector returns indeterminate, not aligned')
print('NONCLAIM: no global anticyclotomic height value was computed')
