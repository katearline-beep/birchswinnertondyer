# C-0009: 6,000-term conditional exact-rational twist derivative enclosure

**Research date: 2026-10-19.** **Status: computationally reproduced, conditional on the published elliptic modular L-function identity and the stated coefficient/local-factor bounds; *not independently expert-reviewed*.** This does **not** prove the original rank-four curve's complex analytic-rank equality or BSD.

## Objects and exact mathematical assumptions

The original elliptic curve is

```
E: y²+xy=x³−x²−79x+289,  N=234446.
d=−7,   Et = E^(−7): Y²=X³−62083X−5909890.
M=49N=11487854, global twist root sign −1.
c=2π/√M.
```

For the coefficients \(a_n\) of the original curve's weight-two modular form and the primitive quadratic character \(\chi_{-7}\), assume the standard modularity / quadratic-twist / functional-equation identities

\[
L'(E^{-7},1)=2\sum_{n\ge1}\frac{a_n\chi_{-7}(n)}{n}E_1(cn),
\qquad
E_1(x)=\int_x^\infty\frac{e^{-u}}{u}\,du.
\]

This formula is [derived in the project](MELLIN_IDENTITY.md) and appears independently in [SageMath elliptic L-series documentation](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/lseries_ell.html). The bound \(\lvert a_n\rvert\le d(n)\sqrt{n}\le2n\) is a consequence of the Hasse bound at good primes, the semistable bad Euler factors and coefficient multiplicativity. A subject-matter expert should still review all analytic assumptions and normalizations before promoting C-0009 to a theorem.

## Two separate exact-arithmetic programs

1. The **new** [6,000-term rational-per-term implementation](independent_rational_derivative_6000.py) evaluates the logarithm, Euler constant and exponential-integral power-series enclosures using \(\mathbb Q\), then rounds **each entire summand outward** only on addition to an integer-scale accumulator. It does not import any previous output or coefficient list. All arithmetic assertions passed on CPython 3.11, 3.12 and 3.13.
2. The **older historical fixed-point program** `bsd_session5_twist_refined.py` was independently executed again in the project workspace (source digest SHA-256 `c6cef58a2845e9dc19064d3b62660ea65d8fd6153aced14b67ff5dcecee1e761`). Its earlier-source rounding strategy is distinct. It is **not yet checked into the repository**, so this digest is provenance, not an independently retrievable source artifact. It reported finite interval \((34.172033867962,34.172034029117)\), total tail \(0.0028949705419440567\), and conditional whole interval \((34.169138897420055,34.174928999658945)\). Neither algorithm constitutes *independent human* review.

The **new separately executed 6,000-term script** prints:

```
FINITE EXACT INTERVAL 34.17200907 34.17205867
RATIONAL TAIL UPPER 0.0028949705419440567
CONDITIONAL LPRIME INTERVAL 34.169114099458056 34.17495364054194
PASS: independent exact term enclosures imply positivity given stated analytic identity
```

Its mathematical inequalities hold with exact \(\mathbb Q\) and integer comparisons; the displayed decimals are **approximations to rational bounds**, not outward-certified printed endpoints. A concise conservative statement, taking care with rounding, is

\[
\boxed{34.1691<L'(E^{-7},1)<34.1750}
\]

**conditionally on the mathematical hypotheses above.** The interval contains the historical interval and also PARI's independent **numerical** value \(\approx34.17203446096447\).

### Why the new interval is conservative

The improved implementation uses 55 nonzero terms in the exponential-integral alternating series for \(0<x\le12\). Its omitted 56th term has magnitude at most

\[
\frac{12^{56}}{56\cdot56!}<10^{-12}
\]

and is a valid alternating-tail bound because subsequent terms decrease. It separately bounds the difference between \(c_0n\) and \(cn\) via \(|E_1'(x)|\le 1/x\).

For \(c\ge c_0=1853789485821/10^{15}>0\), let \(q=(1+c_0)^{-1}\). Using \(E_1(x)\le e^{-x}/x\) and \(e^{-c}\le q\),

\[
\left|2\sum_{n>6000}\frac{a_n\chi_{-7}(n)}{n}E_1(cn)\right|
\le \frac{4q^{6001}}{6001c_0(1-q)} <0.002895.
\]

The extension from 2,000 to 6,000 terms reduces the infinite-tail uncertainty from about 14.322 to below 0.002895 while preserving the exact-rational argument. It is a **stronger supporting certificate**, but not proof of a new complex rank-equality theorem.

## Independent Fourier coefficient oracle

[PARI/GP's \(\mathrm{ellan}(E,6000)\)](../harness/pari_fourier_6000.gp) was compared **term-by-term** against the coefficients independently computed by the new Python certificate. All 6,000 integers agreed; the [comparator](../harness/compare_fourier_coefficients_6000.py) rejects a deliberately altered \(a_{17}\).

SHA-256 of the canonical comma-separated vector \((a_1,\dots,a_{6000})\):

```
3b4d1fb4039c5f18e339566cd7f9a8e395ee0e4c6af2c92f7b69addf094f11ea
```

This does not independently verify modularity or every infinite coefficient, but it makes the **finite** certificate's input considerably more credible. PARI's decimal derivative is a third numerical corroboration, not an independently certified error bound.

## Reproduction

```bash
python3 -I -B research/anticyclotomic_11/independent_rational_derivative_6000.py
gp -q -f research/harness/pari_fourier_6000.gp > /tmp/bsd-pari-6000.txt
python3 -I -B research/harness/compare_fourier_coefficients_6000.py /tmp/bsd-pari-6000.txt
```

The GitHub Actions [exact Python matrix](../../.github/workflows/split11.yml) and [independent PARI oracle](../../.github/workflows/research_harness.yml) execute these programs with negative controls.

## Open proof and peer-review obligations

- Verify the Mellin-transform derivation, factor of two, root-number/conductor, every local Euler factor, and correctness of the uniform all-\(n\) growth bound.
- Line-by-line inspect the exact power-series enclosure, Euler–Mascheroni bound, sign-dependent summand intervals, and complete tail argument.
- Seek a third independent implementation using FLINT/Arb, or independent Sage rigorous interval facilities.
- **Do not** declare analytic rank one for the twist as independently established merely from green CI and agreeing AI-authored scripts; expert arithmetic-geometry review is outstanding.
- Even after such review, an analytic rank-one result for \(E^{-7}\) proves neither \(\Sha(E^{-7})[11]=0\) nor \(L''(E,1)=0\) for the original E, and does **not** resolve rank-four BSD or the full leading-coefficient conjecture.

**Whole-problem status at this checkpoint:** no new mathematical arrow from four rational points to complex \(L''(E,1)=0\) has been proved. This is a valuable reproducibility improvement on a supporting claim, not a leapfrog toward the central obstruction.
