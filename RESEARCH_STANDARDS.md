# Research integrity protocol (v1, 2026-10-17)

This is a computational research notebook, **not a claimed proof of BSD**. Speed, agent consensus, attractive plots, and passing tests do not establish mathematical truth. All results are open to corrections and withdrawal.

## Claim types (record separately from review state)

- **CONJECTURE:** a precise unproved statement, even if widely believed.
- **NUMERICAL EVIDENCE:** approximate computation without a fully justified enclosure.
- **COMPUTATIONAL CERTIFICATE:** finite exact arithmetic or rigorously bounded computation, together with stated assumptions, a proof that the computation implies the claim, and inspectable code/data. Successful tests alone are not enough.
- **CONDITIONAL THEOREM:** a complete derivation with all unproved hypotheses explicit.
- **THEOREM (ESTABLISHED):** a valid deductive proof from established results. Cite the actual theorem and check its hypotheses; computing examples is not a substitute.
- **FORMALLY VERIFIED:** a checked proof in a named proof assistant and pinned toolchain, with the checked source available. Do not use this status for Python assertions.

Each claim also has a **review state**: draft; internally reproduced; independently implemented (without separate human review); subject-matter expert reviewed; peer reviewed/corrected; withdrawn. These dimensions are independent. Two AI-written implementations are useful *cross-checks*, not independent human peer review.

## Required record for every substantive claim

1. Stable claim ID and one-sentence precise statement with quantifiers and objects defined.
2. Type and review state; date, contributor roles, disclosure of AI assistance.
3. Exact curve/model, field, primes, normalizations, sign conventions, and definitions.
4. Dependencies: numbered lemmas and precise literature citations (author, title, year, theorem/page, DOI or stable URL); which hypotheses were checked and how.
5. Proof sketch and *proof obligations* distinguishing mathematical deductions from script outputs.
6. Reproduction: script paths, runtime and version, commands, exact input data, expected output, deterministic seed when used, and commit SHA. Record memory/CPU/time if relevant.
7. Error model: exact arithmetic vs. floating point; validated intervals, truncation/tail bounds, numerical precision, and coverage of exceptional cases. A decimal close to zero never certifies zero.
8. Independent validation plan: alternative algorithms, cross-checks with Sage/Pari/LMFDB or expert sources, property tests, and adversarial attempts.
9. Known limitations and explicit nonclaims, prior-art search, next falsifiable question.
10. Correction history: keep prior statements visible and link each change to its issue/PR. Never silently change status.

## Acceptance rules

- Treat all new results as *provisional* until proof obligations and reproducibility are documented.
- Never merge an alleged new BSD theorem based only on AI consensus or passing CI; require expert examination of all analytic and arithmetic dependencies.
- CI must verify the actual published certificate, including a second algorithm when feasible; not just parse files or compare a stored result to itself.
- All derivations involving analytic continuation, Selmer corank, height normalization, BSD leading coefficients, twists, periods or regulators get a dedicated assumptions audit.
- No public claim of novelty until a documented literature search; no claim of Lean verification without checked Lean source and pinned versions.
- Results can be corrected, downgraded, or withdrawn; record the reason and impact on dependent claims.
- Contributions by humans and agents must be attributed accurately. Never represent an AI-generated report as independent expert review.
- Large numerical searches need reproducible parameters, raw result provenance, completeness argument, and clear separation from a proof.
- Respect source licenses and copyright. No automatic open-source license is implied by publishing a GitHub repository.

## Workflow

Open issue → investigate on a branch → add/update claim record → deterministic certificate + independent check → critical PR review → merge only after CI → update ledger and downstream dependencies. Research logs preserve failures and rejected approaches.

## Methodological references

- Mathlib4 contribution guidance: https://leanprover-community.github.io/contribute/how-to-contribute.html
- GitHub Actions secure use: https://docs.github.com/en/actions/reference/security/secure-use
- Lean/mathlib formal mathematics: https://lean-lang.org/use-cases/mathlib/
- J. H. Silverman, *The Arithmetic of Elliptic Curves*, second edition, Springer, 2009 (for formal groups and heights).

This is a project policy, not a substitute for mathematical peer review.
