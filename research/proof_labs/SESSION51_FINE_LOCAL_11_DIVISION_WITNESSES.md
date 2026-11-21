# Session51 — two genuinely local 11-division points for the secondary fine-MW detectors

**2026-11-21, America/New_York. AI-assisted finite local arithmetic, not independently human reviewed.** Stacked on Session50 / draft PR #93. This is an actual arithmetic *local* construction on the focal elliptic curve, not an explicit global first correction, genuine secondary height, or implication toward BSD. The immutable Nov20 WPR and C-series claim ledger are unchanged.

## Question and pass/fail specification

Can we replace the abstract statement "the two fine test classes Z1,Z2 are locally divisible by 11" with explicit **11-adic local division points**, independently verified by a different group-law formula, so that the local nullhomotopies required by compact-support Poitou–Tate can be anchored at real points?

Inputs are the ACTUAL short Weierstrass model
  E: Y² = X³−1267X+17230
(isomorphic over Q to minimal [1,−1,0,−79,289]), the four rational points
  P1=(15,40), P2=(19,4), P3=(23,16), P4=(31,88)
and the two fine positive classes from Session50
  Z1=−2P1+3P2+P3, Z2=−9P1+6P2+P4.

**Predeclared acceptance threshold:** produce Q1,Q2∈E(Q11) such that [11]Qj=Zj, with fully specified reductions mod 11^4=14641. Independently check [11]Qj using **division polynomials** rather than the formal-group method used to construct them. Mutate each point by a NONZERO formal translation still on E and show the target equality fails. A merely vanishing logarithm or an unvalidated 11-division-point search is not enough.

## Exact result and dual model arithmetic

The exact rational MW group law supplies these coordinates reduced modulo 14641:

| Point | x mod14641 | y mod14641 | role |
|---|---:|---:|---|
| Z1 | 1963 | 11547 | actual rational fine MW combination |
| Z2 | 12587 | 6055 | actual rational fine MW combination |
| **Q1** | **3612** | **6189** | local 11th root of Z1 |
| **Q2** | **13874** | **12447** | local 11th root of Z2 |

These exact congruences have been reproduced using two independent algorithms: a formal-group-based construction with Jacobian multiplication and, independently, the standard short-Weierstrass **division-polynomial identities** for [11].

On the original curve E mod11, exhaustive affine point enumeration gives **#E(F11)=18**, so E(Q11)[11]=0 (good reduction, no residual 11-torsion and formal group torsion-freeness for p=11). The mod11 map [11] is an automorphism of E(F11), and its kernel on E(Q11) is zero. Consequently any local 11-division point of a fixed Z is UNIQUE.

**Constructive local Hensel argument:** For each rational Zj, set Tj=[18]Zj∈E1(Q11). Let \(t=-X/Y\) be the short-model formal parameter at infinity, with \(E_1(\mathbf Q_{11})\simeq11\mathbf Z_{11}\) via the formal logarithm. The exact Jacobian 18-multiple produces:

| j | \(t([18]Z_j)\pmod{11^4}\) | \(t(U_j)\pmod{11^3}\), where \([11]U_j=[18]Z_j\) |
|---|---:|---:|
| 1 | **14520** | **1320** |
| 2 | **12584** | **1144** |

Both t([18]Zj) are divisible by 11², giving an independent exact local divisibility certificate. Standard good-reduction formal-group theory implies [11]:E1(Q11)→E2(Q11) is an isomorphism (defined by multiplying formal logarithms by11). Therefore UNIQUE actual Uj∈E1(Q11) exists with [11]Uj=Tj. Define, **as an exact equality of p-adic points**,
  \[
  \boxed{Q_j=[5]Z_j-[3]U_j.}
  \]
Then [11]Qj=[55]Zj−[54]Zj=Zj. This constructs actual 11-adic division points, not merely residues satisfying a formal equation.

**Why the precision arithmetic is valid:** For a short model Y²=X³+AX+B with t=−X/Y, the invariant differential gives log_E(t)=t+O(t^5), with the n-th coefficient n-adically integral after multiplication by n. For t∈11Z11, every omitted term is divisible by at least11^4 (in fact more). Thus at these precisions t(Uj)≡t(Tj)/11 mod11³, and translation of a finite point (x,y) by a formal element of parameter s∈11Z11 has the exact degree-three reductions
  \[
  x' \equiv x+2ys+(3x^2+A)s^2+4xys^3 \pmod{11^4},
  \]
  \[
  y' \equiv y+(3x^2+A)s+6xys^2+
                   (10x^3+6Ax+4B)s^3 \pmod{11^4}.
  \]
