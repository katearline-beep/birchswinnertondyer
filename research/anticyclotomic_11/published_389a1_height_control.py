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


# Second published result, now with its denominator computed (not supplied
# by the paper). A2=P2+S is integral on the minimal equation, so d(A2)=1;
# the integral division polynomial psi_9(A2) must be primitive.
from functools import lru_cache
def kp(z,n):
    a=K(1)
    for _ in range(n):a=a*z
    return a

P2=(K(0),K(0))
A2=add(P2,S)
assert A2==(K(0,-2),K(-12,-4))
x,y=A2
b2,b4,b6,b8=4,-4,1,-3
f2=2*y+1
f3=3*kp(x,4)+b2*kp(x,3)+3*b4*kp(x,2)+3*b6*x+b8
f4=f2*(2*kp(x,6)+b2*kp(x,5)+5*b4*kp(x,4)+10*b6*kp(x,3)
       +10*b8*kp(x,2)+(b2*b8-b4*b6)*x+(b4*b8-b6*b6))
@lru_cache(None)
def division(n):
    if n==0:return K(0)
    if n==1:return K(1)
    if n==2:return f2
    if n==3:return f3
    if n==4:return f4
    m=n//2
    if n%2:
        return division(m+2)*kp(division(m),3)-division(m-1)*kp(division(m+1),3)
    return division(m)*(division(m+2)*kp(division(m-1),2)-
                         division(m-2)*kp(division(m+1),2))/f2
D2=division(9)

# Exact independent Euclidean-gcd check of denominator ideal of [9]A2.
# In O_K=Z[omega], omega=(1+sqrt(-11))/2, the norm is Euclidean.
def wgen(a,b):return K(F(2*a+b,2),F(b,2))
def norm(z):return z.a*z.a+11*z.b*z.b
def integral(z):return (z.a-z.b).denominator==1 and (2*z.b).denominator==1
def kgcd(a,b):
    assert integral(a) and integral(b)
    while b!=K(0):
        v=a/b
        c,d=round(v.a-v.b),round(2*v.b)
        q=min((wgen(i,j) for i in range(c-2,c+3)
               for j in range(d-2,d+3)),key=lambda h:norm(v-h))
        r0=a-b*q
        assert integral(r0) and norm(r0)<norm(b)
        a,b=b,r0
    return a
T2=None
for _ in range(9):T2=add(T2,A2)
x2,y2=T2
den=lcm((x2.a-x2.b).denominator,(2*x2.b).denominator)
g=kgcd(x2*den,K(den))
assert integral(D2) and integral(x2*D2*D2) and integral(y2*D2*D2*D2)
assert norm(D2)**2 == F(den**2)/norm(g)

# Sigma_5(t)=t+O(t^3) because a1=0. Both normalized t parameters
# and the independently computed D2 have valuation exactly one.
t2=-x2/y2
units2=[]
for root0 in (r,-r%mod):
    vt,ut=unit(t2,root0)
    vd,ud=unit(D2,root0)
    assert vt==vd==1
    units2.append(ut*pow(ud,-1,p*p)%(p*p))
q2=units2[0]*pow(units2[1],-1,p*p)%(p*p)
h9_2=((pow(q2,p-1,p*p)-1)//p)*pow(p-1,-1,p)%p
hA2=h9_2*pow(9*9,-1,p)%p
assert (q2,hA2)==(16,3), (q2,hA2)
print('PASS second published BCLMN height: 389a1 h(P2+S)=3 mod5')
print('PASS independently computed psi_9 and primitive ideal gcd for [9](P2+S)')
