#!/usr/bin/env python3
"""Exact finite-group controls for a typed Bockstein no-go and its escape.

These groups are algebraic controls, NOT computed Galois groups/cochains.
The arithmetic application requires the separately audited image, Kummer
independence and class-field disjointness lemmas. Finite obstruction may
inflate to zero: it is NOT a global Selmer non-liftability certificate.
"""
from itertools import product

P = 11


def vadd(x,y): return tuple((a+b) % P for a,b in zip(x,y))
def scale(k,x): return tuple(k*a % P for a in x)
def mv(A,x): return ((A[0]*x[0]+A[1]*x[1]) % P,(A[2]*x[0]+A[3]*x[1]) % P)
def mm(A,B):
    return ((A[0]*B[0]+A[1]*B[2]) % P,(A[0]*B[1]+A[1]*B[3]) % P,
            (A[2]*B[0]+A[3]*B[2]) % P,(A[2]*B[1]+A[3]*B[3]) % P)

I = (1,0,0,1)
ZERO = (0,0)


def base_multiply(g,h):
    x,A,k = g; y,B,l = h
    return vadd(x,mv(A,y)),mm(A,B),(k+l) % P


def cover_multiply(g,h):
    """(c0,rho,chi,c1); forgetting c1 gives the natural finite quotient."""
    x,A,k,w = g; y,B,l,z = h
    return (vadd(x,mv(A,y)),mm(A,B),(k+l) % P,
            vadd(vadd(w,mv(A,z)),scale(k,mv(A,y))))


def cover_matrix(g):
    x,A,k,w = g
    return ((A[0],A[1],0,0,x[0]),(A[2],A[3],0,0,x[1]),
            (k*A[0] % P,k*A[1] % P,A[0],A[1],w[0]),
            (k*A[2] % P,k*A[3] % P,A[2],A[3],w[1]),(0,0,0,0,1))


def matrix_product(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(5)) % P
                       for j in range(5)) for i in range(5))


def heisenberg(g,h):
    k,a,b = g; l,c,d = h
    return (k+l) % P,(a+c) % P,(b+d+k*c) % P


def second_cover(g,h):
    k,a,b,e = g; l,c,d,f = h
    return ((k+l) % P,(a+c) % P,(b+d+k*c) % P,
            (e+f+k*d+(k*(k-1)//2)*c) % P)


def main():
    vectors = list(product(range(P),repeat=2))
    tau = (ZERO,I,1)
    translation = ((1,0),I,0)
    assert base_multiply(tau,translation) == base_multiply(translation,tau)
    # For EVERY possible c1(tau), the two commuting-element equations differ
    # by the nonzero translation c0. c1(translation) cancels algebraically.
    for w in vectors:
        lhs = cover_multiply((*tau,w),(*translation,ZERO))
        rhs = cover_multiply((*translation,ZERO),(*tau,w))
        assert lhs[:3] == rhs[:3] and lhs[3] != rhs[3]
    print('PASS nontrivial translation: no first lift factors through H x C11')
    # A coboundary c0=(rho-1)v DOES admit a lift: c1=k*rho*v.
    matrices = [I,(-1 % P,0,0,-1 % P),(1,1,0,1),(1,0,1,1),(2,0,0,1)]
    v = (3,4)
    for A,B,k,l in product(matrices,matrices,range(P),range(P)):
        x = vadd(mv(A,v),scale(-1,v)); y = vadd(mv(B,v),scale(-1,v))
        got = cover_multiply((x,A,k,scale(k,mv(A,v))),(y,B,l,scale(l,mv(B,v))))
        C = mm(A,B)
        assert got == (vadd(mv(C,v),scale(-1,v)),C,(k+l) % P,scale(k+l,mv(C,v)))
    print('PASS negative control: a coboundary class DOES lift on the product quotient')
    # Verify the actual finite cover group law on a deterministic spanning set.
    elements = [(x,A,k,w) for x in ((0,0),(1,0),(0,1))
                for A in matrices for k in (0,1,10) for w in ((0,0),(1,0))]
    for g,h in product(elements,elements):
        assert cover_multiply(g,h)[:3] == base_multiply(g[:3],h[:3])
        assert cover_matrix(cover_multiply(g,h)) == matrix_product(cover_matrix(g),cover_matrix(h))
    samples = elements[::7]
    for g,h,j in product(samples,samples,samples):
        assert cover_multiply(cover_multiply(g,h),j) == cover_multiply(g,cover_multiply(h,j))
    print('PASS twisted E11-vector group cover; kernel has121 elements')
    # Positive control: inflation to a Heisenberg group kills the first cup class.
    group = list(product(range(P),repeat=3))
    for g,h in product(group,group):
        result = heisenberg(g,h)
        assert result[0] == (g[0]+h[0]) % P
        assert result[1] == (g[1]+h[1]) % P
        assert result[2] == (g[2]+h[2]+g[0]*h[1]) % P
    t,z = (1,0,0),(0,0,1)
    assert heisenberg(t,z) == heisenberg(z,t)
    # At order T^2, t and central z commute but chi(t)*c1(z)=1.
    # Therefore a second lift cannot factor through THIS Heisenberg group.
    assert (t[0]*z[2]+(t[0]*(t[0]-1)//2)*z[1]) % P == 1
    assert (z[0]*t[2]+(z[0]*(z[0]-1)//2)*t[1]) % P == 0
    print('PASS inflation can kill first obstruction; first lift need not kill second')
    # A larger class-three coefficient extension supplies the next correction.
    for k,l in product(range(P),repeat=2):
        assert ((k+l)*(k+l-1)//2-k*(k-1)//2-l*(l-1)//2-k*l) % P == 0
    sample2 = [(k,a,b,c) for k,a,b,c in product((0,1,10),repeat=4)]
    for g,h,j in product(sample2[::5],repeat=3):
        assert second_cover(second_cover(g,h),j) == second_cover(g,second_cover(h,j))
    print('PASS larger class-three cover supplies second correction in a synthetic control')
    # Exact arithmetic degree consequences IF the focal GL2 image input holds.
    gl2 = (P*P-1)*(P*P-P)
    assert gl2 == 13200
    assert P**10*gl2 == 342374004733200
    assert P**2*gl2*P*P**2 == 2125873200
    print('CONDITIONAL DEGREE five-class Kummer field:',P**10*gl2)
    print('CONDITIONAL DEGREE single-class first-lift splitting field:',P**2*gl2*P*P**2)
    print('NONCLAIM: no actual arithmetic cover realization, local Selmer lift, h2 or BSD')


if __name__ == '__main__': main()
