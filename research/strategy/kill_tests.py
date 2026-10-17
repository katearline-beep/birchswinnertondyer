#!/usr/bin/env python3
"""Falsification/logic guardrails for speculative BSD analytic-rank routes.

These are algebraic countermodels and exact derivative identities. They DO NOT
compute an elliptic L-function, Galois cohomology or p-adic derived heights.
"""
from math import factorial

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

# An even sign and L(1)=0 can coexist with analytic order 2 OR 4.
rank2_model=[0,0,1,0,0,0,0]
rank4_model=[0,0,0,0,1,0,0]
for E in (rank2_model,rank4_model):
    assert_even_parity(E)
    assert deriv_at_centre(E,0)==0 and deriv_at_centre(E,1)==0
    assert deriv_at_centre(E,3)==0
assert deriv_at_centre(rank2_model,2)==2
assert deriv_at_centre(rank4_model,2)==0
assert deriv_at_centre(rank4_model,4)==24

# A quadratic twist with odd sign and nonzero central derivative gives
# (L(E/K))'''(1) = 3 L''(E,1) * L'(twist,1), using functional equation.
twist_odd=[0,5,0,3]
for E in (rank2_model,rank4_model):
    product=multiply(E,twist_odd)
    assert deriv_at_centre(product,3)==3*deriv_at_centre(E,2)*deriv_at_centre(twist_odd,1)
    assert deriv_at_centre(product,3)==0 if E==rank4_model else deriv_at_centre(product,3)!=0

# The inverse inference FAILS without nonzero twist derivative.
twist_deriv_zero=[0,0,0,1]
assert deriv_at_centre(multiply(rank2_model,twist_deriv_zero),3)==0
assert deriv_at_centre(rank2_model,2)!=0

# No fixed finite p-adic congruence is evidence of exact real equality:
# this nonzero integer vanishes mod 11^m.
for m in (1,2,4,8):
    nonzero=11**m
    assert nonzero!=0 and nonzero%(11**m)==0

print("PASS: parity and L(1)=0 DO NOT distinguish rank-two vs rank-four Taylor germs")
print("PASS: third derivative factorization over K_D; fails converse without twist derivative")
print("PASS: finite p-adic divisibility DOES NOT imply exact zero")
print("NONCLAIM: these are formal toy germs, not actual L-functions or proofs of BSD")
