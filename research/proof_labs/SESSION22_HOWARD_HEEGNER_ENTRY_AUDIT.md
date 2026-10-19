# Session 22 — Howard big Heegner class becomes a source-qualified candidate on the focal rank-four curve

**2026-10-19. Published theorem plus exact arithmetic checks, not an independent construction of a Heegner Euler system or a proof of BSD.**

Sources: Benjamin Howard, [*Variation of Heegner points in Hida families*, arXiv 1202.6358](https://arxiv.org/pdf/1202.6358), especially **Hypothesis 1.0.1** and §§2.1–2.4; [Castella–Hsieh (2022) Theorems 4.1/4.5](https://web.math.ucsb.edu/~castella/Kato.pdf); [Castella, *On the p-adic variation of Heegner points*](https://web.math.ucsb.edu/~castella/Heegner.pdf).

## Objective — an actual published candidate type, not a hypothetical new class

Our previous Session21 showed that CH Theorem 4.1's derived height filtration **exists** for the original rank-four elliptic curve at \(p=11,K=\mathbb Q(\sqrt{-7})\), but Theorem4.5's Coleman-map formula still requires an actual global Iwasawa class \(z\in\widehat H^1(K_\infty,V_{11}E)\) and its conjugate with verified augmentation filtration.

Howard constructs **norm-compatible big Heegner classes** in the extended Selmer/cohomology groups of a Hida-family representation \(T^\dagger\), under Hypothesis 1.0.1. The question is now concrete: does our original curve meet the theorem's actual entry conditions, so that we have a *published global-class construction to investigate* rather than designing one out of thin air?

### The original elliptic curve and Heegner setup

Use
\[
E:y^2+xy=x^3-x^2-79x+289,\quad N=2\cdot117223=234446,\quad p=11,
\quad K=\mathbb Q(\sqrt{-7}).
\]
Both bad primes **2 and 117223 split in K**, so there is an ideal \(\mathfrak N\subset\mathcal O_K\) of norm N with \(\mathcal O_K/\mathfrak N\simeq\mathbb Z/N\mathbb Z\) (Howard's Heegner splitting hypothesis). The Minkowski bound \((2/\pi)\sqrt7<2\) proves \(h_K=1\). The discriminant -7 is coprime to \(Np\); \(p=11\) splits, \(p\nmid 6N\) and \(p\nmid\phi(N)=117222\). Direct point count gives \(\#E(\mathbb F_{11})=18\), \(a_{11}=-6\): p is good ordinary, so the ordinary p-stabilization of its modular newform exists, with 11-adic unit root of \(X^2+6X+11\).

**The potentially hard residual hypothesis is also exactly testable**, without importing an LMFDB "maximal image" declaration.

## A two-Frobenius absolute-irreducibility certificate over G_K

The [independent stdlib verifier](howard_heegner_residual_focal.py) counts finite-field points **two different ways**: affine enumeration and Legendre-character sums. At good primes 23 and 43, both split in K:
\[
a_{23}(E)=-6,\qquad a_{43}(E)=-4.
\]
The mod11 Frobenius characteristic polynomial \(X^2-a_\ell X+\ell\) has discriminant
\[
D_{23}=(-6)^2-4(23)=-56\equiv10\pmod{11},
\qquad
D_{43}=(-4)^2-4(43)=-156\equiv9\pmod{11}.
\]

**First:** 10 is a nonsquare modulo11, so the characteristic polynomial at a split K-prime above 23 is irreducible over \(\mathbb F_{11}\). Therefore the restricted representation \(\bar\rho_{E,11}|_{G_K}\) has no invariant \(\mathbb F_{11}\)-line: it is **irreducible over \(\mathbb F_{11}\)**.

**Second, absolute irreducibility:** Suppose it became reducible over \(\overline{\mathbb F}_{11}\) despite F11-irreducibility. The invariant eigenlines would be interchanged by coefficient Frobenius and the representation would split over \(\mathbb F_{121}\) as \(\chi\oplus\chi^{11}\). For *every* group element, its two eigenvalues would be equal (discriminant zero) or form a nontrivial conjugate quadratic pair (nonsquare discriminant in F11). But Frobenius at the second split K-prime, 43, has discriminant \(9\)—a **nonzero square modulo11** and hence two *distinct* F11 eigenvalues. Contradiction.

Thus
\[
\boxed{\bar\rho_{E,11}|_{G_K}\ \text{is absolutely irreducible}.}
\]
This is a small rigorous arithmetic fact about the original curve (subject to correct local counting and standard Galois descent), stronger than Howard's absolute-irreducibility requirement over \(G_{\mathbb Q}\), and independent of the *provisional* anticyclotomic global height computations. The verifier also checks two split primes, K class-number bound, conductor factorization, ordinarity and wrong-prime controls.

## What Howard's theorem actually constructs and what is still missing

Howard Hypothesis 1.0.1:
- **(a)** \(p\nmid6N\): checked.
- **(b)** there is \(\mathfrak N\) with \(\mathcal O_K/\mathfrak N\simeq\mathbb Z/N\mathbb Z\): splitting of both conductor primes checked.
- **(c)** the residual semisimplified modular Galois representation is absolutely irreducible: independently verified above, even after restriction to \(G_K\).
- His introduction additionally assumes \(p\nmid\phi(N)\) and discriminant coprime N; both checked. Ordinary p-stabilization is available from \(a_{11}\ne0\bmod11\).

Under its precise setup, **Howard's published Hida-family theorem already constructs classes**
\[
\mathfrak X_c\in\widetilde H^1_f(H_c,T^\dagger)
\]
in Nekovář's extended Selmer group over ring class fields \(H_c\), with norm compatibilities forming an Euler system. At weight two, suitable specializations recover Kummer images of classical Heegner points. This is a **published existence construction** whose hypotheses we now have an arithmetic certificate for; we have not calculated \(\mathfrak X_c\) or its nonzero specialization for our actual E.

**The crucial typed-comparison gap remains:**
\[
\boxed{\mathfrak X_c\in\widetilde H^1_f(H_c,T^\dagger)}
\quad\xrightarrow[\text{projection, twist, limits, local conditions}]{\text{NOT constructed here}}\quad
\boxed{z\in\widehat H^1(K_\infty,V_{11}E)}
\quad\xrightarrow[\text{Coleman images in }J^r]{\text{NOT evaluated}}\quad
\boxed{h^{(r)}(\operatorname{pr}_Kz,\cdot).}
\]
Neither Howard's abstract existence, nor the ordinary p-stabilization, nor the p=11 local logs automatically supplies **CH Theorem4.5's two Coleman augmentation bounds**, a nonzero Bockstein derivative, or a comparison to **the original complex \(L''(E,1)\)**. The base-level Heegner class may vanish at augmentation in high rank even when a compatible tower class exists; such behavior is a *problem to analyze*, not evidence that a higher derived class has been constructed.

## Strategy and decisive follow-up

We can now replace the vague LF-007 instruction "invent some rank-four global class" with a sharply falsifiable **Howard-to-CH specialization audit**:

1. Check the exact tame-level and ordinary critical twist \(T^\dagger\), the weight-two arithmetic specialization, and the sequence of norm/corestriction maps down to anticyclotomic \(K_\infty\).
2. Write and verify a *typed* arrow from Howard's Nekovář extended Selmer class to the **specific** compact Iwasawa cohomology target demanded by CH4.5; identify possible missing local conditions at the two primes above 11.
3. Compute or bound the \(J\)-adic orders of **both** Coleman images, including the conjugate. If order is unknown, **do not apply** CH4.5 at positive \(r\).
4. Independently audit the normalization link between this CH derived \(h^{(1)}\) and our provisional BCLMN anticyclotomic height. Do not infer equality just from conjugation symmetry.
5. Require a **separate new theorem** before drawing conclusions about the original complex \(L''\), Sha or general BSD.

This does not eliminate the complex analytic-rank obstruction, but it gives the H1 derived-height program a **specific published global class family with independently checked hypotheses**, rather than a speculative unconstructed object. The geometric and mathematical novelty of the class is Howard's, not ours.

**Reproduce:**
\`\`\`bash
python3 -I -B research/proof_labs/howard_heegner_residual_focal.py
\`\`\`

No actual Heegner-class coordinates, higher Coleman logarithm, derived-height value or original complex BSD result is claimed.
