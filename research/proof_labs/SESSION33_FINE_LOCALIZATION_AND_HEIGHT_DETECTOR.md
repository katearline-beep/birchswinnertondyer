# Session33 — predeclared fine-localization / supported-Bockstein test

2026-10-20 America/New_York. Baseline de7f12a / PR65. AI-assisted and unreviewed. Plan: issue66.

Before computation: recover the actual mod11 Kummer localization of the five known MW classes from normalized local logarithms and nonanomalous formal groups. Test the predicted fine basis P2, P3−2P1, P4−9P1. Then audit finite Selmer-duality naturality: a supported global first lift must have first height zero against every locally trivial residual test class. Only if integral coefficient/base-change and unit character normalization match may a nonzero measured height detect a supported obstruction.

Safe lemma: actual local Kummer matrix. Credible leapfrog: detect an obstruction by duality without constructing huge Galois fields. Wild option: core vertices or higher geometric cycles, with no established original-complex comparison. Falsifiers: wrong local Kummer interpretation, missing integral comparison, nonunit character rescaling, or a test class that is not fine. No original complex BSD progress is expected.

Predeclared auxiliary-support extension (before subset computation): tame inertia requires an added good prime to have an11-torsion reduction direction. C0035's five split reduction primes are candidates. Restrict their actual reduction rows to the known three-dimensional fine MW space; test whether their row span contains the first-height detector. Failure gives a fine-class dual certificate that the selected support still cannot lift R. Passing is only necessary, because unknown fine Sha directions may remain. Enumerate all subsets of the fixed five candidates and preserve explicit failing witnesses.

Predeclared adaptive prime design (before searching): the five preselected independence primes need not be efficient obstruction-killing primes. Search good split primes q<=20000 with valuation-one11-primary reduction, asking for a NONZERO local row on the three fine MW classes proportional to (2,5,10). A hit removes the known-MW necessary obstruction only; it does not certify the full fine group or a lift. Failure in this bounded search proves no nonexistence. In parallel audit whether the central-scalar/isotypic Kummer argument plus Chebotarev can realize any prescribed functional on the entire finite fine group, yielding nonconstructive one-auxiliary-prime existence for a single supported H2 class.

## Outcome and exact scope

Conditional on the recorded arithmetic and source-normalized **integral first-height** inputs, the actual negative point R has a nonzero supported first Bockstein. Consequently R cannot have a residual first lift over G_{K,Σ}; every unrestricted lift from C0037 must acquire extra ramification. This is a source/duality deduction, not an evaluated Galois 2-cocycle.

A standard Chebotarev/isotypic-module argument also shows that **one suitably chosen auxiliary K-prime suffices to kill any one class of H²(G_{K,Σ},E[11])** under the stated image/local hypotheses. This is nonconstructive, concerns the first residual global lifting stage, and enforces no Greenberg or second-stage compatibility.

The bounded arithmetic search finds **q=3389** with the correct localization functional on the known fine MW classes. It does not certify that this particular prime works on the full fine group. No supported arithmetic lift or second height is constructed. C0039 is the actual finite Kummer kernel; C0040 is the conditional supported obstruction; C0041 is the one-prime existence/explicit candidate distinction.

## C0039 — a typed finite Kummer map

E is the minimal model [1,-1,0,-79,289]; its short model is w²=z³−1267z+17230. K=Q(√−7), p=11. Σ contains the places above2,11,117223 and infinity. In the short coordinates,

    P1=(15,40), P2=(19,4), P3=(23,16), P4=(31,88),
    R=(−3355/63, (128780/1323)√−7).

C0035 makes their five residual Kummer classes independent; denote their F11 span by M. This is not an assertion that M is the full11-Selmer group.

At v|11, good reduction has order18 and no11-torsion. The formal logarithm on E1(Q11) is an isomorphism to11Z11. Since multiplication18 is a unit on the11-primary completion,

    E(Q11)/11E(Q11) → F11,
    Q ↦ log_short([18]Q)/(18·11) mod11

is an isomorphism. Thus zero residue here means **actual local11-divisibility**, not an approximation to an unspecified height. The minimal-model invariant differential is twice the short one, an11-adic unit change. PARI uses the minimal curve, [18]Q and division by36·11 to match this normalization.

