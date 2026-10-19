# Session 18 — Conditional integral transversality and a sharper target for H2

**2026-10-19. AI-assisted internal arithmetic, conditional on C-0011/13's still-provisional global height values. Not independently peer reviewed.**

## The new deduction

Let \(\Lambda^+=\sum_{i=1}^4\mathbb Z_{11}P_i\) denote our **rank-four test lattice** inside the rational-invariant eigenspace, with no assertion that this determines the full Selmer group. Restrict the independently PARI-checked local logarithm to this lattice, and compare with the global anticyclotomic cross-height functional \(P\mapsto h_\rho(P,R)\), assuming the heights of C-0011/13 use the correct published normalization.

Normalizing both vectors by their first 11-adic-unit coefficient, we obtain
\[
\ell=(1,704,772,856),\qquad a=(1,739,766,668)\pmod{1331}.
\]

The minor in columns \(P_1,P_2\) is
\[
\det\begin{pmatrix}1&704\\1&739\end{pmatrix}=35\equiv2\pmod{11}.
\]
**Therefore, conditional on the first global-height digit, the two maps are integrally transverse:** the combined map \(\Phi=(\ell,a):\Lambda^+\to\mathbb Z_{11}^{\,2}\) is **split surjective**, and its common kernel is a **saturated free direct summand of rank two**. The crucial unit-minor statement already follows modulo 11 and is unaffected by *any* higher 11-adic corrections or unit rescalings.

Using the two remaining coordinates as free variables, a basis of the common coefficient kernel modulo 1331 is
\[
\boxed{\begin{aligned}
W_3&=20P_1+1103P_2+P_3,\\
W_4&=2P_1+842P_2+P_4.
\end{aligned}\qquad(\bmod1331)}
\]
Their reductions modulo 11 are \(9P_1+3P_2+P_3\) and \(2P_1+6P_2+P_4\). These are **modular approximations to 11-adic linear combinations** in a kernel, NOT exact rational Mordell–Weil point relations or defined Selmer classes.

The proof is elementary linear algebra over \(\mathbb Z_{11}\). It is **not a previously unknown general theorem**; its contribution here is an explicit conditional arithmetic certificate on our focal curve, stronger than noting two hyperplanes have different first digits.

## Methodology: what survives, what should stop

The formerly attractive auxiliary **L11** idea identified the local-log kernel with the radical of the first global anticyclotomic height. Equal dimensions do **not** imply equality; the unit minor is a definitive conditional obstruction and cannot be repaired by more precision.

The conservative next milestone is **independently reproducing a complete global BCLMN height**, including the canonical sigma, exact numerator/denominator ideals, all finite-place contributions and character normalization. The independent PARI ellpadics2 comparison verifies the *sigma slope convention* but **not the complete global height**.

A credible leapfrog would then be to define the actual one-prime modified Selmer/Bockstein complex and test whether the newly identified saturated two-dimensional common kernel occurs in a genuine exact sequence. No such identification has been established. An unrelated high-upside avenue is a third-derivative geometric formula for the **complex** base-change L-function with explicit comparison back to \(L''(E,1)\), not another p-adic identity.

## Reproducibility and negative controls

The [pure-Python verifier](../methodology/local_global_transversality_11.py) reconstructs both primitive profiles from raw values, proves the unit pivot and a splitting modulo 1331, checks both kernel vectors and lower-precision reductions, and rejects:
- dependent functionals (zero minor),
- almost-dependent maps (minor divisible by 11),
- a height vector spuriously multiplied by 11 that no longer has a primitive unit entry.

Run: python3 -I -B research/methodology/local_global_transversality_11.py.

**Mathematical status:** conditional on the still-provisional **first global height digit**. Passing these tests does not certify the BCLMN global-height computation, construct a higher derived regulator, bound an 11-Selmer group, prove Sha finiteness, establish \(L''(E,1)=0\) for the original **complex** L-function, or prove any part of general BSD. No new missing implication toward complex BSD was established by this session.

Sources: [local-log audit](../split11/LOCAL_GLOBAL_ALIGNMENT_AUDIT.md), [three-digit height audit](SESSION17_CANONICAL_SIGMA_MOD1331.md), [first height radical](FIRST_HEIGHT_RADICAL_MOD11.md), [BCLMN 2016](https://arxiv.org/abs/1610.08729).
