# WPR-2026-10-23-01 — independent-minded whole-BSD checkpoint

**Friday 2026-10-23 (America/New_York)** · AI-assisted internal critical review, **not independent human/expert review** · Baseline **main `154eca9b6053`** (merge PR #75, 2026-10-22 13:48:41 UTC) · Previous immutable checkpoint **WPR-2026-10-22-01** · Next due **2026-10-30**. No subsequent main commit or newly merged PR was returned by the GitHub API at this review. PRs #71 (2026-10-21), #73 (2026-10-21), #75 (2026-10-22), issues #70/#72/#74 (closed), and open issue #61 were explicitly examined; prior review's `reviewed_prs` omitted #75 even though it discussed C-0048/49, corrected in this checkpoint. All six main-branch GitHub Actions workflow families at the baseline head had completed **successfully**. Green CI does not verify mathematical proofs.

## Reconstruct the full conjecture, not just our example

For **every** elliptic curve \(E/\mathbb Q\), BSD predicts \(r=\mathrm{rank}\,E(\mathbb Q)=\mathrm{ord}_{s=1}L(E,s)\), finiteness of \(\Sha(E/\mathbb Q)\), and the normalized leading coefficient

\[
\lim_{s\to1}\frac{L(E,s)}{(s-1)^r}
=\frac{\Omega_E\,\mathrm{Reg}_E\,|\Sha(E/\mathbb Q)|\prod_{\ell}c_\ell}
{|E(\mathbb Q)_{\rm tors}|^2},
\]

with the appropriate standard real-period convention. Rank equality by itself would **not** establish the leading coefficient, integral Sha order, or Sha finiteness.

**Original focal curve**, not its twist: \(E:y^2+xy=x^3-x^2-79x+289\), Cremona 234446.a1, conductor 234446, known algebraic rank four and root number +1. The rank-zero theorem and four known independent points exclude analytic order zero; even functional-equation parity excludes odd completed orders. Thus the unresolved step to order **at least four** is the exact **complex** identity \(L''(E,1)=0\); exact order four further requires **\(L^{(4)}(E,1)\ne0\)**. The fourth derivative is supported numerically, not yet rigorously nonzero in this project. The completed-L parity and the ordinary-L derivative must be handled with the lower Taylor coefficients correctly. Even success for this E would not prove general BSD or its leading coefficient.

The \(-7\) twist \(E^{-7}\) is a *different* elliptic curve. The 6,000-term rational interval and independent Arb corroboration support its **first** derivative, not original \(L''(E,1)\). Over \(K=\mathbb Q(\sqrt{-7})\), the exact product-rule identity \(L'''(E/K,1)=3L''(E,1)L'(E^{-7},1)\) (using the known lower-order zeros) makes the missing object a **third complex derivative**; no characteristic-zero geometric vanishing theorem for it has been found.

## Answer to the required progress question

**New proved implication toward original complex \(L''(E,1)=0\), exact analytic rank four, general BSD, Sha finiteness of original E, or the full leading coefficient since 2026-10-22: NONE.**

In fact there were **no new merged mathematical commits after PR #75** at the baseline checked. This review adds a *new independently executed falsification/typing check*, not a new arithmetic theorem. The most recent real mathematical input remains **C-0048**: the actual degree-11 anticyclotomic local field and formal point with \(\log_{\min}N_E(Q)/11\equiv115\pmod{121}\), yielding residual ordinary local reference classes. **C-0049** uses this input to specify a **unique normalized residual global first Selmer cohomology class**, **conditionally** on the finite integral height/duality and Selmer-fibre existence inputs of C-0045. It does not compute that global class's cocycle, an integral compatible normalization, the second Bockstein, the original complex derivative, or a BSD theorem.

### C-series audit — all 49 live ledger entries checked, no status promotion

| Claim IDs | Valid output / literature category | Current unproved boundary |
|---|---|---|
| **C-0001, 0002** | Exact finite split-11 local logarithm arithmetic | Local kernels are not Selmer groups or global heights. |
| **C-0003, 0004** | Conditional anticyclotomic theorem applicability; classical quadratic Selmer splitting | Required Sha/local hypotheses and *separate* Selmer upper bounds not supplied by the split. |
| **C-0005, 0006, 0009** | PARI numerical twist derivative; 2,000- and 6,000-term conditional rational enclosures | Published modular/Mellin assumptions and independent expert audit; neither proves original complex L''. |
| **C-0007, 0008** | Finite local Galois and integral augmentation anti-vacuity checks | No derived global Kato class or complex reciprocity. |
| **C-0010, 0011, 0012, 0013, 0014** | Character arithmetic, provisional BCLMN global first heights, canonical sigma digits, conditional transversality | Correct p-adic height normalization and third-party independent end-to-end audit; not a global second height. |
| **C-0015, 0019** | Castella–Hsieh source-scope/no-go, published 433a1 rank-two control, rank-four derived filtration applicability | CH Theorem A's rank-two nonvanishing and odd-inert hypotheses cannot be used to prove rank four. |
| **C-0016, 0017, 0018** | Ulmer characteristic-p BSD mechanism; corrected prime-field vs geometric ranks; one independently checked Jacobi eigenvalue | Neither finite-fibre counts nor a characteristic-p Fermat quotient imply characteristic-zero BSD. |
| **C-0020, 0021, 0022, 0023** | Howard/Heegner entry hypotheses, base Heegner torsion, two-variable no-go, source-derived weight-prime divisibility | Howard horizontal non-torsion is conjectural; no actual original complex L'' comparison. |
| **C-0024, 0025, 0026, 0027, 0028** | Corrected Howard norm; nonzero T-divided class and strict Greenberg membership conditional on source inputs; universal-norm height no-go; 3→1 alternating-form leapfrog | No nonzero base projection, Coleman J-order pair, evaluated h², or complex comparison. |
| **C-0029, 0030, 0031, 0032** | Independent first-digit height arithmetic, Macias Castillo–Sano *2026 preprint* comparison, published BD first-height comparison, independent Arb twist enclosure | Sign/convention/derived-Selmer hypotheses require explicit audit; no second-height value or original complex implication. |
| **C-0033, 0034, 0035, 0036** | Actual C11/C121 Artin layers, Kummer torsors, 11-saturated known points, finite quotient obstruction | Finite quotient may discard correcting cochains; no evaluated full global cocycle. |
| **C-0037, 0038, 0039, 0040, 0041** | Conditional unrestricted lift via duality, supported H² lower bound, exact known-MW localization, conditional first obstruction, one-prime existence argument | Unrestricted does not mean fixed-support/Greenberg; full fine group and actual arithmetic correction uncomputed. |
| **C-0042, 0043, 0044, 0045** | Zhang/Sakamoto source gates, exact q3389 Kurihara \(\delta=10\pmod{11}\), conditional twist Selmer line and first positive Selmer survivors | Published theorem assumptions, modular-symbol normalization and finite integral height-duality inputs must be independently audited; no original positive Selmer bound. |
| **C-0046, 0047** | Conditional signed global H² vanishing and integral first global lifts with a one-parameter ambiguity | Global existence does **not** enforce local Greenberg conditions; no actual cochains or secondary obstruction. |
| **C-0048, 0049** | Exact local formal norm and residual reference; conditional affine normalization of *three* first Selmer fibres | Not a mod121 augmentation lift from C11, not an evaluated global class, and not an h² or BSD theorem. |

**Corrections preserved:** C-0016 prime-field ranks 2/3/7 vs geometric 3/7/25; C-0013 sigma-series vs PARI slope; C-0024 norm factor \(U_{11}\); C-0037 unrestricted vs supported lift; C-0049 conditional fibre nonemptiness. No C-series claim has received independent expert peer review. We did not replace a ledger entry, change its type, or infer mathematical truth from green tests.

## Independent literature/scope review, as of 2026-10-23

1. **Published:** Ryotaro Sakamoto, *p-Selmer group and modular symbols*, *Documenta Mathematica* **27** (2022), 1891–1922, DOI **10.4171/DM/X21**, https://ems.press/journals/dm/articles/13131888. It supports a route from correctly normalized nonzero modular-symbol/Kurihara data to a Selmer bound; the paper's abstract alone is **not** a verification of our focal q3389 input or every specialized hypothesis.
2. **2026 preprint, not peer-reviewed by this project:** D. Macias Castillo–T. Sano, *On Selmer complexes, Stark systems and derived p-adic heights*, arXiv:2603.23978, https://arxiv.org/abs/2603.23978. It proves a conditional comparison of Nekovář and Poitou–Tate complexes and compares BD/Nekovář derived heights, explicitly noting that **classical Selmer groups and H¹ of the Nekovář complex need not coincide without hypotheses** and that a comparison sign matters. This reinforces an **exact local-condition/comparison gate** before claiming C-0049's classical affine fibre produces a Selmer-complex h².
3. **Established derived-height machinery:** Bertolini–Darmon, *Derived p-adic heights*, Theorem 2.18, https://www.math.mcgill.ca/darmon/pub/Articles/Research/13.Derived-p-adic/paper.pdf. Higher heights and universal-norm radicals are p-adic arithmetic objects; they are not a theorem forcing original complex L'' zero.
4. **Current but outside focal scope:** the October 7, 2026 *OpenAI Math Release* manuscript claiming a full BSD formula for Selmer corank \(\le1\), https://github.com/openai/math/tree/main/preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026, is **an unformalized preprint claim, not externally validated here**. Even if correct, its corank 0/1 hypothesis cannot apply to our rank-four E; no theorem is imported from it. Recent Gross–Zagier papers on **first** derivatives likewise do not fill the H3 third-derivative gap.
5. **Global duality source:** J. S. Milne, *Arithmetic Duality Theorems*, Chapter I, https://jmilne.org/math/Books/ADTnot.pdf. Its duality theorems must be applied with the actual Cartier dual, local conditions, ramification set and comparison maps. A finite-dimensional toy is not a proof that a particular arithmetic cochain exists.

No source-matched theorem was found here that sends the evaluated local norm, derived 11-adic heights, or twist L' to **original complex** L''(E,1)=0. Absence in this bounded search is **not** proof that no such theorem exists.

## Adversarial falsification (executed; finite algebra, not curve cohomology)

New [exact standard-library control](controls/first_lift_second_obstruction_2026_10_23.py), locally run 2026-10-23, prints **three PASS lines** and a NONCLAIM. It checks:

- Over \(\mathbf F_{11}[T]/T^2\), \((1+T)^{11}=1\), but over \((\mathbf Z/121)[T]/T^2\), \((1+T)^{11}=1+11T\ne1\). The actual C11 action cannot be silently reused at modulus 121; C121 is needed.
- The actual C-0048 local norm **115 mod121** has unit residue **5 mod11**, but a residue-5 first-order coordinate does not determine a mod121 coefficient. The **known** 115 is genuine extra local precision, not a higher global lift.
- Two explicit free two-term complexes over \(\mathbf F_{11}[u]/u^3\) have identical base and first-order data and the same uniquely solvable affine normalization \(5t+3=0\), \(t=6\). In one \(d_2=0\); in the other \(d_2=\mathrm{id}\), and **no second-order cocycle lift exists** for the same base class. All 121 candidate first-order corrections are checked. This kills the inference “unique normalized first Selmer lift ⇒ second Bockstein vanishes.” It does **not** show the actual curve's second obstruction is nonzero.

These are exact **nonimplication** controls and *do not alter C-0048/49*, which already expressly deny a higher lift. They guard against a future erroneous promotion. The key new insight is a **proof-interface separation**: residual local normalization, integral/tower-compatible Selmer comparison, and secondary arithmetic obstruction are **three distinct proof obligations**, not one solved computation.

## H1–H6 competing research bets, with actual stopping rules

| Track | Status / latest real gain | Missing arrow and cheapest decisive falsifier |
|---|---|---|
| **H1 derived Kato/Heegner** | **Prioritize**: C-0044 negative Selmer line; C-0046/47 conditional supported global first lifts; C-0048/49 local reference and conditional normalized first Selmer fibre. | Evaluate **one actual supported global cochain** for \(x=P_2-2P_1\), with explicit action, cocycle, Greenberg localization and comparison to [10]Q; fail if no finite quotient captures the cocycle/correction. Even success does not give complex L''. |
| **H2 mixed derived heights** | **Limited**: C-0029/31 first height and C-0045 conditional first Selmer survivor domain. | Compute a **genuine** second Bockstein with its local homotopies, normalization, and independent source-matched Selmer-complex comparison; toy alternating form or first height is insufficient. |
| **H3 quadratic-field geometry** | **Limited**: exact product derivative identity and function-field higher derivative analogues. | Demand an actual characteristic-zero **third** derivative formula for weight-two \(E/K\) plus an independent geometric vanishing reason; a first-derivative theorem fails scope. |
| **H4 Mazur–Tate** | **Park**: audited BKS 2025 routes either assume BSD/Perrin–Riou or cover rank one. | Reopen only with a noncircular original-complex L'' interpolation theorem. |
| **H5 numerical curvature** | **Diagnostic**: near-zero original L'' and numerically nonzero fourth derivative; twist first derivative independently enclosed. | No number of extra digits certifies exact zero. Use validated fourth-derivative nonzero only if a separate exact L'' proof emerges. |
| **H6 period geometry** | **Park**: even functional-equation parity admits rank-two controls with L'' nonzero. | Reopen only for a well-defined second-order projector with a proved complex comparison. |

**Allocation for next bounded sprint:** H1 60% (actual global correction, not local digits), H2 20% (source-level Selmer-complex/local-condition interface), H3 15% (third-derivative theorem search), H5 5% (targeted falsification), H4/H6 0% until new theorems. The **safe lemma** is a complete typed finite quotient/cochain/localization *interface* with no assumed solvability. The **credible leapfrog** is an explicit supported first correction, then an actual second obstruction value; the **wild** option is a characteristic-zero higher cycle/complex derivative comparison with an independently checkable vanishing argument. No analogy is counted as a theorem.

**Selected decisive next test, predeclared:** for \(x=P_2-2P_1\), construct a finite quotient of \(G_{K,\Sigma}\) carrying (i) the *actual* E[11] representation and anticyclotomic C11 character, (ii) the actual Kummer cocycle of x, (iii) an explicitly evaluated first correction \(c_1\) solving \(d_0c_1=-d_1x\), and (iv) explicit local restrictions at both 11-adic places and bad primes satisfying the **Greenberg** local condition, matching the [10]Q reference at the chosen v. Require two independently computed cocycle/localization checks and an explicit negative control (mutate the anticyclotomic character or local reference). **Pass** means an actual residual supported normalized first cochain is produced; **fail/inconclusive** means the proposed quotient is too small, the support condition fails, or exact arithmetic disagrees, all separately logged. A quotient unable to encode the cocycle is *not* a global nonexistence proof. If no manageable quotient is found, stop and record a representation/ramification information barrier instead of enumerating the huge five-torsor closure. Only *after* this first-stage success compute the secondary \(H^2\) class and the true derived height. Independently, neither stage alone implies original complex BSD.

**Deprioritized:** additional 11-adic digits, auxiliary-prime enumeration, local norm refinements, generic full-Galois-closure brute force, and unsupported transfers from characteristic p. The full-problem bottleneck remains a **noncircular map to the original complex second derivative**, even if the selected arithmetic cochain experiment succeeds.

## Reproduction, scope and next review

```bash
python3 -I -B research/reviews/controls/first_lift_second_obstruction_2026_10_23.py
python3 -I -B research/harness/validate.py
python3 -I -B research/harness/test_validate.py
python3 -I -B research/harness/validate_full_review.py
python3 -I -B research/harness/test_full_review.py
python3 -I -B research/harness/validate_leapfrogs.py
python3 -I -B research/harness/test_leapfrogs.py
```

The first command was run locally and all assertions passed. Remaining repository-wide checks are **required GitHub Actions merge gates** and must not be described as passed until exact-head CI reports success. No expert review, formal proof, new theorem, original \(\Sha\) finiteness, original complex rank-four equality or BSD leading coefficient is claimed. Next independent-minded full review due **2026-10-30**, or earlier after three substantive merges or a genuine falsification.
