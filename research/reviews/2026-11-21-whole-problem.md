# WPR-2026-11-21-01 — a bounded ORIGINAL Sha[2] implication, without a BSD rank bridge

**November 21, 2026, America/New_York · AI-assisted/unreviewed whole-problem checkpoint.** This is a new immutable journal, replacing the *current pointer only*; the November 20 dated review remains unchanged. Full audit of existing C-0001–C-0050 plus newly registered C-0051 and H1–H6.

## Original targets and nonclaims

General BSD is STILL UNSOLVED: for every E/Q, the algebraic rank must equal the order of vanishing of the original complex L(E,s); Sha finiteness and the full leading-term formula are additional substantial problems. Our test E=234446.a1, y²+xy=x³−x²−79x+289, has rational rank four, root sign+1, but **exact original complex L''(E,1)=0 has NOT been proved**. Proving it would force complex order≥4; rigorous nonzero L^(4)(E,1) would establish exact analytic rank four. Neither has been certified. Sha finiteness for E is NOT known, and neither is the exact leading coefficient. Our positive twist derivative and anticyclotomic p-adic derived classes concern different L-functions or cohomological invariants.

**What changed:** unlike the auxiliary torsion-field class-group and conditional height projects, Session53 gives a reproducible **direct theorem about the ORIGINAL curve's arithmetic BSD invariant at the prime2**:
- Four actual rational points on E have 4×4 mod11 Kummer reduction matrix determinant5 at q2843,3019,5147,5737; an independent exact good-prime count #E(F3)=7 kills rational 2 and11 torsion. This establishes rank E(Q)≥4 without importing the database's rank4.
- **Two maintained arithmetic libraries** called in the pinned Sage10.6 environment return **dim_F2 Sel2(E/Q)=4**, independently: PARI and eclib/mwrank. Actual GitHub Actions logs on source commit cdae3ed5eb6dd69c52e7de401fbbdf557289b896, run44926513944/job136913681055, show the exact four reduction rows and both Selmer results. Two further independently scheduled true Sage jobs 44926218323/job136912780575 and 44926199989/job136912724697 both gave dim4, with negative controls 389a1 rank2/Sel2=2 and 571a1 rank0/Sel2=2.
- The standard exact sequence 0→E(Q)/2E(Q)→Sel2(E/Q)→Sha(E/Q)[2]→0 then proves **rank E(Q)=4 and Sha(E/Q)[2]=0**, hence Sha(E/Q)[2^\infty]=0. An honest *original-curve arithmetic BSD-component implication* using accepted descent algorithms; not novel unless a prior-art audit says so (likely classically computable), not human-peer-reviewed, and not general BSD.

The 2-Selmer numerical output is an exact algorithmic Selmer group dimension, NOT the analytic Sha≈1 rounded in LMFDB. The published Selmer exact sequence—not any heuristic BSD leading term—supplies the deduction. This entire new assertion is C-0051, explicitly typed as internally independently implemented *computational certificate plus theorem deduction*. DO NOT mark general BSD proved, original Sha finite, original complex analytic rank four or expert review.

## What remains hardest: the typed logical gap to complex L''

We still have **NO characteristic-zero theorem** producing exact L'''(E/K,1)=0 for K=Q(sqrt(-7)), which via L(E/K,s)=L(E,s)L(E^{-7},s) and the nonzero twist derivative would imply original complex L''(E,1)=0. Bockstein, Massey, Kummer radicands, derived 11-adic heights, Ulmer positive-characteristic surface rank results and p-adic L-series are different objects; no source-validated bridge converts them into this complex derivative identity. No conditional universal claim, no numerical-vanishing claim, and no hidden use of Sha finiteness should be promoted.

## Full H1–H6 adversarial ranking and decision

- **H1 derived Kato/Iwasawa corrections — active limited.** Session46 certified actual finite joint Kummer image, Sessions49–50 formulated exact second global Bockstein and two fine-dual detectors, Sessions51–52 constructed local roots and an auxiliary unramified class-field quotient. No actual supported global normalized first Galois cochain c1 or Greenberg local homotopies. Missing complex reciprocity remains. Next test only when a concrete non-split order121 corrected extension is proposed; verify two Frobenius commutators and both v|11 Greenberg maps, otherwise pause.
- **H2 derived Selmer height — active limited.** Existing known fine tests Z1,Z2 annihilate the first height of R, but no real secondary Bockstein pairing D1,D2 is computed. The new Sha[2] certificate does not evaluate 11-primary Selmer higher height. Next: require actual globally evaluated c1 and true compact-support cochain before evaluating h2. A synthetic group nonzero obstruction does not suffice.
- **H3 complex geometric comparison — active prioritized.** No published exact rank-four third-complex-derivative comparison applied. Liu's November 2026 geometric generating-function result gives first derivatives in a different output type. The source theorem from rank-two Kato cannot force analytic rank four. Next: look for literal characteristic-zero complex L'''(E/K,1) comparison with an exact algebraic higher cycle; no speculative identity without a rank-two falsifier.
- **H4 Mazur–Tate integral finite-layer conjectures — parked.** C0008 integral trace falsifier: mod11 high augmentation vanishing can mask integral augmentation11. No actual two-layer cohomological bridge to original complex order. Remain parked.
- **H5 complex L-function numerics — diagnostic only.** Original L'' numerically tiny, L^(4) apparently positive, analytic Sha≈1; no exact zero. Next numerical activity only if a rigorous contour/functional equation method can prove equality and supplies certified error-zero bound, not merely more digits.
- **H6 period/motive cross-field analogies — parked speculative.** Ulmer's characteristic-p high-rank BSD and Fermat-surface zeta factors do not transfer to original characteristic-zero complex L(E,s). Need an actual cycle map yielding a literal complex analytic derivative identity.

