#!/usr/bin/env python3
"""Synthetic F11 local-global gluing countermodel; NOT elliptic Galois cohomology."""
from itertools import product
P=11
V=list(product(range(P),repeat=2))
def f(v): return (v[0]+v[1])%P==9
def a(v): return v[0]==0
def b(v): return v[1]==0
assert len(V)==121
assert [sum(t(v) for v in V) for t in (f,a,b)]==[11,11,11]
assert sum(f(v) and a(v) for v in V)==1
assert sum(f(v) and b(v) for v in V)==1
assert sum(a(v) and b(v) for v in V)==1
assert sum(f(v) and a(v) and b(v) for v in V)==0
# Deliberately failing original constraint: zero target admits global solution.
assert sum(((v[0]+v[1])%P==0) and a(v) and b(v) for v in V)==1
def rank(M):
    M=[row[:] for row in M]; r=0
    for j in range(len(M[0])):
        pivot=next((i for i in range(r,len(M)) if M[i][j]%P),None)
        if pivot is None: continue
        M[r],M[pivot]=M[pivot],M[r]
        inv=pow(M[r][j],-1,P); M[r]=[inv*x%P for x in M[r]]
        for i in range(len(M)):
            if i!=r:
                q=M[i][j]; M[i]=[(u-q*v)%P for u,v in zip(M[i],M[r])]
        r+=1
        if r==len(M): break
    return r
A=[[1,1],[1,0],[0,1]]
assert rank(A)==2
assert rank([row+[rhs] for row,rhs in zip(A,[9,0,0])])==3
assert rank([row+[rhs] for row,rhs in zip(A,[0,0,0])])==2
print("PASS: 121 vectors; all pairwise systems solvable, triple impossible; independent rank check; zero-target control")
