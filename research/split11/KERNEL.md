# C-0002 — An explicit finite-precision split-11 local-log kernel

**Classification:** exact-arithmetic computational certificate *conditional on the formal-group normalization below*. **Review:** two AI-authored algorithms agree on P1/P2/P3/R/H; P4 has been checked by one algorithm only. Not externally peer-reviewed, not claimed novel.

Fix E : y²=x³−1267x+17230, K=Q(√−7), and p=11. Let P1=(15,40), P2=(19,4), P3=(23,16), P4=(31,88), and H=((37+3√−7)/2,−16+12√−7). The four rational points are a permutation of the generators listed by [LMFDB](https://www.lmfdb.org/EllipticCurve/Q/234446/a/1). Their independence **over Q** is recorded there; this computation does not independently verify a full K-basis.

Let λ₊,λ₋ be the two normalized local elliptic logarithms, defined by (1/11)log_E at the embeddings √−7↦156785,4266 (mod 11⁵), using ω=dx/(2y). As #E(F₁₁)=18 and 18 is an 11-adic unit, the logarithm can be computed via [18]P and the formal parameter t=−x/y. On the integral good-reduction short model, the invariant differential has a series with integral coefficients and starts 1+O(t⁴), hence log_E(t) = t + O(t⁵). For t ∈ 11Z₁₁ the terms of the remaining logarithm series have valuation at least 5 (including possible denominators divisible by 11), so log_E([18]P)/11 equals t([18]P)/11 modulo 11⁴. No floating point is used.

The exact program produces the matrix, **modulo 14641**, with columns P1,P2,P3,P4,H:

```
           P1     P2     P3     P4     H
lambda+  7462  14432   1427   7989   1495
lambda-  7462  14432   1427   7989   7921
```

The two rows differ only in the H column, by 6426 ≡ 2 (mod 11), a unit. The P1 entry 7462 ≡ 4 (mod 11) is also a unit. Therefore the map from the *abstract coefficient module* (Z/14641)^5 onto (Z/14641)^2 is surjective, and its kernel is free of rank 3 with basis

```
P2 -  8690 P1
P3 - 14082 P1
P4 - 12835 P1   (mod 14641).
```

Here symbols refer to coefficient vectors; this is **not** a claim that those literal large multiples are zero in E(K). Rather their normalized local logarithms vanish to the specified precision. At precision 11² the coefficients reduce to 99, 46 and 9 respectively, matching C-0001. The minor det(P1,H) = 1537 (mod 14641) is 8 (mod 11).

## Reproduce

From repository root (Python standard library; imports existing C-0001 verifiers):

```bash
python3 -I -B research/split11/kernel_mod11_4.py
```

The script recomputes all six logarithm columns via exact number-field arithmetic and rechecks P1/P2/P3/R/H by modular projective arithmetic. P4 is **not** independently verified by the second algorithm because its projective coordinates are nonprimitive. Reviewers should cross-check with Sage, PARI/GP or a third implementation; confirm the series truncation, unit hypotheses and embedding normalization.

## Additional independent algorithm and scale-safe falsification

[Session 12](LOCAL_GLOBAL_ALIGNMENT_AUDIT.md) supplies an independent guarded-precision Jacobian computation including **P4**, plus a primitive projective gate for speculative local/global height alignment. Its mod-11 necessary profile is [1:0:2:9]; a common 11-power in a height vector can fake raw wedge vanishing, so the [negative control](../methodology/height_alignment_scale_gate.py) divides out that factor. Neither test computes a genuine anticyclotomic height, Sha, or complex L''.

## Why this is not yet a derived-height computation

The kernel of a local logarithm map is **not canonically identified** with the radical of an anticyclotomic p-adic height pairing. A putative anticyclotomic first-height matrix on four positive and one negative conjugation eigendirections has off-diagonal form determined by an unknown four-component functional. Our local map supplies a *different* functional on the rational eigenspace. Two nonzero functionals on a four-dimensional vector space can have different three-dimensional kernels.

Before using this in BSD-related conjectures, compute the anticyclotomic heights with a specified splitting/character and verify the relevant Selmer-complex hypotheses. Compare with [Agboola–Castella (2021)](https://www.numdam.org/articles/10.5802/jtnb.1174/). Do **not** substitute Sage's cyclotomic p-adic height for the anticyclotomic pairing: [Sage's documented height routine](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html) is cyclotomic.

**Scope:** an exact finite-precision local algebra calculation, not a proof of analytic rank four, a nonzero derived height, or BSD. Human–AI exploratory work, 17 October 2026.
