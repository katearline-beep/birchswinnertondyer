#!/usr/bin/env python3
"""Exact local 11-adic log determinant for y²=x³-1267x+17230 over Q(sqrt(-7)).
Checks finite congruences, NOT p-adic heights or BSD.
"""
from fractions import Fraction as F
D,A,B,p=-7,-1267,17230,11
mod=p**3
class K:
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o):
        if not isinstance(o,K):o=K(o)
        return K(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self,o):return self+-o
    def __mul__(self,o):
        if not isinstance(o,K):o=K(o)
        return K(self.a*o.a+D*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        if not isinstance(o,K):o=K(o)
        n=o.a*o.a-D*o.b*o.b
        return self*K(o.a/n,-o.b/n)
    def __eq__(self,o):
        if not isinstance(o,K):o=K(o)
        return self.a==o.a and self.b==o.b
def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x,y=P; u,v=Q
    if x==u and y==-v:return None
    m=(3*x*x+A)/(2*y) if x==u else (v-y)/(u-x)
    z=m*m-x-u
    return z,m*(x-z)-y
def mul(n,P):
    out=None
    while n:
        if n&1:out=add(out,P)
        P=add(P,P);n//=2
    return out
def red(f):
    assert f.denominator%p!=0
    return f.numerator*pow(f.denominator,-1,mod)%mod
roots=[x for x in range(mod) if x%p==2 and (x*x+7)%mod==0]
assert roots==[1058]
r,s=roots[0],(-roots[0])%mod
points={
"P1":(K(15),K(40)),
"P2":(K(19),K(4)),
"P3":(K(23),K(16)),
"P4":(K(31),K(88)),
"R":(K(F(-3355,63)),K(0,F(128780,1323))),
"H":(K(F(37,2),F(3,2)),K(-16,12)),
}
for name,(x,y) in points.items():
    assert y*y==x*x*x+A*x+B,name
assert mul(2,points["H"])==add(add(points["P3"],points["P4"]),points["R"])
count=1+sum(1 for x in range(p) for y in range(p) if (y*y-x*x*x-A*x-B)%p==0)
assert count==18
logs={}
for name,point in points.items():
    x,y=mul(18,point)
    t=-x/y
    vals=[(red(t.a)+w*red(t.b))%mod for w in (r,s)]
    assert all(v%p==0 for v in vals)
    logs[name]=tuple((v//p)*pow(18,-1,p*p)%(p*p) for v in vals)
assert logs=={"P1":(81,81),"P2":(33,33),"P3":(96,96),"P4":(3,3),"R":(108,13),"H":(43,56)}
det=(logs["P1"][0]*logs["H"][1]-logs["P1"][1]*logs["H"][0])%121
assert det==85 and det%11==8
print("PASS: E(F_11) has 18 points; local logs:",logs)
print("PASS: determinant is 85 mod 121 and 8 mod 11")
