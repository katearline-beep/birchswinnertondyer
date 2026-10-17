# The -7 twist: independent analytic input audit (2026-10-17)

**Status:** independent **numerical** computation and exact rational curve data check. Does not certify analytic rank or the finiteness of Tate–Shafarevich. The separate old rational interval script is **not yet in this repository**, so its proof of completeness has not been audited or published here.

The original elliptic curve is E: y²+xy=x³−x²−79x+289, with N=234446. On its short model E0:y²=x³−1267x+17230, the quadratic twist by d=−7 is

```
Et: Y²=X³−62083 X−5909890.
```

PARI/GP 2.15.4 computes independently:

```
conductor(Et) = 11,487,854 = 49 × 234446
root number(Et) = −1
analytic-rank routine: [1, 34.172034460964473032879936363633231813]
ellL1(Et,1) = 34.172034460964473032879936363633231813
```

Reproduce with `gp -q -f research/anticyclotomic_11/twist_analytic.gp`. The [workflow](../../.github/workflows/twist_analytic.yml) runs this in Ubuntu with an independently installed PARI library, checks expected conductor/sign and two numerical methods, and rejects GP interpreter errors.

## Why this matters, and what it does not show

A private earlier exact-rational arithmetic script constructed a **coarse positive enclosure**, reportedly

```
19.8525532686253 < L'(Et,1) < 48.4964175466687
```

using truncated exponential-integral series and an explicit infinite tail bound, conditional on its conductor, root number, Fourier coefficients and approximate-functional-equation identity. The independent PARI value lies strictly within that interval. This is a meaningful cross-check, but a loose interval alone does not validate its derivation.

**Next:** bring the entire original interval-checking Python program into the repository unchanged as a historical artifact; audit the functional equation, sign, conductor, exact coefficient recursion, outward interval arithmetic, tail bound and expected output, then commission an independent implementation. Only then consider elevating the positivity to a computational certificate.

A genuinely rigorous nonvanishing theorem for L'(Et,1) would imply analytic rank 1 and, by the appropriate Gross–Zagier and Kolyvagin results, algebraic rank one and finiteness of Sha(Et/Q). **This does not force Sha(Et/Q)[11]=0:** an additional 11-primary descent/index check would be needed. It also does not settle the original rank-four factor E/Q, or BSD.

The phrase 'analytic rank 1' in PARI's output is **numerical software classification** based on a precision threshold, not a mathematical proof.

## Methodological note

This is analogous to validating a biological finding with a different measurement platform: the two programs agree on the biological *observable* (here the derivative), while theory is still needed to establish what the measurement implies.

References: [PARI elliptic functions](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html) (`ellrootno`, `ellanalyticrank`, `ellL1`); Gross–Zagier, *Heegner points and derivatives of L-series* (1986); Kolyvagin, *Finiteness of E(Q) and Sha(E,Q) for a subclass of Weil curves* (1990); Agboola–Castella (2021), Corollary 6.4.

**Provenance:** Human–AI exploration, 17 Oct 2026. Literature applications remain subject to qualified mathematical review.
