# Whole-problem checkpoint WPR-2026-10-19-01

*2026-10-19 · AI-assisted internal review; not independent peer review · Next full checkpoint due 2026-10-26 or sooner after a major breakthrough or three substantive merges.*

## The question we must not lose

**General BSD:** For elliptic curves over Q, show (i) algebraic rank equals complex analytic vanishing order, and (ii) the precise leading-coefficient formula involving Sha finiteness, periods, regulator, Tamagawa numbers and torsion.

**Our difficult example:** E=234446.a1 has established algebraic rank four, but no project proof that its **original complex** L''(E,1)=0, hence no proof of analytic rank four. The nonzero fourth derivative is so far numerical. Even a future analytic rank-four proof for this example does not settle the leading-coefficient formula or BSD in general.

**What previously missing mathematical implication toward general BSD or the curve's original complex L'' was established since the previous checkpoint? NONE.**

## What genuinely changed since WPR-2026-10-17-01

**Supporting computational result C-0009 improved materially**: independently implemented rational-per-term summation now covers **6,000** coefficients rather than 2,000. A precise conditional interval for the -7 twist's **first derivative** is

\[
34.1691 < L'(E^{-7},1) < 34.1750.
\]

The entire tail after 6,000 is bounded by 0.002895 under the established modular-form coefficient-growth inequality and the correctly normalized exponential-integral Mellin identity. PARI/GP independently matches **all 6,000** original Fourier coefficients, with an intentionally corrupted coefficient rejected. The previous different historical fixed-point code agrees. Three CPython versions pass the exact mathematical assertions. The earlier 2,000-term tail was about 14.322.

This is a much better independently reproducible **conditional subsidiary certificate**. The twist is NOT the rank-four original E; its derivative is NOT L''(E,1). Neither Gross–Zagier–Kolyvagin consequences nor Sha(E^{-7})[11]=0 are newly claimed without the needed mathematical review and separate p-primary hypotheses.

## Claim and six-track review

The claim ledger now contains C-0001 through **C-0009**, each subject to its existing limitations. Specifically:

- **C-0001/2:** finite split-11 local-log matrices; no global derived height.
- **C-0003:** conditional anticyclotomic *p-adic* theorem; required Sha(E/K)[11∞] finiteness unproved.
- **C-0004:** standard quadratic classical 11-Selmer splitting; neither dimension upper bound established.
- **C-0005/6/9:** numerical + rational interval twist first-derivative certificates; C-0009 adds 6,000-term independently checked arithmetic. Not a theorem on original L''.
- **C-0007/8:** cyclotomic field and integral augmentation mathematical checks; no constructed derived Kato class or complex reciprocity.

| Track | Current decision | Exact bottleneck |
|---|---|---|
| H1 Derived Kato | Active but restricted | Missing noncircular complex L'' comparison; BKS results include unproved Sha finiteness. |
| H2 Selmer/Bockstein heights | Restricted | No computed global mixed pairing and no complex reciprocity. |
| H3 Quadratic-field higher geometry | Prioritize theorem-level search | Need actual cubic weight-two derivative vanishing formula, not a higher-weight **first** derivative. |
| H4 Mazur–Tate | Park | 2025 main theorem assumes BSD; rank-one corollary does not apply. |
| H5 numerical curvature | Diagnostic only | Apparent near-zero is never an exact complex zero. |
| H6 geometric period cancellation | Park | No operator beyond parity with a rigorously defined second derivative map. |

### Falsification discipline and decision

**Negative control:** a rank-two curve and rank-four curve can share positive root number, vanish at the center, and have a quadratic-base-change **first** derivative equal to zero; their **third** derivatives can still differ. Therefore a first-height Gross–Zagier theorem cannot by itself produce the original complex rank-four condition. Separately the mod-11 scalar norm false-positive shows why finite congruences must not be confused with integral/Iwasawa vanishing.

**Near-term conservative work:** independently review the newly strengthened twist certificate's Mellin normalization, all-n coefficient bounds, sign/tail enclosure and existing source statements. It is the closest practical subsidiary mathematical theorem. **Not another increase to 10,000 digits or coefficients**.

**Credible leapfrog:** continue H3 exact third-derivative geometry theorem search only if a precise candidate mathematical map is found.

