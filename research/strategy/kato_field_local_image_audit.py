#!/usr/bin/env python3
"""Exact checks for BKS local hypotheses at F=Q(zeta_23)^+, p=11.

Standard Tate-curve inertia, Neron-model, formal-group, and elementary
generation theorems are MATHEMATICAL inputs, not proved by this script.
Sha(E/F)[11^infinity] remains unknown; no Kato/BSD theorem is claimed.
"""
from collections import deque
from math import isqrt
a1,a2,a3,a4,a6=1,-1,0,-79,289
N,q,p,ram=234446,117223,11,23
assert N==2*q
def is_prime(n):
    return n>1 and all(n%d for d in range(2,isqrt(n)+1))
assert all(is_prime(x) for x in (3,11,23,q))
b2=a1*a1+4*a2
b4=2*a4+a1*a3
b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
c4=b2*b2-24*b4
c6=-b2**3+36*b2*b4-216*b6
delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
assert (b2,b4,b6,c4,c6,delta)==(-3,-158,1156,3801,-232605,4*q)
assert delta%q==0 and (delta//q)%q!=0 and c4%q!=0
assert delta%4==0 and delta%8!=0 and c4%2!=0
assert pow((-c6)%q,(q-1)//2,q)==1  # split multiplicative I1

def count_projective(q0):
    """Count 1 point at infinity plus finite solutions on an integral model.

    For bad q0=2 this includes a singular point: do NOT use as #E(F2).
    """
    return 1+sum(
        (y*y+a1*x*y+a3*y-(x**3+a2*x*x+a4*x+a6))%q0==0
        for x in range(q0) for y in range(q0))

assert {l:count_projective(l) for l in (2,3,11,23,199)}=={
    2:4, 3:7, 11:18, 23:30, 199:220}
# Bad 2 has an affine node. a2=2-(#finite affine solutions)=-1.
assert 2-(count_projective(2)-1)==-1
# For nonsplit I2 at 2: component order 2, torus F2 nonsplit of size 3.
# For split I1 at 117223: component order 1, torus Fq* of size q-1.
assert all(n%p for n in (2,2+1,1,q-1))
# Real cyclotomic 23-subfield: degree 11; 23 totally ramified,
# residue field unchanged, good reduction E(F23) of size 30.
assert (ram-1)//2==11 and ram not in (2,11,q)
assert count_projective(23)%p!=0
# Other S primes are unramified in F, residue degrees divide 11:
# f is 1 or 11. Multiplicative split type at q persists; at 2
# nonsplit type persists since f is odd.
a11=11+1-count_projective(11)
assert a11==-6
for f in (1,11):
    assert (pow(2,f,p)+1)%p!=0
    assert (pow(q,f,p)-1)%p!=0
    # For good ordinary reduction at 11, Frobenius trace S_f modulo 11
    # is a11^f modulo 11, since alpha*beta=11=0 mod 11.
    assert (1-pow(a11,f,p))%p!=0
# For p=11, unramified local formal-group torsion-freeness is
# AN ADDITIONAL mathematical theorem beyond finite point counts.

a3_frob=3+1-count_projective(3)
assert a3_frob==-3
assert (a3_frob*a3_frob-4*3)%p==8
assert 8 not in {x*x%p for x in range(p)}
# Split I1 at q has Tate parameter of valuation 1, hence the
# 11-adic inertia image is a FULL unipotent root group (Tate theorem).
# Irreducible Frobenius at 3 moves its fixed line; conjugate root
# groups generate SL2(Z11) by elementary matrices over a local ring.
# Verify only a finite-field model: SL2(F11) has order 1320.
def mul(a,b):
    return ((a[0]*b[0]+a[1]*b[2])%p,(a[0]*b[1]+a[1]*b[3])%p,
            (a[2]*b[0]+a[3]*b[2])%p,(a[2]*b[1]+a[3]*b[3])%p)
identity=(1,0,0,1)
seen={identity}
queue=deque([identity])
forbidden=(1,1,0,1)
while queue:
    m=queue.popleft()
    for g in ((1,1,0,1),(1,0,1,1)):
        z=mul(m,g)
        if z not in seen: seen.add(z);queue.append(z)
assert len(seen)==p*(p*p-1)==1320
assert all((z[0]*z[3]-z[1]*z[2])%p==1 for z in seen)
# Negative control: good prime 199 would violate local 11-torsion
# if it were in the chosen S-set. It is NOT in S for F_23.
assert count_projective(199)%p==0
print("PASS exact E invariants, bad fibers, trace at 3, S-local point counts")
print("PASS F=Q(zeta23)^+: no 11-torsion in residue/group components")
print("PASS full SL2(F11) finite root subgroup generation, order 1320")
print("PASS negative control: good 199 has 11-divisible reduction order")
print("ASSUMED: Tate-curve inertia, formal-log torsion, Neron structure, SL2(Z11) generation")
print("UNPROVED: Sha(E/F)[11^infinity] finite; no BKS theorem is unconditional")
