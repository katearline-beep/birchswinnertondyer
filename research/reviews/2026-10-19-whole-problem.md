# Whole-problem checkpoint WPR-2026-10-19-01

*2026-10-19 · AI-assisted internal review; not independent peer review · Next full checkpoint due 2026-10-26 or sooner after a major breakthrough or three substantive merges.*

## The question we must not lose

**General BSD:** For elliptic curves over Q, show (i) algebraic rank equals complex analytic vanishing order, and (ii) the precise leading-coefficient formula involving Sha finiteness, periods, regulator, Tamagawa numbers and torsion.

**Our difficult example:** E=234446.a1 has established algebraic rank four, but no project proof that its **original complex** L''(E,1)=0, hence no proof of analytic rank four. The nonzero fourth derivative is so far numerical. Even a future analytic rank-four proof for this example does not settle the leading-coefficient formula or BSD in general.

**What previously missing mathematical implication toward general BSD or the curve's original complex L'' was established since the previous checkpoint? NONE.**

## What genuinely changed since WPR-2026-10-17-01

**Supporting computational result C-0009 improved materially**: independently implemented rational-per-term summation now covers **6,000** coefficients rather than 2,000. A precise conditional interval for the -7 twist's **first derivative** is

\[
34.1691 < L'(E^{-7},1) < 34.1750.
\]

The entire tail after 6,000 is bounded by 0.002895 under the established modular-form coefficient-growth inequality and the correctly normalized exponential-integral Mellin identity. PARI/GP independently matches **all 6,000** original Fourier coefficients, with an intentionally corrupted coefficient rejected. The previous different historical fixed-point code agrees. Three CPython versions pass the exact mathematical assertions. The earlier 2,000-term tail was about 14.322.

This is a much better independently reproducible **conditional subsidiary certificate**. The twist is NOT the rank-four original E; its derivative is NOT L''(E,1). Neither Gross–Zagier–Kolyvagin consequences nor Sha(E^{-7})[11]=0 are newly claimed without the needed mathematical review and separate p-primary hypotheses.

## Claim and six-track review

The claim ledger now contains C-0001 through **C-0009**, each subject to its existing limitations. Specifically:

- **C-0001/2:** finite split-11 local-log matrices; no global derived height.
- **C-0003:** conditional anticyclotomic *p-adic* theorem; required Sha(E/K)[11∞] finiteness unproved.
- **C-0004:** standard quadratic classical 11-Selmer splitting; neither dimension upper bound established.
- **C-0005/6/9:** numerical + rational interval twist first-derivative certificates; C-0009 adds 6,000-term independently checked arithmetic. Not a theorem on original L''.
- **C-0007/8:** cyclotomic field and integral augmentation mathematical checks; no constructed derived Kato class or complex reciprocity.

| Track | Current decision | Exact bottleneck |
|---|---|---|
| H1 Derived Kato | Active but restricted | Missing noncircular complex L'' comparison; BKS results include unproved Sha finiteness. |
| H2 Selmer/Bockstein heights | Restricted | No computed global mixed pairing and no complex reciprocity. |
| H3 Quadratic-field higher geometry | Prioritize theorem-level search | Need actual cubic weight-two derivative vanishing formula, not a higher-weight **first** derivative. |
| H4 Mazur–Tate | Park | 2025 main theorem assumes BSD; rank-one corollary does not apply. |
| H5 numerical curvature | Diagnostic only | Apparent near-zero is never an exact complex zero. |
| H6 geometric period cancellation | Park | No operator beyond parity with a rigorously defined second derivative map. |

### Falsification discipline and decision

**Negative control:** a rank-two curve and rank-four curve can share positive root number, vanish at the center, and have a quadratic-base-change **first** derivative equal to zero; their **third** derivatives can still differ. Therefore a first-height Gross–Zagier theorem cannot by itself produce the original complex rank-four condition. Separately the mod-11 scalar norm false-positive shows why finite congruences must not be confused with integral/Iwasawa vanishing.

**Near-term conservative work:** independently review the newly strengthened twist certificate's Mellin normalization, all-n coefficient bounds, sign/tail enclosure and existing source statements. It is the closest practical subsidiary mathematical theorem. **Not another increase to 10,000 digits or coefficients**.

**Credible leapfrog:** continue H3 exact third-derivative geometry theorem search only if a precise candidate mathematical map is found.

**Wild bet:** an independently constructed complex period projector, falsified against rank-two controls before numerical implementation.

**Selected next experiment:** seek expert-level mathematical audit for C-0009; in parallel carry out a bounded theorem-applicability audit for a genuinely **third**-derivative identity, not high-weight first-derivative analogies.

**Deprioritized:** expanding local-11 logarithms, computing many more cyclotomic fields, and increasing derivative precision without a different proof hypothesis. Our comparative advantage has shifted from computational output to finding a valid logical bridge.

## Sources, status and next review

Reviewed [the claim ledger](../../CLAIMS.md), [C-0009 exact program](../anticyclotomic_11/independent_rational_derivative_6000.py), [its audit](../anticyclotomic_11/EXACT_6000_AUDIT.md), [H3 no-go](../strategy/H3_DERIVATIVE_ORDER_AUDIT.md), prior [whole-problem review](2026-10-17-whole-problem.md) and merged PR #29. Automated independent PARI cross-check and original numerical derivative workflow agree. No independent human expert review has been performed, no new statement proving complex rank four has been established, and no BSD proof is claimed.

**Next periodic review:** 2026-10-26 (with the standing weekly independent-minded review cadence). Never silently promote a computational result to a mathematical theorem.
