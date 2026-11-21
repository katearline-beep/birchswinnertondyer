# Session52 — an everywhere-unramified fine Kummer quotient and an 11-class-group rank bound

**2026-11-21, America/New_York. AI-assisted source-dependent arithmetic theorem/certificate, not independently expert reviewed.** Narrow continuation of Session51/PR #94. General BSD rank equality, original E234446.a1 complex \(L''(E,1)=0\), nonzero \(L^{(4)}(E,1)\), original Sha finiteness and BSD leading coefficient are all **unproved**. **New mathematical implication toward BSD: NONE.** Do not confuse a class-group result for a large auxiliary torsion field with the Tate–Shafarevich group of E/Q.

## Exact question and objects

Can the three already known **fine** Mordell–Weil classes give a *genuine finite everywhere-unramified extension* of the actual 11-torsion field, with a certified full Galois translation group, and therefore a class-group consequence? This was selected after Session51 exhibited actual local 11-division points. The acceptance test requires:
1. **Three** actual fine MW classes, with checked zero localization at both \(11\)-adic places and cited bad-prime local 11-divisibility;
2. only THREE actual reduction Frobenius words giving independent 11-Kummer signatures, plus an irreducible conjugating Frobenius;
3. a correct local and global Kummer proof that the relative division field is everywhere unramified and completely split at every supported prime; and
4. an explicit fail-closed distinction between a certified class-group QUOTIENT and a computed class group or a BSD implication.

Let \(K=\mathbf Q(\sqrt{-7})\), \(V=E[11]\), \(L=K(E[11])\), and \(\Sigma\) include the K-places over 2, 11, 117223 and infinity. The three positive Q-rational fine classes from C0039 and Session50 are:
\[
\begin{aligned}
Y_1&=P_2,\\
Z_1&=-2P_1+3P_2+P_3,\\
Z_2&=-9P_1+6P_2+P_4.
\end{aligned}
\]
They form an invertible change of basis from \(Y_1=P_2,\,Y_2=P_3-2P_1,\,Y_3=P_4-9P_1\), so are independent in the five-point residual Kummer span. Write
\[
 F_{\mathrm{fine}}=L([11]^{-1}Y_1,[11]^{-1}Z_1,[11]^{-1}Z_2).
\]
This is a *specified actual finite number field*, by adjoining all 11-division points of the displayed rational points. No enormous defining polynomial is claimed.

## Three-prime finite-field certificate: exact relative image \(V^3\)

The Session46 independent Python/PARI arithmetic supplies good split principal primes \(q=743,2843,3019\), all with 11-primary reduction of valuation exactly one and \(q\not\equiv1\bmod11\). Their five-point 11-Kummer signatures, in order \((P_1,P_2,P_3,P_4,R)\), are
\[
\begin{array}{c|ccccc}
q& P_1&P_2&P_3&P_4&R\\\hline
743&1&0&0&2&6\\
2843&1&4&9&9&1\\
3019&1&8&0&4&1.
\end{array}
\]
Projecting to \((Y_1,Z_1,Z_2)\) gives
\[
\boxed{
S=\begin{pmatrix}
0&9&4\\
4&8&2\\
8&0&10
\end{pmatrix},\quad \det S=1\pmod{11}.}
\]

The good-prime Frobenius powers \(w_q=\mathrm{Frob}_{\mathfrak q}^{m_q}\), with \(m_q\) the actual order of the residual Frobenius on \(V\) (10, 5, 5), lie in \(\ker\rho\) and give Kummer images \(u_q\otimes S_{q,*}\in V\otimes\mathbf F_{11}^3\), with **one nonzero but UNKNOWN global torsion vector** \(u_q\in V\) for each q. This is the exact local good-reduction Kummer/Frobenius norm lemma already independently checked in Session46; it does not identify residue-field point coordinates with a global E[11] basis.

The actual Frobenius at the split K-prime over23 has residual matrix with irreducible characteristic polynomial \(X^2+6X+1\) (discriminant 10, a nonsquare in F11). Thus each \(u_q\ne0\) and its conjugate \(A_{23}u_q\) span V. The six Kummer translations
  \(u_q\otimes S_{q,*}\) and \(A_{23}u_q\otimes S_{q,*}\)
