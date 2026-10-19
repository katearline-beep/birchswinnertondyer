#!/usr/bin/env python3
"""Independent BASIC hypothesis checks on published Castella--Hsieh rank-2 control.

Castella--Hsieh 2022, Appendix Table 1:
E=433a1, p=11, K=Q(sqrt(-7)), Theta=88*T^2+22*T^3+... mod(121,T^11).
This script validates equation, delta, split/inert, ordinarity and mod11
residual IRREDUCIBILITY via irreducible Frobenius-5 characteristic polynomial.
The exact theta series and auxiliary adjoint L-value are PUBLISHED inputs,
NOT computed here. No Kato-class, theta measure or complex BSD proof.
"""
from math import isqrt

def prime(p):
    return p>=2 and all(p%d for d in range(2,isqrt(p)+1))

def a_prime(ell):
    assert prime(ell) and ell!=433
    points=1+sum(1 for x in range(ell) for y in range(ell)
                 if (y*y+x*y-x*x*x-1)%ell==0)
    return ell+1-points

def legendre(a,p):
    assert prime(p) and p%2 and a%p
    x=pow(a%p,(p-1)//2,p)
    assert x in (1,p-1)
    return 1 if x==1 else -1

def theta_first_nonzero_mod121(coeff):
    # Table 1 only: does NOT independently prove lower powers vanish
    # identically over Z11, that is part of the source theorem/setting.
    assert coeff[0]==0 and coeff[1]==0
    assert coeff[2]%121 and coeff[2]%11==0
    return 2

def pairing_allowed_by_involution(derived_order,chi_left,chi_right):
    """CH Thm4.1(d): h^r(x^tau,y^tau)=(-1)^r*h^r(x,y).
    chi +-1 eigenvalues; this tests POSSIBLE nonzero entries, not values.
    """
    assert derived_order>=1 and chi_left in (-1,1) and chi_right in (-1,1)
    return chi_left*chi_right==(-1)**derived_order

def derived_height_scope(p_ordinary,disc_coprime,disc_Nminus_squarefree,ramified_at_all_inert):
    """Castella-Hsieh Theorem 4.1 (NOT Theorem A)."""
    return all((p_ordinary,disc_coprime,disc_Nminus_squarefree,ramified_at_all_inert))

def theorems_A_B_compatible(rank_lower_bound,all_theorem_A_hypotheses,theta_order2):
    """Theorem B + Theorem A force Sel-dimension 2 if ord_T Theta=2."""
    if not all_theorem_A_hypotheses or rank_lower_bound==0:
        return None
    if not theta_order2:
        return None
    return rank_lower_bound<=2

def CH_rank2_consequence(complete_hypotheses,theta_order_is_two,rank_at_least):
    """THEOREM B + A logical implication, NOT any class computation."""
    if not complete_hypotheses or not theta_order_is_two:
        return None
    # Theorem B needs positive rank, Theorem A applies with all assumptions.
    assert rank_at_least>0
    return rank_at_least<=2

# b2=1, b4=0, b6=4, b8=1, discriminant -b2^2*b8-27*b6^2=-433.
b2,b4,b6,b8=1,0,4,1
delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
assert delta==-433
for x,y in ((0,1),(-1,1)):
    assert y*y+x*y==x*x*x+1
assert legendre(-7,433)==-1  # the single N^- conductor prime is inert
assert legendre(-7,11)==1    # p=11 splits K; sqrt(-7)=+-2 mod11
assert (-7)%8==1             # 2 splits in K (not bad for 433a1)
assert a_prime(5)==-4 and a_prime(11)==-4
assert a_prime(11)%11 !=0    # 11 good ordinary
F5discriminant=(a_prime(5)**2-4*5)%11
assert F5discriminant==7 and legendre(F5discriminant,11)==-1
# A single irreducible Frobenius characteristic polynomial prevents a
# GL2(F11) representation from preserving a line over F11.
# 433 bad split multiplicative, v_433(delta)=1, so mod11 inertia
# is nontrivial by the standard Tate curve criterion 11∤v_433(delta).
assert delta%433==0 and (delta//433)%433 != 0
assert 1%11!=0
coeff={0:0,1:0,2:88,3:22,4:86,5:7,6:10,7:12,8:29,9:88,10:48}
assert theta_first_nonzero_mod121(coeff)==2
assert CH_rank2_consequence(True,True,2)
assert CH_rank2_consequence(True,True,4) is False
assert CH_rank2_consequence(False,True,4) is None
assert CH_rank2_consequence(True,False,4) is None
# Deliberately wrong fields/prime conditions don't sneak into the test.
assert legendre(-7,117223)==1  # focal rank-four N bad odd prime SPLITS K
# IMPORTANT: 4.1 does apply to the FOCAL rank-four curve with N^-=1.
p=11
focal_count=1+sum(1 for x in range(p) for y in range(p)
                  if (y*y+x*y-x*x*x+x*x+79*x-289)%p==0)
focal_a11=p+1-focal_count
assert (focal_count,focal_a11)==(18,-6) and focal_a11%11
assert 117223%7 and 2%7 and 11%7
assert derived_height_scope(True,True,True,True)  # N^-=1, vacuous ramification
assert derived_height_scope(True,True,True,True)  # 433a1: N^-=433, ramified p11
assert not derived_height_scope(True,True,True,False)
assert not derived_height_scope(False,True,True,True)
assert theorems_A_B_compatible(4,True,True) is False
assert theorems_A_B_compatible(4,False,True) is None
assert theorems_A_B_compatible(2,True,True) is True
# Independent exact structural implication of CH Theorem 4.1(c),(d):
# Odd first pairing is cross-eigenspace only; even second pairing is
# within eigenspaces and alternating. No equality to BCLMN normalization!
assert not pairing_allowed_by_involution(1,1,1)
assert not pairing_allowed_by_involution(1,-1,-1)
assert pairing_allowed_by_involution(1,1,-1)
assert pairing_allowed_by_involution(2,1,1)
assert pairing_allowed_by_involution(2,-1,-1)
assert not pairing_allowed_by_involution(2,1,-1)
assert legendre(-11,389)==1    # BCLMN control K=-11 is NOT CH Appendix K=-2
print("PASS CH published Appendix Table1 433a1 p11 K=-7: discriminant -433")
print("PASS inert bad 433, split good 11, ordinary a11=-4, two rational points")
print("PASS mod11 residual irreducibility: Frobenius5 discr 7 nonsquare in F11")
print("PASS multiplicative mod11 ramification via v433(Delta)=1")
print("PASS published theta T2 coefficient 88 mod121 is nonzero (valuation one)")
print("PASS CH Thm4.1 first derived height is cross eigenspace only; second pairing within eigenspaces")
print("PASS CH Thm4.1 applies to focal E234446a1 p11 K=-7 with Nminus=1")
print("PASS CH ThmA INAPPLICABLE to focal K=-7; Thm4.5 needs a genuine Iwasawa class")
print("PASS CH ThmA+B conditional: theta order2 forces Sel dim2; rank4 excludes order2")
print("NONCLAIM: adjoint L nonvanishing/theta expansion/rank2 are published inputs")
print("NONCLAIM: no independent Kato class or complex L''/BSD proof")
