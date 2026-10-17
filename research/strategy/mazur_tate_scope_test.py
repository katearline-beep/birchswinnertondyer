#!/usr/bin/env python3
"""Applicability/logic negative controls for BKS 2025 Mazur–Tate result.

Checks elementary arithmetic and prevents use of a theorem WHICH ASSUMES BSD
as if it proves BSD. No Mazur–Tate modular element is computed.
The theorem numbering is from arXiv:2103.11535v1, not audited final typeset.
"""
from math import gcd,isqrt

N,p,r=234446,11,4
def is_squarefree(m):
    return all(m%(k*k) for k in range(2,isqrt(m)+1))
def smooth_good(q):
    return 1+sum(
       (y*y+x*y-x**3+x*x+79*x-289)%q==0
       for x in range(q) for y in range(q))
assert smooth_good(11)==18
a11=12-smooth_good(11)
assert a11==-6 and a11%11!=0  # good ordinary, NOT supersingular at 11

# Our selected fields both have abstract Gal = C11, but their
# conductors differ; the 2025 Theorem 1.1 hypothesis (a) includes
# a SQUAREFREE conductor for the extension.
m_other,m_tower=23,121
assert gcd(m_other,N)==gcd(m_tower,N)==1
assert is_squarefree(m_other)
assert not is_squarefree(m_tower)
assert r==4 and r!=1

def theorem1_1_can_be_invoked(field_conductor,bsd_proved,perrin_riou_proved):
    """Theorem 1.1 has other hypotheses not handled by this checker!

    This predicate models only the explicitly blocking conditions (a),(d),(e).
    A True response is NOT complete theorem eligibility.
    """
    return (is_squarefree(field_conductor)
            and bsd_proved is True
            and perrin_riou_proved is True)

assert not theorem1_1_can_be_invoked(m_other,None,None)
assert not theorem1_1_can_be_invoked(m_tower,True,True)
assert not theorem1_1_can_be_invoked(m_other,False,True)
assert theorem1_1_can_be_invoked(m_other,True,True)  # still needs (b),(c)
# Corollary 1.2 requires analytic rank ONE and supersingular at every p|11.
assert r!=1 and a11%11!=0

print("PASS: E has rank-four input and good ordinary reduction at 11; rank-one corollary inapplicable")
print("PASS: Q(zeta23)^+ conductor 23 squarefree; cyclotomic Q1 conductor 121 not squarefree")
print("PASS: theorem conditional dependency gate rejects unproved BSD and Perrin–Riou")
print("NONCLAIM: no Mazur–Tate element, BSD proof, or full hypothesis verification")
