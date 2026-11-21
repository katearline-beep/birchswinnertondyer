#!/usr/bin/env python3
"""Five independent cup obstructions on the ACTUAL Session46 finite base.

Finite linear algebra, NOT a computation of arithmetic H^2 or inflation.
The 4D supported inflation-kernel lower bound is conditional on C0047.
"""
from itertools import permutations, product

P = 11
ZERO2 = (0, 0)
Z = (0, (ZERO2,)*5)


def add(u, v):
    return tuple((x+y) % P for x,y in zip(u,v))


def sub(u, v):
    return tuple((x-y) % P for x,y in zip(u,v))


def groupadd(g,h):
    e,x=g;f,y=h
    return (e+f)%P, tuple(add(a,b) for a,b in zip(x,y))


def cup(i,g,h,ell_scale=1):
    """-ell(g)*c_i(h), coefficients V trivial on Gal(B5/L)."""
    e,_=g
    _,v=h
    return tuple((-ell_scale*e*z) % P for z in v[i])


def tchar():
    return (1,(ZERO2,)*5)


def generator(i, vector=(1,0)):
    coords=[ZERO2]*5
    coords[i]=vector
    return (0,tuple(coords))


def determinant(m):
    n=len(m)
    out=0
    for perm in permutations(range(n)):
        t=(-1)**sum(perm[i]>perm[j] for i in range(n)
                    for j in range(i+1,n))
        for i in range(n): t*=m[i][perm[i]]
        out+=t
    return out%P


def rank(rows):
    a=[list(row) for row in rows]
    n=len(a[0])
    r=0
    for c in range(n):
        p=next((i for i in range(r,len(a)) if a[i][c]%P),None)
        if p is None:continue
        a[r],a[p]=a[p],a[r]
        scale=pow(a[r][c],-1,P)
        a[r]=[x*scale%P for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                fac=a[i][c]
                a[i]=[(x-fac*y)%P for x,y in zip(a[i],a[r])]
        r+=1
    return r


def cocycle_identity():
    # Deterministic many-coordinate sample plus all five basis generators.
    elements=[Z,tchar()]+[generator(i) for i in range(5)]
    elements+=[generator(i,(0,1)) for i in range(5)]
    elements += [
        (2,((1,2),(3,4),(5,6),(7,8),(9,10))),
        (7,((2,10),(4,8),(6,6),(8,4),(10,2))),
        (10,((7,3),(1,5),(9,2),(6,8),(3,4)))]
    for g,h,k in product(elements,repeat=3):
        for i in range(5):
            # δα(g,h,k) = α(h,k)-α(g+h,k)+α(g,h+k)-α(g,h).
            d=add(sub(cup(i,h,k),cup(i,groupadd(g,h),k)),
                  sub(cup(i,g,groupadd(h,k)),cup(i,g,h)))
            assert d==ZERO2
    return len(elements)**3*5


def anti_matrix(modified=False):
    t=tchar()
    matrix=[]
    for i in range(5):
        z=generator(i)
        row=[]
        for j in range(5):
            if modified and j==4:
                a=add(cup(0,t,z),cup(1,t,z))
                b=add(cup(0,z,t),cup(1,z,t))
            else:
                a=cup(j,t,z)
                b=cup(j,z,t)
            anti=sub(a,b)
            assert anti[1]==0
            row.append(anti[0])
        matrix.append(row)
    return matrix


def main():
    tested=cocycle_identity()
    m=anti_matrix()
    assert m==[[10 if i==j else 0 for j in range(5)]
               for i in range(5)]
    assert rank(m)==5 and determinant(m)==10
    # An arbitrary coboundary for an abelian group with trivial V
    # coefficients is symmetric, so these nonzero alternating
    # evaluations are genuine nonzero and independent H^2 classes.
    dependent=anti_matrix(modified=True)
    assert rank(dependent)==4 and determinant(dependent)==0
    # A zero anticyclotomic character kills all five cross-cups.
    for i in range(5):
        assert cup(i,tchar(),generator(i),ell_scale=0)==ZERO2
    # Source-dependent C0047 kills first four under arithmetic
    # inflation. It does NOT determine the fifth image. These two
    # synthetic maps from a 5D input show both possibilities:
    zero_all=[(0,)*5]
    detect_fifth=[(0,0,0,0,1)]
    assert rank(zero_all)==0 and rank(detect_fifth)==1
    print(f"PASS {tested} exact 2-cocycle triple identities")
    print("PASS 5x5 alternating commutator matrix=-I, determinant10 mod11")
    print("PASS dependent fifth point, zero-character and exact-vs-lower-bound controls")
    print("CONDITIONAL: C0047 source hypotheses kill four of these five classes")
    print("NONCLAIM: no arithmetic H2 or inflation computed by code; no first cochain or BSD")


if __name__=="__main__":
    main()
