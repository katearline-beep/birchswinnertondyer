# Session 29 — one-sided Selmer control gives an exact second-height domain

**2026-10-19, America/New_York. AI-assisted, internally reproduced, not expert-reviewed.** Baseline `fa077743e001e5761b00a11bab62a90dadde24fb` / PR57. Original E=234446.a1, K=Q(sqrt(-7)), p=11. No original complex L'' theorem, full positive Selmer bound, or second-height value is claimed.

## Selected question, whole-problem review and decisive test

Must we prove the entire Selmer signature (4,1) before constructing any exact first-radical classes for h2? **No:** a one-dimensional **negative** Selmer eigenspace is enough for three height-defined positive classes. The existing twist-derivative certificate offers a source-derived way to establish that one-sided condition, without assuming the original curve's Sha is finite.

Safe lemma: identify the first-height normalization using a direct published comparison. Credible leapfrog LF013: use twist analytic rank one to construct a genuine three-dimensional subspace in S2, then evaluate the second Bockstein there. Wild alternative: a rank-sensitive complex cycle/period identity; no such theorem was found in the sources examined. H1/H2 remain active; H3 still lacks the complex third-derivative identity, H4/H6 remain parked and H5 remains diagnostic. **New implication toward original complex L''=0: none.** The new implications concern the twist and the domain of the arithmetic experiment.

Pass/fail chosen before computation: corroborate C0009 using independently maintained ball arithmetic, with the same 6000 coefficients/terms and the same tail; source-match first heights on Mordell–Weil classes; prove the one-sided lemma and exhibit a countermodel when its negative-dimension hypothesis is removed. Do not fabricate an arithmetic T³ Selmer presentation.

## C0031 — a direct comparison already exists; no number-field extrapolation is needed

