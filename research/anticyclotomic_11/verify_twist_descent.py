#!/usr/bin/env python3
"""Exact data checks for quadratic-twist 11-Selmer descent roadmap.

The cohomological Selmer splitting is a mathematical theorem, NOT proven
by this script. Tests only coordinates and finite group algebra.
"""
from fractions import Fraction as Q

D,A,B=-7,-1267,17230
for x,y in ((15,40),(19,4),(23,16),(31,88)):
    assert y*y==x*x*x+A*x+B

Ad,Bd=D*D*A,D**3*B
assert (Ad,Bd)==(-62083,-5909890)
X,Y=Q(3355,9),Q(128780,27)
assert Y*Y==X*X*X+Ad*X+Bd
assert X.denominator==9

def multiply(u,v):
    a,b=u;c,d=v
    return a*c+D*b*d,a*d+b*c
def add(u,v):return u[0]+v[0],u[1]+v[1]
def cube(x):return multiply(multiply(x,x),x)
def conjugate(u):return u[0],-u[1]

# Quadratic twist isomorphism over K: (X,Y) -> (X/D,Y/(D*sqrt(D))).
x,y=(X/D,Q(0)),(Q(0),Y/Q(49))
assert x==(Q(-3355,63),Q(0))
assert y==(Q(0),Q(128780,1323))
assert multiply(y,y)==add(add(cube(x),multiply((Q(A),Q(0)),x)),(Q(B),Q(0)))
assert conjugate(x)==x
assert conjugate(y)==(-y[0],-y[1])

# Projectors (1 +/- sigma)/2 in F_11[C2], exactly p != 2.
p=11
inv2=pow(2,-1,p)
assert inv2==6
plus=[[inv2,inv2],[inv2,inv2]]
minus=[[inv2,-inv2],[-inv2,inv2]]
def matmul(m,n):
    return [[sum(m[i][k]*n[k][j] for k in range(2))%p
             for j in range(2)] for i in range(2)]
assert matmul(plus,plus)==[[v%p for v in row] for row in plus]
assert matmul(minus,minus)==[[v%p for v in row] for row in minus]
assert matmul(plus,minus)==[[0,0],[0,0]]
assert [[(plus[i][j]+minus[i][j])%p for j in range(2)] for i in range(2)]==[[1,0],[0,1]]
print('PASS: rational points, quadratic twist, explicit anti-invariant point')
print('PASS: plus/minus C2 idempotents mod 11')
print('NOT PROVEN HERE: Galois cohomology and local Selmer compatibility')
print('NOT KNOWN: Selmer dimensions, Sha[11], complex analytic rank')
