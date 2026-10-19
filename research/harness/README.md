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

## Session 13 — an executable global-height entry point, not a result yet

Our [published-height adaptation audit](../anticyclotomic_11/SHADOW_LINES_HEIGHT_IMPLEMENTATION.md) identifies a genuine elliptic anticyclotomic height formula (BCLMN 2016, Algorithm 4.2) and a practical polarization identity `h_ac(P_i+R)=2h_ac(P_i,R)` for the symmetric height. The [character coefficient calculator](../anticyclotomic_11/character_coefficients.py) computes six unramified split-prime values (C-0010) with a separate first-digit Fermat quotient; [point prerequisites](../anticyclotomic_11/point_prerequisites.py) verify minimal-model coordinates and possible denominator primes. These are **not** global heights. The rank-two *shadow line theorem* of BCLMN does not apply directly to our rank-four E.

```bash
python3 -I -B research/anticyclotomic_11/character_coefficients.py
python3 -I -B research/anticyclotomic_11/point_prerequisites.py
```

The next implementation must supply 11-adic sigma series **and** exact denominator ideals of [36](P_i+R), including all split bad primes, before making any height or kernel-alignment claim. The [2026-10-19 whole-problem supplement](../reviews/2026-10-19-whole-problem.md) preserves the original complex L'' obstruction.

## Session 14 — provisional global height digits and a necessary change of strategy

An [exact-arithmetic implementation](../anticyclotomic_11/provisional_height_mod11.py) of BCLMN Proposition 2.4 now gives *provisional* anticyclotomic self-height residues `(1,2,7,8)` mod 11. The [audit](../anticyclotomic_11/SESSION14_HEIGHT_MOD11_AUDIT.md) proves denominator ideals for `A_i` and `2A_i` by Euclidean gcd, computes immense `[36]A_i` denominator generators via integral division polynomials, checks equality by distinct `2A_i*18` and `4A_i*9` routes, and checks height homogeneity at `[72]A_i`. The naive denominator recurrence from the unadjusted `A_i` fails at bad prime 2 for three points. The primitive height vector disagrees with local-log `[1:0:2:9]`, **conditionally falsifying speculative L11 kernel alignment**.

This is AI-authored and **not yet independently reproduced with a second p-adic height library or peer reviewed**. Do not promote it to a certified global-height computation without Sage/Magma/PARI sigma and denominator audit; certainly do not infer original complex L'' vanishing. H2's genuine derived-height/complex comparison problem is still open.

```bash
python3 -I -B research/anticyclotomic_11/provisional_height_mod11.py
```

### Published BCLMN example as an adversarial control

An additional exact-affine regression reproduces the BCLMN Section 5.1 first digit `h_ρ(P1+S)=3 mod 5` on 389a1 over `Q(sqrt(-11))`, using the paper's printed denominator generator and a different group-law implementation. Unlike the previous 36/72 homogeneity test, this is an independently published numerical target. It checks the elementary first sigma coefficient and prime orientation, **not** the entire sigma series or our rank-four denominator ideals. Run:

```bash
python3 -I -B research/anticyclotomic_11/published_389a1_height_control.py
```

**Second published control and first radical:** The published BCLMN 389a1 example now yields both first height digits 3 mod5, with the second divisor computed and checked using an independent Euclidean ideal gcd. The [conditional first-height radical](../anticyclotomic_11/FIRST_HEIGHT_RADICAL_MOD11.md) shows that, if C-0011 is confirmed, the global first pairing has exact rank two with mod-11 radical `P2−2P1, P3−7P1, P4−8P1`, distinct from the old local-log kernel. Verify with `python3 -I -B research/anticyclotomic_11/conditional_first_radical_mod11.py`. Neither result upgrades C-0011 beyond **provisional** or proves complex BSD.

## Session 15 — full [36] denominator certificate and six-pair falsification

The [independent minimal-model affine verifier](../anticyclotomic_11/independent_affine_ideal_and_polarization.py) directly computes [36]Q for all ten Q among P_i+R and P_i+P_j+R, verifies `x([36]Q)*D^2,y([36]Q)*D^3∈O_K`, and proves denominator ideal primitivity by the **integer norm gcd** `gcd(N(xD²),N(D))=1` in every case. Unlike our previous denominator-route checks, this does not use the same projective scalar multiplication. It then verifies all six distinct-vector polarization identities (height values 3,8,9,9,10,4 mod11), compared to the individual first digits (1,2,7,8). See the [extended C-0011 audit](../anticyclotomic_11/SESSION14_HEIGHT_MOD11_AUDIT.md).

```bash
python3 -I -B research/anticyclotomic_11/independent_affine_ideal_and_polarization.py
```

**Scope:** validates the *candidate division-polynomial denominator generator* against exact direct affine points, but still shares the published BCLMN height formula and Mazur–Tate sigma first coefficients. Not a substitute for an independent Sage/Magma height computation, and not proof of complex BSD.

## Session 16 — two-digit global p-adic height and exact sigma integrality

[The MST canonical sigma coefficient checker](../anticyclotomic_11/canonical_sigma_integrality_11.py) reconstructs the rational sigma family through t^13 from the original minimal Weierstrass formal group and enforces canonical 11-adic integrality, uniquely obtaining c11=4 mod11. Its independent oracle is the published MST conductor-37/p5 sigma t^7 polynomial, which it also reproduces. The [two-digit height checker](../anticyclotomic_11/conditional_heights_mod121.py) combines the sigma coefficient with BCLMN Proposition 2.4, certifies primitive denominator ideals at ten exact [36]Q points, and verifies all six mixed global height identities modulo 121; it rejects c=0 as the wrong second-digit normalization. The provisional vector is (100,90,7,8), normalized [1:13:40:63] mod121 (manually guessed incorrect alternatives must never be used). Full [audit and obligations](../anticyclotomic_11/SESSION16_CANONICAL_SIGMA_MOD121.md).

```bash
python3 -I -B research/anticyclotomic_11/canonical_sigma_integrality_11.py
python3 -I -B research/anticyclotomic_11/conditional_heights_mod121.py
```

Passing AI-authored code is not independently maintained Sage/Magma sigma, expert theorem review, a derived height or a result on original complex BSD. Continue H3 in parallel with H2.

## Security / completeness boundaries

The manifest validator only checks syntax, references, and basic evidence-policy invariants. It does **not** evaluate or execute commands from `experiments.json`. Commands in untrusted PRs must never be interpolated into shell steps. The test runner invokes a fixed list of pinned Python/GP programs.

It cannot certify local Kummer compatibility, analytic continuation, Satake/Euler-factor identities, Selmer upper bounds, a global height pairing, or BSD. External review must be real and attributed. A checked box in this JSON file proves nothing mathematically.
