# Session35 — bounded exact Kurihara computation

2026-10-21 America/New_York. Baseline68665ab / PR69; issue70. AI-assisted, no external mathematical review. EX021/LF018 continuation, not a claim of novelty.

Predeclared experiment: compute the C0043 twist certificate at q3389. All3388 rational twisted modular symbols, their six components, complete discrete-log weights and a SHA256 transcript are required. Nonzero would give the negative residual Selmer line by Sakamoto2022 Remark1.6 and C0035's nonzero Kummer point, WITHOUT needing the C0032 analytic certificate. Zero is inconclusive. Source-dependent symbol normalization remains a mathematical obligation; transcript arithmetic alone is not an independent focal modular-symbol evaluation.

The local environment has no Sage/eclib. A GitHub-hosted job uses Sage10.6, resolving and recording the Docker image digest and then executing its immutable image ID with network disabled,6GiB memory, no additional swap, two CPUs,20min computation and30min total job. Only session35 PRs or explicit manual workflow runs execute this expensive job. A timeout, memory kill, initialization error or incomplete output is failure to compute, never a zero value. Do not repeat high-cost jobs without a diagnosed implementation or mathematical reason.

[Sage official modular-symbol documentation](https://doc.sagemath.org/html/en/reference/libs/sage/libs/eclib/newforms.html) and the [10.6 source](https://github.com/sagemath/sage/blob/10.6/src/sage/libs/eclib/newforms.pyx) require ECModularSymbol(E,0) for minus evaluations M(r,-1); constructor sign-1 is rejected. The source uses numerical period comparison to normalize its exact rational eigensymbol. That is a trusted implementation input, not an interval-certified normalization. Both displayed focal curves have positive discriminant; the twisting isomorphism's differential/homology comparison from Session34 changes the desired symbol by an11-unit. We must still distinguish a computed transcript from an externally audited arithmetic certificate.

Controls before focal setup:37a1 and its -7 twist must reproduce the six independent PARI values(1,1,1,-2,1,-2), up to explicitly reported common11-unit convention factors. The original-plus/wrong-sign sum must disagree at each tested point. Focal setup uses ONLY original conductor234446. Three exact Hecke identities are checked, with traces independently recomputed by the standard-library verifier. Every row's six exact components must have denominators prime to11; their character sum must match exactly. Full conjugate symmetry, table-log and running-power weighted sums, alternate generator3^5, source-head provenance, transcript hash, row completeness and error/completion handling are checked. Mutations must fail.

Conservative lemma: validate the complete exact transcript and identify implementation limitations. Credible leapfrog: a true nonzero certificate removes hidden negative residual directions before finite first-Bockstein construction. Wild option: a characteristic-zero geometric complex comparison; no typed map exists, so do not spend this computation on an analogy. The imported validation technique is proof-carrying computation: a small rational checker detects transcription, weighting and algebra errors, but not a shared theorem/normalization error.

Whole-BSD review at sprint start: all C0001–C0043 retain their stated boundaries; H1 prioritized, H2/H3 limited, H4/H6 parked, H5 diagnostic. New implication to original complex Lpp=0, exact rank4, original Sha finiteness or leading coefficient: **NONE**. General BSD remains open. No actual cochains or h2.

## Execution status

Planned; no focal value is presumed. The scoped PR and run IDs will record the actual outcome.

Reproduce in Sage10.6:

    sage -python research/proof_labs/sage_kurihara_3389.py > transcript.txt
    python3 -I -B research/proof_labs/verify_kurihara_3389.py transcript.txt

Set SOURCE_HEAD to the40-character source commit before the producer. The checker requires explicit provenance. GitHub records the resolved container digest separately.

### First execution: environment failure, no mathematical output

Head e5640cb7b946dec561e0dbff791312bc0a2634dd, workflow39662360034, job119438405489. The official image resolved to sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb. After a50s image pull the container could not open /home/sage/sage/sage because the host runner UID differs from the image's Sage user. No Sage process or focal arithmetic ran. Corrected by using the image's default Sage user, with the repository still read-only and networking disabled; pinned the observed image digest. This retry addresses a diagnosed launch defect, with the same memory/time gate.

### Second execution: focal initialization killed; algorithm pivot predeclared

Head d229d462eb5b274ae6c8cf5f58f610416f5c7141, workflow39662622982, job119439543248. Sage10.6 reproduces all six PARI values EXACTLY with both scale factors1, then exits137 after about283s in focal sign0 initialization, under6GiB. This is consistent with a memory kill; OOM state was not retained by the removed container, so the precise kill cause is not asserted. No focal values or delta were output.

The official Sage documentation identifies a fundamentally different algorithm: Wuthrich2018 numerical integration with PROVED denominator bounds and rigorous error estimates, returning exact rational symbols through implementation='num' (not modular_symbol_numerical, which returns approximations). It avoids a full modular-symbol basis. This is the required denominator-control bridge missing from the earlier decimal quotient argument, not an inference from real proximity. Use bulk exact values at denominator23723=7*3389, all unitary because original conductor234446 is squarefree. Keep the same6GiB/20min cap. Require original semistability and singleton isogeny class so the curve is optimal independently of an optional database. Cesnavicius, The Manin constant in the semistable case, supplies the optimal Manin-constant theorem; this is a source input, not proved by the script. This third run changes the algorithm; it does not blindly enlarge memory. All transcript and Hecke gates remain.

Sources: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/mod_sym_num.html ; https://arxiv.org/pdf/1703.02951 .

### Numerical backend initialization succeeds; strict input coercion corrected

Head1e8b5a2a52dba5f7899511eaf5648c91900bdf53, job119445051159. Semistability and singleton isogeny-class gates PASS; numerical symbol construction completes in about0.5s, resolving the full-space initialization obstacle. The first base-cusp test passed a Python int0, which this Cython API rejects instead of coercing to a rational. Corrected to explicit QQ(0). No focal value or delta was produced. Added exact numerical-backend37a1/-7 checks against the independently obtained eclib/PARI values before retrying, so the new backend is separately covered. Same resource cap retained.

### Pre-transcript integer-denominator prediction

While the bulk run is in progress, before observing any focal symbol output: independent direct enumeration gives #E(F3)=7 and #E(F5)=10, excluding rational torsion. The original conductor is squarefree, so all X0(N) cusps are rational. Their images under the optimal parametrization based at infinity are rational torsion by Manin–Drinfeld, hence zero. Cesnavicius's Manin-constant theorem identifies the path integrals with actual Neron periods up to sign. Positive discriminant gives a rectangular period lattice. Therefore the original normalized minus symbols at all target cusps should be INTEGERS, not merely11-integral rationals. This is a source-derived, unreviewed normalization lemma and an independent prediction to test on the eventual transcript. A noninteger component stops any Selmer upgrade pending a convention/theorem audit. The code does not prove modularity, Manin–Drinfeld or the published Manin theorem.

## Executed result — nonzero certificate and its precise consequence

Source head **bd120ce552279fc4c73e2566252a661854e73a50**, pull_request workflow **39664821411**, Sage job **119446956023**. Image digest19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb, Sage10.6. The proven-rational algorithm initialized the focal symbol in0.75s including controls, computed all20328 denominator23723 values in115.93s, and completed in**116.10s**. Both numerical and eclib/PARI six-point controls agree EXACTLY with scale1. All three focal Hecke identities pass.

With primitive generator h=3 and the connected-period twisting convention, the weighted sum is

\[\widetilde\delta_{3389}^{\mathrm{conn}}(E^{-7})=\boxed{10}\pmod{11}.\]

The complete [frozen transcript](certificates/session35_kurihara_3389.txt) has3388 rational rows and20328 component values. Canonical row SHA256:

    0997e306c3b838ff43d29cb6eaf34e7ce06701db5c678bf56946cc1ea6e75f78

An independent standard-library checker recomputes every character sum, verifies full conjugation symmetry, rational integrality, Hecke traces by direct point enumeration, discrete-log table and independent running-power sums. The alternate primitive generator3^5 gives residue2=5^(-1)*10 mod11. All20328 components satisfy the separately predicted INTEGER bound. First and last character sums are both25, a symmetry control; neither alone is the certificate. Missing/duplicated rows, interpreter diagnostics and missing completion are rejected. The frozen checksum and nonzero residue are regression-locked; a hash does not prove modular-symbol truth.

The paper's Neron-period convention may differ from the connected period by a factor2; twisting orientation may change a common sign. All are11-units and preserve NONVANISHING. We claim the native value10 with this transcript's conventions, not an unqualified convention-independent value. The published denominator-controlled integration algorithm and the arithmetic/source inputs remain trusted dependencies, not independent expert review. Unlike the earlier near4 decimal, the rational recovery here has an explicit denominator theorem and error-control algorithm. Cesnavicius Theorems1.2/2.13 verify the semistable optimal Manin input; the singleton isogeny class was actually checked.

### C0044 — residual Selmer line, without using the analytic certificate

Accept the recorded residual GL2, ordinary and Tamagawa inputs audited in Session34, the source-normalized symbol algorithm and the above certificate. Sakamoto2022 Remark1.6 then gives

\[\dim_{\mathbf F_{11}}\operatorname{Sel}_{11}(E^{-7}/\mathbf Q)\le1.\]

C0035 supplies a nonzero Kummer point, so the dimension is EXACTLY1. The standard Kummer/Selmer exact sequence gives algebraic rank1 and **Sha(E^{-7}/Q)[11]=0**, hence the entire11-primary torsion subgroup is zero. Quadratic restriction/corestriction, since2 is invertible mod11, identifies the FULL negative residual Selmer part over K with the line generated by R. This removes the hidden-negative-Sha caveat in the residual-domain question. It does not give a positive Selmer upper bound for original E.

There is also a separate source-derived analytic route: the twist's p-infinity Selmer corank is now1, so Zhang2014 Theorem1.4(i), under the same explicitly checked nonsquarefree hypotheses, gives analytic rank1 and finite total Sha for the TWIST. This does not use C0032's analytic interval. It is a corollary of published theorems, not a new converse theorem or a proof about original complex Lpp. It also does not determine the twist's full Sha order or all-prime BSD leading coefficient.

### C0045 — conditional first Selmer lift existence on the three positive classes

Retain the integral first-height comparison, character-unit normalization and perfect finite Selmer-complex obstruction duality hypotheses of C0040. C0044 now supplies the previously missing full negative residual line. The character is anti-invariant, so same-sign first pairings vanish. A positive class annihilating R therefore annihilates the ENTIRE dual Selmer domain, even if the positive domain has unknown extra classes. With the row(1,2,7,8), the three independent residual classes

    P2-2P1, P3-7P1, P4-8P1

have zero first Selmer Bockstein and hence first-stage residual Selmer lifts, **under these finite integral comparison/duality hypotheses**. This is a nonconstructive existence deduction; no correction cochain is supplied. It is not an integral Z11/E121 or T3 compatibility certificate. These mod11 classes are not literal substitutes for the exact Q11 height-ratio classes Xj. No h2 value, full(4,1) signature or original complex BSD theorem follows.

### Next hard decision and whole-BSD scope

Stop more prime searches and height-digit accumulation. The next test is an actual constrained first-lift/cochain for one of the known positive residual classes, followed by a true second-Bockstein pairing on appropriate exact classes. An independent arithmetic-geometry audit should focus on the twisting/period unit, Manin denominator control, recorded residual image, Sakamoto specialization and finite integral height-duality identification. No upstream contact was made.

New mathematical implication about ORIGINAL complex Lpp, analytic rank4, original Sha finiteness or full BSD: **NONE**. The subsidiary twist residual-domain bound is a concrete advance. General BSD remains open and all mathematical-review flags remain unreviewed. H1 remains prioritized toward genuine cochains; H2/H3 limited; H4/H6 parked and H5 diagnostic. CI normally checks the frozen full transcript; manual workflow dispatch recomputes the producer under the same cap, rather than repeating the costly experiment on every edit.
