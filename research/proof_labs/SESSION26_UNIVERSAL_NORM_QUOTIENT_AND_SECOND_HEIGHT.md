# Session 26 — Whole-problem redirection: universal norms are **not** the missing derived regulator

**2026-10-19 · Primary-source re-audit, not external peer review.** The original complex Hasse–Weil \(L''(E/\mathbb Q,1)=0\), complex analytic rank four, Sha finiteness, leading BSD coefficient and general BSD remain **UNPROVED**. E = 234446.a1, \(K=\mathbb Q(\sqrt{-7})\), \(p=11\).

**Sources:** Benjamin Howard, [*Derived p-adic heights and p-adic L-functions*](https://arxiv.org/pdf/1202.6343), especially **Theorem 4.2, Corollary 4.3, Conjecture 4.4**, with the comments immediately before Conjecture 4.4 identifying \(e_\infty=1\) as a previously proved anticyclotomic Heegner theorem of Bertolini/Cornut; Howard [*Variation of Heegner points in Hida families*](https://arxiv.org/pdf/1202.6358), Theorem 3.1.1, Corollary 3.1.2, §3.3 and Remark 3.3.2; standard [Krull intersection theorem for finite modules over noetherian local rings](https://websites.umich.edu/~mmustata/ReviewSheet3_2017.pdf). Session25 [prior source-derived claim](SESSION25_DIVIDED_HEEGNER_GLOBAL_COHOMOLOGY.md) is a **nonzero norm-compatible strict Greenberg Iwasawa class, not a computed base Selmer vector**.

## 1. The most important correction: first nonzero base universal norm is NOT a nonzero higher-height regulator

Howard **Theorem 4.2** constructs decreasing derived-height spaces \(S_p^{(r)}\) and pairings
\[
h^{(r)}:S_p^{(r)}(E/K)\times S_p^{(r)}(E/K)\to
(J^r/J^{r+1})\otimes\mathbb Q_{11},
\qquad\operatorname{rad} h^{(r)}=S_p^{(r+1)}.
\]
It proves that
\[
\boxed{S_p^{(\infty)}=\bigcap_{r\ge1}S_p^{(r)}
=\{\text{base-field universal norms, up to }\mathbb Q_{11}\text{-span}\}.}
\]
Therefore ANY norm-compatible Iwasawa Selmer class \(w\), including the divided Howard \(z_r\) **if its local Selmer structures match this framework**, has base \(\operatorname{pr}_K w\) in the universal-norm subspace, and
\[
\boxed{h^{(r)}(\operatorname{pr}_K w,x)=0\quad
\text{for ALL defined }r\text{ and every }x\in S_p^{(r)}.}
\]
Even a NONZERO \(\operatorname{pr}_K(z_r)\) cannot witness NONZERO higher-height curvature. **Session25's Issue #51 had accidentally aimed to use just such a base universal norm as a higher regulator. The right next experiment is NOT to compute more digits of that norm.** It can be useful to identify the universal-norm line, but the regulator must be sought on the **quotient by that line**.

**Hypothesis boundary:** Howard's Theorem 4.2 is for the Selmer setup in that paper. Matching its integral/Bloch–Kato conditions with Howard's nonexceptional strict Greenberg model for the focal curve still needs explicit source-level control; the universal-norm/radical theorem is **published**, and no equality of two independently chosen Selmer structures is invented here.

## 2. Finite exact augmentation order is available from standard finiteness: do not chase mere existence

Let \(\Lambda=\mathbb Z_{11}[[T]]\), \(T=\gamma-1\), and let \(M\) be the **finitely generated** integral compact Iwasawa cohomology/Selmer module under standard Galois-cohomology finite-\(S\) hypotheses, with the source-normalized weight-two Howard class \(0\ne z\in M\) as in C-0025/26. The finite-generation input is standard compact Iwasawa-cohomology theory (Howard 1202.6358 Remark 3.3.2 quotes Nekovář's \(R_\infty\)-module rank-one result for the big extended Selmer Iwasawa modules; the exact f.g. lattice and weight-two-to-Greenberg identification must be matched before using it unconditionally for this \(M\)). Because \(\Lambda\) is local noetherian, \(T\) belongs to its maximal ideal \((11,T)\), and Krull's intersection theorem for f.g. modules gives
\[
\bigcap_{n\ge0}T^n M=0.
\]
Assuming the integral Shapiro/LES injection and Greenberg preservation of C-0025/26 have their precise source lattice conventions matched, \(T\) is injective on \(M\) and \(\ker(\mathrm{pr}_K)=TM\) by global cohomology exactness and the local quotient diagrams.

Thus **once finite generation is certified for the exact target**, every nonzero \(z\) has a finite exact order \(r\) with
\[
\boxed{z\in T^r M\setminus T^{r+1}M,\quad
z=T^r z_r,\quad \mathrm{pr}_K z_r\ne0.}
\]
The order is at least 1 because the undivided classical base projection vanishes. Its value is NOT determined (so r=1 may fail), and the actual divided class/base coefficient has **not been computed**. An artificial module where \(T\) is invertible, e.g. \(\mathbb F_{11}((T))\) viewed as an \(\mathbb F_{11}[[T]]\)-module, is a counterexample: \(1\) is divisible by every power of \(T\), but the module is **not finitely generated**. The finiteness hypothesis is therefore substantive, not a formality.

**Decisive change to our strategy:** proving *some* nonzero base universal-norm class is an application of finite generation and nonzero tower, NOT evidence for a nonzero derived pairing. There is little reason to spend the next session computing which \(r\) produces that norm unless it is needed to identify the universal-norm line.

## 3. Howard Conjecture 4.4 predicts precisely the staged rank pattern our first-height numerics suggest

For anticyclotomic \(K\) satisfying the Heegner hypothesis, Howard writes \(s_+,s_-\) for the \(+/-\) conjugation eigenspace dimensions of the FULL \(11\)-adic base Selmer group. His **Conjecture 4.4** predicts
\[
\boxed{\dim S^{(2)}=|s_+-s_-|,\qquad \dim S^{(3)}=1.}
\]
The **universal-norm line** has dimension 1 by Howard's cited Bertolini/Cornut anticyclotomic results, **assuming the source's complete Selmer setup**. This is a PUBLISHED theorem framework plus a PUBLISHED CONJECTURE, NOT a proof of Conjecture 4.4 for our E.

We know **at least four independent positive eigendirection rational points** and **at least one negative eigendirection twisted point** \(R\) on E(K), but **the exact FULL 11-adic Selmer dimensions \(s_+=4,s_-=1\) are not established**. The original rank4 curve's Sha[11^\infty] and full Selmer upper bounds are unproved. **Conditionally** on exact signature (4,1), the first and proposed higher steps would read
\[
\dim S^{(1)}=5
\overset{\text{first pairing nonzero}}{\longrightarrow}
\dim S^{(2)}=3
\overset{\text{second pairing nonzero}}{\longrightarrow}
\dim S^{(3)}=1
=S^{(\infty)}.
\]

**Why the parity matters:** Howard Theorem 4.2/CH Theorem4.1 give complex-conjugation anti-equivariance of \(h^{(1)}\). A first symmetric anticyclotomic height on \(V^+\oplus V^-\) with dimensions \(4+1\) must have block form
\[
H^{(1)}=
\begin{pmatrix}0_{4\times4}&v\\ v^{\rm T}&0\end{pmatrix},
\quad v\in\mathbb Q_{11}^4.
\]
If \(v\ne0\), this has rank **exactly 2**, hence \(S^{(2)}\) is **positive-only dimension 3**. Our previous **provisional** BCLMN global heights suggest \(v\bmod11=(1,2,7,8)\), hence would be nonzero IF independently confirmed and IF normalized to Howard/CH's genuine \(h^{(1)}\). Those are still **two unproved identification steps**; mere agreement of dimensions cannot certify them.

On the resulting **three-dimensional** positive radical, \(h^{(2)}\) is **alternating** and takes matrix form
\[
H^{(2)}=
\begin{pmatrix}0&a&b\\-a&0&c\\-b&-c&0\end{pmatrix}.
\]
Over characteristic zero, its rank is either 0 or 2. Consequently, **one genuine nonzero second-height pairing between two exact \(S^{(2)}\) classes would FORCE the second-radical dimension 1** in this five-dimensional situation. Its one-dimensional radical would contain the universal-norm line and hence equal it. This is the **correct high-upside leapfrog**: a single independently certified nonzero alternating height on a valid quotient can collapse an otherwise large higher-dimensional problem.

But if \(a=b=c=0\), the second radical remains dimension3; that is a **mandatory negative control**, not something first-height data excludes. The \(\bmod11^3\) "radical vectors" recorded in Session17 are p-adic approximations, **not exact rational/global Selmer classes in \(S^{(2)}\)**. They cannot be input to \(h^{(2)}\) without exact lifting and a source-normalized first pairing.

## 4. The actual right next experiment (with rigorous kill gates)

**Step A, necessary:** Independently certify the **COMPLETE** previously computed BCLMN anticyclotomic first-height values (global denominator ideals, local terms and correct Mazur–Tate sigma) using a truly independent Sage/Magma or second mathematical implementation, and establish the pairing's normalization on the **full relevant Selmer subspace** against Howard/CH \(h^{(1)}\). PARI sigma alone is NOT an independent full global-height oracle. In parallel establish the exact \((s_+,s_-)\) Selmer dimensions or label all 5→3→1 conclusions conditional.

**Step B, leapfrog:** Build \(S^{(2)}\) by **exact** first-height kernel, and pick **two non-universal-norm classes** \(x,y\in S^{(2)}\). Construct the published Howard/CH **second Bockstein-derived** pairing (not a second digit of the first ordinary height), test \(h^{(2)}(x,y)\) rigorously and include the zero pairing as null hypothesis. If a nonzero value is certified, it forces rank2 on the 3-space under exact 4+1/full-first-height hypotheses; if zero, investigate independent class pairs rather than assert Conjecture 4.4.

**Step C, required for ORIGINAL BSD:** A separate noncircular theorem from the resulting \(11\)-adic Selmer filtration/regulator to the **ORIGINAL COMPLEX Hasse–Weil \(L''(E/\mathbb Q,1)\)** is still absent. If not found, no rank-four analytic-rank or leading-coefficient claims may be promoted. The independent function-field Ulmer Tate-cycle/characteristic-zero comparison laboratory should remain active.

**Things to stop doing:** spending time measuring the already-zero height of a universal norm, conflating norm-compatible \(z_r\) with a regulator witness, treating a predicted \(S^{(2)}\) dimension as proven from an approximate BCLMN vector, treating finite-order Krull intersection as a computed order, or assuming the original complex rank follows from any \(p\)-adic height.

## 5. Executable logic controls and whole-problem implication

[Exact F11 parity/alternating and negative-control checker](howard_second_height_quotient_controls.py) verifies the conditional rank2 first block, dimension3 first radical, that a 3×3 alternating second form has rank 0 OR 2, and that the nonzero case leaves radical dimension1. It explicitly rejects "universal norm supplies nonzero pairing" and illustrates failure of Krull separation in a non-finitely-generated Laurent module. **No actual second derived height is computed, nor is the first BCLMN height independently certified.**

**New-to-project progress:** we discovered that our planned universal-norm base-nonvanishing exercise cannot supply the desired regulator, and found a **one-pairing decisive test** of a published higher-height conjecture under exact signature/normalization gates. This is a better allocation of effort, NOT a newly proved BSD statement.

**Proof flags unchanged:** no exact complex \(L''(E,1)=0\), analytic rank4, 11-Selmer full upper bound, Sha finiteness, nonzero second derived height or general BSD proof. Next human specialist review and rigorous independent global-height reproduction are high priority.
