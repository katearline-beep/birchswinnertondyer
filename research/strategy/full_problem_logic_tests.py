#!/usr/bin/env python3
"""Logic guardrails for whole-BSD review.

Formal Taylor polynomials and numerical rounding countermodels are NOT real
elliptic L-functions. The experiment only rejects inference shortcuts.
"""
from fractions import Fraction as F
from math import factorial

def D(poly,r):
    return (poly[r] if r<len(poly) else 0)*factorial(r)

# Both COMPLETED even-sign germs satisfy vanishing at order 0 and 1.
# A root sign + and vanishing L(1) do NOT prove order four.
rank2_candidate=[F(0),F(0),F(1),F(0),F(1)]
rank4_candidate=[F(0),F(0),F(0),F(0),F(1)]
for germ in (rank2_candidate,rank4_candidate):
    assert D(germ,0)==D(germ,1)==D(germ,3)==0
assert D(rank2_candidate,2)==2
assert D(rank4_candidate,2)==0
assert D(rank4_candidate,4)==24

# A finite positive fourth derivative does not exclude a second-order zero.
mixed=[F(0),F(0),F(1),F(0),F(1)]
assert D(mixed,4)==24 and D(mixed,2)!=0

# Approximate BSD special-value quotients may coincide under reported
# decimals but differ exactly; numerical Sha_an≈1 does not prove Sha=1.
reported=F(1)
perturbed=F(1)+F(1,10**40)
assert reported!=perturbed
assert f"{float(reported):.10f}"==f"{float(perturbed):.10f}"

# Even full BSD verified for one labelled curve would not establish it
# universally. Toy predicate on a universe of two labels.
case_proved={"234446.a1":True,"arbitrary_other_curve":False}
assert case_proved["234446.a1"] is True
assert not all(case_proved.values())

# The pair (rank-four algebraic datum, numerical analytic rank four)
# does not encode a proven exact zero. Merely "tiny" numerical L''
# can be nonzero at any fixed finite precision.
for k in (20,40,90):
    small=F(1,10**k)
    assert small!=0
    assert small<F(1,10**(k-1))

print("PASS: even sign and fourth derivative alone do not force second derivative zero")
print("PASS: approximate analytic Sha=1 does not establish exact Sha order")
print("PASS: one-curve theorem is not the full quantified BSD conjecture")
print("PASS: numerical smallness does not imply an exact complex zero")
print("NONCLAIM: these are formal logical controls, not elliptic L-functions")
