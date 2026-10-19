#!/usr/bin/env python3
"""Howard (arXiv:1202.6358) Hypothesis 1.0.1 audit on E234446.a1.

Checks Heegner splitting, ordinary p11, conductor/discriminant constraints,
and ABSOLUTE mod11 irreducibility of rho|G_K via two split Frobenius primes:
23 -> nonsquare discriminant => F11-irreducible;
43 -> distinct F11 roots => cannot become reducible over F121.
This uses a standard Galois descent dichotomy and two INDEPENDENT point
count algorithms. Does NOT construct Howard's Euler-system class or
Castella-Hsieh's required localized global z / Coleman-order bounds.
"""
from math import isqrt,pi,sqrt

A=(1,-1,0,-79,289)
p=11
N=2*117223
D=-7

def prime(n):
    return n>=2 and all(n%k for k in range(2,isqrt(n)+1))

def chi(x,ell):
    x%=ell
    if not x:return 0
    v=pow(x,(ell-1)//2,ell)
    assert v in (1,ell-1)
    return 1 if v==1 else -1

def curve_value(x,y,ell):
    return (y*y+x*y-(x*x*x-x*x-79*x+289))%ell

def trace_affine(ell):
    return ell+1-(1+sum(curve_value(x,y,ell)==0
                         for x in range(ell) for y in range(ell)))

def trace_character(ell):
    # y²+xy = x³−x²−79x+289; complete the square.
    return -sum(chi(x*x+4*(x*x*x-x*x-79*x+289),ell)
                for x in range(ell))

assert prime(117223) and prime(23) and prime(43)
assert N==234446 and N%p and (6*N)%p
assert (117223-1)%p != 0  # Howard introduction extra p ∤ phi(N)
assert D%8==1  # 2 splits
assert chi(D,117223)==1 and chi(D,23)==1 and chi(D,43)==1
assert chi(D,11)==1 and (D%11)==4 # 11 splits, roots ±2
assert (2/pi)*sqrt(7)<2  # Minkowski bound => class number K = 1

traces={}
for ell in (11,23,43):
    assert ell != 117223 and ell != 2
    a=trace_affine(ell)
    assert trace_character(ell)==a
    assert abs(a)<=2*sqrt(ell)
    traces[ell]=a
assert traces=={11:-6,23:-6,43:-4},traces
assert traces[11]%11 # p=11 good ordinary

delta23=(traces[23]**2-4*23)%p
delta43=(traces[43]**2-4*43)%p
assert (delta23,delta43)==(10,9)
assert (chi(delta23,p),chi(delta43,p))==(-1,1)
# Proof: If rho|GK were reducible over F11, Frob23 would have a
# split characteristic polynomial: impossible due to delta23 nonsquare.
# If irreducible over F11 but reducible over its algebraic closure, it
# becomes chi ⊕ chi^11 over F121. Each characteristic polynomial is then
# either repeated-root or irreducible over F11; the split DISTINCT
# polynomial at Frob43 rules out this non-split torus possibility.
# Thus rho|GK is ABSOLUTELY irreducible. This relies on standard
# 2-dimensional Galois descent, not on a numeric conjecture.
assert delta43 != 0 and delta23 != 0
assert pow(3,2,11)==delta43

# Falsifiers:
assert chi(delta23,p)!=chi(delta43,p)
assert chi(D,3)==-1 # an inert prime cannot substitute for split Frob
assert N%7 != 0
assert N%p != 0

print("PASS Howard Hyp1.0.1: p=11 excludes 6N; p∤phi(N), all N bad primes split K")
print("PASS K Qsqrt(-7) class number 1 by Minkowski and p=11 splits")
print("PASS p11 ordinary a11=-6; Frob 23 and 43 both split in K")
print("PASS independent point enumeration/character traces:",traces)
print("PASS Frob23 discr 10 nonsquare, Frob43 discr 9 split distinct over F11")
print("PASS rho_bar_E,11 restricted to G_K absolutely irreducible by descent")
print("NONCLAIM: p-stabilized Hida local model and norm-compatible Heegner class not explicitly computed")
print("NONCLAIM: no Coleman augmentation, derived Selmer regulator or original complex L''/BSD proof")
