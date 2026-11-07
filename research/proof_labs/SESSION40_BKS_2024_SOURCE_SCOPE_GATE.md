# Session 40 — Burns–Kurihara–Sano source-scope gate (2026-11-06)

**Status:** preliminary source-triage note, AI-assisted and unreviewed. **New proved implication toward original complex BSD: NONE.** Base: PR #79. This note is deliberately not a C-series theorem claim and does not update the immutable weekly review.

## Exact question
Does Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, J. Math. Soc. Japan **76** (2024), 855–919, DOI 10.2969/jmsj/90699069, prove the original characteristic-zero complex equality `L''(234446.a1,1)=0` from the focal curve's known rank four?

## Evidence actually inspected
Publisher abstract, https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_article/-char/en (accessed 2026-11-06). It describes (i) a **new generalized Perrin–Riou conjecture** relating Darmon-type derivatives of Kato zeta elements to higher complex L-derivative values, (ii) an **unconditional arbitrary-rank order-of-vanishing part under mild technical hypotheses**, (iii) a higher-rank Rubin formula for **p-adic** L-function derivatives, and (iv) an explicit relation between p-primary classical BSD and an Iwasawa main conjecture. These are distinct assertions.

**Scope gate:** The publisher abstract does NOT state that the unconditional order-of-vanishing result proves the complex analytic rank bound. The relevant full theorem statement, definition of its order filtration, and hypotheses have **not yet been checked**. No inference to original complex `L''=0` is licensed by this abstract. In particular, a theorem about the order of an Euler-system derivative or p-adic L-function is not automatically a theorem about the order of the original complex L-function.

## Typed dependency graph
Known rank E(Q)=4 -> [Kummer / arithmetic Selmer inputs]. Published BKS order-vanishing theorem -> [output type TO BE VERIFIED from full text]. Generalized Perrin–Riou comparison of Darmon derivative and higher complex L-derivative -> **conjectural in publisher abstract**. Missing arrow: verified unconditional map from the theorem's exact output to original complex `L''(E,1)`, with all focal hypotheses. Therefore no new implication.

## Adversarial negative control (logical)
Let formal arithmetic output `A=0` and independent complex Taylor coefficient `B=1`. Any proposed implication `A=0 => B=0` fails without an additional comparison hypothesis. This is a model of the *invalid inference*, not a model of an elliptic curve. The concrete falsifier is to locate in the full BKS text an **unconditional theorem** explicitly identifying the relevant derivative of the original complex L-function, check all hypotheses for E234446a1, and revise this note if one exists. Conversely, if the only comparison is the generalized Perrin–Riou **conjecture**, keep H1/H4 complex bridge blocked.

## Next decisive test / priorities
1. Read full paper, identify exact theorem/lemma numbers and their output objects, not just the abstract.
2. Construct a table: source theorem; input ring and local conditions; output; focal hypotheses; conjectural dependencies; complex comparison.
3. Compare to C-0008 Mazur–Tate circularity gate and existing H1/H4 no-go; do not relabel a conjectural complex comparison as a theorem.
4. If an unconditional source-matched complex arrow is found, request independent arithmetic-geometer review before any claim promotion.

**Allocation:** retain H1 40%, H2 15%, H3 40%, H5 5%, H4/H6 parked. This source check is a low-cost H1/H4 scope falsifier, not a reason to reactivate H4. Do not spend more digits on local p-adic logs or original L'' approximations. No tests are introduced by this documentation-only note. The full PR #79 CI and required negative controls remain the validation gate; none are claimed executed in this session.


## Full-text theorem audit (added 2026-11-07; supersedes preliminary abstract-only gate)

**Primary full text:** Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, J. Math. Soc. Japan 76 (2024), 855–919, https://kurihara.math.keio.ac.jp/bks4.pdf. The following numbered results and hypotheses were checked against the full-text introduction and Section 6; this is not independent human review.

- **Conjecture 1.1(i)** (p.857) predicts `N_{F/Q}(z_F) ∈ H¹(O_{F,S},T_p(E)) ⊗ I^{r-1}`, with `r=rank E(Q)`. The object is a cohomology-valued *equivariant norm of Kato's zeta element*, and `I` is the augmentation ideal of `Z_p[Gal(F/Q)]`. It is **not** `ord_{s=1} L(E,s) >= r`.
- **Theorem 1.3** (p.857) proves precisely this containment assuming **(a)** `p>3`; **(b)** the `p`-primary part of `Sha(E/F)` is finite; **(c)** the image of `G_Q→GL₂(Z_p)` contains `SL₂(Z_p)`; **(d)** `E(Q_l)[p]=0` for every prime `l∈S`. The source explicitly calls these conditions. For focal `p=11`, (a) passes. **(b) is unproved for F=Q, and for general F**. (c) requires a full integral image certificate, not merely mod-11 residual irreducibility. (d) requires local torsion checks at every prime of S, not just ordinary reduction at 11. Therefore **we cannot assert Theorem 1.3 applies to our focal example**, even to the cohomological norm, without further work.
- **Conjecture 1.1(iii)** is the conjectural **leading term** identity between the cohomological norm's image in `I^{r-1}/I^r` and a Bockstein regulator applied to `eta^BSD`. The latter contains the relevant complex leading-value information. The paper does **not** prove this identity in arbitrary rank. Theorem 1.5 concerns the analytic-rank-one case, not rank four.
- **Proposition 6.1** (p.895, citing Kato's Theorem 18.4) gives a rank-based augmentation lower bound for the **p-adic** L-function: `L_{S,p} ∈ I^r` for good or nonsplit multiplicative reduction, `I^{r+1}` for split multiplicative reduction. This is not a bound on the vanishing order of the **complex** L-function. Theorem 1.9 / 6.2 is a higher-rank Rubin formula for a **p-adic** leading term, again not the complex derivative.

**Adversarial hypothesis-control:** A hypothetical curve satisfying (a),(c),(d) but with unknown/infinite `Sha(E/F)[p∞]` does **not** meet the stated Theorem 1.3 hypotheses; a rank-four algebraic curve with an `I³`-divisible cohomological zeta norm can still have an unconstrained complex quadratic Taylor coefficient absent a separately proved comparison. This is a *logical nonimplication*, not an example of an actual elliptic curve with BSD failure.

**Sharper stopping rule:** Do not spend time computing (c) and (d) merely to claim unconditional applicability: (b) remains the decisive blocker. If an independent Sha-finiteness result becomes available, verify integral Galois image and all S-local p-torsion, then consider the cohomological filtration. For the original complex `L''`, demand a distinct unconditional source theorem or a new proof of Conjecture 1.1(iii) with noncircular `eta^BSD` hypotheses. **Result: NO NEW BSD IMPLICATION; H4 stays parked.**

**Additional source-scope warning:** The project uses anticyclotomic `K=Q(sqrt(-7))` classes as well as cyclotomic classes. The BKS theorem is formulated for finite **real abelian** `F/Q`; do not silently substitute an imaginary quadratic field or anticyclotomic tower into its theorem.
