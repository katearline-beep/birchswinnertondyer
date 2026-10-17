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

## Security / completeness boundaries

The manifest validator only checks syntax, references, and basic evidence-policy invariants. It does **not** evaluate or execute commands from `experiments.json`. Commands in untrusted PRs must never be interpolated into shell steps. The test runner invokes a fixed list of pinned Python/GP programs.

It cannot certify local Kummer compatibility, analytic continuation, Satake/Euler-factor identities, Selmer upper bounds, a global height pairing, or BSD. External review must be real and attributed. A checked box in this JSON file proves nothing mathematically.
