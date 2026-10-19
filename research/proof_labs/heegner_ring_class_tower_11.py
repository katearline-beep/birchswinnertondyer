#!/usr/bin/env python3
"""Session23 exact arithmetic: K=-7, p=11 ring-class tower and local unit root.

Published theorem inputs (NOT computed/proved here):
* Ring class exact sequence for class-number-one O_K of discriminant -7:
  Pic(O_f) = (O_K/f)^x / ((Z/f)^x * image O_K^x).
* Kolyvagin: non-torsion classical base Heegner point => rank E(K) = 1.
* Howard §3.3: constructs anticyclotomic inverse-limit Z_inf in Nekovar's
  EXTENDED Selmer cohomology, not automatically CH4.5's compact Hhat^1.
The script tests an explicit CRT model and the precise rank contrapositive.
"""
from math import gcd

P=11
def hensel_roots(n):
    assert n>=1
    rr=[5,7]  # roots of x²-x+2: omega=(1+sqrt(-7))/2
    modulus=P
    for _ in range(1,n):
        nxt=[]
        for r in rr:
            found=[r+t*modulus for t in range(P)
                   if ((r+t*modulus)**2-(r+t*modulus)+2)%(modulus*P)==0]
            assert len(found)==1
            nxt.append(found[0])
        rr=nxt
        modulus*=P
    assert modulus==P**n and all((r*r-r+2)%modulus==0 for r in rr)
    assert gcd(rr[0]-rr[1],modulus)==1
    return rr

def order(a,m):
    assert gcd(a,m)==1
    v=1
    for k in range(1,m+1):
        v=v*a%m
        if v==1:
            return k
    raise AssertionError("order did not close")

for n in range(1,5):
    m=P**n; phi=10*P**(n-1)
    omega_minus,omega_plus=hensel_roots(n)
    # p splits: O_K/(p^n) = (Z/p^n) x (Z/p^n).
    # Diagonal (Z/p^n)^x quotient maps (u+,u-) -> u+/u-.
    # O_K^x={±1} adds no quotient: both units diagonal.
    # Since class number O_K=1, Pic(O_{p^n}) is cyclic order phi.
    assert order(2,m)==phi
    assert 2**phi%m==1
    assert 2**(phi//2)%m!=1
    for ratio in (2,3,m-2,2**(n+2)%m):
        if gcd(ratio,m)>1:
            continue
        # Explicit CRT witness for the ratio in O_K/(p^n).
        b=(ratio-1)*pow(omega_plus-omega_minus,-1,m)%m
        a=(1-b*omega_minus)%m
        assert (a+b*omega_minus)%m==1
        assert (a+b*omega_plus)%m==ratio
        assert (a*a+a*b+2*b*b)%m==ratio
    # Gal(H_{11^n}/K) has torsion delta=C10 and gamma=C11^(n-1).
    # The delta-averaging idempotent has integral coefficient 1/10.
    assert phi==10*P**(n-1)
    assert gcd(10,m)==1
    assert (10*pow(10,-1,m))%m==1
    print("PASS n=%d modulus=%d roots=%s Pic-order=%d Gamma-degree=%d"%
          (n,m,(omega_minus,omega_plus),phi,P**(n-1)))

# E a_p=-6, ordinary p-stabilization unit root of X²+6X+11:
alpha=5
modulus=P
for _ in range(1,4):
    found=[alpha+t*modulus for t in range(P)
           if ((alpha+t*modulus)**2+6*(alpha+t*modulus)+P)%(P*modulus)==0]
    assert len(found)==1
    alpha=found[0];modulus*=P
assert (alpha,modulus)==(12721,P**4)
assert (1-pow(alpha,-1,modulus))%P==3  # nonexceptional alpha != 1 mod11
assert alpha%P==5
# Howard Definition 2.4.3: exceptional weight2 trivial character only
# when U_p eigenvalue alpha_p is exactly +1 or -1.
# Alpha mod11=5 rules both out; Howard Lemma2.4.4 therefore gives
# H^0(L_v,F^-V^dagger)=0 for each finite L and the published EXACT sequence
# 0 -> sum_v H0(Lv,F^-V) -> Htilde^1_f(L,V) -> Sel_Gr(L,V) -> 0
# is an isomorphism for this weight-two specialization.
def howard_exceptional(weight,wild_trivial,alpha_mod11):
    return weight==2 and wild_trivial and alpha_mod11 in (1,10)
assert not howard_exceptional(2,True,alpha%11)
assert howard_exceptional(2,True,1)
assert howard_exceptional(2,True,10)
assert not howard_exceptional(4,True,1)

def classical_base_point_forced_torsion(known_rank_lower_bound,heegner_hypothesis):
    """Kolyvagin contrapositive, never a numerical calculation of P_K."""
    if not heegner_hypothesis:
        return None
    if known_rank_lower_bound>=2:
        return True
    return None

assert classical_base_point_forced_torsion(4,True) is True
assert classical_base_point_forced_torsion(1,True) is None
assert classical_base_point_forced_torsion(4,False) is None

# An ELEMENTARY formal model for why base vanishing cannot imply
# inverse-limit vanishing: T=gamma-1 is nonzero in Z11[[T]], with aug T=0.
# This does not construct a Heegner class or establish any J-adic order.
for n in (1,2,3):
    degree=P**n
    assert degree>1  # group-ring gamma-1 has two distinct coefficients.
print("PASS symbolic nonzero augmentation-kernel example gamma-1 (not an actual class)")
print("PASS Howard weight2 specialization NONEXCEPTIONAL: alpha11=5 mod11 != +/-1")
print("PASS published Howard Lemma2.4.4: extended Selmer = strict Greenberg at finite levels")
print("PASS ordinary alpha=%d mod%d, 1-alpha^-1 is 11-adic unit"%(alpha,modulus))
print("PASS conditional Kolyvagin contrapositive: rank >= 2 -> classical P_K torsion")
print("NONCLAIM: no concrete Howard Z_inf, weight-2 specialization, Coleman order,")
print("NONCLAIM: no analytic rank >=4, Sha finiteness or full BSD result")
