# Session44 — conditional existence of the exact first 121-kernel arithmetic field

**2026-11-20, America/New_York.** AI-assisted source-dependent corollary combining *previous* Sessions31/36/38 with Sessions42/43. This is **not** a newly proved implication toward BSD and is not expert reviewed. Previous full-problem checkpoint WPR-2026-11-20-01 remains valid, with exact complex L''(234446.a1,1)=0, nonzero complex fourth derivative, original Sha finiteness and full leading coefficient all **unproved**. No historical WPR snapshot is modified.

## One sharp question rather than another large enumeration

**Does the already-derived supported global FIRST-lift existence statement C-0047, when combined with the actual q23/q127 Frobenius-image constraints, imply existence of a finite arithmetic Galois field of a completely specified *relative* group type and precise support?**

**Answer, CONDITIONAL on the recorded source hypotheses: yes.** Crucially, this is *nonconstructive mathematical existence*, not an evaluated Galois cocycle or a computed number-field polynomial, not first-**Selmer**/Greenberg existence for arbitrary x, and certainly not a T³ second lift.

### Exact inputs and review boundaries

E/Q: y²+xy=x³−x²−79x+289, conductor 234446, rank4. Let K=Q(sqrt(-7)), p=11, V=E[11], L=K(E[11]), and Σ contain primes over 2,11,117223 and infinity. Let ell:G_(K,Σ)→F11 be the actual anti-cyclotomic first character, D1 its degree11 fixed field. Let x=P₂−2P₁ in E(Q) (positive under complex conjugation).

1. **C-0035/36** (Session31) obtains eleven-saturation of the five known points by independent reductions and, **subject to the residual-GL2 source argument**, Gal(L/K)=GL₂(F11), full Kummer translation Gal(L([11]⁻¹x)/L)=V, and disjointness from D1. Its image-degree claims are source-dependent, NOT independently constructed number fields.
2. **C-0044** (Session35) deduces the negative residual Selmer line using the focal exact Kurihara-number computation and Sakamoto's published theorem, with detailed residual/image/period and independent implementation caveats. C-0044 has NOT been independently reviewed by a subject-matter expert.
3. **C-0046/47** (Session36) uses that line, local11-torsion absence and Poitou–Tate / signed Euler characteristic to deduce H²(G_(K,Σ),T_11E)^−=0; thus the connecting obstruction to lifting every *positive* integral Kummer class to B₂=T_11E⊗Z11[[T]]/(T²) vanishes. This is **fixed-ramification-support GLOBAL H¹**, not a proof of the finer Greenberg local constraints. The exact positive sequence is 0→Z11*T κ(R)→H¹(G,B₂)^+→H¹(G,T_11E)^+→0. All original source-specialization assumptions and independent-review obligations remain in force.
4. **C-0050** (Session38) supplies the actual Frobenius23/127 inputs: h=Frob23^12, g=Frob127^10 both have rho=1, ell(h)=2, ell(g)=7; c₀(h)=0 and c₀(g)≠0 for x. Frobenius23 has irreducible characteristic polynomial X²+6X+1 over F11. Session42's exact group argument uses this irreducibility to generate the full coefficient translation space for any T²/T³ lift. These finite-arithmetic inputs do not require *independent* full GL2 surjectivity.

The statement below is a theorem **conditional on all those source-derived inputs**, not an assertion that C-0044's use of published theorems has been externally validated. No Sha(E/Q) finiteness is supplied or assumed in this corollary. The presence of a preprint-level or arithmetic hypothesis somewhere upstream is not concealed.

## Main conditional arithmetic-existence corollary

Let F_x=L([11]⁻¹x) and B=F_x D1. Then **under C-0035/36/44/46/47 arithmetic and source assumptions** there exists a finite Galois extension M₂/K, unramified outside Σ, such that:

1. M₂ contains B and L, and Gal(B/L)≅V×C11, order 11³=1331. The arithmetic first-layer base B is known only through its *defining division-point/ray-class description*, not an explicit primitive polynomial or full Galois table.
2. Gal(M₂/L) is **isomorphic to**
   \[
   G_2=(V\otimes_{\mathbf F_{11}}\mathbf F_{11}[T]/T^2)\rtimes C_{11},
   \]
   where e∈C11 acts by (1+T)^(-e). Hence |Gal(M₂/L)|=11⁵=161,051; this is a two-step 11-group with commutator subgroup TV of order 11²=121 and abelianization V×C11 of order 11³.
