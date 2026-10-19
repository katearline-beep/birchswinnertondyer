#!/usr/bin/env python3
"""Conditional integral transversality certificate for two Q11 linear maps.

Local: two-prime normalized elliptic log on rational eigenspace V+,
        raw values from C-0002 (independently checked by PARI).
Global: anticyclotomic cross-height linear functional from C-0013,
        three digits are PROVISIONAL conditional on BCLMN 2016.

The crucial unit 2x2 determinant is already visible mod11. Hence, if the
reported first global height digits are valid, the two maps together are
surjective Z11^4 -> Z11^2, with a saturated rank-two common kernel.
This is NOT a Selmer group, derived height, complex rank or BSD theorem.
"""
from math import gcd

p=11
M=p**3
local_raw=[7462,14432,1427,7989]  # C-0002, all modulo 11^4
height_raw=[1068,1300,854,8]      # C-0013, modulo 11^3, provisional

def primitive(vals,m):
    if all(v % p == 0 for v in vals):
        raise ValueError('not a primitive height/log functional: divide common 11 powers first')
    assert vals[0]%p, 'first coordinate cannot normalize: use a unit pivot'
    inv=pow(vals[0],-1,m)
    return [v*inv%m for v in vals]

L=primitive(local_raw,M)
H=primitive(height_raw,M)
assert L==[1,704,772,856],L
assert H==[1,739,766,668],H

D=(L[0]*H[1]-L[1]*H[0])%M
assert D==35 and D%p==2 and gcd(D,M)==1

def dot(a,v,mod=M):return sum(x*y for x,y in zip(a,v))%mod

frame=[]
for free in (2,3):
    v=[0]*4;v[free]=1
    v[1]=(L[free]-H[free])*pow(D,-1,M)%M
    v[0]=(-L[free]-L[1]*v[1])%M
    assert dot(L,v)==dot(H,v)==0
    frame.append(v)
assert frame==[[20,1103,1,0],[2,842,0,1]],frame

# Explicit splitting of the map modulo p^3, valid for any precision
# by the unit-minor argument over Z_11.
for target in ((0,0),(1,0),(0,1),(5,7),(M-1,M-2)):
    y0,y1=target
    x2=(y1-y0)*pow(D,-1,M)%M
    x1=(y0-L[1]*x2)%M
    assert dot(L,[x1,x2,0,0])==y0
    assert dot(H,[x1,x2,0,0])==y1

assert [[x%p for x in v] for v in frame]==[[9,3,1,0],[2,6,0,1]]
assert [[x%121 for x in v] for v in frame]==[[20,14,1,0],[2,116,0,1]]

# Dependent and nearly-dependent controls are nonunits at p:
for bogus in (L,[x+(p if i==1 else 0) for i,x in enumerate(L)]):
    badD=(L[0]*bogus[1]-L[1]*bogus[0])%M
    assert badD%p==0
    try:pow(badD,-1,M)
    except ValueError:pass
    else:raise AssertionError('nonunit determinant accepted')

# Multiplying all provisional heights by p masks the projective profile.
try:primitive([p*x for x in height_raw],M)
except ValueError:pass
else:raise AssertionError('primitive/scale trap was missed')

print('PASS local profile',L,'provisional global profile',H)
print('PASS unit minor 35 mod1331, 2 mod11')
print('PASS common-kernel basis mod1331:',frame)
print('PASS direct split surjectivity; nonunit and scale negative controls')
print('CONDITIONAL: combined Z_11^4 -> Z_11^2 map is split surjective,')
print('with saturated free rank-2 common kernel IF C-0011 global first digit holds.')
print('NONCLAIM: no Selmer identification, derived pairing, complex Lpp or BSD.')
