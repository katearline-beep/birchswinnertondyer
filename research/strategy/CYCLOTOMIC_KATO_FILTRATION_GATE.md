# C-0008 — The cyclotomic (11)-tower and a finite-layer false-positive trap

**Date:** 2026-10-17. **Status:** established elementary algebra and a source-level correction to our research plan. Exact Python and independent PARI/GP checks; no Kato zeta element or new BSD theorem computed. Expert review of higher arithmetic conclusions remains open.

## 1. Prefer the canonical first layer, not an arbitrary (C_{11})-field

For (p=11), let (Q_infty/mathbb Q) be the cyclotomic (mathbb Z_{11})-extension, and (Q_n) its degree (11^n) subfield. The first nontrivial layer
[
Q_1=mathbb Q(zeta_{121})^{C_{10}},qquad [Q_1:mathbb Q]=11
]
is **totally real and ramified only at 11**, because ((mathbb Z/121mathbb Z)^	imessimeq C_{110}). All ten nontrivial characters of (operatorname{Gal}(Q_1/mathbb Q)) have conductor (121), so the conductor–discriminant formula gives
[
operatorname{disc}(Q_1)=121^{10}=11^{20}.
]

Our previous proposal (F_{23}=mathbb Q(zeta_{23})^+) is also real cyclic of degree 11, but ramifies at **23**, has discriminant (23^{10}), and is **not a layer** of the cyclotomic (mathbb Z_{11})-extension. A first-layer group-ring computation over (Q_1) is directly compatible with Burns–Kurihara–Sano's Iwasawa–Darmon derivatives and transition maps, whereas (F_{23}) is a different legitimate but less canonical test. [Independent PARI/GP polynomial and field discriminant oracle](cyclotomic_field_oracle.gp) checks this distinction.

### The crucial qualification in Burns–Kurihara–Sano (2024)

In their published paper, *On derivatives of Kato's Euler system for elliptic curves*, [§4, p.876](https://kurihara.math.keio.ac.jp/bks4.pdf), the authors state **at the beginning of the section**:

> Throughout this section, we assume that (H^1(mathbb Z_S,T)) is (mathbb Z_p)-free and (Sha(E/mathbb Q)[p^infty]) is finite.

