# Session47 — five independent finite-quotient cup obstructions, at least four killed by supported inflation

**2026-11-20, America/New_York · AI-assisted exact group-cohomology deduction, not independently expert reviewed.** Stacked on Session46 / draft PR #88. No new implication toward original complex L''(234446.a1,1), nonvanishing of its fourth derivative, Sha finiteness, full BSD leading coefficient or the general BSD conjecture: **NONE**. This addresses the H1 obstruction and the precise limits of the finite-quotient no-go in C-0036 using an actual arithmetically certified residual quotient.

## Question, objects, and pre-existing conditions

**Question:** Does Session46's unconditional-with-respect-to-full-GL2 *actual* base quotient let us measure how many independent first-Bockstein obstructions are present on the finite product quotient, and how many are killed when passing to the supported arithmetic Galois group? Demand exact typed inflation and do not equate its kernel with elliptic Sha.

Let K=Q(sqrt(-7)), V=E[11], L=K(E[11]), D1 the actual first anticyclotomic layer, F5=L([11]^-1P1,...,[11]^-1P4,[11]^-1R), Σ the primes above 2,11,117223 and infinity, and B5=F5D1. Session46 uses 5 actual good split Frobenius signatures, q23 irreducibility and C0033's class-field normalization to prove
  **G0=Gal(B5/L)≅V^5×C11**,
without assuming full rho(G_K)=GL2(F11).

Write G_{L,Σ_L}=Gal(L_Σ/L), where Σ_L are primes of L over Σ. Since the five division torsors and D1 are unramified away from Σ_L, the natural surjection
  q:G_{L,Σ_L}↠G0
exists. Here V is a TRIVIAL G0-module (L contains E[11]). Let c_i:G0→V be the i-th Kummer translation coordinate and ell:G0→F11 the C11 character. The coefficient sequence for the **inverse** first jet is 0→V*T→V[T]/T²→V→0 with action (1+T)^(-ell) restricted to G_L.

## Exact nonzero and independent cup classes on the ACTUAL finite quotient

For each of the five points X_i define the normalized 2-cocycle
  alpha_i(g,h)= -ell(g)*c_i(h)  ∈ V.
It is the boundary of c_i under the inverse first-jet coefficient sequence. This equation is typed: both actions on the outer V are trivial, and alpha_i is an F11-bilinear cross-cup product.

**Lemma (unconditional finite group theory once G0 is certified):** The five classes
  [alpha_1],...,[alpha_5] ∈ H²(G0,V)
are F11-linearly INDEPENDENT, so their span has dimension five.

**Proof:** G0=V^5×C11 is abelian. Any 2-coboundary for trivial V coefficients has the form (df)(g,h)=f(g)+f(h)−f(gh), and is SYMMETRIC in (g,h). Let t=(0,1) be the pure character generator and, for each i and fixed u∈V nonzero, let z_i(u) be the pure Kummer translation supported in the i-th V-coordinate. Then
  alpha_j(t,z_i(u))−alpha_j(z_i(u),t) = −delta_ij*u.
If a linear combination of [alpha_j] were zero, its representing 2-cocycle would be a coboundary and hence have zero antisymmetric part. Evaluating on the five pairs forces every scalar coefficient to be zero. This is independent of an actual first-correction cocycle or of the residual full-GL2 image.

The five-point field data are essential: on the insufficient product quotient the first obstruction classes are genuinely NONZERO; one may not identify this nonzero finite H² with a supported arithmetic obstruction before checking inflation.

## The supported-inflation statement: dimension at least four, CONDITIONAL on C-0044/46/47

For i=1,2,3,4, the point P_i∈E(Q) has positive complex-conjugation sign. Under the recorded **C0044 residual negative-Selmer-line and C0046/47 signed global duality hypotheses**, Session36 deduces H²(G_{K,Σ},T_11E)^−=0 and **existence of a first global supported B2 lift** for each Kummer κ(P_i), with B2=T_11E⊗Z11[[T]]/(T²). Reduce modulo11 and restrict to G_{L,Σ_L}. The resultant 1-cocycle c_{i,0}+T c_{i,1} has residual c_{i,0}=c_i∘q (up to a coboundary; on G_L residual coboundaries vanish because rho=1). Its first-order cocycle equation gives
  dc_{i,1} = ell ∪ c_{i,0},
