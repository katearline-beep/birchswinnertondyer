# Session 25 leapfrog — a canonical nonzero **divided GLOBAL Iwasawa cohomology class**

**2026-10-19. Source-derived existence via a standard long exact sequence (not a computed point or derived Selmer height).** This improves the zero-base audit in [Session25](SESSION25_HOWARD_ZERO_AUGMENTATION_AUDIT.md). Original complex BSD remains **completely open**.

## The four ingredients and their exact proof domains

Let \(\Gamma=\mathrm{Gal}(D_\infty/K)\cong\mathbb Z_{11}\), \(\Lambda=\mathbb Z_{11}[[\Gamma]]=\mathbb Z_{11}[[T]]\) with \(T=\gamma-1\). Fix the **integral** 11-adic Tate lattice \(T_{11}E\) of original \(E=234446.a1\) over \(K=\mathbb Q(\sqrt{-7})\) (and a commensurable lattice for Howard's weight-two p-stabilized representation). Use the *integral compact* module
\[
M=H^1_{\mathrm{Iw}}(D_\infty/K,T_{11}E)
 = \varprojlim_s H^1(D_s,T_{11}E)
 \simeq H^1(G_{K,S},\Lambda^\#\widehat\otimes_{\mathbb Z_{11}}T_{11}E),
\]
where standard Shapiro's lemma and the cohomological finite-ramification setup supply the isomorphism. We may invert 11 **after** building the integral inverse limit; taking an inverse limit of separate \(\mathbb Q_{11}\)-vector spaces and replacing it naively by \(\mathbb Q_{11}[[T]]\) can have different integrality/topology! Weight-two Howard classes map into a single commensurable integral lattice after one **uniform** 11-power scaling; no claimed explicit coordinate or denominator.

**1. Zero base augmentation (published, proved in the preceding Session25 audit).**
Howard Proposition 2.3.1 and §3.3 give the exact norm relation
\[
\mathrm{pr}_K(Z_\infty)=U_{11}X_1,
\]
NOT simply \(X_1\). Castella Theorem6.5/Rem6.6 gives \(\nu_2(X_1)=(1-\alpha^{-1})^2\kappa(P_K)\), and Kolyvagin plus \(\mathrm{rank}E(K)\ge4\) forces \(P_K\) torsion. Thus the specialized \(z:=\nu_2(Z_\infty)\) has
\[
\mathrm{pr}_K(z)=0\in H^1(K,V_{11}E).
\]
Residual absolute irreducibility of \(E[11]|_{G_K}\) (C-0020) additionally implies \(E[11](K)=0\), hence \(H^1(K,T_{11}E)\) has no 11-torsion (from the ordinary coefficient short exact sequence and \(H^0(K,E[11])=0\)). Thus an integral representative of this rationally-zero base class is actually zero after a fixed scaling into the lattice.

**2. The weight-two anticyclotomic tower is NONZERO, via *trivial torsion-character* deep-level nonvanishing.**
Howard **Theorem 3.1.1/Corollary 3.1.2** asserts that for **every** arithmetic specialization \(\nu\) and each torsion character \(\chi\) of \(G_{\mathrm{tors}}=\mathrm{Gal}(H_{11^\infty}/D_\infty)\), including **the trivial character**, the \(\chi\)-projected \(X_{11^n}\) is nonzero in rationalized \(11\)-adic Greenberg Selmer at sufficiently deep \(n\).

For this \(K\), \(G_{\mathrm{tors}}\simeq C_{10}\), and \(D_{n-1}=H_{11^n}^{C_{10}}\) by the exact split-p ring-class computation C-0021. In group cohomology,
\[
\operatorname{res}_{H_{11^n}/D_{n-1}}
\circ\operatorname{cor}_{H_{11^n}/D_{n-1}}(x)
=\sum_{\delta\in C_{10}}\delta x=10e_{\rm triv}x.
\]
If \(e_{\rm triv}\nu_2(X_{11^n})\ne0\), the corestricted class **cannot** be zero (regardless of any injectivity claim for restriction), and ordinary \(U_{11}^{-(n-1)}\) is a nonzero unit. Hence the weight-two specialized Howard component \(z_{n-1}\) is **nonzero** for sufficiently deep \(n\). Therefore
\[
\boxed{z=\nu_2(Z_\infty)\ne0\quad\text{as an integral/commensurable rationalized GLOBAL Iwasawa }H^1\text{ class}.}
\]
This nonzero statement is substantially stronger than generic big \(R_\infty\)-nontorsion alone, which would NOT rule out an identically-zero weight-two fiber. We have used the **trivial torsion-character** case of Howard's independent *vertical nonvanishing*, not §3.4's still-unproved **horizontal** non-torsion Conjecture 3.4.1.

**3. Canonical division by \(T\) follows from an ACTUAL cohomology long exact sequence.**
Write \(\mathbb T=\Lambda^\#\widehat\otimes T_{11}E\). Multiplication by \(T\) on this coefficient module is injective, giving
\[
0\to \mathbb T\xrightarrow{T}\mathbb T\to T_{11}E\to0.
\]
The Galois-cohomology long exact sequence has
\[
H^0(K,T_{11}E)\to M\xrightarrow{T}M\xrightarrow{\mathrm{pr}_K}H^1(K,T_{11}E).
\]
Since \(E(K)[11^\infty]\) is finite (Mordell–Weil) and has no nonzero Tate module, \(H^0(K,T_{11}E)=0\); stronger, \(E[11](K)=0\) by C-0020. Thus multiplication by \(T\) on \(M\) is **injective**, and
\[
\ker(\mathrm{pr}_K)=T M.
\]
Because \(\mathrm{pr}_K z=0\), **there exists exactly one** \(\tilde z_1\in M\) satisfying
\[
\boxed{T\tilde z_1=z.}
\]
The nonzero \(z\) from step 2 implies **\(\tilde z_1\ne0\)**. This constructs a genuine **nonzero canonically \(T\)-divided global Iwasawa Galois cohomology class** from published classes and standard long exact-sequence algebra, with no guessing of an anticyclotomic first coefficient.

**Scope boundary:** We have not shown that the *base projection* \(\mathrm{pr}_K(\tilde z_1)\) is nonzero; it may itself vanish, requiring further division. We have not proved the actual \(\tilde z_1\) belongs to a chosen **Selmer** Iwasawa module or that its localization satisfies the exact Greenberg conditions after division. For that one must inspect possible \(T\)-torsion in the **local-quotient cohomology** defining Selmer, especially at the two split primes above11 and bad conductor primes. Without that check, do not call \(\tilde z_1\) a nonzero *derived Selmer point*, or equate it with Castella–Hsieh's \(S^{(r)}\) or a height vector. Neither its Coleman outputs nor any original COMPLEX Taylor coefficient are computed.

**4. The source's local ordinary data may make the Selmer gate tractable.**
At \(p=11\), \(E\) has \(\alpha\equiv5\not\equiv\pm1\), and Howard Lemma2.4.4 identifies finite-level extended with Greenberg Selmer, while the ordinary rank-one unramified \(F^-V\) has no invariants over base \(K_{\mathfrak p}\). This suggests that multiplication by \(T\) may be injective on the relevant **p-local Greenberg quotient cohomology**, preserving local conditions after division, but the global norm-compatible local tower and all other local conditions still require a SOURCE-LEVEL exact-sequence proof. Treat this as the **next open lemma**, not already established.

## Leapfrog and failure tests

The [source-hypothesis/trivial-character exact verifier](howard_bockstein_exact_sequence_gate.py) checks explicit \(C_{10}\) trace/projector arithmetic, including the nontrivial-character **counterexample** (a globally nonzero character component whose norm is zero), and tests the algebraic injectivity/uniqueness logic in truncated \(\mathbb F_{11}[[T]]\) with a deliberate torsion-failure mutation. The finite polynomial script is NOT an implementation of Galois \(H^1\), and the proof of long exactness and Howard deep-level nonvanishing come from **published** inputs.

**High-flyer hypothesis LF-010:** If \(\tilde z_1\) (or its first further divided class with nonzero augmentation) can be shown to satisfy a **canonical derived Greenberg Selmer local condition** and if the two CH4.5 Coleman maps can be normalized on that class with a nonzero coefficient, we gain a genuine rank-sensitive derived regulator candidate. We still require a separately PROVED original **complex** \(L''(E/\mathbb Q,1)\) comparison; p-adic height nonzero alone will not prove BSD.

**Kill:** If local-quotient \(T\)-torsion prevents Selmer condition propagation, park the derived **Selmer** claim but retain the genuine global cohomology division. If the divided class is zero at base, repeat the controlled global cohomology division only if precise augmentation control and nontriviality remain; never assert first-order nonvanishing without observing it. If the source weight-two projector for the trivial \(C_{10}\)-character has an overlooked local normalization, correct/withdraw the NONZERO class claim.

**Zero proof-status changes:** No proof of exact analytic rank four, original complex \(L''(E/\mathbb Q,1)=0\), \(\Sha\) finiteness, BSD leading term or general BSD.
