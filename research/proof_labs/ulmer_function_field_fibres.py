#!/usr/bin/env python3
"""Finite-fibre arithmetic checks for Ulmer's PROVEN high-rank function-field family.

Known THEOREM (not proven here): D. Ulmer, Annals of Mathematics 155
(2002), Theorem 1.5 + Remark 1.6:
E: y²+xy=x³-t^d, d=p^n+1 over F_p(t), has rank p^n
unless 6|d, when rank=p^n-2. The associated BSD/Tate result is
an input from the paper. Our point counts test only finite fibres.
"""
from math import isqrt

def prime(p):
    return p >= 2 and all(p % k for k in range(2,isqrt(p)+1))

def legendre(a,p):
    a %= p
    if a == 0:return 0
    v=pow(a,(p-1)//2,p)
    assert v in (1,p-1)
    return 1 if v==1 else -1

def fibre_trace(p,d,t):
    td=pow(t,d,p)
    disc=td*(1-432*td)%p
    if disc==0:return None
    count=1+sum(1 for x in range(p) for y in range(p)
                if (y*y+x*y-x*x*x+td)%p==0)
    trace=p+1-count
    trace2=-sum(legendre(x*x+4*(x*x*x-td),p) for x in range(p))
    assert trace==trace2,(p,d,t,trace,trace2)
    assert trace*trace<=4*p
    return trace

def run_case(p,n,want_rank,want_good):
    assert prime(p) and p>=5 and n>=1
    d=p**n+1
    rank=p**n-(2 if d%6==0 else 0)
    assert rank==want_rank
    assert d%p==1 and 432%p
    # Delta=t^d(1-432*t^d), j=1/Delta, nonconstant as rational function.
    traces={t:fibre_trace(p,d,t) for t in range(p)}
    good={t:a for t,a in traces.items() if a is not None}
    assert len(good)==want_good,good
    assert all(pow(t,d,p)==t*t%p for t in range(p))
    assert any(good.values())
    print(f"p={p} n={n} d={d}: published theorem rank={rank}; good fibres={len(good)}; sum a_p(t)={sum(good.values())}; finite-count PASS")
    return good

if __name__=="__main__":
    a=run_case(5,1,3,4)
    run_case(7,1,7,6)
    b=run_case(5,2,25,4)
    assert a==b, (a,b)  # CRITICAL: identical local traces, globally different ranks
    assert fibre_trace(5,6,0) is None
    assert all(fibre_trace(5,6,t) is not None for t in range(1,5))
    print("PASS independent affine/Legendre point counts, Hasse bounds and excluded bad fibres")
    print("NONCLAIM: finite counts do not prove rank, a global L-polynomial, Tate or BSD")
