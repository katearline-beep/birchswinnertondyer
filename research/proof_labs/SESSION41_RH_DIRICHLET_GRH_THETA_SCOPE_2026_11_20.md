# Session 41 — RH / Dirichlet-GRH theta-chain transfer gate (2026-11-20)

**AI-assisted source-scope investigation, not independent expert review; no new proved implication toward BSD.** Base: November 20 WPR PR #82. Do not alter the dated November 20 WPR snapshot or claim ledger. This is a bounded H3/LF-003 source audit with an exact formal-function negative control, *not* proof that the announced RH argument transfers to elliptic curves.

## Actual target and dependency graph

General BSD for every elliptic curve E/Q requires (i) rank E(Q)=ord_(s=1)L(E,s), (ii) finite Sha(E/Q), (iii) the period/regulator/Tamagawa/torsion/Sha normalized leading coefficient. Our 234446.a1 has known algebraic rank 4, but **exact original complex** L''(E,1)=0, L^(4)(E,1)≠0, Sha finiteness, and the BSD coefficient remain open.

Existing H3 route: for K=Q(sqrt(-7)) and E^(-7), the **complex** base-change factorization
L(E/K,s)=L(E,s)L(E^(-7),s)
implies, assuming the already established lower vanishing L(E,1)=L'(E,1)=0 and odd-twist central vanishing,
L'''(E/K,1)=3 L''(E,1) L'(E^(-7),1).
The twist's nonzero first derivative is currently a provisional, assumption-dependent computational certificate; the **missing arrow** is an unconditional theorem forcing the **third complex derivative on the left** to vanish independently. A first-derivative, an Eisenstein-series derivative, a p-adic derivative, or an RH-style zero-free region is not a substitute.

## Newly reported external result, rigorously typed

Levent Alpöge, 2026-11-20 announcement: https://alpo.ge/remark.pdf, original publication and 14-part Lean archive. The author credits collaboration with Claude; reports RH and Dirichlet GRH, with a proposed mechanism from Stepanov-style divisors, chains of theta lifts and a chain length about sqrt(X). **The four-page announcement alone is not a derivation of this mechanism or evidence of an elliptic theorem.**

Andrew Sutherland (MIT), https://math.mit.edu/~drew/grh/, report updated **2026-11-20 22:05 UTC**: all 175,187 Lean modules compile in v4.33.1; the five final declarations use only propext, Classical.choice, Quot.sound; every module passes leanchecker replay; nanoda and con-leche accept the export; con-leche --compare accepts all five theorem statements. Independent LUMI build (https://github.com/aapolipponen/rh-lean-check-lumi) corroborates the build and byte-equal Main.olean. This is **strong independent evidence of formal checking of the stated results**; some further comparator/Lean replay runs were ongoing at the time reported. We did not download/rebuild the 239MB archive or independently run any Lean kernel ourselves. Distinguish software proof checking from human understanding of a vast new argument.

**Critical scope:** Mathlib's RiemannHypothesis addresses riemannZeta(s), and the extra final theorems address Dirichlet L(s,chi), *not* Hasse–Weil L(E,s), its derivatives, or even all automorphic GL2 L-functions. In particular the author explicitly describes *Extended RH* as possible future work, not a completed result. Do not use Dirichlet GRH to assume Dedekind or Artin GRH for the nonabelian Kummer quotient in H1; effective Chebotarev under relevant Dedekind/Artin hypotheses would require separate theorems.

Independent *AI-assisted* (not expert-refereed) guide to the Lean source, https://github.com/aapolipponen/rh-lean-check-lumi/blob/main/docs/02-proof-map.md, describes:
- top analytic output: Dirichlet zero-free half-plane Re(s)>1/2, reached from arithmetic Gm-window bounds;
- inputs: automorphic theta chains, Hermitian slope and congruence bounds, Galois representations and Tate-twist Galois cohomology;
- the displayed Sha^1 terms are groups for coefficients Q_l/Z_l(-e) over abelian CM extensions, **not** Sha(E/Q) with elliptic E[p^infty] coefficients. Similar notation is not a map or comparison theorem;
- the guide itself warns that many mathematical bridges remain unread and its content descriptions derive from AI source reviews. We do **not** treat its inferred proof map as an independently checked published source theorem.

## Source-matched theta results / transfers, with explicit typed outputs

1. **Classical Rallis inner-product formula:** Petersson norms of global theta lifts relate to *central values* of suitable automorphic L-functions, with local factors and theta nonvanishing hypotheses (e.g. Gan, Automorphic Forms and Theta Correspondence, https://swc-math.github.io/aws/2022/2022GanNotes.pdf). The output is a *value*, not the third complex base-change derivative of E.
2. **Arithmetic theta / Kudla–Rapoport style formulas:** geometric height pairings can equal *first central derivatives* of certain convolution L-functions (Bruinier–Howard–Yang, https://arxiv.org/abs/1303.0549; Kudla–Rapoport–Yang overview https://arxiv.org/abs/math/0308296). Output is first derivative of a source-specific L-function, not L'''(E/K,1) for our weight-two E. Some higher Siegel–Weil results give higher derivatives of *Eisenstein series*, which again is a different analytic object.
3. **New RH theta-chain mechanism:** an unreviewed technique described in the announcement and an AI-generated proof map, not a cited theorem that produces a central L-derivative from Mordell–Weil points. Mapping the construction to the GL2 cusp representation pi_E would need a new stated functor, local data at conductor 234446 and 11, and actual derivative-output identification.

