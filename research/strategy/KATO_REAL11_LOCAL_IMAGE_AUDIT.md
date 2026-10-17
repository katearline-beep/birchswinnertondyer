# Local-hypothesis audit for derived Kato experiment over the real 11-cyclic field

**17 October 2026 — C-0007, existing arithmetic theory specialized to one curve.**
**Status:** exact input checks plus a mathematical reduction using standard Tate-curve, Néron reduction and elementary-group theorems. External expert review outstanding; **not** a proof of Burns–Kurihara–Sano's Theorem 1.3 for this curve because its 11-primary Sha finiteness hypothesis remains open. No BSD breakthrough is asserted.

## The concrete field and theorem target

Take
```
E: y² + xy = x³ − x² − 79x + 289
N=234446=2·117223, Δ_min=4·117223, c4=3801, c6=−232605
p=11
F=Q(zeta_23)^+,   Gal(F/Q)=C11
```
Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, J. Math. Soc. Japan **76** (2024), Theorem 1.3 and Conjecture 1.1, [DOI](https://doi.org/10.2969/jmsj/90699069), concerns a **derived Kato norm in an augmentation filtration** for **real** abelian F/Q. It does *not* directly assert complex analytic rank. See the [missing-comparison audit](KATO_BRIDGE_AUDIT.md).

## The four source hypotheses — explicit status

| Source requirement | Status for F | Why |
|---|---|---|
| p>3 | Checked | 11>3 |
| E(Q_ℓ)[11]=0 for every finite ℓ in S(F) | **Arithmetic argument; external review needed** | S(F)⊆{2,11,23,117223}; precise residue and Néron data below |
| Image of ρ_E,11 contains SL₂(Z₁₁) | **Mathematical argument supplied; external review needed** | Tate-curve full inertia at split I₁ prime 117223, and Frobenius at 3 moves inertia's line |
| Sha(E/F)[11^∞] finite | **OPEN** | No unconditional theorem or computational upper bound is provided by this work |

The first three rows are not substitutes for the fourth. At most this audit **isolates the one major hypothesis** still unresolved for this chosen example, subject to expert checking the standard lemmas.

### A. Local 11-torsion at the rational S-primes

The original integral curve is minimal and semistable with conductor N, so its bad primes are 2 and q=117223. For F=Q(ζ₂₃)^+ the only new ramified rational prime is 23. Thus take S={2,11,23,q} (enlargements must be checked afresh).

- **ℓ=2:** minimal discriminant valuation 2 and c₄ a unit imply multiplicative type I₂. Counting the nodal reduction gives a₂=−1, i.e. **nonsplit** multiplicative. Its nonsingular identity component over F₂ has order 2+1=3 and the component group order is at most 2. Neither is divisible by 11. Reduction kernels are pro-2, so E(Q₂)[11]=0.
- **ℓ=q=117223:** valuation of Δ is 1 and c₄ a q-adic unit: type I₁. Since −c₆ is a square modulo q (verified by Euler's criterion), reduction is **split** multiplicative. The nonsingular F_q group has order q−1≡6 mod 11, and the component group has order one. The reduction kernel is pro-q. Hence E(Q_q)[11]=0.
- **ℓ=23:** good reduction with exactly #E(F₂₃)=30 (including infinity). Since 11∤30 and the reduction kernel is pro-23, E(Q₂₃)[11]=0.
- **ℓ=11:** good ordinary reduction with #E(F₁₁)=18, a₁₁=−6. The point-count excludes 11-torsion from the reduction group. Unlike ℓ≠11, the reduction kernel is pro-11, so **point counting alone does not suffice**: the standard elliptic formal-group logarithm on 11Z₁₁ rules out its 11-torsion for this unramified base field (11≥3). Therefore E(Q₁₁)[11]=0.

**Stronger check:** for the actual completions of F over S, the residue degrees at 2,11,q divide [F:Q]=11 and are therefore f=1 or f=11; the extensions at these primes are unramified. At 2, f is odd, so nonsplit remains nonsplit and 11∤(2^f+1). At q, split stays split and 11∤(q^f−1). At 11, the reduction count modulo 11 satisfies #E(F_(11^f))≡1−a₁₁^f≡1−5≡7 mod 11 for f=1 or 11, and the local formal group has no 11-torsion over unramified 11-adic completions. At 23, F/Q is totally ramified with residue F₂₃; 11∤30. These stronger conclusions E(F_v)[11]=0 follow from the same standard reduction theorems, though BKS only requires the rational E(Q_ℓ)[11] condition. Do not confuse this torsion check with Sha finiteness.

### B. Full 11-adic Galois image: a shorter proof route

At q=117223, E has **split multiplicative type I₁**. The Tate uniformization provides a Z₁₁-basis in which inertia has matrices
`[[1,t],[0,1]]`, where t runs over **all** Z₁₁ because the Tate parameter has valuation exactly one at q. This is a full unipotent root subgroup U⁺⊂ρ(G_Q).

At the good prime 3, direct counting gives #E(F₃)=7 and a₃=−3. Frobenius has characteristic polynomial
`T²+3T+3`, discriminant −3≡8 mod 11, a **nonsquare**. Thus its reduction has no invariant line over F₁₁ and, for the invariant line of U⁺, carries it to a transverse line.

The conjugate Frobenius·U⁺·Frobenius⁻¹ is then a **second full unipotent root subgroup** fixing the transverse line. After a Z₁₁ basis change adapted to the two primitive lines, these are the full upper and lower elementary unipotent subgroups. Over Z₁₁, those generate SL₂(Z₁₁) by elementary row operations/Bruhat decomposition. Hence, **assuming the standard Tate-curve inertia and group-generation lemmas**, the image contains SL₂(Z₁₁). Since its determinant is the cyclotomic character, it is plausibly all GL₂(Z₁₁) as well, though BKS only needs the SL₂ containment.

[The exact checker](kato_field_local_image_audit.py) independently verifies the reduction counts, splitness residues, discriminant, and **finite-field illustration** that upper/lower elementary unipotents generate all 1320 elements of SL₂(F₁₁). It does **not** prove that a particular Galois representation contains a full unipotent over Z₁₁ or the infinite matrix-group lemma; those are the cited mathematical inputs. **A specialist should scrutinize this argument**, especially the exact Tate parameter valuation and full inertia image.

### C. Why the degree-11 field actually exposes a new graded layer

For a real quadratic F and p=11, the augmentation ideal I satisfies I²=I because 2 is invertible in Z₁₁. That is a poor experiment for rank-four derived order three. By contrast
`F₁₁[C₁₁]≅F₁₁[T]/T¹¹`, so I³/I⁴≠0 mod11 for the chosen F. This is **elementary finite algebra**, not an Euler-system calculation.

## Counterexample-first controls

The good prime ℓ=199 has #E(F₁₉₉)=220, divisible by 11. Prime-to-199 torsion lifts through reduction, so E(Q₁₉₉)[11] is nonzero. Thus a hypothetical field **ramified at 199** would fail the local no-torsion condition, demonstrating this screening actually distinguishes permitted candidates. ℓ=199 is **not** in S(F) for the selected F.

## Honest status and next leapfrog gate

- **New deliverable:** the arithmetic checks and source-based local/Galois proof route, with a new favorable field F and one adverse-control prime.
- **Not delivered:** a derived Kato norm in I³/I⁴; a proof that Sha(E/F)[11∞] is finite; a new reciprocity comparing that norm to L''(E,1); a new BSD case.
- **Next cheap decisive experiment:** determine if the BKS derived norm can be *defined and reduced modulo 11* in this 11-cyclic extension with a computationally available modular-symbol or cohomology presentation, *without* quietly assuming Sha finiteness or the complex rank equality. If no such finite algorithm exists, park H1 and shift resources to H3.
- **Expert-review request:** check the local Tate inertia at I₁, the unipotent generation over Z₁₁, local 11-torsion at 11, and exact source hypotheses in BKS 2024 Theorem 1.3.

Sources: [BKS 2024](https://doi.org/10.2969/jmsj/90699069); J. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves*, ch. V on Tate uniformization; [Sage's Tate-curve documentation](https://sporadic.stanford.edu/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_tate_curve.html) for the equality between the Tate parameter valuation and multiplicative reduction index; [Casselman, *Classical and adelic automorphic forms*, Lemma 1.3 and Corollary 1.4](https://www.math.ubc.ca/~cass/research/pdf/Adeles.pdf) for elementary generation over fields and finite p-power rings; J. Silverman, *The Arithmetic of Elliptic Curves*, chs. IV/VII on reduction/formal groups. **Authored as human–AI exploratory mathematics, not independently peer-reviewed.**
