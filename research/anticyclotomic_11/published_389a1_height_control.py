#!/usr/bin/env python3
"""First-digit regression against BCLMN Shadow Lines (2016), Sec. 5.1.

E: y^2+y=x^3+x^2-2x, K=Q(sqrt(-11)), p=5.
Independent exact AFFINE elliptic additions; published square-root
denominator generator d_h([9]A) is an oracle, not our own divisor recurrence.
a1=0 => sigma_p(t)=t+O(t^3); t is 5-adically of valuation one.
Paper reports h_rho(P1+S)=3+O(5); this reproduces the first digit only.
"""
from fractions import Fraction as F
from math import lcm

class K:
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,v):
        if not isinstance(v,K):v=K(v)
        return K(self.a+v.a,self.b+v.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self,v):return self+-v
    def __mul__(self,v):
        if not isinstance(v,K):v=K(v)
        return K(self.a*v.a-11*self.b*v.b,self.a*v.b+self.b*v.a)
    __rmul__=__mul__
    def __truediv__(self,v):
        if not isinstance(v,K):v=K(v)
        d=v.a*v.a+11*v.b*v.b
        return self*K(v.a/d,-v.b/d)
    def __eq__(self,v):
        if not isinstance(v,K):v=K(v)
        return self.a==v.a and self.b==v.b

def oncurve(P):
    x,y=P
    return y*y+y==x*x*x+x*x-2*x

def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P;u,v=Q
    if x==u:
        if y+v+1==K(0):return None
        m=(3*x*x+2*x-2)/(2*y+1)
    else:m=(v-y)/(u-x)
    nu=y-m*x
    z=m*m-1-x-u
    w=-m*z-nu-1
    assert oncurve((z,w))
    return z,w

P=(K(-1),K(1))
S=(K(F(1,4)),K(F(-1,2),F(1,8)))
A=(K(F(27,25),F(-6,25)),K(F(29,125),F(-62,125)))
assert oncurve(P) and oncurve(S) and oncurve(A) and add(P,S)==A
T=None
for _ in range(9):T=add(T,A)
t=-T[0]/T[1]
# BCLMN printed d_h([9]A), their equations on pp. 12-13:
D=K(-147355399895912034115896942557395263175125,
    24227041862247516754088925710922259344570)
p=5;prec=50;mod=p**prec
r=2
for k in range(1,prec):
    lifts=[r+j*p**k for j in range(p)
           if ((r+j*p**k)**2+11)%p**(k+1)==0]
    assert len(lifts)==1
    r=lifts[0]

def vp(x):
    if x==0:return prec
    k=0
    while x%p==0:k+=1;x//=p
    return k

def unit(z,root):
    d=lcm(z.a.denominator,z.b.denominator)
    n=int(z.a*d)+int(z.b*d)*root
    vn,vd=vp(n),vp(d)
    assert 0<=vn-vd<prec-5
    return vn-vd,(n//p**vn)*pow(d//p**vd,-1,p*p)%(p*p)

u=[]
for root in (r,-r%mod):
    vt,ut=unit(t,root)
    vd,ud=unit(D,root)
    assert vt==vd==1,(vt,vd)
    u.append(ut*pow(ud,-1,p*p)%(p*p))
q=u[0]*pow(u[1],-1,p*p)%(p*p)
h9=((pow(q,p-1,p*p)-1)//p)*pow(p-1,-1,p)%p
h=h9*pow(9*9,-1,p)%p
assert q==9 and h9==h==3,(q,h9,h)
assert -h%p!=3  # deliberately reversed orientation fails
print('PASS published BCLMN 389a1 h(P1+S)=3 mod5; exact affine and p-adic control')
print('PASS printed d_h([9]A) and deliberate wrong-orientation negative control')
print('NONCLAIM: published first-digit test not independent Sage/Magma sigma implementation')
