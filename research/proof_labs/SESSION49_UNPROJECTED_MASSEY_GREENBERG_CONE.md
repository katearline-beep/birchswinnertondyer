# Session49 — an unprojected one-variable Massey identity, but a missing ordinary Selmer cone

**2026-11-21, America/New_York.** AI-assisted source-level primary-theorem audit, explicit finite-group algebra and cochain equations; **not independently expert-reviewed, not a new BSD implication**. Base: Session48 PR #91 and Session47's actual five-Kummer-field finite quotient. The standing 2026-11-20 whole-problem review and C-series claim statuses are deliberately unchanged.

## Mandatory whole-problem boundary

General BSD for **every** E/Q asks (i) \(\mathrm{ord}_{s=1}L(E,s)=\mathrm{rank}E(\mathbf Q)\); (ii) finiteness of \(\Sha(E/\mathbf Q)\); (iii) the full normalized leading-coefficient identity. For focal curve \(E:y^2+xy=x^3-x^2-79x+289\), exact original **COMPLEX** \(L''(E,1)=0\), rigorous \(L^{(4)}(E,1)\ne0\), Sha finiteness and leading term are NOT proved. The existing nonzero twist derivative plus quadratic base-change product do not produce the missing complex cubic vanishing. H1 correction remains unevaluated, H2 true Selmer second height unevaluated, H3 complex comparison missing, H4/H6 parked, H5 numerical only. **New proved implication toward BSD: NONE**.

## Critical new source correction: Theorem 6.10 is NOT projected

Anwesh Ray and Ramdorai Sujatha, *Massey products and the Iwasawa theory of fine Selmer groups*, **Canadian Journal of Mathematics** (online October 16 2026), DOI 10.4153/S0008414X26102478, source full HTML https://multimediafluids.uam.elogim.com/core/journals/canadian-journal-of-mathematics/article/massey-products-and-the-iwasawa-theory-of-fine-selmer-groups/63A377A368F3E5B6318FA71730A60524 .

- **Definition 6.1** (paper §6.1): \(\Psi^{(n)}\) is the connecting map for \(0\to V\otimes I^n/I^{n+1}\to V\otimes\Omega/I^{n+1}\to V\otimes\Omega/I^n\to0\), with \(\Omega=\mathbf F_p[[H]]\). For \(G\) of \(p\)-cohomological dimension 2 and \(H\simeq\mathbf Z_p\), the domain is \(H^1(G,V\otimes\Omega/I^n)\), range \(H^2(G,V)\otimes I^n/I^{n+1}\).
- **Proposition 6.4:** the FIRST generalized Bockstein is the actual cup product with the tower character.
- **Theorem 6.9** (paper §6.2): for a general pair \((\phi,\theta)\), the formula is after applying a projection \(p_{\phi,\theta}\); the authors immediately before the theorem **explicitly warn** it need not determine the entire Bockstein image.
- **Theorem 6.10** (same §6.2, attributed to Lam–Liu–Sharifi–Wake–Wang 2023 Theorem 4.3.1): for **one variable** \(H=\mathbf Z_p\), it instead gives an **UNPROJECTED** identity \(\Psi^{(n)}([f])=(\kappa^{(n)},\lambda)_{\tau_{x^n}}\,x^n\), where \(\tau_{x^n}\) is the specified proper defining system coming from the chosen lift \(f\). This corrects a potential overgeneralization of the projection no-go: \(\Psi^{(2)}\) on global Galois cohomology can be recorded exactly by a triple Massey product in the paper's conventions, **without** the theorem-6.9 projection loss.
- **Theorem 7.1** is about **fine-Selmer \(\mu=0\)** (under its finite decomposition and total-ramification hypotheses); it is **not** the existence of a Greenberg-compatible focal-class lift or a BSD leading term.

Our anticyclotomic tower is one-variable. The coefficient **inverse-character** convention \(\rho(g)(1+T)^{-\chi(g)}\) is matched to the paper's conventional \(\Omega\)-action by choosing the inverse generator \(\gamma^{-1}\) or applying the Iwasawa anti-involution. At order 3, the coordinate changes \(U=(1+T)^{-1}-1=-T+T^2\) modulo \(T^3\), not simply \(U=-T\). **Sign and coefficient conventions must be fixed before quoting an equality.**

The theorem's global \(H^1\to H^2\) operation is a genuine tool for our **GLOBAL** first/second Bockstein; neither Theorem 6.9 nor 6.10 is a theorem asserting the analogous equality for our **ordinary Greenberg SELMER mapping cone**. Do not silently identify their fine Selmer \(\mu\)-criterion with our ordinary condition.

