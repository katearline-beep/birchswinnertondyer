# Session 13 — A published global-height algorithm and exact anticyclotomic character data

**2026-10-19 · internal AI-assisted reproducibility note · not externally reviewed.**

## Why this changes the implementation plan

Balakrishnan–Çiperiani–Lang–Mirza–Newton, *Shadow Lines in the Arithmetic of Elliptic Curves* (2016), [author PDF](https://math.bu.edu/people/jbala/ShadowLines.pdf), [arXiv 1610.08729](https://arxiv.org/abs/1610.08729), contains an **elliptic-curve-specific algorithm** for anticyclotomic p-adic heights. Its Proposition 1.4 gives an explicit idèle class character for a class-number-one imaginary quadratic field; Proposition 2.4 relates the self-height to p-adic sigma functions and denominator ideals; Algorithm 4.2 calculates the height; Algorithm 4.3 specializes to rank-two shadow lines.

**Important distinction:** the standalone *height construction* in Algorithm 4.2 accepts an arbitrary nontorsion P∈E(K), assuming good ordinary p, p split in K and conditions enforced by its multiples. The *shadow-line interpretation* in Algorithms 4.1/4.3 assumes analytic ranks 2 and 3, **not satisfied or proved for our rank-four/five case**. Adapt the height calculation, not those rank-two conclusions. An external mathematical review of this applicability distinction remains necessary.

## Height polarization turns the four cross-pairings into four self-heights

Our short-model E is y²=x³−1267x+17230 with four rational points P1=(15,40), P2=(19,4), P3=(23,16), P4=(31,88), and R=(−3355/63,(128780/1323)√−7), satisfying σ(Pi)=Pi, σ(R)=−R.

Let h_ρ be a **symmetric** anticyclotomic p-adic height pairing with h_ρ(σX,σY)=−h_ρ(X,Y). Then h_ρ(Pi,Pi)=h_ρ(R,R)=0, and, setting Ai=Pi+R,

```
h_ρ(Ai,Ai) = 2 h_ρ(Pi,R).
h_ρ(Pi+Pj+R,Pi+Pj+R) = h_ρ(Ai,Ai)+h_ρ(Aj,Aj).
```

Therefore the projective vector of four self-heights equals the projective cross-height vector relevant to the L11 test (common unit 2 does not affect any ratios). The second equation is a required **bilinearity negative control** for a future implementation. This formal implication is independent of assuming the conjectural height-kernel alignment.

## Fix an explicit class-number-one anticyclotomic character

Let K=Q(w), w²=−7, ω=(1+w)/2, O_K=Z[ω], N(a+bω)=a²+ab+2b². The Minkowski bound for imaginary quadratic discriminant −7 is (2/π)√7<2, proving class number one. Set p=11; the two embeddings are w↦w₊≡2 and w↦w₋≡−2 mod11. Let log₁₁(11)=0 and log₁₁ be zero on roots of unity. We adopt the **Proposition 1.4 normalization** ρ=(1/11)log₁₁ of the quotient of the two p-local unit components, with the + embedding specified first.

For a split prime q≠11 and a prime ideal (α) above q with α=a+bω and N(α)=q, Proposition 1.4 gives

```
ρ_𝔮(uniformizer α) = -(1/11) log_11(α₊/α₋).
ρ_{conj 𝔮}(conj α) = -ρ_𝔮(α).
```

This is an **unramified local character coefficient**, not an elliptic local height; the conjugate orientation changes its sign. For inert q, the prime ideal (q) is conjugation-fixed; for ramified 7, its prime is also fixed. Lemma 2.2 of the paper makes these coefficients zero.

Using Hensel roots modulo 11¹⁰ and an exact finite p-adic logarithm series, [the executable program](character_coefficients.py) obtains:

| q | generator a+bω (norm q) | ρ_𝔮 modulo 11⁴ | residue modulo 11 |
|---:|---|---:|---:|
| 2 | 0+ω | 12285 | 9 |
| 43 | 5+2ω | 8549 | 2 |
| 569 | 3+16ω | 6736 | 4 |
| 1201 | 29+8ω | 8230 | 2 |
| 1327 | −1+26ω | 2819 | 3 |
| 117223 | 65+222ω | 5836 | 6 |

The script checks norms, conjugation sign, additive logarithm properties, inert/ramified vanishing, and the **independent mod-11 Fermat-quotient formula**. Exact p-adic residues are only as strong as the source character normalization and log-series proof, still subject to external review. Do **not** substitute this table for global heights.

## Concrete elliptic points on the minimal equation

The original minimal model is `Y²+XY=X³−X²−79X+289`, obtained from the short model by X=(x+1)/4, Y=(y−x−1)/8. Exact field arithmetic in [point_prerequisites.py](point_prerequisites.py) gives the following **rational coefficient denominator supports** for Ai=Pi+R:

| Point | primes in denominators of X(Ai), Y(Ai) |
|---|---|
| A1 | 5, 43 |
| A2 | 2, 569 |
| A3 | 1201 |
| A4 | 1327 |

These are **not** exact local denominator-ideal valuations; cancellations can occur in O_K (especially at 2). At 5, which is inert in K, the local anticyclotomic character is zero. Bad primes 2 and 117223 split and cannot be discarded. Most importantly, the local denominator ideal of **T=[n m₀]Ai**, not just Ai, is needed in Proposition 2.4; new primes can appear after multiplication. No local height sum has been performed.

The minimal discriminant has valuations 2 at prime 2 and 1 at 117223 (both multiplicative, I₂ and I₁). Every bad component group is killed by 2; both local reduction groups at p=11 have order 18. Thus **[36]Ai** is a convenient safe multiple that reaches the identity components at bad primes and the formal group at the two primes above 11; it need not be the smallest choice. This does not compute the sigma-function or division-polynomial denominator of [36]Ai.

## Next precise algorithmic target and nonclaims

1. Independently check the author's Proposition 2.4 sign and normalization against the printed source (they explicitly note a corrected sign relative to an older reference).
2. Implement/verify the 11-adic sigma function for the minimal model, and establish enough guard precision for `σ([36]Ai)` at **both embeddings**.
3. Compute the **global denominator ideal** of X([36]Ai), or use the division polynomial recurrence with a *certified* integrality/cancellation proof. Construct its generator `d_h([36]Ai)`, since class number h=1. Do not infer it by factoring the much smaller denominator of Ai.
4. Combine the sigma ratio with conjugate denominator ratio following the **published** formula, rescale by 36², and cross-check bilinearity on Pi+Pj+R and a rank-two published 389a1 example.
5. Only after genuine height values exist, use Session 12's primitive [1:0:2:9] necessary test. Even if it passes, **the complex L''(E,1)=0 gap persists**.

**Whole-BSD review:** Since the prior checkpoint, no missing implication from algebraic rank four to original complex L'' vanishing has been proved. The breakthrough here is *locating a suitable published arithmetic method and calculating one of its global-character ingredients*, not proving BSD, a new global height, or a previously unpublished mathematical theorem.
