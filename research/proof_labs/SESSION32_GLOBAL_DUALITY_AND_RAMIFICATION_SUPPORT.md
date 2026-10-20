# Session32 — absolute lift existence and the obstruction hidden by forgetting support

2026-10-20. AI-assisted source deduction; internally audited, not independently expert reviewed. Claims C-0037/38; experiment EX-019; candidate LF-016. Predeclared issue: https://github.com/katearline-beep/birchswinnertondyer/issues/64 . Baseline: 630e863a7fbfde24bffd500596f995f5dea4e1bc.

## Result and scope

Conditional on the recorded residual-image and local arithmetic inputs, **every residual class in H¹(G_{K,Σ},E[11]) has a continuous lift to H¹(G_K,E[11]⊗F11[T]/T³)** for the actual first anticyclotomic character. This is an existence theorem allowing unspecified finite auxiliary ramification. It does not construct correction cochains, impose Greenberg conditions, or give integral Tate-module lifts.

At the same time **dim_F11 H²(G_{K,Σ},E[11]) ≥ 3**, and the map from this group to absolute H²(G_K,E[11]) is zero. Thus the unrestricted existence result discards a genuine space of possible fixed-support obstructions. We do not prove any particular first or second Bockstein is nonzero in that space.

These deductions refine Session31's open arithmetic-realization question, without contradicting its finite-quotient no-go. That quotient is too small; absolute G_K permits too much ramification. A supported Selmer calculation remains the target.

## Objects and recorded inputs

E/Q is [1,-1,0,-79,289], conductor 234446=2·117223, discriminant 4·117223. K=Q(√−7), p=11, V=E[11]. Σ consists of the places above 2,11,117223 and the complex place. All three rational primes split in K, so their completions are Q_l.

The coefficient dual throughout is the **Cartier dual** M^D=Hom(M,μ11), with its Galois action. Weil pairing gives V^D≅V. Plain linear dual V* is not interchangeable with V: the cyclotomic determinant twist matters.

Inputs from C0007/20/33/35/36:
1. The recorded residual image on G_K is GL2(F11). Its source argument uses split I1 Tate monodromy at117223 for a transvection, irreducible Frobenius23 (a23=−6, discriminant10 mod11) for a transverse line, elementary generation of SL2, and determinant disjointness K∩Q(ζ11)=Q. It remains subject to expert review; this session does not recompute it.
2. The genuine first anticyclotomic layer D1/K has group C11, is unramified outside11, and is disjoint from K(V). Indeed GL2(F11) has abelianization F11* of order10, so no C11 quotient. Hence the joint image is GL2(F11)×C11.
3. E(K_v)[11]=0 for v in Σ. At2 nonsplit I2 has nonsingular group order3 and component order at most2, with pro2 formal kernel. At117223 split I1 has nonsingular group order117222≡6 mod11, trivial component group and pro117223 formal kernel. At11 good reduction has order18, and the formal logarithm on11Z11 is torsion-free. **Order18 alone would not exclude formal11-torsion.** Complex H² is zero.
4. Five actual MW classes are independent mod11 by C0035's determinant5 certificate. Their Kummer classes lie in H¹(G_{K,Σ},V): outsideΣ good prime-to11 reduction makes Kummer classes unramified.

Let χ:G_K→F11 be C0033's character, and set k=−χ for the inverse Iwasawa convention. Put A3=V⊗F11[T]/T³ with action ρ(g)(1+T)^{k(g)}. In characteristic11 this is well defined for k mod11. In coefficient coordinates (x0,x1,x2), its matrix is lower triangular with blocks A, kA, binom(k,2)A. We use the actual finite coefficient module, not E[121].

The exact sequence 0→W=T A3→A3→V→0 has W filtered by two copies of V. Its Cartier dual is filtered by two copies of V^D. In the joint finite image, s=(−I,0) is central and acts as −1 on W and W^D.

## Lemma A: absolute localization is injective

For M=V or W, let L/K be the finite Galois splitting field of M^D and G=Gal(L/K). The image of s remains central and acts as −1. If c is a 1-cocycle of G in M^D, comparing c(sg) and c(gs) gives

    −2 c(g) = (g−1)c(s).

