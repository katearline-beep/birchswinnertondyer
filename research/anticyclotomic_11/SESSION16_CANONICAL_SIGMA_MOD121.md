# Session 16 — Canonical 11-adic sigma coefficient and provisional global heights modulo 121

**2026-10-19 · AI-authored and internally reproducible · mathematical literature dependencies explicit · external Sage/Magma or expert review not completed.**

## Whole BSD context and exact question

Our target remains BSD for \(E/\mathbb Q\) with minimal equation \(y^2+xy=x^3-x^2-79x+289\), conductor 234446, algebraic rank four, and no project proof of the **original complex** \(L''(E,1)=0\). Global **anticyclotomic \(11\)-adic heights** are different invariants and a potentially informative H2 subproblem, not a theorem connecting rational rank to complex vanishing.

The falsifiable Session 16 question is: can the canonical Mazur–Tate sigma coefficient be recovered without Sage, so that the four **provisional** first anticyclotomic height digits from C-0011 can be independently extended to **two** 11-adic digits? Then do the six genuinely mixed \(P_i+P_j+R\) checks still pass?

## A published integrality algorithm, not an arbitrary sigma parameter

Mazur–Stein–Tate, [*p-Adic Heights and Log Convergence* (2006)](https://ems.press/content/book-chapter-files/27479), Algorithms 3.1 and 3.3, describe the canonical sigma series with **two different conventions**: their sigma-series auxiliary variable \(c_{\mathrm{series}}=E_2/12\) (the coefficient in \(\exp(c_{\mathrm{series}}z^2/2)\)) and the PARI/MST slope \(s_2=(b_2-E_2)/12=b_2/12-c_{\mathrm{series}}\). Here \(b_2=a_1^2+4a_2=-3\) for our minimal model. The **canonical sigma-series parameter** is constrained by integrality of the coefficients of the canonical sigma series. Here the first informative denominator is the coefficient of \(t^{13}\).

For \(t=-x/y\), \(w=-1/y\), on \(y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6\), use the exact formal equation
\[
w=t^3+a_1tw+a_2t^2w+a_3w^2+a_4tw^2+a_6w^3.
\]
The invariant differential defines
\[
z'(t)=\frac{w-tw'}{w(-2+a_1t+a_3w)},\quad z(0)=0.
\]
Write \(\wp(z)=z^{-2}+\sum_{k\ge1}w_kz^{2k}\), with \(w_1=g_2/20,\ w_2=g_3/28,\ g_2=c_4/12,\ g_3=c_6/216\); the remaining \(w_k\) satisfy \(\wp''=6\wp^2-g_2/2\). The Mazur–Tate formula is
\[
\frac{d^2}{dz^2}\log(\sigma_c(z)/z)=z^{-2}-\wp(z)+c.
\]
Therefore \(\sigma_c(z(t))=\sigma_0(z(t))\exp(c\,z(t)^2/2)\), enabling a **pure-standard-library**, exactly rational formal-series computation of every coefficient as a polynomial in \(c\), without a CAS or p-adic floating point.

The complete derived coefficient is
\[
[t^{13}]\sigma_c(t)=
\frac{
1774080c^6+292723200c^5-61449474240c^4
-3609872323200c^3+414591819943752c^2
+2098715391767160c-106502304179884375
}{81749606400}.
\]
The denominator has \(v_{11}=1\); every \(c\in\{0,\ldots,10\}\) except \(c=4\) gives a coefficient with \(11\)-adic valuation \(-1\). Thus **under the published Mazur–Tate integrality theorem**, the unique candidate is
\[
\boxed{c_{\mathrm{series},11}\equiv4\pmod{11},\quad E_2=12c_{\mathrm{series},11}\equiv4\pmod{11},\quad s_2\equiv4\pmod{11}.}
\]
At the precision needed here,
\[
\boxed{\sigma_{11}(t)/t=1+\tfrac12t+\tfrac{c_{11}}2t^2+O(t^3).}
\]

**Independent published sanity control:** the exact same implementation reconstructs the published conductor-37 \(E:y^2+y=x^3-x\), \(p=5\) coefficient
\[
[t^7]\sigma_c(t)=103/120-(73/120)c+(1/48)c^3,
\]
with unique \(c_5\equiv1\pmod5\), as displayed by Mazur–Stein–Tate in their §4.1 worked example. This is stronger than asserting our target expression against its own hardcoded polynomial, but the formal-series code remains AI authored and is not independently reviewed.

Source: [canonical_sigma_integrality_11.py](canonical_sigma_integrality_11.py).

## Heights one digit higher: ten full denominator checks and six independent mixed points