At v above2 or117223 the local Kummer quotient is zero: the component/reduction orders are prime to11 and the formal pro-l group is11-divisible (C0007/37/38). At the complex place it is zero. OutsideΣ good prime-to11 Kummer classes are unramified. Therefore the exact typed map is

    M ⊂ H¹(G_{K,Σ},V) → ⊕_{v∈Σ} H¹(K_v,V),  V=E[11],

whose image on M lies in the two local Kummer lines. The recomputed matrix in the order P1,P2,P3,P4,R is

    L = [[4,0,8,3,9], [4,0,8,3,2]] mod11.

Its rank is2; the complete kernel **within M** is three-dimensional with basis

    Y1=P2,  Y2=P3−2P1,  Y3=P4−9P1.

These are actual residual fine-localization classes. This upgrades the old local-log coefficient calculation using an explicit finite-Kummer bridge and C0035 independence. It does not identify a Q11 height radical, the whole fine group, or elliptic Sha. In particular finite11-divisibility is not literal zero of the integral local logarithm.

The guarded Jacobian implementation and a separate PARI minimal-model calculation agree on all ten residues modulo121: (81,81),(33,33),(96,96),(3,3),(108,13). No first-height assumption is needed for C0039.

## Integral duality bridge: why a fine class detects a global obstruction

Let C_Sel be the ordinary Selmer complex for the lattice T11(E), with unramified conditions away11, and let C_G=RΓ(G_{K,Σ},T11(E)). Reduce in the **derived** sense modulo11. Write C_c for compact-support cohomology, the cone of global-to-local cochains shifted by−1. The coefficient sequence for the first anticyclotomic augmentation is

    0 → V·T → A2=V⊗F11[T]/T² → V → 0,

with action ρ(g)(1+T)^{−χ(g)}. This is not the coefficient sequence 0→E[11]→E[121]→E[11]→0.

Projection of complexes gives the naturality square

    H¹(C_Sel/11) --β_Sel--> H²(C_Sel/11)
          |                         |
          v                         v
    H¹(G_{K,Σ},V) --β_G--> H²(G_{K,Σ},V).

The lower Bockstein is the connecting obstruction to a supported A2 lift. Global duality and the self-dual ordinary local conditions give compatible pairings

    H²(C_Sel/11) × H¹(C_Sel/11) → F11,
    H²(G_{K,Σ},V) × H¹(C_c(V^D)) → F11,

where V^D=Hom(V,μ11)≅V by Weil pairing, not plain linear dual. The projection in degree2 is adjoint to the compact-support-to-Selmer map in degree1.

For a fine MW class y, choose its compact-support lift y_c. Its image in the Selmer complex is the ordinary Kummer Selmer class of y. At11 this follows because H⁰(K_v,F⁻V)=0 (the nonanomalous unit root is5), so H¹(F⁺V)→H¹(V) is injective. Away11 the unramified H¹ injection has the same property. Thus local triviality in full H¹ also trivializes the local Selmer component; no missing local homotopy is being assumed as a new arithmetic computation.

Naturality of the cup-product duality then gives the **finite integral identity**, up to one fixed convention sign,

    <β_G(x), y_c>_PT = <β_Sel(x), y>_Sel = h_Nek(x,y) mod11.

In particular, if a supported global first lift of x exists, its β_G is zero, and its first height against every such fine y is zero mod11. No full Selmer upper bound or assertion that all fine classes are MW is required for the contrapositive.

Trusted source/proof inputs: Nekovář's compact-support and Selmer dualities/naturality (Selmer complexes, §§5.4,6.3,9.7,11.1), explicitly recalled in Macias Castillo–Sano **2026 PREPRINT**, §2.3.4 equations(2.3.3)–(2.3.7), Proposition4.7 and §4.3. The argument above applies their cone/cup-product naturality to the global projection; it is our stated specialization/derivation, not a quotation of a source theorem about this curve.

### Why rational comparison alone is insufficient, and the integral bridge used

