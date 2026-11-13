# WPR-2026-11-13-01 — independent-minded whole-problem BSD review

**Friday 2026-11-13, America/New_York.** AI-assisted, not human expert reviewed. Baseline: repository main still last merged PR #75 (2026-10-22); open stacked PRs #76–#80 checked on 2026-11-13. Previous immutable review: [WPR-2026-11-06-01](2026-11-06-whole-problem.md). This review is proposed atop PR #80; no merge or theorem promotion. Next due **2026-11-20**.

## General conjecture and focal example

For every elliptic curve E/Q, BSD predicts (i) `ord_{s=1} L(E,s)=rank E(Q)=r`; (ii) finiteness of Sha(E/Q); (iii) the normalized leading term `L^(r)(E,1)/r! = Omega_E Reg(E/Q) |Sha(E/Q)| product_l c_l / |E(Q)_tors|^2`, with compatible period and regulator conventions. Rank equality does not prove Sha finiteness or the leading coefficient.

For the focal rank-four curve `E:y²+xy=x³−x²−79x+289` (234446.a1, root number +1), the original **complex** equality `L''(E,1)=0` is unproved. Exact analytic order four further requires `L^(4)(E,1) != 0` proved rigorously. Its original Sha finiteness and leading-coefficient identity are open. Twist `L'(E^-7,1)`, p-adic heights, Kato norms and function-field L-functions are different mathematical objects.

**NEW PROVED IMPLICATION TOWARD BSD SINCE NOVEMBER 6: NONE.** No new arithmetic result merged. No original complex comparison, evaluated supported first cochain, second Bockstein, Sha finiteness or fourth-derivative certificate was obtained.

## All C-series claims (C-0001–C-0050)

All 50 canonical IDs were inspected in the prior full ledger and retained in the machine-readable audit. Their evidence/status categories remain:
- **0001–0009:** exact local 11-adic and Selmer decompositions; twist derivative enclosures conditional on analytic identities; original complex L'' only numerical. Finite cyclotomic trace counterexample prevents false integral-filtration promotions.
- **0010–0014:** exact character/denominator/sigma arithmetic and conditional first global anticyclotomic height residues; no independently certified global height or h².
- **0015–0019:** Castella–Hsieh rank-two theorem-scope no-go, Ulmer characteristic-p theorem and corrected Fp(t) ranks 2,3,7 (geometric 3,7,25), exact Jacobi/Fermat controls; no number-field complex theorem.
- **0020–0028:** Howard/Heegner published tower construction and source-dependent norm-divided classes; base Heegner torsion and universal-norm regulator no-go; no higher Coleman orders or complex comparison.
- **0029–0041:** provisional first-height/complex twist corroboration, ray layers, five division torsors, saturation and conditional global/support obstruction; no actual nonabelian global cochain.
- **0042–0049:** exact twist Kurihara certificate and local norm reference; conditional signed global first-lift existence, normalization and local comparison; no evaluated supported cocycle or second obstruction.
- **0050:** unmerged source-dependent Frobenius commutator necessary condition; neither a constructed correction nor a second lift.
No ledger entry is upgraded. Historical corrections (Ulmer field of definition, sigma digits, denominator ideal, first/second Bockstein, Howard base vs tower, and CH rank-two scope) remain operative. Exact computations, conditional published results, numerical/provisional certificates, literature no-go findings, and infrastructure are separate classes.

