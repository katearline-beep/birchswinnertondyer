#!/usr/bin/env python3
"""Reconstruct Ulmer 2002 Theorem 9.2 exact rank formula from q-Frobenius orbits.

Inputs from published Tate/Fermat Jacobi-sum theorems are NOT proved.
Crucial field distinction: rank over Fp(t) is (2,3,7), while ranks over
Fp^(2n)(t) are (3,7,25). Character fields and fibre correction counted.
"""
from math import isqrt

def isprime(p):
    return p>=2 and all(p%i for i in range(2,isqrt(p)+1))

def rank_from_orbits(p,n,d,m):
    assert isprime(p) and n>0 and m>0 and d>0 and (p**n+1)%d==0 and d%p
    q=p**m
    # Gamma^perp=< (3,-6,2,1)>; admissible a=0 or 6*a!=0 mod d.
    remain={a for a in range(d) if a==0 or (6*a)%d!=0}
    orbits=[]
    while remain:
        first=min(remain);v=first;orbit=[]
        while v not in orbit:
            assert v in remain
            orbit.append(v);v=v*q%d
        assert v==first
        for a in orbit:remain.remove(a)
        orbits.append(tuple(orbit))
    # Ulmer Prop.6.4, Cor.7.7, Prop.8.1, Theorem9.2.
    c2=int(d%2==0 and (q-1)%4==0)
    c3=0 if d%3 else (2 if (q-1)%3==0 else 1)
    result=len(orbits)-1+c2+c3
    assert result>=0
    return result,orbits,(c2,c3)

def quotient_P2(q,orbits):
    """Published Corollary 7.7 + Proposition 8.1 give a Frobenius H2 factor.

    P2(Fd/Gamma,T) = product_orbits (1 - q^len(orbit)*T^len(orbit)).
    This constructs the GLOBAL factor conditional on Ulmer's Jacobi-sum theorem.
    """
    poly=[1]
    for orbit in orbits:
        n=len(orbit)
        other=[0]*(len(poly)+n)
        for i,c in enumerate(poly):
            other[i]+=c
            other[i+n]-=c*q**n
        poly=other
    assert len(poly)-1==sum(map(len,orbits))
    assert poly[0]==1
    return poly

if __name__=="__main__":
    for p,n,d,base,geometric in ((5,1,6,2,3),(7,1,8,3,7),(5,2,26,7,25)):
        rank0,o0,c0=rank_from_orbits(p,n,d,1)
        rank_big,obig,cbig=rank_from_orbits(p,n,d,2*n)
        assert (rank0,rank_big)==(base,geometric)
        assert rank_big>=rank0 and base!=geometric
        assert p**(2*n)%d==1
        assert all(len(z)==1 for z in obig)
        small_poly=quotient_P2(p,o0)
        big_poly=quotient_P2(p**(2*n),obig)
        assert len(small_poly)-1 == len(big_poly)-1
        # Nontrivial global Frobenius factors, NOT deductions from local fibres.
        if (p,d)==(5,6):assert small_poly==[1,-5]
        if (p,d)==(7,8):assert len(o0)==4 and sorted(map(len,o0))==[1,2,2,2]
        if (p,d)==(5,26):assert len(o0)==7 and sorted(map(len,o0))==[1,4,4,4,4,4,4]
        print(f"PASS p={p},d={d}: Fp(t) rank={rank0}, "
              f"Fp^(2n)(t) rank={rank_big}; orbit counts={len(o0)},{len(obig)}, corrections={c0},{cbig}")
    try:rank_from_orbits(5,1,7,1)
    except AssertionError:pass
    else:raise AssertionError("invalid Ulmer d not rejected")
    print("PASS published Jacobi-sum-based GLOBAL quotient surface P2 factors, distinct from finite fibre counts")
    print("PASS prevents erroneous equation of geometric rank with Fp(t) rank")
    print("NONCLAIM: published Tate, BSD, and Jacobi-sum Frobenius eigenvalue theorem are dependencies")
