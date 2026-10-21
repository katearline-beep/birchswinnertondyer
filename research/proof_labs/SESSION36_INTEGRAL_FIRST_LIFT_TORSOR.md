# Session36 — integral first lifts with one parameter

2026-10-21. Baseline main42a859c / PR71; predeclared issue72, EX022/LF019. AI-assisted source derivation, unreviewed; no novelty claim. All source and arithmetic dependencies of C0044 remain explicit. This is a stronger supported GLOBAL existence result, not an evaluated correction cochain or a Selmer-complex computation.

## Question, selection and whole-problem review

Can the negative residual Selmer line eliminate the negative *global* obstruction group and make first corrections a one-parameter problem? Safe lemma: signed finite-support duality. Credible leapfrog: prove the integral statement by exact coefficient sequences and specify the remaining secondary obstruction. Wild alternative: a characteristic-zero motivic/complex regulator comparison; no such typed bridge has been established. Do not replace that missing theorem with a p-adic calculation.

At sprint start main, open issues, no open PRs, and the rank-two/H3 branch heads were inspected. Other-instance heads remain ad91e78/e17b3bc, as at Session35. All C0001–45 and H1–H6 retain their boundaries. New implication toward original complex L''(E,1)=0, analytic rank four, original Sha finiteness, leading coefficient or general BSD: **NONE**. H1 is selected for the signed integral test, H2/H3 limited, H4/H6 parked, H5 diagnostic. Auxiliary-prime searches and additional first-height digits are deprioritized.

## Objects and dependencies

E=[1,-1,0,-79,289], conductor234446=2*117223; K=Q(sqrt(-7)); p=11. Sigma contains places above2,11,117223 and infinity. Write G=G_{K,Sigma}, V_n=E[11^n], L=T_11(E), and c for complex conjugation. Superscripts +/- mean eigenspaces for its natural action on cohomology; 2 is a unit. The known anti-invariant point is R=(-3355/63,128780*sqrt(-7)/1323) on the short model. Its Kummer class is kappa_n(R).

Inputs:

1. C0044, with its recorded residual GL2, local, modular-symbol and published-theorem inputs, gives Sel_11(E/K)^-=F11*kappa_1(R). It uses neither the C0032 analytic interval nor the provisional first heights. C0035 supplies residual nonzero/independence.
2. C0039 gives nonzero localization of kappa_1(R): normalized local Kummer coordinates (9,2) at the two11-adic places. These are actual local divisibility coordinates. They do not measure a global height.
3. Recorded local torsion vanishing gives H0(K_v,V_1)=0 at all finite v in Sigma. Weil pairing identifies the **Cartier** dual V_1^D=Hom(V_1,mu_11) with V_1, equivariantly, including under c. Global H0(G,V_1)=0 by the residual image input.
4. Milne, *Arithmetic Duality Theorems*, second edition, Chapter I Corollary2.3, Theorem4.10(a,c), Corollary4.15, Theorem5.1 and Proposition0.22(c): https://jmilne.org/math/Books/ADTnot.pdf . We use finite-module local/global duality, Euler characteristic, finiteness and inverse-limit control. The next deductions are our specialization of these published tools, not a source theorem mentioning this curve.

## C0046 — the entire negative global group, at every coefficient level

Define F=ker(H1(G,V_1) -> direct_sum_(v in Sigma) H1(K_v,V_1)). A class in F is locally zero at Sigma. At a good prime outside Sigma it is unramified, hence in the classical Kummer local condition. Thus F is contained in the classical residual Selmer group. This inclusion is c-equivariant. Its negative part lies in F11*kappa_1(R), whose localization is nonzero. Therefore F^-=0.

Local duality and input3 give H2(K_v,V_1)=0 at Sigma; the complex place contributes zero. Hence H2(G,V_1) is its finite-support localization kernel. The Poitou–Tate pairing with F, using the Cartier self-duality, is perfect and c-invariant with target Q/Z. The local invariant map is unchanged by the field isomorphism c; it does not acquire an extra sign. Opposite eigenspaces pair to zero because 2 is invertible. Consequently

\[
H^2(G,V_1)^-=0.
\]

**Euler characteristic and the prime7 check.** For descent to Q first enlarge Sigma to include the place above7, since K/Q ramifies there. Direct enumeration on the minimal model and an independent quadratic-character sum on the short model both give #E(F7)=13, a7=-5. Thus neither1 nor7 is a residual Frobenius eigenvalue: det(Frob-1)=13 and det(Frob-7)=7*13, both11-units. The good-prime localization terms for adding7 vanish, including the V_1(-1) terms. Adding/removing this prime does not change H1 or H2, equivariantly. Equivalently its local H0, H1 and H2 vanish; the explicit eigenvalue check also checks the singular term rather than assuming local H1 vanishing alone suffices for removing support.

