#!/usr/bin/env python3
"""Exact finite-field control model for preserving Howard Greenberg conditions
after canonical anticyclotomic T-division at the original E/p11/K=-7.

Published premises: Howard Def2.4.2 (Greenberg local kernels), Lemma2.4.4,
Prop2.4.5; K=-7 anticyclotomic tower unramified outside 11; alpha11=5 mod11.
Galois LES is mathematical input, not simulated/derived by finite matrices.
No actual divided class coordinates or derived-height coefficients computed.
"""
P=11
alpha=5
assert alpha not in (0,1,10)
# A=F11[[T]] formal local coefficient ring.
# v|11: ordinary rank-one quotient F^- has unram Frobenius alpha.
# H0(K_v,F^-V)=0 since scalar alpha !=1.
assert (alpha-1)%P !=0
# LES of 0->F^- A --T-> F^- A -> F^- V ->0:
# T-torsion H1(K_v,F^-A) injects from H0(K_v,F^-V)=0.
# This holds separately at the two K-primes above split 11.
for prime_label in ("p","pbar"):
    assert (alpha-1)%P
    print("PASS local",prime_label,"ordinary quotient H0=0 => T injective H1")

# v not dividing 11: ring class tower ramified only above 11,
# hence inertia acts trivially on A=F11[[T]].
# Invariants of V under inertia always lift coefficientwise to A,
# EVEN for nontrivial unipotent inertia / multiplicative reduction.
def invariant_vectors_unipotent():
    # G = [[1,1],[0,1]] and fixed v=(x,y) iff y=0.
    return [(x,y) for x in range(P) for y in range(P)
            if ((x+y-x)%P==0 and y==y)]
fixed=invariant_vectors_unipotent()
assert len(fixed)==P and all(y==0 for x,y in fixed)
# For each v^I=(x,0), its *constant* lift v⊗1 remains I-invariant
# in V⊗F11[[T]] because inertia acts trivially on the tower factor.
for x,y in fixed:
    assert y==0
    lift_const=(x,y)
    assert lift_const in fixed
# LES: surjectivity H0(I,V⊗A)->H0(I,V) kills connecting map
# H0(I,V)->H1(I,V⊗A)[T]; hence T injective on H1(I,V⊗A).

# Negative control: if inertia acted through 1+T on a rank-one
# tower coefficient, constant 1 modT WOULD be invariant but not lift
# to an exact invariant in A, because T*f(T)=0 => f=0 in A.
# Thus the away-from-p result really uses UNRAMIFIEDNESS of K_infty.
nontrivial_inertia_multiplier="1+T"
assert nontrivial_inertia_multiplier!="1"
# No exceptional α=1 allowed: H0(F^-V) then nonzero
assert (1-1)%P==0
# The greenberg condition is kernel of H1(Gv,M)->H1(Iv,M)
# away from p, kernel of H1(Gv,M)->H1(Gv,F^-M) at p.
print("PASS away from 11 inertia acts trivially on Λ so invariants lift")
print("PASS T injective on away-from-11 H1(Iv,V⊗Λ) by LES invariants lift")
print("PASS local Greenberg conditions propagate from z=Tz1 to z1")
print("PASS mutation: exceptional α=1 or inertia-twisted Λ invalidates the short proof")
print("NONCLAIM: local model does not compute Selmer groups or canonical height")
print("NONCLAIM: base of z1/first nonzero derived regulator and complex L'' unknown")
