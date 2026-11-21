# Session46 — five pure Frobenius witnesses certify the FULL joint Kummer–anticyclotomic image

**2026-11-20, America/New_York. AI-assisted finite arithmetic and source-dependent arithmetic deduction; not independently expert reviewed, no novelty or BSD proof claimed.** Stacked on Session45 / draft PR #87. Existing WPR-Nov20 and its 50 C-series claim statuses are not changed. This refines the arithmetic-field part of C-0035/36 without relying on the previously assumed *full* residual GL₂ image or the whole five-class Sah/inflation argument.

## Precomputation whole-problem checkpoint and decisive question

General BSD still requires rank equality for every E/Q, Sha finiteness, and the complete normalized leading-coefficient formula. For our rank-four E=234446.a1 the **original complex** L''(E,1)=0 and L^(4)(E,1)≠0, Sha finiteness, and the BSD coefficient remain unproved. The conditional first H¹ lift in C-0047 does **not** make the second corrected class exist or prove complex analytic rank four. **New implication toward BSD: NONE.** H1 remains arithmetic construction, H2 second genuine Selmer Bockstein, H3 missing characteristic-zero complex third derivative, H4/H6 parked, H5 only diagnostic.

**Question selected:** Can a handful of **actual** split Frobenius powers, all with ell=0 but nonzero Kummer translations for five points, certify Gal(F₅D₁/K(E[11]))=E[11]^5×C11 **without** full rho(G_K)=GL₂(F11), and reject the tempting but invalid use of a q≡1 mod11 double-eigenvalue prime?

**Answer: yes, conditioned on the previously recorded C-0033 class-field normalization and standard local good-reduction Kummer identification.** The finite arithmetic below was computed independently by Python short-model point arithmetic and PARI minimal-model/ray-class arithmetic. The deductive step uses only elementary Galois conjugation and the 2D irreducibility of rho(Frob23).

## Typed objects and hypotheses

Let K=Q(sqrt(-7)), omega=(1+sqrt(-7))/2, E on the minimal model [1,-1,0,-79,289], V=E[11], L=K(E[11]). Let P1,P2,P3,P4 be the four recorded rational points with short-model coordinates (15,40),(19,4),(23,16),(31,88), and R=(-3355/63,128780 sqrt(-7)/1323)∈E(K) on that short model. Write X=(P1,P2,P3,P4,R). Fix Q_i with [11]Q_i=X_i, and F₅=L(Q_1,...,Q_5), the full five-point Kummer splitting field over L. Let D₁/K be the **actual anticyclotomic first degree-11 layer**, with C0033 character ell:G_K→F11 and ramification at 11 only. Let B₅=F₅ D₁.

For each i define the actual residual Kummer cocycle c_i(s)=sQ_i−Q_i∈V and joint C(s)=(c_1(s),...,c_5(s))∈V⁵. This is a G_K 1-cocycle, and its restriction to N=ker rho is a homomorphism to additive V⁵. Both C and ell factor through finite Galois extensions by construction. No first-order corrected cocycle c1 is assumed anywhere in this theorem.

**Source inputs:** C0033/Session30 ray-class reciprocity establishes ell using the calibrated ratio (a+16b)/(a−15b) modulo121 for a principal split prime (a+b omega), raised to the 10th power and logged base12. The good-reduction exact sequence identifies E(F_q)/11E(F_q) with H¹_unr(K_q,V)=V/(rho(Frob_q)−I)V. The full residual rho(G_K)=GL₂(F11), finite twist Sha hypotheses and derived-height claims are NOT inputs. These standard source statements and the arithmetic source specialization still merit independent subject-matter review.

## Five exact independently checkable pure Frobenius rows