## Exact first/second cochain formulas in our actual coefficient convention

Set \(p=11\), \(G=G_{K,\Sigma}\), \(V=E[11]\), \(\rho:G\to\mathrm{GL}(V)\), and \(\chi:G\to\mathbf F_{11}\) the mod11 reduction of the actual first anticyclotomic character. Let \(A_r=V\otimes\mathbf F_{11}[T]/T^r\), acted on by \(a(g)=\rho(g)(1+T)^{-\chi(g)}\). Write \(c=c_0+Tc_1+T^2c_2\) and use the **inhomogeneous** differential
\[
 d_\rho f(g,h)=f(g)+\rho(g)f(h)-f(gh).
\]
Coefficient comparison of \(d_{A_3}c=0\) gives:
\[
\begin{aligned}
 d_\rho c_0(g,h)&=0,\\
 d_\rho c_1(g,h)&=\chi(g)\,\rho(g)c_0(h),\\
 d_\rho c_2(g,h)&=\chi(g)\,\rho(g)c_1(h)
                 - \binom{\chi(g)+1}{2}\rho(g)c_0(h).
\end{aligned}
\]
The second RHS is a **2-cocycle** once the first equation is solved, and its class in \(H^2(G,V)\) is precisely the (sign/convention-adjusted) obstruction to extending the chosen \(A_2\) cocycle to \(A_3\). It depends on the chosen first defining system \(c_1\); this is NOT a canonically evaluated arithmetic class before \(c_1\) is given. For an INTEGRAL class, replace \(\chi\) by the true \(\mathbf Z_{11}\) character and work in the actual integral augmentation tower; a mod11 computation alone does not certify an integral lift.

### Why the finite corrected quotient has a NONZERO second obstruction

Let \(G_2=(\mathbf F_{11}[T]/T^2)\rtimes C_{11}\) with coordinate triples \((e,u,v)\), group law
\[
(e,u,v)(f,x,y)=(e+f,u+x,v+y-e x),
\]
and its tautological first cocycle \(c_0(e,u,v)=u,\ c_1(e,u,v)=v\). Define the explicit normalized two-cocycle
\[
\boxed{b_2((e,u,v),(f,x,y))
  =e\,y-\binom{e+1}{2}\,x.}
\]
It is closed (verified by the cocycle identity and direct binomial identity); the canonical central extension
\[
1\to T^2\mathbf F_{11}\to G_3\to G_2\to1
\]
has extension cocycle **\(-b_2\)** under the section with top coefficient zero. Let \(h=(2,0,0)\) and \(w=(0,1,0)\). In \(G_2\), \([h,[h,w]]=1\). However for **every** lift of these generators to \(G_3\), the double commutator is \(4T^2\ne0\). Thus the extension has **no group section**: \([b_2]\ne0\in H^2(G_2,\mathbf F_{11})\). This is an exact NONZERO **FINITE-GROUP** second Bockstein, not a class computed on \(G_{K,\Sigma}\). The full two-dimensional V-coefficient analogue has two independent such directions, subject to the actual arithmetic first affine image.

**Essential source scope:** \(G_2\) is a *finite 11-group*, whose 11-cohomological dimension is not two; Ray–Sujatha Theorem 6.10 is NOT being applied to \(G_2\). The finite group's \(b_2\) is a direct cochain calculation. The theorem may be applied to global \(G\) after verifying its hypotheses and the augmentation/anti-involution conventions; **inflation can annihilate** the finite-group \([b_2]\), just as in Session47's first-stage example.

## The FULL ordinary-Greenberg local cone: three separate equations

At each place \(v\mid11\), take the actual ordinary stable submodule \(F_v^+V\hookrightarrow V\), twisted compatibly in each \(A_r\). A *Selmer degree-one cocycle*, not merely a global 1-cocycle, is a triple
\[
(c,\{a_v\},\{b_v\}),\qquad
 c\in C^1(G,A_r),\quad
 a_v\in C^1(K_v,F_v^+A_r),\quad
 b_v\in C^0(K_v,A_r),
\]
with \(d c=d a_v=0\) and \( \mathrm{res}_v(c)-\iota(a_v)=d b_v\). This is the mapping-fibre definition
\[
R\Gamma_f(K,A_r)
=\operatorname{Cone}\!\left(
 C^\bullet(G,A_r)\oplus\bigoplus_{v\mid11} C^\bullet(K_v,F_v^+A_r)
 \longrightarrow\bigoplus_{v\mid11}C^\bullet(K_v,A_r)
\right)[-1]
\]
with the usual unramified conditions away 11 suppressed from this displayed local-only formula (but **mandatory** in any real computation).

