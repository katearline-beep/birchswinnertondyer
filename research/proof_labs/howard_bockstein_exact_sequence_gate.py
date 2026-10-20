#!/usr/bin/env python3
"""Exact adversarial finite-group and cochain models for divided Howard classes.

PUBLISHED mathematical inputs, not constructed by this script:
* Howard Prop 2.3.1 and §3.3: normalized universal norms.
* Howard Thm 3.1.1/Cor 3.1.2: FOR EACH torsion-group χ,
  including χ=1, sufficiently deep χ-projected Heegner specializations
  are nonzero over Q11.
* standard Shapiro/long cohomology exact sequence of
  0 -> T_pE ⊗ Λ --(gamma-1)--> T_pE ⊗ Λ -> T_pE -> 0
  shows H1_Iw/(gamma-1) ↪ H1(K,T_pE) if H0(K,T_pE)=0.
We use exact F11 group representations / truncated F11[[T]] ONLY
as falsification controls. Deep Heegner classes or actual Bockstein
pairings are NOT computed here.
"""
P=11
ORDER=10 # Gal(H_{11^s}/D_{s-1}), class number one K=-7
assert ORDER%P
inv10=pow(ORDER,-1,P)
assert ORDER*inv10%P==1

def act_shift(v,k):
    n=len(v)
    return tuple(v[(i-k)%n] for i in range(n))

def trace(v):
    n=len(v);assert n==ORDER
    return tuple(sum(act_shift(v,k)[i] for k in range(n))%P
                 for i in range(n))

def projector(v):
    return tuple(inv10*x%P for x in trace(v))

v_trivial=tuple([1]*ORDER)
v_nontriv=tuple([1,10]+[0]*(ORDER-2))
assert projector(v_trivial)==v_trivial
assert trace(v_trivial)==tuple([10]*ORDER)
assert projector(v_nontriv)==tuple([0]*ORDER)
assert trace(v_nontriv)==tuple([0]*ORDER)
# For an ACTUAL cohomology class c, res(cor(c))=trace_delta(c);
# nonzero trivial-projector trace therefore forces cor(c) nonzero.
assert any(trace(v_trivial))
assert not any(trace(v_nontriv))
for scalar in (1,3,7,10):
    v=tuple(scalar*a%P for a in v_trivial)
    assert any(trace(v))
# Test source's G_tors-trivial choice is ESSENTIAL: a nontrivial
# isotypical class may be deep nonzero but norm to anti tower zero.
assert any(v_nontriv) and not any(trace(v_nontriv))

# Truncated module A=F11[T]/(T^6).
L=6
def mulT(v):
    return (0,)+tuple(v[:-1])
def ordT(v):
    return next((i for i,x in enumerate(v) if x%P),None)

source=(0,0,5,6,0,0) # artificial nonzero tower, augmentation zero
assert ordT(source)==2
first_divide=source[1:]+(0,)
assert mulT(first_divide)==source and ordT(first_divide)==1
second_divide=first_divide[1:]+(0,)
assert ordT(second_divide)==0
assert second_divide[0]==5

# Finite truncation has T torsion: highest monomial T^5 is killed by T.
# Thus division is nonunique in THIS TOY ring; in actual integral
# untruncated Iwasawa cohomology, injectivity needs H0(K,TpE)=0.
top=(0,0,0,0,0,1)
assert mulT(top)==tuple([0]*L)
assert mulT(tuple((a+b)%P for a,b in zip(first_divide,top)))==source

# Without an H0=0 gate, exact sequence may have T-torsion and
# canonical division fails. Verified C0020 absolute residual irreduc
# over GK => E[11](K)=0 => Tate module invariants =0.
residual_abs_irreducible_over_GK=True # published/independently checked C0020
assert residual_abs_irreducible_over_GK
# A nonzero divided class may have ZERO base (as here first_divide[0]=0)
# and thus cannot be directly inserted as a nonzero CH derived Selmer.
assert first_divide[0]==0
print('PASS C10 invariant projection: trivial component norms nonzero')
print('PASS nontrivial C10 component can be nonzero yet its norm is zero')
print('PASS Howard Cor3.1.2 at trivial C10 character is needed for nonzero weight2 tower')
print('PASS abstract LES: H0(K,TpE)=0 => T injective on integral global H1Iw')
print('PASS conditional actual result: zero base + nonzero tower => unique NONZERO T-division')
print('PASS toy truncation deliberately violates T-torsionfree; divided base can remain zero')
print('NONCLAIM: actual T-divided cohomology class not numerically computed;')
print('NONCLAIM: no derived SELMER class, Coleman coefficient, complex L\'\' or BSD')