Bertolini–Darmon, [*Derived p-adic heights*, author PDF](https://www.math.mcgill.ca/darmon/pub/Articles/Research/13.Derived-p-adic/paper.pdf), **Theorem2.18(4)** explicitly identifies the first derived height restricted to E(K)'s p-adic completion with the Mazur–Tate/Schneider height relative to the chosen Zp-extension. It is a theorem over the number field K, not restricted to Q. Its §1.1 assumptions are met on the recorded arithmetic inputs: p odd, good ordinary/non-anomalous at both p-places, p-prime-to-component groups, Cartan residual image; Proposition1.1 supplies local norm surjectivity. These are the C0003/20/30 source hypotheses, not fresh Galois-image results from a test script.

BCLMN [§2, equations(14)–(15)](https://arxiv.org/pdf/1610.08729) defines its quadratic self-height q(P)=h_rho(P) as **−1/2** of the universal Mazur–Tate bilinear self-pairing. For opposite conjugation eigenclasses P,R this gives the exact convention

\[
\lambda_\rho h^{(1)}_{BD}(P,R)=-q(P+R).
\]

Here lambda_rho identifies (J/J²) tensor Q11 with Q11 using **the same** anticyclotomic idele-class character and reciprocity convention as BCLMN. Reversing reciprocity or rescaling the character changes one common nonzero scalar, and cannot change the kernel or the ratios below. The ordinary unit-root choice is canonical; changing a splitting is a different pairing and cannot be treated as a harmless common rescaling.

Macias Castillo–Sano, [arXiv2603.23978v1 Theorem4.2](https://arxiv.org/pdf/2603.23978), has hBD=−hNek. Thus under matched conventions the first Bockstein/Nekovar cross row is **+q(P_i+R)**, while the BD row is its negative. No value of h2 follows from this comparison. In particular, the conventional half-polarization of q is not itself the published BD bilinear pairing; kernels still agree.

This shorter chain avoids an unnecessary gap: Balakrishnan–Besser's [Corollary4.3](https://arxiv.org/pdf/1201.6016) displays its global denominator formula over Q with a cyclotomic character. Its local unit-root comparison is useful, and Besser's [Theorem1.1](https://arxiv.org/pdf/math/0209006) compares Coleman–Gross with the older Nekovar construction for the same choices. Neither should be silently relabeled as the exact anticyclotomic global statement. BD Theorem2.18(4) and BCLMN's own bilinear convention supply the required direct bridge on Mordell–Weil classes.

## C0032 — independent Arb corroboration of the twist input

Write Et=E^(-7)/Q, conductor M=11487854, root sign−1. Modularity, the quadratic-twist functional equation and the Mellin calculation in the existing audit give

\[
L'(Et,1)=2\sum_{n\ge1}\frac{a_n\chi_{-7}(n)}n E_1(2\pi n/\sqrt M).
\]

The new [FLINT/Arb implementation](../anticyclotomic_11/arb_twist_derivative.py), pinned to python-flint0.9.0 at160 bits, uses the library's outward balls for pi, square root and E1. It imports none of the project's rational E1/gamma/log approximations. CI supplies a PARI `ellan` coefficient file; the standalone mode independently counts finite-field square frequencies. Both are required to match the existing full6000 coefficient SHA256. The same elementary |a_n|≤2n and geometric infinite-tail bound are retained: **no new terms or precision-only objective**.

Result: finite sum `[34.17203394870802891891059 +/- 3.60e-24]`; the full tail is bounded above by0.002895. The program certifies the rational inequalities **34.1691 < L'(Et,1) < 34.1750** using ball comparisons, rather than trusting printed rounded endpoints. A coefficient mutation is rejected; an artificially inflated error radius crosses zero and is correctly refused despite its positive midpoint. The original rational certificate remains separate, and agrees. The analytic identity, local factors and all-n bound are mathematical inputs documented in C0009; software success is not independent human review.

By the **Gross–Zagier–Kolyvagin theorem for elliptic curves over Q** (e.g. [Darmon Theorem3.22](https://www.math.mcgill.ca/darmon/pub/Articles/Research/36.NSF-CBMS/chapter.pdf)), accepting that certified nonvanishing and the exact sign gives

\[
\operatorname{rank}Et(\mathbb Q)=1,\qquad \Sha(Et/\mathbb Q)\text{ finite}.
\]

This applies to **Et/Q**, not Et/K (which is isomorphic to E/K), and not E/Q. The Tate module of a finite p-primary group is zero, even when its p-torsion is nonzero. Hence the rational p-adic Selmer exact sequence and quadratic restriction/corestriction give

\[
S^-:=\operatorname{Sel}(K,V_{11}E)^-
\simeq\operatorname{Sel}(\mathbb Q,V_{11}Et)
=Et(\mathbb Q)\otimes\mathbb Q_{11},\quad\dim S^-=1.
\]

This is a **source-derived consequence of the accepted analytic certificate**, retaining its review boundary, rather than a new unconditional expert-certified computation of an 11-Selmer group. It does not prove Sha(Et/Q)[11]=0, nor any Sha finiteness for E/Q or E/K. In particular a finite Sha can enlarge the mod11 Selmer group while contributing nothing to this Q11 Selmer dimension.

## The one-sided lemma and actual classes it defines

Let S=S+ direct-sum S− be the full Q11 Selmer space with its symmetric anticyclotomic first height b. Assume dim S−=1, generated by the known nonzero Kummer class R. Let P1,...,P4 be the known independent positive Mordell–Weil classes, and put **exactly**

\[
a_i=q(P_i+R),\qquad
X_j=P_j-(a_j/a_1)P_1\quad(j=2,3,4),\qquad a_1\ne0.
\]

The canonical height defines these coefficients as Q11 numbers; they are not replaced by their finite residues. C0029 corroborates ai mod11=(1,2,7,8), so a1 is a unit under that normalization, subject to the documented arithmetic/theorem assumptions. By the source comparison, b(Xj,R)=0. Conjugation forces b(S+,S+)=0. Since **every** negative Selmer class is a multiple of R, b(Xj,S)=0, so

\[
\boxed{U=\operatorname{span}_{\mathbb Q_{11}}\{X_2,X_3,X_4\}
\subseteq\operatorname{rad}(b)=S^{(2)},\qquad\dim U=3.}
\]

Independence follows from the coefficients of P2,P3,P4. **No upper bound on dim S+ is needed.** Additional positive Sha directions do not invalidate these three classes. The mod11 frame P2−2P1, P3−7P1, P4−8P1 is only the reduction of this exact recipe; finite approximate vectors alone are still not exact S2 membership certificates.

This supplies exact, source-defined Selmer classes **conditionally on the analytic/height inputs**, not explicit Galois cocycles or first-order Bockstein lifts. We do not know whether an individual Xj is a universal norm; do not assume it is non-universal. A true nonzero h2(Xi,Xj), if obtained, would itself exclude that possibility for the participating classes. Its nonzero alternating restriction to U would have rank2 and radical dimension1 **on U**, even if full S2 is larger. It would not identify the full S3 or its radical with the universal-norm line without additional full-Selmer control.

## Falsifier, implementation and next move

The [exact linear-algebra controls](one_sided_selmer_control.py) verify the lemma's mechanism for positive dimensions4,6,8 with negative dimension1. A model with signature(4,3) preserves **all four measured P_i/R heights** yet gives first-height rank6; the proposed three vectors no longer all belong to the full radical. Thus proving only a Mordell–Weil height, or ignoring the twist-side Selmer theorem, is insufficient. Common nonzero normalization scalars preserve the ratios, while finite Sha is correctly distinguished from trivial Sha[11]. These are synthetic algebra controls, not computed Selmer groups.

Next: source-normalized arithmetic representatives/lifts for Xj in the actual Selmer complex modulo T³, then a genuinely nonzero second pairing. The full positive Selmer upper bound remains necessary for the **full**5→3→1 claim, but it is no longer a prerequisite for defining this three-dimensional test domain. If full S2 is larger, even an exactly zero restriction to U does not prove that h2 vanishes on all of S2. No actual D(T), x1 or arithmetic h2 value has been computed. Do not repeat global-height digits or universal-norm height measurements as substitutes.

Reproduce with the pinned external dependency:

```
python3 -m pip install --only-binary=:all: --no-deps python-flint==0.9.0
python3 -I -B research/anticyclotomic_11/arb_twist_derivative.py
python3 -I -B research/proof_labs/one_sided_selmer_control.py
```

**Outcome:** a published first-height identification, an independent maintained-library validation of a finite analytic input, and a conditional exact S2 test subspace. No new theorem about original complex L'', full E-Sha finiteness, leading coefficient or general BSD; no novelty assertion or external mathematical review.
