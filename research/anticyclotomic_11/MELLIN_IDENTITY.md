# Twist root sign and Mellin derivative identity: auditable mathematics

**Status:** specialization of established results, with exact local-data checks. This note is not an independently reviewed analytic-rank theorem or a BSD proof. It is part of the experiment EX-002 hypothesis audit.

## 1. Objects and exact local conditions

Use the minimal model `E:y²+xy=x³−x²−79x+289`, conductor `N=234446=2×117223`, discriminant `Δ=4×117223`, and `c4=3801`. Let `K=Q(√−7)`, fundamental discriminant `D=−7`, and `Et=E^D` be the quadratic twist.

- At 2, `v_2(Δ)=2` and `c4` is a 2-adic unit: multiplicative reduction; counting the minimal fiber gives `a_2=−1`, **nonsplit**.
- At 117223, `v_q(Δ)=1` and `c4` is a q-adic unit: multiplicative reduction. `−c6 ≡ 115382 (mod q)` is a nonzero quadratic residue, so it is **split** and `a_q=+1`.
- The global root number is the archimedean factor −1 times local factors `−a_l` at multiplicative primes: `w(E)= (−1)(+1)(−1)=+1`.
- The quadratic character modulo 7 has residues `χ_{−7}(1)=χ_{−7}(2)=χ_{−7}(4)=+1`. As `q≡1 (mod 7)`, `χ_{−7}(-N)=-1`.
- For a **fundamental quadratic discriminant D coprime to conductor N**, the standard twist-sign formula is `w(E^D)=χ_D(-N)w(E)`; hence `w(Et)=-1`. The standard coprime-conductor formula gives `N(Et)=D² N=11,487,854`. Independently, PARI/GP reports this conductor and sign.

[An exact checker](verify_root_sign.py) verifies the minimal invariants, conductor factorization, local Legendre and character arithmetic, and predicted signs. The local-root and twist-sign theorems are inputs to the inference, not proved by the checker.

**References:** standard quadratic twist root-number argument [MathOverflow (with mathematical proof and citations)](https://mathoverflow.net/questions/157631/root-number-of-a-quadratic-twist-of-an-elliptic-curve), and [Kellock, *Root numbers and parity phenomena*, Bulletin of the London Mathematical Society (2023), §2.3](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/blms.12931). A qualified reviewer should check local factors at p=2.

## 2. Exact series formula for the derivative

By the **modularity theorem for elliptic curves over Q** (and twisting of weight-two newforms), let `b_n=a_n χ_D(n)` be the coefficients of `Et`. Its level is `M=49N`. Set

```
c = 2π/√M,
F(t) = Σ_(n≥1) b_n exp(-c n t),
Λ(s) = c^(-s) Γ(s) L(Et,s).
```

Thus `Λ(s)=∫_0^∞ F(t)t^(s−1)dt` initially in the convergence half-plane. The completed L-function has functional equation `Λ(s)=w(Et)Λ(2−s)`. Equivalently, the modular transformation gives

```
F(1/t) = w(Et)*t²*F(t),     t>0.
```

Splitting the integral at 1 and changing variables in its (0,1) part yields the analytic continuation

```
Λ(s) = ∫_1^∞ F(t) [t^(s−1) + w(Et)*t^(1−s)] dt.
```

Since `w(Et)=−1`, `Λ(1)=L(Et,1)=0` and

```
Λ'(1) = 2 ∫_1^∞ F(t) log(t) dt.
```

The identity `∫_1^∞ e^(−x t)log(t)dt = E1(x)/x` follows by integration by parts, for `x>0`, where `E1(x)=∫_x^∞e^(−u)du/u`. Because `L(1)=0`, differentiating the gamma/conductor factor adds no surviving term: `L'(1)=c Λ'(1)`. Thus

```
L'(Et,1) = 2 Σ_(n≥1) [b_n/n] E1(c n).
```

The derivation relies on modularity, the weight-two functional equation and justified interchanges of uniformly exponentially converging series and integrals for `t≥1`. It is **not** an identity inferred by curve point-counting alone.

An independent established implementation documents this very formula, including the factor two, under its `deriv_at1()` routine: [SageMath's elliptic L-series manual](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/lseries_ell.html). See also Henri Cohen, *A Course in Computational Algebraic Number Theory*, §7.5.3.

## 3. A uniform Fourier-coefficient and tail bound

For a good prime \(\ell\), the local Euler factor is \(1-a_\ell T+\ell T^2\). The Hasse bound ensures that its reciprocal roots \(\alpha,\beta\) satisfy \(|\alpha|=|\beta|=\sqrt{\ell}\), so its power-series coefficient obeys \(|a_{\ell^k}|\le (k+1)\ell^{k/2}\). At a multiplicative bad prime (here 2 and 117223), the local factor is \((1-a_\ell T)^{-1}\), with \(a_\ell=\pm1\), so the same estimate holds trivially. By multiplicativity, for **every** integer \(n\ge1\) we obtain \(|a_n|\le d(n)\sqrt n\le 2n\), where \(d(n)\le2\sqrt n\) follows by pairing each divisor with its complementary divisor. Twisting by \(\chi_{-7}\) can only remove terms or change their signs.

For positive \(x\), \(E_1(x)=\int_x^\infty e^{-u}\,du/u\le e^{-x}/x\). Writing \(c\ge c_0>0\) and \(q=(1+c_0)^{-1}\) yields \(e^{-cn}\le q^n\), since \(e^{c_0}\ge1+c_0\). Therefore the complete tail after M terms satisfies

\[
\left|2\sum_{n>M}\frac{a_n\chi_{-7}(n)}{n}E_1(cn)\right|
\le\frac{4q^{M+1}}{c_0(M+1)(1-q)}.
\]

This is the algebraic tail inequality in our scripts. It follows from **standard elliptic local Euler factors, the Hasse bound, multiplicativity and elementary analysis**. The root-sign and Fourier coefficient series must refer to the *same* newform and conductor. The independent PARI oracle has checked all coefficients \(a_n\) **for n≤2000 only**; 117223 exceeds that range, and its bad Euler factor is justified by the separate multiplicative-reduction argument.

## 4. What was computationally corroborated

The exact rational program [independent_rational_derivative.py](independent_rational_derivative.py) computes 2,000 terms and an explicit entire tail, conditional on the formula above. GitHub Actions additionally compares **every original curve Fourier coefficient** `a_1,…,a_2000` against PARI's independent `ellan(E,2000)` implementation, not just the first few terms. [GP oracle](../harness/pari_fourier.gp) and [comparator](../harness/compare_fourier_coefficients.py). It tests a deliberately corrupted coefficient.

The coefficient comparison validates the arithmetic *implementation* of `a_n`; the twist formula and the tail's **mathematical inequalities** remain logical inputs requiring human review. The root number and conductor are also cross-checked numerically/arithmetically by PARI. [Current audit and claims](DERIVATIVE_CERTIFICATE_AUDIT.md).

**Stop rule:** If any local factor, analytic normalization, sign or tail enclosure is unproved or contradictory, downgrade the analytic nonvanishing claim. None of this proves the original rank-four BSD conjecture.
