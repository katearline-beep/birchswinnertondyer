#!/usr/bin/env python3
"""Falsification/logic guardrails for speculative BSD analytic-rank routes.

These are algebraic countermodels and exact derivative identities. They DO NOT
compute an elliptic L-function, Galois cohomology or p-adic derived heights.

Parity is for the COMPLETED elliptic L-function Lambda, not raw L.
"""
from math import factorial
from fractions import Fraction as F

def multiply(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):
            out[i+j]+=x*y
    return out

def deriv_at_centre(p,k):
    return factorial(k)*p[k] if k<len(p) else 0

def assert_even_parity(p):
    assert all(p[j]==0 for j in range(1,len(p),2))

# Completed L-functions of even sign can have central orders 2 or 4.
completed_rank2=[0,0,1,0,0,0,0]
completed_rank4=[0,0,0,0,1,0,0]
for lam in (completed_rank2,completed_rank4):
    assert_even_parity(lam)
    assert deriv_at_centre(lam,0)==0 and deriv_at_centre(lam,1)==0
    assert deriv_at_centre(lam,3)==0
assert deriv_at_centre(completed_rank2,2)==2
assert deriv_at_centre(completed_rank4,2)==0

# The complex UNCOMPLETED L differs by a nonconstant analytic factor.
# Toy A(u)=e^u; raw L(u)=e^(-u)*Lambda(u).
inverse_factor=[F((-1)**k,factorial(k)) for k in range(8)]
raw_rank2=multiply(completed_rank2,inverse_factor)
raw_rank4=multiply(completed_rank4,inverse_factor)
assert deriv_at_centre(raw_rank2,0)==0 and deriv_at_centre(raw_rank2,1)==0
assert deriv_at_centre(raw_rank2,2)==2
assert deriv_at_centre(raw_rank2,3)==-6   # NOT zero by parity!
assert deriv_at_centre(raw_rank4,2)==0 and deriv_at_centre(raw_rank4,3)==0
assert deriv_at_centre(raw_rank4,4)==24
# Lambda'''=0 implies raw L'''=-3*(A'/A)*raw L'' when L=L'=0;
# in this toy A'/A=1 at center.
assert deriv_at_centre(raw_rank2,3)==-3*deriv_at_centre(raw_rank2,2)

# An odd-sign quadratic twist with nonzero first derivative:
# (L(E/K))'''(1)=3 L''(E,1) L'(twist,1), using L(E)=L'(E)=Ltwist(1)=0.
completed_twist_odd=[0,5,0,3]
raw_twist=multiply(completed_twist_odd,inverse_factor)
for E in (raw_rank2,raw_rank4):
    product=multiply(E,raw_twist)
    assert deriv_at_centre(product,3)==3*deriv_at_centre(E,2)*deriv_at_centre(raw_twist,1)
    if E==raw_rank4:
        assert deriv_at_centre(product,3)==0
    else:
        assert deriv_at_centre(product,3)!=0

# The inverse inference fails without nonzero twist derivative.
twist_deriv_zero=multiply([0,0,0,1],inverse_factor)
assert deriv_at_centre(multiply(raw_rank2,twist_deriv_zero),3)==0
assert deriv_at_centre(raw_rank2,2)!=0

# No fixed finite p-adic congruence implies exact equality zero.
for m in (1,2,4,8):
    nonzero=11**m
    assert nonzero!=0 and nonzero%(11**m)==0

print("PASS: even functional equation applies to COMPLETED, not raw L")
print("PASS: exact relation raw L'''=-3(A'/A)L'' when L=L'=0")
print("PASS: third derivative quadratic-base-change identity and converse guard")
print("PASS: finite p-adic divisibility DOES NOT imply exact zero")
print("NONCLAIM: toy germs are not actual elliptic L-functions or BSD proofs")
