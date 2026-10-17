#!/usr/bin/env python3
"""Exact local data used in the published quadratic-twist root-sign identity.

Nonalgorithmic dependencies: standard local root numbers for multiplicative
reduction and the quadratic-twist root-number identity for gcd(D,N)=1.
"""
from math import isqrt
p,q,N,D=2,117223,234446,-7
assert p*q==N and N%7!=0
a1,a2,a3,a4,a6=1,-1,0,-79,289
b2=a1*a1+4*a2
b4=a1*a3+2*a4
b6=a3*a3+4*a6
b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
c4=b2*b2-24*b4
c6=-b2**3+36*b2*b4-216*b6
delta=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
assert (b2,b4,b6,c4,c6,delta)==(-3,-158,1156,3801,-232605,468892)
assert delta==4*q and c4%2==1 and c4%q!=0
assert all(q%k!=0 for k in range(2,isqrt(q)+1))
# At p=2: a_2=-1 for original minimal model (nonsplit multiplicative).
affine=sum((y*y+x*y-x**3+x*x+79*x-289)%2==0
           for x in range(2) for y in range(2))
ap2=2-affine
assert ap2==-1
# At q odd >=5: splitting of multiplicative fiber decided by -c6 square.
assert pow((-c6)%q,(q-1)//2,q)==1
apq=1
# Local root at multiplicative prime is -ap.
# Local archimedean sign is -1 for an elliptic curve over Q.
wE=(-1)*(-ap2)*(-apq)
assert wE==1
# Quadratic chi_{-7} mod 7: squares are {1,2,4}; -N = -2*q ≡ 5 mod 7.
chi=lambda v: 0 if v%7==0 else (1 if v%7 in (1,2,4) else -1)
assert (chi(2),chi(q),chi(-N))==(1,1,-1)
# For fundamental D=-7 coprime to N, twist sign w(E^D)=chi_D(-N)*w(E).
w_twist=chi(-N)*wE
assert w_twist==-1
assert 49*N==11487854
print("PASS: minimal invariants, reduction types and local sign inputs")
print("PASS: w(E)=+1, chi_-7(-N)=-1, hence w(E^-7)=-1")
print("PASS: N_twist=49*N under the standard coprime twist-conductor theorem")
print("NONCLAIM: twist root/conductor theorems are referenced, not proved by Python")
