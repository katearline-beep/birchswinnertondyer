#!/usr/bin/env python3
"""Independent exact checks of SOME derivative-certificate error-budget lemmas.

NOT an L'-nonvanishing certificate: no finite Fourier sum is recomputed.
"""
from fractions import Fraction as F
from math import factorial

N,D,M=234446,-7,2000
c_lo=F(1853789485821,10**15)
c_hi=F(1853789485822,10**15)

def atan_interval(z,n=30):
    v=F(0)
    for k in range(n):
        v+=(-1)**k*z**(2*k+1)/F(2*k+1)
    t=z**(2*n+1)/F(2*n+1)
    return v-t,v+t

l1,h1=atan_interval(F(1,5))
l2,h2=atan_interval(F(1,239))
pilo,pihi=16*l1-4*h2,16*h1-4*l2
assert pilo>3 and pihi<F(22,7)
assert c_lo>0 and N*D*D*c_lo*c_lo<4*pilo*pilo
assert 4*pihi*pihi<N*D*D*c_hi*c_hi

# E1(x) for 0 < x <= 4: alternating series tail after k=30.
rem=F(4**31,31*factorial(31))
assert rem<F(1,10**12)

# Assuming |a_n| <= 2n, E1(cn) <= exp(-cn)/(cn) and
# exp(-c) <= (1+c_lo)^(-1), derive the entire n>2000 tail.
q=1/(1+c_lo)
tail=4*q**(M+1)/(c_lo*(M+1)*(1-q))
assert 14<tail<15

# Value reported by the older still-unported exact Fourier-sum program.
# NOT a recomputed finite-sum certificate in this file!
reported_finite_lower=F(34174485397474,10**12)
assert reported_finite_lower-tail>19

# Negative control: if an exponent in the tail bound is mistakenly
# reduced to M/4, positivity MUST cease to be certified.
corrupt=4*q**(M//4)/(c_lo*(M+1)*(1-q))
assert corrupt>reported_finite_lower

print("PASS: exact pi/c and E1 Taylor remainder bounds")
print("PASS: exact infinite tail bound: 14 < tail < 15")
print("PASS: conditional positive gap using UNVERIFIED historical finite sum")
print("PASS: corrupted tail exponent detected by negative control")
print("MISSING: independent finite sum, coefficients, functional equation")
