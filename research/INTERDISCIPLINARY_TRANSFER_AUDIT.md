# Transfer audit: which *other disciplines* can help our BSD work?

*2026-10-17 · Scope: E=234446.a1, K=Q(√−7), p=11. This is a research design and audit document, not a BSD theorem.*

We distinguish **mathematical transfer** (an actual theorem, algorithm, or validation method) from **analogy** (a useful mental model, incapable of proving a claim). A discipline earns attention only if we can specify the changed computation or proof obligation and a falsifiable test. Research status belongs in [CLAIMS.md](../CLAIMS.md).

## Decision matrix

| Domain | Transfer to our work | Concrete next experiment / artifact | Failure mode / exclusion | Priority |
|---|---|---|---|---|
| **Validated numerics / metrology** | Outward enclosures, uncertainty budgets, machine-checkable error estimates. Crucial for L'(E^−7,1). | Reproduce our historical 2000- and 6000-term rational derivative certificates as immutable scripts; check series identity, Euler–Maclaurin bounds, coefficients and tail, then implement an *independent* FLINT/Arb ball check. | A PARI decimal, repeated high precision or an uncited functional equation is not a proof. | **Immediate** |
| **Error-correcting codes / constraint solving** | A classical Selmer group is the kernel of localization maps into quotients by allowed local conditions. For a *finite computed presentation*, local constraints become a sparse matrix over F₁₁, with parity-check-style zero syndromes. | Specify H¹ global generators and all local Kummer maps for E/Q and E^−7/Q; only *then* build an exact row-reduction certificate. Currently run a small, explicit **local-log** syndrome negative control (not Selmer). | The local-log matrix is **not** a matrix for Selmer conditions; linear algebra cannot conjure missing cohomology. | **Immediate for organization; mathematically gated** |
| **Formal methods / programming-language theory** | Proof-carrying computations, minimal trusted checker, machine-readable theorem hypotheses; Lean formalization of elliptic formal groups. | Cite exact formal log/reduction lemmas in Michael Stoll's Lean elliptic-curve project; ask whether a bounded finite congruence can be formalized once certificate is mature. | “Two scripts pass” does not mean Lean-verified; avoid immense formalization with no leverage. | **High** |
| **Control theory / observability / identifiability** | Distinguishes a measured map from a latent pairing. A full-rank observation need not identify an unmeasured operator. | Construct an exact anti-equivariant rank-two pairing with a **different** rank-three radical than our rank-three two-place logarithm kernel; install as a nonimplication test. | Matching dimensions do not identify subspaces or pairings. | **Immediate and completed** |
| **Statistical experimental design / active learning** | Select experiments by whether they distinguish mathematical alternatives or eliminate a hypothesis. | Choose between: rigorous derivative positivity; actual 11-Selmer bound; global anticyclotomic height cross-pairing. Predeclare pass/fail and logical consequences for each. | Bayesian confidence or heuristic scores are not proofs. | **High** |
| **Homological algebra / topology / derived categories** | Not merely analogy: Selmer complexes, Poitou–Tate duality and Bockstein maps formally underlie derived height pairings. | Build a dependency diagram for the Macias Castillo–Sano/Nekovář/Bertolini–Darmon identification, enumerate local splittings and cohomological prerequisites. | A topological filtration in a toy model is not a derived p-adic height on E/K. | **High but requires expert math** |
| **Physics / representation theory & spectral heuristics** | Quadratic Galois conjugation yields exact ± eigenspaces and the odd-11 classical Selmer decomposition; random-matrix theory suggests statistical L-zero phenomena in *families*. | Pursue separate 11-Selmer ranks of E and E^−7 over Q; avoid treating statistics as proof about the fixed curve. | Physical Hamiltonian analogy or random-matrix patterns prove nothing for our concrete curve. | **Already deployed / secondary heuristics** |
| **Biology / causal inference & assay design** | Orthogonal assays; negative controls; distinguish mechanistic theory from observables. | Re-run PARI versus exact rational arithmetic; mutate inputs and confirm CI fails on genuine mathematical or interpreter errors. | A second library sharing the same theorem or hidden implementation is not completely independent; agreement is not causal proof. | **Immediate operational** |
| **Dependency graphs / software supply-chain engineering** | Explicit DAG of theorem assumptions and tests, version/commit locks, reversibility and impact analysis when an assumption fails. | Add machine-readable dependency fields and a correction rule for claims C-0001–0005; track that a false-positive GP test was fixed. | Green badges and more commits are not progress if core theorem remains unjustified. | **High** |
| **Neuroscience / analogy-driven intuition** | Possible creativity prompts for latent-variable hypotheses. | None until a specific mathematical transformation or falsifiable prediction exists. | Uncontrolled metaphor inflation; no direct proof mechanism. | **Park** |

