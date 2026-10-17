# Audit of the earlier E^-7 derivative positivity experiment (2026-10-17)

**Status:** an evidence audit, not yet an externally reviewed analytic nonvanishing certificate or a new theorem. This file documents exactly which parts have and have not been rechecked.

## Source provenance

The original local historical programs were re-run/read in the research workspace, but their **full source has not yet been committed** to GitHub. Original SHA-256 content digests:

```
bsd_session5_twist_nonvanishing.py
460f0737381142c13b5dddc4a5131dab3a1fb696eef4a762b76f1e36d0997491

bsd_session5_twist_refined.py
c6cef58a2845e9dc19064d3b62660ea65d8fd6153aced14b67ff5dcecee1e761
```

These checksums are **identifiers only**; they do not make the source reproducible until the exact archived bytes are committed. Do not treat this record as a substitute for source control.

The 2,000-term historical script ran again and printed:

```
Certified c in 0.001853789485821 0.001853789485822
Certified Euler gamma interval 0.577215664901532 0.577215664932576
Partial sum interval for first 2000 Fourier coefficients:
  34.174485397474 34.17448541782
Whole infinite-tail absolute bound: 14.321932128848701
CERTIFIED: L_prime(E_twist_minus7,1) lies in
  19.8525532686253 48.4964175466687
CERTIFIED: L_prime(E_twist_minus7,1) > 0
```

**Interpret 'CERTIFIED' here as the historical program's output, not our acceptance of a proof.** A *new, separately written* exact-rational finite-sum implementation is now available below; the original historical implementation and the analytic identity still require mathematical review. The 6,000-term historical script previously reported an interval approximately (34.1691,34.1749), but this current audit did not independently rerun it.

## Rechecked exact mathematical bounds

The *independently written* [analytic-component checker](audit_derivative_error_budget.py) uses `fractions.Fraction` and proves exact rational inequalities for:

1. Bounds on `c=2π/√(49N)` from Machin's formula with alternating arctangent remainders.
2. The alternating exponential-integral series truncation bound `4^31/(31·31!) < 10^-12` for inputs `0<x≤4`.
3. A complete infinite-tail bound **14 < T < 15** after `n>2000`, conditional on the conventional Fourier-coefficient growth inequality `|a_n|≤d(n)√n≤2n`, the elementary `E₁(x)≤e^-x/x`, and the series formula for the derivative.
4. The **conditional** positive gap between the old *reported* finite-sum lower endpoint and the independently recomputed upper tail, exceeding 19.

It also has a deliberately corrupt-tail-exponent negative control: the erroneously shortened exponential decay exponent gives a tail too large to claim positivity. The checker rejects the bad inference.

## Proof obligations still open

- **Central identity**: derive the exact factor 2 and kernel `E₁(cn)/n` from the Mellin transform, the normalization of the completed L-function, and the twist's functional equation sign. Check all constants and conductor/root sign against independent sources.
- **Fourier coefficients**: re-evaluate all `a_n` on the minimal original model, including bad primes 2 and 117223, and verify the multiplicative/Hecke prime-power recursion.
- **Finite-series enclosures**: the new independent exact-rational program below recomputes them. Still import the original source and audit every original rounding branch; obtain a third implementation using FLINT/Arb, and compare all 2,000 Fourier coefficients and normalization choices.
- **Tail assumption**: independently justify `|a_n|≤d(n)√n` including bad prime factors, and the relevant `E₁` bound. The exact arithmetical tail algebra alone is insufficient without its theorem hypotheses.
- **System integrity**: independent machine/library implementation, version-pinned dependencies, full raw logs, and negative tests for altered conductor, root sign, coefficient input and exceptional points.

## Current logical boundary

PARI/GP 2.15.4 reports `L'(E^-7,1) ≈34.17203446096447` and sign −1, agreeing with the historical finite-series enclosure. This is independent **numerical corroboration**. The component auditor separately checks exact error terms, and the new per-term rational script independently encloses the entire 2,000-term finite sum. **The conditional computational implication is stronger, but the analytic identity and theorem hypotheses still require expert review before a claim of a fully vetted proof of analytic rank one.**

If a fully rigorous derivative nonvanishing certificate is accepted, the appropriate Gross–Zagier/Kolyvagin theorems would imply rank one and finiteness of Sha for the twist. This would **not** prove triviality of its 11-primary Sha or settle the rank-four factor.

## Additional exact-rational finite-sum verification — independent algorithm

The new [independent rational certificate](independent_rational_derivative.py), run using only Python's standard library, computes the 2,000-term finite sum by **rational evaluation of every full term**, with outward fixed-point rounding only when the term enters the accumulator. The earlier historical program instead rounded *inside* its intermediate transcendental series. They share the elliptic curve and standard analytic definitions, but their interval algorithms differ.

This new calculation reports:

```
FINITE EXACT INTERVAL 34.17447712 34.17449367
RATIONAL TAIL UPPER 14.321932128848701
CONDITIONAL LPRIME INTERVAL 19.852544991151298 48.4964257988487
```

The displayed decimal bounds are summaries rounded from the internal *exact rational* interval. The program asserts the key strict inequalities before printing. It uses fresh rational power series for logarithms/Euler's constant and the exponential integral; independent prime point counts and Hecke recurrences compute the 2,000 Fourier coefficients.

**Proof obligation remains:** the identity `L'(1)=2Σ a_nχ(n)E₁(cn)/n`, conductor/sign, the global Fourier coefficients, and the coefficient bound are mathematical premises not established *by* the program. An expert should examine the code and analytic derivation. The word 'certificate' denotes a candidate conditional arithmetic certificate, **not** an externally reviewed BSD theorem.

The original historical code's SHA-256 digests remain recorded above; it still needs to be committed unchanged as a provenance artifact. This new separate implementation is already in the repository and running under CI.

## Related

- [Previous numerical audit](TWIST_ANALYTIC_AUDIT.md)
- [Interdisciplinary research transfer priorities](../INTERDISCIPLINARY_TRANSFER_AUDIT.md)
- [C-0005](../../CLAIMS.md)

**Methodology reference:** FLINT [ball enclosure semantics](https://flintlib.org/doc/using.html), emphasizing that mathematical enclosure requires both valid input assumptions and an inclusion-preserving algorithm.