Since −2 is invertible in F11, c is a coboundary. Thus H¹(G,M^D)=0 (the central-scalar/Sah argument).

Now consider an absolute class locally zero at all places (indeed outside any finite set suffices). Its restriction to G_L is a homomorphism to M^D. Choose a finite normal extension through which the cocycle and action factor. Chebotarev tests each element in the kernel of the coefficient action by an unramified Frobenius. Local triviality forces the cocycle value there to be zero, since that element acts trivially on M^D. Consequently the class inflates from H¹(G,M^D), which is zero.

This is the argument in **Milne, Arithmetic Duality Theorems, 2nd ed. (2006), I Lemma9.3**. Hence the absolute local-trivial kernel X¹(K,M^D) vanishes. Applying **I Theorem4.10(a)** with S all places, its perfect pairing with X²(K,M) implies X²(K,M)=0. Therefore

    H²(K,M) → ∏_v H²(K_v,M)

is injective. Only the kernel is used; no surjectivity is asserted.

This is a general finite-module duality argument. We do **not** apply Milne I Theorem9.2's solvability hypotheses, nor I Proposition9.12's nonsplit CENTRAL-extension theorem: our GL2 embedding problem has noncentral kernel and does not meet that shortcut's hypotheses.

## Lemma B: unrestricted residual T³ lifts exist (C-0037)

For c0∈H¹(G_{K,Σ},V), let δ(c0)∈H²(K,W) be the connecting obstruction for A3.

At each finite v∈Σ, H⁰(K_v,V^D)=0 by the recorded local calculation. The filtration of W^D then implies H⁰(K_v,W^D)=0. **Milne I Corollary2.3**, local Tate duality, gives H²(K_v,W)=0.

OutsideΣ the modules and c0 are unramified. Naturality puts the local connecting class in the image of H²(Gal(k_v^sep/k_v),W)=0: the residue Galois group has 11-cohomological dimension one. Thus δ(c0) is locally zero everywhere. Lemma A forces δ(c0)=0 globally. The cohomology long exact sequence supplies the claimed lift.

A representative can be adjusted by a coboundary so its constant coefficient is a chosen representative c0. The correction coefficients exist as continuous finite-module cochains; we have not evaluated them. Continuity means a lift factors through a finite extension, so any extra ramification is finite, but this proof gives neither its primes nor an effective supported construction.

The same proof applies to the first-order sequence with kernel V. This resolves unrestricted weak-solvability of the residual cover problem from Session31 under the listed inputs. No assertion of a prescribed full T³ splitting-group image is needed.

Crucially, **no first-height radical hypothesis is used**: the result holds for every supported residual class. That is a warning that absolute residual lift existence is much weaker than lifting an exact rational S2 class in the Selmer complex.

## Lemma C: the supported obstruction space has dimension at least three (C-0038)

Write X^i_Σ(K,M)=ker(H^i(G_{K,Σ},M)→⊕_{v∈Σ}H^i(K_v,M)). This is a finite-module localization kernel, **not** the elliptic Tate–Shafarevich group and **not** the absolute kernel using all places.

Local Kummer images satisfy:
- At the four places above2 and117223, E(K_v)/11E(K_v)=0, using the same prime-to11 component/reduction and formal-group facts.
- At the two places above11, each quotient has F11 dimension one, by good nonanomalous reduction and formal logarithm.
- At the complex place the quotient is zero.

Thus localization of the five-dimensional known MW subspace lands in a space of dimension at most two. Rank–nullity gives at least three independent classes in X¹_Σ(K,V). This does not compute the actual local matrix or its rank, nor assert the full Selmer or MW dimension.

Finite-Σ Poitou–Tate duality (**Milne I Theorem4.10(a)**, with Σ containing the primes above11 and infinity) pairs X¹_Σ(K,V^D) perfectly with X²_Σ(K,V). Self-duality of V and Lemma C's kernel give dim X²_Σ(K,V)≥3. All H²(K_v,V) for v∈Σ vanish by local duality, so

    dim_F11 H²(G_{K,Σ},V) = dim X²_Σ(K,V) ≥ 3.

