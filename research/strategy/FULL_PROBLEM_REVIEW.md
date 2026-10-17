# Whole-problem BSD review protocol (WPR-1)

**Mandatory for human and AI research collaborators.** A full-problem review is *not* an encouraging retrospective, a substitute for proof, or another narrow literature audit. Its purpose is to detect research drift, wasted effort, and unsupported promotions of evidence.

## The full mathematical problem

For every elliptic curve \(E/\mathbb Q\), BSD predicts

1. \(\operatorname{ord}_{s=1}L(E,s)=\operatorname{rank}E(\mathbb Q)\) (**rank equality**).
2. The appropriately normalized leading coefficient is described by the regulator, real period, Tamagawa numbers, torsion factors and the order of the Tate–Shafarevich group when finite (**leading-term formula**).

The second item is not settled by proving rank equality; our work does not prove either general statement.

For **our test curve** \(E:y^2+xy=x^3-x^2-79x+289\), conductor \(234446\), known algebraic rank four and root number +1, the missing analytic-rank-at-least-four condition is **\(L''(E,1)=0\)**. Given this, parity of the *completed* L-function also forces the third derivative to vanish, while exact order four additionally needs \(L^{(4)}(E,1)\ne0\). These are statements about the original **complex** L-function. Vanishing of a derived Kato class in an \(11\)-adic group ring, a BDP anticyclotomic \(p\)-adic L-function, or a quadratic-twist derivative concerns **different objects**.

**Never use a positive twist derivative, finite local logarithm matrix, or tiny approximate complex derivative as a proof of the original complex equality.** A properly reviewed exact twist nonvanishing result is nevertheless valid subsidiary mathematics.

## When the review is compulsory

- At the **start of every autonomous research sprint** and before selecting an expensive experiment.
- **At least weekly** while the project is active.
- After **three substantive research merges**, after a significant rejected leapfrog, or after a numerical contradiction, even if less than a week has passed.
- Immediately before announcing a theorem, seeking outside mathematical endorsement or submitting a manuscript.

A review creates a **dated immutable snapshot** under \(research/reviews/\), updates \(current.json\), and records a next review due date. Subsequent reviewers must not overwrite historical snapshots. Source pointers and the list of merged PRs/issues examined are required; a green CI badge alone is not source evidence.

GitHub Actions enforces completeness and contradictions in review metadata, **not** that a review occurred on schedule, that a theorem is true, or that issues were actually examined. The recurring ChatGPT research review is an additional operating mechanism; a paused task or absent collaborator cannot guarantee an on-time review. If overdue, mark it overdue and prioritize it before new large work.

## Required full-problem scan

1. **Reconstruct the original target:** distinguish general BSD, this particular analytic-rank-four example, exact-order-four condition and leading coefficient.
2. **Rebuild a typed dependency graph:** mathematical objects → available published theorems → checked hypotheses → missing logical arrows → actual BSD implications. Ask specifically whether *any* newly proved arrow reaches the original \(L''(E,1)\).
3. **Review all claims:** numerical evidence vs exact conditional computation vs theorem vs peer-reviewed result, including negative results and corrections. Separate **research output** from **progress toward the theorem**.
4. **Adversarially compare competing routes** H1–H6, currently H1 derived Kato, H2 mixed heights, H3 quadratic-field geometry, H4 Mazur–Tate, H5 diagnostics, H6 period geometry. For each: last measurable gain, most important missing arrow, what would kill it, and next cheapest falsifier. Pausing/killing a weak track is a valid outcome.
5. **Run at least one stress test:** consider a rank-two control, a different completion, a mismatched L-function, an unverified Sha hypothesis, an ordinary-versus-supersingular mismatch, or a finite-layer false positive. Select one relevant to the proposed next bet.
6. **Set an allocation decision:** name one safe lemma, one credible leapfrog and one wild alternative. Choose one practical next task; explicitly explain what work is being *deprioritized*.
7. **Publish two summaries:** a concise honest human summary of actual progress and a structured machine-checkable record. Never promote a claim's mathematical status automatically from this review.

## Evidence-to-progress standard

| Evidence | Reproducible output | What it does **not** buy |
|---|---|---|
| Local 11-adic logs (C-0001/2) | Exact finite local congruences | Neither global derived heights nor complex analytic rank |
| Anticyclotomic theorem applicability (C-0003) | Conditional implication given finite Sha | No unconditional Sha finiteness, no equality of orders, no complex L'' |
| Quadratic Selmer splitting (C-0004) | Standard exact decomposition | No 11-Selmer dimension bound from code alone |
| Twist derivative (C-0005/6) | Independent numerical and provisional bounded positive series | Does not settle original E's analytic rank |
| Galois/local and cyclotomic ring audits (C-0007/8) | Exact input and failure-mode checks | No derived Kato cohomology class, no complex reciprocity |
| H5 numerical L''~0, fourth derivative stable | Numerical heuristic on specific E | No rigorous exact zero, no general BSD proof |

**Decision test:** When a sprint ends, answer in ordinary language: *“What exact theorem, proof obligation, or rigorously justified implication toward BSD became established that was not established at the previous review?”* If none, say **none**. Infrastructure, reproductions and dead-end eliminations may still be useful, but should not be passed off as mathematical breakthroughs.

## Review document and machine gate

The permanent journal is \(research/reviews/\). A review's snapshot uses:

- \(review_id\), ISO date, reviewer type (human, AI, joint); no false independent human review.
- Explicit general-BSD and curve-specific goals, status of the original complex L'' equality and leading coefficient.
- At least one line for **each of H1–H6**, including last evidence, missing bridge, decision and next falsifier.
- A categorized ledger of **what changed since the previous review** and **what was not established**.
- One near-term selected test, one safe lemma, one moonshot, one wild possibility, and a dated next checkpoint.
- At least one documented reason for **not** pursuing another track.
- Review sources (files, issues, literature) and affected claim IDs.

\(research/harness/validate_full_review.py\) verifies field structure, chronological order, coverage, references and fail-closed status constraints. It cannot independently assess mathematical validity.

See [first snapshot](../reviews/2026-10-17-whole-problem.md) and [machine-readable current review](../reviews/current.json).

## Research selection consequence of the first audit

The live obstacle is **not** numerical precision, the choice of one more cyclotomic field, or a new group-ring divisibility calculation. It is a missing **noncircular** relation from known rank-four arithmetic to the exact *complex* central second derivative. Allocate work to (1) an *external mathematical review* of the independently bounded twist derivative (the nearest checkable subsidiary certificate), and (2) a **literature-level go/no-go test** for a genuinely higher Gross–Zagier identity over quadratic fields, while limiting expensive H1 computations until the missing complex comparison is specified. Do not claim that any geometric third-derivative theorem already exists.

This is a research allocation choice—not a theorem about BSD.