With s=−3t(Uj) these produce the displayed Q1 and Q2. The power-series proof only guarantees the claimed finite precision; it does NOT claim the displayed residues uniquely define p-adic points without the formal-log existence argument.

## Orthogonal multiplication check: exact division polynomials

The separate verifier implements standard short-Weierstrass division polynomials ψ0=0, ψ1=1, ψ2=2y, ψ3=3x⁴+6Ax²+12Bx−A², ψ4 and the exact even/odd recursions through ψ13, then checks
  \[
  x([11]Q)=x-\frac{\psi_{10}\psi_{12}}{\psi_{11}^2},\qquad
  y([11]Q)=\frac{\psi_{13}\psi_{10}^2-\psi_9\psi_{12}^2}
                   {4y\psi_{11}^3}\pmod{11^4}.
  \]
All required denominators are 11-adic units for these two points. The resulting exact congruences are
  [11](3612,6189)=(1963,11547),
  [11](13874,12447)=(12587,6055) (mod14641).
This verification does NOT use the Jacobian 18-multiple, the ODE for formal translation, or the logarithm construction; it is a different finite arithmetic algorithm and source assumption.

**Adversarial negative control:** Translate each Qj by a nonzero formal point of parameter11 (the group law preserves the curve) and verify its [11] multiple is NOT Zj mod14641. Swapping the two targets also fails. If the formal 11-division factor, coefficient or target is corrupted, the independent ψ11 equality rejects it. The checker records the short curve, exact rational group combinations, #E(F11), both formal parameters, the two independent [11] checks and on-curve mutants.

## Global corollary: an ACTUAL fine Kummer field of relative degree \(11^4\), split at every supported place

The local witnesses also suggest a useful genuinely **global** arithmetic object. Let
  \(L=K(E[11])\), \(F_Z=L([11]^{-1}Z_1,[11]^{-1}Z_2)\), and \(V=E[11]\).
Then \(F_Z/L\) is a Galois Kummer extension of exponent11. In fact, **under the previously certified Session46 good-prime Kummer/Frobenius inputs**, its Galois group is the **FULL** \(V^2\), so
\[
\boxed{\operatorname{Gal}(F_Z/L)\simeq E[11]^2\simeq(\mathbf F_{11})^4,\qquad
[F_Z:L]=11^4=14{,}641.}
\]
This corollary requires only two of the five Session46 pure-Frobenius rows, not the full residual \(\mathrm{GL}_2(\mathbf F_{11})\) image, the global C0040 height oracle or first-corrected classes.

**Independent two-prime proof:** use the Session46 q743 and q2843 principal split prime orientations, both with anticyclotomic character0 and simple residual 1-eigen Frobenius. Their five-point Kummer reduction rows are \(r_{743}=(1,0,0,2,6)\) and \(r_{2843}=(1,4,9,9,1)\). Project to the coefficient vectors of \(Z_1=(-2,3,1,0,0)\) and \(Z_2=(-9,6,0,1,0)\), obtaining
  \(s_{743}=(9,4)\) and \(s_{2843}=(8,2)\).
The determinant is \(9\cdot2-4\cdot8=-14\equiv\mathbf 8\bmod11\ne0\). Their Frobenius powers in \(\ker\rho\) therefore give two Kummer translation vectors \(u_{743}\otimes s_{743}\), \(u_{2843}\otimes s_{2843}\) with nonzero \(u_q\in V\). Conjugation by the actual q23 Frobenius, whose mod11 action is irreducible, supplies \(A_{23}u_q\otimes s_q\), independent from the first for each q. The resulting four vectors span **all** \(V\otimes\mathbf F_{11}^2=V^2\), independently of the unknown local-to-global E[11] basis identifications. The new script checks the determinant, all120 nonzero q23 orbits and the full four-vector span (with rank-reducing mutation controls). The inputs for the Frobenius norm-to-Kummer translation bridge were independently checked in Session46, and remain explicit dependencies.

