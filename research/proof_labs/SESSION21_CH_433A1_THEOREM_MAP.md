# Session 21 — Genuine rank-two Castella–Hsieh control; what applies to our rank-four curve

**2026-10-19. Published theorems plus independent elementary arithmetic.** Sources: [Castella–Hsieh (2022), Theorems A/B, 4.1, 4.5, 5.3, Appendix Table 1](https://web.math.ucsb.edu/~castella/Kato.pdf); [LMFDB 433.a1](https://www.lmfdb.org/EllipticCurve/Q/433/a/1). No Kato class, theta series, higher derived height or BSD assertion is independently proved by these scripts.

## The chosen rank-two control is real, not the earlier mismatched example

Castella–Hsieh Appendix Table 1 gives **E=433a1**, \(p=11\), \(K=\mathbb Q(\sqrt{-7})\), with
\[
E:y^2+xy=x^3+1,\qquad N=433,\quad\Delta=-433,\quad\operatorname{rank}E(\mathbb Q)=2.
\]
Its appendix records
\[
\boxed{\Theta_{f/K}(T)\equiv
88T^2+22T^3+86T^4+7T^5+10T^6+12T^7+
29T^8+88T^9+48T^{10}\pmod{(121,T^{11})}.}
\]
The **coefficient of \(T^2\) is 88**, which is *zero modulo 11* but *nonzero modulo 121*. Therefore using only mod11 precision to read the first nonzero term would be **misleading**; the authors' mod121 calculation and source arguments yield \(\operatorname{ord}_T\Theta_{f/K}=2\). We do **not** independently compute theta via Brandt modules, nor claim that a finite truncation alone can prove lower-degree coefficients vanish exactly without the source theory.

The [exact stdlib prerequisite checker](castella_hsieh_433a1_control.py) verifies:
- the minimal model and two displayed rational points \((0,1),(-1,1)\) lie on E; *their independence/rank two is a published source/LMFDB input*;
- the standard Weierstrass invariants give \(\Delta=-433\), so q=433 is multiplicative of valuation one, and \(11\nmid v_{433}(\Delta)\), ensuring mod11 Tate ramification at q;
- the Kronecker/Legendre symbol \(({-7}/433)=-1\) and \(({-7}/11)=+1\): 433 is the **single inert bad conductor prime** \(N^-=433\), while \(p=11\) splits in K;
- direct \(\#E(\mathbb F_5)=10\), \(\#E(\mathbb F_{11})=16\) yield \(a_5=a_{11}=-4\). Thus p=11 is good ordinary;
- \(a_5^2-4\cdot5=-4\equiv7\pmod{11}\) is a **nonsquare**, so the Frobenius-at-5 characteristic polynomial is irreducible over F11. A globally reducible 2-dimensional F11 representation would have a Frobenius-stable rational line at **every** good prime, hence every characteristic polynomial would split. Therefore \(\bar\rho_{E,11}\) is **irreducible**, independently of assuming LMFDB's image classification.
- conditional Theorems B+A: \(\operatorname{ord}_T\Theta=2\Rightarrow\kappa\ne0\Rightarrow\dim_{\mathbb Q_{11}}\operatorname{Sel}(\mathbb Q,V_{11}E)=2\), with all theorems' hypotheses required.

**What is *only* imported from the authors:** the construction and expansion of \(\Theta_{f/K}\); \(L(E^K,1)\ne0\); existence of an auxiliary ring-class character with required nonzero \(L(E/K,\chi,1)\) (via their cited theorem); analytic and algebraic rank 2, and all global Kato / Coleman-map identities. We have therefore chosen an actual *published* theorem-valid rank-two laboratory without claiming to reproduce its hard global cohomology or L-value computations.

## Unexpected direct applicability to our original rank-four test curve

The two published statements have **different local hypotheses**, and we must not mix them.

| Item | 433a1 / p11 / K=-7 control | Original E=234446.a1 / p11 / K=-7 |
|---|---|---|
| Bad conductor primes | {433}, inert ⇒ \(N^-=433\) | {2,117223}, **both split** ⇒ \(N^-=1\) |
| Ordinary at 11 | \(a_{11}=-4\ne0\bmod11\) | \(a_{11}=-6\ne0\bmod11\), \(\#E(\mathbb F_{11})=18\) |
| Discriminant of K coprime to 11N | Yes | Yes |
| \(\bar\rho_{E,11}\) ramified at each inert bad prime | Yes, \(v_{433}\Delta=1\) | **Vacuously yes** (there are none) |
| Castella–Hsieh **Theorem 4.1** derived-height filtration | **Applies** | **Applies** (because \(N^-=1\) is squarefree and ramification is vacuous) |
| **Theorem A / B** nonzero generalized Kato criterion | Published case, full global hypotheses via authors | **Does not apply at K=-7**: requires an odd number of inert bad conductor primes |
| **Theorem 4.5** formula for a specific global Iwasawa class \(z\) | Published construction and application by authors | Abstract formula available only **IF** a valid \(z\in\widehat H^1(K_\infty,V_{11}E)\) with specified Coleman orders exists. **None constructed.** |
| Original complex analytic rank-four conclusion | Not relevant, rank2 control | **Still not proved**; p-adic heights do not imply complex \(L''=0\) |

**Key upgrade over the previous research plan:** Theorem 4.1 **already rigorously supplies** a decreasing filtration
\[
S^{(1)}=\operatorname{Sel}(K,V_pE)\supseteq S^{(2)}\supseteq\cdots
\]
and higher pairings
\[
h^{(r)}:S^{(r)}\times S^{(r)}
\longrightarrow (J^r/J^{r+1})\otimes_{\mathbb Z_p}\mathbb Q_p,
\qquad S^{(r+1)}=\operatorname{rad}h^{(r)}
\]
for our **original rank-four E at p=11 and K=-7**, without requiring Theorem A's odd-inert premise. Theorem 4.1 supplies symmetry for odd \(r\), alternating behaviour for even \(r\), and Galois conjugation anti-equivariance according to \(r\). This existence statement comes from **published mathematics**; it does not compute the filtration stages or prove that the provisional BCLMN self-height vector is exactly normalized as CH \(h^{(1)}\).

## A rank-sensitive conditional theta-order obstruction

Under **all** the simultaneous hypotheses of Theorems **A and B**, and assuming \(\operatorname{rank}E(\mathbb Q)>0\):
\[
\operatorname{ord}_T\Theta_{f/K}=2
\Longrightarrow \kappa_{\alpha,\alpha^{-1}}\neq0
\Longrightarrow \dim_{\mathbb Q_p}\operatorname{Sel}(\mathbb Q,V_pE)=2.
\]
The standard Kummer injection gives \(\operatorname{rank}E(\mathbb Q)\le\dim\operatorname{Sel}\). Hence if \(\operatorname{rank}E(\mathbb Q)\ge4\) **and all Theorem A/B hypotheses are met**, then
\[
\boxed{\operatorname{ord}_T\Theta_{f/K}\ne 2.}
\]
**Important:** This does *not* imply the order is exactly four, that our old K=-7 satisfies Theorem A, or that the original complex \(L''(E,1)\) vanishes. To deduce \(\operatorname{ord}\Theta\ge4\) would require separately proving lower-bound and parity/order exclusions; we do **not** claim those here. The theorem simply rules out a rank-two theta behaviour for any admissible rank-four instance. This is an elementary *new-to-our-project corollary* of published theorems, not a previously unknown general theorem.

## Typed Coleman/derived-height mechanism and the missing arrows

Theorem 4.1: **published and applicable to the original E.**

\[
\operatorname{Sel}(K,V_pE) = S^{(1)}\ \supseteq\ S^{(2)}\
\supseteq\cdots,\quad
h^{(r)}:S^{(r)}\otimes S^{(r)}\to(J^r/J^{r+1})\otimes\mathbb Q_p.
\]

Theorem 4.5: **a theorem about a *supplied* Iwasawa cohomology class**, not a procedure that constructs it:

1. **Input:** a specified \(z\in\widehat H^1(K_\infty,V_pE)\), with conjugate \(\bar z=z^\tau\).
2. **Localizations and Coleman maps:** \(\mathrm{Loc}_{\mathfrak p}(z)\) and \(\mathrm{Loc}_{\mathfrak p}(\bar z)\) feed \(\mathrm{Col}_\eta\) into the anticyclotomic Iwasawa algebra \(\Lambda\), with augmentation ideal \(J\).
3. **Hypothesis gate:** both Coleman images must lie in \(J^r\), with **a demonstrated augmentation-order bound**, not merely local elliptic logarithms.
4. **Output:** the projected class \(\mathrm{pr}_K(z)\in S^{(r)}\) and a formula for \(h^{(r)}(\mathrm{pr}_K(z),x)\) modulo \(J^{r+1}\), involving those *actual* Coleman images and the local logarithms of \(x\in S^{(r)}\).
5. **Further missing bridge:** an independently proved theorem relating such a \(p\)-adic regulator/derived height to the **original complex** \(L''(E,1)\) (and separately Sha/leading coefficient) does not follow from Theorems 4.1/4.5.

Our rank-four C-0011/13 BCLMN first heights, if independently verified, may provide clues about the **shape** of \(S^{(2)}\), but **no identification of BCLMN's height with the normalized CH \(h^{(1)}\), nor its radical with full \(S^{(2)}\), has been made**. Theorem 4.5 cannot be invoked on those numeric heights as though they were a global \(z\).

## Next high-value test

**Do not repeat** local logarithms or arbitrary height digits. Source-audit the construction of the Iwasawa-global class in Theorem 5.3 and characterize precisely which ingredients are absent in rank four. The existence of the general filtration has crossed from conjectural to *published-applicable* status; the **global cohomology-class construction and complex comparison** are now the research bottlenecks.

**Reproduce:**
\`\`\`bash
python3 -I -B research/proof_labs/castella_hsieh_433a1_control.py
\`\`\`

This checker is an exact arithmetic/theorem-scope control, **not** an independent computation of \(\Theta\), \(\kappa\), Selmer dimension, \(h^{(r)}\), original complex analytic rank, Sha or BSD.
