# C-0004 — Odd-prime quadratic-descent decomposition of the 11-Selmer group

**Type:** specialization of standard Galois cohomology / Selmer-descent mathematics; no claim of novelty. **Review:** cohomological argument drafted, exact point checks available, but full argument not externally reviewed or formally verified.

## Statement

Let E be the elliptic curve over Q of conductor 234446 (LMFDB 234446.a1), let K=Q(√−7), let \(\chi_{-7}\) be its quadratic character, and put \(p=11\). For the **ordinary classical p-Selmer group** defined by local Kummer images, there is an isomorphism of F₁₁-vector spaces

\[
\operatorname{Sel}_{11}(E/K)\simeq
\operatorname{Sel}_{11}(E/\mathbb Q)\oplus
\operatorname{Sel}_{11}(E^{-7}/\mathbb Q).
\]

In particular, dimensions add. This is an **odd-p theorem** and does not apply unmodified to p=2. It should not be confused with the *one-prime modified Selmer group* used for anticyclotomic derived heights.

## Proof route and its explicit obligations

Let \(G=\operatorname{Gal}(K/\mathbb Q)=\{1,\sigma\}\). Since 2 is invertible modulo 11, the idempotents \(e_\pm=(1\pm\sigma)/2\) split every 11-primary G-module. The character decomposition of the induced trivial representation is \(\operatorname{Ind}_{G_K}^{G_\mathbb Q}\mathbf F_{11}\simeq\mathbf F_{11}\oplus\mathbf F_{11}(\chi_{-7})\).

Apply the projection formula and Shapiro's lemma to \(M=E[11]\), with the twist identification \(E^{-7}[11]\simeq E[11]\otimes\chi_{-7}\). This identifies the **global cohomology**

\[
H^1(K,E[11])\simeq H^1(\mathbb Q,E[11])\oplus
H^1(\mathbb Q,E^{-7}[11]).
\]

**Important separate step:** check compatibility with the local Kummer subspaces at **every** place. At a place where K/Q is split, the two local coordinates diagonalize as symmetric/antisymmetric vectors. At a nonsplit place, restriction/corestriction, with composite multiplication by 2, yields the requisite isomorphisms on 11-primary Kummer quotients. This includes ramified primes, because 2 remains invertible on 11-primary groups. Therefore the global cohomology decomposition restricts to the *classical* Selmer groups.

This is a conventional restriction/corestriction + Shapiro argument, not a theorem established by a script. Expert checking and a precise book/paper citation for the local Kummer compatibility are still required before marking this internally drafted proof externally reviewed.

## Application to our exact points

The short model is \(E_0:y^2=x^3-1267x+17230\), and the twist is

\[
E^{-7}:Y^2=X^3-62083X-5909890.
\]

The exact point \(T=(3355/9,128780/27)\) lies on the twist. It is **non-torsion**: the twist is an integral short Weierstrass equation with nonsingular discriminant, while the Nagell–Lutz theorem requires the x-coordinate of a rational torsion point to be integral. Here x(T)=3355/9 is nonintegral.

Over K let \(w=\sqrt{-7}\). The map \((X,Y)\mapsto (X/(-7),Y/(-7w))\) sends T to

\[
R=(-3355/63,(128780/1323)w)\in E_0(K)
\]

and satisfies \(\sigma R=-R\). The four previously recorded rational generators belong to the \(+\)-eigenspace. **Conditional on the documented rational rank four**, \(\operatorname{rank}E(K)\ge 5\). We do not require a full Mordell–Weil basis or an unreviewed analytic twist rank certificate.

The script [verify_twist_descent.py](verify_twist_descent.py) checks all exact coordinates, the anti-invariance of R, and the splitting idempotents in \(\mathbf F_{11}[G]\); it **does not** test the global cohomological argument or calculate Selmer groups.

## More specific target for removing the missing Sha assumption

Because of the splitting and the lower rank bounds,