**Local splitting at the finite support \(\Sigma\):** For both places \(v\mid11\), our actual Qj∈E(Q11)=E(K_v) yield all the division points of each Zj after adjoining \(E[11]\), which is already contained in L. Therefore **every prime of L over \(v\mid11\) splits completely in \(F_Z/L\)**. For places \(v\mid2\) and \(v\mid117223\), the previously checked C0039 local Kummer quotient \(E(K_v)/11E(K_v)=0\) gives local divisibility of Zj, so the same conclusion holds. Archimedean places of K are complex, giving no residual odd-11 decomposition obstruction. By good-reduction Kummer theory, \(F_Z/L\) is unramified outside the places above \(\Sigma\); consequently it is **everywhere unramified and completely split at all primes above \(\Sigma\)**. These statements are relative to L, **not K**: the torsion field L/K itself can ramify at 11. Do **not** erroneously claim the full compositum with anticyclotomic D1 is locally split, since D1 is ramified at 11.

Thus we have a concrete **finite fine-Kummer quotient** of the actual Galois group over L, with full relative group and trivial supported decomposition groups. This fits the *object type* of compact-support cohomology more closely than a generic mod11 group countermodel. It does **not** construct the first corrected affine extension \(M_2/B_x\), compute the global second obstruction, or provide a Greenberg-Selmer class.

**Adversarial boundary:** two unrelated residue-field signatures do not identify a common global torsion basis; irreducible q23 conjugation is essential. The relative full-image conclusion would fail if either projected row were zero/dependent or the actual Frobenius had reducible action. The local-splitting conclusion additionally depends on C0039's BAD-PRIME local divisibility, not solely on the two p=11 point computations. These hypotheses should be checked independently before promoting this corollary beyond an internally reproduced, source-dependent arithmetic deduction.

---

## What this gives the compact-support arithmetic calculation

Both Zj are positive Q-rational points, and 11 **splits** in K=Q(sqrt−7). At the two places v,\bar v|11, the rational subfield embeds as the SAME Q11, so the uniquely determined Qj∈E(Q11) are naturally **compatible under complex conjugation**. This explicitly anchors the local divisibility at BOTH ordinary primes and avoids having to treat the two p-adic scalar coordinates as independently chosen.

For a chosen global 11th division point \(\widetilde Z_j\in E(\bar K)\), its global Kummer cochain is \(s\mapsto s\widetilde Z_j-\widetilde Z_j\). The local point Qj determines an exact local torsion adjustment \(\widetilde Z_j-Q_j\in E[11]\), which yields a local **degree-zero nullhomotopy** of the restriction of the Kummer cocycle at each v|11. This is the correct kind of object to insert into the compact-support Poitou–Tate pairing against a hypothetical computed global β2 class.

**Boundary:** We have *not* selected/evaluated \(\widetilde Z_j\) as an algebraic point in a global splitting field, nor computed the action of the local Galois group on the torsion adjustment. Thus the numerical Qj residues are concrete local reference points but NOT a fully evaluated Galois cochain or a Poitou–Tate pairing. Bad-prime local nullhomotopies outside 11 and the global first corrected class are also missing. A nonzero D1/D2 still has NOT been measured.

## Reproduction and research choice

Run:
  python3 -I -B research/proof_labs/session51_local_division_fine_detectors.py

All operations use standard-library fractions and modular arithmetic at 11^4. The construction route and division-polynomial route are independent algorithms but share the short-model constants/point inputs; neither is independent human peer review. For underlying formal-group standard mathematics see Silverman, *The Arithmetic of Elliptic Curves*, 2nd ed., Chapter IV and VII, and Session37's actual local formal log/norm construction.

**Next decisive test:** use the now-specified local Q1,Q2 as compact-support local trivialization origins, then actually construct a normalized global first correction c1 for a positive x, evaluate the global second 2-cocycle, and pair against the two Zj via a fully specified reciprocity/compact-support chain map. A measured nonzero pair would obstruct every supported global T³ lift of x. Merely reproducing the two local Qj again, or incrementing the same precision without a Galois cochain, is not productive.

No new implication toward **general BSD**, focal original complex L''(E,1)=0, nonzero fourth derivative, Sha finiteness or leading coefficient. **NONE**. H1/H3 stay active; H2's narrow local input advanced. Preserve all source assumptions (C0039/40/44/47) and all 50 existing claim statuses. Do not merge pending CI, independent audit and authorization.
