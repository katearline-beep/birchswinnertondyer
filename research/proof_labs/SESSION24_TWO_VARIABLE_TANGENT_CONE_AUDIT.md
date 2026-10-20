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


## 6. Published base-field weight-control sequence: the obstacle is narrower

A further primary-source check of **Howard §3.4, proof of Corollary 3.4.3**, reveals an explicit control sequence we must **not** pretend is missing at the *base field*. If \(\mathfrak p\subset R\) is a weight arithmetic prime, Nekovář's Selmer-complex specialization gives, after localization at \(\mathfrak p\),
\[
0\longrightarrow
\frac{\widetilde H_f^1(K,T^\dagger)_{\mathfrak p}}
     {\mathfrak p\,\widetilde H_f^1(K,T^\dagger)_{\mathfrak p}}
\longrightarrow
\widetilde H_f^1(K,V^\dagger_{\mathfrak p})
\longrightarrow
\widetilde H_f^2(K,T^\dagger)_{\mathfrak p}[\mathfrak p]
\longrightarrow0.
\]
**This is a published INJECTION for weight specialization at \(K\)**, under the source's localization/setup. The last \(H^2[\mathfrak p]\) is a **cokernel**, not a kernel that makes the first arrow noninjective. It does not require us to postulate arbitrary failure of weight-control at base \(K\).

**Exact remaining boundaries:** (i) this is the **base-field** weight-only specialization for \(\widetilde H_f^1(K,T^\dagger)\), NOT a verified simultaneous weight-plus-anticyclotomic specialization of the inverse-limit \(\widetilde H^1_{f,\mathrm{Iw}}(D_\infty,T^\dagger)\); (ii) mapping a specialized extended Selmer class into a *particular observed classical Kummer point* involves the correct normalization and comparison; (iii) knowing that this base Kummer observation is zero does not, without a fully verified identification, show \(Z_\infty\in(W,T)M\) or \(Z_{\mathrm{wt2}}\in T M_{\mathrm{wt2}}\).

Accordingly, the noninjective control **toy counterexample in §3 is not a purported counterexample to Howard's actual base-field injection**; it shows exactly why that *published injection* or its analog must be verified at the **different** Iwasawa/simultaneous specialization arrow before promoting a divisibility claim. This refinement **reduces the open proof obligation** to a new finite-to-infinite compatibility/control calculation, not discovering a base-weight injection from scratch.

**Next decisive experiment upgraded:** Source-audit the Iwasawa-theoretic analogue of the displayed exact sequence for \(D_\infty/K\), including the order of specializing and taking inverse limits, the \(H^2\)-torsion/derived tensor terms, and which local Greenberg conditions are preserved. An actual statement in this direction could convert the forced torsion classical Heegner point into *rigorously controlled* augmentation information; until then the first two-variable jet remains unknown.


## 7. Higher-upside conditional consequence: a horizontal *weight*-derived base class

The same source creates a **genuinely curve-directed leapfrog** when combined with C-0021. Howard §3.4 proves the *base-\(K\)* **weight-specialization injection** written in §6. Under the additional **unverified** identification of the specialized \(Z_0\) with the classical traced Heegner Kummer class (with its specific Euler/unit normalization), Kolyvagin's theorem forces the image of \(Z_0\) in \(\widetilde H^1_f(K,V^\dagger_{\mathfrak p})\) to be zero, because \(P_K\) is torsion. Injectivity would imply
\[
\boxed{Z_0\in\mathfrak p\,\widetilde H^1_f(K,T^\dagger)_{\mathfrak p}.}
\]
This is a *conditional divisibility statement about the base-field Hida-weight class*, **not** about \(Z_\infty\) being divisible by the **anticyclotomic** augmentation \(T\), and **not** claimed unconditionally until the specialized \(Z_0\leftrightarrow P_K\) normalizations are inspected. In particular, we have not computed \(Z_0\).

Now also assume Howard's still-unproved **Conjecture 3.4.1** (\(Z_0\) is non-\(R\)-torsion), a discrete-valuation/regular local weight parameter \(\pi\) at \(\mathfrak p\), and finite torsionfree/separated local Selmer module \(M\) with \(\bigcap_{n\ge0}\pi^nM=0\). Then \(Z_0\neq0\) and \(\pi\mid Z_0\), so there is a **finite** \(r\ge1\) with
\[
Z_0\in\pi^rM\setminus\pi^{r+1}M.
\]
Its leading quotient determines a **nonzero weight-leading graded class**
\(\operatorname{gr}_\pi^r(Z_0)\in\pi^rM/\pi^{r+1}M\); after choosing a uniformizer, the divided representative \(\pi^{-r}Z_0\bmod\pi M\) is meaningful up to unit scaling. This is **elementary DVR module algebra**, not a theorem that Howard's \(\mathfrak p\)-local Heegner class actually satisfies all premises, or that its weight derivative is nonzero at order exactly one.

**Why it could bear fruit:** A source-normalized *horizontal Hida-weight* leading term is a more logically justified alternative than assuming a first anticyclotomic derivative. It leverages an EXISTING injection, the known rank obstruction, and a specific published (but unproved) horizontal conjecture. The next falsifying experiment is therefore **the exact equality of the specialized Howard \(Z_0\) and the p-stabilized classical Kummer \(P_K\)**, followed by local regularity and the horizontal non-torsion condition. If any premise fails, do **not** promote the deduction. Even when they hold, a new derived reciprocity and independently proved **original complex** \(L''\) comparison are still missing.

This conditional horizontal lemma complements—not replaces—the two-variable \(Z_\infty\) experiment. Crucially a weight-leading base class need not induce any anticyclotomic leading jet of \(Z_\infty\) after weight-two specialization.
