#!/usr/bin/env python3
"""2026-10-23 WPR: exact toy nonimplications, not arithmetic E/K cochains.

Demonstrates that a C11 group ring mod 11 cannot substitute for the C121
layer at modulus 121 and that a uniquely normalized first-order lift does not
force a second-order lift. Pure standard-library finite algebra.
"""
P = 11

def mul(a, b, modulus, degree=2):
    out = [0] * degree
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j < degree:
                out[i + j] = (out[i + j] + x*y) % modulus
    return tuple(out)

def power(a, exponent, modulus, degree=2):
    out = (1,) + (0,) * (degree - 1)
    while exponent:
        if exponent & 1:
            out = mul(out, a, modulus, degree)
        a = mul(a, a, modulus, degree)
        exponent //= 2
    return out

# Group relation gamma^11=1 is compatible with gamma->1+T over F11[T]/T^2,
# but NOT over (Z/121)[T]/T^2; the latter requires gamma^121=1.
assert power((1, 1), 11, 11) == (1, 0)
assert power((1, 1), 11, 121) == (1, 11)
assert power((1, 1), 121, 121) == (1, 0)
assert power((1, 1), 11, 121) != (1, 0)
print('PASS: C11 residual group-ring action fails the mod121 T^2 relation; C121 is needed')

# The actual Session37 local norm residue 115 mod121 is 5 mod11; the residual
# datum 5 alone cannot determine a lift to Z/121, despite being a unit.
assert 115 % 11 == 5 % 11
assert 115 % 121 != 5 % 121
assert 115 % 11 != 0
print('PASS: unit residual norm coordinate does not identify its mod121 lift')

# Two complexes of free modules over F11[u]/u^3, concentrated in degrees 1,2.
# Differential d_0=d_1=0 in both. In A, d_2=0; in B, d_2=identity.
# Both have exactly the same base cocycle x=1 and first-order lifts.
# Choose a local affine coordinate 5*t+3; it has a UNIQUE zero modulo 11.
solutions = [t for t in range(P) if (5*t + 3) % P == 0]
assert solutions == [6]

def differential(x, second_coefficient):
    # For x=1+a*u+b*u^2, d(x) = second_coefficient*u^2 mod u^3.
    return (0, 0, second_coefficient*x[0] % P)

for a in range(P):
    for b in range(P):
        lift = (1, a, b)
        assert differential(lift, 0) == (0, 0, 0)
        assert differential(lift, 1) == (0, 0, 1)
print('PASS: identical uniquely normalized first-order data coexist with zero or nonzero second obstruction')
print('NONCLAIM: toy complexes and group rings are NOT Galois cochains, Selmer lifts, h2, or complex L derivatives')
