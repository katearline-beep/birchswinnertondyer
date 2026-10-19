#!/usr/bin/env python3
"""Exact point coordinates and rational denominator candidates for h_ac(P_i+R).

Not local denominator ideals of [36](P_i+R); not global heights.
"""
from fractions import Fraction as F
from math import lcm

class K:
    def __init__(self,a=0,b=0):
        self.a,self.b=F(a),F(b)
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
        return self*K(o.a/n,-o.b/n)
    def __eq__(self,o):
        if not isinstance(o,K):o=K(o)
        return self.a==o.a and self.b==o.b

def add(P,Q):
    x,y=P;u,v=Q
    m=(v-y)/(u-x) if x!=u else (3*x*x-1267)/(2*y)
    z=m*m-x-u
    return z,m*(x-z)-y

def oncurve(P):
    x,y=P
    return y*y==x*x*x-1267*x+17230

def factor(n):
    result={};d=2
    while d*d<=n:
        while n%d==0:
            result[d]=result.get(d,0)+1
            n//=d
        d+=1 if d==2 else 2
    if n>1:result[n]=1
    return result

def integral_tuple(z):
    d=lcm(z.a.denominator,z.b.denominator)
    return (int(d*z.a),int(d*z.b),d)

points=[(K(15),K(40)),(K(19),K(4)),(K(23),K(16)),(K(31),K(88))]
R=(K(F(-3355,63)),K(0,F(128780,1323)))
assert all(oncurve(P) for P in points+[R])
assert 1+sum(1 for x in range(11) for y in range(11)
       if (y*y-x*x*x+1267*x-17230)%11==0)==18

expected=[
    ({5:2,43:2},{5:3,43:3}),
    ({2:3,569:2},{2:4,569:3}),
    ({1201:2},{1201:3}),
    ({1327:2},{1327:3}),
]
for i,P in enumerate(points):
    z,w=add(P,R)
    assert oncurve((z,w))
    X=(z+1)/4
    Y=(w-z-1)/8
    assert Y*Y+X*Y==X*X*X-X*X-79*X+289
    xt=integral_tuple(X);yt=integral_tuple(Y)
    support=(factor(xt[2]),factor(yt[2]))
    assert support==expected[i],(i,support)
    print(f'A{i+1}=P{i+1}+R: X=({xt[0]} + ({xt[1]})w)/{xt[2]}; Y=({yt[0]} + ({yt[1]})w)/{yt[2]}')
    print('  rational coefficient denominator factors:',support)
# Formal height identities: If h has symmetric anti-conjugation shape,
# then h(Pi+R,Pi+R)=2h(Pi,R), regardless of rank.
a=(1,2,3,4)
def toy_height(x,y):
    return sum(a[i]*(x[i]*y[4]+x[4]*y[i]) for i in range(4))
r=(0,0,0,0,1)
for i in range(4):
    v=tuple(1 if j in (i,4) else 0 for j in range(5))
    assert toy_height(v,v)==2*a[i]
    for j in range(i+1,4):
        w=tuple(1 if k in (i,j,4) else 0 for k in range(5))
        assert toy_height(w,w)==2*(a[i]+a[j])
print('PASS exact addition, minimal-model conversion and formal polarization controls')
print('NONCLAIM: denominator supports are not local ideal valuations after [36]')
