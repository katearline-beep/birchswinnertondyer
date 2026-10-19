# Session 14 — Exact denominator ideals, first 11-adic height digits, and a falsified *candidate* alignment

**Date:** 2026-10-19. **Status:** AI-authored, computationally reproduced in two multiplication arrangements and quadraticity control, **provisional pending independent Sage/PARI mathematical review**. This is not a proof of BSD or any statement about the original complex \(L''(E,1)\).

## The real problem, unchanged

For the rational elliptic curve \(E: Y^2+XY=X^3-X^2-79X+289\) (234446.a1), the original complex analytic assertion \(L''(E,1)=0\) remains **unproved** here. Our calculations below concern a different, global **anticyclotomic 11-adic height**. The height may be a useful arithmetic invariant, but p-adic height computations do not imply complex derivative vanishing.

We use the equivalent short model \(W^2=Z^3-1267Z+17230\), \(K=\mathbb Q(w)\) with \(w^2=-7\), \(P_i=(15,40),(19,4),(23,16),(31,88)\), and \(R=(-3355/63,(128780/1323)w)\), with \(A_i=P_i+R\).

### 1. Exact *ideal* denominator generators for \(A_i\)

Writing \(\omega=(1+w)/2\), \(\mathcal O_K=\mathbb Z[\omega]\), all four points have \(\delta(A_i)=(d_i)^2\) on the minimal model. The exact generators and their norms are

| \(i\) | \(d_i\) | \(N(d_i)\) |
|---|---|---:|
| 1 | \(5(7-2\omega)\) | 1075 |
| 2 | \((1-\omega)(19-16\omega)\) | 1138 |
| 3 | \(29+8\omega\) | 1201 |
| 4 | \(-1+26\omega\) | 1327 |

This refines Session 13's *rational coefficient denominator candidates*, which do not identify which split prime ideal occurs. Example: at 43 only one of the conjugate prime ideals appears in \(\delta(A_1)\). To prove the exact ideals without integer factorization, use \(x(A)=(u+v\omega)/D\) with coprime rational coefficient denominator \(D\), compute \(G=\gcd_{\mathcal O_K}(u+v\omega,D)\) using exact Euclidean division, and verify
\[
N(\delta(A))=D^2/N(G)=N(d)^2,\quad x(A)d^2,\;Y(A)d^3\in\mathcal O_K.
\]
These conditions force equality of denominator ideals. The verifier checks each Euclidean remainder decreases norm, all inclusions, and the exact norm equality.

### 2. A necessary bad-component correction at 2

Let \(B_i=2A_i\). Computing the *primitive* square-root denominator generators produces
\[
\boxed{d(B_i)=\frac{\psi_2(A_i)d(A_i)^4}{c_i}},\qquad (c_1,c_2,c_3,c_4)=(2,1,2,2),
\]
where \(\psi_2(A)=2Y(A)+X(A)=W(A)/4\) on the minimal equation. Their exact norms are
\[
\bigl(N(d(B_1)),N(d(B_2)),N(d(B_3)),N(d(B_4))\bigr)
=(47295512879050,\;9503262597784,\;9476672644861,\;224062363149514).
\]

**Negative control:** Omitting \(c_i=2\) for \(i=1,3,4\) yields algebraic integers that clear both coordinate denominators but are *not primitive*: their putative denominator-ideal norms are inflated by precisely \(2^4=16\). All four corrected generators are proved by the independent norm-Euclidean gcd criterion. This illustrates why BCLMN Algorithm 4.2 first multiplies into identity components at bad primes. The observed correction at 2 is specific to these points, **not** a universal replacement formula.

### 3. Computing global denominator generators of \([36]A_i\) without factoring huge coordinates