for q=743,2843,3019 span ALL \(V\otimes\mathbf F_{11}^3\), since \(\det S=1\). Hence, without assuming \(\rho(G_K)=\mathrm{GL}_2(\mathbf F_{11})\),
\[
\boxed{\operatorname{Gal}(F_{\mathrm{fine}}/L)\cong V^3
       \cong(\mathbf Z/11\mathbf Z)^6,\qquad
       [F_{\mathrm{fine}}:L]=11^6=1{,}771{,}561.}
\]
The source-derived theorem relies only on the authenticated actual 23/743/2843/3019 Frobenius inputs, the standard Kummer local norm statement and the field-defining division points; it does NOT rely on the anticyclotomic \(\chi=0\) values at the three primes, C0040 first heights, C0044 Selmer rank, C0047 corrected lifts or Sha finiteness.

**Independent algebraic certifier:** over F11, for each nonzero \(u=(u_0,u_1)\), \(A_{23}u=(-u_1,u_0+5u_1)\), and
\[
\det[u,A_{23}u]=u_0^2+5u_0u_1+u_1^2\ne0
\]
because its quadratic discriminant is10, nonsquare mod11. The six-by-six determinant formed by the six image vectors equals \((\det S)^2\prod_q\det[u_q,A_{23}u_q]\), hence never zero. The script independently evaluates a full 6×6 Leibniz determinant=3 in one representative, checks all120 possible nonzero q23 orbits, and rejects dependent-row/reducible-action mutations.

## At every finite prime: the extension is unramified and SPLIT at support