**GO/NO-GO:** A proposed transplant must produce, with independently verified hypotheses, a *characteristic-zero complex* identity
   A(E,K) = c(E,K) L'''(E/K,1),
with c(E,K)≠0, an arithmetic-geometric argument independently proving A(E,K)=0 from established rank-four inputs, and a separately proved map showing this is the Hasse–Weil L-function of pi_E/base change. It must not assume BSD, a rank-four analytic vanishing, or Sha finiteness as an unproved input. Without that chain of arrows, it is **NOT** an H3 breakthrough.

## New strict negative control: even elliptic-style GRH would not settle multiplicity

Let t=s-1 and phi(t)=sinh(t)/t, phi(0)=1. The functions
  F2(s)=t^2 phi(t), F4(s)=t^4 phi(t), G(s)=t phi(t)
are real entire of order 1. Their functional equations have signs +,+,- under s→2-s. Zeros of phi are precisely i*pi*n for n∈Z\{0}; the remaining central zeros are t=0 of order 2, 4, and 1. **Every zero of every function lies on the central line Re(s)=1**. Nevertheless:
  F2''(1)=2, F4''(1)=0, G'(1)=1,
  (F2 G)'''(1)=6, (F4 G)'''(1)=0.
Thus **even critical-line location for the very L-function being studied, plus exact functional-equation symmetry, does not force the central zero multiplicity**. This strict formal-function negative control strengthens Nov 6's parity-only test and does not purport to model Euler products, elliptic curves, or modularity. In particular the theorem of Dirichlet GRH is *weaker in relevance* than the fictitious elliptic zero-location hypothesis tested here.

Run the finite exact coefficient checks: 
  python3 -I -B research/reviews/controls/rh_dirichlet_grh_multiplicity_negative_control_2026_11_20.py

The script checks rational Taylor jets by independent convolution and Leibniz calculations, and asserts the wrong vanishing shortcut fails. Its finite computation does **not** certify the global zero location; that assertion follows by the elementary zero set of sinh(t).

## Portfolio and next decisive test

Keep H1 40%, H2 15%, H3 40%, H5 5%, H4/H6 parked as in WPR Nov20; allocate a **bounded H3 source-read only**, not a seventh undisciplined moonshot. Safe lemma: rigorously disambiguate the RH proof's exact Sha^1 coefficient module and GRH quantifiers against elliptic Sha and GL2. Credible leapfrog: find a source-defined arithmetic theta lift attached to pi_E over K whose literal output is L'''(E/K,1), with independently proved zero. Wild alternative: adapt iterated theta chains to the *central Taylor multiplicity* of automorphic GL2 L-functions, not just off-center zero-free regions; record a genuine arithmetic multiplicity comparison and falsify it at analytic rank two.

**Selected cheapest decisive next test:** inspect an explicit arithmetic theta inner-product theorem at weight 2 and K=-7; create a theorem/hypothesis/output table checking exact analytic derivative **order and L-function identity**. If only central values/first derivatives or Eisenstein higher derivatives occur, mark the transplant NO-GO, refocus H1 arithmetic quotient and H3 existing complex geometry. No large Lean download, no massive new Galois field, no new p-adic digits, no alteration of any C-series status. Nothing here proves original complex L''=0, a second derived height, Sha finiteness, or the general BSD conjecture.

## Reproduction/provenance

Local isolated CPython 3 exact-rational script run 2026-11-20: PASS (the output is recorded in session transcript, not a trusted independent audit). This is an exact formal-coefficient check, not independent peer review. New draft branch is stacked on PR #82; no merge authorized. The existing WPR Nov20 immutable snapshot and current.json are intentionally not modified within the same checkpoint.


## Primary theorem spot-check completed after the initial audit

Li–Liu, *Chow groups and L-derivatives of automorphic motives for unitary groups, II* (Forum of Mathematics, Pi), **Theorem 1.5(1)**: https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/chow-groups-and-lderivatives-of-automorphic-motives-for-unitary-groups-ii/09D1312B3B0BE1F60B5146CEBC6216DF. The printed identity is a normalized arithmetic theta-lift **height pairing** equal to a nonzero normalizing factor times **L'(1/2,pi)** and local doubling integrals; its hypotheses explicitly include **Hypothesis 4.11** (modularity of special-cycle generating functions), along with the parity, local/representation and other conditions in Assumption 1.3 and the stated paper. **Remark 1.6(2)** compares the ordinary Rallis identity whose output is **L(1/2,pi)**, not L'. The paper says the arithmetic inner-product formula is *conditional* on that modularity hypothesis in its stated generality. We have **not** checked a specialization to the focal weight-two pi_E, K=-7, and do not assert one exists. **Go/no-go result:** this concrete theorem's literal output is the **FIRST derivative of a specific automorphic L-function**, not the **THIRD derivative of original complex L(E/K,s)**; even complete applicability would not deliver H3's missing arrow.

That is a sharper, theorem-numbered negative result than citing the source's abstract alone. Remaining test: look for an independently established third-derivative extension with exact L(E/K,s) and hypotheses, not a restatement of the above first-derivative identity.
