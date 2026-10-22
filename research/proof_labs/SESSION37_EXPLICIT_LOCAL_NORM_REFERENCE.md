# Session37 — an explicit local reference point

2026-10-22 America/New_York. Baseline main1be0d88 / merged PR73; issue74 predeclared EX023/LF020 before arithmetic. AI-assisted, mathematically unreviewed; no novelty claim. Unlike the earlier synthetic lift matrices, the point and all norm/trace values below concern the actual focal curve and actual anticyclotomic local field. No supported global correction cochain is evaluated.

## Choice and whole-problem scope

C0047 established integral first GLOBAL existence with one parameter, but lacked a local origin for normalization. The selected experiment is a finite local norm-point certificate. Safe lemma: a unit norm for an explicit formal point. Credible leapfrog: Kummer/corestriction and Shapiro turn that point into residual local reference classes. Wild alternative: a higher characteristic-zero cycle/complex regulator comparison, still missing a typed original-complex bridge.

At sprint start main, open PRs (none), and other-instance branches were checked. Rank-two/H3 heads remain ad91e78/e17b3bc. All47 previous claims and H1–H6 retain their scope. H1 selected, H2/H3 limited, H4/H6 parked, H5 diagnostic. New implication toward original complex L''=0, exact analytic rank four, original Sha finiteness, leading coefficient or general BSD: **NONE**. This experiment supplies a local arithmetic input rather than additional first-height digits or auxiliary-prime searches.

## C0048 — actual field, actual point and actual elliptic norm

E is the minimal curve [1,-1,0,-79,289], K=Q(sqrt(-7)), p=11. Fix one v|11. C0033 identifies the actual first anticyclotomic completion L=D1_v with Q11[xi]/f(xi), where

    f(X)=X^11-33X^9-176X^8+418X^7+11649X^6+108009X^5
          +711337X^4+3244989X^3+9160173X^2+14938803X+11133855.

The unique root of f modulo11 is4. With pi=xi-4, its polynomial is

    g(X)=X^11+44X^10+847X^9+9196X^8+60258X^7+240185X^6
          +725153X^5+4598605X^4+39930605X^3+214003625X^2
          +616891275X+756406651.

