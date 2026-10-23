# WPR-2026-10-23-02 — supported-cochain attempt and arithmetic constraint

2026-10-23 America/New_York. AI-assisted internal review; no independent
human/expert review. Baseline PR76 head `fdf80d191f38d00ed65ec60ec309f2c936bbcb33`,
main `154eca9b6053c11e7b05f305219c313fcc628612`. PR76 remains open and
unmerged; its six pull-request workflow families succeeded at that head.
Recent merged PR75/73/71 and open issue61 were examined. Remote rank-two
and H3 branch heads remain `ad91e78c1ecd` and `e17b3bcd517f`.
Their existing source-gate work supplies no evaluated focal cochain.
The preceding [whole-problem review](2026-10-23-whole-problem.md) and
[immutable structured record](https://github.com/katearline-beep/birchswinnertondyer/blob/fdf80d191f38d00ed65ec60ec309f2c936bbcb33/research/reviews/current.json) are preserved.
Next whole review remains due2026-10-30 or earlier under WPR-1.

## Original objective and complete scope audit

General BSD asks for equality of algebraic rank and complex analytic order,
Sha finiteness and the period/regulator/Tamagawa/torsion leading-coefficient
formula. For original E=234446.a1 the missing exact identity remains
L''(E,1)=0; exact order four additionally needs a rigorously nonzero fourth
derivative. Neither the twist's first derivative nor an11-adic first
correction supplies that complex comparison. Original Sha finiteness and
the full leading coefficient remain unproved.

**New proved implication toward those BSD objectives: NONE.**

All49 existing C-series entries retain the scope and review boundaries
listed individually/by group in the preceding same-day review, checked
against the current ledger. No existing claim is promoted: local log and
height inputs C0001–14 remain distinct; source-scope and function-field
claims C0015–23 retain their hypotheses; divided universal norms C0024–28
cannot witness a nonzero regulator; C0029–32 comparison and domain claims
do not evaluate h2; arithmetic inputs and finite quotient limitations
C0033–41 do not realize a supported cochain; C0042–47 Selmer/existence
deductions retain their source assumptions; C0048/49 give local references
and conditional normalization, not global cocycle values. Corrections to
Ulmer ranks, sigma, norm factors and supported/unrestricted scope remain.

New C0050 is limited to a necessary relation for a first correction:
for the specified actual prime Frobenii, c1([Frob23^12,Frob127^10]) equals
9*c0(Frob127^10), which is nonzero. Its finite arithmetic and elementary
cochain deduction are internally checked, source-dependent and unreviewed.
It supplies no actual full correction, local homotopies or second height.

## Attempt, result and stopping decision

The PR76 target was a supported first global correction for x=P2-2P1,
with evaluated Galois action, all relations, Greenberg local restrictions
and comparison to the chosen [10]Q Shapiro reference. Inspection confirmed
that Session31's explicit algebraic cover is not an arithmetic realization
and Sessions36/37's existence and normalization do not supply its matrices.

Before further arithmetic, EX018/LF015 recorded a bounded test at23 and127.
The [Session38 audit](../proof_labs/SESSION38_FROBENIUS_COMMUTATOR_CONSTRAINT.md)
derives the exact commutator relation, uses actual finite reduction to
prove its Kummer input nonzero, and separates that deduction from a full
cochain evaluation. This rejects any proposed quotient that makes the
two powered Frobenii commute, including refinements abelian over K(E11).
It does not reject the necessary nonabelian extension or prove that no
supported solution exists.

**Full construction outcome: not obtained.** No manageable arithmetic
nonabelian realization with the required local maps was supplied by the
inspected branches or constructed here. The representation-information
stopping rule from PR76 applies. Further scalar normalization or more
local norm digits cannot fill these missing inputs. A narrow PR recording
the necessary arithmetic constraint is warranted; a claim of a solved
global test is not.

## Competing tracks and next decision

| Track | Decision | Evidence and remaining falsifiable step |
|---|---|---|
|H1|Prioritize within a bounded construction attempt|C0050 rejects commuting refinements. Supply a nonabelian arithmetic realization, then test every relation and the original ramification support.|
|H2|Limited|First-lift existence/local reference remain conditional. Supply actual Greenberg cone maps and normalization before computing the corrected second Bockstein.|
|H3|Limited|The original complex comparison is still absent. Require a characteristic-zero third-derivative theorem and an independent vanishing reason; function-field analogies fail scope.|
|H4|Parked|No noncircular original-complex interpolation bridge; extra modular-symbol congruences cannot replace it.|
|H5|Diagnostic|Numerical smallness does not certify zero. A fourth-derivative enclosure alone would leave L'' unresolved.|
|H6|Parked|No typed period projector or complex comparison; rank-two counterexamples still block parity-only arguments.|

Safe lemma: arithmetic commutator necessary condition, now recorded.
Credible leapfrog: realize the nonabelian embedding problem on actual
G_(K,Sigma), then verify local Greenberg maps and [10]Q normalization.
Wild alternative: a characteristic-zero higher-cycle complex regulator
comparison, still **no valid bridge identified**. Maintain the prior
60/20/15/5 allocation for H1/H2/H3/H5, with no H4/H6 allocation; do not
repeat failed quotient enumeration or precision-only searches.

The exact transfer used is the crossed-homomorphism law and its associated
group extension, with arithmetic Frobenius witnesses. Formal-methods
relation checking supplies a validation method. Neither analogy nor the
unipotent matrix control is an arithmetic Galois realization. No useful
additional transfer from physics or biology is identified for this test.

## Checks and review boundary

Two different elliptic models/group algorithms and two Artin-coordinate
computations agree. Group-word expansion and3x3 matrix multiplication
independently check the commutator sign. Zero character/Kummer inputs,
reversed commutator/character, commuting-quotient and corrupt-oracle
controls discriminate failure modes. PARI regeneration and all existing
workflow checks are included in the PR gates; their final status must be
read from the submitted head, not inferred from this document.

Reproduction commands and mathematical source dependencies are in the
Session38 audit. This review does not announce new BSD mathematics,
external review, a solved cochain or a computed h2. No merge is authorized.

Local run: all62 matrix commands passed on Python3.14.4; the separate direct-coordinate first-height oracle also passed. The new PARI oracle is delegated to its explicit CI step because GP is not installed locally. The journal validator now accepts a numbered same-day immutable checkpoint; legacy filenames and every existing proof-status gate remain enforced, with a new malformed-suffix negative control.