At a place \(v\mid11\) of K, all THREE positive fine points are locally 11-divisible over K_v=Q11. Session51 explicitly constructs Qj∈E(Q11) for Z1 and Z2, with independent 11-division-polynomial verification mod 11^4; this session independently adds the missing third local division:
\[
\boxed{[11]Q_{Y_1}=P_2,\qquad
        Q_{Y_1}\equiv(225,4535)\pmod{14641}}
\]
on the short model \(y^2=x^3-1267x+17230\). The exact rational 18-multiple has formal parameter \(t([18]P_2)\equiv2541\pmod{14641}\), divisible by121, so the formal 11th root U exists with \(t(U)\equiv231\bmod1331\) and \(Q_{Y_1}=[5]P_2-[3]U\). A different algorithm using division polynomials through \(\psi_{13}\) checks \([11]Q_{Y_1}=(19,4)\bmod14641\). Both on-curve wrong-division mutations and formal correction omissions fail. Since \(\#E(\mathbf F_{11})=18\), E(Q11)[11]=0, and this determines the unique genuine local 11th root. At **both** split primes \(v,\bar v\mid11\), the same Q11 points are compatible under the rational-field conjugation.

At places \(v\mid2,117223\), the source-certified C0039 local quotient \(E(K_v)/11E(K_v)\) is ZERO (prime-to-11 component/reduction orders and 11-divisible pro-\(\ell\) identity group). Therefore every displayed fine point is 11-divisible already in \(E(K_v)\), even though no explicit bad-prime point coordinates are produced here. At complex places, local odd-11 division is automatic.

Fix **any** place \(w\) of \(L\) above such v. Every root of [11]Q=Y or Z differs from one K_v-rational root by a point of \(V=E[11](L_w)\). Thus **all** 11-division points already lie in \(L_w\). It follows that
\[
 \mathrm{Gal}(F_{\mathrm{fine}}/L)_{\mathrm{decomp},w}=\{1\}
 \quad\text{for every }w\mid\Sigma,
\]
i.e. every supported prime of L splits completely in F_fine/L.

At finite primes \(w\nmid\Sigma\), E has good reduction over the underlying K-place and the residue characteristic is NOT11. Standard étale Kummer theory for [11] on the Néron model implies that the division-point extension is **unramified** there. In particular this handles primes over7, where K/Q is ramified but E still has good reduction. Consequently F_fine/L is **everywhere unramified at all finite primes**. It is even split at every \(w\mid\Sigma\). This is an extension of the torsion field L, NOT an assertion that L/K or the anticyclotomic field D1 is unramified or locally split.

These bad-prime local divisibility and good-prime Kummer statements are independently named source dependencies; the finite Python script cannot prove local Néron-model theorems.

## New class-group consequence (not new general mathematics)

The Weil pairing places \(\mu_{11}\subset L\), so L is totally complex. By the existence theorem for the maximal everywhere-unramified abelian extension (Hilbert class field) and global Artin reciprocity, the actual finite abelian exponent-11 extension F_fine/L is a quotient of \(\mathrm{Cl}(L)\). Therefore
\[
\boxed{\dim_{\mathbf F_{11}}\mathrm{Cl}(L)/11\,\mathrm{Cl}(L)\ge6,\qquad
       11^6\mid h_L.}
\]
Moreover every \(w\mid\Sigma\) splits, so the **\(\Sigma_L\)-split class group**
\[
\mathrm{Cl}_{\Sigma_L}^{\rm split}(L)
=\mathrm{Cl}(L)/\left\langle[\mathfrak p]:
           \mathfrak p\mid2\cdot11\cdot117223\right\rangle
\]
has an F11 quotient of dimension **at least six**. (Complex places impose no extra obstruction.) As an \(H=\mathrm{Gal}(L/K)\)-module this quotient is the **threefold diagonal residual module** \(E[11]^3\), by conjugation functoriality of class field theory and the actual rational points; no assumption \(H=\mathrm{GL}_2\) is needed.

This is **a new explicit application for this particular torsion field**, not a novel class-field theorem or evidence for finite \(\Sha(E/\mathbf Q)\). The general MW-rank-to-unramified-division-field mechanism is known: see Jędrzej Garnek, *On class numbers of division fields of abelian varieties*, *Journal de théorie des nombres de Bordeaux* 31 (2019), 227–242, DOI https://doi.org/10.5802/jtnb.1077. Our input is different: three actual fine points at the first 11-level, plus finite Frobenius rank certifiers.

**Negative controls and claim boundaries:** If any one of the three projected rows is replaced by a dependent row, \(\det S=0\), and the dimension-six conclusion is no longer justified. If residual q23 were reducible or only scalar, the 2D conjugation step would fail. If a point were NOT 11-divisible at just ONE bad/11-adic supported place, the extension could ramify there and the ordinary ideal-class-group bound would not follow (only an S-ray-class bound might remain). The source C0039 bad-prime local quotient must not be silently replaced by a good-reduction assertion. **No class number of L has been directly computed**. Existence of an unramified abelian quotient supplies a rigorous class-number divisibility implication only if all recorded arithmetic and source hypotheses hold.

## Reproduction and next research decision

Run the new standard-library exact verifier
  python3 -I -B research/proof_labs/session52_fine_kummer_classgroup_gate.py
and the inherited local divisor checks
  python3 -I -B research/proof_labs/session51_local_division_fine_detectors.py
together with Session46's independent PARI-GP full five-prime Kummer oracle and Session33's independently verified K_v local matrix. Source theorem: Silverman, *Arithmetic of Elliptic Curves*, for [11] étale Kummer at good primes and p-adic formal groups; Artin global class field theory for the ideal class quotient.

**Research relevance:** We now have an **actual** six-dimensional finite abelian *fine* Galois quotient of \(G_L\), unramified everywhere and split at all supported places. This gives a source-matched finite arena in which to represent the compact-support fine dual classes and test eventual secondary obstructions; abstract toy groups are no longer the only finite laboratory. But the missing arithmetic first corrected cochain over \(G_K\) is still absent, and neither the ideal class quotient nor local Q11 witnesses evaluate \(D_1,D_2\), a genuine Selmer h², original complex L'' or BSD. The next mathematically decisive task remains to build an actual supported first corrected c1 and compute its secondary compact-support pairings; stop pursuing raw division precision beyond what is needed for that map.

**Status:** Source-conditional computational certificate and established general local/class-field theorem specialization, not human-reviewed. No new C-series status promotion, no immutable WPR alteration, no merges without authorization and passing CI. **New implication toward general BSD: NONE.**
