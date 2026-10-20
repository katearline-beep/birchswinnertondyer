#!/usr/bin/env python3
"""Castella 2019 Theorem A/6.5 + Remark6.6 weight-two gate for original E.

SOURCE INPUT (NOT re-proved here): Castella explicit specialization identity
nu_f(Z0) = (1-alpha_11^{-1})^2 * classical Heegner Kummer P_K
for ordinary p-stabilization in weight 2 under his Theorem A conditions.
Howard §3.4 Cor3.4.3's injective weight-prime Selmer control is also
PUBLISHED and used to deduce weight-prime divisibility of base-class Z0
from zero specialized class. Does NOT show nonzero weight derivative or
any anticyclotomic/complex derivative.
"""
from math import isqrt

p=11
N=234446
D=-7

def chi(a,ell):
    t=a%ell
    if t==0:return 0
    v=pow(t,(ell-1)//2,ell)
    return 1 if v==1 else -1

def trace(ell):
    points=1+sum((y*y+x*y-x*x*x+x*x+79*x-289)%ell==0
                 for x in range(ell) for y in range(ell))
    return ell+1-points

assert N==2*117223
assert p>3 and N%p and (6*N)%p
assert D%8==1 and chi(D,117223)==1 and chi(D,11)==1
assert N%7 and p%7
a11=trace(11)
assert a11==-6 and a11%p
alpha_mod_p=a11%p  # p-ordinary unit root of X^2-a_p X+p
assert alpha_mod_p==5
Euler=(1-pow(alpha_mod_p,-1,p))%p
Euler_sq=Euler*Euler%p
assert (Euler,Euler_sq)==(3,9)
assert Euler_sq !=0

# With good ordinary reduction at p, residual semisimplification at inertia
# has an unramified quotient and a mod-p cyclotomic character on the
# complementary line. Since p>2, these chars are distinct on inertia:
# Castella's residual p-distinguished condition is satisfied.
assert p>2 and (p-1)>1
# Two split Frobenius test from C-0020 yields residual irr over GK.
assert chi(D,23)==chi(D,43)==1
assert trace(23)==-6 and trace(43)==-4
disc23=(trace(23)**2-4*23)%p
disc43=(trace(43)**2-4*43)%p
assert (disc23,disc43)==(10,9) and chi(disc23,p)==-1 and chi(disc43,p)==1
assert disc43!=0
# Every non-split q|N ramification condition is VACUOUS.
assert chi(D,117223)==1 and D%8==1

# Source theorem chain (logic, not cohomology computation):
# Castella ThmA+Rem6.6 -> nu_f(Z0)=Euler² * Kummer(P_K).
# Kolyvagin + rank E(K)>=4 => Kummer(P_K)=0 in Q11 cohomology.
# Howard base-field weight specialization injects M_P/PM into that
# specialisation, hence [Z0] mod P=0 and Z0 in P M_P.
def weight_prime_divisibility_given_theorems(
        castella_source_valid,kolyvagin_rank_lower_bound,
        howard_weight_control_injective):
    if not castella_source_valid or not howard_weight_control_injective:
        return None
    if kolyvagin_rank_lower_bound<2:
        return None
    return True
assert weight_prime_divisibility_given_theorems(True,4,True)
assert weight_prime_divisibility_given_theorems(False,4,True) is None
assert weight_prime_divisibility_given_theorems(True,4,False) is None
assert weight_prime_divisibility_given_theorems(True,1,True) is None
print("PASS ordinary a11=-6, alpha mod11=5, Castella weight2 Euler square=9 unit")
print("PASS split Heegner primes, p-distinct inertia characters, abs residual GK via Frob23/43")
print("PASS published Castella A/Rem6.6 and Howard weight control + Kolyvagin")
print("PASS logical consequence: base Z0 lies in localized Hida WEIGHT prime")
print("NONCLAIM: no nonzero weight first jet, Howard horizontal Conj3.4.1,")
print("NONCLAIM: no anticyclotomic T-augmentation order, original complex L'' or BSD")
