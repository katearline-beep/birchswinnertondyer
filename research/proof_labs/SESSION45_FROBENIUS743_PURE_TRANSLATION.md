# Session45 — a second actual arithmetic Frobenius witness: the pure Kummer prime 743

**2026-11-20, America/New_York. AI-assisted exact finite-field/class-character arithmetic and conditional group deduction, not independently expert reviewed.** Parent is Session44 / draft PR #86. No new proved implication toward *general* BSD or the original curve's exact complex L''(E,1)=0, nonzero fourth derivative, original Sha finiteness or full BSD leading coefficient. This is a sharper H1 finite-quotient and local-cohomology gate; historical WPR-Nov20 current.json remains the standing review.

## New mathematical question / predeclared acceptance test

Can one find a **single actual unramified Frobenius power** w such that (i) rho(w)=1, (ii) the actual first anticyclotomic character ell(w)=0, (iii) the residual Kummer cocycle c₀(w) of x=P₂−2P₁ is nonzero, thus replacing Session42's formal product w=g h² with a genuine prime Frobenius power? And can this new prime independently test a bad shortcut from the residual characteristic polynomial to the number of higher unramified local cohomology lifts?

**PASS at the split degree-one K-prime over rational 743** subject to the inherited source normalization of C0033's ray-class character. The exact arithmetic is newly reproduced below and in two independent computational paths. This is *not* an evaluated global first or second correction.

## Exact number-field and finite-reduction data

Let K=Q(√−7), ω=(1+√−7)/2, E on the minimal model [1,−1,0,−79,289], and use the short model Y²=X³−1267X+17230 for the finite reduction. Choose

\[
\mathfrak q_{743}=(27-14\omega),\quad
N(27-14\omega)=27^2+27(-14)+2(-14)^2=743,\quad
\sqrt{-7}\equiv109\pmod{743}.
\]

The prime orientation is checked directly:
  109²+7=16·743,
  27−14·(1+109)/2 = 27−770 = −743 ≡0 mod743.

For the *actual* C0033 anticyclotomic character, ω=16 mod121 and the conjugate ωbar=1−ω=−15 mod121. With the same arithmetic Frobenius/inverse-Iwasawa convention as Sessions30/38,
  a+bω = 27−14·16 =45 (mod121),
  a+bωbar =27+210=116 (mod121),
  ratio =45/116=112 (mod121),
  ratio^10=1 (mod121),
  **ell(Frob_q743)=log_12(1)=0 mod11**.
Both conjugate choices give zero. This calculation is independently reproduced by PARI ray-class coordinates calibrated once against ω, just as in the existing Session38 arithmetic oracle.

Exact point counting gives
  #E(F743)=770=70·11, a743=743+1−770=−26.
The mod11 Frobenius polynomial is
  X²−a743 X+743 ≡ X²+4X+6=(X−1)(X−6).
Its order on V=E[11] is10. **It is exactly the same residual characteristic polynomial as at q127**, even though ell(Frob127)=4 while ell(Frob743)=0.

On the short model the points P1=(15,40), P2=(19,4) reduce. Exact independent group laws give
  T743=[70]P1=(114,527), [11]T743=O,
  [70]P2=O,
  [70](P2−2P1)=[9]T743=(185,342) ≠O.
The earlier Session31 five-prime reduction certificate independently recorded q743's MW signature row (1,0,0,2,5), so the x coefficient is 0−2·1=9 mod11, agreeing with the full point calculation. Unlike a mere character-polynomial computation, this certifies the actual local unramified Kummer class is nonzero.

Define
  h=Frob_(q23)^12 and w=Frob_(q743)^10
as elements of G_(K,Σ), using the same choice of arithmetic Frobenius and decomposition-group embeddings as Session38. Then
\[
 \rho(h)=\rho(w)=1,\quad \ell(h)=2,\quad \ell(w)=0,\quad
 c_0(h)=0,\quad c_0(w)=u_{743}\ne0.
\]
The c₀(h)=0 fact uses the q23 Frobenius order12 and zero 12-term norm operator; the c₀(w)≠0 fact uses the q743 11-primary reduction. The actual vector u743 is **not** identified with the displayed reduced coordinate (185,342) in a globally fixed torsion basis. There is no implicit choice of 11-division point or comparison of q743 and q127 torsion bases.

## Two new exact necessary relations, independent of all unknown corrections

For *every hypothetical* global first correction c=c₀+Tc₁ obeying the inverse action \(\rho(s)(1+T)^{-\ell(s)}\),

\[
\boxed{c_1([h,w])=-2u_{743}=9u_{743}\ne0.}
\]

For *every hypothetical* global SECOND correction c=c₀+Tc₁+T²c₂,

\[
\boxed{c_2([h,[h,w]])=4u_{743}\ne0.}
\]