It is Eisenstein at11, so pi is a uniformizer with v11(pi)=1/11. The derivative terms have L-valuations (22,23,24,36,26,27,28,29,30,20,21); the unique minimum20 gives v_L(g'(pi))=20. PARI independently gives v11(disc(g))=20. These agree with the known local different. **The tail proof below uses a separate Newton-recurrence certificate and does not need to assume the different formula.** C0033's global dihedral/class-field identification, together with the Eisenstein degree, identifies this completion as the cyclic degree11 extension at v; its polynomial over Q is globally non-Galois. Do not substitute an arbitrary cyclotomic local extension.

For the minimal-model parameter t=-x/y put w=-1/y=t^3 U(t). The curve equation gives

\[
U=1+(t-t^2)U-79t^4U^2+289t^6U^3.
\]

There is a unique integral series U(0)=1. At t=pi the implicit derivative is a unit, so the convergent Hensel branch determines an actual point

\[
Q=(\pi/w,-1/w)\in\widehat E(\mathfrak m_L),\qquad
w=\pi^3 U(\pi).
\]

This is an exact local definition by a polynomial and a specified Hensel branch; it is not a claim that Q has rational coordinates in the global degree11 field. Its coordinates have valuations -2/11,-3/11. No global point search is being asserted.

The minimal invariant differential and formal logarithm are

\[
\omega=\frac{2+tU'/U}{2-t}\,dt=\sum_{n\ge1}b_{n-1}t^{n-1}dt,
\quad\log_E(t)=\sum_{n\ge1}\frac{b_{n-1}}n t^n.
\]

All b_j are11-integral: U and its inverse are integral and2 is a unit. Initial values are (1,1,0,-1,-159,-474,...). In particular the coefficient of t^11 in log is -95640/11. Let S_n=Tr_(L/Q11)(pi^n). Newton sums and an independent multiplication-matrix algorithm compute the same exact integers; S_1=-44, S_2=242, S_11=-4033588361.

### Infinite-tail certificate

The actual S_1,...,S_11 satisfy v11(S_n)>=floor((n+20)/11). For n>11 the Newton recurrence is S_n=-sum_(j=1)^11 g_(11-j) S_(n-j). The checker verifies all121 periodic floor inequalities, one for each n mod11 and j, proving by induction that this bound holds for **every** n, not just the computed33 terms.

For n>=23, writing k=v11(n),

\[
v_{11}\bigl((b_{n-1}/n)S_n\bigr)
\ge\lfloor(n+20)/11\rfloor-k\ge3.
\]

For k=0 the bound begins at23; for k=1, n>=33; for k>=2 the lower bound 11^(k-1)+1-k is at least10 and increasing. Thus every omitted term is in11^3 Z11, and the tail converges. Linearity/continuity of trace and the formal-group logarithm give, for the elliptic norm N_E(Q)=sum_sigma sigma Q,

\[
\frac{\log_E N_E(Q)}{11}
=\frac1{11}\operatorname{Tr}\log_E(Q)
\equiv\boxed{115}\pmod{121}.
\]

The norm lies in E1(Q11), whose formal log is an isomorphism to11 Z11. It is therefore a generator modulo11 of the local Kummer line. Applying the formal exponential also gives

\[
t(N_E(Q))\equiv\boxed{418}\pmod{1331}.
\]

For a base-field parameter t in11 Z11, every logarithm term of degree n>=3 has valuation at least n-v11(n)>=3. Thus log(t)=t+t^2/2 modulo1331 and its inverse is t=z-z^2/2 there; this justifies the parameter precision independently of any finite exponential truncation. These are norm/log values, **not** heights or correction coefficients. The degree-one trace alone gives -4=7 mod11, whereas the actual normalized norm is5 mod11. Omitting the degree11 logarithm term also gives7; this is a failing negative control on the actual arithmetic input.

## From the point to a local residual first lift

Let V=E[11], Gamma1=Gal(L/Q11)=C11, and B2=V tensor F11[T]/T^2, with the actual C0033 generator/character and inverse group-ring action. The quotient F11[Gamma1] -> F11[T]/T^2 sends gamma to1+T. For a base local point class P, choose s in F11 so that

    s * log_min(N_E(Q))/11 = log_min(P)/11  mod11.

For a nonformal P, interpret the right side as log_min([18]P)/(18*11), since #E(F11)=18. Then N_E([s]Q) and P have the same actual local Kummer class. The standard Kummer/corestriction square and Shapiro augmentation give

\[
\kappa_L([s]Q)\in H^1(L,V)
\xrightarrow{\rm Shapiro}H^1(Q_{11},V\otimes\mathbf F_{11}[\Gamma_1])
\longrightarrow H^1(Q_{11},B_2),
\]

whose reduction at T=0 is kappa(P). Its augmentation is corestriction, namely kappa(N_E([s]Q)); it is not restriction of P or a scalar trace substituted for an elliptic point. The formal point has a formal11-division point, so its Kummer cocycle takes values in the ordinary connected submodule F+V. Shapiro and the coefficient quotient preserve that submodule. Thus the construction supplies an **ordinary/Greenberg local reference class**, with the point specified and its norm evaluated, although individual Galois cocycle values are not listed.

The unramified ordinary quotient F-V has Frobenius alpha=5 mod11, so H0(Q11,F-V)=0; this remains true over the totally ramified degree11 field. The usual good-ordinary Kummer comparison therefore has no exceptional local H0 ambiguity. Local duality gives H2(Q11,F+V)=0 and Euler characteristic gives dim H1(Q11,F+V)=1; its image is the local Kummer line. This is the finite-coefficient local proof, not an unsupported reduction of a rational nonexceptional theorem.

### Explicit scalars and the model factor

C0039's coordinates use the SHORT differential. The minimal invariant differential is TWICE that one. Since the norm above uses the minimal curve, the residual scalar is 2*ell_short(P)/5. At the chosen v,

| Residual class | Multiple of Q defining its local reference |
|---|---:|
| P1 | 6 |
| P2 | 0 |
| P3 | 1 |
| P4 | 10 |
| R | 8 |
| P2-2P1 | 10 |
| P3-7P1 | 3 |
| P4-8P1 | 6 |

At the conjugate place choose the conjugate Hensel point and conjugate Shapiro identification; the character generator is inverted as prescribed by C0033. Positive-class scalars are the same; R has scalar3 instead of8. The zero reference for P2 is valid because its base local Kummer class is zero. The finite combinations in the table remain residual classes, not exact Q11 height-ratio classes.

## C0049 — an explicit normalization of conditional global Selmer fibres

Retain C0044/46/47 and, for first SELMER existence on the three kernel combinations, all the finite integral height/duality assumptions of C0045. For each such positive residual x the positive first global Selmer fibre is a torsor for F11*T*kappa(R). Localization at the chosen v maps this fibre to the ordinary local first-lift fibre of loc_v(x).

The latter is a torsor for T*H1(Q11,F+V), a one-dimensional space. Its map to full local cohomology is injective here: H0(F-V)=0, including for B2 by its filtration, and H0(V)=0 removes the first-lift coefficient H0 term. Under the kernel map, kappa(R) localizes nontrivially (C0039: short coordinate9). The map of these affine fibres is consequently a **bijection**. There is a unique positive residual global Selmer cohomology class restricting at v to the supplied reference, given respectively by [10]Q,[3]Q,[6]Q through the displayed Shapiro map.

This removes the missing-local-origin ambiguity at the residual first stage. It does not evaluate the normalized GLOBAL class or its Galois cochains. Existence remains conditional on C0045's source/height inputs; uniqueness uses the full negative global line. A local reference cannot repair a failed Greenberg defect. For an arbitrary positive base class, global first existence from C0047 does not imply the Selmer fibre is nonempty.

## Coefficient, provenance and research boundaries

The 121/1331 precision above certifies the norm of a point in the DEGREE11 field. It does **not** produce a mod121 first augmentation lift: (1+T)^11=1+11T modulo T^2 over Z/121, so the C11 group ring cannot map to the desired mod121 B2. The actual C121 layer is required there. No integral/tower-compatible local reference, supported global cochain, Selmer T^3 lift or second height is supplied by this finite calculation. Local norm points also do not define global universal norms or escape Howard's higher-height radical theorem.

Run:

    python3 -I -B research/proof_labs/local_norm_reference_11.py
    gp -q -f research/proof_labs/pari_local_norm_reference_11.gp > local37.txt 2>&1
    python3 -I -B research/proof_labs/local_norm_reference_11.py local37.txt

The full frozen transcript is certificates/session37_local_norm_reference.txt, SHA256 05dec73cfe2146e9b6756c54f914e27770e97df77c8ced4cb2af68ba6824fb26. Actual local run used PARI2.15.4 and Python3.12. Python constructs the differential from the curve/Hensel equation and traces by both Newton and companion matrices; maintained PARI independently uses ellformallog, ellformalexp, polynomial discriminant and polmod traces. All33 rational coefficients/traces/contributions, two truncations and the formal parameter agree. PARI also recomputes the base-point local logs on the minimal curve and independently reproduces every displayed reference scalar. Missing/duplicated rows, interpreter errors, changed result and incomplete output are refused. The finite periodic tail certificate, omitted degree11 term, nonintegral rational reduction and C11/mod121 mismatch are explicit controls. These checks are not expert mathematical review.

Source inputs: C0033 class-field certificate; Milne *Algebraic Number Theory* Proposition7.55/Remark7.56 (Eisenstein and uniformizer basis), https://jmilne.org/math/CourseNotes/ANT.pdf ; PARI official formal-group API, https://pari.math.u-bordeaux.fr/pub/pari/manuals/2.13.3/refcard-ell.pdf and built-in2.15.4 help; Bertolini–Darmon *Derived p-adic heights*, Proposition1.1 and Section1.2 (ordinary nonanomalous norm context and Kummer/local duality), https://www.math.mcgill.ca/darmon/pub/Articles/Research/13.Derived-p-adic/paper.pdf ; Howard Definition2.4.2 for the strict ordinary local condition, https://arxiv.org/pdf/1202.6358 . The Shapiro/corestriction identification is standard finite-index group cohomology with the coefficient action explicitly fixed above. No claim of a new norm theorem, independent human review or original complex BSD implication.

Next decisive arithmetic target: evaluate a positive supported global correction on a finite Galois refinement, with these explicit local residual references. A completion of the local problem is not a solution of that global embedding problem. The original complex comparison remains independently unresolved.

Local verification: all60 fixed Python workflow commands passed in65.94s; the updated PARI scalar transcript and its Python comparison were then run successfully again. The frozen transcript is checked in the Python matrix, and the orthogonal workflow independently regenerates it with GP. All six pull_request workflow families on the final commit remain required before merge.
