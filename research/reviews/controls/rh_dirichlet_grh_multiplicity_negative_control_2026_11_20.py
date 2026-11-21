#!/usr/bin/env python3
"""Exact central-Taylor countermodel, not an elliptic-curve L-function.

Let t=s-1, phi(t)=sinh(t)/t with phi(0)=1.
F_2=t^2 phi, F_4=t^4 phi, G=t phi. Each is an entire function
of order one, with all zeros on Re(s)=1 and signs F(2-s)=+F(s),
G(2-s)=-G(s). Yet F_2''(1)=2 and F_4''(1)=0 while G'(1)=1.
The real-analytic zero-location assertion is proved in the accompanying
note from zeros of sinh(t), not by finite testing.
"""
from fractions import Fraction
from math import factorial

N = 10

def product(a, b):
    """Convolution in Q[t]/(t^(N+1))."""
    return [sum((a[k] * b[j - k] for k in range(j + 1)), Fraction(0))
            for j in range(N + 1)]

def shift(a, k):
    return [Fraction(0) if j < k else a[j - k] for j in range(N + 1)]

def derivative_at_zero(a, k):
    return a[k] * factorial(k)

# sinh(t)/t = sum_{n>=0} t^(2n)/(2n+1)! exactly.
phi = [Fraction(1, factorial(j+1)) if j % 2 == 0 else Fraction(0)
       for j in range(N + 1)]
f2 = shift(phi, 2)
f4 = shift(phi, 4)
g = shift(phi, 1)

assert phi[0] == 1
assert all(phi[j] == 0 for j in range(1, N + 1, 2))
assert all(f2[j] == f4[j] == 0 for j in range(1, N + 1, 2))
assert all(g[j] == 0 for j in range(0, N + 1, 2))
assert derivative_at_zero(f2, 2) == 2
assert derivative_at_zero(f4, 2) == 0
assert derivative_at_zero(g, 1) == 1

b2 = product(f2, g)
b4 = product(f4, g)
assert derivative_at_zero(b2, 3) == 6
assert derivative_at_zero(b4, 3) == 0

# Independent Leibniz computation of third derivative, using lower jets.
def product_third(f, twist):
    return (derivative_at_zero(f, 3) * derivative_at_zero(twist, 0)
            + 3 * derivative_at_zero(f, 2) * derivative_at_zero(twist, 1)
            + 3 * derivative_at_zero(f, 1) * derivative_at_zero(twist, 2)
            + derivative_at_zero(f, 0) * derivative_at_zero(twist, 3))
assert product_third(f2, g) == derivative_at_zero(b2, 3)
assert product_third(f4, g) == derivative_at_zero(b4, 3)

# Deliberately reject the overstrong conclusion "functional equations
# and all zeros on the central line force vanishing second derivative".
assert not (derivative_at_zero(f2, 2) == 0), "negative control failed"
assert derivative_at_zero(f4, 2) == 0, "rank-four comparison failed"
print("PASS: exact order-1 entire completed-function model: critical-line zeros")
print("F2''(1)=2, F4''(1)=0, G'(1)=1; base-change cubic jets=6 and 0")
print("No claim about actual elliptic curves or Dirichlet L-functions")