Expand \(a_v=\sum T^j a_{v,j}\) and \(b_v=\sum T^j b_{v,j}\). The local ordinary cocycle equations duplicate the global ones **inside F_v^+V**. The gluing equations, however, add indispensable 0-cochain terms:
\[
\begin{aligned}
  \mathrm{res}\,c_0-\iota(a_{v,0})&=d_\rho b_{v,0},\\
  \mathrm{res}\,c_1-\iota(a_{v,1})&=d_\rho b_{v,1}
        -\chi(g)\rho(g)b_{v,0},\\
  \mathrm{res}\,c_2-\iota(a_{v,2})&=d_\rho b_{v,2}
        -\chi(g)\rho(g)b_{v,1}
        +\binom{\chi(g)+1}{2}\rho(g)b_{v,0}.
\end{aligned}
\]
These are exact cochain identities for the chosen section and coefficients. In particular, a vanishing global Massey/Bockstein class does NOT supply the local ordinary \(a_{v,j}\) and the homotopies \(b_{v,j}\). It is an additional construction—not a theorem-scope technicality—that must be furnished at **both** primes \(v\mid11\). For a positive globally conjugation-symmetric class with conjugate choices of local references, the two conditions may be related by complex conjugation; this relation must be established with the exact inverse-generator convention before dropping either place.

### A small actual simplification: one INDEPENDENT ordinary-local test in a signed eigenspace

At \(p=11\), the field K has **two conjugate places** \(v,\bar v\). Complex conjugation \(c\) exchanges them. Because E is good ordinary at 11, the connected ordinary line \(F_v^+V\) and its conjugate \(F_{\bar v}^+V\) are transported by the natural Galois map; the inverse anticyclotomic augmentation coordinate is likewise transported via
  \(c(T)=(1+T)^{-1}-1=-T+T^2\pmod{T^3}\).
This is NOT \(-T\) at second order; using that incorrect expression changes \(\binom{\chi+1}{2}\) to \(\binom{\chi}{2}\) and drops a nonzero \(\chi T^2\) term. The new exact test explicitly falsifies the wrong quadratic truncation.

For a **global cohomology class in a fixed \(c\)-eigenspace**, the local ordinary-membership conditions at \(v\) and \(\bar v\) are equivalent: if \(\mathrm{loc}_{v}(x)\) lies in \(\mathrm{im}(H^1(K_v,F_v^+A_r)\to H^1(K_v,A_r))\), the conjugate localization belongs to the conjugate ordinary subgroup, and conversely. Similarly, matching a **specified** local reference at \(v\) forces the matching conjugate reference at \(\bar v\), **provided** the second reference was chosen as the actual signed/inverse-Iwasawa conjugate. This is cohomological covariance, not an explicit global cocycle or an assertion that the ordinary condition is automatically satisfied.

For the negative residual point R, Session33/C0039 computes the actual short local logarithm coordinates \((9,2)=(9,-9)\bmod11\), consistent with sign \(-\); multiplying its Kummer class by the \(c\)-anti-invariant T makes \(T\kappa(R)\) positive. In Session37/C0049 the positive normalized local first-lift references are conjugate and fixing the reference at \(v\) fixes the affine 1-parameter origin (the local R coordinate 9 is a unit). The useful practical reduction is therefore: **one mathematically independent ordinary-local test and one local normalization for a positive class**, with the conjugate place retained in the code as a **mandatory sign/orientation integrity check**. A local defect at the first place still blocks the global positive Selmer lift and cannot be repaired by adjusting the \(T\kappa(R)\) scalar, since that ambiguity already lies in the ordinary local line.

This does not apply to an arbitrary cochain without its signed Galois cohomology class and correctly conjugated local conditions; in particular, do not discard the second 11-adic prime from a raw finite-Galois presentation without first certifying its conjugation action.

**Proposed output-type comparison square, currently MISSING:**
\[
\begin{array}{ccc}
 H^1(R\Gamma_f(K,A_2)) &\xrightarrow{\beta_{2,f}}& H^2(R\Gamma_f(K,V))\\
 \downarrow & & \downarrow\\
 H^1(G,A_2) &\xrightarrow{\Psi^{(2)}_{\mathrm{global}}}& H^2(G,V)
\end{array}
\]
with the correct quotient by first-stage defining-system ambiguity and normalized \(\mathrm{Shapiro}\) image. This natural square exists formally from the coefficient short exact sequence if the ordinary local conditions are compatible and exact; what is **missing** is a computed upper-row image and its arithmetic cochain representatives. Bullach–Burns (arXiv:2509.13894, §4–6) supplies a relevant general Selmer-complex framework, but no checked theorem produces the focal top arrow's actual value or a new complex \(L\)-derivative.