**Wild bet:** an independently constructed complex period projector, falsified against rank-two controls before numerical implementation.

**Selected next experiment:** seek expert-level mathematical audit for C-0009; in parallel carry out a bounded theorem-applicability audit for a genuinely **third**-derivative identity, not high-weight first-derivative analogies.

**Deprioritized:** expanding local-11 logarithms, computing many more cyclotomic fields, and increasing derivative precision without a different proof hypothesis. Our comparative advantage has shifted from computational output to finding a valid logical bridge.

## Sources, status and next review

Reviewed [the claim ledger](../../CLAIMS.md), [C-0009 exact program](../anticyclotomic_11/independent_rational_derivative_6000.py), [its audit](../anticyclotomic_11/EXACT_6000_AUDIT.md), [H3 no-go](../strategy/H3_DERIVATIVE_ORDER_AUDIT.md), prior [whole-problem review](2026-10-17-whole-problem.md) and merged PR #29. Automated independent PARI cross-check and original numerical derivative workflow agree. No independent human expert review has been performed, no new statement proving complex rank four has been established, and no BSD proof is claimed.

**Next periodic review:** 2026-10-26 (with the standing weekly independent-minded review cadence). Never silently promote a computational result to a mathematical theorem.

---

## Session 13 supplement — WPR-2026-10-19-02 (2026-10-19)

**Scope of incremental review:** After merged PR #31 and the present Session 13 source audit, no mathematical implication from four independent rational points to original *complex* L''(E,1)=0 has been proved. No analytic rank-four or BSD claim has been advanced. The Sha finiteness and leading-coefficient obligations remain open.

**Concrete new subsidiary fact (C-0010):** Source verification of BCLMN (2016) Proposition 1.4, Proposition 2.4 and Algorithm 4.2 identified a *genuinely global* elliptic anticyclotomic height formula, distinct from their rank-two shadow-line theorem. We have computed the prime-to-11 anticyclotomic idèle-class-character coefficients for the split primes 2,43,569,1201,1327,117223 and exact four point coordinates P_i+R. The two pure-Python scripts assert Hensel/finite-log congruences, Fermat-quotient first digits, conjugation and polarization. They **do not** compute global p-adic heights; no independently reviewed claim of novelty is made.

**H1** derived Kato: no new complex comparison, still restricted. **H2** Selmer/Bockstein heights: prioritized for the near-term arithmetic implementation, using the published formula only after auditing ordinary splitting, sigma function, component multiples and *global denominator ideals* of [36](P_i+R); no rank-two shadow-line inference. **H3** third-derivative geometry: remains the high-upside complex bridge candidate, no suitable proven theorem found. **H4** Mazur–Tate remains parked due to circularity risks; **H5** is diagnostic only; **H6** geometric period cancellation remains parked.

**Conservative next lemma:** verify the character coefficients with genuinely independent PARI/GP and prove the finite local denominator-ideal input. **Credible leapfrog:** compute global height cross-pairings via the BCLMN formula and falsify the proposed local/global kernel alignment using primitive 11-adic ratios. **Wild option:** search for a noncircular geometric map from a derived two-variable height to original complex L''; kill if it just connects to p-adic order.

**Priority and stopping rule:** do not mistake primes in rational coordinate denominators of P_i+R for the *complete* denominator ideals of [36](P_i+R), and do not use finite agreement as evidence that two exact Q11-hyperplanes coincide. Even successful global height computation would not prove the complex L'' bridge.

