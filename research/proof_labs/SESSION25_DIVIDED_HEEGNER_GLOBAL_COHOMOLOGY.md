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


---

## Session25 source/LES upgrade C-0026 — the first divided class DOES preserve strict Greenberg local conditions

The prior audit stated Selmer local condition preservation as the next unproved test. That test **can be closed directly from Howard's published Definition2.4.2/Proposition2.4.5**, the unramified-away-from-11 nature of the anticyclotomic tower and *two short cohomology long exact sequences*. This does **NOT** prove nonzero base projection or a derived regulator.

Howard **Definition2.4.2** defines strict Greenberg local condition on a module \(A\):

- \(v\mid11\): \(\ker(H^1(K_v,A)\to H^1(K_v,F^-A))\), with ordinary rank-one unramified quotient \(F^-\).
- \(v\nmid11\): \(\ker(H^1(K_v,A)\to H^1(I_v,A))\), where \(I_v=\operatorname{Gal}(\overline{K_v}/K_v^{\rm unr})\).

Howard **Proposition2.4.5**, since \(N\) and \(\operatorname{disc}K=-7\) are coprime, guarantees the \(X_{11^n}\) lie in strict Greenberg Selmer **without multiplying by a further \(\lambda\)**. Weight-two specialization respects these local conditions (Howard Lemma2.4.4), as do the source's ordinary \(U_{11}\)-renormalization and corestriction.

Let \(A=\Lambda^\#\widehat\otimes T_{11}E\), \(T=\gamma-1\), \(z=Tz_1\) the canonical global division proved above. We now show \(z_1\) preserves all strict Greenberg conditions **at the level of global cohomology**.

### At BOTH \(v\mid11\): no quotient invariants

Use the exact coefficient sequence
\[
0\to F^-A\xrightarrow{T}F^-A\to F^-T_{11}E\to0.
\]
The ordinary rank-one quotient has unramified Frobenius value \(\alpha_{11}\equiv5\pmod{11}\), which is **not 1**. Hence
\[
H^0(K_v,F^-T_{11}E)=0
\]
at **each** of the two split-11 completions, in agreement with Howard Lemma2.4.4. The long exact sequence therefore makes multiplication by \(T\) injective on \(H^1(K_v,F^-A)\). Now \(z\) is already strict Greenberg, so its localization in that quotient is zero. As \(z=Tz_1\),
\[
0=\operatorname{loc}_{F^-}(z)
 =T\,\operatorname{loc}_{F^-}(z_1)
\quad\Longrightarrow\quad
\operatorname{loc}_{F^-}(z_1)=0.
\]

### At EVERY finite \(v\nmid11\): inertia invariants lift

The tower \(D_\infty/K\) is **unramified away from 11**. Thus \(I_v\) acts trivially on the Iwasawa \(\Lambda\)-coefficient factor. If \(a\in(T_{11}E)^{I_v}\), then its **constant-coefficient lift** \(a\otimes1\in A^{I_v}\) is invariant. Consequently
\[
H^0(I_v,A)\longrightarrow H^0(I_v,T_{11}E)
\]
is SURJECTIVE. The long exact sequence for \(0\to A\xrightarrow{T}A\to T_{11}E\to0\) then makes \(T\) injective on \(H^1(I_v,A)\), **even if local multiplicative inertia on \(T_{11}E\) is nontrivial**. Because \(z\) is unramified at \(v\),
\[
0=\operatorname{res}_{I_v}(z)
=T\,\operatorname{res}_{I_v}(z_1)
\quad\Longrightarrow\quad
\operatorname{res}_{I_v}(z_1)=0.
\]
This includes the two bad-conductor prime types \(v\mid2\) and \(v\mid117223\). Local Frobenius action on \(\Lambda\) may be nontrivial, but INERTIA acts trivially; only the latter is needed.

Therefore the unique nonzero divided global Iwasawa cohomology class from C-0025 is in fact a **nonzero divided strict Greenberg Iwasawa class**
\[
\boxed{0\ne z_1\in
\operatorname{Sel}_{\mathrm{Gr,Iw}}(D_\infty/K,T_{11}E)
\otimes_{\mathbb Z_{11}}\mathbb Q_{11},
\qquad T z_1=z.}
\tag{25.3}
\]
Here \(\operatorname{Sel}_{\mathrm{Gr,Iw}}\) denotes the norm-compatible classes in global \(H^1_{\rm Iw}\) satisfying the above Howard **strict Greenberg** conditions at every place; no identification with a *higher derived base-field Selmer point* is claimed.

**Independence / base caveat:** This divided class is **nonzero in the inverse-limit Selmer group**, but its base \(\operatorname{pr}_K(z_1)\) may equal zero. Thus there is **no** established nonzero \(h^{(r)}\), no actual Coleman coefficient in \(J/J^2\), no full algebraic rank of \(E(K)\) certified, and no original complex BSD implication. The next high-value task is to determine whether \(\operatorname{pr}_K(z_1)\ne0\). If zero, the same *global and local* argument provides a further canonical division (provided integral/source compatibility remains), but **the first positive exact order remains unproved**. A finite nonzero order additionally needs a precise separatedness or rank-one/flatness statement for this weight-two inverse-limit Selmer module.

[Exact arithmetic/logic controls](howard_divided_greenberg_local_gate.py) verify split-11 \(\alpha\ne1\), unipotent-multiplicative inertia invariants lifting at primes away from11, and adversarial countermodels with exceptional \(\alpha=1\) or \(\Gamma\)-ramified inertia. They do NOT implement Galois cohomology. The proof consists of the two standard LES applications plus Howard's **published** local Selmer statement, and requires no conjectural Sha finiteness.

**Remaining proof obligations:** Determine actual first nonzero augmentation graded/base class; derive source-normalized pair of Coleman \(J\)-leading coefficients for it using Castella/CH; ensure weight-two lattice identifications and local comparison match the exact conventions; and prove a novel noncircular original complex \(L''(E/\mathbb Q,1)\) bridge. These remain formidable open questions.
