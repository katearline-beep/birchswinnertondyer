#!/usr/bin/env python3
"""Session 15: exact MINIMAL-MODEL affine check of C-0011, six cross-point tests.

Independently obtains [36]Q on the *minimal* Weierstrass equation and
certifies the proposed division-polynomial denominator D is primitive by
gcd_Z(N(x([36]Q) D^2), N(D)) = 1. Also tests all six cross-height
bilinearity relations h(Pi+Pj+R)=h(Pi+R)+h(Pj+R) mod 11.

Imports C-0011 as a SOURCE for proposed division-polynomial D, the
Q(sqrt(-7)) arithmetic and coefficients. Thus an orthogonal arithmetic
check, NOT an independent end-to-end p-adic sigma package or proof of BSD.
"""
import contextlib
import importlib.util
import io
import math
import sys
from fractions import Fraction as F
from math import isqrt, lcm
from pathlib import Path

sys.set_int_max_str_digits(100000)
source = Path(__file__).with_name("provisional_height_mod11.py")
spec = importlib.util.spec_from_file_location("_bsd_s14_source", source)
s14 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(s14)
K = s14.K
P = [((x+1)/4, (y-x-1)/8) for x, y in s14.points]
R = ((s14.R[0]+1)/4, (s14.R[1]-s14.R[0]-1)/8)
mod = 11**7
prime = 11

def oncurve(Q):
    x, y = Q
    assert y*y+x*y == x*x*x-x*x-79*x+289

def add(Q, U):
    if Q is None: return U
    if U is None: return Q
    x, y = Q
    a, b = U
    if x == a:
        if y+b+x == K(0): return None
        slope = (3*x*x-2*x-79-y)/(2*y+x)
    else:
        slope = (b-y)/(a-x)
    intercept = y-slope*x
    xx = slope*slope+slope+1-x-a
    yy = -(slope+1)*xx-intercept
    V = xx, yy
    oncurve(V)
    return V

def mul(n, Q):
    total = None
    while n:
        if n & 1: total = add(total, Q)
        n //= 2
        if n: Q = add(Q, Q)
    return total

def integer(z):
    return (z.a-z.b).denominator == 1 and (2*z.b).denominator == 1

def sqrt_rat(z):
    if z < 0: return None
    a, b = isqrt(z.numerator), isqrt(z.denominator)
    return F(a, b) if a*a == z.numerator and b*b == z.denominator else None

def sqrt_k_up_to_unit(z):
    for sign in (1, -1):
        zz = z*sign
        rootnorm = sqrt_rat(s14.norm(zz))
        if rootnorm is None: continue
        for s in (rootnorm, -rootnorm):
            a = sqrt_rat((zz.a+s)/2)
            if a is not None and a:
                b = zz.b/(2*a)
                root = K(a, b)
                if root*root == zz: return root
        if zz.b == 0 and zz.a <= 0:
            b = sqrt_rat(-zz.a/F(7))
            if b is not None: return K(0, b)
    raise AssertionError("x-denominator ideal not a principal square up to unit")

def initial_denominator(Q_short):
    x, y = s14.mincoord(Q_short)
    a, b = x.a-x.b, 2*x.b
    D = lcm(a.denominator, b.denominator)
    g = s14.gcd(x*D, K(D))
    d = sqrt_k_up_to_unit(K(D)/g)
    s14.cert(Q_short, d)
    return d

def next_denominator(Q_short, d):
    B = s14.add(Q_short, Q_short)
    raw = (Q_short[1]/4)*d*d*d*d
    candidates = []
    for c in (1, 2, 4, 8, 16):
        candidate = raw/c
        if not integer(candidate): continue
        try:
            s14.cert(B, candidate)
        except AssertionError:
            continue
        candidates.append((c, candidate))
    assert len(candidates) == 1, "unique primitive doubling correction"
    c, dB = candidates[0]
    return B, c, dB

def wroot():
    r = 2
    for j in range(1, 7):
        r = next(r+k*prime**j for k in range(prime)
                 if ((r+k*prime**j)**2+7) % prime**(j+1) == 0)
    return r

def reduced(z, w):
    def modrat(f):
        assert f.denominator % prime != 0, "unexpected 11-adic denominator"
        return f.numerator*pow(f.denominator, -1, mod) % mod
    return (modrat(z.a)+w*modrat(z.b)) % mod

roots = (wroot(), -wroot() % mod)

def test_height(Q_min, D):
    T = mul(36, Q_min)
    x, y = T
    X = x*D*D
    Y = y*D*D*D
    assert integer(X) and integer(Y), "candidate D does not clear denominators"
    norm_D, norm_X = s14.norm(D), s14.norm(X)
    assert norm_D.denominator == norm_X.denominator == 1
    assert math.gcd(int(norm_D), int(norm_X)) == 1, "NONPRIMITIVE denominator"
    # If a prime ideal divided both X and D, its rational prime would
    # divide both norms. Coprime integer norms therefore prove primitivity.
    t = -x/y
    t_over_D = t/D
    units = []
    for w in roots:
        tm, um = reduced(t, w), reduced(t_over_D, w)
        assert tm % prime == 0 and um % prime != 0
        # The integral sigma series is t + (1/2)t^2 + O(t^3).
        units.append(um*(1+tm*pow(2, -1, mod)) % mod)
    q = units[0]*pow(units[1], -1, mod) % (prime**2)
    h36 = ((pow(q, 10, 121)-1)//11)*pow(10, -1, 11) % 11
    h = h36*pow(36*36, -1, 11) % 11
    return q, h

def to_short(Q):
    x, y = Q
    return 4*x-1, 8*y+4*x

for Q in P+[R]:
    oncurve(Q)

single_heights = []
for i in range(4):
    A = add(P[i], R)
    short = to_short(A)
    d = initial_denominator(short)
    assert s14.norm(d) == s14.expected_dA[i]
    B, c, dB = next_denominator(short, d)
    assert c == s14.corrections[i]
    big = s14.division(B, dB, 18)*dB
    q, h = test_height(A, big)
    assert (q, h) == (s14.expected_q[i], s14.expected_height[i])
    single_heights.append(h)
    print(f"A{i+1}: primitive 36A denominator PASS; q={q}; h={h} (mod 11)")

pair_q = {(0,1):47, (0,2):67, (0,3):15, (1,2):15, (1,3):16, (2,3):64}
for (i,j), expected_q in pair_q.items():
    Q = add(add(P[i], P[j]), R)
    short = to_short(Q)
    d = initial_denominator(short)
    B, c, dB = next_denominator(short, d)
    big = s14.division(B, dB, 18)*dB
    q, h = test_height(Q, big)
    assert q == expected_q
    assert h == (single_heights[i]+single_heights[j]) % 11
    print(f"A{i+1}{j+1}: primitive denominator PASS; q={q}; h={h}, pair bilinearity PASS")
assert single_heights == [1,2,7,8]
print("PASS four independently affine 36A primitivity certificates and all SIX distinct polarization controls.")
print("CONDITIONAL: h vector [1:2:7:8] differs from local log [1:0:2:9] mod 11.")
print("NONCLAIM: uses C-0011 division-polynomial D and first sigma coefficient;")
print("NONCLAIM: no external Sage/Magma height package, derived height, or BSD proof.")