C0031 uses BD Theorem2.18(4) on MW classes and BCLMN equations(14)–(15): the BD cross-height is −q(P+R). The preprint MCS Theorem4.2 gives the opposite Nek/Bockstein sign. For this application we need more than an equality after tensoring Q11. MCS Proposition4.7 gives integral perfect/self-dual Selmer complexes and coefficient base change; §4.3 defines the modulo11^n pairing on C/11^n, and §4.4 explicitly compares the **finite** BD and Bockstein pairings for every n. BD §2.4/Theorem2.18(4) gives compatibility with MW Mazur–Tate heights. The integral Bockstein and reduction commute by the coefficient-sequence square above. Equality of the integral MW values inside Q11, with the same character and unit normalization below, therefore identifies their mod11 reductions. We are not reducing an arbitrary rationally rescaled pairing.

Retained assumptions/review boundary: the recorded Cartan/residual and local hypotheses for these source results, ordinary nonanomalous local conditions, p-prime-to-Tamagawa input, the accepted BCLMN global height formula/normalization and C0029 corroboration. The finite comparison remains sourced to a preprint, not independently peer-reviewed by this project. Passing code does not prove this integral diagram or validate those theorems. No twist analytic certificate is needed for the R obstruction.

### Character calibration is a unit, not a discarded11 factor

BCLMN uses ρ=(1/11)log with the sqrt(−7)=+2 orientation. C0033 uses the opposite ratio r^{-1} and ell=log_12((r^{-1})^10). On unramified arithmetic Artin elements,

    ρ = [log(12)/(10·11)] ell,    ell ≡ 10ρ mod11.

The bracket is an11-adic unit, residue1/10. Frobenius density extends this character identity; the inverse Iwasawa action and global duality sign must be kept separately. All110 unit ratios modulo121 satisfy the same calibration in the executable control. Multiplying the character by11 would erase the residual detector and is explicitly rejected as a harmless normalization. We report height coordinates in the BCLMN ρ normalization; conversion to the C0033 Γ coordinate multiplies by a fixed unit, with the convention sign recorded rather than inferred from tests.

## C0040 — a specific supported obstruction is nonzero

C0029's complete direct-coordinate first-height oracle recomputed here gives

    q(P2+R) ≡ 2 mod11,   squared sigma/ideal ratio =100 mod121.

The independently corroborated full first row is a=(1,2,7,8). In ρ-normalization the fine-class detector on β_G(R) is

    ( h_Nek(R,Y1), h_Nek(R,Y2), h_Nek(R,Y3) ) = (2,5,10) mod11,

up to the common nonzero unit/sign from the chosen Γ/duality coordinate. Hence **β_G(R)≠0 in H²(G_{K,Σ},V)**, conditionally on the explicit integral/source/height inputs above. The point R has no supported residual A2 lift. Consequently it cannot have a supported A3 lift either, since reduction would give an A2 lift. C0037's absolute lifts are consistent: all acquire auxiliary ramification.

This is a dual certificate for a class in actual arithmetic cohomology, not an evaluated representative of that class. The three values are tests against known fine MW classes, not coordinates in a proved complete basis of H². Positives P_i have zero values against these three positive tests by conjugation symmetry; this **does not show β_G(P_i)=0**, because unknown fine negative classes may detect it.

Even adding both primes above127 does not fix the R obstruction: Y1+Y3=P2+P4−9P1 is locally11-divisible at the old Σ and at both127 places, while its height against R is1 mod11. Thus it remains a fine-class obstruction witness for that enlarged support.

## C0041 — one-prime existence and targeted arithmetic support

### Standard auxiliary-prime lemma, with a proof and no novelty claim

Under C0037/38's residual/local hypotheses, any single η∈H²(G_{K,Σ},V) can be killed after enlarging Σ by **at most one** finite K-prime outsideΣ. If a nonzero η is specified, choose a prime with one-dimensional unramified H¹(K_v,V). The prime in this existence argument is not computed.