3. The next extension M₂/B has **order exactly 11²=121**, and its central relative group is TV≅V. The central extension over Gal(B/L) is **non-split**: the arithmetic h,g satisfy c₁([h,g])=−2c₀(g)≠0. It cannot be modeled by merely adjoining an independent **abelian direct-product** C11² layer.
4. With the C-0036 source assumption Gal(L/K)=GL₂(F11), the **conditional total degrees** are
   \[
   [L:K]=13,200,\quad [B:K]=17,569,200,\quad
   [M₂:K]=2,125,873,200.
   \]
   These are deductions from proven finite-group orders **assuming** the specified arithmetic image and lift input, not a computational construction of degree-two-billion fields.

**Proof:** By C-0047, the positive integral class κ(x) has a first global H¹ lift for the actual inverse anticyclotomic action with ramification contained in Σ. Reduce this continuous integral class modulo11. Choose any cocycle representative c=c₀+Tc₁ with coefficients V[T]/T². The map Ψ(s)=(c(s),rho(s),ell(s)) into the finite affine semidirect group is a continuous **homomorphism**; let M₂ be the fixed field of ker Ψ. Its order and support follow from finite continuous Galois theory. Mod T, Ψ is the Kummer/character representation cutting out B.

Inside ker rho, use h,g and w=g h²: ell(w)=7+2·2=0 and c₀(w)=c₀(g)≠0. Thus Ψ(w) is a pure translation with nonzero constant vector u∈V. Commutating with Ψ(h), whose ell value is2, gives −2Tu≠0. Conjugating w and [h,w] by sigma=Frob23, with irreducible residual rho(sigma), supplies four independent pure translations (the leading pairs u,Au in both degrees 0 and 1). They span **all** V[T]/T², while ell(h) surjects onto C11. Therefore Ψ(ker rho)=G₂, **independently of the unknown c₁ values or normalization**. The commutator subgroup equals (a−1)V[T]/T²=TV for a=(1+T)⁻². Hence the abelian quotient is precisely (c₀,ell), defining B, and the kernel M₂/B is TV, order121. The explicit commutator proves nonsplitting on the h,g subgroup. The total-degree formulas follow after multiplication by |rho(G)|=13200, an *additional, recorded assumption*.

**Important nuance:** Although the group is forced for *every* first lift, the field M₂ is not unique without choosing a global first-lift cohomology class. C-0047's one-parameter ambiguity Tκ(R) may change M₂. C-0049's normalized SELMER fibre is separately conditional on further finite height/duality inputs and a chosen local reference. Do **not** claim that the source-derived global existence automatically gives a Greenberg-compatible class, or that changing the R scalar repairs a local defect.

## What remains of the T³ question

Suppose **further** that the same c₀ has a compatible *second* lift c₂ in A₃=V[T]/T³ with the same support. Then Session42 proves the minimal M₃ has
  Gal(M₃/L)=G₃=(V[T]/T³)⋊C11,
  |G₃|=11⁷=19,487,171,
and M₃/M₂ has order11²=121, with kernel T²V. The source-dependent total degree would be 257,230,657,200. Unlike M₂, **existence of M₃ has NOT been deduced from any existing theorem.**

The staged relative tower, all contingent on the recorded inputs, is:
  L = K(E[11])
    ⊂ B = L([11]⁻¹x) D1                  (relative 11³; given arithmetic base)
    ⊂ M₂ = first Bockstein-affine field   (relative factor 11²; conditional existence via C-0047)
    ⊂ M₃ = second Bockstein-affine field  (relative factor 11²; existence **open**).

For r=1,2,3 the forced relative groups G_r have lower central quotients of F11-dimensions
  G₁: (3),                         |G₁|=11³;
  G₂: (3,2),                       |G₂|=11⁵;
  G₃: (3,2,2),                     |G₃|=11⁷.
The lower central terms are G_r^(1)=(a−1)V[T]/T^r, G_r^(2)=(a−1)²V[T]/T^r etc. The corresponding extension from G₂ to G₃ is **again nonsplit** over the given Frobenius subgroup: Session43's conditional double bracket [h,[h,g]]=4T²c₀(g) is nonzero, while its mod-T² image is zero. The r=2 existence cannot be used to assert r=3 existence; that would assume vanishing of the still-unknown, properly supported secondary obstruction.

