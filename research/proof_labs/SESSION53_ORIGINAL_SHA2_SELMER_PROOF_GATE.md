# Session53: a proof gate for the ORIGINAL curve's 2-primary Sha

**November 21, 2026. AI-assisted, not independently peer reviewed.** New general BSD implication: **NONE**. The question is whether the original curve's 2-primary arithmetic BSD invariant can be certified now, not another auxiliary Kummer-field calculation. No changes to the historical WPR or C-series status.

## Falsifiable arithmetic question

Let E/Q be 234446.a1: y²+xy=x³−x²−79x+289. Its Mordell–Weil rank is **4** (Cremona/LMFDB), and E(Q)[2]=0 because the short-form 2-division cubic X³−1267X+17230 is irreducible. The exact Kummer/Selmer sequence says

  0 → E(Q)/2E(Q) → Sel_2(E/Q) → Sha(E/Q)[2] → 0.

Hence **dim_F2 Sha(E/Q)[2] = dim_F2 Sel_2(E/Q) − 4**. If the complete actual 2-Selmer rank is exactly **4**, then Sha(E/Q)[2]=0 and *all* 2-primary torsion in Sha vanishes: every nontrivial 2-power-order class has a nonzero multiple of order2. This implication needs neither complex analytic rank information nor prior Sha finiteness. It is a standard theorem, not a novel BSD proof; an arithmetic computation must supply its missing hypothesis.

A result greater than4 is an INCONCLUSIVE result for this shortcut, and a result less than4 contradicts the established four rational directions. Neither the numerical analytic Sha≈1 shown by LMFDB nor the 2026 auxiliary class-field 11-rank lower bound certifies the original Sha[2].

## Executable acceptance and negative controls

Use the documented Sage 10.6 method E.selmer_rank(algorithm="pari") AND E.selmer_rank(algorithm="mwrank") for independent actual **2-Selmer** computations; both must agree on E. See Sage/PassageMath online reference under EllipticCurve_rational_field.selmer_rank. This API is NOT an 11-Selmer computation.

Control curves:
- 389a1, minimal [0,1,1,-2,0]: rank2, 2-Selmer dimension2.
- 571a1, [0,-1,1,-929,-10595]: rank0, **2-Selmer dimension2** with Sha[2]=(Z/2)^2. This catches accidentally reporting rank instead of Selmer dimension.
- Exact 2-division cubic irreducibility tests E(Q)[2]=0.
- Both computational implementations must agree, and output 2-Selmer >=4.
- Print an explicit NO-SHA-CERTIFICATE if 2-Selmer >4, and do not call any failed/timeout run a mathematical result.

New source: research/proof_labs/sage_original_sha2_descent_gate.py.
New bounded workflow: .github/workflows/original_sha2_descent.yml (official immutable Sage10.6 Docker digest, network disabled, 6GB memory, two CPUs, 900s process limit). The workflow output, NOT a prior imagined value, is the eventual certificate. Mathematical dependencies are complete/verified 2-descent algorithms and the classical Selmer exact sequence. Not a formal proof or expert mathematical audit.

## ACTUAL completed certificate: first direct original-curve Sha[2] vanishing result

The pinned Sage10.6 GitHub Actions workflow executed the **ACTUAL** algorithms, rather than merely installing a test. Its latest source head prior to this documentation update was **7b4bbd98e2ac01626586b00973f2b3cfc0d4e994**, with two complete independent workflow runs **44926218323** (job **136912780575**) and **44926199989** (job **136912724697**), both successful. Job logs were read directly with the GitHub Actions job-log API, and they record exact output:

    SELMER2 571a1-Sha2-control PARI=2 MWRANK=2
    SELMER2 389a1-rank2-control PARI=2 MWRANK=2
    SELMER2 234446a1 PARI=4 MWRANK=4
    CERTIFICATE_CONCLUSION Sha(E/Q)[2]=0
    CERTIFICATE_CONCLUSION Sha(E/Q)[2^infinity]=0

The two backends are **PARI's 2-descent** and **eclib/mwrank's 2-descent** as called by the *same pinned Sage10.6 instance*. This is an orthogonal library-level reproduction but not a proof assistant or independent human review. Source exact rank4 is known from the audited Cremona/LMFDB entry; the Sage computation verifies irreducibility of its rational 2-division cubic. The two-Selmer result therefore gives the actual arithmetic consequence

\[
\boxed{\operatorname{Sel}_2(E/\mathbf Q)\simeq(\mathbf Z/2)^4,
\quad \Sha(E/\mathbf Q)[2]=0,
\quad \Sha(E/\mathbf Q)[2^\infty]=0.}
\]

This is a **special-case computational certificate for the original elliptic curve** and a deduced exact BSD arithmetic invariant, not a new technique or novel general statement. The values are plausibly already known from the classical Cremona two-descent rank verification; do not assert priority/novelty without a systematic prior-art check. All non-2-primary Sha, original complex L''(E,1)=0, nonzero fourth complex derivative as an exact rank statement, full BSD leading coefficient and general BSD remain OPEN.

**Scope of validation:** Current-head software tests and independent algorithms support internal reproducibility. A user-facing and repository claim must still disclose that its proof uses published algorithm correctness and the externally established Mordell–Weil rank4, and has not undergone independent arithmetic-geometer review. The timestamped logs are the mathematical numerical evidence; green job indicators alone would not suffice. A later source commit that edits this note does not invalidate the pinned prior source-output certificate, but must not be mistaken for a new independent computation.

---

## Why the older 11-descent result does not transfer

Session35/C0044's actual nonzero twist Kurihara number (10 mod11 at 3389) and Sakamoto's published residual-Selmer theorem imply, under source/normalization hypotheses, dim_F11 Sel_11(E^{-7}/Q)=1 and twist Sha[11]=0. This controls the *minus* eigenspace over K=Q(sqrt(-7)). The odd-prime quadratic decomposition is

  Sel_11(E/K) = Sel_11(E/Q) ⊕ Sel_11(E^{-7}/Q).

Thus the twist result only gives
  dim Sel_11(E/K)=dim Sel_11(E/Q)+1;
four rational points imply dim Sel_11(E/Q)>=4, but **no upper bound** follows. To prove original Sha(E/Q)[11]=0, we still need a complete dim Sel_11(E/Q)<=4 (equivalently dim Sel_11(E/K)<=5) certificate, with every global 11-Galois cohomology and ordinary classical local Kummer condition accounted for. Neither Dainobu class-field rank, finite Kummer images, derived 11-adic heights, nor the Sage **2**-Selmer rank routine supplies this 11 upper bound.

## Full-BSD status and next step

General BSD for all E/Q, original complex L''(E,1)=0, exact analytic rank4, original whole Sha finiteness, and full normalized BSD leading coefficient remain UNPROVED. A certified original Sha[2-infinity]=0 would be a finite, meaningful BSD-arithmetic component, but not an analytic rank theorem, not full Sha finiteness, and not claimed novel before literature review.

One safe lemma is the exact 2-Selmer / Sha short exact sequence; the credible computational step is dual independent 2-descent with a Sha-bearing control; the high-risk step is a complete original 11-descent with four-dimensional upper bound. Stop further auxiliary Kummer field-degree work unless it feeds an explicitly typed Selmer upper bound or characteristic-zero complex L-function theorem. Independent exact algorithms are a **validation method**, not a substitute for mathematical proof. Draft only; don't merge without CI and arithmetic-geometry review.