The minimal discriminant has bad-component exponents killed by \(m_0=2\), and \(\#E(\mathbb F_{11})=18\) at both split primes. Thus \(T_i=[36]A_i=[18]B_i\) lies in the connected components at bad primes and in the formal groups at the primes above 11.

For \(B_i=2A_i\), set
\[
F_n(B_i)=\psi_n(B_i)d(B_i)^{n^2-1}\in\mathcal O_K.
\]
The integral elliptic division-polynomial recurrences compute \(F_n\) from scaled integral coordinates. BCLMN Algorithm 4.2, Step (5), gives
\[
\boxed{d(T_i)=F_{18}(B_i)d(B_i).}
\]
No 4,000-digit integer factorization is needed. The executable implementation verifies the formula independently using \(C_i=[4]A_i\):
\[
\boxed{F_{18}(B_i)d(B_i)=\pm F_9(C_i)d(C_i)}
\]
**exactly as algebraic integers**. It also checks the same generators against independently computed coordinate denominator ideals for multipliers \(2,3,4\) of \(B_i\). Their norms at \(T_i\) have roughly 4,500–4,900 decimal digits.

### 4. Only the first 11-adic digit needs the universal sigma quadratic coefficient

BCLMN [Proposition 2.4 and Algorithm 4.2](https://arxiv.org/pdf/1610.08729) state for \(T_i\)
\[
h_\rho(T_i)=\frac1{11}\log_{11}\left(
\frac{\sigma_{11}(t_{i,+})}{\sigma_{11}(t_{i,-})}
\frac{d(T_i)_{-}}{d(T_i)_{+}}\right),
\qquad h_\rho(A_i)=\frac{h_\rho(T_i)}{36^2}.
\]
Here \(t=-X/Y\) on the *minimal model*. We compute its two embeddings by Jacobian arithmetic on the short model and the **explicit algebraic** isomorphism between models, rather than inferring a global height from a local log.

On the minimal model, \(a_1=1\). The Mazur–Tate sigma function is odd under the *formal inverse*. That inverse has \(t\mapsto-t-a_1t^2+O(t^3)\), forcing
\[
\sigma_{11}(t)=t+\frac12t^2+O(t^3).
\]
Because each \(t_{i,\pm}\) has 11-adic valuation **one**, and the sigma power series has integral 11-adic coefficients, the \(O(t^3)\) term cannot affect the first digit of \((1/11)\log_{11}\) after dividing by the equally valued denominator generator. **This conclusion relies on the standard Mazur–Tate integrality and normalization theorem**, not on an independently computed full sigma series.

The resulting unit quotients \(q_i\bmod121\) and normalized self-height residues are:

| \(i\) | \(q_i\pmod{121}\) | \(h_\rho(36A_i)\pmod{11}\) | \(h_\rho(A_i)\pmod{11}\) |
|---|---:|---:|---:|
| 1 | 58 | 9 | 1 |
| 2 | 78 | 7 | 2 |
| 3 | 70 | 8 | 7 |
| 4 | 115 | 6 | 8 |

We use the Fermat quotient \(\frac1{11}\log_{11}(q)\equiv \frac{q^{10}-1}{11\cdot10}\pmod{11}\), valid for any 11-adic unit under \(\log_{11}(11)=0\). As a separate homogeneity check, computing \(h_\rho(72A_i)\) with a separately constructed \(d(72A_i)=F_{18}(4A_i)d(4A_i)\) yields **four times** \(h_\rho(36A_i)\) in every case.

Thus the implementation gives the **provisional** 11-adic height vector
\[
\boxed{(h_\rho(A_1),h_\rho(A_2),h_\rho(A_3),h_\rho(A_4))\equiv(1,2,7,8)\pmod{11}.}
\]

### 5. Consequence for L11, conditional on the mathematical audit

The published local-logarithm matrix (C-0002) has primitive projective vector \([1:0:2:9]\) modulo 11. By anti-invariance, polarization relates our self-heights to the four global cross-pairings by **one common nonzero factor** (depending only on the bilinear-height convention). Therefore, if the source normalization and the implementation above are correct, the primitive global cross-height vector \([1:2:7:8]\) differs from the local one already in the second coordinate.

**Conditional conclusion:** the speculative *L11 local-global kernel alignment* is **falsified**, rather than supported. This is **not** a falsification of any established theorem, nor of BSD, and **not** evidence that the global first-height radical cannot be computed. The broader H2 mixed-Bockstein/derived-height route remains separate.

### 6. Review gates and next steps

**Required independent audit before promoting the result:** reproduce the first digit with Sage's actual \`EllipticCurve(...).padic_sigma(11,N)\` series and Magma/PARI or an independent elliptic division-polynomial implementation; verify the exact sign and the invariant-differential normalization in BCLMN Proposition 2.4, including the minimal-vs-short model. Check both split embeddings, ideal orientations, and the published rank-two 389a1 control.

The executable [provisional_height_mod11.py](provisional_height_mod11.py) runs entirely in the Python standard library with exact rational/number-field arithmetic and no factorization of huge integers; it checks prime-ideal primitivity, two distinct denominator paths, low-multiple ideal norms, and height quadraticity at 36/72. **Passing its own assertions is not independent expert review.**

**Next mathematics:** reconstruct or independently compute global anticyclotomic heights with more than one 11-adic digit, establish actual first-height radical, then evaluate the genuinely derived height on that radical. This remains **p-adic BSD research**, not the absent complex \(L''(E,1)\) bridge.

**References:** BCLMN (2016), [Shadow Lines in the Arithmetic of Elliptic Curves](https://arxiv.org/pdf/1610.08729), §1, Proposition 2.4, Algorithm 4.2; Mazur–Tate p-adic sigma function as documented by [SageMath](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html); [Session 13](SHADOW_LINES_HEIGHT_IMPLEMENTATION.md); [Session 12](../split11/LOCAL_GLOBAL_ALIGNMENT_AUDIT.md).

**What was proved about complex BSD in this session:** **nothing new**. This is a potentially substantive, but not externally certified, arithmetic computation and a negative test of a speculative auxiliary conjecture.