At each prime q below use the specific principal ideal (a+b omega), with **norm q**, and the corresponding chosen embedding sqrt(-7)=r modq, where (a+b(1+r)/2)=0 modq. The listed row is the five-point Kummer reduction signature relative to T_q=[#E(Fq)/11]P1, a nonzero order-11 point in E(Fq).

| q | a,b | sqrt(-7) mod q | #E(Fq) | rho(Frob) order m | T_q on short model | (P1,P2,P3,P4,R) reduction row |
|---:|---|---:|---:|---:|---|---|
| 743 | (13,14) | 634 | 770 | 10 | (114,527) | (1,0,0,2,6) |
| 2843 | (43,14) | 399 | 2893 | 5 | (2693,2385) | (1,4,9,9,1) |
| 3019 | (23,30) | 400 | 2959 | 5 | (1325,2149) | (1,8,0,4,1) |
| 5147 | (15,46) | 4474 | 5236 | 2 | (4813,1927) | (1,2,9,8,1) |
| 5737 | (71,8) | 4284 | 5632 | 10 | (832,2511) | (1,5,5,0,9) |

Each principal norm equation is a²+ab+2b²=q. Every q has v11(#E(Fq))=1 and q≠1 mod11; hence the mod11 Frobenius polynomial splits with **distinct** eigenvalues 1 and q mod11, with order m=ord_F11*(q)∈{2,5,10}. For each row the actual C0033 ratio has tenth power 1 modulo121, so **ell(Frob_q)=0** and therefore ell(Frob_q^m)=0. The whole five-by-five matrix of rows has **determinant 5 mod11** (checked by independent permutation expansion and Gaussian rank).

**Orientation control:** Session45 used the conjugate q743 prime, sqrt(-7)=109, for which the fifth coordinate is 5; here the conjugate embedding sqrt(-7)=634 yields fifth coordinate 6=−5 mod11. The sign change is the expected anti-invariance of R, not a disagreement between computations. All five roots in this table are fixed consistently by their principal norm generators.

## Source-dependent THEOREM: full relative image without full GL₂

Let N=ker rho and N₀=N∩ker ell, and set w_q=Frob_(mathfrak q)^m for the five primes above. The chosen good-prime Frobenius lifts satisfy rho(w_q)=1 and ell(w_q)=0, so w_q∈N₀.

**Local Kummer norm lemma:** For q with v11(#E(Fq))=1 and q≠1 mod11, put A_q=rho(Frob_q) with eigenvalues 1 and a=q mod11≠1, m=ord(a). For any Kummer class c_i unramified at q,
  c_i(Frob_q^m)= (1+A_q+...+A_q^(m−1)) c_i(Frob_q).
The norm operator is **m times the projector to the 1-eigenspace**, and m is invertible mod11. The Kummer isomorphism E(Fq)/11→V/(A_q−I)V, plus the common finite reduction row, implies
  C(w_q)=u_q ⊗ row_q ∈V⊗F11⁵,
for ONE nonzero vector u_q in the q-specific Frobenius-fixed line, and all five coordinates share the SAME u_q. It is essential that these are true local Kummer cocycles and the order-m Frobenius words; five unrelated finite-field rows would not themselves give five global translation vectors. No global torsion basis is inferred from the displayed coordinates of T_q.

**Irreducible conjugation:** Let sigma=Frob_(mathfrak q23). Its actual residual polynomial is X²+6X+1 (discriminant 10 is nonsquare in F11), so for every nonzero u∈V the vectors u and rho(sigma)u are linearly independent. Since N₀ is normal in G_K, the conjugates sigma w_q sigma^−1 also lie in N₀ and satisfy
  C(sigma w_q sigma^−1)=rho(sigma)u_q⊗row_q.
Thus the image C(N₀) contains **the entire V⊗span(row_q)** for each q (each two vectors span the V factor). The five rows have rank five, so
  **C(N₀)=V⁵**.
This argument needs NEITHER surjectivity of rho nor the transvection at bad prime117223 nor Sah cohomology. It uses only one irreducible Frobenius action and five actual unramified Kummer rows.

**Anticyclotomic factor:** The earlier C0050 computation gives h=Frob_(mathfrak q23)^12 with rho(h)=1 and ell(h)=2≠0. Its entire five-point Kummer translation is zero, because A23−I is invertible and sum_(j=0)^11 A23^j=0, so C(h)=0. Hence the image of
  N → V⁵×F11, s↦(C(s),ell(s))
contains V⁵×{0} by the five witnesses, and also (0,2), which generates {0}×F11. It is therefore the FULL product V⁵×C11.

**Corollary (actual arithmetic field conclusion):**
\[
\boxed{\operatorname{Gal}(B_5/L)\simeq V^5\times C_{11},\qquad
 [F_5:L]=11^{10},\quad [B_5:L]=11^{11}=285{,}311{,}670{,}611.}
\]
The degree-11 anticyclotomic field D₁ is linearly disjoint from the entire five-point Kummer splitting field F₅ over L, and the joint five-point Kummer action over L D₁ is full V⁵. These are **source-dependent exact arithmetic deductions**, not constructed defining polynomials of enormous degree. They remove the full-GL₂ dependence from the **relative** field-image/disjointness portion of C0036. They do NOT eliminate C0044/C0047's separate residual-image/Selmer hypotheses or establish a global c1/c2.

In particular, projecting from V⁵×C11 onto any nonempty subset of the five points yields the analogous full relative group for that subset, including x=P2−2P1. The degree for the one-point base B_x=L([11]⁻¹x)D₁ is **11³** over L even without rho(G_K)=GL₂. This independently reinforces Session44's base-field statement while retaining the source-dependent C0047 existence gate for the first 121-kernel extension.

## Adversarial no-go and distinction from earlier results

- **Invalid shortcut (actual q3851):** #E(F3851)=3938 is divisible by11 only once, and a residual reduction row might look useful, but **3851≡1 mod11** makes the residual Frobenius polynomial (X−1)². Its order may be 1 or11, and the needed norm projector cannot be inferred from the polynomial. We **exclude** this prime; simply using all five earliest rank-increasing character-zero rows would be unsound. The fifth accepted witness is q5737 instead.
- **Character mutation:** A prime can have a nonzero Kummer class and distinct eigenvalues but **ell(Frob)≠0** (q127 is the existing counterexample). Its Frobenius power does not lie in N₀. The pure translation argument requires BOTH conditions.
- **Rank mutation:** Replacing any one accepted row with a duplicate makes the 5×5 determinant vanish and reduces the pure translation span. The certificate checks a duplicate-first-row mutation; the group deduction fails in that model.
- **Basis/gauge mutation:** The finite projected points T_q have different residue fields and are NOT a shared global E[11] basis. The proof only uses the scalar ratios within EACH q-row; the irreducible q23 conjugation proves full span for **every possible nonzero u_q**. Exact 2×2 determinants were checked on all 120 nonzero vectors, while a deterministic 10×10 stacked witness rank check provides an independent sanity check.
- **No mathematical overreach:** This result supplies an **actual arithmetic quotient** of the residual Galois group and an exact splitting-field degree **relative to L**. It does not produce a first-corrected nonabelian quotient, global Bockstein, Selmer-complex map or noncircular complex L-function derivative equality. H1 remains blocked at that explicit first correction and Greenberg local gluing.

## Reproduce and independent verification

Standard-library certificate and fail-closed mutations:
  python3 -I -B research/proof_labs/session46_pure_frobenius_five_kummer.py

Independent minimal-model/ray-class PARI:
  gp -q -f research/proof_labs/pari_pure_frobenius_five_kummer.gp > /tmp/bsd-pure5.txt 2>&1
  python3 -I -B research/proof_labs/session46_pure_frobenius_five_kummer.py /tmp/bsd-pure5.txt

The Python script independently obtains all five good-prime counts, reductions, signatures and Frobenius orders on the short curve. PARI uses **another Weierstrass model** and ellcard/ellmul and certifies the K class number/ray-class character, including all 25 logarithms. Both rely on standard elliptic/Kummer reciprocity theorems and the source orientation C0033; independent code cannot replace expert review of those source claims. The rank-five determinant is 5 mod11; no floating-point zero or infinite series is involved. The source assumption C0033 anticyclotomic identification is not silently promoted to a theorem in this session.

**Next decisive H1 test:** With the now-explicit actual residual full V⁵×C11 image over L, build an arithmetic first-corrected representation for x over B_x, whose relative 121-kernel extension is known to exist only **under C0044/47's source hypotheses**. Candidate construction must supply its true global cocycle, algebraic/radicand and local Galois data, both ordinary Greenberg local maps and the C0049 Shapiro reference; compare the 23/127 AND 23/743 commutator constraints. Do not enumerate the huge Kummer polynomial directly. All 50 C-series statuses unchanged, and **new implication toward BSD: NONE**.
