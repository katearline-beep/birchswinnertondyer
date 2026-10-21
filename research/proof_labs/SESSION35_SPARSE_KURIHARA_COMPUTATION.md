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