The first equation is the same algebraic commutator law as C0050 but applied to **an independently identified arithmetic prime** with character zero; the second is the Session43 double-bracket law. Both follow directly from the affine cochain equation because h,w∈ker rho, ell(w)=0, c₀(h)=0, c₀(w)≠0. Every c₁(h),c₁(w),c₂(h),c₂(w) cancels; this is an exact conditional necessity and **does not claim any first/second cochain actually exists**.

**Practical improvement:** Session42's class-two and class-three Galois-image lower bounds can be obtained from h,w at primes **23 and 743 alone**, without the auxiliary word Frob127^10 · Frob23^24. Since rho(Frob23) has an irreducible degree-two polynomial, conjugating u743 by it gives a second independent V direction, which then forces the full translation modules V[T]/T² and V[T]/T³ if the respective lifts exist. This supplies an **orthogonal arithmetic witness for the same conditional image theorem**, not a new BSD consequence or a new distinct conjecture.

## A real arithmetic H¹_unramified negative control: 127 versus 743

Both q127 and q743 have (mod11) Frobenius polynomial (X−1)(X−6), and at both primes x has a nonzero residual unramified Kummer class. Their anticyclotomic characters differ:
  ell(Frob127)=4 ≠0,
  ell(Frob743)=0.

Let A_r=V⊗F11[T]/T^r with the actual character twist, r=1,2,3. Because unramified local Galois groups are procyclic,
  H¹_unr(K_q,A_r) ≅ A_r / (rho(Frob_q)(1+T)^(-ell(Frob_q)) −1)A_r.

At q127 the 1-eigenspace forms **one nontrivial Jordan chain of length r**, so the above cokernel has dimension1 and its map to H¹_unr(K_q,V) is an isomorphism. At q743, ell=0 makes its 1-eigenspace **r separate Jordan blocks of size one**, and its cokernel has dimension r. Consequently:

| r | dim H¹_unr at q127 | dim H¹_unr at q743 | number of H¹_unr lifts of a fixed residual class at q743 |
|---|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 11 |
| 3 | 1 | 3 | 121 |

Here “number of lifts” is the number of cohomology classes in the affine fibre, not distinct cochain representatives. Neither prime contributes a new obstruction to *existence* of an unramified local lift; the comparison exposes the **difference in ambiguity** caused solely by the character, at two actual good primes with matched residual Frobenius conjugacy classes. This eliminates the false shortcut “the same E[11] Frobenius polynomial implies the same higher-local lift space.” It also demonstrates why a local reference value from q127 cannot simply be copied to a q743 calculation or a common global torsion basis.

The finite matrix verifier checks ranks of Frob−1 on A_r over F11 for all r, with q23 as a zero-H¹ control and a wrong-character mutation. The PARI oracle independently checks q743's point count, exact reductions, Artin character and Frobenius order, and the Python transcript parser rejects modified, truncated and error-bearing rows.

## What this does and does not unlock

This strengthens the H1 **necessary finite-quotient data** and identifies a cleaner actual Frobenius generator that can test any proposed 121-kernel arithmetic realization, in addition to the original q127 and the abstract group checks. It is **actual elliptic arithmetic at a new prime**, rather than just an artificial group countermodel.

It does **not** produce the first global c₁, a complete Galois presentation, the Greenberg local maps at both primes over11, the C0049 local reference comparison, the second Selmer Bockstein, Sha finiteness or original complex L'' vanishing. The fact that q743 is good and outside Σ makes its unramified local lift calculations easy; the hard compatible global/local support problem is unchanged.

**Next decisive falsifier:** any proposed explicit first corrected field over B=L([11]⁻¹x)D1 must realize the 23/743 pure-Frobenius first bracket above *and* the earlier 23/127 bracket, agree with all full group relations and local ordinary conditions, and furnish a Shapiro-normalized cochain. The second bracket is a T³ necessary test **only after** an actual first correction exists. Do not confuse character-zero at q743 with vanishing of the Kummer class or with an implicit globally evaluated c₁.

## Reproduction and citations

- Standard-library exact finite arithmetic plus 11⁴ exhaustive correction-coordinate controls:
  \`python3 -I -B research/proof_labs/session45_frobenius743_pure_translation.py\`
- Independent PARI minimal-model/ray-class oracle:
  \`gp -q -f research/proof_labs/pari_frobenius743_oracle.gp > /tmp/bsd-frob743.txt 2>&1\`
  \`python3 -I -B research/proof_labs/session45_frobenius743_pure_translation.py /tmp/bsd-frob743.txt\`.
- Source precedent: C0033 / Session30 actual anticyclotomic ring-class Artin calibration; C0035 / Session31 five-prime saturation matrix; C0050 / Session38 q23/q127 Frobenius and commutator equation; Session43 second-bracket conditional identity. The independent PARI code uses bnrinit and bnrisprincipal; it remains an implementation, not an external human mathematical review.

CI must run all relevant checks before merge. We do not change C-series claim statuses in this sprint or alter the standing dated WPR. **New proved mathematical implication toward BSD: NONE.**
