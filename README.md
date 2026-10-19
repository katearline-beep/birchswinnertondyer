# Birch–Swinnerton-Dyer — open arithmetic research notebook

**Status:** exploratory mathematics and independently checkable computations. **No proof of the BSD conjecture, no claim of novel mathematical results, and no independent expert review yet.**

We investigate specific elliptic curves and the boundary between numerical evidence, exact computation, conditional mathematical implications, and proof. All reasoning and code remain open to correction. This project includes AI-assisted contributions, explicitly attributed as such.

**New global-class candidate (Session22):** [Howard big-Heegner entry audit on original rank4 curve](research/proof_labs/SESSION22_HOWARD_HEEGNER_ENTRY_AUDIT.md), with two-split-Frobenius absolute residual irreducibility certificate. Published class family exists under checked starting hypotheses; specialization to CH4.5 and complex BSD bridge remain open.

## Start here

**Session21 verified theorem scope:** [Castella–Hsieh 433a1 rank-two control and original-rank4 Theorem4.1 applicability](research/proof_labs/SESSION21_CH_433A1_THEOREM_MAP.md) is now part of the source-checked proof lab. The derived-height filtration on focal E/p11/K=-7 exists **by published theorem**, but TheoremA/B nonzero-Kato criterion does not apply there, and the needed global Iwasawa class/complex L'' comparison are missing.

**Research direction as of 19 October 2026:** [theorem-first pivot](research/strategy/THEOREM_FIRST_PIVOT_2026-10-19.md), with [rank-two Castella–Hsieh theorem lab](research/proof_labs/RANK_TWO_KATO_THEOREM_SCOPE.md) and [Ulmer proved high-rank function-field BSD lab](research/proof_labs/ULMER_FUNCTION_FIELD_BSD_LAB.md). We retain our rank-four elliptic curve as a stress test, not our sole discovery mechanism. Stage-one tasks: [#41](https://github.com/katearline-beep/birchswinnertondyer/issues/41) and [#42](https://github.com/katearline-beep/birchswinnertondyer/issues/42).


- [AGENTS.md](AGENTS.md): standing research instructions for human and AI collaborators, including an explicit cross-disciplinary transfer gate and falsifiable experiment design.
- [Machine-checked research harness](research/harness/README.md): executable experiment registry, review-status enforcement, negative controls, and independent Fourier coefficient checks.

- [Research integrity standards](RESEARCH_STANDARDS.md): statuses, proof obligations, provenance, correction policy, and review workflow.
- [Claim ledger](CLAIMS.md): precise claims, evidence, limitations, and outstanding review.
- [Contribution guidelines](CONTRIBUTING.md): how to provide an independent check or report an error.
- [Split-11 example](research/split11/NOTE.md) and [reproduction protocol](research/split11/REPRODUCIBILITY.md).

### Representative computations and their proof boundaries

For the curve `y²=x³−1267x+17230` over `Q(√−7)`, two AI-authored but algorithmically distinct exact-arithmetic Python programs produce a normalized local 11-adic logarithm minor equal to **85 modulo 121** (a unit modulo 11). See claim C-0001. This historical local-log calculation is **not** a global anticyclotomic height or a BSD advance. Later [C-0011 through C-0013](CLAIMS.md) compute **provisional** global anticyclotomic heights (three 11-adic digits) using BCLMN and Mazur–Tate. Their canonical sigma input has an independent PARI check, but the **complete global height pipeline has not independently been reviewed** and none of the calculations proves the original **complex** L''(E,1)=0.

Reproduce without third-party packages:

```bash
python3 -I -B research/split11/verify.py
python3 -I -B research/split11/independent_check.py
```

GitHub Actions runs both on Python 3.11, 3.12, and 3.13, with immutable pinned actions.

## High-risk leapfrog portfolio

[Leapfrog conjecture protocol](research/strategy/LEAPFROG_PROTOCOL.md) and [H1 derived-Kato gap audit](research/strategy/KATO_BRIDGE_AUDIT.md) are now part of the standing [AI-agent contract](AGENTS.md). The accompanying [leapfrog research registry](research/harness/leapfrogs.json) keeps eight tracked moonshot directions falsifiable, explicit about missing mathematical bridges and willing to be killed. These are **speculative ideas**, not newly established theorems.

## Periodic whole-problem reorientation

We deliberately [reassess the **entire** Birch–Swinnerton-Dyer conjecture](research/strategy/FULL_PROBLEM_REVIEW.md) at every research-sprint start, at least weekly, and after major results or three mathematical merges. The [current machine-checked whole-problem review](research/reviews/current.json) distinguishes the general conjecture, this curve's unresolved **complex** L''(E,1), exact analytic-rank-four requirements, and the still-open Sha/leading-coefficient formula.

The review must answer what *new mathematical implication* toward BSD was actually **proved**; “none” is a valid and often essential result. The [machine-readable research snapshot](research/reviews/current.json) is checked in CI with negative controls. **This is research accountability, not an automatic theorem verifier.**

## Working method

One narrowly scoped claim per issue/PR; define mathematical objects and dependencies; attempt to falsify; use exact arithmetic or certified error bounds; compare an independent algorithm; document the limits. Do not move a result to “proved” just because CI is green. We welcome corrections more than publicity.

## Attribution, permissions, and reuse

Research emerged from human–AI exploration in October 2026. The code and documents in this repository are not yet accompanied by an explicit reuse license: public visibility alone is **not** permission to reuse or redistribute. Selecting a license is an open maintainer decision. Please provide attribution for both human and AI contributions when describing this work.

**Ulmer proof-lab correction (Session20):** [source-audited Fermat map and global Frobenius rank computation](research/proof_labs/SESSION20_FERMAT_ORBITS_AUDIT.md) distinguishes ranks 2,3,7 over the prime constant fields from geometric ranks 3,7,25. Earlier prime-field labels were wrong and have been corrected. The original complex L'' remains open.