**Provenance and next review:** AI-assisted internal review; no external mathematical peer review. Revisit the full problem by 2026-10-26 or after three mathematical merges. Detailed source and reproduction: [Session 13 note](../anticyclotomic_11/SHADOW_LINES_HEIGHT_IMPLEMENTATION.md), [C-0010](../../CLAIMS.md), [BCLMN arXiv](https://arxiv.org/abs/1610.08729).

---

## Session 14 supplement — WPR-2026-10-19-03

**General BSD:** No new implication is established from Mordell–Weil rank to complex analytic order, no theorem proves the original complex `L''(E,1)=0`, and neither Sha finiteness nor a leading-term BSD formula has been proved. This is an AI-assisted *internal* mathematical review, not peer review. The next whole-problem checkpoint is due by 2026-10-26 or sooner upon meaningful changes.

**What changed:** C-0011 gives exact prime-ideal denominator generators for `A_i=P_i+R` and `2A_i`. A previously tempting uncorrected division-polynomial formula fails primitivity by ideal norm factor 16 for three points; the correct factor 2 is detected by norm-Euclidean gcd. Using BCLMN's explicit anticyclotomic height formula, integral division polynomials, and the universal first sigma coefficient, a standard-library verifier reports *provisional* `h_rho(A_i)=(1,2,7,8) mod 11`. The computation agrees for `2A_i × 18` versus `4A_i × 9` denominator generators and satisfies the 36/72 quadraticity test. **No external Sage/Magma/PARI full height reproduction yet.**

**Falsification decision:** Session 12's speculative local/global kernel-alignment profile was `[1:0:2:9]`. Conditional on the height implementation and normalization, the new *global* first-digit profile is `[1:2:7:8]`. Their second coordinates already differ; thus the *auxiliary alignment conjecture* has serious counterevidence, and should be **killed after** an independent actual height implementation confirms C-0011. The broader H2 derived-height route is not logically ruled out.

**Six-track reorientation:** H1 derived Kato remains blocked by the complex comparison and Sha hypotheses. H2 shifts from assuming local alignment to independently computing genuine global first/derived height radicals and the missing reciprocity bridge. H3 higher geometric third complex derivatives remains the main prospective complex-route leapfrog but lacks a proven theorem. H4 modular congruence route is parked due to circularity risk. H5 numerical central curvature is diagnostic only. H6 geometric projector remains parked without a new period identity.

**Conservative next step:** reproduce one or more anticyclotomic height digits with Sage's actual `padic_sigma(11,...)` and an independent denominator/division-polynomial library, plus a published 389a1 rank-two sample. **Credible leapfrog:** use real derived heights and a separately proved complex comparison theorem if one can be found; do not confuse their output types. **Wild alternative:** find a rank-sensitive geometric operator that annihilates the second complex period, and reject generic Atkin–Lehner/parity restatements.

**Negative controls:** a naive `psi_2(A_i)d(A_i)^4` is integral but nonprimitive at bad prime 2 for three points; the old local-log/height alignment conjecture is actively challenged by different numerical profiles. Exact 11-adic finite digits do not prove complex analytic vanishing.

**References:** [C-0011 audit](../anticyclotomic_11/SESSION14_HEIGHT_MOD11_AUDIT.md), [verifier](../anticyclotomic_11/provisional_height_mod11.py), [BCLMN Proposition 2.4](https://arxiv.org/pdf/1610.08729), [Mazur–Tate sigma Sage docs](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_rational_field.html). The repository's research standards and independent reviewer rules remain mandatory.


---

## Session 15 supplement — WPR-2026-10-19-04

**Goal check:** General Birch–Swinnerton-Dyer, the original rank-four curve's complex \(L''(E,1)=0\), finiteness of Sha and the full leading-coefficient identity are all **still unproved** here. No new theorem about the original complex analytic rank or general BSD has emerged. This is an AI-assisted internal analysis, not independent human review.

**What actually changed since Session 14:** Using a separate affine addition law on the original minimal model, we directly constructed all ten points \([36]Q\) for \(Q\in\{P_i+R,\;P_i+P_j+R\}\). For each we certified both coordinate integrality after multiplication by the candidate \(D^2,D^3\), and *primitivity* through
\(\gcd_{\mathbf Z}(N(x([36]Q)D^2),N(D))=1\). This proves the enormous denominator ideals have no hidden cancellations, independent of the earlier projective group-law route (though the denominator candidates still originate from the same division-polynomial recurrence). Direct minimal-model p-adic substitution reproduces individual C-0011 first digits \((1,2,7,8)\bmod11\). Six genuinely mixed points produce first-digit heights \(3,8,9,9,10,4\), equal to every predicted sum \(h(P_i+R)+h(P_j+R)\). The published 389a1 mod5 height-control has also passed all GitHub CI checks (merged PR #35). These checks materially strengthen **internal** corroboration but do not replace an independent Sage/Magma height algorithm or expert mathematical audit of BCLMN normalization.

**Conditional arithmetic implication:** The nonzero anticyclotomic cross-height vector is \((1,2,7,8)\bmod11\), whereas the two-prime elliptic logarithm vector is projectively \((1,0,2,9)\bmod11\). *If* the published height input and sigma coefficient are correctly specialized, the first-height pairing has rank exactly two on the five-dimensional eigenspace and three-dimensional positive radical. Its mod11 generators are \(P_2-2P_1,\ P_3-7P_1,\ P_4-8P_1\). This provides strong conditional evidence **against auxiliary L11 kernel alignment**, not against BSD, and no exactly 11-adic lift of the radical or higher derived height has yet been calculated.

**Six-track audit:** H1 remains blocked by the complex reciprocity bridge and finiteness assumptions; H2 now has a plausible nontrivial first global height and a concrete *different* radical, but no mixed derived height or complex bridge; H3 stays the leading speculative higher complex-derivative geometry direction without a third-derivative theorem; H4 and H6 remain parked; H5 remains numerical diagnostics. None is promoted to a BSD theorem or mathematical novelty claim.

**Conservative next test:** independently verify the Mazur–Tate sigma power series and BCLMN character/ideal normalization in an external Sage/Magma implementation. **Credible moonshot:** evaluate a genuine derived height on the actual global height radical and find a *noncircular* complex comparison only if available. **Wild alternative:** derive a genuinely rank-sensitive period projector that forces complex second-derivative vanishing and survives rank-two counterexamples.

**Negative controls and stop rule:** nonprimitive bad-2 denominator trap, exact direct-affine ideal primitivity, and six cross-point bilinearity controls all enforced in CI. Stop if a claimed "global height" uses only a local elliptic logarithm or if an auxiliary p-adic statement is substituted for complex \(L''=0\). Next full review by 2026-10-26, earlier for substantive merges.

Source: [Session 14/15 updated audit](../anticyclotomic_11/SESSION14_HEIGHT_MOD11_AUDIT.md), [independent affine/polarization test](../anticyclotomic_11/independent_affine_ideal_and_polarization.py), [published BCLMN method](https://arxiv.org/abs/1610.08729).


---

## Session 16 supplement — WPR-2026-10-19-05

**General BSD and exact logical status (2026-10-19):** Nothing new has proved the missing implication from algebraic rank four to \(L''(E,1)=0\) for the **original complex** L-function of 234446.a1. No analytic rank-four theorem, proof of the correct leading coefficient, finiteness of Sha, or general Birch–Swinnerton-Dyer solution has been obtained. This review is AI-assisted and not independent human expert assessment. Next whole-problem checkpoint due by 2026-10-26 or after three substantive research merges.

**New internal mathematics (C-0012, not a new theorem of BSD):** Derive the sigma-family coefficient \([t^{13}]\sigma_c(t)\) by exact rational formal-group series, prove that the canonical integrality requirement uniquely selects \(c_{11}=4\bmod11\), and independently reproduce the *published* MST E37/p5 \([t^7]\sigma_c\) polynomial and \(c_5=1\bmod5\). Using the BCLMN global anticyclotomic height formula, a now-determined second coefficient \(c_{11}\) gives conditional global self-heights of \(A_i=P_i+R\):
\[
(h_\rho(A_1),\ldots,h_\rho(A_4))\equiv(100,90,7,8)\pmod{11^2}.
\]
Ten complete [36]Q global denominator ideals have exact direct-coordinate primitivity tests; the six mixed Q=P_i+P_j+R heights \((69,107,108,97,98,15)\bmod121\) all satisfy bilinearity. Wrong sigma c=0 preserves first digits but changes the second and is rejected. The normalized projective height vector is **[1:13:40:63] mod121** (earlier hand-computed 25,46,92 was an error, corrected with exact inversion assertions). The local-log profile is [1:99:46:9] mod121. The L11 auxiliary kernel alignment is therefore contradicted already mod11 **conditional on the global-height implementation**, but the entire H2 derived-height/complex comparison program is not falsified.

**H1 derived Kato:** unchanged; no noncircular complex \(L''\) comparison nor required Sha finiteness. **H2 Selmer/Bockstein:** increased arithmetic feasibility; now *conditional two-digit* global first heights and a mod121 positive radical, but no independently maintained Sage/Magma complete height computation, no higher derived height, and no complex reciprocity. **H3 higher Heegner geometry:** continues as a high-upside but unproved route specifically needing a theorem on the third derivative of the **complex weight-two** \(L(E/K,s)\), not a first-derivative or unrelated p-adic theorem. **H4 Mazur–Tate:** parked because of circular BSD assumptions in tempting statements. **H5 numerical curvature:** diagnostics only, no exact complex zero. **H6 geometric period projector:** parked without a genuinely rank-sensitive second-order operator.

**Conservative next test:** calculate \(E_2(11)\), the canonical sigma series and the resulting full \(h_\rho\) vector via an independently maintained Sage/Magma program on the original minimal equation, verifying the actual Hodge/differential convention and all local terms. Our newly reconstructed symbolic MST series and E37 control do not replace this. **Credible leapfrog:** compute the true higher derived p-adic height pairing on the global radical reducing to P2−13P1, P3−40P1, P4−63P1 mod121, then identify (or fail to identify) a theorem to the original complex L''. **Wild route:** independently construct a rank-sensitive operator annihilating the complex second derivative that rank-two controls do not annihilate; no evidence of this operator yet.

**Kill and negative-control gates:** (1) any new Sage sigma discrepancy forces correction of C-0012; (2) a wrong arbitrary Hodge splitting changes second digits and cannot be called canonical; (3) claims that local logs equal global height radicals already disagree modulo 11; (4) a finite mod121 match could never prove exact Q11 equality; (5) an anticyclotomic height, even if fully verified, is not a complex L-function derivative; (6) missing Sha or reciprocity hypotheses may not be silently assumed. Distinguish computations, published theorem assumptions and genuinely missing conjectural arrows.

**Sources and provenance:** [Session 16 audit](../anticyclotomic_11/SESSION16_CANONICAL_SIGMA_MOD121.md), [sigma integrality checker](../anticyclotomic_11/canonical_sigma_integrality_11.py), [ten-point height checker](../anticyclotomic_11/conditional_heights_mod121.py), [MST 2006](https://ems.press/content/book-chapter-files/27479), [BCLMN 2016](https://arxiv.org/abs/1610.08729). No human mathematical peer review.


---

## Session 17 supplement — WPR-2026-10-19-06

**General BSD / exact complex target (2026-10-19):** Nothing has proved the missing implication \(L''(E,1)=0\) for the original complex Hasse–Weil L-function of E=234446.a1. The known four independent rational points and algebraic rank do not by themselves supply the missing complex comparison theorem. No Sha finiteness or leading-term formula has been proved here; no general BSD result, and no human independent expert review.

**New internally reproducible C-0013 subsidiary mathematics:** MST's canonical \(\sigma_c\) integrality constraint at \(t^{23}\) for E forces the uniquely admissible second sigma digit \(c_{11}=26\pmod{121}\), or \(E_2=48\pmod{121}\); an independent published conductor-37, p=5 control likewise yields the known \(c_5=6\pmod{25}\). The exact rational polynomial obeys \(11[t^{23}]\sigma_{4+11k}\equiv8-4k\pmod{11}\), ruling out ten wrong candidates. BCLMN's global-height formula and this sigma input give **provisional** \(h_\rho(P_i+R)=(1068,1300,854,8)\pmod{1331}\), all six mixed-point heights obeying bilinearity, with ten exact primitive denominator-ideal checks. Replacing the sigma coefficient by the stale \(c=4\) preserves lower two height digits but alters third digits, so this tests an actual new sigma datum. The projective height profile is [1:739:766:668] mod1331, whereas the local logarithm profile is [1:704:772:856]. This strongly challenges the *auxiliary speculative* L11 kernel equality, **conditional** on the published normalization and independent package validation, but does not kill the separate H2 derived-height program or touch complex BSD.

**Six-track review:** H1 derived Kato remains blocked by an actual cohomological regulator and complex comparison (and Sha hypotheses). H2 now has a conditional three-digit global first-height functional but neither independent Sage/Magma BCLMN implementation nor a genuine derived-height Bockstein class or noncircular complex comparison. H3 is still the principal speculative route potentially touching original complex L'' via the genuinely *third* complex derivative of weight-two \(L(E/K,s)\); no exact vanishing formula exists in our ledger. H4 Mazur–Tate remains parked due to circularity concerns. H5 central curvature is diagnostics, not proof of exact zero. H6 geometric period projector is parked without a nontrivial operator and rank-two falsification test.

**Conservative next test:** obtain an independently maintained Sage/Magma canonical E2 and sigma calculation on the *original minimal differential*, verifying \(c_{11}=26\bmod121\) and at least one genuine BCLMN anticyclotomic global height. **Credible leapfrog:** determine the higher global height values enough to construct the actual one-prime modified Selmer derived pairing on the Q11 radical reducing modulo1331 to \(P_2-739P_1,P_3-766P_1,P_4-668P_1\). This is still *p-adic* research until a typed explicit reciprocity reaches original complex L''. **Wild route:** an independently proved rank-sensitive complex period identity, challenged against a rank-two curve, remains unconstructed.

**Negative controls and kill gates:** (i) the published E37/p5 sigma second digit is a cross-curve oracle; (ii) wrong \(c=4\) fails only on the new third height digit; (iii) six mixed-input heights must remain additive and all ten exact [36] ideal denominators primitive; (iv) finite mod1331 agreement would not prove an exact Q11 equality; (v) any external full sigma disagreement requires claim downgrading; (vi) no p-adic result may be silently relabeled complex rank or BSD. Next full review due no later than 2026-10-26 or after substantive merges.

**Source and provenance:** [Session17 exact sigma/height audit](../anticyclotomic_11/SESSION17_CANONICAL_SIGMA_MOD1331.md), [canonical second digit](../anticyclotomic_11/canonical_sigma_integrality_121.py), [ten-point height verifier](../anticyclotomic_11/conditional_heights_mod1331.py), [MST2006](https://ems.press/content/book-chapter-files/27479) and [BCLMN2016](https://arxiv.org/abs/1610.08729). Internal AI-authored mathematics and software, not peer review.


### Explicit sigma-convention erratum (2026-10-19, Session 17)

The exact formal-series variable `u` in `sigma_u(z)=sigma_0(z) exp(u z²/2)` equals **E2/12**. PARI `ellpadics2` instead reports the Mazur–Stein–Tate slope **s2=(b2−E2)/12=b2/12−u**. For the target curve b2=−3, series u=26 modulo 121 and independent PARI s2=4 modulo 121, so **E2=70 modulo 121**, correcting the erroneous E2=48 printed in the historical Session17 review. In the published E37/p5 example u=6 and independent PARI s2=19 modulo25. At precision 11, u and s2 accidentally both reduce to 4.

The numeric self-heights were calculated using u in the sigma expansion, not s2, so their provisional residues remain unchanged. Independent PARI sigma agreement does not replace an independent complete global anticyclotomic height computation or provide any complex BSD theorem. Review the executable [PARI oracle](../anticyclotomic_11/pari_canonical_sigma_oracle.gp) and [Session17 audit](../anticyclotomic_11/SESSION17_CANONICAL_SIGMA_MOD1331.md).


---

## Session 18 supplement — WPR-2026-10-19-07

**Scope and truth status:** No progress has proved original *complex* L''(E,1)=0 for E=234446.a1, nor full BSD, Sha finiteness, a derived height or a noncircular comparison theorem. This is AI-authored arithmetic and review, not externally peer-reviewed mathematics. Next review no later than 2026-10-26 or three substantive merges.

**New conditional deduction C-0014:** The independently PARI-checked rational-invariant local elliptic logarithm has primitive projective vector [1:704:772:856] mod1331. The still-provisional global anticyclotomic cross-height functional from C-0011/13 has [1:739:766:668] mod1331. The columns P1,P2 have **unit minor 35≡2 mod11**. Conditional on validating just the global first-height digit, the two honest Z11-linear forms give a **split surjection** from the explicit rank-four Z11 test lattice to Z11², with a **saturated common rank-two kernel**. Its finite-level frame modulo1331 is (20,1103,1,0),(2,842,0,1). The unit condition already holds modulo11 and cannot be repaired by higher-precision corrections. This is elementary linear algebra applied to provisional arithmetic input, not a new general theorem.

**H1–H6 full scan:** H1 remains restricted by unknown Kato comparison and Sha conditions. H2 now has stronger conditional evidence that the local-log and global-height kernels are **integrally transverse rather than equal**, but no verified Selmer-complex identification of their two-dimensional common kernel, no second derived pairing, and no proven map to complex L''. H3 remains a plausible high-upside *complex* base-change third-derivative route but still lacks the necessary independently proved theorem. H4 remains parked due to circularity; H5 remains numerical and cannot prove an exact complex zero; H6 period geometry remains parked without a rank-sensitive exact operator. No track has generated a new theorem forcing original complex L'' vanishing.

**Portfolio decision:** (safe) independently reproduce the *entire* BCLMN global height, not just sigma, with another library or an external arithmetic geometer; (credible) define a precise one-prime Selmer/Bockstein exact sequence and determine **whether** the saturated common kernel even belongs to its domain (it might not); (wild) find a genuine theorem on the third derivative of the *complex weight-two* base-change L-function that survives rank-two countermodels. Stop automatic local-log and sigma-digit upgrades; unit-minor transversality is settled conditional on the first global digit.

**Adversarial checks:** unit determinant, direct modular kernel verification, explicit splitting on arbitrary test outputs, dependent and nearly dependent rows rejected, all-11-scaled height values rejected as nonprimitive. A shared kernel dimension does not imply the same kernel; a conditional two-dimensional intersection is not a Selmer group. Absence of a complex comparison is the central missing arrow.

**Sources:** [Session18 audit](../anticyclotomic_11/SESSION18_TRANSVERSALITY_AUDIT.md), [executable verifier](../methodology/local_global_transversality_11.py), [Session17 provisional heights](../anticyclotomic_11/SESSION17_CANONICAL_SIGMA_MOD1331.md), and all prior claim IDs C-0001 through C-0013. Research novelty has *not* been assessed by independent experts; new-to-this-project calculations are not claims of new globally publishable theorems.


---

## Session 19 whole-problem research pivot — WPR-2026-10-19-08

**General BSD and focal curve (2026-10-19):** **No new implication** establishing original complex \(L''(E,1)=0\), analytic rank four, Sha finiteness or the normalized leading-coefficient equality; no general BSD theorem and no human mathematical peer review. The arithmetic rank-four/anticyclotomic p-adic work remains a useful conditional test, not proof of complex analytic order. Next WPR by 2026-10-26 or upon another three substantive merges.

**Portfolio reset:** We have invested disproportionate effort in the difficult target curve E=234446.a1 and in improving p-adic height precision. The new [theorem-first binding plan](../strategy/THEOREM_FIRST_PIVOT_2026-10-19.md) allocates 45% to rank-two derived Selmer/Kato theorem applicability, 30% to **already proved high-rank BSD** over finite-characteristic function fields, 15% to **independent end-to-end** verification of our rank-four global BCLMN height, and 10% to ambitious exact-complex rank-sensitive geometry. These percentages are relative effort, not chance of success. Two new experiment records EX-010/011 and leapfrogs LF-007/008 enforce their hypothesis gates. Focused next-stage issues [#41](https://github.com/katearline-beep/birchswinnertondyer/issues/41) and [#42](https://github.com/katearline-beep/birchswinnertondyer/issues/42) specify the actual research deliverables.

**New *source-audit* C-0015, rather than a claimed original theorem:** Castella–Hsieh, Forum of Mathematics, Sigma 2022, Theorem A proves nonzero generalized Kato class \(\kappa\) implies \(2\)-dimensional \(p\)-adic Selmer **under every listed condition** (auxiliary adjoint nonvanishing, root sign, ordinarity, residual representation and a squarefree odd number of inert conductor primes with ramification). The standard Kummer inclusion gives Selmer dimension \(\ge4\) for our rank-four E, so if all those conditions hold the particular \(\kappa\) must be **zero**, *not* a new nonzero rank-four class. Our K=-7 fails the odd-inert condition because both 2 and 117223 split, hence the theorem does not apply there. Critically, the same paper's **Theorem 4.1 already develops a derived-height filtration in arbitrary rank** under its own hypotheses, with Theorem 4.5 giving a Coleman-map formula for specified Iwasawa global classes. What is missing is the appropriate **rank-four class** and any original complex comparison, not a general definition of derived heights. [Audit](../proof_labs/RANK_TWO_KATO_THEOREM_SCOPE.md), [program](../proof_labs/kato_rank_scope_gate.py), [primary source](https://doi.org/10.1017/fms.2021.85).

**New *published-theorem laboratory* C-0016:** Ulmer, Annals 2002, proved BSD and exact large ranks over \(\mathbb F_p(t)\) for \(y^2+xy=x^3-t^{p^n+1}\) via Fermat-surface quotients, the Tate conjecture and Gauss sums. The published ranks are \(3\) for \(p=5,n=1,d=6\), \(7\) for \(p=7,n=1,d=8\), and \(25\) for \(p=5,n=2,d=26\). Our independent finite-fibre counting algorithm, *not* Ulmer's proof, verifies point counts two ways and the Hasse bound. The p=5 rank-three and rank-25 examples have **identical \(\mathbb F_5\)-rational finite-fibre counts**, so this local arithmetic cannot diagnose global rank. Ulmer explicitly warns the corresponding \(\mathbb Q(t)\) family has rank **bounded** independently of \(d\). The correct high-level mechanism is exact algebraic-cycle/Tate-to-Frobenius/zeta geometry; transferring it to number fields is a new conjectural challenge, not accomplished here. [Audit](../proof_labs/ULMER_FUNCTION_FIELD_BSD_LAB.md), [program](../proof_labs/ulmer_function_field_fibres.py), [primary source](https://annals.math.princeton.edu/2002/155-1/p09).

**H1–H6 adversarial scan:** H1 Kato is repurposed from conjectural rank-four cohomology precision to a verified *rank-two theorem-scope and exact class* problem; CH Theorem A's nonvanishing route is blocked in rank four. H2 global height C-0011/13 remains provisional; independent PARI sigma does not validate all global ideal/character terms and we stop precision-only upgrades. H3 complex third-derivative geometry remains speculative at a small 10% effort until an actual theorem statement arises, not a first-derivative identity in disguise. H4 Mazur–Tate congruences remain parked due to circular assumptions. H5 complex curvature diagnostic remains exact-zero-inconclusive. H6 projector remains parked without a nontrivial rank-sensitive operator. The new function-field proof lab is **not** a claim that an H1–H6 arrow to original complex BSD was found.

**Safe next lemma:** instantiate a genuine published rank-two CH appendix example and write a typed proof-obligation diagram for derived Selmer filtration, Iwasawa class and Coleman map. **Credible leapfrog:** reconstruct Ulmer's *actual* Fermat quotient for the small p=5,d=6 curve and one global Gauss-sum zeta factor, then test a precisely specified cycle-comparison conjecture in characteristic zero. **Wild option:** an exact complex period or third-derivative construction that distinguishes analytic rank two from four and survives a rank-two countermodel. No such complex theorem presently exists in our materials.

**Negative controls/stop rules:** CH Theorem A's rank-two nonzero κ cannot certify rank four; K=-7 fails its odd-inert hypothesis. Theorem 4.1's arbitrary-rank height filtration is already published; do not reinvent it. Two Ulmer curves have equal *local* finite-fibre traces despite different *global* ranks. Do not transport Frobenius/Tate BSD proofs to complex Hasse–Weil Taylor coefficients or infer general BSD. Distinguish an independently published theorem from our elementary reproduction and from speculative conjectural transfers. No more automatic 11-adic digits without a named comparison hypothesis or independent complete height certification.

**Sources:** [Theorem-first program](../strategy/THEOREM_FIRST_PIVOT_2026-10-19.md), [Castella–Hsieh 2022](https://doi.org/10.1017/fms.2021.85), [Ulmer Annals 2002](https://annals.math.princeton.edu/2002/155-1/p09), [GitHub issues #41](https://github.com/katearline-beep/birchswinnertondyer/issues/41) and [#42](https://github.com/katearline-beep/birchswinnertondyer/issues/42). **New direct progress on the central complex rank-four implication: none.**
