# Session 24 — The two-variable tangent-cone leapfrog: where Howard nonvanishing stops

**2026-10-19; theorem-first research, AI-assisted, not human peer-reviewed.** This is a *new-to-project logical and methodological deduction*, not a computed Heegner class, original theorem about elliptic curves, or proof of BSD.

**Primary references (source checked):** Howard, [*Variation of Heegner points in Hida families*](https://arxiv.org/pdf/1202.6358), especially **§1, Corollary 3.1.2, §§3.3–3.4 and Conjectures 3.3.1/3.4.1**; Castella–Hsieh, [*On the non-vanishing of generalised Kato classes for elliptic curves of rank 2*](https://web.math.ucsb.edu/~castella/Kato.pdf), §4.5.

## 1. A crucial quantifier distinction in the primary source

Howard constructs a norm-compatible class
\[
Z_\infty\in \widetilde H^1_{f,\mathrm{Iw}}(D_\infty,T^\dagger)
\]
over **the two-variable** Iwasawa algebra \(R_\infty=R[[\Gamma_{\rm ac}]]\), where \(R\) parametrizes a Hida-family branch. By Corollary 3.1.2, **Howard §3.3 says \(Z_\infty\) is not \(R_\infty\)-torsion**. Importantly, this is not a theorem that its **weight-two specialization** is nonzero at the base anticyclotomic augmentation, or that its 11-adic Coleman images are nonzero to a determined order. Howard calls **non-\(R\)-torsion of the base class \(Z_0\)** *Conjecture 3.4.1* rather than a theorem.

For our particular E=234446.a1 over \(K=\mathbb Q(\sqrt{-7})\), Kolyvagin plus the known four independent rational points force the *classical base Heegner point* to be torsion (C-0021). Howard's nonexceptional coefficient specialization and extended/strict-Greenberg comparison are published; **the precise identification of the resulting zero rationalized base Heegner Kummer image with the augmentation of \(Z_\infty\)** still requires source-matched critical-twist and local-control normalization, and we have not verified that equality. Even if granted, **base-zero is weaker than weight-two-Iwasawa-zero or a nonzero derived class**.

## 2. The leapfrog candidate: two-variable leading terms, not assumed anticyclotomic order one

Suppose, **conditionally**, that the local Hida branch \(R\) is regular/smooth at the weight-two point, with a chosen weight coordinate \(W\), that \(\Gamma_{\rm ac}\cong\mathbb Z_{11}\) has a fixed generator \(\gamma\) and parameter \(T=\gamma-1\), and that the relevant class lives in a **torsion-free/controlled** \(R_\infty\)-module \(M\). Work locally over \(\mathcal O[[W,T]]\) (or after rationalizing over \(\mathbb Q_{11}\)); let \(\mathfrak m=(W,T)\). Under additional **injective base-control** and genuinely vanishing class in \(M/\mathfrak mM\), one may consider the first nonzero leading term of \(Z_\infty\) in
\[
\mathfrak m^rM/\mathfrak m^{r+1}M
\cong \operatorname{Sym}^{r}(\mathfrak m/\mathfrak m^2)\otimes M/\mathfrak mM
\]
when \(M\) is locally free and the standard associated-graded comparison holds. None of these conditions has yet been demonstrated on the actual Howard module at the focal arithmetic prime. Without them **the expression above is a candidate template, not a proved isomorphism**.

A base-zero class could have **weight-leading** term \(W\), **anticyclotomic-leading** term \(T\), a genuinely higher term \(T^2\), or a mixed term \(WT\). Its nonzero two-variable generic fiber does **not** select one of those. If the leading term is pure weight \(W\), specializing \(W=0\) kills it: an anticyclotomic Coleman derivative will not recover a first-order signal from that term.

The potentially useful high-risk idea is to **classify the leading tangent cone first**, and only then select an anti-direction \(T\)-derived Selmer class or, if all anti terms vanish, a *weight-derivative* construction with its own separately proved reciprocity. A weight derivative is not automatically a valid Selmer class. The decomposition depends on the Hida coordinate and fixed anticyclotomic generator; invariant assertions should concern the appropriate filtered class and separately normalized tangent directions.

## 3. Exact fail-closed algebraic experiment, including control obstructions

The [self-contained standard-library experiment](two_variable_heegner_specialization_controls.py) computes in the *toy truncated ring* \(\mathbb F_{11}[W,T]/(W,T)^5\). This is **not** the actual coefficient ring nor an implementation of the Howard class. It is a controlled **logical countermodel** to overconfident transfer claims:

| Toy big class | Base value | Weight-two specialization (\(W=0\)) | First-order two-variable direction |
|---|---|---|---|
| \(W\) | 0 | **0 identically** | weight |
| \(T\) | 0 | \(T\) | anticyclotomic |
| \(T^2\) | 0 | \(T^2\) | none (second order) |
| \(W+T\) | 0 | \(T\) | mixed |
| \(WT\) | 0 | **0 identically** | none (second order) |

In particular, a nonzero class over a two-variable domain may specialize to the **zero** entire weight-two family, even though its base is zero for the trivial reason. Its \(\mathfrak m\)-order and specialized \(T\)-order can differ: e.g. \(W+T^2\) has total order one but specialized \(T\)-order two.

Three additional independent negative controls guard the *cohomology* reasoning:

1. **Noninjective base-control trap:** In \(M=Ae_1\oplus Ae_2\), a base cohomology observation \((u,v)\mapsto u(0,0)\) sends \(e_2\) to zero while \(e_2\notin\mathfrak m M\). **Zero observed Kummer class does not imply ideal divisibility** unless the actual control map is injective on the relevant specialization.
2. **T-torsion/derived class nonuniqueness:** In \(M=Ae\oplus (A/(T))f\), the same \(Te\) is divisible by \(T\) as \(T(e)\) or \(T(e+f)\). The two divided classes differ at augmentation. To define a canonical \(T\)-derivative in a Selmer module, verify torsion/control/choice independence (or a derived Bockstein in a correct exact triangle).
3. **Both local Coleman maps:** An arbitrary nonzero global class can lie in the common kernel of two local maps, and the two maps can have **different augmentation orders**. Castella–Hsieh Theorem 4.5 requires **both** \(\mathrm{Col}_\eta(\operatorname{Loc}_{\mathfrak p}z)\) and its conjugate to lie in \(J^r\). One zero or one precision result does not validate a positive derived regulator.

The code also checks parameter specialization, first jets, and a case where specialization increases the minimal order. Its coefficient ring is \(\mathbb F_{11}\), so passing cannot prove an 11-adic integrality or torsion statement about real cohomology.

## 4. Decision gates — what to test and what kills the leapfrog

**Conservative theorem gate:** Identify the precise localized Hida branch \(R\) near the original weight-two ordinary eigenform and prove the smoothness/regularity (or use the actual nonregular cotangent complex rather than pretending \(R\simeq\mathcal O[[W]]\)). Identify the Howard module \(M=\widetilde H^1_{f,\mathrm{Iw}}(D_\infty,T^\dagger)\), its Tor/specialization control exact sequence, and whether nonzero Howard \(Z_\infty\) gives a nonzero *weight-two anticyclotomic* class. Use Howard's **published** \(Z_\infty\), Lemma 2.4.4, and Conjecture 3.4.1 with correct theorem/conjecture labels.

**First decisive leapfrog test:** Determine the **two leading coefficients** of the relevant class, or of **both** source-normalized Coleman image series, along (i) the weight direction and (ii) the anticyclotomic augmentation direction. Prefer a theorem implying one direction is zero/nonzero over unsupported extra numerical digits. The weight-direction may be nonzero even when anticyclotomic specialization has no leading term; the reverse is also possible.

**Falsifiers/kill gates:** Park the specific two-variable derivative conjecture if the required localized module is not flat/controlled, its projection is not injective, the relevant first-jet class is killed by the appropriate local Coleman maps, or the supposed higher Bockstein depends on a noncanonical choice. If the only obtained result concerns a \(p\)-adic \(L\)-function rather than the **original complex** \(L''(E/\mathbb Q,1)\), record useful arithmetic progress but no analytic-rank breakthrough.

**Wild bridge hypothesis (strictly speculative):** A *new* rank-sensitive reciprocity/leading-term theorem could potentially identify the first nonzero well-defined weight/anticyclotomic mixed derivative with an independently defined derived Selmer regulator, and ultimately connect a specific component to complex Hasse–Weil Taylor data. We do not have this theorem; even a nonzero two-variable first jet would **not** by itself establish \(\operatorname{ord}_{s=1}L(E,s)\ge4\).

## 5. New progress versus the original BSD goal

What is **actually** new to our project: a source-grounded shift from an unsupported one-direction derivative assumption to a two-variable tangent-cone program with four precise logical counterexamples, a cohomology-control no-go, and an explicit construction/falsification checklist. These are standard algebraic observations, **not** novel publishable theorems.

What remains unproved: a nonzero weight-two Howard \(Z_\infty\) specialization, exact leading jets/augmented Coleman images, a higher derived Selmer class, comparison with BCLMN numerics or CH \(h^{(r)}\), original complex \(L''(E/\mathbb Q,1)=0\), Sha finiteness and full/general BSD.

**Cross-discipline methodology:** use two-variable deformation theory (tangent cones/flatness), singularity-theoretic associated graded structures, and software negative controls to find hidden category errors before attempting elliptic-curve theorems. The *biological/physical intuition* is only heuristic: a two-control-parameter system can be invisible along one slice despite meaningful variation in another. No biological/physical model is mathematical evidence here.