Proof:
1. Since local H² atΣ is zero, finite-Σ Poitou–Tate identifies η with a linear functional λ on X¹_Σ(K,V^D). If η=0 there is nothing to kill. Otherwise fix a basis y1,...,yd of this finite fine group and use V^D≅V.
2. The simultaneous cocycle map for this basis has image **V^d⋊GL2(F11)**. Indeed central−I gives H¹(GL2,V)=0. If the translation subgroup in V^d were proper, the matrix-span/isotypic argument of C0036 would give a nonzero scalar relation among the restrictions of the y_i. Inflation–restriction would make that relation a global coboundary, contradicting their independence. No Maschke theorem in characteristic11 is used.
3. Choose A=diag(1,a) with a∈F11* and a≠1. The quotient V/(A−1)V has dimension one. In the full semidirect image choose the translation coordinates so that their images in this quotient are exactly the functional values λ(y_i). Chebotarev realizes that conjugacy class as an unramified Frobenius outsideΣ. A change of representative multiplies the common target coordinate by a unit and leaves its kernel unchanged. One may choose a degree-one K-prime, avoiding any finite forbidden set; degree-two primes have density zero among K-primes.
4. For Σ'=Σ∪{v}, every fine class for Σ' is unramified at v, hence inflates from Σ. Thus X¹_Σ'(K,V^D) identifies with the kernel of localization at v in X¹_Σ(K,V^D), which by construction is ker λ. Inflation of η has zero local image at v because the old class is unramified there and residue-field H² is zero. It is therefore in X²_Σ', and the naturality of Poitou–Tate pairs it trivially with the entire X¹_Σ'. Perfect duality forces its inflation to vanish.

This is a specialization of standard Chebotarev, isotypic Kummer and duality methods, not a claimed new general theorem. The argument needs the **full fine group** in step1; it does not make the known MW basis complete. Local H² at the new prime can be nonzero: we kill the specified class, not the whole new H² group. Applying the lemma to β_G(R) proves existence of a first residual lift with one auxiliary prime, but gives neither its cochains nor Greenberg conditions. Nothing here supplies a compatible second-stage lift. One may allow the conjugate prime as well if conjugation-stable support is desired.

For possible extra ramification awayΣ, tame inertia also gives a useful necessary type condition. If a first correction ramifies at a good v∤11, its inertia value z∈V is nonzero, and Frob·τ·Frob^{-1}=τ^{Nv} implies ρ(Frob)z=(Nv)z. Weil self-duality/determinant Nv makes this equivalent to an eigenvalue1, hence E(k_v)[11]≠0. Wild pro-l inertia cannot map nontrivially to V. This is a necessary condition, not a promise that every such prime works.

### Exact necessary test on the five known candidate primes

Restrict C0035's actual reduction homomorphisms to (Y1,Y2,Y3). Both conjugate places give the same row here because all Y_i are positive rational combinations:

| q | row on Y1,Y2,Y3 |
|---|---|
|127|(4,10,7)|
|743|(0,9,4)|
|907|(1,1,3)|
|1087|(1,7,2)|
|1117|(10,5,3)|

A proposed subset must have row span containing a_F=(2,5,10). Otherwise a vector in its common kernel but not ker(a_F) gives a surviving fine MW obstruction witness for R. All32 subsets were checked both by row reduction and independent enumeration of such dual witnesses. No singleton or pair passes. Eight of the ten triples pass. This lower bound applies **only to this declared five-prime menu**, not to all primes, and passing remains necessary rather than sufficient for a lift.

### A better designed prime:3389

