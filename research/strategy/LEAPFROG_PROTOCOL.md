# Leapfrog-conjecture protocol (LCP-1)

**Status:** research strategy, not a claim of new mathematical results. **Goal:** find a *new, valid mathematical implication* that removes an otherwise intractable BSD proof obligation. One must not confuse boldness with proof.

## What qualifies as a leapfrog?

A **leapfrog conjecture** is a clearly specified *missing theorem or counterexample target*, capable—**if proved and after checking hypotheses**—of bypassing an identified hard step in a conventional route. It is not merely a prediction of BSD, a more precise computation, a metaphor, or an already published theorem.

Every active exploratory track (EX-004 onward) needs a corresponding LF entry in [leapfrogs.json](../harness/leapfrogs.json), even when the decisive idea has not been found; in that case the entry must say **NO VALID BRIDGE IDENTIFIED**. A candidate is automatically classified as **speculative** until independently reviewed. An imaginative idea is not a theorem, and apparent novelty requires a prior-art audit.

## Before each new experiment, do this

1. **Target:** Which exact current obstruction? Here: \(L''(E,1)=0\) for E=234446.a1, not the vanishing order of an unrelated p-adic L-function. Specify original/completed versus uncompleted L-functions.
2. **Baseline:** Identify the existing theorem or method and why its hypotheses/output do **not** settle the target. Cite the specific theorem, its variables, and conditions; do not rely on an abstract.
3. **Leapfrog statement:** Write “IF [named checkable assumptions] THEN [precise conclusion]” as a **candidate theorem**, distinguishing proved inputs from the conjectural arrow. Never assume the sought conclusion in its hypotheses.
4. **Translation audit:** If borrowed from topology, physics, biology, coding theory, etc., name the mathematical functor/invariant/algorithm that transports information. Analogies do not qualify as a bridge.
5. **Red team:** Produce a known lower-rank control or a formal countermodel that satisfies the *weaker* premises but violates the proposed conclusion. If it does, explicitly state the extra hypothesis needed; if no extra hypothesis can be given, kill/downgrade the proposal.
6. **First decisive experiment:** Choose the *smallest* computation, reading task or lemma whose failure would eliminate the idea. Prefer failure information over repetitive precision increases.
7. **Impact:** Record exactly what would be unlocked, and what would remain. Proving complex analytic rank four does not itself prove the BSD leading coefficient or finiteness of Sha.
8. **Decision:** Promote, pivot, park or kill with dated evidence. Record failed conjectures and counterexamples. Rebalance the high-risk portfolio rather than endlessly pursuing every track.
9. **Ownership of a proof:** A numerical value, AI consensus, and passing tests **cannot** promote a conjecture to a theorem. Require a fully justified mathematical argument and meaningful external review.

## Barbell allocation, not indiscriminate moonshots

For each iteration consider **one conservative next lemma**, **one credible high-upside bridge**, and **one wild but falsifiable alternative**. Choose one to act on with justification, while parking others. Maintain several tracks but cap concurrent high-cost computation; the fastest research program is not necessarily the one with the most generated code.

### Five-stage gate

| Gate | Acceptable evidence | Next action |
|---|---|---|
| G0: scope | Exact target, baseline and known nonimplication | Literature and definitions audit |
| G1: candidate | Falsifiable IF/THEN conjectural arrow and countermodel | Try to break it |
| G2: feasibility | A mathematically defined obstruction and a small control result | Independent implementation or proof of sublemma |
| G3: conditional lemma | Every assumption explicit, deductions checked, no circularity | Expert review and generalization |
| G4: externally reviewed | Independent mathematical review of the *actual bridge*, not code alone | Consider a manuscript, no novelty assertion before prior-art search |

A project can remain useful at G0/G1. **Do not automatically advance a gate because of CI.** The manifest enforces documentary honesty, not correctness of mathematics.

## Case study: the derived Kato trap

Burns–Kurihara–Sano (2024), [Conjecture 1.1](https://doi.org/10.2969/jmsj/90699069), defines the **derived norm** \(\mathcal N_{F/\mathbb Q}(z_F)\), an element of a cohomology group tensored with the group ring \(\mathbb Z_p[G]\). Its **order-of-vanishing** claim is membership in the *augmentation ideal* \(I^{r-1}\). In our algebraic-rank-four context that is \(I^3\).

**Crucial distinction:** \(\mathcal N(z_F)\in I^3\) does **not** assert \(L''(E,1)=0\). It is about a different object in a different coefficient ring. The accompanying conjectural *leading term* formula relates an augmentation quotient to a Bockstein regulator of \(\eta_{\rm BSD}\). No implication from the proven containment alone to the vanishing of the original **complex** second derivative has been established.

Moreover the cited [Theorem 1.3](https://doi.org/10.2969/jmsj/90699069) requires **all** of: p>3; finiteness of \(\Sha(E/F)[p^\infty]\); a specified large \(p\)-adic Galois image; and no local p-torsion at primes of S. None can be silently treated as automatic. F varies over finite *real* abelian fields, whereas the original anticyclotomic experiments used imaginary quadratic K.

**A valid leapfrog route must therefore produce an additional, proven bridge from the derived class and exact height/regulator data to a complex Taylor coefficient.** Testing augmentation filtrations on toy polynomials is a useful **logic negative control**, never a replacement for Euler-system computations. Full theorem audit: [KATO_BRIDGE_AUDIT.md](../strategy/KATO_BRIDGE_AUDIT.md).

## Template for a potential leapfrog conjecture

> Given E/Q, prime p and an explicitly defined cohomological regulator \(\mathcal R\), assume [named independently verifiable arithmetic hypotheses]. If a specified derived Euler-system class lies in the **kernel of a proven complex regulator comparison** \(\Phi\), then \(L''(E,1)=0\).

As written, this is **a research schema, not a mathematical conjecture**: the domain, construction and existence of \(\Phi\) are not yet specified, and it is possible such a map doesn't exist. A useful result would be a nontrivial well-defined comparison that does *not* bake the desired zero into its definition.

## Persistent artifacts

- The research agent contract [AGENTS.md](../../AGENTS.md) mandates LCP-1.
- [leapfrogs.json](../harness/leapfrogs.json) stores exact baseline, bridge, gain, falsifier, failure conditions and decision for each high-risk track.
- [validate_leapfrogs.py](../harness/validate_leapfrogs.py) rejects nonexistent experiment references and fabricated review status.
- [test_leapfrogs.py](../harness/test_leapfrogs.py) contains deliberately invalid data (negative controls).
- The main [experiment registry](../harness/experiments.json) remains the authoritative record of ordinary investigations.

**References:** Burns–Kurihara–Sano, *On derivatives of Kato's Euler system for elliptic curves*, Journal of the Mathematical Society of Japan 76 (2024) 855–919, §§1.2, 2–3 (Theorem 1.3, Conjecture 1.1). [Full article](https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_pdf/-char/en). This is a method guideline, not a proof of BSD.