## New source-level audit and substantive correction to PR #80

Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, J. Math. Soc. Japan 76 (2024), 855–919, [publisher DOI](https://doi.org/10.2969/jmsj/90699069), [full text](https://nms.kcl.ac.uk/david.burns/web_page/katozeta.pdf), Theorem 1.3 states a **cohomological Kato zeta-norm augmentation containment** (Conjecture 1.1(i)), assuming p>3, **both** `Sha(E/F)[p∞]` and `Sha(E/Q)[p∞]` finite, full integral Galois image containing SL2(Zp), and absence of p-torsion in E(Q_l) for all l in S. The previous PR #80 note explicitly named Sha(E/F) but **omitted Sha(E/Q)** in its hypothesis list: this review corrects that omission. Neither finiteness condition is established for the focal rank-four curve. Even if all hypotheses were met, the theorem's output would be the **Kato cohomological norm**, not the original complex L'' vanishing. The higher complex comparison appears in the generalized Perrin–Riou **Conjecture 1.1(iii)**. Proposition 6.1 concerns a p-adic L-function. Moreover F is a finite **real abelian** extension, not the imaginary anticyclotomic K=-7. This is a rigorous source-scope blocker, not a proof that no other theorem exists.

Burns–Kurihara–Sano, *On derivatives of Kato's Euler system and the Mazur–Tate conjecture*, IMRN 2025(4), rnaf012, DOI 10.1093/imrn/rnaf012, gives unconditional evidence for positive-rank Mazur–Tate congruences, **not** a proved original complex rank-four implication. Castella–Hsieh (2022) Theorem A is rank-two scoped; Kim's higher Gross–Zagier (2026) concerns Kolyvagin systems; Sano/Macias Castillo–Sano are p-adic derived-height machinery; Ulmer is characteristic p. October 2026 low-Selmer-corank preprints, regardless of eventual validity, have corank<=1 assumptions excluded by algebraic rank four via Kummer injection.

## H1–H6 decisions and typed missing arrows

| Track | Allocation | Evidence, obstruction and kill criterion |
|---|---:|---|
| H1 derived Kato / supported global correction | 35% | C-0044–50 exact finite and conditional first-lift inputs; actual nonabelian arithmetic Galois quotient, cochain and local Greenberg homotopies missing. BKS source audit confirms cohomological augmentation != complex vanishing. Kill candidate if any relator/Frobenius/local support fails. |
| H2 mixed heights / second Bockstein | 15% | Provisional first heights and conditional first lifts, no evaluated second h². Reject mismatched local conditions or use of universal-norm radical as nonzero regulator. |
| H3 characteristic-zero quadratic geometry | 45% | Product identity `L'''(E/K,1)=3L''(E,1)L'(E^-7,1)` under lower-order vanishings has correct output type; no proved third complex derivative vanishing. Reject parity-only and function-field substitutions; search for genuine cycle formula. |
| H4 Mazur–Tate | 0% parked | BKS 2025 unconditional congruence evidence does not supply original complex comparison; restart only with noncircular exact map. |
| H5 numerical diagnostics | 5% | Twist enclosure useful, tiny original L'' remains only heuristic; do not spend precision without a theorem. |
| H6 period projector | 0% parked | No constructed period projector or complex derivative identity; parity-only rank-two controls fail. |

**Safe lemma:** source-verify the complete BKS Theorem 1.3 hypotheses (including BOTH Sha groups) and map every output to its exact coefficient ring; this is now a documented no-go for the focal complex claim.

**Credible leapfrog:** construct a small *actual* nonabelian arithmetic Galois quotient and normalized supported first correction for x=P2−2P1, evaluate all relations, Frobenius 23/127, ramification and Greenberg restrictions, and match the [10]Q Shapiro reference. **Falsifier:** any failed relator, wrong Frobenius commutator, or missing local map stops the candidate before a second Bockstein.

**Wild alternative:** a characteristic-zero higher Gross–Zagier/cycle theorem whose literal output is `L'''(E/K,1)` and whose vanishing follows from an independently proved geometric mechanism. Demand an exact theorem and no assumed BSD input.

**Selected next decisive task:** H3 source-theorem search for a characteristic-zero *third complex derivative* vanishing mechanism, with full hypotheses; parallel H1 only if a finite quotient can be arithmetically realized without unmotivated giant splitting fields. Deprioritize extra p-adic digits, brute-force huge torsors, numerical L'' precision and formal rank-parity arguments.

## Adversarial negative control, run result and limits

The new `research/reviews/controls/bks_integral_complex_nonimplication_2026_11_13.py` checks the exact integral cyclic-11 trace `sum_{k=0}^{10}(1+T)^k`: augmentation is **11**, although modulo 11 it is `T^10`. Therefore a mod-11 deep-augmentation appearance cannot imply integral I-divisibility. A separate formal countermodel fixes a zero cohomological graded symbol while allowing a nonzero independent complex quadratic coefficient; without a proven comparison arrow, the latter is unconstrained. Both tests ran successfully in an independent Python session on 2026-11-13. **Neither is an actual elliptic curve or a Kato-class computation.** This test rejects the logical shortcut, not the source theorem.

Required repository checks: `python3 -I -B research/harness/validate.py`, `test_validate.py`, `validate_leapfrogs.py`, `test_leapfrogs.py`, `validate_full_review.py`, `test_full_review.py` and existing math tests. Full checkout was blocked by DNS resolution in the run environment; the GitHub PR's CI must run them. Do not assert green CI without inspection.

## GitHub provenance and blockers

On 2026-11-13, inspected PRs #76–#80: all **open**, stacked; main last merged #75 on 2026-10-22. Open issues #61, #53, #49, #42, #41, #32, #25, #23, #22, #21, #20, #19, #18, #15, #11, #8, #6, #5, #4, #3 were listed. No new claim or issue was closed. The present PR remains unmerged and cannot be landed ahead of its dependency stack. No independent mathematical expert has reviewed the new source-hypothesis correction. The principal mathematical blocker remains the absent noncircular original complex L'' comparison; the immediate engineering blocker is the unmerged five-PR stack and unavailable local full checkout.

**Verdict: NONE proved toward BSD.** The real gain is a corrected published-theorem hypothesis audit and an exact anti-vacuity test, not a mathematical breakthrough.
