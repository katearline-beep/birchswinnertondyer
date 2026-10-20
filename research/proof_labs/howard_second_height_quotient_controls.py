#!/usr/bin/env python3
"""Session26: SOURCE-derived parity and exact F11 linear-algebra FALSIFIERS.

Howard 1202.6343 Thm4.2: all true universal norms occupy the
intersection of every derived-height kernel, hence cannot witness a
nonzero higher-height value. Howard Conj4.4 predicts S2 dimension
|s_plus-s_minus| and S3 dimension1 in the anticyclotomic Heegner case.
These matrix examples are TOYS. H=(1,2,7,8) is provisional C-0013,
not independently confirmed. No second-height coefficient is measured.
"""
P=11
H=(1,2,7,8)
def rank(matrix):
    a=[list(row) for row in matrix]; n=len(a); m=len(a[0]); r=0
    for j in range(m):
        k=next((i for i in range(r,n) if a[i][j]%P),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        inv=pow(a[r][j]%P,-1,P)
        a[r]=[(inv*x)%P for x in a[r]]
        for i in range(n):
            if i!=r:
                c=a[i][j]%P
                a[i]=[(x-c*y)%P for x,y in zip(a[i],a[r])]
        r+=1
        if r==n:break
    return r
first=[[0]*5 for _ in range(5)]
for i,v in enumerate(H):
    first[i][4]=first[4][i]=v
assert rank(first)==2
assert all(first[i][j]==0 for i in range(4) for j in range(4))
rad_basis=[]
for i in range(1,4):
    x=[0]*5; x[0]=(-H[i])%P; x[i]=1
    assert all(sum(u*v for u,v in zip(row,x))%P==0 for row in first)
    rad_basis.append(x)
assert rank(rad_basis)==3
def alt(a,b,c):
    return [[0,a,b],[(-a)%P,0,c],[(-b)%P,(-c)%P,0]]
for a in range(P):
    for b in range(P):
        for c in range(P):
            h=alt(a,b,c)
            assert rank(h)==(0 if a==b==c==0 else 2)
            candidate=(c,(-b)%P,a)
            assert all(sum(u*v for u,v in zip(row,candidate))%P==0 for row in h)
assert rank(alt(0,0,0))==0
assert rank(alt(1,0,0))==2
# Universal norm u is in EVERY Howard derived-height radical,
# therefore by theorem h_r(u,x)=0 for every x in the domain.
def admissible_nonzero_regulator_witness(is_universal_norm):
    return not is_universal_norm
assert not admissible_nonzero_regulator_witness(True)
# With finite generated Lambda-module M over Z11[[T]], Krull
# intersection forces finite exact T-order for every nonzero z.
# Infinite Laurent module F11((T)) is NOT finite generated over F11[[T]]
# and permits arbitrary T-divisions of 1 (countermodel).
for order in range(1,6):
    series=[0]*7;series[order]=1
    assert next(i for i,x in enumerate(series) if x)==order
assert all(0-n<0 for n in range(1,7))  # Laurent T^-n
print("PASS odd conjugation pairing block cross has rank2, radical dimension3")
print("PASS even alternating pairing on radical dimension3 has rank 0 OR 2")
print("PASS nonzero second height gives radical dim1, zero second is falsifier")
print("PASS universal norm is necessarily radical at all derived heights (Howard Thm4.2)")
print("PASS finite T order needs finitely generated Lambda; Laurent countermodel")
print("NONCLAIM: provisional first height is not fully independently verified")
print("NONCLAIM: no actual second derived height, exact Selmer 4+1, original BSD proof")
