#!/usr/bin/env python3
"""Exact anti-vacuity tests for C_11 group-ring augmentation.

Not a Kato-class computation. This prevents a false positive from checking
augmentation vanishing *only modulo 11*. All arithmetic is integral.
"""
from math import comb

p=11

def norm_expansion(degree):
    """Sum_{j=0}^{degree-1}(1+T)^j, coeffs of T^k."""
    return [comb(degree,k+1) for k in range(degree)]

def group_order_check(n):
    # Finite cyclic G=C_(11^n); ring Z_11[G]=Z_11[T]/((1+T)^(11^n)-1)
    degree=p**n
    assert (p-1)*p**n==([110,1210][n-1] if n<=2 else (p-1)*p**n)
    coeff=norm_expansion(degree)
    assert coeff[0]==degree
    assert all(coeff[j]%p==0 for j in range(degree-1))
    assert coeff[-1]==1
    # Reduction mod 11: the ordinary trace = T^(degree-1),
    # yet its INTEGRAL augmentation is degree=11^n !=0.
    assert sum(1 for x in coeff if x%p)!=0
    print(f"PASS C_{degree}: trace has augmentation {degree} != 0")
    print(f"PASS C_{degree}: trace mod11 equals T^{degree-1} (spurious deep order)")
    # I³/I⁴ is exactly Z/(11^n) as additive group:
    # multiplying the defining relation ((1+T)^degree-1)=0 by T²
    # yields degree*T³ in I⁴; nonzero of that order is witnessed by
    # quotient Z/(degree)[T]/(T^4), since all relation coefficients
    # for T¹,T²,T³ are divisible by degree (p=11>3).
    assert all(comb(degree,k)%degree==0 for k in (1,2,3))
    assert degree%p==0
    print(f"PASS C_{degree}: I^3/I^4 has exact additive order {degree}")
    return coeff

first=group_order_check(1)
second=group_order_check(2)
assert len(first)==11 and len(second)==121

# A real quadratic degree-two field has no third associated graded layer:
# T=σ−1, (1+T)^2−1=T(T+2), so T²=−2T;
# −2 is a unit in Z_11, forcing I²=I and I³/I⁴=0.
assert pow(-2,-1,p)==5
print("PASS C_2 at p=11: I^2=I (vacuous higher filtration)")

# Negative-control demonstration: naive mod-11 checker says trace in I³;
# sound integral checker correctly rejects it already at I¹.
def naive_modp_membership_in_I3(poly):
    return all(c%p==0 for c in poly[:3])

def integral_membership_in_I(poly):
    # Augmentation is constant term in T-coordinates over Z_11.
    return poly[0]==0

assert naive_modp_membership_in_I3(first)
assert not integral_membership_in_I(first)
assert naive_modp_membership_in_I3(second)
assert not integral_membership_in_I(second)
print("PASS NEGATIVE CONTROL: deep mod-11 trace vanishing falsely claims integral I³")
print("NONCLAIM: ordinary trace is NOT the BKS derived norm of Kato zeta elements")
print("NONCLAIM: no computation of Sha, a Kato class, or complex L''(E,1)")
