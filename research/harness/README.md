# Machine-checkable research harness

The repository's **permanent research operating procedure** is in [AGENTS.md](../../AGENTS.md). Read it with [RESEARCH_STANDARDS.md](../../RESEARCH_STANDARDS.md) and the [cross-disciplinary audit](../INTERDISCIPLINARY_TRANSFER_AUDIT.md).

`experiments.json` is a small, version-controlled experiment registry: each record states an exact falsifiable question, immutable claim IDs, proof dependencies, a negative control, nonclaims, and the particular mathematical or experimental technique borrowed from another field. It is **not** an automated proof checker. Human/AI review status is kept separate from code validity.

Run from the repository root:

```bash
python3 -I -B research/harness/validate.py
python3 -I -B research/harness/test_validate.py
python3 -I -B research/methodology/local_kernel_negative_controls.py
python3 -I -B research/anticyclotomic_11/independent_rational_derivative.py
```

CI additionally performs **independent PARI-GP arithmetic** and compares the first 2,000 Fourier coefficients of the original curve with the 2,000 coefficients independently derived by our rational certificate. This closes a particularly important shared-input weakness (but not the mathematical analytic identity, conductor, character, or tail theorem).

Before new research:
1. Add an experiment entry with a precise question and explicit stopping rule. Link to the claim ledger and published references.
2. Name a *genuine mathematical transfer* (e.g. Galois representation splitting, Selmer complexes) or a *validation method* (e.g. exact ball arithmetic, negative controls). Mark metaphor-only ideas as **analogy**, never proof.
3. Record what would falsify the hypothesis, not merely what would confirm it.
4. Put executable programs, exact sources, frozen data and references under version control. Test every stated prediction including a deliberately bad input.
5. Promote a claim only after verifying theorem assumptions and independently reviewing the mathematics; CI alone is never sufficient.

## Leapfrog conjecture overlay

Every **EX-004 and later** high-risk experiment must have an entry in [leapfrogs.json](leapfrogs.json), with an auditable missing theorem, IF/THEN candidate, gain, countermodel, decision and kill criterion. Our [LCP-1 protocol](../strategy/LEAPFROG_PROTOCOL.md) requires alternating a conservative lemma, a credible leapfrog and a wild but falsifiable hypothesis; review the known result's mathematical **output type** before inferring an L-value.

```bash
python3 -I -B research/harness/validate_leapfrogs.py
python3 -I -B research/harness/test_leapfrogs.py
python3 -I -B research/strategy/logic_gate_tests.py
```

This is an organizational quality gate, **not** formal verification of any conjecture. The initial six records are all speculative; nothing here has external expert review.

## Session 12 local/global alignment falsifier

The [primitive 11-adic projective height gate](../split11/LOCAL_GLOBAL_ALIGNMENT_AUDIT.md) refines the H2/L11 speculation. The existing local logarithm coefficient vector projects to **[1:0:2:9] mod 11**; a genuinely global anticyclotomic cross-height vector would have to agree after removing common powers of 11 for the proposed hyperplanes to coincide. This is a necessary criterion, not an actual height calculation; all-zero finite observations are indeterminate. Run the deliberately masked false-positive and independent all-column Jacobian checks:

```bash
python3 -I -B research/methodology/height_alignment_scale_gate.py
python3 -I -B research/split11/independent_jacobian_all_columns.py
```

CI now enforces both checks. The formal toy heights do not belong to the curve's actual global p-adic height pairing. No claim toward complex L'' has been promoted.

## Periodic whole-problem checkpoint

[WPR-1](../strategy/FULL_PROBLEM_REVIEW.md) is mandatory at the beginning of each research sprint, at least weekly, after three substantive merges, and before major mathematical announcements. A dated [whole-problem review](../reviews/2026-10-17-whole-problem.md) and its [machine-readable current snapshot](../reviews/current.json) capture general BSD, the original complex analytic-rank obstacle, all six competing leapfrog tracks, falsifiers and reprioritizations. Crucially the review must answer whether anything previously unproved **about the actual BSD conjecture** became proved. No is an allowed and common answer.

```bash
python3 -I -B research/harness/validate_full_review.py
python3 -I -B research/harness/test_full_review.py
```

The validator enforces completeness, review chronology and explicit nonclaims, but neither proves mathematical progress nor guarantees that future scheduled reviews will run. The operating cadence is a **separate human/agent obligation**.

## Security / completeness boundaries

The manifest validator only checks syntax, references, and basic evidence-policy invariants. It does **not** evaluate or execute commands from `experiments.json`. Commands in untrusted PRs must never be interpolated into shell steps. The test runner invokes a fixed list of pinned Python/GP programs.

It cannot certify local Kummer compatibility, analytic continuation, Satake/Euler-factor identities, Selmer upper bounds, a global height pairing, or BSD. External review must be real and attributed. A checked box in this JSON file proves nothing mathematically.
