# WPR-2026-10-30-01 — weekly independent-minded whole-BSD review

**Friday 2026-10-30, America/New_York.** AI-assisted adversarial review, **not independent human or expert review**. Baseline main `154eca9b6053c11e7b05f305219c313fcc628612` (last merged PR #75, 2026-10-22 13:48 UTC); unmerged [PR #76](https://github.com/katearline-beep/birchswinnertondyer/pull/76) head `fdf80d191f38d00ed65ec60ec309f2c936bbcb33` and [PR #77](https://github.com/katearline-beep/birchswinnertondyer/pull/77) head `86214a879063b200058494d29d176f9c7af0443d`. This checkpoint is **stacked on PR #77** to preserve its 50th claim and immutable October 23 reviews, and must not be confused with the older `main` current.json. No PR was merged after #75 in the inspected GitHub PR/commit listings as of this review. Both open PRs have six successful workflow families at their respective final heads, but are **not merged or expert reviewed**. Previous immutable review: [WPR-2026-10-23-02](2026-10-23-whole-problem-02.md). Next due **2026-11-06**, or earlier after three substantive merges or a major falsification.

## 1. Reconstruct the entire conjecture and the example separately

For **every** elliptic curve `E/Q`, the general Birch–Swinnerton-Dyer conjecture predicts
\[
r=\operatorname{rank} E(\mathbb Q)=\operatorname{ord}_{s=1} L(E,s),
\]
finiteness of \(\Sha(E/\mathbb Q)\), and, with standard real-period normalization,
\[
\frac{L^{(r)}(E,1)}{r!}
=\frac{\Omega_E\,\operatorname{Reg}(E/\mathbb Q)\,
|\Sha(E/\mathbb Q)|\,\prod_\ell c_\ell}
{|E(\mathbb Q)_{\mathrm{tors}}|^2}.
\]
The exact period convention and all finite factors are proof obligations. Rank equality does **not** imply the leading-term identity or Sha finiteness.

The project's original curve `E: y²+xy=x³−x²−79x+289` (`234446.a1`, algebraic rank four, functional-equation sign +1) requires the **original complex**
\[
L''(E,1)=0
\]
for analytic rank at least four, in addition to its known lower-order vanishing. Even after exact second-derivative vanishing, exact order four needs a **rigorous** `L^{(4)}(E,1) != 0`. Numerical smallness of `L''` and numerical apparent nonzero fourth derivative are insufficient. The \(-7\) twist's certified `L'(E^{-7},1)>0`, 11-adic Bockstein or Coleman augmentation, Ulmer function-field zeta factors, and a derived height are *different objects*. Original Sha finiteness and the leading-coefficient formula remain open.

**New proved mathematical implication toward the original complex rank, general BSD, original Sha finiteness, or leading coefficient since WPR-2026-10-23-02: NONE.** There are no new merged mathematical changes since the prior review. PR #77 adds a provisional source-dependent **necessary first-correction commutator**, not a constructed global cochain or any complex comparison.

## 2. All 50 C-series claims: complete coverage without silent promotion

Read the entire [claim ledger](../../CLAIMS.md), including correction and nonclaim columns; preserve **C-0001 through C-0050** in the structured review. Classification and unresolved dependency by exhaustive ID range:

| IDs | Valid output / literature / corrections | Not established |
|---|---|---|
| C-0001–0004 | Finite split-11 local logs and exact Selmer decomposition; conditional anticyclotomic applicability | Global derived height, complete original Selmer, Sha finiteness or complex L'' |
| C-0005–0009 | PARI numerical twist data; two independently organized exact-rational 6000-term twist derivative enclosures and independent Fourier oracle | Original E's second derivative; expert analytic identity/normalization review still needed |
| C-0010–0014 | Exact character/denominator/sigma arithmetic; provisional BCLMN first-height residues; conditional local/global transversality, including corrected sigma digits and nonidentical kernels | Independently certified global heights or a true second height |
| C-0015–0019 | Castella–Hsieh rank-two vs rank-four hypothesis no-go; corrected Ulmer **F_p(t)** ranks 2,3,7 vs geometric 3,7,25; Fermat quotient/Jacobi checks; genuine 433a1 rank-two control | Number-field rank-four analytic theorem; function-field Tate results cannot be transported without a map |
| C-0020–0023 | Howard/Heegner source prerequisites, base-point torsion, weight-two specialization and source-derived weight-prime divisibility | Nonzero higher weight/anticyclotomic jet, Coleman orders, original complex bridge |
| C-0024–0028 | Source-derived T-divided norm-compatible Iwasawa class with Greenberg hypotheses, universal-norm **radical no-go**, conditional alternating second-height rank test | Nonzero second height or complex comparison; no base universal norm can be used as a nonzero derived regulator witness |
| C-0029–0032 | Independent direct-coordinate first-height and FLINT/Arb twist checks; published/preprint first-height and Selmer-complex comparison with explicit hypotheses | Verified h² on actual classes or original L'' |
| C-0033–0041 | Exact ray towers, five division torsors, reduction/saturation and local Kummer matrices; conditional global/support duality and first-Bockstein obstruction | Evaluated nonabelian arithmetic Galois action, full supported first correction or higher Selmer complex |
| C-0042–0044 | Source-dependent rank-one twist theorem gate and **actual** exact Kurihara `delta_3389=10 mod11` transcript; conditional twist residual Selmer line | Original E/Q Sha, original complex rank, independent expert validation |
| C-0045–0047 | Conditional signed global first-lift existence and one-parameter ambiguity from finite/integral duality | Actual normalized correction cochain or local Greenberg compatibility |
| C-0048–0049 | Actual local formal norm point `115 mod121`, conditional unique normalized *cohomology class* | Evaluated global cochain, integral next layer, actual second obstruction |
| C-0050 | Unmerged PR #77's finite arithmetic plus source-dependent identity `c1([h,g])=9c0(g) !=0` for powered Frobenii at 23,127; excludes commuting quotients | Constructed first correction, Selmer lift, nonzero second Bockstein, any original-complex statement |

All prior corrections (wrong Ulmer prime-field ranks, temporary sigma/height coordinates, naive denominator ideal, old Howard norm normalization, missing vs published tower map, source scope of CH Theorem A, first vs second Bockstein, and supported vs unrestricted cohomology) remain visible. An internally reproducible or conditional result is **not** upgraded to peer-reviewed theorem by this review.

Evidence types are kept separate: exact finite computations (local/Frobenius/Artin/Kurihara), analytic enclosures with stated identities, conditional published-theorem applications (Sakamoto, Kolyvagin, Howard, CH), literature no-go and theorem-scope findings, numerical complex diagnostics, and CI/review infrastructure. Neither six green workflow families nor multiple AI implementations certify source assumptions.

## 3. Recent GitHub and outside literature audit

Inspected PRs **#71, #73, #75 (merged)** and **#76, #77 (open)**, and current open issues **#61, #41, #53, #49, #20, #18, #19, #22, #23**. The latest main commit remains the October 22 merge of #75. PR #76's 49-claim October 23 WPR and normalized-first-lift falsifier are still proposed; PR #77 is **stacked on #76**, adds C-0050 and a same-day 50-claim WPR. Do not merge the October 30 review directly into main without resolving this stack. PR #77's exact finite arithmetic and PARI oracle passed its six CI families; that is evidence about the scripts, not independent theorem review.

Outside sources rechecked on 2026-10-30:

- [Castella–Hsieh, *On the nonvanishing of generalised Kato classes for elliptic curves of rank 2* (2022)](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-the-nonvanishing-of-generalised-kato-classes-for-elliptic-curves-of-rank-2/72ED842AB428A7ED619B1B84287A6864): Theorem 4.1 defines derived heights in generality, but Theorem A's nonzero Kato class forces Selmer dimension **two** and its odd-inert hypotheses fail here. Not a rank-four converse.
- [Kim, *A higher Gross–Zagier formula and the structure of Selmer groups* (arXiv:2203.12161, paper dated March 22, 2026)](https://arxiv.org/abs/2203.12161), Introduction §1.1 explicitly distinguishes its **Kolyvagin-system/modular-symbol structural refinement** from a characteristic-zero third derivative identity. The attractive title does **not** supply the missing `L'''(E/K,1)=0` formula. The paper itself contrasts the number-field situation with Yun–Zhang's function-field higher derivative work.
- [Macias Castillo–Sano, *On Selmer complexes, Stark systems and derived p-adic heights* (2026 preprint)](https://arxiv.org/abs/2603.23978): source for conditional comparison of Nekovář/Poitou–Tate complexes and BD/Nekovář derived heights. Check exact local-condition and sign hypotheses before applying to a specific `E[11]` Selmer complex. It does not compute our cochain or original complex L''.
- [Sano, *Derived Bockstein regulators and anticyclotomic p-adic BSD conjectures* (arXiv:2308.08875)](https://arxiv.org/abs/2308.08875): derived descent relates Iwasawa main conjectures to **p-adic** leading terms (often up to units); the bridge to complex leading terms is framed through additional conjectural special elements/compatibilities. No unconditional `L''(E,1)=0` implication for our curve is supplied by the statements inspected.

This is a **bounded source-scope search**, not a proof that no relevant theorem exists anywhere. No newly applicable original-complex comparison was identified.

## 4. New adversarial negative control: even the *noncommuting* first quotient can fail at order two

To stress-test the tempting upgrade from C-0050 to a second Bockstein, construct the deliberately **nonarithmetic** group
\[
G=\langle h,g\mid [h,[h,g]]=1\rangle
\]
and its affine cocycles with inverse character action \((1+T)^{-\ell}\) over \(\mathbb F_{11}[T]/T^n\). Set \(\ell(h)=2,\ell(g)=7,c_0(h)=0,c_0(g)=1\). These match the **scalar shape** of C-0050, not an actual global `E[11]` torsor. The first commutator is nonzero:
\[
c_1([h,g])=-2=9\pmod{11}.
\]
At \(n=2\) the defining *double* commutator \([h,[h,g]]\) is killed, so a **nonabelian first lift** descends to \(G\). At \(n=3\), however, every choice of first and second generator corrections gives
\[
c([h,[h,g]])=4T^2\ne0.
\]
Thus **no second lift exists in this toy group**, despite the exact nonzero first commutator relation. The [pure standard-library verifier](controls/commutator_second_lift_nonimplication_2026_10_30.py) checks all \(11^4=14641\) generator-correction choices and deliberately kills the obstruction by zeroing the character or Kummer input. This is a **falsifier of the logical shortcut**, not a computed arithmetic second obstruction. It does **not** imply that the actual Galois class fails to lift: the toy relator is not known to hold in the actual Galois group. In particular it does not refute C-0047's source-dependent first-lift existence.

Interdisciplinary transfer: **exact group-cohomology/Bockstein obstruction theory** supplies the affine crossed-homomorphism law; **formal-methods finite model checking** supplies exhaustive negative controls. Both have precisely typed outputs. No speculative analogy from physics or biology contributes a missing map; coding-theory syndromes would be validation only after actual global/local matrices exist.

## 5. H1–H6 allocation and decisive next test

| Track | Decision | Most important current evidence / missing arrow / falsifier |
|---|---|---|
| **H1 derived Kato/global correction** | **Prioritized, capped at 45%** | C-0050 forbids commuting quotient and requires a nonabelian realization. Need actual finite Galois action \(\rho,\ell,c_0,c_1\), support and local homotopies. Kill any proposed quotient whose relators fail the actual cocycle test. No complex comparison. |
| **H2 mixed heights/Bockstein** | **Limited, 20%** | C-0046–49 supply conditional first-lift existence/local origin, not evaluated cochains. New toy shows even nonzero first commutator cannot force second lift. Need actual Greenberg complex and derived h² with source-matched normalization; reject any missing local conditions. |
| **H3 quadratic-field higher geometry** | **Prioritized literature/typed theorem audit, 30%** | Product rule `L'''(E/K,1)=3L''(E,1)L'(E^-7,1)` has the desired type when lower derivatives vanish, but no **characteristic-zero geometric vanishing** theorem is supplied. Reject Kim's structural "higher Gross–Zagier" or Yun–Zhang characteristic-p theorem as a direct third complex derivative formula. |
| **H4 Mazur–Tate** | **Parked, 0%** | Existing purported shortcut is conditional/circular on BSD; no noncircular complex comparison. |
| **H5 numerical diagnostics** | **Diagnostic, 5%** | Keep independent outward enclosures when a theorem supplies an exact vanishing reason; more precision cannot prove zero. |
| **H6 period projector** | **Parked, 0%** | No well-defined projector and original complex period comparison; parity-only rank-two countermodels kill the shortcut. |

**Safe lemma:** Before any huge splitting field, write a minimal finite presentation of an *actual arithmetic quotient* with certified Frobenius lifts at 23/127 and exact Galois action on the five 11-division torsors; explicitly state how local Greenberg restrictions descend. Merely inventing a finite nonabelian cover is not enough.

**Credible leapfrog:** Construct one **actual** supported normalized global correction for `x=P2-2P1`, evaluate it on a generating set, verify all group relations including C-0050, ramification support, and both ordinary local conditions, and match the [10]Q reference by a *computed* Shapiro cochain/coboundary. Only then compute the second Bockstein. **Kill criterion:** if a finite quotient is not arithmetically realized, fails a relation, or lacks local maps, stop; do not substitute toy algebra or another local digit.

**Wild falsifiable route:** Find a characteristic-zero cycle/height formula with precisely the **third complex** derivative of the base-change `L(E/K,s)` as its output and a geometrically forced zero; verify that its product rule isolates `L''(E,1)` with a certified nonzero twist `L'`. No such theorem has been identified. The absence of the theorem is the obstacle, not a reason to assert one.

**Deprioritize** further raw local 11-adic digits, huge unmotivated torsor-field enumerations, abelian refinements excluded by C-0050, additional numerical `L''` precision, and automatic promotion of p-adic conjectures to complex BSD. The next checkpoint is due **2026-11-06**.

## 6. Reproducibility, blockers and truth-status

Run
```sh
python3 -I -B research/reviews/controls/commutator_second_lift_nonimplication_2026_10_30.py
python3 -I -B research/harness/validate.py
python3 -I -B research/harness/test_validate.py
python3 -I -B research/harness/validate_leapfrogs.py
python3 -I -B research/harness/test_leapfrogs.py
python3 -I -B research/harness/validate_full_review.py
python3 -I -B research/harness/test_full_review.py
python3 -I -B research/proof_labs/frobenius_commutator_constraint.py
```

The new control was executed locally and passed all 14,641 exhaustive cases and its two zero-input controls. Existing six workflow suites were green on **PR #76 and #77** at their inspected heads. **The October 30 PR-head checks must be evaluated separately after submission**; the dated review is not a claim of pre-existing green CI. No claim ID or mathematical status is promoted; no new BSD theorem or external human review is asserted.

**Blockers:** PRs #76/#77 remain unmerged and stacked; their conditional C-0050 is not on main. The actual finite nonabelian arithmetic realization, supported Greenberg cochain and second obstruction remain unevaluated. There is no noncircular theorem reaching original complex `L''(E,1)=0`. Until these are resolved, the appropriate research verdict is **NONE toward BSD**.
