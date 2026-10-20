# Session 28 — independent first-digit oracle and a source-defined second Bockstein

**2026-10-19 (America/New_York); AI-assisted, unreviewed.** Baseline: `4d2f6dfb9caac0160e30d08cca53de303377a127`, after merging Session27 PR #55 (all six workflow families passed). This session does not compute an arithmetic second height, bound the full Selmer group, or prove any new implication toward original complex BSD.

## The question chosen before computation

Can we remove the shared division-polynomial denominator machinery from the complete BCLMN **first-digit** calculation, and specify the actual second Bockstein's required input rather than guess a skew matrix from that first height?

Pass: an independent, import-free exact-coordinate/ideal implementation reproduces the four first digits and published controls; the second-stage construction has a proved lifting formula and explicit invariance tests. Failure: any discrepancy in the first digits, denominator primitivity, orientation, or lifting ambiguity halts interpretation. No extra precision-only calculation is selected.

The conservative lemma is the direct denominator-ideal identity below. The credible leapfrog remains LF-011: a true nonzero second height on exact non-universal first-radical classes. The wild option remains a cycle/complex-period comparison; no rank-four complex derivative theorem was found in the sources examined. All H1–H6 proof boundaries remain unchanged.

## C-0029: the denominator ideal directly from the multiplied point

Work on the minimal equation `y²+xy=x³−x²−79x+289`, in `O_K=Z[omega]`, `omega²−omega+2=0`. For a coordinate `x=N/D` with integral N and positive integer D, compute the principal ideal

\[
\operatorname{den}(x)=(D)/(N,D)=(\delta).
\]

This follows prime by prime from `v(den(x))=max(0,v(D)−v(N))`. The norm-Euclidean gcd computes `(N,D)` directly; `x*delta` is integral and its ideal gcd with delta is a unit. At a negative valuation of x on an integral minimal Weierstrass equation, comparison of valuations in the equation gives `v(x)=−2e`, `v(y)=−3e`, so `(delta)` is the **square** of the point denominator ideal `(d)`. No denominator generator from an earlier script or division-polynomial recurrence enters this construction.

Class number one and units `{±1}` let us avoid selecting a square root: `delta=±d²`, and the unit sign cancels under conjugation. BCLMN Proposition2.4 then gives, for `U=[n]Q`,

\[
h_\rho(Q)=\frac1{2pn^2}\log_p\left(
\frac{\sigma(t_+)^2\delta_-}{\sigma(t_-)^2\delta_+}\right),
\qquad t=-x(U)/y(U).
\]

All non-p denominator contributions are included through the exact global ideal. For **one height digit**, sigma integrality and `t in pZ_p` give
`(sigma(t)/t)²=1+a1*t mod p²`; the unknown E2/canonical sigma coefficient cannot affect this precision. This is a first-digit-only oracle, not independent certification of the second or third height digit.

Use `n=18`: it kills both order-18 reduction groups above11 and the I2/I1 bad component groups (orders divide2). The older convenient `36=2*18` is also valid; taking a multiple divisible by the **lcm** suffices. The new [18] calculation is compared to the old independent implementation at [36], avoiding a redundant large-coordinate multiplication in this oracle. Both embeddings have matching denominator/formal-parameter valuations; guard loss is explicitly checked. The p-adic logarithm of a unit q is evaluated modulo p² using `log(q)/p=((q^(p−1)−1)/p)/(p−1) mod p`.

The standalone [oracle](../anticyclotomic_11/direct_coordinate_height_mod11.py) imports **no repository code**. It uses integral-basis field arithmetic, minimal affine group law, direct multiplied coordinates, exact ideal gcd, and the squared formula above. It checks all four self-heights, all six mixed sums, two published 389a1/K=-11/p5 heights, opposite embeddings, a wrong sigma correction and a nonrational wrong ideal factor. These test implementation errors in global arithmetic; they share the BCLMN theorem and character normalization, and are **not independent human review or an independently maintained Sage/Magma global-height package**.

In the conventional polarized bilinear height, `h(P+R)=2<h(P),R>` because the eigenspace self-heights vanish; a common factor2 does not change the projective kernel. Its normalization against Howard/CH is still a separate obligation. No exact full-Selmer radical follows from these Mordell–Weil first digits.

## C-0030: the exact chain-level object needed for the second stage

