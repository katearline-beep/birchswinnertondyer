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

## Adversarial check and decision

Pure Python verifier:
  python3 -I -B research/proof_labs/session44_relative_tower_gate.py

It independently computes lower-central ranks over F11 for r=1,2,3 from the actual inverse-character unipotent action, confirms the group orders 11³/11⁵/11⁷ and the two successive kernels 11², checks explicit nonsplitting commutator and double-commutator values for every scalar higher-correction assignment in a bounded test, and fails if ell or Kummer input is removed. It does **not** prove C-0047's signed-duality hypotheses, actual existence of M₂, or any Galois field polynomial. The proof of the conditional *arithmetic existence* relies on Session36's source-dependent duality—not on passing this test.

**Priority/stop:** H1 40%: attempt an actual arithmetic realization of B's Galois action and c₁ and simultaneous ordinary localizations; H2 15%: second supported Bockstein only after c₁; H3 40%: source-defined exact complex third-derivative bridge in parallel; H5 5% diagnostics; H4/H6 parked. One safe lemma (the precise staged 121-kernel field existence conditional on existing source inputs), one credible leapfrog (explicitly construct c₁ with Shapiro/Greenberg normalization), one wild alternative (new characteristic-zero geometric vanishing theorem). Stop claiming progress if only the abstract group has been re-enumerated. **New implication toward original complex L''=0 or general BSD: NONE.**
