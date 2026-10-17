# Whole-problem checkpoint WPR-2026-10-17-01

*2026-10-17 · AI-assisted internal review, **not** independent mathematical review · Next full checkpoint: 2026-10-24.*

## The whole conjecture, not merely the example

BSD for an elliptic curve over Q has a **complex analytic rank equality** component and a **leading coefficient / regulator / Tamagawa / Sha** component. We have not proved either in general. Our specific test curve, LMFDB **234446.a1**, has algebraic rank four and numerical evidence consistent with complex analytic order four, but the exact complex identity \(L''(E,1)=0\) is still not proved. Proving the *exact* analytic rank also needs nonzero \(L^{(4)}(E,1)\), and even then the full BSD leading-coefficient conjecture remains.

**Question that must be asked after every sprint:** What exact new mathematical implication toward \(L''(E,1)=0\), or toward the full BSD theorem, was proved since the preceding checkpoint?

**Answer at this checkpoint: none.**

This is not a claim that no useful work occurred. It prevents a long collection of computations about other invariants from being mistaken for a new analytic-rank-four theorem.

## What actually exists

| Evidence / claim | Current best established output within this project | Still **not** established |
|---|---|---|
| C-0001/2: local logarithms | Exact finite local matrices modulo 11⁴ with separate PARI/GP agreement | Derived height radical, global Selmer or original L'' |
| C-0003: Agboola–Castella | Conditional **anticyclotomic p-adic** vanishing-order bound, assuming Sha(E/K)[11∞] finite | The finiteness hypothesis, equality of p-adic order, any complex rank implication |
| C-0004: 11-Selmer splitting | Standard algebraic splitting into E and its −7 twist over Q | A complete 11-Selmer upper bound of dimensions 4 and 1 |
| C-0005/6: −7 twist | Numerically corroborated and exact-rational candidate positive **twist first derivative** enclosure | Independent expert-audited proof, implication for E's complex second derivative |
| C-0007/8: real/cyclotomic 11-adic | Exact field, Tate local-data and false-positive group-ring tests; published theorem hypotheses isolated | Actual derived Kato class, Sha finiteness, complex reciprocity |
| H5: direct PARI derivatives | Strong numerical signature of complex rank four and rank-two negative control | A proof that the original complex second derivative equals exactly zero |

We did useful research-quality work by **rejecting** two false shortcuts: first-layer mod-11 augmentation divisibility posing as integral I-adic vanishing, and a Mazur–Tate theorem that *assumes* BSD being used backward to prove BSD. Neither rejection is a new BSD theorem.

## Six-track reassessment

| Track | Decision | Most important missing arrow / next useful test |
|---|---|---|
| H1 Derived Kato | **Active, computationally limited** | Only augmentation classes are studied; no proven transfer to complex L''. Next: feasibility of a genuine cohomological derived class, not another field. |
| H2 Mixed Bockstein heights | **Active, computationally limited** | No genuine global one-prime modified Selmer cross-height and no complex comparison. Next: fully specified pairing. |
| H3 Quadratic-field geometry | **Prioritize theorem audit** | Product identity is exact, but its cubic base-change derivative has no proven geometric vanishing formula in our sources. Next: check candidate theorems' derivative **order**. |
| H4 Mazur–Tate congruences | **Park** | The tempting 2025 theorem's BSD premise is circular for our goal; congruences alone don't establish complex zeros. |
| H5 Numerical curvature | **Use as diagnostic only** | Numerical near-zeros do not prove exact complex zeros; no justification for additional precision-only runs. |
| H6 Period projectors | **Park** | Root-number parity allows analytic rank two; no novel period operator specified. |

## Focused near-term mathematical check

A targeted source review found two contemporary examples where “higher” refers to **higher weight forms, generalized Heegner cycles or higher-dimensional geometry**, but the actual theorem still concerns a **FIRST** central derivative:

- D. T.-B. G. Lilienfeldt and A. Shnidman, [*Derivatives of Rankin–Selberg L-functions and heights of generalized Heegner cycles*](https://arxiv.org/abs/2408.04375), Theorem 1.1. The forms have weight \(2k\) and the geometric cycles are higher codimension; the L-function derivative order is **one**.
- T. Du and Z. Peng, [*On the central derivatives of L-functions and modularity of Heegner cycles*](https://arxiv.org/abs/2603.15795) (2026 preprint), an arithmetic intersection formula for **central derivatives** in **higher weights**, again not a demonstrated cubic-derivative vanishing result for our weight-two E/K.

**This does not establish that a cubic-derivative theorem is absent from the literature.** It *does* disqualify these two tempting references as a direct H3 bridge unless some additional, explicitly stated specialization is proved.

Our exact product identity for an eligible odd-sign quadratic twist with certified \(L'(E^D,1)\ne0\) is
\[
L'''(E/K_D,1)=3L''(E,1)L'(E^D,1).
\]
A geometric proof that the **left side equals zero** would force the missing complex condition. Merely evaluating a twist first derivative or restating this factorization cannot make that conclusion.

### Three bets before the next checkpoint

- **Conservative:** submit our conditional exact rational twist derivative certificate (C-0006) for a focused expert audit of Mellin normalization, coefficients and complete tail; no claim of BSD.
- **Credible leapfrog:** H3 theorem-identity go/no-go audit: find or formulate a genuine geometric **third** derivative formula with testable hypotheses. Stop if only first-derivative generalizations exist.
- **Wild but testable:** H6 geometric period cancellation, conditional on a defined operator and a rank-two counter-control. Do **not** start implementation without that definition.

**Selected next experiment:** the H3 theorem-identity audit, combined with continued external-review preparation for C-0006. **Deprioritized:** computing more cyclotomic finite layers, increasing local-log precision, and unreviewed H4/H6 experiments until they can supply the missing arrow.

## A stress test of our methodology

Take the completed even-sign Taylor germs \(t^2\) and \(t^4\). Both satisfy positive functional-equation parity and vanishing constant term, but one has nonzero second derivative and the other does not. Likewise the exact third-derivative product formula by itself permits either case. It is therefore *not* legitimate to infer order four from ordinary parity, an unrelated (p)-adic order or a quadratic-field factorization alone.

## Decision provenance

Reviewed repository files: [CLAIMS.md](../../CLAIMS.md), [high-upside portfolio](../strategy/HIGH_UPSIDE_PORTFOLIO.md), [derived-Kato audit](../strategy/KATO_BRIDGE_AUDIT.md), [cyclotomic failure-mode audit](../strategy/CYCLOTOMIC_KATO_FILTRATION_GATE.md), [Mazur–Tate applicability audit](../strategy/MAZUR_TATE_2025_SCOPE.md). Recent merged PRs examined: #24, #26, #27, #28. Primary source links above; no claim of exhaustive literature coverage. All mathematical claims remain at their existing ledger status; **none promoted**.

The structured record is [current.json](current.json), and CI will check documentation consistency. Neither this report nor CI substitutes for independent mathematical review.

**Next review due: 2026-10-24**, or sooner after three substantive PR merges or a major falsification. Report honestly if no new implication toward BSD has been established.
