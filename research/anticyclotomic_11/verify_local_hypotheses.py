#!/usr/bin/env python3
"""C-0003: exact local arithmetic for Agboola--Castella Hypotheses 6.1.

E: y^2+xy=x^3-x^2-79x+289, K=Q(sqrt(-7)), p=11.
Tate-curve inertia, Dickson subgroup classification, the cited global
rank, and Sha finiteness are MATHEMATICAL inputs, not Python assertions.
"""
from math import isqrt

a1,a2,a3,a4,a6 = 1,-1,0,-79,289
b2=a1*a1+4*a2
b4=2*a4+a1*a3
b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
c4=b2*b2-24*b4
delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
N,q,p=234446,117223,11
assert c4==3801 and delta==468892==4*q and N==2*q
assert all(q%d!=0 for d in range(2,isqrt(q)+1))
assert c4%2 and c4%q
assert delta%3 and delta%11
assert delta%(2**3)!=0 and delta%q==0 and delta%(q*q)!=0

# Fundamental discriminant -7. O_K=Z[u], u^2-u+2=0.
# Two simple roots mod 2 -> 2 splits.
assert [(u*u-u+2)%2 for u in range(2)]==[0,0]
# 117223 splits; explicit square root mod q of -7.
assert q%4==3
root=pow(-7%q,(q+1)//4,q)
assert (root*root+7)%q==0 and root%q!=0
# 11 splits too, with roots 2 and 9.
assert [x for x in range(11) if (x*x+7)%11==0]==[2,9]

# Short model (invertible change of variables away from 2):
# W^2=Z^3-1267Z+17230.
def count_points(k):
    return 1+sum(
        1 for x in range(k) for y in range(k)
        if (y*y-x*x*x+1267*x-17230)%k==0
    )
assert count_points(3)==7
assert count_points(11)==18
a3=3+1-count_points(3)
a11=11+1-count_points(11)
assert a3==-3 and a11==-6
assert a11%p!=0 and a11%p!=1 and count_points(11)%p!=0

# Characteristic polynomial T^2-a3*T+3 has non-square
# discriminant -3 = 8 mod 11, hence is irreducible over F_11.
disc=a3*a3-4*3
assert disc==-3 and disc%p==8
assert 8 not in {x*x%11 for x in range(11)}

print('PASS original minimal-model c4=',c4,'delta=',delta,'N=',N)
print('PASS Heegner split primes: 2,',q,'(root of -7 mod q:',root,')')
print('PASS p=11 split, good ordinary, nonanomalous: #E(F11)=18, a11=-6')
print('PASS F3: a3=-3; Frobenius discriminant -3 nonsquare mod 11')
print('PASS multiplicative bad fibers I2 and I1 (c4 is a unit at each)')
print('NOT AUTOMATED: Tate-curve inertia and irreducible-transvection lemma')
print('NOT ESTABLISHED: finiteness of Sha(E/K)[11^infinity]')
