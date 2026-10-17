# High-upside BSD research portfolio — October 2026

**Category:** Research hypotheses and route selection, **NOT claimed new conjectures/theorems**. The decision target is the original curve **234446.a1**, not the already numerically well-behaved −7 twist. Status: all six proposed breakthroughs are open. Scientific goal: identify a valid mechanism for vanishing of the complex second derivative, not merely a zero of a different p-adic L-function.

## The exact bottleneck

Let E/Q: y²+xy=x³−x²−79x+289. Its arithmetic rank is 4, conductor 234446, root sign +1. Its **completed** L-function, Λ(E,s)=(sqrt(N)/(2π))^s Γ(s)L(E,s), has an even functional equation about s=1. (Uncompleted L(E,s) is generally **not** an even function.) A nonzero central L-value would imply rank zero by analytic rank-zero theorems, contradicting known rank four, so L(E,1)=0. Then Λ'(E,1)=0 by parity, forcing L'(E,1)=0. If **L''(E,1)=0**, the completed parity relation Λ'''(E,1)=0 also forces L'''(E,1)=0. Conversely if L'' is nonzero the raw L''' need not vanish: writing A(s)=(sqrt(N)/(2π))^s Γ(s), its relation is L'''(E,1)=-3(A'(1)/A(1))L''(E,1) when L=L'=0. Thus the missing route to *order at least four* is exactly **L''(E,1)=0**. To establish order *exactly* four also requires L^(4)(E,1)≠0 (in principle certifiable by rigorous real intervals); full BSD additionally requires Sha finiteness and the correct leading-coefficient identity.

The LMFDB reliability note presently labels 234446.a1's analytic rank as 2 or 4, not rigorously distinguished. **A tiny numerical value of L'' is not a proof that it is zero.** Separate original-complex, anticyclotomic-p-adic and twist L-functions at every step.

## Selection criteria

For each route keep five fields: (A) precise proposed mathematical bridge, (B) theorem assumptions, (C) strongest result that would follow *if bridge were proved*, (D) a low-cost kill test, and (E) explicit stopping rule. These are ideas to **challenge**, not results to cite.

| Track | Portfolio bet | How it could touch L''(E,1) | Near-term falsifier / milestone | Upside | Risk |
|---|---|---|---|---|---|
| H1 | **Derived Kato / Perrin–Riou** | Build a provable higher-derivative explicit reciprocity linking rank-four global points to the complex 2nd derivative | Read 2024 Burns–Kurihara–Sano theorem hypotheses and isolate the exact *missing* implication for E and p=11 | Very high | Very high |
| H2 | **Multi-directional Iwasawa/Bockstein heights** | New mixed cyclotomic–anticyclotomic reciprocity could constrain original complex derivative | Map actual ordinary height, modified one-place Selmer complex, local splittings, and L-function normalization; seek one cross-height value | High if bridge exists | Very high |
| H3 | **Quadratic-field tomography** | For each odd-root-number twist with L'_D(1)≠0, (L(E/K_D))'''(1)=3 L''(E,1)L'_D(1); seek a geometric formula forcing left side zero | Verify the identity symbolically; find 3 suitable K_D splitting the conductor, with distinct local conditions; identify an actual higher-Gross–Zagier theorem | Very high if formula found | Very high |
| H4 | **Modular-symbol/Mazur–Tate congruences** | Infinite compatible exact congruences of *appropriately related derived* classes might force a global zero, after a proven comparison to complex L'' | Check if a proposed congruence is about the *same* invariant as complex L''; generate modest finite congruences with 389a1 rank-two negative control | High | Very high |
| H5 | **Adversarial central-curvature laboratory** | Not a direct proof of zero, but could quickly falsify mathematical assumptions; a rigorous nonzero L'' would be an extraordinary contradiction requiring independent audits | Compute L'' and L^(4) numerically at ≥2 precisions for 234446.a1 and rank-two control 389a1, using PARI's ellL1; never infer exact zero from smallness | Very high diagnostic value | Low implementation, high interpretive risk |
| H6 | **Exact geometric period cancellation** | Find a proven symmetry/period relation showing the L'' period pairing is zero, not merely small | Test candidates against full Atkin–Lehner and Hecke action; exclude generic sign/parity explanations already insufficient for rank four | Transformative | Extreme |

### H1 — Derived Kato "rank-to-analytic" bridge

Starting literature: Burns, Kurihara, Sano, *On derivatives of Kato's Euler system for elliptic curves*, J. Math. Soc. Japan 76 (2024), 855–919, DOI 10.2969/jmsj/90699069. Their generalized Perrin–Riou conjecture relates higher complex L-derivatives and derived Kato zeta elements and their abstract states an order-of-vanishing result in arbitrary rank **under hypotheses**. That does **not** itself state BSD rank equality. Our first challenge is to diagram exactly which arrow connects point rank four to a *complex L'' vanishing*, versus only an order statement about algebraic Kato elements.

**Working hypothesis, not known:** four independent Kummer classes impose a second-order vanishing condition on a suitably normalized derived Kato regulator, and a proven explicit reciprocity transfers it to complex L''. Search for a rank-two control where the same proposed implication *must fail*, then find the hypothesis that distinguishes it. An explicit conditional theorem with one independently plausible missing hypothesis would be useful even if the conjecture fails.

**Stop:** if the available theorems concern only p-adic L-function vanishing without a bridge to the complex Taylor coefficient, label it a promising *p-adic* result but do not describe it as progress on the analytic rank-four gap.

### H2 — Mixed-direction derived regulator

Starting literature: Agboola–Castella (2021); Castella–Hsu–Kundu–Lee–Liu, *Derived p-adic heights and the leading coefficient of the Bertolini–Darmon–Prasanna p-adic L-function* (published 2025); Castella (2017), two-variable p-adic Gross–Zagier/Beilinson–Flach classes. Develop the **actual one-place** modified Selmer complex at split p=11, with cyclotomic and anticyclotomic directions. Calculate one genuine cross pairing before speculative statements about its radical. The predicted anticyclotomic order six is a different derivative object from complex L''.

**Working hypothesis, not known:** a two-variable explicit reciprocity or deformation identity provides an algebraic obstruction which, under independently verified non-degeneracy, implies a relation on the **complex** rank-four derivative. Write the arrow and hypotheses precisely or stop.

### H3 — Field tomography and higher Heegner geometry

For K_D = Q(sqrt D), where D<0 is a fundamental discriminant and gcd(D, N)=1 with all primes of N split, let F_D(s)=L(E/K_D,s)=L(E,s)L(E^D,s). If the twist has odd sign and L'(E^D,1)≠0, then (using L(E,1)=L'(E,1)=L(E^D,1)=0)

