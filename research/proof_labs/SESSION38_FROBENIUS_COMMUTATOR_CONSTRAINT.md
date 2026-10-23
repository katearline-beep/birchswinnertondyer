# Session38 — a necessary arithmetic commutator value for the first correction

2026-10-23, America/New_York. AI-assisted derivation and exact arithmetic,
not expert reviewed or a novelty claim. Baseline PR76 head
`fdf80d191f38d00ed65ec60ec309f2c936bbcb33`; main
`154eca9b6053c11e7b05f305219c313fcc628612`. Follow-up to issue61,
EX-018/LF-015 and C-0036. The experiment was recorded in those manifests
before the calculation. No original complex BSD implication: **NONE**.

## Result and the uncompleted target

For the actual residual Kummer class of **x=P2-2P1**, small-prime arithmetic
and the first cocycle equation force

\[
 \boxed{c_1([h,g])=9c_0(g)\ne0,\quad
 h=\mathrm{Frob}_{\mathfrak q_{23}}^{12},\quad
 g=\mathrm{Frob}_{\mathfrak q_{127}}^{10}.}
\]

This is a **necessary relation for every first correction that exists**,
not a table of evaluated global cochain values. It rules out any candidate
finite Galois realization that kills this commutator, in particular one
abelian over K(E[11]). It does not rule out the nonabelian kernel-V cover
of Session31, construct a supported solution, compare it with [10]Q,
or compute a second obstruction. The full PR76 success criterion is
**not met**; its permitted representation-information stopping rule applies.

## Objects, conventions and arithmetic witnesses (C-0050)

E=[1,-1,0,-79,289], K=Q(sqrt(-7)), V=E[11], and
Sigma consists of primes over2,11,117223 and infinity. On the short model
Y²=X³-1267X+17230, P1=(15,40), P2=(19,4).
Let omega=(1+sqrt(-7))/2. Fix arithmetic Frobenius and the C-0033
anticyclotomic character ell with omega=16 mod121 and generator12:

    ell((a+b*omega)) = log_12(((a+16b)/(a-15b))^10) mod11.

Use the **inverse** action rho(s)(1+T)^(-ell(s)) on V[T]/T² and
the commutator convention [h,g]=h g h^(-1) g^(-1).
The two degree-one primes are

    q23=(-5+2*omega),  sqrt(-7)=4 mod23;
    q127=(-11+6*omega), sqrt(-7)=45 mod127.

Their generator norms are23 and127. The computations give:

| prime | #E(Fq) | a_q | residual characteristic polynomial | order of rho(Frob) | ell(Frob) | ell(Frob^order) |
|---|---:|---:|---|---:|---:|---:|
| q23 |30|-6|X²+6X+1|12|2|2|
| q127 |143|-15|X²+4X+6=(X-1)(X-6)|10|4|7|

The first polynomial is irreducible over F11 (discriminant10);
the second has distinct roots1,6. Thus the companion-matrix order
calculation applies to the actual residual representation, without
constructing a global torsion basis or assuming its full image is GL2.
At23, A-I is invertible and sum_(j=0)^11 A^j=0.
At127, sum_(j=0)^9 A^j=10 times the projector onto its1-eigenspace.

The finite reduction calculation at127 gives

    T127=[13]P1=(20,115),  order(T127)=11,
    [13](P2-2P1)=2*T127 != O.

Here143=13*11 has11-adic valuation one. Consequently x is not
11-divisible in E(F127), so its unramified local Kummer class is nonzero.
**T127 is a reduction-point generator, not an evaluated c0(Frob) in a
chosen global basis.** No numerical identification between those objects
is made. That would need additional division-point arithmetic.

## Deduction from the first cochain equation

Let c0 be a Kummer cocycle for x. At these good primes,11 is invertible
and multiplication by11 is finite etale on the good model. Division of
the reduction point lifts over the maximal unramified extension by
Hensel lifting. Thus c0 is unramified there; its class is the local
unramified Kummer class in V/(A-I)V. The Kummer sequence over the finite
field injects E(Fq)/11 into H1(Fq,V). These standard good-reduction and
Kummer facts, together with C-0033's class-field identification, are the
mathematical inputs; Python does not prove them.

Choose embeddings of decomposition groups and lifts of the indicated
arithmetic Frobenii to G_(K,Sigma). For a cocycle,

    c0(F^m) = (1+A+...+A^(m-1))*c0(F).

Therefore h,g lie in N=ker(rho), c0(h)=0, and c0(g)!=0. The latter follows
because the norm operator at127 has kernel exactly (A-I)V and the local
Kummer class is nonzero. This proof does not identify its nonzero vector
with a finite reduction point. The conclusions hold for any choices of
the Frobenius lifts; embeddings change vector coordinates but not
nonvanishing or the stated vector relation.

Any first correction obeys

\[
c_1(st)=c_1(s)+\rho(s)c_1(t)-\ell(s)\rho(s)c_0(t).
\]