Restriction/corestriction over the resulting quadratic extension identifies the negative groups with those over Q for V_1 tensor chi_K, unramified outside {2,7,11,117223,infinity}. That two-dimensional representation is odd: c has one + and one - eigenvalue. Milne I Theorem5.1 gives Euler characteristic 11/121=1/11. Global H0 is zero and negative H2 has just been shown zero, so dim H1(G,V_1)^-=1. Its nonzero Kummer class is R. The same calculation for the untwisted representation gives dim H1(G,V_1)^+ = 1+dim H2(G,V_1)^+, **not a positive upper bound**.

Now use the c-equivariant exact sequence

\[
0\longrightarrow V_{n-1}\longrightarrow V_n\xrightarrow{11^{n-1}}V_1\longrightarrow0.
\]

The inclusion is the natural inclusion of torsion points. Induction in the long exact sequence proves H2(G,V_n)^-=0 for every n. Since H0(G,V_1)=0, its negative degree-one sequence is short exact. Therefore #H1(G,V_n)^-=11^n. Also H0(G,V_{n-1})=0, so the sequence 0 -> V_1 -> V_n -> V_{n-1} ->0 injects H1(G,V_1) into H1(G,V_n). Naturality of Kummer maps gives

\[
11^{n-1}\kappa_n(R)=\iota_*\kappa_1(R)\ne0.
\]

Thus H1(G,V_n)^- is **cyclic of order11^n generated by kappa_n(R)**, not merely a group of that order. The natural multiplication-by11 coefficient maps send kappa_(n+1)(R) to kappa_n(R).

All the finite cohomology groups used are finite (Milne I4.15). For the compact continuous cochains of L=lim V_n, the usual kernel/cokernel sequence for inverse limits gives 0 -> lim^1 H^(i-1)(G,V_n) -> H^i_cont(G,L) -> lim H^i(G,V_n) ->0. Here lim^1 vanishes by finiteness, Milne I0.22(c); this is a countable system of **abelian groups**, not a general assertion about inverse limits in arbitrary abelian categories. Cochain-level transition maps are surjective because continuous finite-valued maps admit locally constant lifts. Hence

\[
\boxed{H^2_{\rm cont}(G,L)^-=0,\qquad
H^1_{\rm cont}(G,L)^-=\mathbf Z_{11}\kappa(R).}
\]

No height comparison, Sha assumption for original E, positive Selmer upper bound, or added auxiliary ramification was used. These conclusions remain conditional on the stated C0044/arithmetic inputs and source specialization; they have not received expert review.

## C0047 — supported integral first lifts and their exact ambiguity

Let Gamma be the actual anticyclotomic Z11-extension Galois group, gamma a generator, T=gamma-1, and chi:G -> Z11 its coordinate. Set B2=L tensor Z11[[T]]/(T^2), with g acting as rho(g)*(1+T)^(-chi(g)). Conjugation acts by rho(c) on L and sends T to -T modulo T^2. This defines a c-equivariant sequence

\[
0\longrightarrow L\,T\longrightarrow B_2\longrightarrow L\longrightarrow0,
\]

whose kernel has the **opposite** c-sign to L. The connecting obstruction for x in H1(G,L)^+ therefore belongs to H2(G,L)^-=0. As H0(G,L)=0, the injection on degree one has no H0 ambiguity. The exact positive sequence is

\[
\boxed{0\longrightarrow\mathbf Z_{11}\,T\kappa(R)
\longrightarrow H^1(G,B_2)^+
\longrightarrow H^1(G,L)^+\longrightarrow0.}
\]

Every positive integral global class, including each kappa(P_i), consequently has a **fixed-support first global lift**. The fibre is a torsor for exactly one Z11 parameter. Identical statements hold over Z/11^n using V_n and the actual character modulo11^n. They are compatible under reduction by the integral sequence, not an inference from a single mod11 zero. In particular mod121 requires the actual C121 character (C0033), not a C11 substitution. Integral existence does not mean we have computed those lifts.

### Why the remaining scalar does not solve the Selmer conditions

The kernel class T*kappa(R) itself satisfies the ordinary/unramified local conditions. The difference of two global first lifts therefore has **zero image in every local Selmer quotient**. If those conditions are defined by the ordinary Selmer complex, either all global lifts of a fixed x satisfy them or none do. Changing the scalar cannot repair a nonzero local defect. On the residual classes of C0045, the additional finite integral height/duality assumptions give existence in that Selmer fibre; those assumptions are still needed. No claim that each P_i has a Selmer lift is made.

