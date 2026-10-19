#!/usr/bin/env python3
"""Derive the canonical sigma-series coefficient u=E2/12 modulo p.

Exact stdlib Fraction series from Mazur--Stein--Tate formal-group equations.
sigma_u(z) = sigma_0(z) * exp(u*z^2/2). NOT PARI s2=b2/12-u. The first coefficient with
denominator p forces c_p mod p. Published E37/p5 result is an oracle.
AI-authored symbolic implementation, not a peer-reviewed theorem or BSD proof.
"""
from fractions import Fraction as F
from math import factorial

def add(x,y,n):
    return [(x[k] if k<len(x) else F(0))+(y[k] if k<len(y) else F(0)) for k in range(n)]

def mul(x,y,n):
    a=[F(0)]*n
    for i,v in enumerate(x[:n]):
        if v:
            for j,w in enumerate(y[:n-i]):
                if w:a[i+j]+=v*w
    return a

def inversion(x,n):
    assert x[0]
    a=[F(0)]*n;a[0]=1/x[0]
    for k in range(1,n):
        a[k]=-sum(x[j]*a[k-j] for j in range(1,min(k,len(x)-1)+1))/x[0]
    return a

def translate(x,n,p=1):
    return [F(0)]*p+list(x[:n-p])

def exp(x,n):
    a=[F(0)]*n;a[0]=1
    for k in range(1,n):
        a[k]=sum(j*x[j]*a[k-j] for j in range(1,min(k,len(x)-1)+1))/k
    return a

def sigma_c_polynomial(a1,a2,a3,a4,a6,degree):
    # Formal w=-1/y, t=-x/y for y^2+a1*x*y+a3*y=x^3+a2*x^2+a4*x+a6.
    n=degree+6
    w=[F(0)]*n;w[3]=1
    for j in range(n):
        nxt=translate([F(1)],n,3)
        nxt=add(nxt,[a1*z for z in translate(w,n,1)],n)
        nxt=add(nxt,[a2*z for z in translate(w,n,2)],n)
        nxt=add(nxt,[a3*z for z in mul(w,w,n)],n)
        nxt=add(nxt,[a4*z for z in translate(mul(w,w,n),n,1)],n)
        nxt=add(nxt,[a6*z for z in mul(mul(w,w,n),w,n)],n)
        if nxt==w:break
        w=nxt
    else:raise AssertionError('w(t) did not stabilize')
    # dz/dt=(w-t*w')/[w*(-2+a1*t+a3*w)] for invariant differential.
    v=[F(0)]*n;v[0]=-2;v[1]=a1
    v=add(v,[a3*z for z in w],n)
    den=mul(w,v,n)[3:]
    num=[(1-j)*w[j] for j in range(3,n)]
    n0=degree+2
    der=mul(num,inversion(den,n0),n0)
    z=[F(0)]*n0
    for j in range(n0-1):z[j+1]=der[j]/(j+1)
    b2=a1*a1+4*a2;b4=2*a4+a1*a3;b6=a3*a3+4*a6
    c4=b2*b2-24*b4;c6=-b2*b2*b2+36*b2*b4-216*b6
    g2=F(c4,12);g3=F(c6,216)
    # wp(z)=z^-2+sum wp[k]*z^(2k); wp''=6wp^2-g2/2.
    wp={1:g2/20,2:g3/28}
    for k in range(3,degree//2+1):
        wp[k]=6*sum(wp[i]*wp[k-1-i] for i in range(1,k-1))/(2*k*(2*k-1)-12)
    # Here c is series u=E2/12. PARI ellpadics2 returns s2=b2/12-u.
    # d^2/dz^2 log(sigma_u(z)/z)=1/z^2-wp(z)+u.
    f0=[F(0)]*n0
    for k,val in wp.items():
        power=2*k+2
        if power<n0:f0[power]=-val/F((2*k+1)*(2*k+2))
    sigma_z0=translate(exp(f0,n0),n0)
    base=[F(0)]*n0;zpow=[F(0)]*n0;zpow[0]=1
    for coeff in sigma_z0:
        if coeff:base=add(base,[coeff*x for x in zpow],n0)
        zpow=mul(zpow,z,n0)
    # Recover coefficients of powers of c by exp(c*z(t)^2/2).
    poly=[];z2=mul(z,z,n0);zk=[F(0)]*n0;zk[0]=1
    for k in range(degree//2+1):
        poly.append(mul(base,zk,n0)[degree]/F((2**k)*factorial(k)))
        zk=mul(zk,z2,n0)
    return poly

def primitive_integral_c(poly,p):
    roots=[]
    for c in range(p):
        value=sum(a*c**j for j,a in enumerate(poly))
        if value.denominator%p:roots.append(c)
    assert len(roots)==1,(p,roots)
    return roots[0]

control=sigma_c_polynomial(0,0,1,-1,0,7)
assert control[:4]==[F(103,120),F(-73,120),F(0),F(1,48)]
assert primitive_integral_c(control,5)==1
print('PASS published MST E37/p5 sigma t^7 and c_5=1 mod5 control')

poly=sigma_c_polynomial(1,-1,0,-79,289,13)
D=81749606400
numer=[-106502304179884375,2098715391767160,414591819943752,
       -3609872323200,-61449474240,292723200,1774080]
assert poly==[F(x,D) for x in numer],(poly,numer)
assert D%11==0 and (D//11)%11!=0
c11=primitive_integral_c(poly,11)
assert c11==4
assert (12*c11)%11==4
assert ((-3*pow(12,-1,11)-c11)%11)==4
print('PASS exact sigma t^13 polynomial and unique canonical c_11=4 mod11')
print('PASS E2=12*u=4 mod11; PARI s2=b2/12-u=4 mod11')
print('NONCLAIM: canonical sigma theorem and BCLMN height normalization remain dependencies')
