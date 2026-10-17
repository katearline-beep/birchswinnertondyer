# Contributing to the BSD research notebook

Thank you for helping test the mathematics. **Trying to break an argument is a valuable contribution.**

Read [RESEARCH_STANDARDS.md](RESEARCH_STANDARDS.md) before posting a mathematical claim. Use the issue templates for reproduction, peer-review requests, and corrections; make substantive edits through a focused branch and PR.

## Minimum contribution checklist

- Give an exact statement, precise model and field, quantifiers, normalizations, and a stable claim ID.
- State whether the item is a conjecture, numerical evidence, a computational certificate, a conditional theorem, or a theorem; record review **separately**.
- Cite existing work precisely (authors, year, theorem or section; stable link), including any prior-art search.
- Identify proof obligations not discharged by the source code. Identify conditions on reductions, ranks, Sha, L-functions, and all intermediate theorems.
- Supply reproducible commands, pinned dependencies, deterministic input/seed, expected output, and committed data. Use exact arithmetic where possible; otherwise rigorous interval and tail bounds for proof claims.
- Prefer a *different* verification algorithm to a rewrite of the same code. Include negative cases or adversarial tests.
- Disclose AI use, distinct roles, and human mathematical reviewers accurately. AI consensus is not peer review.
- Label unreviewed output accordingly; do not promote a result to “formally verified” without a checked proof in Lean/another named assistant.
- Record limitations, failed attempts, and corrections with links to dependent claims.
- Do not merge a new BSD theorem claim solely because CI is green.

## Review norms

Reviewers should check the statement and its dependencies *before* inspecting the outputs; trace mathematical assumptions and implementation exceptions; reproduce in a clean environment; and distinguish a script that runs from an argument that is valid. Seek an independent expert on any claimed novel theorem.

## Corrections

Open a [correction issue](.github/ISSUE_TEMPLATE/correction.md) including a minimal counterexample or failing step. Do not silently rewrite historical claims: state the old and corrected versions, impact, and commit references. Retractions are acceptable.

## Licensing

No open-source license has been selected. Contributions do not implicitly grant others rights to republish; a suitable license and contributor terms require a maintainer decision before substantial outside contributions.