`F_D'''(1)=3 L''(E,1)L'(E^D,1)`.

Thus **one proven vanishing** F_D'''(1)=0 implies the target L''(E,1)=0. Varying K_D gives different geometric incarnations of exactly the same unknown number, which is the key leverage (not just accumulating examples). Try to identify a theorem computing F_D''' in terms of a higher Heegner cycle whose vanishing follows from four global rational points. A higher-rank "Gross–Zagier" bridge is a research problem, not an available theorem assumed here.

**First exact field screen:** [field_tomography_candidates.py](field_tomography_candidates.py) enumerates negative fundamental discriminants for which 2, 117223 and 11 all split. The four smallest are **−7, −87, −95 and −127**. For all of these, the quadratic twist has predicted root sign −1 and conductor \(N D^2\) under the standard coprime conductor formula. We have **not** yet checked that any twist except −7 has nonzero central derivative, much less obtained a higher Heegner-cycle vanishing formula.

**Stop:** if variation merely reproduces the analytic factorization without a new arithmetic/geometric identity, it has NOT advanced the proof.

### H4 — Modular-symbol congruence microscope

Finite calculations mod 11^m can never prove a real number zero without a valid algebraic interpolation/period comparison. Work on Mazur–Tate elements and derived Kato congruences that **are algebraic**. Design compatibility tests as m and conductor change; use 389a1 rank-two and 5077a1 rank-three controls. Seek a published or newly provable period relation before targeting complex L''.

