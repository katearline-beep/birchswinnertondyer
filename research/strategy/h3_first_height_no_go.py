#!/usr/bin/env python3
"""H3 falsifier: first-derivative Heegner height cannot distinguish rank 2/4.

Exact formal Taylor arithmetic; this does NOT compute any E/K L-function
or any Heegner point. It rules out one logically invalid proof shortcut.
"""
from math import factorial

def product(a,b):
    p=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            p[i+j]+=x*y
    return p

def deriv(a,k):
    return factorial(k)*a[k] if k<len(a) else 0

# t = s-1, E has order >=2; twist has first-order zero.
twist=[0,5,0,1]
rank2=[0,0,1,0,3]
rank4=[0,0,0,0,1]

for curve in (rank2,rank4):
    basechange=product(curve,twist)
    assert deriv(basechange,0)==0
    assert deriv(basechange,1)==0
    assert deriv(basechange,2)==0
    assert deriv(basechange,3)==3*deriv(curve,2)*deriv(twist,1)

# Both have vanishing first derivative, although the third differs.
assert deriv(product(rank2,twist),1)==deriv(product(rank4,twist),1)==0
assert deriv(product(rank2,twist),3)==30
assert deriv(product(rank4,twist),3)==0

# The first derivative of a higher-weight L is also *one* derivative,
# irrespective of the weight integer k. Its derivative order is not 2k-1.
for k in range(2,8):
    assert 1 != 2*k-1

print("PASS: first base-change derivative vanishes for rank-two and rank-four models")
print("PASS: cubic base-change derivative separates two cases: 30 vs zero")
print("PASS: changing modular weight does not upgrade first to third derivative")
print("NONCLAIM: no cubic geometric identity or exact original L'' has been proved")
