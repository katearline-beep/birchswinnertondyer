#!/usr/bin/env python3
"""PROVISIONAL anticyclotomic self-heights mod 11 for E(234446.a1)/Q(sqrt(-7)).

Implements first 11-adic digit of BCLMN (2016), Proposition 2.4,
using division-polynomial denominator generators and sigma(t)=t+t^2/2+O(t^3).
Values are conditional on paper normalization and the exact recurrences;
not externally peer-reviewed, not BSD. Python standard library only.
"""
import sys
from fractions import Fraction as F
from math import lcm
from functools import lru_cache
sys.set_int_max_str_digits(100000)

class K:
    def __init__(self,a=0,b=0):self.a,self.b=F(a),F(b)
    def __add__(self,o):
        if not isinstance(o,K):o=K(o)
        return K(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self,o):return self+-o
    def __mul__(self,o):
        if not isinstance(o,K):o=K(o)
        return K(self.a*o.a-7*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        if not isinstance(o,K):o=K(o)
        n=o.a*o.a+7*o.b*o.b
        assert n
        return self*K(o.a/n,-o.b/n)
    def __eq__(self,o):
        if not isinstance(o,K):o=K(o)
        return self.a==o.a and self.b==o.b

O=K(0)
def omega(a,b):return K(F(2*a+b,2),F(b,2))
def norm(z):return z.a*z.a+7*z.b*z.b
def integer(z):return (z.a-z.b).denominator==1 and (2*z.b).denominator==1

def quo(a):
    u,v=a.a-a.b,2*a.b
    x,y=round(u),round(v)
    q=min((omega(i,j) for i in range(x-2,x+3) for j in range(y-2,y+3)),
          key=lambda t:norm(a-t))
    assert norm(a-q)<1
    return q

def gcd(a,b):
    assert integer(a) and integer(b)
    steps=0
    while b!=O:
        r=a-b*quo(a/b)
        assert integer(r) and norm(r)<norm(b)
        a,b=b,r;steps+=1
        assert steps<3000
    return a

def mincoord(Q):
    z,w=Q
    return (z+1)/4,(w-z-1)/8

def denorm(Q):
    x,y=mincoord(Q);u,v=x.a-x.b,2*x.b
    D=lcm(u.denominator,v.denominator)
    G=gcd(x*D,K(D))
    z=F(D*D)/norm(G)
    assert z.denominator==1
    return int(z)

def cert(Q,d):
    x,y=mincoord(Q)
    assert integer(d) and integer(x*d*d) and integer(y*d*d*d)
    assert norm(d)**2==denorm(Q),('nonprimitive denominator',norm(d)**2,denorm(Q))

def add(P,Q):
    x,y=P;u,v=Q
    slope=(v-y)/(u-x) if x!=u else (3*x*x-1267)/(2*y)
    z=slope*slope-x-u
    return z,slope*(x-z)-y

def scale(n,P):
    R=None
    while n:
        if n&1:R=P if R is None else add(R,P)
        n//=2
        if n:P=add(P,P)
    return R

b2,b4,b6,b8=-3,-158,1156,-7108

def division(B,d,n):
    # f_n=psi_n(B)*d^(n^2-1) in O_K, by integral recurrence.
    x,y=mincoord(B);X=x*d*d;Y=y*d*d*d
    assert integer(X) and integer(Y)
    xx=[K(1)];gg=[K(1)]
    for _ in range(6):xx.append(xx[-1]*X)
    for _ in range(12):gg.append(gg[-1]*d)
    f2=2*Y+X*d
    f3=3*xx[4]+b2*xx[3]*gg[2]+3*b4*xx[2]*gg[4]+3*b6*xx[1]*gg[6]+b8*gg[8]
    f4=f2*(2*xx[6]+b2*xx[5]*gg[2]+5*b4*xx[4]*gg[4]+10*b6*xx[3]*gg[6]+10*b8*xx[2]*gg[8]
           +(b2*b8-b4*b6)*xx[1]*gg[10]+(b4*b8-b6*b6)*gg[12])
    @lru_cache(None)
    def f(k):
        if k==0:return K(0)
        if k==1:return K(1)
        if k==2:return f2
        if k==3:return f3
        if k==4:return f4
        m=k//2
        if k%2:z=f(m+2)*f(m)*f(m)*f(m)-f(m-1)*f(m+1)*f(m+1)*f(m+1)
        else:z=f(m)*(f(m+2)*f(m-1)*f(m-1)-f(m-2)*f(m+1)*f(m+1))/f2
        assert integer(z),('bad division polynomial recursion',k)
        return z
    return f(n)

p=11;PREC=10;M=p**PREC

def wroot():
    w=2
    for k in range(1,PREC):
        w=next(w+j*p**k for j in range(p) if ((w+j*p**k)**2+7)%p**(k+1)==0)
    return w

def embed(z,w):
    return (z.a.numerator*pow(z.a.denominator,-1,M)+z.b.numerator*pow(z.b.denominator,-1,M)*w)%M

def jdbl(P):
    x,y,z=P;Y2=y*y%M;S=4*x*Y2%M;V=(3*x*x-1267*pow(z,4,M))%M
    xx=(V*V-2*S)%M
    return xx,(V*(S-xx)-8*Y2*Y2)%M,(2*y*z)%M

def jadd(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y,z=P;u,v,t=Q
    z2=z*z%M;t2=t*t%M
    U=x*t2%M;V=u*z2%M
    Y=y*t2*t%M;W=v*z2*z%M
    H=(V-U)%M;R=(W-Y)%M
    if H==0:return jdbl(P) if R==0 else None
    H2=H*H%M;H3=H*H2%M
    xx=(R*R-H3-2*U*H2)%M
    return xx,(R*(U*H2-xx)-Y*H3)%M,(H*z*t)%M

def jmul(n,P):
    Q=None
    while n:
        if n&1:Q=jadd(Q,P)
        n//=2
        if n:P=jdbl(P)
    return Q

def vp(x):
    if x==0:return PREC
    k=0
    while x%p==0:k+=1;x//=p
    return k

def scaled_height_mod11(A,d,n):
    # Proposition 2.4: 1/p log( sigma(t_plus)*d_minus /
    #                          (sigma(t_minus)*d_plus) ).
    # sigma(t)=t+(a1/2)t^2+O(t^3), with a1=1, and t in pZp.
    root=wroot();u=[]
    for w in (root,(-root)%M):
        x=embed(A[0],w);y=embed(A[1],w)
        assert (y*y-x*x*x+1267*x-17230)%M==0
        X,Y,Z=jmul(n,(x,y,1))
        den=(Y-X*Z-Z**3)%M
        assert den%p
        t=(-2*Z*(X+Z*Z))*pow(den,-1,M)%M
        dd=embed(d,w)
        e=vp(t)
        assert e==vp(dd) and e>=1 and e<=PREC-3
        sig=(t+t*t*pow(2,-1,M))%M
        unit=((sig//p**e)*pow((dd//p**e)%(p*p),-1,p*p))%(p*p)
        u.append(unit)
    q=u[0]*pow(u[1],-1,p*p)%(p*p)
    return ((pow(q,10,p*p)-1)//p)*pow(10,-1,p)%p,q

points=[(K(15),K(40)),(K(19),K(4)),(K(23),K(16)),(K(31),K(88))]
R=(K(F(-3355,63)),K(0,F(128780,1323)))
dA=[5*omega(7,-2),omega(1,-1)*omega(19,-16),omega(29,8),omega(-1,26)]
corrections=[2,1,2,2]
expected_dA=[1075,1138,1201,1327]
expected_dB=[47295512879050,9503262597784,9476672644861,224062363149514]
expected_q=[58,78,70,115]
expected_height=[1,2,7,8]
heights=[]
for i,(P,g,c) in enumerate(zip(points,dA,corrections)):
    A=add(P,R);B=add(A,A);C=add(B,B)
    cert(A,g)
    assert norm(g)==expected_dA[i]
    inflated=(A[1]/4)*g*g*g*g
    dB=inflated/c
    cert(B,dB)
    assert norm(dB)==expected_dB[i]
    assert norm(inflated)**2==denorm(B)*c**4
    for k in (2,3,4):cert(scale(k,B),division(B,dB,k)*dB)
    dC=division(B,dB,2)*dB
    cert(C,dC)
    d36=division(B,dB,18)*dB
    d36b=division(C,dC,9)*dC
    assert d36==d36b or d36==-d36b
    h36,q=scaled_height_mod11(A,d36,36)
    h72,_=scaled_height_mod11(A,division(C,dC,18)*dC,72)
    assert h72==4*h36%11
    hA=h36*pow(36*36,-1,11)%11
    assert hA==expected_height[i] and q==expected_q[i]
    heights.append(hA)
    print('A',i+1,'N(d_2A)',norm(dB),'bad-2 correction',c,
          'q mod121',q,'h(A) mod11',hA,'[72] quadraticity PASS')
assert heights[1]%11!=0 # L11 required a2=0
print('PASS exact ideal gcds, 2A*18=4A*9, 72A quadraticity')
print('PROVISIONAL global anticyclotomic h(P_i+R) mod11:',heights)
print('CONDITIONAL L11 counterevidence: global [1:2:7:8], local [1:0:2:9]')
print('NONCLAIM: no external Sage/PARI audit, no complex L-double-prime theorem, no BSD proof')