This staged approach is precisely why enumerating a 2-billion-degree field is not a computational solution. The useful arithmetic object is an explicitly **presented solvable 121-kernel embedding problem** with actual global and local maps. The next experiment must exhibit a concrete *Galois* presentation of B and evaluate the correction cocycle/cochains, not merely simulate G₂ or G₃.

## A constructive Kummer-radicand acceptance test for the first 121-kernel

The conditional field existence can be translated into **two explicit arithmetic objects to search for**, rather than an abstract "solve the embedding problem" directive.

**Fact:** the Weil pairing places the entire group \(\mu_{11}\) inside L=K(E[11]) and therefore inside B=F_x D1. The central relative kernel \(\operatorname{Gal}(M₂/B)\simeq V\) has exponent11 and rank two. By ordinary Kummer theory for a field containing \(\mu_{11}\), there must be two independent classes
  \([a_1],[a_2]\in B^\times/B^{\times11}\)
such that, after choosing compatible 11th roots,
  \(M₂=B(\sqrt[11]{a_1},\sqrt[11]{a_2}).\)
This is an **existence of radicands conditional on C-0047 and the prior relative-group theorem**, not a computation of a₁,a₂.

Let \(\Gamma_0=\operatorname{Gal}(B/L)\simeq V\times C_{11}\), generated by two Kummer translations \(\sigma_1,\sigma_2\) and one anticyclotomic element \(\tau\) with ell(τ)=1. Define W=span([a₁],[a₂]). The centrality of the relative 121-kernel means **each class in W is fixed by every element of Γ₀**, whereas Galois descent to K additionally requires the correct dual Galois module for the full Gal(B/K) (the cyclotomic twist cannot be discarded; the Weil pairing identifies Hom(V,μ11) with V equivariantly).

For every \(s\in\Gamma_0\) and chosen \(a_j\), invariance means there is a \(b_{s,j}\in B^\times\) with
  \(s(a_j)/a_j=b_{s,j}^{11}.\)