\[
\begin{aligned}
\dim\operatorname{Sel}_{11}(E/K) \le 5
\quad\Longleftrightarrow\quad&
\dim\operatorname{Sel}_{11}(E/\mathbb Q)=4\quad\text{and}\\
&\dim\operatorname{Sel}_{11}(E^{-7}/\mathbb Q)=1.
\end{aligned}
\]

The equivalence uses \(\dim\operatorname{Sel}_{11}(E/\mathbb Q)\ge 4\), \(\dim\operatorname{Sel}_{11}(E^{-7}/\mathbb Q)\ge1\), and integer dimensions. If these exact Selmer bounds can be independently certified, the Kummer exact sequence forces \(\Sha(E/K)[11]=0\). Since any nontrivial 11-primary torsion group has a nonzero element killed by 11, this implies \(\Sha(E/K)[11^\infty]=0\) and discharges the finiteness hypothesis in our application of Agboola–Castella.

**We have not computed either Selmer dimension.** This note identifies a narrower theorem-proving target; it is not the achievement of the target.

## Cross-disciplinary methods (math first, analogies second)

**Physics — representation theory / symmetry sectors.** The exact +/- decomposition above is the mathematical analogue of decomposing a Hamiltonian by a commuting symmetry. This analogy suggests using projectors *before* large computations. Random-matrix statistics of L-function zeros supply statistical hypotheses about *families*, not certificates for a specified curve ([Katz–Sarnak overview](https://collaborate.princeton.edu/en/publications/zeroes-of-zeta-functions-and-symmetry/)).

**Physics — perturbation and first nonvanishing term.** Derived p-adic heights are connected to Iwasawa augmentations, filtrations and Bockstein maps—not merely to the ordinary local logs computed in C-0001/2. Follow the genuine Selmer-complex literature: Mazur–Rubin, *Organizing the arithmetic of elliptic curves* (2005); Macias Castillo–Sano, [*On Selmer complexes, Stark systems and derived p-adic heights*](https://arxiv.org/abs/2603.23978) (2026 preprint). The physical picture of higher-order response may help organize calculations, but does not substitute for the cohomological pairing.

**Biology — orthogonal assays and negative controls.** Every novel computational result must be checked by a genuinely different library/algorithm, not only by AI restating the same formulas. Include intentionally invalid inputs or wrong normalizations that tests *must reject*. The previous PARI interpreter false-positive is a recorded cautionary example.

**Biology — identifiability and experimental design.** The local-log kernel is an observable, not necessarily the anticyclotomic height radical (a different object). Choose computations that distinguish models; prioritize certified 11-Selmer ranks and a well-defined global height cross-pairing, not another increment of p-adic precision.

## Immediate work packages

1. The twist factor: audit the numerical L'(E^{-7},1) certificate with a rigorous tail bound and independently implement the analytic check. If established nonzero, Gross–Zagier/Kolyvagin give analytic rank one and finiteness of Sha for the twist. Do not claim this until the derivative and hypotheses are rigorously checked.
2. The original rank-four factor: investigate possible 11-Selmer upper bounds over Q with explicit descent or alternative theorems. Do **not** assume eclib's 2-Selmer computation also provides 11-descent.
3. Conditional anticyclotomic heights: use the one-prime *modified* Selmer complex and a specified anticyclotomic character. Do not substitute the two-prime coefficient kernel.
4. Ask an arithmetic geometer to check the local Selmer compatibility and theorem applicability before announcing consequences.

## References / provenance

Silverman, *The Arithmetic of Elliptic Curves* (2nd ed.); Milne, *Arithmetic Duality Theorems* (Galois cohomology and restriction–corestriction); Agboola–Castella, [*On anticyclotomic variants of the p-adic Birch and Swinnerton-Dyer conjecture*](https://doi.org/10.5802/jtnb.1174); [Mazur–Rubin 2005](https://doi.org/10.1016/j.aim.2005.05.024). Prepared by human–AI exploration, 17 October 2026.
