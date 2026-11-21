#!/usr/bin/env python3
"""Two exact fine-Kummer detectors of an UNCOMPUTED secondary global obstruction.

C0039 local Kummer and C0040 Nek first-height are sourced arithmetic inputs;
this code verifies only their mod-11 dual linear algebra. NO beta2 computed.
"""
from itertools import product

P=11
L=((4,0,8,3,9),(4,0,8,3,2))
Y=((0,1,0,0,0),(-2,0,1,0,0),(-9,0,0,1,0))
A=(2,5,10)  # C0040 first-obstruction pairings, up to common unit.


def dot(u,v):
    return sum(x*y for x,y in zip(u,v))%P


def add(u,v):
    return tuple((x+y)%P for x,y in zip(u,v))


def scale(k,u):
    return tuple(k*x%P for x in u)


def detectors(b):
    return (3*b[0]+b[1])%P,(6*b[0]+b[2])%P


def rank(rows):
    a=[list(row) for row in rows]
    r=0
    for j in range(len(a[0])):
        piv=next((i for i in range(r,len(a)) if a[i][j]%P),None)
        if piv is None:continue
        a[r],a[piv]=a[piv],a[r]
        inv=pow(a[r][j],-1,P)
        a[r]=[inv*z%P for z in a[r]]
        for i in range(len(a)):
            if i!=r:
                z=a[i][j]
                a[i]=[(x-z*y)%P for x,y in zip(a[i],a[r])]
        r+=1
    return r


def run():
    assert rank(Y)==3
    assert all(dot(l,y)==0 for l in L for y in Y)
    Z1=add(scale(3,Y[0]),Y[1])
    Z2=add(scale(6,Y[0]),Y[2])
    assert Z1==(9,3,1,0,0)
    assert Z2==(2,6,0,1,0)
    assert rank((Z1,Z2))==2
    assert all(dot(l,z)==0 for l in L for z in (Z1,Z2))
    assert dot(A,(3,1,0))==dot(A,(6,0,1))==0
    assert A[0]!=0 and detectors(A)==(0,0)

    combinations=0
    for b in product(range(P),repeat=3):
        # Any change of first correction moves secondary pairings by
        # an arbitrary multiple of the first height row (2,5,10).
        for t in range(P):
            assert detectors(add(b,scale(t,A)))==detectors(b)
            combinations+=1
        # Both detector values vanish iff b restricted to KNOWN
        # three dimensional fine MW subspace is in first-obstruction line.
        assert (detectors(b)==(0,0)) == (b in {scale(t,A) for t in range(P)})
    assert combinations==P**4

    # Mutate the actual first-height datum. The claimed annihilator
    # ceases to work; using the wrong ratio is NOT harmless.
    wrong=(2,5,9)
    assert detectors(wrong)!=(0,0)
    assert dot(wrong,(6,0,1))!=0
    # A nonzero raw secondary vector may be pure first-lift ambiguity.
    assert scale(4,A)!=(0,0,0) and detectors(scale(4,A))==(0,0)
    # A synthetic secondary vector genuinely outside the ambiguity line
    # is detected; this is NOT a value for the real elliptic curve.
    assert detectors((1,0,0))==(3,6)
    print("PASS: two independent actual fine Kummer test combinations Z1/Z2")
    print("PASS: exact first-obstruction height row (2,5,10) annihilates both")
    print("PASS: all 14,641 (secondary-vector, first-lift-normalization) controls")
    print("PASS: dual quotient test is complete ONLY on the known 3D fine-MW space")
    print("PASS: wrong first-height row and nonzero-but-pure-gauge controls")
    print("NONCLAIM: no actual second Bockstein pairing evaluated; no Selmer h2 or BSD")


if __name__=="__main__":
    run()
