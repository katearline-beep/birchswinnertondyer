# Birch–Swinnerton-Dyer — open arithmetic research notebook

**Status:** exploratory mathematics and independently checkable computations. **No proof of the BSD conjecture, no claim of novel mathematical results, and no independent expert review yet.**

We investigate specific elliptic curves and the boundary between numerical evidence, exact computation, conditional mathematical implications, and proof. All reasoning and code remain open to correction. This project includes AI-assisted contributions, explicitly attributed as such.

## Start here

- [AGENTS.md](AGENTS.md): standing research instructions for human and AI collaborators, including an explicit cross-disciplinary transfer gate and falsifiable experiment design.
- [Machine-checked research harness](research/harness/README.md): executable experiment registry, review-status enforcement, negative controls, and independent Fourier coefficient checks.

- [Research integrity standards](RESEARCH_STANDARDS.md): statuses, proof obligations, provenance, correction policy, and review workflow.
- [Claim ledger](CLAIMS.md): precise claims, evidence, limitations, and outstanding review.
- [Contribution guidelines](CONTRIBUTING.md): how to provide an independent check or report an error.
- [Split-11 example](research/split11/NOTE.md) and [reproduction protocol](research/split11/REPRODUCIBILITY.md).

### Current scoped computational result

For the curve `y²=x³−1267x+17230` over `Q(√−7)`, two AI-authored but algorithmically distinct exact-arithmetic Python programs produce a normalized local 11-adic logarithm minor equal to **85 modulo 121** (a unit modulo 11). See claim C-0001. This is **not** an independently peer-reviewed proof, a computation of anticyclotomic heights, or a BSD advance.

Reproduce without third-party packages:

```bash
python3 -I -B research/split11/verify.py
python3 -I -B research/split11/independent_check.py
```

GitHub Actions runs both on Python 3.11, 3.12, and 3.13, with immutable pinned actions.

## High-risk leapfrog portfolio

[Leapfrog conjecture protocol](research/strategy/LEAPFROG_PROTOCOL.md) and [H1 derived-Kato gap audit](research/strategy/KATO_BRIDGE_AUDIT.md) are now part of the standing [AI-agent contract](AGENTS.md). The accompanying [leapfrog research registry](research/harness/leapfrogs.json) keeps six moonshot directions falsifiable, explicit about missing mathematical bridges and willing to be killed. These are **speculative ideas**, not newly established theorems.

## Periodic whole-problem reorientation

We deliberately [reassess the **entire** Birch–Swinnerton-Dyer conjecture](research/strategy/FULL_PROBLEM_REVIEW.md) at every research-sprint start, at least weekly, and after major results or three mathematical merges. The [current six-track checkpoint](research/reviews/2026-10-17-whole-problem.md) distinguishes the general conjecture, this curve's unresolved **complex** L''(E,1), exact analytic-rank-four requirements, and the still-open Sha/leading-coefficient formula.

The review must answer what *new mathematical implication* toward BSD was actually **proved**; “none” is a valid and often essential result. The [machine-readable research snapshot](research/reviews/current.json) is checked in CI with negative controls. **This is research accountability, not an automatic theorem verifier.**

## Working method

One narrowly scoped claim per issue/PR; define mathematical objects and dependencies; attempt to falsify; use exact arithmetic or certified error bounds; compare an independent algorithm; document the limits. Do not move a result to “proved” just because CI is green. We welcome corrections more than publicity.

## Attribution, permissions, and reuse

Research emerged from human–AI exploration in October 2026. The code and documents in this repository are not yet accompanied by an explicit reuse license: public visibility alone is **not** permission to reuse or redistribute. Selecting a license is an open maintainer decision. Please provide attribution for both human and AI contributions when describing this work.
