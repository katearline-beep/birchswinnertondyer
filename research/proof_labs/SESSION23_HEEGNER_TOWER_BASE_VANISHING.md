# Session 23 — Forced base Heegner vanishing, an actual Howard anticyclotomic inverse limit, and explicit ring-class tower

**2026-10-19 · Theorem-first source audit, independent modular arithmetic and conditional category bookkeeping.** No new theorem beyond standard consequences of Kolyvagin, Gross–Zagier, Howard and quadratic class field theory; no original complex rank-four BSD result.

**Primary sources:** Darmon, *Heegner points, elliptic curves and arithmetic of modular forms*, [CBMS notes, Theorem 3.21](https://www.math.mcgill.ca/darmon/pub/Articles/Research/36.NSF-CBMS/chapter.pdf) (Kolyvagin); Howard, [*Variation of Heegner points in Hida families*](https://arxiv.org/pdf/1202.6358), §§1, 2.3 and **3.1–3.3** (particularly Corollary 3.1.2 and construction of \(Z_\infty\)); Castella–Hsieh, [Theorems 4.1 and 4.5](https://web.math.ucsb.edu/~castella/Kato.pdf). Standard ring class number formula, Cox *Primes of the Form \(x^2+ny^2\)*, Theorem 7.24.

## 1. We should expect the classical base Heegner point to vanish rationally

Our focal elliptic curve \(E:y^2+xy=x^3-x^2-79x+289\), conductor \(N=2\cdot117223\), has **four independent rational points** \(P_1,\ldots,P_4\) already known from the arithmetic-rank certification used throughout the project. Thus
\[
\operatorname{rank}E(K)\ge \operatorname{rank}E(\mathbb Q)=4>1,
\qquad K=\mathbb Q(\sqrt{-7}).
\]
Both conductor primes **split in \(K\)**, so classical Heegner points and the corresponding norm-compatible Heegner system exist, and \(h_K=1\).

**Published Kolyvagin Theorem (Darmon, Theorem 3.21):** If the classical traced Heegner point \(P_K\in E(K)\) associated to a modular parametrization \(X_0(N)\to E\) is non-torsion, then \(\operatorname{rank}E(K)=1\) (and \(\Sha(E/K)\) is finite).

By immediate logical contrapositive, because \(\operatorname{rank}E(K)\ge4\),
\[
\boxed{P_K\text{ must be torsion, and }P_K\otimes1=0
       \text{ in }E(K)\otimes_{\mathbb Z}\mathbb Q_{11}.}
\]
This is an **exact conclusion** from the published theorem and rank≥4 input. It is not a numerical guess, and it requires neither proving \(E(K)\) has *exactly* rank five nor evaluating a \(p\)-adic height. Gross–Zagier further identifies the classical canonical height of \(P_K\) with the complex *base-change first derivative*, yielding
\[
L'(E/K,1)=0.
\]
Because classical Heegner setup also gives global sign \(-1\) for \(L(E/K,s)\), its central analytic order is at least 3 (odd). **This does not establish original complex \(L''(E/\mathbb Q,1)=0\)**: \(L(E/K,s)=L(E,s)L(E^{-7},s)\), and the exact twist first derivative is an independent factor. A known rank-four arithmetic group does not force four complex zeros by this argument.

**Crucial qualification:** It is the **classical Kummer image of \(P_K\)** that is rationally zero. Whether the augmentation of a particular \(p\)-stabilized, critically twisted, Nekovář-extended **Howard** class equals that Kummer image multiplied by a nonexceptional Euler factor requires checking the precise specialization map and local correction terms. Do not silently equate a vanishing classical point with vanishing of *every* extended Selmer coordinate.

## 2. Howard §3.3 already constructs the inverse-limit class we had called missing

We should correct the earlier Session22 wording. **Howard does more than produce isolated** \(\mathfrak X_c\in\widetilde H_f^1(H_c,T^\dagger)\). He gives the norm-compatible anticyclotomic tower class explicitly.

In §3.3, let \(D_s/K\) be the degree-\(11^s\) subextension of the anticyclotomic \(\mathbb Z_{11}\)-extension \(D_\infty/K\), and let \(G_{\mathrm{tors}}\) be the prime-to-11 torsion group of the ring-class Galois tower. Howard chooses \(t\) large enough that \(D_s\subseteq H_{11^{t+1}}\) and defines
\[
Z_s=\operatorname{cor}_{H_{11^{t+1}}/D_s}
\bigl(U_{11}^{-t}\,\mathfrak X_{11^{t+1}}\bigr)
\in \widetilde H_f^1(D_s,T^\dagger).
\]
Howard proves **independence of \(t\)** and **norm compatibility** \(Z_{s+1}\mapsto Z_s\), obtaining the **actual published class**
\[
\boxed{Z_\infty=\varprojlim_s Z_s\in
\widetilde H^1_{f,\mathrm{Iw}}(D_\infty,T^\dagger),}
\]
and proves it is not torsion over the two-variable Iwasawa algebra \(R_\infty\). This is not merely a hypothetical object; it is the source-level bridge from ring-class Euler classes to the anticyclotomic tower we sought in Session22.

**Correction to our stop/go diagram:** The *ring-class → anticyclotomic norm-compatible inverse limit* arrow is **PUBLISHED AND CONSTRUCTED**. The arrows **still missing for our rank-four target** concern the weight-two specialization of \(T^\dagger\), the quotient/identification of extended Selmer with the relevant compact global Iwasawa cohomology target, and each local Coleman-map \(J\)-adic valuation.

Howard's Corollary 3.1.2 also proves nonzero specialization at **sufficiently high \(11\)-power conductor levels**. That is perfectly compatible with a torsion base Heegner point: a nonzero power series can have zero constant coefficient. Nonzero in the tower is **not** the same assertion as nonzero augmentation at \(s=0\).

## 3. Exact arithmetic: the entire anticyclotomic ring-class tower is concrete here

Write \(\mathcal O_K=\mathbb Z[\omega]\), \(\omega=(1+\sqrt{-7})/2\), \(\omega^2-\omega+2=0\). The field \(K\) has class number 1 (Minkowski bound \(2\sqrt 7/\pi<2\)) and \(\mathcal O_K^\times=\{\pm1\}\). Because 11 splits, the Chinese remainder theorem yields for every \(n\ge1\)
\[
\mathcal O_K/11^n\mathcal O_K
\simeq (\mathbb Z/11^n)^2.
\]
The ring-class exact sequence gives
\[
\operatorname{Pic}(\mathbb Z+11^n\mathcal O_K)
\simeq\frac{(\mathcal O_K/11^n)^\times}
{(\mathbb Z/11^n)^\times\cdot\mathcal O_K^\times}
\simeq(\mathbb Z/11^n)^\times,
\]
where the last map is the **ratio** of the two split components and the units \(\{\pm1\}\) lie in the diagonal already.

Therefore
\[
\boxed{[H_{11^n}:K]=\varphi(11^n)=10\cdot 11^{n-1},\qquad
\operatorname{Gal}(H_{11^n}/K)\simeq C_{10}\times C_{11^{n-1}}.}
\]
There is an **integral** order-ten torsion projector \(e_\Delta=10^{-1}\sum_{\delta\in\Delta}\delta\) over \(\mathbb Z_{11}\), and the fixed field \(H_{11^{s+1}}^\Delta\) is **exactly \(D_s\)** of degree \(11^s\) over \(K\). This recovers Howard §3.3's **offset \(\delta=0\)** in our class-number-one setting, not merely for sufficiently large \(s\).

The [pure stdlib tower verifier](heegner_ring_class_tower_11.py) lifts the two roots of \(x^2-x+2\) at 11 to precision \(11^4\), constructs explicit CRT witnesses for arbitrary norm-one-second-component pairs, proves 2 is a primitive root modulo \(11^n\) for \(n=1,2,3,4\), and checks the integral \(1/10\) projector and extension degrees:

| n | Ring-class group order | \([D_{n-1}:K]\) |
|---:|---:|---:|
| 1 | 10 | 1 |
| 2 | 110 | 11 |
| 3 | 1210 | 121 |
| 4 | 13310 | 1331 |

It also independently computes the unit root \(\alpha_{11}\) of \(X^2+6X+11\):
\[
\boxed{\alpha_{11}\equiv12721\pmod{11^4},\qquad
1-\alpha_{11}^{-1}\equiv3\pmod{11}.}
\]
Thus the elementary Euler factor \(1-\alpha^{-1}\) is a unit; the vanishing of the *classical* base point cannot simply be blamed on \(\alpha\equiv1\pmod{11}\). This **does not** establish the exact Euler factors in Howard's critical twist at augmentation, and should not be substituted for a source-normalized formula.

## 4. The remaining diagram is much smaller, but still seriously open

**Already published:**
\[
\mathfrak X_{11^{t+1}}\in \widetilde H_f^1(H_{11^{t+1}},T^\dagger)
\xrightarrow{\ \operatorname{cor}\,U_{11}^{-t}\ }
Z_\infty\in\widetilde H_{f,\mathrm{Iw}}^1(D_\infty,T^\dagger).
\]

**Still needs a precise map and verification for *this* weight-two specialization:**
\[
Z_\infty
\xrightarrow{\ \text{specialize }T^\dagger\text{ at }E\ }
\text{weight-two anticyclotomic extended Selmer class}
\xrightarrow{\ \text{forget extended conditions/control theorem}\ }
z_E\ \stackrel{?}{\in}\ \widehat H^1(D_\infty,V_{11}E).
\]

**Needed to invoke Castella–Hsieh 4.5:**
\[
\mathrm{Col}_{\eta}(\operatorname{Loc}_{\mathfrak p}z_E),\quad
\mathrm{Col}_{\eta}(\operatorname{Loc}_{\mathfrak p}z_E^\tau)
\quad\text{with independently proved }\operatorname{ord}_J\ge r.
\]

And **after all of that**, a new noncircular comparison to the **original complex** \(L''(E/\mathbb Q,1)\) is required. Howard nonzero over the tower does not prove order \(r=1\), \(r=2\), a nonzero derived height, or even a well-defined CH compact-class map without verifying the relevant Selmer control sequence.

## 5. Portfolio decision, falsifiers, and proof truth flags

**Promote:** Howard's **actual anticyclotomic class** \(\,Z_\infty\,\) (published), with an explicitly computable Galois-tower quotient and the independent Kolyvagin **base-point torsion obstruction**.

**Falsify these shortcuts:** (i) non-torsion classical \(P_K\) on our rank-four curve; (ii) nonzero Howard big class ⇒ nonzero base point; (iii) norm-compatible class in **extended** Selmer ⇒ automatically defined class in CH's **compact** \(H^1\); (iv) vanishing augmentation ⇒ automatically a defined \(J\)-derivative without an exact augmentation/control sequence; (v) \(p\)-adic height or p-adic L-series order ⇒ original complex \(L''\) zero.

**Next milestone:** Verify the weight-two specialization/local-control exact sequence and construct a **typed, source-checked** map \(Z_\infty\to \widehat H^1(D_\infty,V_{11}E)\), or produce a real obstacle; only then investigate its two Coleman orders. Preserve high-rank nontriviality at elevated ring class levels and zero classical base simultaneously. In parallel continue Ulmer's Tate-cycle source audit. Do not add routine local height digits.

**No general BSD theorem, rank-four complex analytic-order theorem, Sha finiteness or leading-coefficient formula has been proved.**
