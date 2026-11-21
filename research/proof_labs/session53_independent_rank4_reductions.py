#!/usr/bin/env python3
"""Exact independent rank >=4 certificate from four good-prime reductions.

Over F_q, project [#E(Fq)/11] P_i to the 1-dimensional 11-primary group.
A rank-four matrix of reduction signatures proves four rational P_i
are independent in E(Q)/11, provided E(Q)[11]=0. Count at q=3 kills
rational 11-torsion (also 2-torsion). No LMFDB rank input used.
"""
from itertools import permutations

P=11
A=-1267
B=17230
POINTS=((15,40),(19,4),(23,16),(31,88))
# q, exact #E(Fq), expected nonzero [n/11]P1, expected four logs
DATA=(
    (2843,2893,(2693,2385),(1,4,9,9)),
    (3019,2959,(1325,2149),(1,8,0,4)),
    (5147,5236,(4813,1927),(1,2,9,8)),
    (5737,5632,(832,2511),(1,5,5,0)),
)


def count(q):
    s=q+1
    for x in range(q):
        f=(x*x*x + A*x+B)%q
        if f:
            s+=1 if pow(f,(q-1)//2,q)==1 else -1
    return s


def plus(U,V,q):
    if U is None:return V
    if V is None:return U
    x,y=U
    z,w=V
    if x==z and (y+w)%q==0:return None
    if U==V:
        assert (2*y)%q!=0
        slope=(3*x*x+A)*pow(2*y,-1,q)%q
    else:
        slope=(w-y)*pow(z-x,-1,q)%q
    xx=(slope*slope-x-z)%q
    return xx,(slope*(x-xx)-y)%q


def mul(n,U,q):
    W=None
    while n:
        if n&1:W=plus(W,U,q)
        U=plus(U,U,q)
        n//=2
    return W


def det_permutation(M):
    total=0
    for perm in permutations(range(4)):
        inversions=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term=(-1)**inversions
        for i in range(4):
            term*=M[i][perm[i]]
        total+=term
    return total%P


def det_gaussian(M):
    X=[list(row) for row in M]
    determinant=1
    for col in range(4):
        pivot=next((i for i in range(col,4) if X[i][col]%P!=0),None)
        if pivot is None:return 0
        if pivot!=col:
            X[col],X[pivot]=X[pivot],X[col]
            determinant=-determinant
        z=X[col][col]%P
        determinant=determinant*z%P
        inv=pow(z,-1,P)
        for i in range(col+1,4):
            c=X[i][col]*inv%P
            for j in range(col,4):
                X[i][j]=(X[i][j]-c*X[col][j])%P
    return determinant%P


def main():
    assert count(3)==7 and 7%2!=0 and 7%P!=0
    # Reduction at a good rational prime q=3 injects rational torsion
    # of orders 2 and 11, so neither can exist in E(Q).
    rows=[]
    for q,n,base,expected in DATA:
        assert q not in (2,11,117223) and count(q)==n
        assert n%P==0 and n%(P*P)!=0
        pts=[(x%q,y%q) for x,y in POINTS]
        assert all((y*y-x*x*x-A*x-B)%q==0 for x,y in pts)
        images=[mul(n//P,pt,q) for pt in pts]
        t=images[0]
        assert t==base and t is not None and mul(11,t,q) is None
        logs={mul(i,t,q):i for i in range(P)}
        assert len(logs)==11 and all(w in logs for w in images)
        row=tuple(logs[w] for w in images)
        assert row==expected
        rows.append(row)
        print(f"MW11_REDUCTION {q} #{n} {row} T={base}")
    d1=det_permutation(rows)
    d2=det_gaussian(rows)
    assert d1==d2==5
    assert det_permutation(rows[:3]+[rows[1]])==0
    mutant=[list(r) for r in rows]
    mutant[0][1]=(mutant[0][1]+1)%P
    assert det_permutation(mutant)!=5
    print("PASS: independent exact F3 count 7 excludes E(Q)[2] and E(Q)[11]")
    print("PASS: 4x4 four-point mod11 reduction determinant=5 by two independent algorithms")
    print("CERTIFICATE_CONCLUSION rank E(Q) >= 4 by independent reductions, no rank database needed")
    print("NONCLAIM: finite reductions alone do NOT bound rank above4 or any Sha")


if __name__=="__main__":
    main()