For commuting base elements s,t define the computable roots-of-unity discrepancy
\[
 \epsilon_{s,t,j}
   =\frac{s(b_{t,j})b_{s,j}}{t(b_{s,j})b_{t,j}}\in\mu_{11}.
\]
Indeed raising this ratio to the eleventh power gives 1 because st=ts on B. After normalizing the Weil/dual basis and the sign convention, \(\epsilon\) measures the **commutator of lifted Galois generators** acting on \(\sqrt[11]{a_j}\). A candidate pair of radicands must yield the **specific nondegenerate vector-valued commutator pairing**
  \([(\ell,e_i),(\ell',e_j)]=\ell'e_i-\ell e_j\)
prescribed by the G₂ group law, as well as the trivial commutators among the \(\sigma_i\). The scalar 11th-power equations alone, even with linear independence of radicands, DO NOT certify this extension class.

**A complete relative-group acceptance list:** (i) a₁,a₂ independent mod 11th powers; (ii) W pointwise Γ₀-invariant and correctly equivariant under Gal(B/K); (iii) all displayed power equations and normalized epsilon commutator relations hold; (iv) lifts of τ,σ₁,σ₂ have **order 11** (so do their permitted products), not 121; (v) tame primes of B outside Σ have valuations \(v(a_i)\equiv0\pmod{11}\), and the remaining 11-adic local fields are checked under the actual ordinary Greenberg and Shapiro identifications. The last condition cannot be inferred from (i)-(iv).

### An exact adverse example: correct commutators, WRONG 11th powers

The pth-power check in (iv) is essential, not an implementation nicety. Model relative elements as \((e,x,y)\in F_{11}\times V\times V\) with multiplication
  \((e,x,y)(f,u,v)=(e+f,x+u,y+v-eu).\)
This is the desired G₂: its central commutator is \((0,0,fx-eu)\), and its 11th powers all vanish.

Now modify **only** the final y-coordinate by adding
  \(\lfloor(e+f)/11\rfloor z_1\),
where e,f are represented as integers 0,…,10 and z₁ is one fixed basis vector of the central V. The integer carry is a normalized 2-cocycle for C11, so the new law is associative and has **the same commutator pairing**. But τ=(1,0,0) now satisfies \(\tau^{11}=z_1\ne1\); this extension has elements of order121. It cannot be the required G₂ despite passing the commutator test. The augmented exact verifier checks the carry cocycle, commutator pairing and τ-order mutation. This falsifies a tempting shortcut: "two radicands with the expected commutators therefore realize the first affine lift."

**Practical next test:** avoid constructing enormous B explicitly if possible; instead search for the Γ₀-invariant two-dimensional, Gal(B/K)-equivariant Kummer eigenspace and certify the 11th-power equations **plus** commutator and order conditions by a smaller class-field/Kummer character presentation. If a precise stable W cannot be exhibited, stop and report the arithmetic realization as genuinely missing. Local Greenberg compatibility and the original complex BSD bridge remain separate.

---

## Exact good-prime local cohomology: uniqueness, not just existence

Session43 constructed explicit *local* q127 Frobenius T³ jets (10,7,5) in a chosen residual eigenbasis. Their coefficients are gauge-dependent. Nevertheless an **intrinsic** statement is available: the **unramified local cohomology lift is unique at the level of cohomology**, simultaneously at truncation depths 1,2,3.

For r=1,2,3 set A_r=V⊗F11[T]/T^r, where at an unramified good place with arithmetic Frobenius q the action is the explicit 2r×2r matrix
  F_{q,r}=rho(Frob_q)⋅(1+T)^(-ell(Frob_q)).
For the procyclic unramified quotient,
  H¹_unr(K_q,A_r)=coker(F_{q,r}−I).

- At q23, rho(Frob23) has polynomial X²+6X+1 and **no eigenvalue1**. Consequently F_{23,r}−I is invertible in every truncation r≤3: **dim H¹_unr(K_q23,A_r)=0**.
- At q127, rho(Frob127) has eigenvalues 1 and6, and ell(Frob127)=4≠0. On the 1-eigenspace, F_{127,r} acts as a single Jordan block of size r with eigenvalue1; its cokernel is one-dimensional. The 6-eigenspace block has invertible F−I. Thus **dim H¹_unr(K_q127,A_r)=1 for r=1,2,3**. The reduction map to H¹_unr(K_q127,V), which is a quotient of the same cokernel, is surjective and both sides are one-dimensional, hence an **isomorphism**. Therefore the given nonzero Kummer residual class at q127 has **exactly one unramified local H¹ class lift** to A₂ or A₃. This does **not** mean it has one canonical cocycle representative; the values (10,7,5) from Session43 depend on the chosen representative.
- Falsifier: if ell(Frob127)=0, the three 1-eigen components do not form a nontrivial Jordan chain, and **dim H¹_unr(K_q127,A_r)=r**, not1. The observed actual ell=4 is essential to local uniqueness.

The amended Session44 exact verifier constructs every Frobenius matrix and independently checks their ranks 2r, 2r−1 and r for r=1,2,3, including the nonzero chosen generator u₀=(5,1) modulo (F−I). This new computation confirms that these two *good-prime* local classes contribute **no additional higher-jet local cohomology freedom**; the difficult remaining compatibility is **global** and involves the **ordinary11-adic Greenberg places**. These good-prime calculations, despite their exactness, do not prove an actual global c₁/c₂ or support a BSD implication.

---

## Adversarial check and decision

Pure Python verifier:
  python3 -I -B research/proof_labs/session44_relative_tower_gate.py

It independently computes lower-central ranks over F11 for r=1,2,3 from the actual inverse-character unipotent action, confirms the group orders 11³/11⁵/11⁷ and the two successive kernels 11², checks explicit nonsplitting commutator and double-commutator values for every scalar higher-correction assignment in a bounded test, and fails if ell or Kummer input is removed. It does **not** prove C-0047's signed-duality hypotheses, actual existence of M₂, or any Galois field polynomial. The proof of the conditional *arithmetic existence* relies on Session36's source-dependent duality—not on passing this test.

**Priority/stop:** H1 40%: attempt an actual arithmetic realization of B's Galois action and c₁ and simultaneous ordinary localizations; H2 15%: second supported Bockstein only after c₁; H3 40%: source-defined exact complex third-derivative bridge in parallel; H5 5% diagnostics; H4/H6 parked. One safe lemma (the precise staged 121-kernel field existence conditional on existing source inputs), one credible leapfrog (explicitly construct c₁ with Shapiro/Greenberg normalization), one wild alternative (new characteristic-zero geometric vanishing theorem). Stop claiming progress if only the abstract group has been re-enumerated. **New implication toward original complex L''=0 or general BSD: NONE.**