## The useful exact mathematical relationship

A *classical* Selmer group is defined from global cohomology and local conditions:
```
Sel_L(K,M) = ker( H^1(K,M) -> product_v [ H^1(K_v,M)/L_v ] ).
```
This is **exact**, not an analogy with error-correcting codes. It implies a linear-algebra problem **only once** we have valid finite presentations of the global H¹ classes and all local quotient maps, plus a completeness argument. The fact that a local-log map also has a matrix of rank two **does not** make that matrix the localization map.

The related form of identifiability error is explicit in [the negative-control program](methodology/local_kernel_negative_controls.py): it constructs a symmetry-compatible rank-two **hypothetical** pairing whose rank-three radical differs from the local-log kernel. It rules out our prior inference from matching dimensions alone; it says nothing about the *actual* anticyclotomic height pairing.

## Next three decision experiments (and stopping rules)

**Experiment A — analytically rigorous twist nonvanishing.** Port the full historical 2000- and 6000-term programs without modifying their assertions; attach SHA-256 checksums and exact console output. Audit the L-series identity, complete Fourier coefficient recursion, all interval endpoints, and infinite-tail estimate. Commission a second FLINT/Arb-based program with a rigorously enclosing `L'(1)`. Pass only if it encloses a strictly positive interval and the coefficient/functional-equation hypotheses are confirmed independently. A numerical PARI value of 34.17 is a cross-check, not a pass.

**Experiment B — algebraically rigorous 11-Selmer bound.** Over Q separately, try to certify `dim Sel_11(E/Q)=4` and `dim Sel_11(E^−7/Q)=1`; the quadratic decomposition then gives a K-bound five. A failed finite search, 2-descent computation, or finite-digit local logarithm cannot establish such an upper bound. Stop rather than fake completeness if no algorithm with verifiable cohomological coverage is available.

**Experiment C — derived-height pairing.** Fix the anticyclotomic character, chosen prime over 11, local splittings, integral structure and Selmer complex. Compute a single cross-height with a certified p-adic error bound and a different implementation. Only then discuss the radical, nondegeneracy, or augmentation-order equality. Keep the two-prime local-log kernel separate.

## References supporting transfers

- Warwick Tucker, *Validated Numerics: A Short Introduction to Rigorous Computations* (Princeton, 2011): https://press.princeton.edu/books/hardcover/9780691149677/validated-numerics
- FLINT/Arb **ball enclosure semantics** (Arb merged into FLINT in 2023): https://flintlib.org/doc/using.html
- Brian Conrad's Galois cohomology/Selmer local condition lecture notes: https://math.stanford.edu/~conrad/modseminar/pdf/L07.pdf
- Michael Stoll, Lean 4 elliptic-curve formalization (formal groups, Mordell–Weil, 2-Selmer): https://github.com/MichaelStollBayreuth/EllipticCurves
- Daniel Macias Castillo and Takamichi Sano, *On Selmer complexes, Stark systems and derived p-adic heights* (2026 **preprint**, https://arxiv.org/abs/2603.23978). Formal identification claims must be read with their hypotheses.
- Experimental design for model discrimination: https://pmc.ncbi.nlm.nih.gov/articles/PMC8924111/
- Agboola–Castella, anticyclotomic p-adic BSD paper (2021): https://www.numdam.org/articles/10.5802/jtnb.1174/

## Research integrity and limitations

The first eight “applications” above vary greatly in evidentiary force. The quadratic Selmer splitting and Selmer-localization kernel are mathematics; physics and coding-theory vocabulary is a guide to *organizing* those facts, not a source of new proofs. Two AI-authored scripts are not independent human peer review. We will not contact outside maintainers without a minimal reproducible result, a precise question, and a scope-accurate status label.
