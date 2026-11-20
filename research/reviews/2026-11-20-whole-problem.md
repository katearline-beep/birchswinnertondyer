# WPR-2026-11-20-01 — weekly independent-minded whole-BSD review

**Friday 2026-11-20, America/New_York.** AI-assisted, unreviewed by independent human expert. Previous [WPR-2026-11-13-01](2026-11-13-whole-problem.md); branch stacked on PR #81. Main HEAD `154eca9b6053c11e7b05f305219c313fcc628612` (last merge PR #75 on Oct 22); GitHub PR listing on Nov 20 shows #76–#81 open. Next checkpoint Nov 27. **No merge authorized or performed.**

## General conjecture and specific analytic gap

For every elliptic curve `E/Q`, BSD asserts `rank E(Q)=ord_{s=1} L(E,s)=r`, finiteness of `Sha(E/Q)`, and the leading coefficient `L^(r)(E,1)/r! = Omega_E Reg(E/Q)|Sha(E/Q)| prod_l c_l / |E(Q)_tors|²` under consistent period conventions. These are three distinct obligations.

For the focal `234446.a1: y²+xy=x³−x²−79x+289`, algebraic rank four and sign +1 do not establish analytic rank four. Exact original **complex** `L''(E,1)=0` is unproved, as is rigorous `L^(4)(E,1)≠0`. Original Sha finiteness and leading coefficient remain unproved. The positive -7 twist derivative, anticyclotomic p-adic heights and Euler-system filtrations are not original complex derivatives.

**NEW PROVED IMPLICATION TOWARD BSD SINCE NOVEMBER 13: NONE.** No merged arithmetic result, source-matched complex comparison, evaluated supported global cochain, second Bockstein, or original complex vanishing proof was identified. This week's contribution is a sharper local-global compatibility falsifier and source-scope review, not a theorem on the curve.

## C-series audit (all 50 retained without promotion)

- **C-0001–0009:** exact finite local 11-adic logs/Selmer decomposition, conditional twist derivative enclosures and integral filtration counterexample; original complex L'' numerical only.
- **C-0010–0014:** exact character, sigma, denominator arithmetic and conditional/provisional first anticyclotomic heights; no independently certified global height or h².
- **C-0015–0019:** published Castella–Hsieh rank-two applicability no-go; Ulmer function-field mechanism (prime-field ranks 2,3,7 versus geometric 3,7,25); Fermat/Jacobi controls; not characteristic-zero complex rank four.
- **C-0020–0028:** Howard/Heegner tower source-derived class, base torsion, divided norm classes and universal-norm regulator no-go; no actual higher Coleman orders or original complex bridge.
- **C-0029–0041:** provisional first heights, exact ray/division torsor and residual saturation computations; conditional supported cohomology, not evaluated global nonabelian cocycle.
- **C-0042–0049:** twist Kurihara delta, local norm reference, conditional first-lift and normalization; no actual supported global correction or second obstruction.
- **C-0050:** source-dependent finite Frobenius commutator constraint on PR #77, not a constructed first correction, second lift, or complex L derivative.

All historical corrections (sigma digits, Ulmer ranks, integral vs mod-11 augmentation, base vs tower Heegner classes, first vs second Bockstein, source theorem hypotheses) remain in force. Categories stay distinct: exact finite arithmetic, provisional certificates, conditional theorem applications, literature no-go findings, and research infrastructure. No claim's reviewed status changes.

## Fresh literature, exact outputs and scope