### A relative normalization, with an explicit missing input

Fix one place v|11. Suppose an actual local reference first lift of loc_v(x) has been supplied, and a Z11-linear coordinate ell on H1(K_v,L) extending the normalized formal Kummer log has been chosen. Nonanomalous local H0/H2 vanish; H1(K_v,L) is free of rank2, and the ordinary Kummer line is saturated, so such an extension exists. The value ell(kappa(R)) is a unit, residue9 in the C0039 orientation. Then for any global first lift b there is exactly one t such that

\[
\ell\bigl((\operatorname{loc}_v(b+tT\kappa(R))-b_v^{\rm ref})/T\bigr)=0.
\]

It is t=-a/ell(kappa(R)), where a is the coordinate of the initial difference. Its inverse-unit factors are 5 mod11 and93 mod121, since the recorded coordinate of R is108 mod121. These factors are **not evaluated correction coefficients**. A different local reference changes the normalized class; no canonical origin has been supplied. At cochain level coboundary ambiguity also remains. An affine torsor without an origin cannot be declared canonically zero. A generic auxiliary good prime need not offer this normalization: its local H0 can kill injection of the T-kernel. The nonanomalous11-adic place avoids that issue.

## A precise secondary global target, not yet a second height

At orderT^3 use u=log(1+T)=T-T^2/2. Since2 is an11-unit, this is an integral change of coordinate at this truncation; c(u)=-u exactly modulo u^3. The action becomes

\[
\rho(g)\exp(-\chi(g)u)
=\rho(g)(1-\chi(g)u+\chi(g)^2u^2/2).
\]

Writing the actual continuous-cochain differential as d0+u*d1+u^2*d2, a positive cocycle x admits a negative x1 with d0*x1=-d1*x by C0047. Its next obstruction is represented by d2*x+d1*x1, in positive H2(G,L). Changing x1 by a negative cocycle changes its class by t*beta1(kappa(R)); changing by a coboundary changes the result by an exact term. Thus there is a well-defined additive secondary GLOBAL operation

\[
\Theta^+(x)= [d_2x+d_1x_1]\ \in\
H^2(G,L)^+/\mathbf Z_{11}\beta_1(\kappa(R)).
\]

The first-lift injection above ensures a fixed base representative can be chosen; H0(L)=0 and the spectral-sequence naturality account for representative changes. The target quotient is by the actual image line/module, **without asserting it is free or saturated integrally**. Mod11, C0040's additional height/duality hypotheses show beta1(R) is nonzero; they do not by themselves prove an integral direct-summand statement.

This is the signed second Bockstein for the GLOBAL complex. It uses an actual cohomological differential in its definition but no such arithmetic d1,d2 or x1 has been evaluated here. A true derived height needs the Selmer local cone, matched duality, and the correct exact first radical. The remaining quotient can contain a nonzero second obstruction: first-order vanishing gives no T^3 lift. In particular the three C0045 residual combinations are not the exact Q11 height-ratio classes X_j. Replacing u by T while incorrectly using c(T)=-T at orderT^3 loses a necessary T^2 term.

## Reproducible controls and stopping rule

Run `python3 -I -B research/proof_labs/integral_first_lift_controls.py` (Python standard library). It independently enumerates #E(F7) on two models, checks the Frobenius unit conditions, all GL2(F11) Cartier-dual identities with complex conjugation, signed action/inversion and the u-coordinate at mod11/mod121, cyclic coefficient/Kummer compatibility, affine unit normalization and mutation controls. Synthetic signed complexes have the same first lift and one-dimensional ambiguity but either zero or nonzero secondary obstruction; all scalar choices preserve their local defect. These examples test algebraic implications, not actual elliptic cochains or source theorems.

The research outcome is C0046/47: signed supported global vanishing and an integral one-parameter first-lift torsor. No actual first correction, local reference lift, Greenberg cochain, T^3 lift or h2 value was computed. The next arithmetic deliverable must be an evaluated first global class together with local reference data and a finite Galois presentation refining the C0036 insufficient product quotient. The secondary operation specifies what then needs evaluation. Stop at this boundary rather than relabel an abstract existence proof as a concrete cochain experiment. No new published theorem that reaches original complex L'' has been found.

Local validation: all59 fixed Python workflow commands passed in62.12s on Python3.12, including the six metadata/negative-control validators and the complete frozen Kurihara checker. This verifies the programs, not the source-derived mathematical proof. All six exact-head pull_request workflow families remain mandatory before merge.
