# Session 12 software applicability audit: genuinely global anticyclotomic 11-adic heights

**2026-10-19. Feasibility/literature audit only; no global heights computed and no mathematical peer review.**

## Exact target

Construct and independently validate the four values `a_i=h_11^ac(P_i,R)` for the specific elliptic curve E=234446.a1, K=Q(sqrt(-7)), with the two primes above p=11, one fixed anticyclotomic idele-class character and a specified Hodge/logarithm splitting. We already know the *local elliptic logarithms* of P_i and R; those are **not** the global anticyclotomic heights. See [primitive comparison gate](../split11/LOCAL_GLOBAL_ALIGNMENT_AUDIT.md). Our speculative L11 test needs genuine global height values with meaningful 11-adic precision, not more local-log digits.

## Candidate algorithms and source-level gates

1. **Besser–Müller–Srinivasan**, *p-adic adelic metrics and Quadratic Chabauty I*, https://arxiv.org/abs/2112.03873, develops canonical p-adic heights on abelian varieties over number fields. It provides theoretical infrastructure; its abstract alone is not executable code for our specific anticyclotomic character.
2. **Balakrishnan–Besser**, *Coleman–Gross height pairings and the p-adic sigma function*, https://arxiv.org/abs/1201.6016, relates elliptic Coleman–Gross and Mazur–Tate constructions. Before using a computation, audit the auxiliary choices and the local contributions at all places.
3. **QCMod-NF**, https://github.com/AashrayaJha/QCMod-NF, contains Magma `heights.m` code for Nekovář heights and wrappers for completions of imaginary quadratic fields. **Important non-applicability caveat:** its documented *quadratic Chabauty driver* assumes a genus > 1 curve and rank = 2g, with sufficient rational points and a suitable Hecke correspondence. Our genus-one E over K has rank five: the driver and its correctness guarantees **do not directly apply**. A source audit may still find reusable local heights, Galois embeddings or p-adic integration components. Do not call its routines on our curve without verifying their hypotheses independently.
4. **Kaya–Bianchi–Müller hyperelliptic height examples**, https://github.com/KayaEnis/padicHeights, and **Gajović local heights**, https://github.com/StevanGajovic/heights_above_p, provide Sage/Magma local Coleman–Gross implementations. The latter explicitly advertises *local cyclotomic* heights over Q_p; a local cyclotomic value is not an anticyclotomic *global* value over K.
5. **Sage documented elliptic height routines**, https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html, compute cyclotomic p-adic heights for E/Q. They are useful control implementations but cannot be silently relabeled as `h_ac(P_i,R)`.

## Implementation decision gate (no computation yet)

**G0 — exact definition.** State the norm-compatible anticyclotomic character on ideles of K, its values at the two primes above 11, the formal logarithm convention and the canonical/ordinary Hodge splitting. Verify conjugation anti-equivariance as a testable identity.

**G1 — all local terms.** Inventory every finite place whose Coleman–Gross or Nekovář local contribution could be nonzero (especially primes over 2, 7, 11, 117223 and divisors of point coordinates). Prove which non-p contributions vanish; do not assume only primes over 11 matter.

**G2 — source portability.** Inspect `QCMod-NF/heights.m` (and dependencies) to separate general local/global height infrastructure from genus>1 / rank=2g / Hecke correspondence assumptions. Prefer a minimal independent example over an imaginary quadratic field with known height behavior before tackling E/K.

**G3 — independent check.** Compute at least two cross-pairings by independent algorithms or a published, independently verified formula; check bilinearity, conjugation sign, dependence on the character scaling, and precision losses. Record primitive mod-11 projective data *only after* all local terms and normalizations are checked.

**G4 — falsify L11.** After primitive normalization, compare the measured height functional to [1:0:2:9] modulo 11, then higher-precision wedge tests. A mismatch kills local/global kernel alignment; a finite match does **not** establish equality.

## Decision

**Potentially actionable software route, not yet executable:** audit the number-field/local-height components of QCMod-NF and the cited elliptic formulas. Do not treat a genus>1 quadratic Chabauty workflow, an E/Q cyclotomic height, or a Q_p local-height routine as a validated solver for our higher-rank E/K anticyclotomic pairing. No complex L'' comparison follows even if this experiment succeeds.

**What new BSD implication was proved:** none. **What uncertainty was reduced:** identified code and exact adaptation/hypothesis gates for the previously unimplemented global-height experiment.