With \(K=\mathbb Q(\sqrt{-7})\), \(R\) anti-invariant, \(P_i\) invariant, \(\sigma_\rho(t)/t\) as above, and the \([36]\)-multiple in both formal groups, [conditional_heights_mod121.py](conditional_heights_mod121.py) implements BCLMN [Proposition 2.4 / Algorithm 4.2](https://arxiv.org/pdf/1610.08729).

For \(Q\in E(K)\) and \(T=[36]Q\), the global ideal generator \(D\) must be **primitive**, checked directly at \(T\) using exact affine multiplication:
\[
x(T)D^2,y(T)D^3\in\mathcal O_K,\qquad
\gcd_{\mathbb Z}(N(x(T)D^2),N(D))=1.
\]
The two 11-adic embeddings produce the normalized units
\[
u_\pm=\left(\frac{t_\pm}{D_\pm}\right)
\left(1+\frac{t_\pm}{2}+\frac{4t_\pm^2}{2}\right)
\pmod{11^3},\quad
q=u_+/u_-,
\]
and the height
\[
h_\rho(Q)=36^{-2}11^{-1}\log_{11}(q)\pmod{121}.
\]
If \(z=q^{10}-1\bmod11^3\), we compute \(11^{-1}\log_{11}(q)\equiv(z-z^2/2)/(11\cdot10)\pmod{121}\). Full \(11\)-adic logarithm branch, character orientation, minimal differential and denominator ratios follow the published convention; a third-party implementation is still required.

| \(Q\) | \(q\bmod 1331\) | Provisional \(h_\rho(Q)\bmod121\) |
|---|---:|---:|
| \(P_1+R\) | 1147 | **100** |
| \(P_2+R\) | 925 | **90** |
| \(P_3+R\) | 675 | **7** |
| \(P_4+R\) | 236 | **8** |
| \(P_1+P_2+R\) | 168 | 69 |
| \(P_1+P_3+R\) | 914 | 107 |
| \(P_1+P_4+R\) | 499 | 108 |
| \(P_2+P_3+R\) | 136 | 97 |
| \(P_2+P_4+R\) | 16 | 98 |
| \(P_3+P_4+R\) | 911 | 15 |

All six mixed heights equal the corresponding **sums** of the first four heights modulo \(121\), not just modulo 11. Every denominator is checked primitive at the full \([36]Q\) point. The deliberately wrong sigma coefficient \(c=0\) changes the second digits but leaves the first unchanged, demonstrating that our new precision actually tests the canonical sigma input.

## Conditional radical at precision 121; correct modular division

Our published C-0002 local-log projective vector reduces to \([1:99:46:9]\pmod{121}\) after division by its first unit entry. The **global self-height** vector is
\[
(100,90,7,8)\pmod{121}.
\]
Since \(100^{-1}\equiv23\pmod{121}\), its projective profile is **exactly**
\[
\boxed{[1:13:40:63]\pmod{121}.}
\]
The conditional first-height positive-direction radical therefore has coefficient-kernel generators modulo 121
\[
P_2-13P_1,\quad P_3-40P_1,\quad P_4-63P_1.
\]
These are **modular approximations to a \(\mathbb Q_{11}\)-subspace**, not literal global height-zero Mordell–Weil points. The local-log and provisional global-height profiles already differ modulo 11, so the auxiliary L11 equality remains strongly disfavored, conditionally on the global height source and arithmetic.

**Correction log:** an intermediate assistant-facing update accidentally wrote coefficients 25,46,92; direct unit inversion showed them wrong. This research note and executable assertions use the **correct** 13,40,63. Preserve the correction; never copy unchecked hand-computed modular ratios into the harness.

## Claim boundaries and next experiment

- The symbolic coefficient and conductor-37 control give a new **internal**, reproducible computation (C-0012). These two 11-adic digits remain **conditional on published Mazur–Tate/BCLMN theorems and the implementation**, not independently certified by external Sage/Magma and no human mathematical peer review.
- No higher derived anticyclotomic height, Sha finiteness, or original **complex \(L''(E,1)=0\)** is proved. This does not address general BSD.
- Before increasing height precision beyond two digits, obtain an *independently maintained* Sage \`padic_E2/padic_sigma\` computation on the exact minimal model and check the \(c_{11}\) and height normalization. The full code is also independently checkable with Magma.
- If those checks succeed, lift the **global** positive radical to higher precision and compute a *derived* pairing; do not revert to the mismatched two-prime local-log kernel. Maintain a separate H3 route targeting a true **complex third-derivative** geometric identity. Our H2 work still has **no comparison theorem** implying \(L''(E,1)=0\).

**Reproduce:**
\`\`\`bash
python3 -I -B research/anticyclotomic_11/canonical_sigma_integrality_11.py
python3 -I -B research/anticyclotomic_11/conditional_heights_mod121.py
\`\`\`


**Correction (2026-10-19, independently exposed by PARI):** The symbol `c` in the polynomial `sigma_0(z)*exp(c*z²/2)` is the *series auxiliary parameter* `u=E2/12`. It is not PARI's `ellpadics2` return `s2=b2/12-u`. These coincide modulo 11 **for this curve by accident**, but diverge at higher precision. All self-height coefficients used the series `u` and are numerically unchanged; the displayed relation `E2=b2−12c` was incorrect and must be read as `E2=12u`. The Session17 [PARI oracle](pari_canonical_sigma_oracle.gp) tests both conventions explicitly.
