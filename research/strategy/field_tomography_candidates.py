#!/usr/bin/env python3
"""Exact candidate discriminants for quadratic-field tomography.

No analytic twist rank, Heegner height, derived Kato class or BSD claim.
Negative fundamental discriminants D with N primes 2,117223 and p=11
all split; record small reproducible test cohort.
"""
from math import gcd,isqrt

N=234446
q=117223
p=11

def is_squarefree(n):
    n=abs(n)
    return all(n%(k*k) for k in range(2,isqrt(n)+1))

def is_fundamental_negative(D):
    if D>=0: return False
    if D%4==1: return is_squarefree(D)
    return D%4==0 and (D//4)%4 in (2,3) and is_squarefree(D//4)

def split_odd(D,r):
    assert r%2==1
    assert gcd(D,r)==1
    assert pow(D%r,(r-1)//2,r) in (1,r-1)
    return pow(D%r,(r-1)//2,r)==1

def eligible(D):
    return (is_fundamental_negative(D) and gcd(D,N*p)==1
            and D%8==1 and split_odd(D,q) and split_odd(D,p))

values=[D for D in range(-3,-1000,-1) if eligible(D)]
assert values[:4]==[-7,-87,-95,-127],values[:4]
assert not eligible(-3)  # 2 is inert in Q(sqrt(-3)).
assert not eligible(-11) # 11 ramifies.
assert all((abs(D)*abs(D)*N)%11!=0 for D in values)
for D in values[:8]:
    # At good coprime twist, root twist(E^D)=chi_D(-N)*root(E).
    # The imaginary quadratic character has chi_D(-1)=-1.
    # The condition that BOTH primes dividing N split gives chi_D(N)=1;
    # thus predicted twist root number is -1 (given root(E)=+1).
    assert D%8==1 and split_odd(D,q)
    print(f"ELIGIBLE D={D} twist_conductor={D*D*N} predicted_twist_sign=-1")
print("PASS: small fundamental D with Heegner and split-11 local conditions")
print("NONCLAIM: no derivative nonvanishing has been tested for new fields")