## Exact falsifiers and reproduction

Run
  python3 -I -B research/proof_labs/session49_unprojected_bockstein_cone_controls.py

It checks (i) binomial law and the source-convention first-cochain equation, (ii) the explicit second 2-cocycle, (iii) exact central-extension sign, (iv) the nonzero double commutator for **all 11^4=14,641** possible higher scalar generator-correction choices, hence no splitting, and (v) an **independent synthetic local-cone** with one Frobenius and two individually consistent ordinary equations but inconsistent joint solution. It also models a projection that discards one nonzero coefficient direction; this is a generic *projection warning*, **not an explicit instance of the paper's specific \(p_{\phi,\theta}\) map**. These controls do not evaluate the actual Galois \(c_1\), Selmer boundary, or \(\Sha\).

**Critical counterexample to a careless conclusion:** the finite \(G_2\) second Bockstein class is provably nonzero even if a finer arithmetic Galois extension happens to kill it under inflation. Therefore “computed \(\beta_2\ne0\) on first-stage finite quotient” does not imply “global \(\beta_2\ne0\),” just as global vanishing does not imply ordinary-Selmer vanishing. All three source/target groups must be labeled.

## Decisive next arithmetic experiment

Safe exact lemma completed: unprojected one-variable source theorem matched to the inverse-action cochain formulas and the finite canonical second obstruction, with a fully typed ordinary local cone. **Next focal test:** choose an **actual** positive first global class whose existence is conditional on C0044/46/47 and try to evaluate its normalized cochain on an arithmetic non-split central order-121 extension of \(B_x\). At \(v,\bar v\mid11\) supply the ordinary \(a_{v,1}\), homotopies \(b_{v,1}\), all ramification support relations and C0049 Shapiro local reference; then compute the top-row \(\beta_{2,f}\) rather than assuming it agrees with the known bottom-row \(b_2\).

**Kill rule:** if only a projected Massey, global H² class, first cochain on an insufficient finite quotient, or source theorem with wrong local conditions is available, record NO-GO; do not promote H2, H3 or any C-series status. H1 40%, H2 15%, H3 40%, H5 5%; H4/H6 parked. **New proved implication toward BSD: NONE.**


## Direct full-PDF source spot-check: Bullach–Burns Theorem 4.20 is NOT an existence theorem for c₁

Dominik Bullach and David Burns, *On Euler systems and Nekovář–Selmer complexes*, author PDF https://dominikbullach.github.io/bb.pdf, PDF p.51 (physical page index50), **Theorem (4.20)**, source checked against the displayed PDF page rather than an abstract. Its input includes **a family of Nekovář structures satisfying Hypothesis 4.1, Hypotheses 4.14 and 4.16, a nonzero free R-module quotient Y with positive modified core rank, and an Euler system of the prescribed rank relative to the Nekovář structure**. The conclusion, localized at appropriate prime ideals and with other Fitting/Tor conditions, is a **containment** relating values of that already-existing Euler system to the **determinant of the associated Selmer complex**. The displayed formula involves a positive power of a Fitting element multiplying the Euler-system value; it does not assert existence of any arbitrary desired arithmetic cocycle, nor identify the focal anticyclotomic normalized c₁.

**Typed missing bridge:** we would have to construct/identify an appropriate Euler system satisfying ALL its hypotheses and map its values to the specific augmentation-first correction / local Shapiro references; the rank-four curve, C0047 H¹ existence, and Section45 finite Kummer quotient supply **none** of those objects. Therefore Theorem 4.20 can organize determinant/Greenberg comparisons *after* a relevant Euler system is available, but it cannot be used to solve our current embedding problem. Existing rank-zero Kato specializations in the paper do not imply exact complex L''(E,1)=0.

The source also makes clear in **Remark (4.22)** that positive modified core rank \(r_{\mathcal F,Y}>0\) is an explicit restriction even for Greenberg–Nekovář structures; the Y quotient is not a decorative hypothesis. This is a second decisive no-go against a direct black-box application.

**Final theorem-level triage:** Ray–Sujatha Theorem 6.10 genuinely supplies the unprojected GLOBAL Bockstein-to-Massey *identity*. Bullach–Burns Theorem 4.20 genuinely supplies a conditional **Euler-system-to-Selmer-determinant containment**. There is no published source theorem among these two that, by their stated inputs, constructs our supported normalized first correction or evaluates the second ordinary-Selmer Bockstein. The only justified active next test remains an explicit global and local cochain with a source-checked comparison map. **New BSD implication: NONE.**
