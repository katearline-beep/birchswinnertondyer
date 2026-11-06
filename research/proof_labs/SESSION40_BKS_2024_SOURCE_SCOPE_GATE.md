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