**Arithmetic opportunity outside H1–H6:** immediately prioritize a full **original 11-Selmer upper bound** instead of further class-group computations. Session35/C0044 nonzero exact twist Kurihara number proves (under stated source assumptions) dim Sel11(E^{-7}/Q)=1. Quadratic splitting gives dim Sel11(E/K)=dim Sel11(E/Q)+1. There is NO upper bound for original Sel11 from this identity. A genuine dim Sel11(E/Q)≤4 certificate would prove original Sha[11^\infty]=0 and extend C0051 to another prime, but this is a new, high-cost **11-descent** obligation; it is NOT achieved by the Sage 2-Selmer API, the 11^6 auxiliary class field, or numerical Sha≈1. Park attempts until the exact global+local full 11-Selmer enumeration/dual upper-bound construction is specified.

## Explicit adversarial stress tests

1. **571a1** has rank0 but actual Sel2 dimension2 (Sha[2] nonzero). The Sage producer verified it in PARI and eclib; if someone mistakes a rank computation for Selmer, this control catches it. 389a1 rank2/Sel2=2 is a second independent control.
2. A *putative* four-dimensional 2-Selmer group alone does not prove rank4, since Sha[2] might occupy its dimensions. The genuine four-prime independent rational-point reduction matrix separately proves rank≥4, and #E(F3)=7 rules out rational 2/11 torsion. If the mod11 determinant were zero, the lower-bound proof would fail. A duplicated row and a mutated residue entry are forced to fail in the verifier.
3. C0044 twist 11-Selmer=1 does NOT bound original positive 11-Selmer. Mod-11 local fine Kummer and the source field class group quotient are *lower-dimensional witnesses*, never upper-Selmer completeness.
4. Claim C0051 cannot change status_flags.Sha_finiteness_for_E_proved from false: showing the 2-primary torsion vanishes does not prove odd-primary components finite or trivial.
5. No script or AI review certifies original complex L''=0. All source output types are kept separate.

## Theorem-first selection, stop rule and next due

- **Safe lemma actually completed:** standard Kummer Selmer exact sequence + independent rank≥4 reduction certificate + actual complete Sel2 upper4 gives original rank4 and Sha[2^\infty]=0. No priority claim or peer review claimed.
- **Credible leapfrog:** an *actual* full original 11-Selmer upper4 via a fully documented 11-descent/dual bound; the twist certificate may help via quadratic decomposition only after a positive upper bound is proved. Explicit C0044 source dependency preserved.
- **Wild alternative:** prove a characteristic-zero complex triple derivative formula over K with the correct motivic/cohomological objects; derive original L''=0 and test against rank-two counterexamples.
- **Kill rule:** no new subgroup-size, local extra digits, numerical Sha rounding or Dainobu class field extension will be promoted as an original BSD claim unless it produces an exact original Selmer **upper** bound or an original complex derivative theorem.
- **Next review due:** November 27, 2026. No historical snapshot overwritten; WPR-2026-11-20-01 stays unchanged.

## Provenance and review state

Original source scripts:
- research/proof_labs/session53_independent_rank4_reductions.py
- research/proof_labs/sage_original_sha2_descent_gate.py
- research/proof_labs/SESSION53_ORIGINAL_SHA2_SELMER_PROOF_GATE.md
- research/proof_labs/SESSION35_SPARSE_KURIHARA_COMPUTATION.md (twist 11 only)
- research/proof_labs/SESSION52_FINE_UNRAMIFIED_CLASSGROUP_QUOTIENT.md (auxiliary)
- research/strategy/THEOREM_FIRST_PIVOT_2026-10-19.md
- Previous independent WPR-2026-11-20-01 in research/reviews/2026-11-20-whole-problem.md
- Sage 10.6 documented full Selmer API: https://passagemath.org/docs/10.6/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html
- Cremona/LMFDB cross-check: https://www.lmfdb.org/EllipticCurve/Q/234446/a/1

Previous review's C-series 50 claims were *not* re-proved by this checkpoint. Claim-by-claim typed status remained as recorded in the prior claim ledger, with C0051 added only as **internally reproduced, unreviewed computational certificate**. The WPR does not change mathematical truth or upgrade independent review. No merges authorized.
