#!/usr/bin/env python3
"""Theorem-first scope gates for Castella--Hsieh 2022 rank-two Kato classes.

Published Theorem A (UNDER ALL ITS HYPOTHESES):
    kappa !=0 => dim_Qp Sel(Q,VpE)=2.
Standard Kummer injectivity: rank E(Q)>=r => dim Sel >=r.
Therefore for rank>=4, hypotheses imply kappa=0 (contrapositive).
This does NOT construct kappa, prove theorem hypotheses, or control
complex analytic L''; for K=Q(sqrt(-7)) Theorem A's odd-inert
N^- condition fails for our conductor 2*117223.
"""
from math import isqrt

def prime(p):
    return p >= 2 and all(p % k for k in range(2,isqrt(p)+1))

def split_at_2(D):
    assert D%4==1 and D%2
    return D%8==1

def quadratic_split(D,q):
    assert prime(q) and q%2 and D%q
    v=pow(D%q,(q-1)//2,q)
    assert v in (1,q-1)
    return v==1

def rank_lower_bound(r):
    # Inject E(Q) tensor Qp into Sel(Q,VpE) via Kummer maps.
    assert r>=0
    return r

def nonzero_kappa_allowed(all_CH_hypotheses,known_MW_rank):
    # This is only a LOGICAL compatibility checker, not a class evaluation.
    if not all_CH_hypotheses:return None  # no Theorem A conclusion
    return rank_lower_bound(known_MW_rank)<=2

# Focal K=-7: both multiplicative bad primes of N=2*117223 split.
assert split_at_2(-7)
assert quadratic_split(-7,117223)
assert not quadratic_split(-43,389)  # an inert prime is possible for a different K.
assert quadratic_split(-11,389)  # BCLMN 389a1/K=-11 is NOT auto-valid as a CH example.
assert (-7)%11 in (1,4,9,16,25,36,49,64,81,100)  # split p=11, no claim on N^-.
assert nonzero_kappa_allowed(True,4) is False
assert nonzero_kappa_allowed(True,2) is True
assert nonzero_kappa_allowed(False,4) is None
# Mutating Kummer's lower bound to 2 would obscure the contradiction;
# preserve the rank-4 dimension gap explicitly.
assert rank_lower_bound(4)>2
# Theorem 4.1 in CH has derived filtrations S^(i) for general rank
# under different hypotheses, not a theorem of complex rank >=4.
print("PASS K=-7: 2 and 117223 split; N^- = 1, NOT odd number of inert primes")
print("PASS CH Theorem A under full hypotheses: nonzero kappa => Sel dim2")
print("PASS rank4 Kummer lower bound => kappa must vanish IF all Theorem A hypotheses hold")
print("PASS no theorem-A deduction when odd-inert and other hypotheses are absent")
print("NONCLAIM: no computation of generalized Kato class, derived height or complex BSD")