Their **Proposition 4.4**, [p.879](https://kurihara.math.keio.ac.jp/bks4.pdf), proves that an appropriately modified Iwasawa Kato zeta class lies in (I_n^a H^1_n), with (a=max(0,r_{m alg}-1)=3) in our case, under this **standing hypothesis**. The introduction's phrase “no conjecture is needed” to obtain the limiting class **does not erase the assumption** of (Sha(E/mathbb Q)[11^infty]) finiteness.

This gives a genuine improvement over our earlier trial field *only in the scope of the difficult arithmetic assumption*: we can use a cyclotomic-tower result requiring finiteness of the **base-field** (11)-primary Sha, rather than the (11)-primary Sha of the non-cyclotomic extension (F_{23}). **Neither finiteness statement has been proved for our rank-four curve.** Hypothesis 2.2 on [p.866](https://kurihara.math.keio.ac.jp/bks4.pdf) also records the same finiteness condition. The (mathbb Z_{11})-freeness condition is compatible with irreducible (E[11]), but exact applications should still trace the particular modified module (T).

**More importantly, the authors' Conjecture 4.8 / their leading-term comparison is a conjecture**; the proven *augmentation containment* does not imply the original complex equation (L''(E,1)=0). Do not mistake conditional Iwasawa theory for a proven analytic-rank bridge.

## 2. Finite group-ring layers, exactly

Let (G_n=C_{11^n}=langlesigma_nangle), let
(R_n=mathbb Z_{11}[G_n]), and (T_n=sigma_n-1).
Then
[
R_nsimeqmathbb Z_{11}[T_n]/((1+T_n)^{11^n}-1),qquad I_n=(T_n).
]
Since (11^nT_n^3in I_n^4), and reduction to
((mathbb Z/11^n)[T]/(T^4)) witnesses exact order, elementary algebra shows
[
oxed{I_n^3/I_n^4 simeq mathbb Z/(11^n)}
]
for (nge1). In particular (I_1^3/I_1^4simeqmathbb F_{11}), whereas (I_2^3/I_2^4simeqmathbb Z/121). At infinite level,
[
Lambda=mathbb Z_{11}[[T]],quad I^3/I^4simeqmathbb Z_{11}.
]
The finite first layer therefore reads only one (11)-adic digit of the third graded coefficient.

**Negative control 1: an apparent first-layer zero.** A genuine nonzero Iwasawa-level class (11T^3) maps to **zero** in (I_1^3/I_1^4) but to a **nonzero** element in (I_2^3/I_2^4). A single finite-level zero thus does **not** prove a zero of the limiting class.

## 3. Even deeper false positives from reducing the full norm modulo 11

Let (mathcal T_n=sum_{gin G_n}g) be the **ordinary scalar trace/norm element** of (R_n). This is **not** the BKS *cohomology-valued derived Kato norm*, and is used here **only as an algebraic negative control**.

Its integral augmentation is (11^n
eq0), hence (mathcal T_n
otin I_n). Yet in characteristic 11,
[
overline{mathcal T}_n
=rac{(1+T_n)^{11^n}-1}{T_n}
=T_n^{11^n-1}inoverline I_n^{10}.
]
Thus a naive “mod-11 order at least three” test would return **true**, while even the integral first-order augmentation claim is **false**. This is exactly the sort of leapfrog-conjecture false positive that our harness should reject before a large computation.

[Exact anti-vacuity program](cyclotomic_integrality_gate.py) checks both (n=1) and (n=2), the finite graded sizes, the misleading mod-11 scalar norm, and the (11T^3) lifting trap. These tests are *algebraic models* of the error, not evidence that BKS zeta elements exhibit it.

A second useful control: for (G=C_2) with (p=11), (T^2=-2T), and (-2inmathbb Z_{11}^	imes), so (I^2=I) and (I^3/I^4=0). This explains why a real quadratic field is a vacuous choice for a third graded experiment.

## 4. Leapfrog decisions

- **G0 already passed:** Distinguish the derived Kato augmentation class from the *complex* L-function; identify the missing reciprocity arrow.
- **New G1 gain:** Use the actual cyclotomic (Q_1), and monitor the compatible (Q_2) rather than study only (F_{23}). Avoid mod-11 norm and first-layer false positives.
- **Outstanding mathematical prerequisite:** (Sha(E/mathbb Q)[11^infty]) finiteness still cannot be assumed for the rank-four curve.
- **Most valuable new theorem target:** a **non-circular, explicitly defined comparison** connecting a certified cyclotomic derived class/Bockstein regulator to the complex second derivative, not merely to the unrelated (11)-adic (L)-function. No such comparison has been obtained.
- **Cheap next test:** Identify a concrete modular-symbol / Selmer presentation giving even a nonzero, correctly normalized (I_1^3/I_1^4) class, and check whether one can compute it without first assuming the unknown (Sha) hypothesis. Estimate complexity and exit early if impossible.
- **Stop:** If all computed leading terms only detect their own mod-11 residue or the conjectured comparison explicitly presupposes analytic rank four, do **not** classify the result as progress on rank equality.

## Source/provenance notes

* Burns–Kurihara–Sano, *J. Math. Soc. Japan* **76** (2024), 855–919: [PDF](https://kurihara.math.keio.ac.jp/bks4.pdf), **Hypothesis 2.2 (p.866), standing assumption (p.876), Proposition 4.4 (p.879), Conjecture 4.8 (p.881)**.
* [PARI/GP `polsubcyclo` documentation](https://pari.math.u-bordeaux.fr/pub/pari/manuals/2.15.5/users.pdf) and [`nfdisc`](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html) for independently exact number-field checks.
* Our [leapfrog protocol](LEAPFROG_PROTOCOL.md) and [H1 prior audit](KATO_BRIDGE_AUDIT.md).

**Nonclaims:** no computed Kato class, proof of analytic rank four, (11)-Selmer upper bound, (Sha) finiteness, new BSD theorem, or external mathematical peer review.