Finally every class in H²(G_{K,Σ},V) has locally zero absolute inflation. At Σ local H² is zero; outsideΣ inflation factors through residue H²=0. Absolute localization injectivity from Lemma A implies that **the entire inflation map H²(G_{K,Σ},V)→H²(K,V) is zero**.

This proves the loss of support information is mathematically substantial. It does not identify δ(c0) in the supported group, prove δ(c0)≠0, or compute any second pairing. In particular it is not a nonexistence theorem for the desired Selmer lifts.

## Source and applicability audit

Primary source: J. S. Milne, *Arithmetic Duality Theorems*, 2nd ed., 2006, https://jmilne.org/math/Books/ADTnot.pdf , Chapter I Cor2.3, Thm4.10(a), Lemma9.3. Number field, finite 11-primary modules, 11 invertible in K, Σ includes archimedean and11 places; all hypotheses explicitly used above.

Independent perspective: A. Pál and T. Schlank, *The Brauer–Manin obstruction to the local-global principle for the embedding problem*, arXiv:1602.04998v2, https://arxiv.org/pdf/1602.04998 , Thm1.1 and its discussion of the locally trivial H² obstruction and dual H¹ kernel. Their abelian-kernel setting matches residual kernel V or W in characteristic zero. We use Milne's direct cohomological proof; neither source is being claimed to enforce our restricted ramification or Greenberg conditions automatically.

Prior art/novelty: these are standard global-duality and central-scalar methods specialized to recorded inputs, not a claimed new duality theorem. No novelty award, Lean verification, human review or BSD implication.

## Translation, falsification, and next experiment

**Exact transfer:** nonabelian deformation/embedding problems are governed here by the connecting H² class of an exact sequence of actual finite Galois modules. Global duality evaluates its local-global obstruction. This is a typed mathematical bridge, not a scalar-Massey analogy.

**Validation transfer:** abstraction refinement in formal methods warns that forgetting constraints may erase obstructions. Here the exact map from supported H² to absolute H² is zero although the source has dimension≥3. The executable controls verify Cartier-dual matrix identities for all13200 GL2(F11) matrices, the truncated action and central scalar, and synthetic constrained/unconstrained complexes with both first- and second-order failure. They cannot verify Chebotarev, Poitou–Tate, the recorded arithmetic, or actual Selmer cochains.

Falsifiers: failure of residual-image/disjointness or any local torsion calculation invalidates the specialization; omitting the determinant twist invalidates self-duality; a local or supported class surviving the claimed vanishing contradicts a proof step and requires correction. Replacing the central scalar by identity leaves H¹(C11,F11) nonzero, so the argument cannot be generalized without its hypotheses.

Next decisive experiment: construct a finite-support cochain presentation for the actual augmentation module and compatible Greenberg local homotopies, locate the supported connecting classes, and exhibit allowed local corrections or a precise surviving obstruction. The ≥3 lower bound prioritizes this calculation; it does not pre-answer it. A residual answer still needs integral/torsion control and normalized duality before h2.

Stop if all that is supplied is an unrestricted lift or a synthetic obstruction matrix. No original complex L'' theorem, analytic-rank-four proof, original Sha finiteness or BSD leading-term result follows.

## Reproduction and coordination

New control: python3 -I -B research/proof_labs/global_duality_support_controls.py . Python standard library only, deterministic, exact F11 arithmetic, no seed or external dependency. Expected final line: PASS: finite-module and support-loss controls; no arithmetic Selmer lift computed.

This session has no usable local execution environment. The Python command and repository checks must run in exact-head GitHub CI before merge; no local Python or GP execution is claimed. Script outputs corroborate algebraic controls only, separately from the source deductions above.

The other instance's rank-two-converse branch ad91e78 and old H3 branch e17b3bc were inspected, not modified or merged. Coordination was posted on PR63; fuller uncommitted handoff material is not presumed published. H3's characteristic-zero motive/comparison and independent vanishing gates remain open. This work touches the global/support lifting question only.
