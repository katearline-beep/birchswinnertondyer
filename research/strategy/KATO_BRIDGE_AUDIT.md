# H1: exact derived-Kato literature applicability and leapfrog gap

**Source-anchored investigation, not a new theorem.** 2026-10-17. The aim is to prevent an apparently promising but invalid deduction about \(L''(E,1)\) for the curve of conductor 234446.

## Primary source actually inspected

David Burns, Masato Kurihara and Takamichi Sano, *On derivatives of Kato's Euler system for elliptic curves*, **J. Math. Soc. Japan 76 (2024), 855–919**, DOI [10.2969/jmsj/90699069](https://doi.org/10.2969/jmsj/90699069). Read the [published PDF](https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_pdf/-char/en), specifically printed pp.856–858 (Conjecture 1.1 and Theorem 1.3), then §§2–3 (precise hypotheses and proofs). Abstract language by itself is **insufficient** to identify the object whose order vanishes.

## What the paper says — typed objects and theorems

Fix a **finite real abelian** extension F/Q, G=Gal(F/Q), an odd prime p, and the p-adic Tate module T_p(E). Let \(I=\ker(\mathbb Z_p[G]\to \mathbb Z_p)\) be the augmentation ideal. Let \(r=\mathrm{rank}\,E(\mathbb Q)\), which is four for our curve.

- Derived norm: \(\mathcal N_{F/\mathbb Q}(z_F)\in H^1(\mathcal O_{F,S},T_p(E))\otimes_{\mathbb Z_p}\mathbb Z_p[G]\).
- **Conjecture 1.1(i):** its containment in \(H^1(\mathcal O_{F,S},T_p(E))\otimes I^{r-1}\). With \(r=4\), the exponent is **3**.
- **Conjecture 1.1(ii):** an integrality property of an \(\eta_{\rm BSD}\) element.
- **Conjecture 1.1(iii):** its derived image modulo \(I^r\) equals the Bockstein regulator of \(\eta_{\rm BSD}\). It is a *conjectural leading-term formula*, **not** an unconditional identification with complex L''.
- **Theorem 1.3:** under enumerated arithmetic hypotheses, the authors prove **only the containment in (i)**, not (iii) or complex analytic rank four. Do not present its term “order of vanishing” as order of vanishing of \(L(E,s)\).
- η_BSD is constructed from a higher complex L-leading quantity and arithmetic regulator data under assumptions described in the paper. Using η_BSD as if it were independently known without analyzing its analytic inputs risks circularity when the desired conclusion is precisely vanishing of a complex derivative.

The logical types are different:

```
[known E(Q) rank=4] + [hypotheses on Sha(E/F), p-adic image, E(Q_l)[p]]
         |
         v (BKS Theorem 1.3, conditional on its hypotheses)
[derived Kato norm belongs to I^3 within H1 ⊗ Z_11[G]]
         |
         X  no known proved comparison in our project
         |
         v
[COMPLEX analytic equation L''(E,1)=0]
```

This is a *broken arrow* diagram, not a proof. The published conjectural leading-term formula concerns an \(I^3/I^4\) class and an arithmetic Bockstein regulator; it must be proved and then shown to constrain the appropriate **complex** coefficient. It is not enough to compute a p-adic congruence.

## Concrete theorem-applicability checklist at p=11 (Theorem 1.3)

| Source condition | Our status | Validation obligation |
|---|---|---|
| (a) p>3 | **verified** p=11 | integer inequality |
| (b) \(\Sha(E/F)[11^\infty]\) finite | **NOT ESTABLISHED** | F is a real abelian field; our twist nonvanishing candidate concerns E^{-7}/Q, **not** finiteness of Sha(E/F) |
| (c) image of \(G_\mathbb Q\to\mathrm{GL}_2(\mathbb Z_{11})\) contains \(\mathrm{SL}_2(\mathbb Z_{11})\) | **needs theorem-level audit** | mod 11 GL2 argument from earlier C-0003 is not automatically identical to the full \(\mathbb Z_{11}\) statement unless an applicable lifting theorem is given |
| (d) E(Q_l)[11]=0 for every rational prime l in S | **needs place-by-place audit for chosen F** | S includes p=11, bad primes 2,117223, and primes ramifying in F; note this is not just a finite-field point-count |

For this particular curve the original minimal-model discriminant is 4·117223. At 11 reduction is good with #E(F11)=18. At 2 and 117223 the reduction is multiplicative with component orders 2 and 1, respectively; these facts are compatible with local absence of 11-torsion, but completing (d) **also requires** checking local p-torsion at primes ramified in the chosen F. One must specify F before claiming all conditions.

**Choosing F=Q is not a shortcut**: the trivial group-ring augmentation ideal contains no derived directional information; a finite extension is essential for any nontrivial augmentation-filtration experiment.

## Three research hypotheses of increasing risk

**K1 (low risk, precise):** There is a suitable finite real abelian field F and a choice of p=11 satisfying (a)–(d). *Falsifier:* 11-primary Sha finiteness has no unconditional certificate or one local torsion/imaging condition fails. This merely accesses an **already proven** derived containment; it does not address complex L''.

**K2 (medium, conditional):** An appropriate specialization of the *conjectural* BKS leading-term formula is provable on a manageable submodule for the curve, with an explicit regulator computation. *Falsifier:* the only accessible leading term contains the as-yet-unknown complex derivative as input, or the relevant module cannot be computed/certified. This could be a genuine p-adic/arithmetic result without resolving rank equality.

**K3 (leapfrog, extreme):** Construct a natural regulator comparison or reciprocity map whose source is an **independently computable** derived Kato/Selmer class and whose target constrains the second Taylor coefficient of the **complex** L-function. The map must be well-defined, injective or otherwise nondegenerate on the relevant quotient, and must not define itself by the unknown complex L''. *Falsifiers:* a control rank-two curve satisfies the source vanishing but has nonzero complex L'', or the comparison invokes BSD rank equality as an assumption. **We have not constructed this map**. The statement is a research schema until a target category and map are specified.

The original rank-four curve's apparently vanishing numerical L'' and nonzero L'''' help define a target, but *are not evidence for K3* (the proposed reciprocity). The fastest path to clarity is to separate K1/K2 from the genuinely new arrow required by K3.

## Small exact countermodel

[logic_gate_tests.py](logic_gate_tests.py) builds (a) a formal augmentation variable u with a Kato-like derived-class polynomial u^3 in I^3, and independently (b) two candidate complex Taylor germs t^2 and t^4. The containment holds in both cases, while the second derivative differs. This demonstrates **logical nonimplication without a bridge**. The toy polynomial is not a Kato Euler system and makes no claim to model all its arithmetic relations.

## Review requirements

1. A specialist should check the entire actual BKS theorem and full Hypothesis 2.2, not only the summary in this note; identify whether a more powerful published theorem already supplies any part of K3.
2. Locate exact relevant Selmer-complex/explicit reciprocity literature and ensure the direction and normalization of a putative comparison are valid.
3. When contacting authors or maintainers, ask a focused, falsifiable question about the missing comparison *after* a peer has reviewed this formulation; don't send a claim of having solved BSD.

**Decision (2026-10-17):** H1 is retained but **reframed as a missing comparison theorem**, with the existing order-of-vanishing containment downgraded to background. We currently have **no novel lemma about complex L''**.