or, with the boundary sign convention, the inflation q*[alpha_i] is zero in H²(G_{L,Σ_L},V).

Since the [alpha_i] are independent for all five i, this proves the **source-dependent arithmetic inequality**
\[
\boxed{
 \dim_{\mathbf F_{11}}\ker\left(
   H^2(G_0,V)\xrightarrow{\mathrm{inf}}
   H^2(G_{L,\Sigma_L},V)
 \right)\ge 4.
}
\]
No complete description of that kernel, finite or global Selmer rank, Sha finiteness, or original complex BSD is asserted.

**IMPORTANT fifth R nuance:** R has negative complex-conjugation sign. C0040's first supported obstruction for R is conditionally nonzero in H²(G_{K,Σ},V); restriction to G_{L,Σ_L} could nevertheless kill it. Therefore do NOT claim that [alpha_5] survives the above inflation, and do NOT infer the kernel has dimension exactly four. The data only force *at least* four. One can consistently have either [alpha_5] in or out of the kernel after restriction, without contradicting the stated source inputs.

**Unrestricted variant, separately conditional:** C0037 (Session32) constructs unrestricted residual T³ lifts on the absolute G_K with unspecified auxiliary ramification, under its separate residual-image/local hypotheses. Restriction to absolute G_L then kills all five alpha_i. This does not make alpha_5 vanish over the FIXED-support G_{L,Σ_L}. It is precisely the distinction between enlarging support and solving the supported Greenberg problem; do not conflate the two H² targets.

## Why this matters for H1

C0036 showed a finite product quotient cannot carry a first lift; C0047 conditionally gives global first H¹ lifts for positive classes. Session46 has now independently certified the entire **actual** product base quotient G0, rather than an unsupported abstract example. The five alpha_i classes make the contradiction *quantitative*: at least four independent finite obstructions must disappear under supported inflation, not because the five finite cocycles were miscomputed, but because the Galois extension needed to represent c1 is genuinely larger and nonabelian.

A candidate central 121-kernel first extension over B_x for a positive residual x must realize the appropriate transgression class so that this inflation vanishes. An arbitrary abelian refinement of B_x or a rank-one numerical height calculation cannot do so. The fact that [alpha_i] are independent does not exhibit the radicands, a global corrected c1, ordinary Greenberg local cochains, Shapiro references, or a second Selmer height. Those are still the decisive deliverables.

## Independent exact negative controls and reproduction

New finite-field cohomology script:
  python3 -I -B research/proof_labs/session47_finite_cup_inflation_controls.py

It checks the 2-cocycle identity on an independent deterministic set of triples in V^5×C11; verifies that antisymmetric commutator evaluations form a 5×5 invertible matrix with all 5 independent source directions; tests that replacing a point coordinate by the sum of two others makes a *dependent* fifth cup class, and that making ell=0 erases every cup obstruction. A separate toy linear map with first four generators in the kernel and fifth possibly in/out verifies that the lower bound does not authorize an exact kernel dimension. This is **finite algebra only**; the arithmetic supported-inflation inequality uses C0047's source-dependent global existence theorem, not passing Python code.

Provenance: C0033 (actual ray-class character), C0035/36 (finite Kummer/quotient), Session46 (five pure Frobenius arithmetic and full relative group), C0044/46/47 (signed global first-lift existence), C0037 (absolute unrestricted-lift scope), C0040 (R obstruction, with source/height assumptions). No new external published theorem is claimed, no C-series status is promoted, and the historical immutable weekly WPR is untouched.

**Next decisive H1 test:** produce the actual degree-121 central arithmetic extension M2/B_x that kills the relevant nonzero alpha_x under inflation, with a verified 11th-root Kummer radical module, power and commutator relations, fixed support and BOTH ordinary 11-adic Greenberg maps. Then evaluate a normalized c1, compare with C0049's Shapiro local reference, and only afterward attempt T³/second Bockstein. Keep H3 characteristic-zero exact complex comparison separately active. **New implication toward BSD: none.**