A predeclared ascending search over good split q≤20000, requiring v11(#E(Fq))=1, found a hit after27 eligible primes:

    q=3389, sqrt(−7)=154,
    #E(F3389)=3498=11·318,
    cyclic11-torsion generator (short model)=(668,1888),
    row on P1,P2,P3,P4,R = (1,10,5,4,8),
    row on Y1,Y2,Y3 = (10,3,6) = 5·(2,5,10) mod11.

An independent PARI minimal-model count, torsion projection and all five discrete logs agree. Both conjugate primes have the same restricted positive row. Thus **every known fine MW class that remains fine after adding3389 annihilates the R height detector**. The known obstruction tests no longer rule out that support.

This is not a computed lift over K with that support. Unknown fine classes, including possible Sha contributions, may have additional functional values. If the three known Y_i exhausted the full fine group, the duality argument would prove that3389 kills β_G(R); that completeness premise is unproved. Finite twist Sha is not trivial twist Sha[11], and none of our rank-one analytic input removes that uncertainty.

## Cross-disciplinary transfer, negative controls, and next decision

Exact transfer: global/compact-support duality turns arithmetic local triviality into a **dual infeasibility certificate** for a lifting equation. The elementary row-span/annihilator step is finite-field linear algebra; its analogy with Farkas-style optimization certificates does not import real convexity or prove an arithmetic hypothesis. Adaptive experimental design then selects a prime whose measured localization matches the obstruction, rather than collecting independent rows without reference to the task.

Controls: a non-fine test class detects a local boundary even though its global image is zero; all local boundary rows annihilate the fine basis; multiplying the character by11 destroys the test; an extra hidden fine class defeats any completeness conclusion from known-MW zero tests. A finite-module control realizes every prescribed three-coordinate functional and rejects a proper diagonal translation image; it does not simulate Chebotarev. GP output with interpreter errors, missing rows or a mutated P2 residue is rejected. Source theorems, expert review, a full Selmer basis and actual Galois cochains are outside what these controls verify.

Next decisive work: use3389 as an explicitly typed first-stage support candidate, and seek a supported cochain construction or a certificate for the missing full-fine directions. R is a benchmark, not the exact positive S2 target for h2; stop auxiliary-prime searches now that a designed candidate is available. Do not spend resources enumerating the huge Kummer closure or accumulating more height digits. The one-prime theorem is not a Greenberg or higher-order local solver.

Whole-problem checkpoint: H1/H2 remain active around genuine constrained cochains. H3's other-instance motive/converse branches remain separate; no characteristic-zero complex comparison or independent vanishing exists. H4/H6 remain parked and H5 diagnostic. **New proved implication toward original complex L'' or BSD: none.** No nonzero genuine second height, full Selmer upper bound, original Sha finiteness, analytic rank-four theorem or leading coefficient follows. Human/expert review and novelty are not claimed.

## Primary references and reproduction

- Milne, *Arithmetic Duality Theorems*, 2nd ed.2006, I Cor2.3, Thm4.10(a), Lem9.3: https://jmilne.org/math/Books/ADTnot.pdf . Finite supported duality and Chebotarev reduction; hypotheses as in Session32.
- Bertolini–Darmon, *Derived p-adic heights*, §2.4/Theorem2.18(4): https://www.math.mcgill.ca/darmon/pub/Articles/Research/13.Derived-p-adic/paper.pdf . MW comparison, with the integral/tower compatibility distinguished above.
- Macias Castillo–Sano, *On Selmer complexes, Stark systems and derived p-adic heights*, arXiv2603.23978v1, **2026 preprint**, §2.3.4, Prop4.7, §§4.3–4.4: https://arxiv.org/pdf/2603.23978 . Finite Selmer duality and Bockstein comparison, not a new complex analytic-rank theorem.
- Balakrishnan–Ciperiani–Lang–Mirza–Newton, *Shadow lines in the arithmetic of elliptic curves*, Prop1.4, Prop2.4, equations14–15: https://arxiv.org/pdf/1610.08729 . Individual first-height formula, not the rank-two shadow-line theorem on our rank-four curve.
- PARI elliptic-curve documentation: https://pari.math.u-bordeaux.fr/dochtml/html/Elliptic_curves.html . Independent ellpadiclog/ellcard/ellmul arithmetic.

Python standard library, exact integer/Fraction and F11 arithmetic; no random seed. The local runtime was available again this session. Python3.12.14 and PARI2.15.4 ran locally; GitHub CI must verify its own declared versions and exact published head. No claim of formal proof verification.

    gp -q -f research/proof_labs/pari_fine_localization_11.gp > /tmp/fine-localization33.txt 2>&1
    python3 -I -B research/proof_labs/fine_localization_height_detector.py /tmp/fine-localization33.txt

The Python comparator rejects GP diagnostics even if the interpreter returns status0. Standalone Python mode recomputes the same arithmetic without an oracle comparison. Expected output includes local rank2/fine dimension3, q(P2+R)=2, ell=10rho, all32 support controls, and q3389's fine row=(10,3,6). Baseline de7f12a and issue66 preserve the precomputation plan. Exact branch/CI/merge SHAs are recorded by the linked PR rather than self-referentially embedded here.
