# Session 24 addendum — Castella's published weight-two identity closes the base specialization gap

**19 October 2026 — theorem-led deduction for focal E=234446.a1, not a new theorem about BSD.** Primary source: Francesc Castella, [*On the \(p\)-adic variation of Heegner points*](https://web.math.ucsb.edu/~castella/Heegner.pdf), **Theorem A / Theorem 6.5, Remark 6.6 and Theorem B / 5.3**. Howard, [*Variation of Heegner points in Hida families*](https://arxiv.org/pdf/1202.6358), proof of Corollary 3.4.3 and §3.3. Kolyvagin's classical Heegner theorem as already used in C-0021. External independent mathematical peer review has **not** occurred.

## An actual theorem identity, rather than the previously missing conjectural normalization

Castella's **Theorem A** gives, for a p-ordinary \(p\)-stabilized form \(f\) of even weight \(2r\), a comparison of Howard's base-class specialization with the étale Abel–Jacobi Heegner cycle:
\[
\nu_f(Z_0)=
(1-p^{r-1}/\alpha_p)^2\;
\frac{\Phi^{\mathrm{ét}}_{f,K}(\Delta^{\mathrm{heeg}}_r)}
{u_K(2\sqrt{-D_K})^{r-1}}.
\]
Crucially, **Remark 6.6 explicitly extends the argument to weight two**, \(r=1\), trivial nebentype, **when \(f\) is the ordinary \(p\)-stabilization of a form of level prime to \(p\)**. The right-hand Heegner-cycle class then is the Kummer image of a **classical Heegner point**. This is no longer an open normalization gap; it is a **published theorem**, subject to its hypotheses. The equivalence requires its genuine p-stabilization, not the \(p\)-new exceptional case excluded in Remark 6.6.

### Hypothesis check on our curve

Take
\[
E:\ y^2+xy=x^3-x^2-79x+289,\quad
N=2\cdot117223,\quad K=\mathbb Q(\sqrt{-7}),\quad p=11.
\]
Castella introduction/ThmA needs \(p\nmid6N\), Heegner splitting at all primes dividing \(N\), good ordinary at \(p\), residual irreducibility **restricted to \(G_K\)**, mod-\(p\) \(p\)-distinguished ordinary Galois representation, and residual ramification at any non-split bad prime.

All are satisfied for the original curve using the **already exact** certificates:
- \(p=11\) good ordinary, \(a_{11}=-6\), so unit root \(\alpha_{11}\equiv5\pmod{11}\) of \(X^2+6X+11\). The original newform has level \(N\) **prime to 11**, and hence an ordinary \(11\)-stabilization.
- Both bad primes 2 and 117223 **split** in \(K\); the source's residual ramification-at-nonsplit-primes condition is **vacuous**, and \(D_K=7\) is odd, greater than 3 and coprime to \(11N\).
- The split good Frobenius primes 23 and 43 give mod11 discriminants 10 (nonsquare) and 9 (nonzero square), respectively. This certifies **absolute irreducibility even on \(G_K\)**, as recorded in C-0020.
- For a good ordinary weight-two elliptic curve with \(p>2\), ordinary residual inertia has an unramified one-dimensional quotient and a cyclotomic determinant on the other graded character. Since the mod11 cyclotomic inertia character is **nontrivial**, these two characters are **distinct**: the source's **\(p\)-distinguished** requirement holds.

For \(r=1\), \(u_K=|\mathcal O_K^\times|/2=1\) and \((2\sqrt{-D_K})^{r-1}=1\). Therefore Castella's source identity simplifies exactly to
\[
\boxed{\nu_f(Z_0)=(1-\alpha_{11}^{-1})^2\,\kappa(P_K),}
\]
where \(P_K\) denotes the classical Heegner point and the scalar normalization is that in the published theorem. The exact local factor is a unit:
\[
\alpha_{11}\equiv5,\quad1-\alpha_{11}^{-1}\equiv3,\quad
(1-\alpha_{11}^{-1})^2\equiv\boxed9\pmod{11}.
\]
The [stdlib independent prerequisite test](castella_howard_weight_prime_gate.py) verifies local coefficients, unit factor, Heegner splitting, residual Frobenius distinctions, and the theorem-logic hypotheses. It does **not** independently compute the cohomology class \(\nu_f(Z_0)\).

## Unconditional divisibility of the base-class weight specialization (source-dependent theorem consequence)

Classical Kolyvagin theory implies \(P_K\) is torsion since \(E(\mathbb Q)\) has four independent points and hence \(\operatorname{rank}E(K)\ge4>1\). Therefore its **rationalized** Kummer image is zero, and the Castella **published** identity implies
\[
\boxed{\nu_f(Z_0)=0\in\widetilde H_f^1(K,V^\dagger_{\mathfrak p}).}
\]

Next Howard, **proof of Corollary 3.4.3**, quotes Nekovář's control exact sequence for the arithmetic prime \(\mathfrak p\):
\[
0\to
\widetilde H_f^1(K,T^\dagger)_{\mathfrak p}/
\mathfrak p\widetilde H_f^1(K,T^\dagger)_{\mathfrak p}
\overset{\mathrm{injective}}{\longrightarrow}
\widetilde H_f^1(K,V^\dagger_{\mathfrak p})
\to \widetilde H_f^2(K,T^\dagger)_{\mathfrak p}[\mathfrak p]
\to0.
\]
**The \(H^2[\mathfrak p]\) contribution is a cokernel, not a kernel.** It follows, without appealing to Howard's horizontal non-torsion conjecture or an unverified *Iwasawa-level* control, that
\[
\boxed{Z_0\in\mathfrak p\,\widetilde H_f^1(K,T^\dagger)_{\mathfrak p}.}
\]

This is a real source-dependent **arithmetic implication about the original rank-four curve**, not a calculation of a nonzero derived point. It means **weight-prime divisibility of Howard's big base class**, and must **not** be confused with divisibility of the anticyclotomic \(Z_\infty\) by \(T=\gamma-1\).

A **nonzero** leading weight derivative is *not proved*. If Howard's **still unproved Conjecture 3.4.1** asserts \(Z_0\) non-\(R\)-torsion and the localized weight Selmer module is finite and separated over a DVR with chosen uniformizer, elementary DVR algebra would guarantee a finite first nonzero weight-graded order \(r\ge1\). Neither the conjecture nor the exact value of \(r\) follows from the identities above.

## Castella already proves the relevant two-variable p-adic reciprocity

Castella **Theorem B (Theorem 5.3)** constructs a Perrin–Riou *big logarithm* on the localizations of a twist of Howard's big anticyclotomic class and proves an **explicit reciprocity law**
\[
\mathcal L^\Gamma_{\omega_f}
 \bigl(\operatorname{res}_{\mathfrak p}(Z_\infty^{\xi^{-1}})\bigr)
 =L_{p,\xi}(\mathbf f)\,\sigma_{\mathfrak p}^{-1}
\]
(in the source's localized coefficient ring and reciprocity normalization). This is **already proved**, not a conjectural map to invent. Its hypotheses and localization factors must be matched to our focal curve.

**Crucial scope:** This is a **two-variable \(p\)-adic** reciprocity identity. Castella–Hsieh Theorem 4.5 requires the correct **two local/conjugate Coleman \(J\)-orders** and a class in its chosen compact cohomology setting; an explicit equality at one local prime is valuable, but **not by itself** a calculation of either required \(J\)-adic order or a nonzero derived Selmer regulator. It is even further from the missing exact **original complex** \(L''(E/\mathbb Q,1)=0\) comparison.

## What the next actual research problem has become

**Safe:** Source-match Castella's two-variable big logarithm to the **two split-11 local Coleman maps** in Castella–Hsieh, including critical twist/character \(\xi\), and verify all Euler denominators and local conditions for this original curve.

**Leapfrog:** Given **proved weight-prime divisibility of \(Z_0\)**, try to obtain a nonzero *higher weight derivative* via Howard horizontal Conjecture 3.4.1 or a new direct computation of a localized Hida-weight logarithm. Independently test the two-variable anticyclotomic \(L_{p,\xi}\) leading Taylor terms using Castella's **already proved** identity; no assumption that the first anti coefficient is nonzero.

**Kill criteria:** If the horizontal class is \(R\)-torsion or localized module unseparated/singular, no nonzero horizontal derivative is established. If local big logarithm requires inversion of a vanishing local Euler factor, isolate and prove any exceptional zero correction first. **Never** treat nonzero p-adic leading term as a proof of the original complex \(L''\) without a separately established analytic comparison.

**Strict nonclaims:** No actual coefficient of \(Z_\infty\), \(Z_0/\pi\) or \(L_{p,\xi}\) has been computed, and no first nonzero derivative order is proved. No original complex analytic rank four, Sha finiteness, BSD leading term or general BSD theorem follows.
