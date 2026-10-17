#!/usr/bin/env python3
"""C-0002: exact constraint / falsification check inspired by coding theory.

NOT a Selmer computation. The alternative pairing is a formal countermodel,
NOT a computed anticyclotomic height.
"""
p = 11
m = p**4
rows = [
    [7462, 14432, 1427, 7989, 1495],
    [7462, 14432, 1427, 7989, 7921],
]

def dot(a,b,n=m):
    return sum(x*y for x,y in zip(a,b))%n

assert rows[0][0]%p != 0
assert (rows[1][4]-rows[0][4])%p != 0
coefs={j:(rows[0][j]*pow(rows[0][0],-1,m))%m for j in (1,2,3)}
assert coefs=={1:8690,2:14082,3:12835}
kernel=[]
for j,c in coefs.items():
    v=[0]*5
    v[0]=(-c)%m
    v[j]=1
    kernel.append(v)
    assert all(dot(row,v)==0 for row in rows)

# Consider an abstract anticyclotomic pairing on eigenbasis
# (P1,P2,P3,P4,R). It pairs P2 with R and otherwise vanishes.
# It is conjugation anti-equivariant and has rank 2. Its plus
# radical is dimension 3, but is different from the log kernel.
def toy_height(v,w):
    return (v[1]*w[4]+v[4]*w[1])%m

r=[0,0,0,0,1]
assert toy_height(kernel[0][:4]+[0],r)==1

# Experimental negative control: corrupt a single residue. A verifier
# must reject the old basis (this is a test of falsifiability).
mutated=[row[:] for row in rows]
mutated[0][1]=(mutated[0][1]+1)%m
assert dot(mutated[0],kernel[0])==1
assert dot(mutated[1],kernel[0])==0

print("PASS exact unit-pivot / rank-3 two-place constraint calculation")
print("PASS rank-2 symmetry-compatible pairing has DIFFERENT radical")
print("PASS mutated-residue negative control rejected")
print("NONCLAIM: no actual global height or 11-Selmer group was computed")