The relevant primary source is Macias Castillo–Sano, [*On Selmer complexes, Stark systems and derived p-adic heights*, arXiv:2603.23978v1](https://arxiv.org/pdf/2603.23978), §4 and AppendixA (a 2026 **preprint**, not an asserted peer-reviewed result). Theorem4.2 identifies the Bertolini–Darmon and Nekovar filtrations and pairings **with a minus sign**, for `1≤k≤p−1`, under Hypothesis4.1. In particular k=2 is covered. Proposition4.7 and Remark4.8 supply a perfect, self-dual Greenberg Selmer complex; AppendixA describes the derived Bockstein via lifts.

Here is the explicit **applicability audit**, retaining dependence on existing arithmetic arguments rather than pretending a script verifies a Galois theorem:

* good ordinary p11: `#E(F11)=18`, `a11=−6` (C-0003/20);
* the split bad primes have types I2 and I1, so `Tam(E/K)=2²=4`, and `11∤4*18²`;
* C-0007's Tate-inertia/irreducibility group argument gives residual image containing `SL2(F11)` over Q, subject to its recorded expert-review boundary;
* that group also lies in the image over K: `G_K` is normal of index2 and `SL2(F11)` is perfect (elementary unipotents are commutators, using `a²≠1`);
* the determinant on `G_K` remains surjective because `K=Q(sqrt(-7))` is disjoint from `Q(zeta11)`, whose unique quadratic subfield is `Q(sqrt(-11))`. Thus the residual image over K is `GL2(F11)`, which contains a Cartan subgroup.

Consequently **on those standard arithmetic inputs**, the preprint provides the second-height comparison and the required Selmer-complex framework on this curve. It does not supply an executable presentation or show our BCLMN normalization agrees with its first pairing. It also does not compare either p-adic height to original complex `L''`.

For an actual finite-free two-term model `C=[C1 -> C2]` over `Z11[[T]]`, choose bases and write

\[
D(T)=D_0+TD_1+T^2D_2\pmod{T^3}.
\]

For `D0*x=0`, the first obstruction is `[D1*x] in coker D0`. If it vanishes, choose **a lift** x1 satisfying

\[
D_0x_1=-D_1x.
\]

Expanding `D(T)(x+Tx1)` proves the second obstruction is

\[
\boxed{\beta^{(2)}(x)=[D_2x+D_1x_1]
\quad\text{in } C^2/(\operatorname{im}D_0+D_1\ker D_0).}
\]

The quotient is indispensable: replacing x1 by x1+k changes the representative by D1*k. Only after evaluating the source-defined duality/cup product against an exact second-stage partner does this become the Nekovar second height (with the comparison sign above). A general multi-term complex requires its full spectral-sequence quotients; the formula here is explicitly for a two-term free presentation.

The [executable lift-and-quotient implementation](second_bockstein_lift.py) works on **synthetic** complexes over `F11[[T]]/(T³)`. Direct polynomial multiplication independently checks its lift residuals. It rejects invalid lifts and verifies ambiguity and T-dependent basis invariance. A sharp countermodel has raw D2=0 but a nonzero rank-two corrected obstruction; another has **identical D0,D1** and a different D2 cancelling that obstruction. Therefore neither the first height nor its additional 11-adic digits determine the second Bockstein. These examples are not Galois cohomology and are not claimed self-dual arithmetic height presentations.

## Exact next deliverable and stop rules

The missing data are now explicit: an actual finite-free presentation of the Greenberg Iwasawa Selmer complex to T³, including all local conditions, arithmetic representatives x/y, a certified first-order lift x1, and the self-duality map. We have **none of those matrices or arithmetic lifts**. Constructing them is the next substantive target; assigning the already-known first height to D1 without a chain-level comparison would be circular. Full Selmer signature (4,1), exact S2 membership and the complex bridge remain open.

A nonzero finite residue can certify nonzero arithmetic h2 only after these input/lattice/lifting identifications and error bounds. A zero residue mod11 **cannot** certify exact vanishing: `11*T²*J` with nonzero alternating J is zero mod11 and nonzero mod121. Thus Session26's zero-form control is an **exact model alternative**, never a finite-precision falsifier of Q11 nonvanishing. Universal norms still pair to zero at every stage by Howard Theorem4.2; they remain excluded as regulator witnesses.

Reproduce:

```
python3 -I -B research/anticyclotomic_11/direct_coordinate_height_mod11.py
python3 -I -B research/proof_labs/second_bockstein_lift.py
```

**Whole-problem outcome:** new independent arithmetic corroboration and a precisely executable homological interface; **no newly proved implication toward original complex L'' or BSD**. No novelty claim, no full-Selmer upper bound, no Sha finiteness, no actual nonzero h2, no rank-four analytic theorem.

Other primary sources: [BCLMN Proposition2.4 and §5.1](https://arxiv.org/pdf/1610.08729); [Howard Theorem4.2/Conjecture4.4](https://arxiv.org/pdf/1202.6343). Their mathematical validity is an input, not tested by Python assertions.