On N, rho is trivial. Expanding the four letters of the commutator,
using c0(s^(-1))=-c0(s) and
c1(s^(-1))=-c1(s)-ell(s)c0(s), gives

\[
c_1([h,g])=\ell(g)c_0(h)-\ell(h)c_0(g).
\]

Substituting the verified arithmetic gives -2*c0(g)=9*c0(g)!=0.
Unknown c1(h),c1(g) cancel. The commutator itself has rho=1, ell=0
and c0=0. Changing a first correction by an ordinary V-valued cocycle
does not change this value: on N that difference is a homomorphism,
so vanishes on [N,N]. Coboundary changes of the full B2 cocycle vanish
on the commutator too. Thus this necessary test survives the R ambiguity
and any later [10]Q normalization; it cannot choose that normalization.

For a finite Galois M/K through which rho, ell, c0 and c1 all factor,
K(E[11]) is contained in M. If M/K(E[11]) were abelian, the images of h,g
would commute, forcing c1([h,g])=c1(1)=0, contradiction. More generally,
reject any proposed quotient relation that makes these images commute.
This **does not** exclude successive class-field constructions over a
larger nonabelian base or show nonexistence on G_(K,Sigma). It strengthens
the specific product-quotient diagnostic of C-0036 with arithmetic primes
and a test independent of the full-GL2 and five-torsor degree deductions.

## Verification and source boundary

The [Python checker](frobenius_commutator_constraint.py) independently
counts points on the short and minimal models, computes the Kummer
projection using binary multiplication versus repeated minimal-model
addition, checks the character by finite discrete log and Fermat quotient,
and calculates Frobenius orders. It checks the norm/image kernel identity
on all121 vectors. The commutator identity is checked by group words and
separate3x3 matrix multiplication on all11^4 character/base-coordinate
inputs; all11^3 choices of the unknown correction coordinates and one
component of c0(g) are checked for the selected arithmetic inputs.

Controls: zero character and zero Kummer input give zero; reversing the
character convention or the commutator changes9 to2; a commuting quotient
falsely predicts zero. An optional [PARI oracle](pari_frobenius_commutator_constraint.gp)
uses ellcard/ellmul on the minimal model and certified ray-class Artin
coordinates calibrated once against omega. The same Python comparator
rejects changed, missing, duplicate or error-bearing output. The two
Python arithmetic paths share standard elliptic/Kummer facts; AI-written
code and a maintained library are not human mathematical review.

Sources: Milne, *Class Field Theory* v4.03, Chapter II Examples1.18,1.20
for crossed homomorphisms and powers,
https://www.jmilne.org/math/CourseNotes/CFT.pdf ; C-0033's audited
ring-class character and arithmetic-Frobenius calibration in
[Session30](SESSION30_ARITHMETIC_CHARACTER_LIFTS.md); C-0035's good
reduction/Kummer argument in [Session31](SESSION31_KUMMER_SATURATION_AND_LIFT_OBSTRUCTION.md).
The displayed commutator identity is derived here directly from the
cocycle equation. Lam–Liu–Sharifi–Wake–Wang, Theorem4.3.1,
https://wangjiuya.github.io/research/augmentation.pdf, requires an actual
proper defining system to identify the higher operation; it is not an
algorithm producing our arithmetic c1. No second-height theorem is applied.

Reproduce from repository root:

```sh
python3 -I -B research/proof_labs/frobenius_commutator_constraint.py
gp -q -f research/proof_labs/pari_frobenius_commutator_constraint.gp > /tmp/bsd-commutator38.txt 2>&1
python3 -I -B research/proof_labs/frobenius_commutator_constraint.py /tmp/bsd-commutator38.txt
```

Exact arithmetic only; no analytic truncation, random seed or precision
extrapolation. The script tests the finite calculations and algebraic
identities, not the arithmetic realization theorem.

## Decision

This supplies C-0050, an internally checked **necessary-condition
certificate with a source-dependent arithmetic deduction**, not a solved
embedding problem. Source specialization remains open to expert review.
No residual GL2 surjectivity, height comparison, Selmer upper bound or
Sha finiteness is used for the necessary relation. Existence of the
normalized supported Selmer lift still retains C-0045/46/49's assumptions.

The remaining concrete deliverable is a finite nonabelian realization
with evaluated rho, ell, c0 and c1, ramification confined to Sigma, and
local Greenberg cochains at both11-adic places and bad primes. Its first
acceptance check is the displayed commutator constraint; subsequent checks
must compare the chosen-v localization to [10]Q through an actual Shapiro
cochain map (up to a verified coboundary). No such arithmetic realization,
local map or correction table was produced in this sprint. Do not replace
them with the algebraic cover coordinates or extra local precision.

Local validation: all62 Python matrix commands passed on Python3.14.4 in56.03s, including all six harness validators/tests and the new checker. The separate direct-coordinate first-height oracle passed in135.29s. PARI is unavailable locally; its independent regeneration is required in the pull-request workflow before reporting oracle agreement. CI success is not mathematical peer review.
