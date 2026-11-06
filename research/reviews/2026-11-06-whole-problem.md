# WPR-2026-11-06-01 — immutable weekly whole-problem BSD review

**Friday 2026-11-06, America/New_York.** AI-assisted, **not independent expert review**. Prior review: [WPR-2026-10-30-01](2026-10-30-whole-problem.md). Main remains commit `154eca9b6053c11e7b05f305219c313fcc628612` (PR #75 merged 2026-10-22). PRs [#76](https://github.com/katearline-beep/birchswinnertondyer/pull/76), [#77](https://github.com/katearline-beep/birchswinnertondyer/pull/77), [#78](https://github.com/katearline-beep/birchswinnertondyer/pull/78) remain OPEN, stacked in that order. Inspected GitHub PR/issue and main commit listings on 2026-11-06. This new review is stacked on #78; do not merge out of order. Next due **2026-11-13**.

## Full conjecture versus the test case

For every elliptic curve `E/Q`, general BSD asserts (1) `rank E(Q) = ord_{s=1} L(E,s)`; (2) finiteness of `Sha(E/Q)`; (3) the normalized leading-term formula
```
L^(r)(E,1)/r! = Omega_E * Reg(E/Q) * |Sha(E/Q)| * product_l c_l / |E(Q)_tors|^2,
```
using the compatible real-period convention. Proving rank equality alone proves neither Sha finiteness nor the leading coefficient.

The focal `E: y^2+xy=x^3-x^2-79x+289` (`234446.a1`) has established algebraic rank four and sign +1. To establish analytic rank at least four one needs exact **original complex** `L''(E,1)=0`; to establish exact order four additionally one needs rigorous `L^(4)(E,1) != 0`. Neither is proved here. The nonzero -7 twist derivative, 11-adic classes, p-adic heights and function-field zeta factors concern different objects. Original Sha finiteness and full leading coefficient remain open.

**New proved mathematical implication toward original complex rank, general BSD, Sha finiteness, or leading coefficient since WPR-2026-10-30-01: NONE.** No new merged arithmetic changes, no actual supported global cochain, no computed second Bockstein, and no complex comparison theorem were found.

## Complete C-series scope (C-0001 through C-0050)

| Claims | What is established/recorded | What is not |
|---|---|---|
| C-0001–0004 | finite local 11-adic arithmetic, exact quadratic Selmer decomposition, conditional anticyclotomic applicability | global Selmer/Sha bound or complex derivative |
| C-0005–0009 | numerical original complex diagnostics, twist-specific rigorous enclosure with source assumptions, integral filtration false-positive gate | exact original L'' zero |
| C-0010–0014 | exact character, sigma, denominator and local linear algebra; provisional BCLMN global first heights, corrected coordinates | independently verified global heights or second height |
| C-0015–0019 | Castella–Hsieh rank-two hypothesis no-go, corrected Ulmer prime-field ranks 2/3/7 versus geometric 3/7/25, exact Fermat/Jacobi controls, 433a1 rank-two control | characteristic-zero rank-four complex theorem |
| C-0020–0023 | source-dependent Howard/Heegner tower, base-point torsion and Castella weight-two specialization | nonzero higher Coleman jets or complex comparison |
| C-0024–0028 | source-derived T-divided Greenberg Iwasawa class, universal-norm regulator no-go, conditional alternating second-height linear algebra | actual nonzero h2 or base derived regulator |
| C-0029–0032 | direct-coordinate provisional first heights, conditional Selmer-complex comparison, twist interval corroboration | actual second Bockstein |
| C-0033–0041 | exact ray layers and torsors, residual 11-saturation, conditional supported cohomology and obstruction | evaluated nonabelian arithmetic action/cochain |
| C-0042–0044 | source-gated twist Selmer line and exact Kurihara delta | original curve's Sha or analytic rank |
| C-0045–0047 | conditional signed global first-lift existence and ambiguity | evaluated normalized supported cochain |
| C-0048–0049 | exact local norm point 115 mod121; conditional uniquely normalized residual global cohomology class | actual global cocycle or h2 |
| C-0050 | unmerged PR #77's necessary nonzero Frobenius commutator constraint | constructed first correction or second lift |

No C-series claim is promoted; corrections in the historical ledger remain intact. Separate categories: exact finite computations; provisional numerical/analytic certificates; conditional applications of published theorems; source-scope no-go findings; and workflow infrastructure. Green CI does not prove a theorem.

## H1–H6, missing arrows and decisions

- **H1 derived Kato / supported Galois correction (40%)**: strongest candidate arithmetic work C-0044–50, but no arithmetically realized nonabelian finite quotient, evaluated `rho,ell,c0,c1`, complete support/Greenberg local comparison or original complex bridge. Reject any candidate violating C-0050 or a defining Galois relation; do not build an enormous field before specifying the quotient.
- **H2 mixed heights / second Bockstein (15%)**: source-dependent first lifts and provisional first heights exist, but no actual second obstruction. October 30 exact synthetic noncommuting countermodel shows first-lift success need not imply second-lift existence. Kill any comparison with mismatched local Selmer conditions or sign.
- **H3 quadratic-field characteristic-zero geometry (40%)**: the typed identity `L'''(E/K,1)=3 L''(E,1)L'(E^-7,1)` (after lower-order vanishing) could isolate the target, but only if a **new independent exact third complex derivative vanishing theorem** is established. No such theorem was located. The new rank-two parity countermodel below rules out parity-only shortcuts. Demand exact characteristic-zero, derivative-order-three theorem and independently proved geometric vanishing.
- **H4 Mazur–Tate (0%, parked)**: apparent bridge relies on BSD/Perrin–Riou premises or mismatched congruences; restart only with noncircular complex comparison.
- **H5 numerical diagnostics (5%)**: exact twist enclosures are valuable; more original `L''` digits cannot certify zero. No precision-only work.
- **H6 period projector (0%, parked)**: no source-defined second-order projector; rank-two parity model kills symmetry-only inference.

**Safe lemma:** certify exact Frobenius/action and relation obligations of a minimal actual finite quotient before attempting a supported first correction. **Credible leapfrog:** construct and evaluate the actual supported `x=P2-2P1` first correction and Greenberg/Shapiro local homotopies. **Wild alternative:** discover a characteristic-zero cycle formula whose literal output is `L'''(E/K,1)`, with a genuinely independent geometric vanishing mechanism. Do not confuse structural Kolyvagin-system refinements with that output.

## New adversarial negative control: H3 parity/product false positive

Let `t=s-1`. Formal completed-function parity models with even `F(t)=t^2+a t^4` (rank two) and odd `G(t)=t+b t^3` (twist rank one) satisfy
```
(FG)'''(0) = 6 = 3 F''(0) G'(0) != 0.
```
Thus functional-equation signs (+1,-1), odd base-change sign, and nonzero twist first derivative **do not force** the third base-change derivative to vanish. By contrast `F=t^4,G=t` gives third derivative zero. Exact standard-library verifier `research/reviews/controls/h3_parity_product_negative_control_2026_11_06.py` checks nine rank-two choices and the rank-four comparison, with an explicitly rejected shortcut. Local execution on 2026-11-06: **PASS**. This is a formal analytic-logic countermodel, not a real elliptic curve or an arithmetic calculation. It rules out an invalid implication, not H3 itself.

Interdisciplinary transfer: formal-model counterexample testing is a **validation method**, not a theorem on elliptic L-functions. Homological algebra can construct h2 only after actual Selmer complexes are specified; coding-theory syndromes could check global/local matrices but cannot create them. Neither physics analogies nor characteristic-p geometry supplies a complex comparison without a proved map.

## Outside mathematical research and scope

- [Castella–Hsieh (2022)](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864): derived-height filtration is distinct from Theorem A's rank-two nonvanishing hypotheses, which do not certify rank four.
- [Kim, higher Gross–Zagier (arXiv:2203.12161)](https://arxiv.org/abs/2203.12161): structural Kolyvagin-system/modular-symbol refinement, not the desired third **complex** derivative identity.
- [Macias Castillo–Sano (2026)](https://arxiv.org/abs/2603.23978) and [Sano (2023)](https://arxiv.org/abs/2308.08875): conditional p-adic Selmer/Bockstein comparisons, not the complex bridge.
- [OpenAI Math low-Selmer-corank BSD manuscripts, revised 2026-10-06/07](https://github.com/openai/math): newly included in this review's outside scan. They **claim** full BSD for Selmer corank at most one; these are unrefereed preprints, with no Lean formalization listed in the inspected catalogue, not established theorems for this project. More decisively, for our rank-four curve the Kummer injection gives `corank_Zp Sel_{p∞}(E/Q) >= rank E(Q) = 4` for **every** p, so the claimed corank <=1 hypothesis fails regardless of whether those preprints withstand review. This is an exact hypothesis no-go, not a new BSD implication.

## GitHub, next test, and reproducibility

GitHub inspected 2026-11-06: main unchanged since merged #75 (2026-10-22); PRs #76, #77, #78 still open; issues [#61](https://github.com/katearline-beep/birchswinnertondyer/issues/61), [#53](https://github.com/katearline-beep/birchswinnertondyer/issues/53), [#49](https://github.com/katearline-beep/birchswinnertondyer/issues/49), [#41](https://github.com/katearline-beep/birchswinnertondyer/issues/41), [#20](https://github.com/katearline-beep/birchswinnertondyer/issues/20), [#18](https://github.com/katearline-beep/birchswinnertondyer/issues/18), [#19](https://github.com/katearline-beep/birchswinnertondyer/issues/19), [#22](https://github.com/katearline-beep/birchswinnertondyer/issues/22), [#23](https://github.com/katearline-beep/birchswinnertondyer/issues/23) remain open. No independent expert mathematical review found. Review is stacked atop #78 and requires its own CI and mathematical review; no merge authorization.

Next **decisive test**: for H3, produce a source-typed table of candidate characteristic-zero third-derivative theorems, each with theorem number, original complex L-function, derivative order, vanishing hypothesis and proof of relevance; stop if every candidate has a different output. In parallel, H1 requires the first *actual* arithmetically realized nonabelian quotient, with explicit relations and local conditions, before any higher obstruction enumeration. Prioritize a source-verified missing arrow, not more local digits.

Run locally / in CI:
```sh
python3 -I -B research/reviews/controls/h3_parity_product_negative_control_2026_11_06.py
python3 -I -B research/reviews/controls/commutator_second_lift_nonimplication_2026_10_30.py
python3 -I -B research/harness/validate.py
python3 -I -B research/harness/test_validate.py
python3 -I -B research/harness/validate_leapfrogs.py
python3 -I -B research/harness/test_leapfrogs.py
python3 -I -B research/harness/validate_full_review.py
python3 -I -B research/harness/test_full_review.py
```
Only the **new** control has been executed locally in this review environment; prior scripts and the full CI suite require a checked-out repo/CI runner and are not claimed passed for this PR. Main blocker remains a noncircular theorem reaching original complex `L''(E,1)=0`, with actual supported cochain and h2 additionally missing. **NONE toward BSD.**
