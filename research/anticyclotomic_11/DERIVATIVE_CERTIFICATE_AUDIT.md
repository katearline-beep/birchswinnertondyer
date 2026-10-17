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

**Interpret 'CERTIFIED' here as the historical program's output, not our acceptance of a proof.** The finite Fourier-sum computation and the analytic identity both still require independent audit. The 6,000-term historical script previously reported an interval approximately (34.1691,34.1749), but this current audit did not independently rerun it.

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
- **Finite-series enclosures**: import the exact source, isolate logarithm and Euler–Mascheroni error estimates, verify every sign/rounding branch, then run a separate FLINT/Arb enclosure calculation.
- **Tail assumption**: independently justify `|a_n|≤d(n)√n` including bad prime factors, and the relevant `E₁` bound. The exact arithmetical tail algebra alone is insufficient without its theorem hypotheses.
- **System integrity**: independent machine/library implementation, version-pinned dependencies, full raw logs, and negative tests for altered conductor, root sign, coefficient input and exceptional points.

## Current logical boundary

PARI/GP 2.15.4 reports `L'(E^-7,1) ≈34.17203446096447` and sign −1, agreeing with the historical finite-series enclosure. This is independent **numerical corroboration**. The component auditor now provides a separate exact check of some error terms. **Neither alone nor together currently constitutes a completely audited proof of analytic rank one.**

If a fully rigorous derivative nonvanishing certificate is accepted, the appropriate Gross–Zagier/Kolyvagin theorems would imply rank one and finiteness of Sha for the twist. This would **not** prove triviality of its 11-primary Sha or settle the rank-four factor.

## Related

- [Previous numerical audit](TWIST_ANALYTIC_AUDIT.md)
- [Interdisciplinary research transfer priorities](../INTERDISCIPLINARY_TRANSFER_AUDIT.md)
- [C-0005](../../CLAIMS.md)

**Methodology reference:** FLINT [ball enclosure semantics](https://flintlib.org/doc/using.html), emphasizing that mathematical enclosure requires both valid input assumptions and an inclusion-preserving algorithm.