- **Yifeng Liu, [*Motivic generating functions and L-derivatives of cohomological automorphic representations*](https://arxiv.org/abs/2611.10478), submitted Nov 7, 2026:** abstract describes a Gross–Zagier-type formula in a doubling-method setting for Hilbert cusp forms and Hecke characters with balanced weights, and formulates a more general motivic arithmetic inner-product *conjecture*. It does not state a characteristic-zero **third** derivative vanishing theorem for our weight-two quadratic base change. Full theorem hypotheses and any specialization remain to be checked; this is abstract-level triage, not a categorical no-go.
- **Du–Peng, [*On the central derivatives of L-functions and modularity of Heegner cycles*](https://arxiv.org/abs/2603.15795), March 2026:** abstract describes central derivative as height pairing of higher-weight Heegner cycles, not an asserted third complex derivative for weight-two E/K. Again, a source-scope lead, not a new implication.
- **MIT [Gross–Zagier 40 Years Later](https://math.mit.edu/events/gross-zagier/), Aug 3–7, 2026:** the higher-derivative Yun–Zhang discussion is explicitly a **function-field analogue**. It does not furnish the number-field comparison.
- **Burns–Kurihara–Sano (2024), Theorem 1.3:** as corrected in Nov 13 review, needs BOTH `Sha(E/F)[p∞]` and `Sha(E/Q)[p∞]` finite and produces cohomological Kato norm augmentation containment, not complex L''; its conjectural comparison cannot be used as a proved arrow.
- **October 2026 low-corank BSD manuscripts:** claims unrefereed; corank≤1 cannot apply when rank E(Q)=4, by Kummer injection.

No newly verified theorem reaches original complex `L''(E,1)=0`. The above scan is bounded, not a universal absence theorem.

## New adversarial stress test: pairwise local compatibility is not global gluing

Over `F_11`, model a two-coordinate **synthetic** first correction `(x,y)` with a Frobenius-style linear requirement `x+y=9`, and two Greenberg-*shaped* local restrictions `x=0` and `y=0`. Each individual and **each pair** of requirements is soluble, yet all three are inconsistent. Exact exhaustive enumeration checks all 121 vectors; independent augmented-matrix ranks are 2 (coefficients) and 3 (inhomogeneous system). The counterfactual Frobenius target zero restores a solution. This invalidates the shortcut **'commutator test passes and each local condition is separately soluble, hence a global supported correction exists'**. It does NOT compute an actual Galois cocycle or show that our curve has an obstruction. In particular these synthetic local constraints are not asserted to be the actual ordinary Greenberg maps.

Run: `python3 -I -B research/reviews/controls/supported_local_gluing_negative_control_2026_11_20.py`. **Executed in an isolated local Python environment on Nov 20: PASS**, with exhaustive and independent linear-algebra checks. Complete repository harness and math tests **not executed locally** because git checkout failed DNS; GitHub Actions verification required. Documentation validators cannot prove the mathematics.

Transfer: exact finite linear algebra/cohomological gluing is valid mathematical machinery; exhaustive model checking is a validation method. Coding-theory parity-check matrices could independently verify a real assembled linear system, but cannot supply the missing arithmetic localization maps. No speculative physical analogy is promoted.

## H1–H6 decisions, falsifiers and next tests

| Track | Allocation | Missing arrow and decisive falsifier |
|---|---:|---|
| **H1 supported derived Kato/Galois correction** | **40%** | No arithmetically realized nonabelian quotient with `rho,ell,c0,c1`, all relations and *simultaneous* Greenberg/local support. New toy proves pairwise tests insufficient. Reject quotient if any actual relator, Frobenius 23/127 or localization fails. |
| **H2 mixed heights/second Bockstein** | **15%** | No actual supported cochain or correctly normalized h². Reject mismatched Selmer complexes, unverified height character, or inference from first-lift existence to second-lift success. |
| **H3 characteristic-zero quadratic geometry** | **40%** | Need a source theorem literally outputting `L'''(E/K,1)` and independently forcing its zero; Nov 2026 motivic source has no verified such specialization. Reject first-derivative, p-adic and function-field substitutions. |
| **H4 Mazur–Tate** | **0%, parked** | No noncircular original complex comparison; BKS theorem requires Sha and addresses different filtration. |
| **H5 complex diagnostics** | **5%** | Numerically small L'' cannot prove zero; no more precision-only work. |
| **H6 period projector** | **0%, parked** | No defined higher projector or source-matched complex comparison; parity-only controls fail. |

**Safe lemma:** assemble the actual finite supported first-correction equations with the same global variables across Frobenius, ramification and both ordinary localizations; prove consistency by a single augmented-matrix certificate, not independent local checks.

**Credible leapfrog:** exhibit an arithmetically realized nonabelian quotient for `x=P2−2P1` and evaluate its normalized supported first cochain, including the `[10]Q` Shapiro comparison, then attempt second Bockstein.

**Wild alternative:** a characteristic-zero motivic cycle identity whose literal output is third complex derivative of `L(E/K,s)`, together with independently proved geometric vanishing. No such theorem is established here.

**Selected next decisive test:** H1 simultaneous global-local cochain feasibility on an *actual* arithmetic quotient, with explicit support and local maps. Before any heavy enumeration, require source-certified finite presentation and Galois action; if unavailable, record that as the blocker. Parallel H3 only source-level theorem triage. Deprioritize raw p-adic digits, brute-force enormous fields, precision-only L'' and additional synthetic controls once this logical point is registered.

## GitHub and blockers

Nov 20 GitHub API: PRs #76–#81 open and stacked, main unchanged since Oct 22; open issues include #61 (residual Kummer/quotient), #53 (second derived height), #20 (H3), #18 (H1). This review is stacked on #81, not merged. New PR CI must be checked independently. No expert arithmetic-geometry review or Sha finiteness proof. Principal blocker remains the missing noncircular original complex L'' comparison; operational blocker is the unmerged six-PR stack and inability to run complete checkout locally.
