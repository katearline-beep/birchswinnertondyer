# Session 25 — Howard's exact base norm, zero weight-two augmentation, and the first-derivative no-go

**19 October 2026. Theorem-first source calculation C-0024, applied to the focal curve E=234446.a1.** AI-audited and executable exact algebra checks; no human mathematics review, no new analytic BSD theorem.

**Primary sources:** Howard, [*Variation of Heegner points in Hida families*](https://arxiv.org/pdf/1202.6358) Proposition **2.3.1** (first and later p-power norm relations) and §**3.3** (normalized \(Z_s\) and \(Z_\infty\)), §3.4 (base \(Z_0\)); Castella, [*On the p-adic variation of Heegner points*](https://web.math.ucsb.edu/~castella/Heegner.pdf), Theorem **6.5** and Remark **6.6** (weight-two classical Heegner Kummer), Theorem **5.3**, Corollary **3.9**, Proposition **5.2** (p-adic local big logarithm and interpolation); Castella–Hsieh, [*On the non-vanishing of generalized Kato classes*](https://web.math.ucsb.edu/~castella/Kato.pdf), Proposition **4.3**, equations **(4.9)–(4.10)**, Theorem **4.5** (two conjugate Coleman maps and augmentation criterion).

## 1. A missing arrow from Session 24 can actually be computed at the source level

Let \(X_c\) be Howard's big Heegner class over ring-class field \(H_c\), with ordinary Hecke operator \(U_p\). **Howard Proposition 2.3.1** states, including \(c=1\),
\[
\operatorname{cor}_{H_{cp}/H_c}(X_{cp})=U_p X_c
\]
for \(c\) prime to \(N\) (so \(c\) may equal higher powers of \(p\)). Since \(p=11\nmid N=234446\), iterating this formula gives
\[
\boxed{\operatorname{cor}_{H_{11^{t+1}}/K} X_{11^{t+1}}=U_{11}^{t+1}X_1},
\]
because \(h_K=1\) and \(H_1=K\).

In **Howard §3.3**, the class at \(D_0=K\) is obtained by normalized corestriction,
\[
Z_0^{\mathrm{tower}}=\operatorname{cor}_{H_{11^{t+1}}/K}
\bigl(U_{11}^{-t} X_{11^{t+1}}\bigr).
\]
Thus, **without any assumption about class values, \(L\)-derivatives, or 11-adic heights**, and using the source's unit \(U_{11}\),
\[
\boxed{\operatorname{pr}_K(Z_\infty)=Z_0^{\mathrm{tower}}=U_{11}X_1.}
\tag{25.1}
\]
**Do not conflate** \(Z_0^{\mathrm{tower}}\) (the zeroth component of the norm-compatible anticyclotomic *tower*) with Howard §3.4's *base-field big Heegner class* \(Z_0^{\mathrm{Howard}}=\operatorname{cor}_{H_1/K} X_1=X_1\) for \(h_K=1\). The exact relation is a **factor \(U_{11}\)**. Omitting it gives the wrong integral norm identity, although the difference is a unit at our ordinary specialization. Castella §4.2 (equation (4.3)) uses an index-shifted but compatible normalization \(U_p^{1-t}X_{p^t}\) at levels \(t\ge1\).

## 2. A genuine arithmetic zero at weight two, not merely a toy counterexample

Our E at \(p=11\) is ordinary with \(a_{11}=-6\). The 11-adic unit-root \(\alpha_{11}\) satisfies \(\alpha_{11}\equiv5\pmod{11}\) and \(\alpha_{11}\equiv12721\pmod{11^4}\). Under the **published** weight-two \(p\)-old specialization of Castella Theorem6.5/Remark6.6, as certified in C-0023,
\[
\nu_2(X_1)=(1-\alpha_{11}^{-1})^2\kappa(P_K)
\]
with factor congruent \(9\bmod11\), a unit. Kolyvagin forces the **classical** \(P_K\) to be torsion because \(\operatorname{rank}E(K)\ge4\). Hence \(\kappa(P_K)=0\) in *rationalized* \(11\)-adic cohomology, giving
\[
\nu_2(X_1)=0,
\qquad
\boxed{\operatorname{pr}_K\bigl(\nu_2(Z_\infty)\bigr)
=\alpha_{11}(1-\alpha_{11}^{-1})^2\kappa(P_K)=0.}
\tag{25.2}
\]
This is a **theorem-based vanishing for the actual original curve**. The weight specialization and finite-layer corestriction commute by standard cohomology functoriality. It does **not** prove \(\nu_2(Z_\infty)\) is a nonzero element of the weight-two Iwasawa cohomology group, nor that it is divisible by the global anticyclotomic augmentation ideal \(J\) as an element of its entire Selmer module. Inverse-limit specialization/control kernels must not be silently identified with \(JM\).

## 3. Consequence for BOTH first Coleman augmentation values — and why it cannot prove anything about the height

Castella–Hsieh **equation (4.10)** and their Perrin–Riou/Coleman interpolation construct the two (complex-conjugate) local Iwasawa maps at \(\mathfrak p\mid11\) and \(\overline{\mathfrak p}\mid11\). Their constant-term specialization is proportional to the Bloch–Kato logarithm of the projected local base-field class (the factor is the displayed ordinary Euler normalization in **Lemma 4.4**, not a freely chosen constant). At our good ordinary **nonexceptional** \(p=11\), \(\alpha_{11}\not\equiv1\pmod{11}\), and the local logarithm of the **zero projected class (25.2)** is zero at BOTH split places. Therefore, for the canonically specialized class **once identified with the source's compact \(H^1\) coefficients/local maps**,
\[
\boxed{\operatorname{aug}\operatorname{Col}_{\mathfrak p}=0,\qquad
\operatorname{aug}\operatorname{Col}_{\overline{\mathfrak p}}=0,}
\]
i.e. **each regular normalized local Coleman series belongs to \(J\)**. This is a *conditional-on-correct-coefficient-map* theorem consequence, not two numerically computed Coleman values. The exact Castella two-variable big logarithm (Theorem5.3) similarly implies that the corresponding weight-two anticyclotomic **p-adic L-function** has zero trivial-character value, **provided** the paper's twisted class/character \(\xi\) and unramified local regulators are specialized compatibly. This is **not** a theorem about the original complex \(L''(E/\mathbb Q,1)\).

**Do not promote an order beyond \(J^1\):** The constant term zero proves neither a nonzero coefficient of \(J/J^2\) nor membership in \(J^2\). It does not determine either local order or whether the conjugate series have matching leading terms.

**Critical automatic-zero trap:** Castella–Hsieh **Theorem 4.5** computes \(h^{(r)}(\operatorname{pr}_K z,x)\) for a specified compact Iwasawa class \(z\). For the specialized **Howard class** we have \(\operatorname{pr}_K z=0\), so every such height is **zero by bilinearity**. Applying Theorem4.5 to the ordinary weight-two Howard class at \(r=1\) therefore cannot produce the **nonzero derived Selmer class** we need. Even if both local Coleman coefficients at order one are nonzero, the resulting equation for the ZERO base class imposes a **cancellation constraint**, not an honest nonzero BSD regulator.

**Research-leapfrog:** Work in an actual Iwasawa **control/Bockstein exact triangle**, attempting to divide the universal norm by the anti augmentation \(T\) or the Hida weight prime only where the necessary torsion-free/injective control and choice-independence hypotheses are proved. The natural next candidate is the *derived* class at the first genuinely nonzero weight/anti graded order, and one should test BOTH Coleman images after correctly deriving it. No formal differentiation of the p-adic L-function alone constructs a Selmer class.

## 4. Exact arithmetic and adversarial controls

The [self-contained standard-library verifier](howard_base_augmentation_gate.py) proves the abstract \(U_{11}\) norm-renormalization identity for seven tower levels and a variety of coefficient values, checks \(\alpha_{11}\equiv12721\pmod{14641}\), \((1-\alpha^{-1})^2\equiv9\bmod11\), and rejects the **wrong normalized base relation \(Z_0^{\mathrm{tower}}=X_1\)**. The source theorem (Howard 2.3.1) remains an EXTERNAL published input; a toy scalar module is not a computation of Heegner points.

Three further concrete falsifiers:
- \(J\)-membership \(\not\Rightarrow\) exact order one or a nonzero derivative; local series \(T,T^2,0\) all have augmentation zero.
- A noninjective base observation can kill a non-\(JM\) global element; source-level (25.2) alone does not establish actual global Selmer \(J\)-divisibility.
- A regulator with an unaccounted pole \(1/T\) can send \(T\) to nonzero constant. The compatibility/nonexceptional **regularity** of the actual Coleman/compact class must be checked before assigning \(J\)-order. Never replace Castella's source normalizations with that toy model.

## 5. Whole BSD review and next experiment

This is the strongest advance in **first anticyclotomic augmentation** in the theorem-first Heegner laboratory: we have computed its BASE cohomological projection exactly, as zero, using Howard's actual norm relations and Castella/Kolyvagin. It lets us stop treating the zeroth coefficient as an unknown measurement.

It is NOT a nonzero derived height or novel higher-rank BSD theorem. It **rules out** the simple strategy of applying Castella–Hsieh Theorem4.5 directly to the un-divided weight-two Howard class to get a nonzero regulator. Next produce a precise, canonically controlled **Bockstein/divided Heegner class** that can have nonzero base projection, and independently test both local J-leading terms. The separate original **complex** \(L''(E/\mathbb Q,1)\) bridge remains missing. Keep Ulmer's independent characteristic-p global proof laboratory alive as a second route.

**No arithmetic rank-four complex analytic order, Sha finiteness, BSD leading coefficient or general BSD proof.**
