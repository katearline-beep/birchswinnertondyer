# Theorem-first BSD research program — binding pivot, 19 October 2026

**Decision:** The existing rank-four research was a useful *arithmetic testbed*, but further anticyclotomic precision is not our default research engine. A theorem-led, multi-laboratory program now sets the agenda. This is a research governance decision, not a new proof of BSD.

## North star: what would actually count?

For all elliptic curves over \(\mathbb Q\), BSD predicts complex analytic rank = algebraic rank and the correctly normalized leading coefficient (with finite Sha). On our focal elliptic curve 234446.a1, \(E:y^2+xy=x^3-x^2-79x+289\), algebraic rank four is known and **original complex \(L''(E,1)=0\)** is unproved here. A result for a *different* anticyclotomic \(p\)-adic L-function, a 3-digit global height, or a finite-field surface is not a substitute.

Our first strategic deliverable is therefore a **typed, sourced diagram** in which each established theorem, computed hypothesis, missing comparison and potential circular dependency has a precisely named *domain* and *codomain*. Focus on what the successful rank-two and positive-characteristic theories actually prove, not speculative analogies.

## The three laboratories

| Laboratory | Published baseline | Chosen control | First executable result | Missing arrow toward original BSD |
|---|---|---|---|---|
| **A: rank-two generalized Kato / derived height** | Castella–Hsieh 2022 Theorems A, 4.1, 4.5; derived Selmer filtration already works at arbitrary rank under its hypotheses | 389a1, p=5, K=Q(sqrt(-11)) is an independently available *height* control, **not** automatically a valid CH Theorem A control | [rank scope/hypotheses checker](../proof_labs/kato_rank_scope_gate.py), [source audit](../proof_labs/RANK_TWO_KATO_THEOREM_SCOPE.md) | Actual Iwasawa cohomology class satisfying Coleman-map hypotheses; then a noncircular comparison to original complex \(L''\) |
| **B: proved high-rank function-field BSD** | Ulmer 2002 Theorem 1.5 and Remark 1.6, GEOMETRIC rank p^n (or p^n−2 if 6|d), BSD proved via surface Tate theory; exact Fp(t) rank requires Thm 9.2 | p5,d6 rank **2 over F5(t)** / 3 geometrically; p7,d8 rank **3 over F7(t)** / 7 geometrically; p5,d26 rank **7 over F5(t)** / 25 geometrically | [finite-field arithmetic double check](../proof_labs/ulmer_function_field_fibres.py), [global mechanism audit](../proof_labs/ULMER_FUNCTION_FIELD_BSD_LAB.md) | A meaningful characteristic-zero *complex L-function* comparison; Frobenius surface zeta pole does not automatically transfer |
| **C: original rank-four test curve** | C-0001 through C-0014 modular/11-adic arithmetic with robust negative controls, **full global height remains provisional** | E=234446.a1, p=11, K=Q(sqrt(-7)) | Retain previously merged tests and [full height validation issue](https://github.com/katearline-beep/birchswinnertondyer/issues/32) | A verified global derived-height class and **independent complex reciprocity**; no extra local digits without a named hypothesis |

**A key correction:** There is no need to invent a general-rank derived-height filtration: Castella–Hsieh Theorem 4.1 already has one. The rank-two bottleneck concerns the **generalized Kato-class nonvanishing implication** in Theorem A, not the existence of the filtration. Indeed, **under all Theorem A hypotheses**, \(\kappa\neq0\Rightarrow\dim_{\mathbb Q_p}\mathrm{Sel}=2\), while rank four gives dimension at least four. The particular \(\kappa\) must therefore vanish **if the hypotheses hold**; our currently used K=-7 does not meet the odd-inert conductor requirement. We must identify a different rank-sensitive higher object rather than assume that the rank-two class itself provides a rank-four nonvanishing certificate.

**B's transfer trap:** Ulmer's proof leverages special Fermat-surface quotients, the Tate conjecture and finite-characteristic zeta functions; he specifically notes the corresponding \(\mathbb Q(t)\) family has rank *bounded independently of d*. The same local finite-field fibres can even arise in published F5(t) rank-2 and rank-7 examples (geometric ranks 3 and 25). One cannot import their rank conclusion into the complex setting by renaming variables.

## Initial research effort allocation

- **45%** Laboratory A: theorem hypotheses, typed derived-height/Kato maps, exact source comparisons, rank-two controls.
- **30%** Laboratory B: reconstruct the published Fermat quotient and zeta-factor mechanism, with characteristic-zero no-go tests.
- **15%** Laboratory C: seek an independent complete global-height implementation or external mathematical review; no automatic new digits.
- **10%** speculative H3/H6: insist on an actual *complex* third-derivative or geometric period formula; an attractive root-sign analogy fails the rank-two falsifier.

These are allocation guidelines, **not** probabilities of solving BSD.

## A staged workflow with stop/go decisions

**Stage 0 (implemented in this PR):** Read primary sources; classify each theorem by object, field, rank hypothesis, local/global conditions and output. Prove the elementary rank-four no-go under CH Theorem A hypotheses. Build Ulmer arithmetic lab with two independent fibre point-count methods, bad fibre exclusions and a **global-rank versus identical-local-fibre** negative control. Add machine-checked experiments and prohibit promoting a theorem from a different category or field to original complex BSD.

**Stage 1 (next substantial calculation):** For the **rank-two** lab, identify a published Theorem A appendix instance with inert conductor, irreducibility, good ordinary p, root sign and nonzero auxiliary adjoint L-value all verifiably satisfied. Separately instantiate Theorem 4.1/4.5's domain/codomain, extension field, augmentation filtration and required Iwasawa class in rank four. For the **function-field** lab, reconstruct a dominant rational map from the Fermat surface to \(\mathscr E_d\) for p5,d6 and verify the equation in finite-characteristic function fields. Reject superficial local-count generalizations. Keep original E as a *test*, not theorem source.

**Stage 2:** Reconstruct the relevant Fermat-zeta/Gauss-sum factor or another global cohomological mechanism. Define a *candidate transfer theorem* to the original complex \(L''\), with at least one rank-two counterexample test and all unproved assumptions explicit. If no concrete map survives, record a documented no-go instead of inventing one.

**Stage 3:** Only after a credible theorem bridge exists should we spend heavily on our rank-four curve to test the exact mechanism and move toward full BSD, including a separate leading-term and Sha strategy.

**Stop conditions:** No inference from first p-adic height to complex order; no naive extension of a nonzero rank-two Kato class to rank four; no mistaken identification of Ulmer's proved function-field BSD with number-field BSD; no local-fibre evidence claimed as a function-field rank calculation; no precision additions without a hypothesis. Passing our harness is not independent mathematical peer review.

## Why this may bear more fruit

The prior work answered *what local/global arithmetic data look like*. This pivot asks *which existing proof mechanisms already force analytic vanishing and how those mechanisms work*. It converts broad speculation about “generalizing rank two” into checkable theorems with failure cases, and it separates **published high-rank BSD** from the unsolved characteristic-zero case.

**What it has actually proved toward complex BSD today:** **none**. The strategic advance is avoiding two hidden category mistakes (rank-two Kato nonvanishing, and positive-characteristic Tate/Frobenius transfer), while creating two reproducible mathematical laboratories and concrete future bridge obligations.

**Primary sources:** [Castella–Hsieh 2022](https://doi.org/10.1017/fms.2021.85), [Ulmer 2002](https://annals.math.princeton.edu/2002/155-1/p09); existing [WPR-1 protocol](FULL_PROBLEM_REVIEW.md) and [leapfrog protocol](LEAPFROG_PROTOCOL.md).


**Session 20 correction and milestone:** [Ulmer §4 exact Fermat map and §9 Frobenius orbit audit](../proof_labs/SESSION20_FERMAT_ORBITS_AUDIT.md) correct Session19's erroneous identification of geometric rank with Fp(t) rank. The map's polynomial identity holds integrally, while the global Frobenius/Jacobi and Tate mechanism is the characteristic-p-specific step. Codes now reproduce rank 2,3,7 over Fp(t) and 3,7,25 after extending constants; Ulmer is the source of the theorems, not the scripts.


## Session21 realized theorem-first rank-two control

The concrete valid published CH case is now **433a1 / p11 / K=Q(sqrt(-7))**, as in [Session21 source map](../proof_labs/SESSION21_CH_433A1_THEOREM_MAP.md). Unlike the prior BCLMN height-only example 389a1/K=-11, it meets the CH Appendix's odd-inert situation and has published theta order2; a short exact checker proves many local and residual irreducibility hypotheses. CH Thm4.1 simultaneously **does apply** to our focal rank4 curve with Nminus1, whereas ThmA/B does not for this old field. Hence stop reselecting a rank-two example: Issue41 should focus on **genuinely constructing and checking global Iwasawa z and Coleman maps**, and separately the impossible-without-new-theorem complex L'' bridge. We did not construct any class or prove BSD.
