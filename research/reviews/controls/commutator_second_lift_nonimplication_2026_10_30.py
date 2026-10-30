#!/usr/bin/env python3
"""2026-10-30 full-BSD review: exact nonarithmetic first/second-lift falsifier.

Builds a finitely presented TOY group G=<h,g | [h,[h,g]]=1> and its
affine cocycles for inverse action (1+T)^(-ell) over F_11[T]/(T^n).
The numeric first commutator mimics C-0050's ell(h)=2, ell(g)=7,
c0(h)=0 and c0(g)!=0; it is NOT a Galois representation or actual
E[11] Kummer cochain. Nonzero first commutator does not imply
second-order liftability even in a noncommuting first quotient.
"""
from itertools import product

P = 11


def poly_mul(a, b, n):
    return tuple(sum(a[i] * b[k-i] for i in range(k+1)) % P
                 for k in range(n))


def act(e, n):
    # (1+T)^(-e) modulo (11,T^n); here n=2 or 3.
    assert n in (2, 3)
    return (1, (-e) % P) + (((e*(e+1)//2) % P,) if n == 3 else ())


def prod(x, y, n):
    e, c = x
    f, d = y
    a = poly_mul(act(e, n), d, n)
    return ((e+f) % P, tuple((c[i]+a[i]) % P for i in range(n)))


def inv(x, n):
    e, c = x
    a = poly_mul(act((-e) % P, n), c, n)
    return ((-e) % P, tuple(-t % P for t in a))


def comm(x, y, n):
    # [x,y]=x*y*x^(-1)*y^(-1), matching C-0050.
    return prod(prod(prod(x, y, n), inv(x, n), n), inv(y, n), n)


def basis(n, e, c0, c1=0, c2=0):
    return (e % P, (c0 % P, c1 % P) + ((c2 % P,) if n == 3 else ()))


def witness(n, h1=0, g1=0, h2=0, g2=0, eh=2, eg=7, g0=1):
    h = basis(n, eh, 0, h1, h2)
    g = basis(n, eg, g0, g1, g2)
    k = comm(h, g, n)
    r = comm(h, k, n)
    return k, r


k2, r2 = witness(2)
k3, r3 = witness(3)
assert k2 == (0, (0, 9)), (k2, r2)
assert r2 == (0, (0, 0)), (k2, r2)
assert k3[1][:2] == (0, 9), k3
assert r3 == (0, (0, 0, 4)), (k3, r3)

# Exhaustively vary both first and second generator corrections: the
# second-order obstruction of the defining relator is unchanged.
for h1, g1, h2, g2 in product(range(P), repeat=4):
    k, r = witness(3, h1, g1, h2, g2)
    assert k[1][1] == 9
    assert r == (0, (0, 0, 4))

# Removing either essential input kills the obstruction.
assert witness(3, eh=0)[1] == (0, (0, 0, 0))
assert witness(3, g0=0)[1] == (0, (0, 0, 0))
assert comm(basis(3, 2, 0), basis(3, 7, 1), 3)[1][1] == 9

print("PASS: C-0050-style nonzero first commutator (9*T) with first lift")
print("PASS: [h,[h,g]] vanishes modulo T^2 but is 4*T^2 modulo T^3")
print("PASS: all 14641 first/second generator corrections fail second lift")
print("PASS: zero-character and zero-Kummer adversarial controls")
print("NONCLAIM: toy group only; no arithmetic cochain, h2, complex Lpp or BSD theorem")
