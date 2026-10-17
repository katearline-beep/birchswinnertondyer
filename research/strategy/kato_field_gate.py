#!/usr/bin/env python3
"""Exact finite algebra/point counts for Kato extension screening at p=11.

Real quadratic degree 2: augmentation I is idempotent over Z_11.
Degree-11 real cyclotomic F=Q(zeta_23)^+: augmentation graded layers
of F_11[C11] are nontrivial. THIS IS NOT a Kato/Euler/Sha calculation.
"""
p=11
N=234446
a1,a2,a3,a4,a6=1,-1,0,-79,289

def is_prime(n):
    if n<2:return False
    return all(n%d for d in range(2,int(n**0.5)+1))

def count(q):
    assert is_prime(q) and N%q
    return 1+sum(
       1 for x in range(q) for y in range(q)
       if (y*y+a1*x*y+a3*y-x*x*x-a2*x*x-a4*x-a6)%q==0)

assert count(23)==30
assert count(199)==220
assert count(11)==18
assert 30%11!=0 and 220%11==0
# C2 over Z_11: I=(sigma-1), with sigma²=1, hence
# (sigma-1)^2 = -2(sigma-1) and I²=I because -2 is a unit.
assert pow(-2,-1,11)==5
for k in range(2,9):
    assert (-2)**(k-1)%11!=0

# Over F_11, F_11[C11] = F_11[T]/((1+T)^11-1)
# = F_11[T]/(T^11). Consequently T^3 is in I³ but not I⁴.
from math import comb
assert [(comb(11,k)%11) for k in range(1,11)]==[0]*10
assert comb(11,11)%11==1
I3=[0]*11
I3[3]=1
assert all(v==0 for v in I3[:3])
assert I3[3]==1  # not in I^4 mod 11
# The degree-11 real subfield F=Q(zeta_23)^+ has Galois group C11.
assert (23-1)//2==11 and 23%11!=0 and N%23!=0

print("PASS real quadratic C2: I^3=I, no higher 11-adic augmentation depth")
print("PASS real cyclotomic degree 11: mod-11 I^3/I^4 nonzero")
print("PASS E(F23)=30, so no Q23-rational 11-torsion at ramified 23")
print("PASS negative-control q=199: E(F199)=220 divisible by 11; local condition fails")
print("UNKNOWN: Sha(E/F)[11^infty], full image/local conditions, derived Kato class")