**Stop:** if a method only shows numerical p-adic divisibility of an unrelated L-value.

### H5 — Falsification-first central derivative benchmark

Implement a PARI/GP program using documented `ellL1(E,r)` for r=2,4, with different numeric precisions, plus the 389a1 control. No threshold-based rank claiming. The test should succeed only if it actually executed and output data, and should explicitly print that apparent zeros are inconclusive. An independent Sage/FLINT route and a rigorous interval estimate are separate later tasks. **A nonzero rigorous L'' for E=234446.a1 would be a purported counterexample to BSD; rule out software, model, and interval errors *before* any public announcement.**

## First diagnostic observation (2026-10-17)

The new **independent PARI/GP** direct-derivative workflow ran on the original model and the rank-two control 389a1. Using documented `ellL1(E,r)` (numerical method, *not* zero certification):

```
389a1:          L''(1) ~ 1.51863300057685354046
234446.a1:      L''(1) ~ -2.33089041160e-56   (40-digit calculation)
234446.a1:      L''(1) ~ -2.55240108738e-96   (90-digit calculation)
234446.a1:    L''''(1) ~ 214.65233750162133711402 (stable 40/90-digit)
```

This strongly supports a numerical *analytic rank-four* classification for 234446.a1: the apparent second derivative shrinks with precision while fourth derivative is stable and nonzero; the rank-two control's second derivative remains visibly nonzero. **This is not a newly proved mathematical fact.** The small values are consistent with numerical error/truncation and there is no exact-zero certificate. In particular, the apparent 90-digit residual at approximately 10^-96 is not meaningful evidence of a literally negative nonzero derivative. It is exploratory guidance for H1/H3/H6 only.

### H6 — Period identity search

Explore whether an explicit modular parametrization, a Hecke projector, or a geometric cycle yields a *second-order* annihilation not explained by ordinary even functional-equation parity. Try exact candidate identities in period/cohomology spaces and falsify on rank-two controls. If every candidate is only an Atkin–Lehner sign +1 relation, it cannot force a second-order zero: stop.

## Parallel allocation and gates

Allocate *investigation effort*, not proof confidence: **H1 30%, H3 25%, H2 15%, H4 10%, H5 15%, H6 5%**. H5 starts immediately as cheap instrumentation; H1/H3 remain the principal breakthrough bets. Promote a track only when it produces a correct new theorem, explicit counterexample, or exact unproved lemma with a realistic validation route. Downrank it when an expert theorem/literature search already settles the question or its proposed bridge fails.

Every track must record its **input, proposed mathematical link, falsifiable prediction, counterexample/negative control, references, and decision log** in `research/harness/experiments.json`. Green CI and numerical evidence cannot upgrade a claim to mathematical review or theorem status. Failures and dead ends should remain public and citable.

## References / prior art

- LMFDB, [reliability of elliptic L-data](https://www.lmfdb.org/L/2/136800/1.1/c1/0/83/Reliability) (234446.a1 analytic rank 2 or 4).
- [Burns–Kurihara–Sano 2024](https://doi.org/10.2969/jmsj/90699069), derived Kato Euler system and generalized Perrin–Riou conjecture.
- [Castella–Hsu–Kundu–Lee–Liu](https://arxiv.org/abs/2308.10474), derived BDP p-adic heights and leading coefficient.
- [Castella 2017](https://doi.org/10.1112/jlms.12058), two-variable p-adic heights/Heegner and Beilinson–Flach classes.
- [Agboola–Castella 2021](https://doi.org/10.5802/jtnb.1174), anticyclotomic p-adic BSD.
- [PARI/GP ellL1 documentation](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html), derivative computations *numerical*.
- [John Cremona ecdata](https://johncremona.github.io/ecdata/), exact rank-two control 389a1.

**No new BSD proof or previously unknown conjecture is asserted here.** The novelty, if any, would arise from an independently validated bridge or theorem developed in one of these tracks.
