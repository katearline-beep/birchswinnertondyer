#!/usr/bin/env python3
"""Second exact-rational enclosure for L'(E^(-7),1).

Independent computational organization: evaluate rational bounds for each
E1(c*n) in Fraction arithmetic, round the FULL term outward only when
adding to a fixed-point accumulator. No imported prior certificate.

The implication for L'(1) ASSUMES the documented Mellin/functional-equation
identity, correct curve Fourier coefficients and standard coefficient bound.
Those are external mathematical proof obligations, not proven by Python.
"""
from fractions import Fraction as F
from math import factorial, isqrt

N=234446
Q=49*N
M=6000
S=10**8
# Taylor at x<=12 uses 55 signed terms; after term 55, terms decrease.
assert 12**56 < 56*factorial(56)*10**12
c0=F(1853789485821,10**15)
c1=F(1853789485822,10**15)

def fl(x): return x.numerator//x.denominator
def ce(x): return -fl(-x)

def atan_int(z,k=24):
    total=sum(((-1)**j*z**(2*j+1)/F(2*j+1)
               for j in range(k)),F(0))
    r=z**(2*k+1)/(2*k+1)
    return total-r,total+r

A,B=atan_int(F(1,5))
C,D=atan_int(F(1,239))
pi0,pi1=16*A-4*D,16*B-4*C
assert Q*c0*c0<4*pi0*pi0
assert 4*pi1*pi1<Q*c1*c1

def log_1_to_2(v,terms=24):
    assert 1<=v<=2
    z=(v-1)/(v+1)
    total=sum((2*z**(2*j+1)/(2*j+1)
               for j in range(terms)),F(0))
    rem=2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
    return total,total+rem

ln2lo,ln2hi=log_1_to_2(F(2))
H=sum((F(1,j) for j in range(1,129)),F(0))
center=H-F(1,256)+F(1,12*128*128)
gamma_lo=center-7*ln2hi-F(1,120*128**4)
gamma_hi=center-7*ln2lo

def log_any_positive(x):
    v=x; power=0
    while v<1: v*=2; power-=1
    while v>=2: v/=2; power+=1
    lo,hi=log_1_to_2(v)
    if power>0:
        return lo+power*ln2lo,hi+power*ln2hi
    return lo+power*ln2hi,hi+power*ln2lo

def e1_interval(x):
    assert 0<x<=12
    ll,lh=log_any_positive(x)
    polynomial=F(0)
    xp=F(1)
    for k in range(1,56):
        xp*=x
        polynomial+=(-1)**(k+1)*xp/(k*factorial(k))
    omitted=xp*x/(56*factorial(56))
    return -gamma_hi-lh+polynomial-omitted, -gamma_lo-ll+polynomial+omitted

def prime_coefficient(p):
    if p==2:
        count=sum((y*y+x*y-x**3+x*x+79*x-289)%2==0
                  for x in range(2) for y in range(2))
        return 2-count
    total=0
    for x in range(p):
        delta=(x*x+4*(x*x*x-x*x-79*x+289))%p
        total+=0 if not delta else (
            1 if pow(delta,(p-1)//2,p)==1 else -1)
    return -total

def coefficients():
    spf=list(range(M+1))
    for p in range(2,isqrt(M)+1):
        if spf[p]==p:
            for n in range(p*p,M+1,p):
                if spf[n]==n: spf[n]=p
    a=[0]*(M+1); a[1]=1; local={}
    for p in range(2,M+1):
        if spf[p]!=p: continue
        v=prime_coefficient(p)
        power=p
        seq=[1,v]
        while power*p<=M:
            seq.append(v*seq[-1] - (0 if N%p==0 else p)*seq[-2])
            power*=p
        local[p]=seq
    for n in range(2,M+1):
        p=spf[n]; k=0; t=n
        while t%p==0: k+=1; t//=p
        a[n]=a[t]*local[p][k]
    return a

a=coefficients()
assert a[1:12]==[1,-1,-3,1,-4,3,-5,-1,6,4,-6]

lo=hi=0
for n in range(1,M+1):
    residue=n%7
    chi=0 if residue==0 else (1 if residue in (1,2,4) else -1)
    if not chi: continue
    L,U=e1_interval(c0*n)
    # E1'(x)=-exp(-x)/x: total change as c varies <= (c1-c0)/c0.
    L-=(c1-c0)/c0
    assert 0<L<=U
    factor=F(2*a[n]*chi,n)
    low,high=(factor*L,factor*U) if factor>0 else (factor*U,factor*L)
    lo+=fl(low*S)
    hi+=ce(high*S)

q=1/(1+c0)
tail=4*q**(M+1)/(c0*(M+1)*(1-q))
lower=F(lo,S)-tail
upper=F(hi,S)+tail
assert 0<lower<upper
assert F(34)<lower<F(35)
assert F(34)<upper<F(35)

print('FINITE EXACT INTERVAL',float(F(lo,S)),float(F(hi,S)))
print('RATIONAL TAIL UPPER',float(tail))
print('CONDITIONAL LPRIME INTERVAL',float(lower),float(upper))
print('PASS: independent exact term enclosures imply positivity given stated analytic identity')
