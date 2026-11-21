# Session50 — two exact dual coordinates for the SECOND GLOBAL obstruction modulo the first-lift ambiguity

**2026-11-21 (America/New_York), AI-assisted conditional arithmetic/duality corollary, not independently expert reviewed.** Narrow follow-up to Session49 / draft PR #92, using pre-existing C0039, C0040, C0046/47 and the explicit defining-system ambiguity in Session36. **No new implication toward the original complex BSD conjecture.** Nothing is merged; all 50 C-series statuses and the immutable Nov20 WPR are unchanged.

## Problem and exact mathematical objects

General BSD requires rank equality, Sha finiteness, and the normalized leading-coefficient identity for every elliptic curve. For focal rank-four E=234446.a1, exact original complex L''(E,1)=0, L^(4)(E,1)≠0, original Sha finiteness and leading coefficient are **unproved**. H1 still lacks an *evaluated arithmetic first correction* and H2 lacks an *actual Greenberg-Selmer second Bockstein*; H3 lacks a characteristic-zero complex third-derivative comparison. The target of this session is **only** the source-normalized mod11 **GLOBAL** secondary obstruction class, NOT a Selmer h² entry or original complex L''.

Write G=G_(K,Σ), K=Q(sqrt(−7)), V=E[11], χ the actual first anticyclotomic character. For a positive class x∈H¹(G,V)^+ admitting a supported first global A₂-lift c₀+Tc₁, the second obstruction to A₃ is (Session36, Session49, same inverse generator)
  Θ(x;c₁) ∈ H²(G,V)^+.
Changing the first lift by t·Tκ(R), where the residual negative Kummer point R spans the entire negative global H¹ under **C0044/46/47 source hypotheses**, changes Θ by ±t·β₁(κ(R)), up to the explicitly fixed sign/unit convention. Thus the secondary obstruction is well defined in
  H²(G,V)^+ / span_F11{β₁(R)}.
A nonzero class in this quotient **blocks every supported GLOBAL second lift** for the chosen positive x. Vanishing there only removes this second GLOBAL obstruction; it is not a proof of ordinary local Greenberg compatibility or of the genuine derived h².

## Pre-existing actual arithmetic and source-conditional first-height data

The exact local finite Kummer matrix from **C0039** for the five independent MW classes P1,P2,P3,P4,R is
  L = [[4,0,8,3,9], [4,0,8,3,2]] mod11.
The three **actual positive residual fine Kummer classes** (locally zero at both v|11 and at the other Σ primes) are
  Y1=P2,
  Y2=P3−2P1,
  Y3=P4−9P1.
They are F11-linearly independent from the five-point saturation certificate. They span a known *subspace* F₀⊂H¹_fine(G,V)^+ of dimension 3; **no claim is made that they exhaust the whole fine group**.

The independently corroborated **C0040 conditional** first-height/duality calculation (source-normalized integral BCLMN/Nekovář comparison, finite duality assumptions **not independently expert reviewed**) gives the pairing of the **actual first global obstruction** β₁(R) with these three fine tests:
  a = (〈β₁(R),Y1〉,〈β₁(R),Y2〉,〈β₁(R),Y3〉)
    = (2,5,10) ∈ F11³,
**up to one common nonzero character/duality unit**. The common unit does NOT change its kernel. The values are not inferred from a decimal approximation of the complex L-function, nor from an assumption of Sha finiteness.

## New exact two-detector corollary

Define two explicit actual fine classes
  **Z1=3Y1+Y2 = −2P1+3P2+P3,**
  **Z2=6Y1+Y3 = −9P1+6P2+P4.**

They are linearly independent and *fine* (because the Yj are). The recorded first-height vector satisfies
  〈β₁(R),Z1〉 = 3·2+5=11=0,
  〈β₁(R),Z2〉 = 6·2+10=22=0 mod11.
They are a BASIS of **ker(a:F₀→F11)**, since a≠0 and dim F₀=3.

Given ANY source-normalized proposed second GLOBAL obstruction class β₂(x;c₁), let its three fine pairings be
  b=(b1,b2,b3),  bj=〈β₂(x;c₁),Yj〉 ∈F11.
Define the **normalization-independent detectors**
\[
  \boxed{D_1(x)=3b_1+b_2,\qquad D_2(x)=6b_1+b_3 \pmod{11}.}
\]
Changing c₁ to a different global first lift changes b by t·a and therefore changes neither D1 nor D2. This is an EXACT quotient invariant of the secondary GLOBAL obstruction, not a heuristic ratio.

**Sufficient criterion (conditional on source normalization and actual arithmetic evaluation):**
  If **D1≠0 OR D2≠0**, then Θ(x)≠0 in H²(G,V)^+/〈β₁(R)〉. Hence NO supported global A₃ lift of x exists, regardless of first-lift normalization; a fortiori no ordinary Selmer A₃ lift. This is a logically decisive negative test for a chosen positive class.

**Important one-sidedness:** If D1=D2=0, then the restriction of β₂(x;c₁) to the **known F₀ only** is a multiple of the first-height functional a, because the kernel of (D1,D2) in F11³ is exactly span(a). This does **NOT** prove the true global class lies in span(β₁(R)); its pairing with unknown fine H¹ classes, possibly arising from Sha, could still be nonzero. It also proves nothing about ordinary Greenberg local homotopies. D1=D2=0 is *not* an existence certificate.

Under the source-dependent C0040 nonzero β₁(R) and C0039 dim F₀=3, Poitou–Tate therefore gives a lower bound of dimension **at least two** on the secondary obstruction quotient H²(G,V)^+/〈β₁(R)〉, assuming the source-normalized duality comparison is valid. The two Zj are explicit independent tests for that quotient, not a claimed complete basis of it.

### Which actual inputs are still missing?

For each target x (e.g. x=P₂−2P₁, a first-radical *residual* recipe, not automatically a true integral first-height radical), we still need a **source-normalized arithmetic first correction** c₁ and the **pairings of the resulting b₂-cochain** with Y1,Y2,Y3, or directly with Z1,Z2. These are not currently computed. C0047 gives only nonconstructive fixed-support global existence of a first lift under its hypotheses; the C0045 ordinary Selmer existence conditions remain separate. The detector converts an open-ended secondary operation into two concrete scalar arithmetic questions **once** those cochains can be evaluated. It does not synthesize any missing cochain and does not prove a second height nonzero.

## Exact falsifiers and independent repro

Run
  python3 -I -B research/proof_labs/session50_two_coordinate_secondary_detectors.py

Checks:
1. both Zj are in the kernel of **both actual local reduction rows** and independent;
2. the C0040 first-obstruction vector (2,5,10) annihilates Z1 and Z2;
3. for **all 11³=1,331** possible proposed second pairing vectors b and all **11** first-lift choices t, D(b+t·a)=D(b);
4. D(b)=0 iff b belongs to span(a) **ON THE KNOWN THREE-TEST SUBSPACE ONLY**;
5. modifying the exact C0040 height input (2,5,10) to (2,5,9) breaks Z2 orthogonality, and a raw unnormalized b in span(a) can be nonzero while the quotient detectors vanish; this prevents mistaking a nonzero raw coefficient for a genuine second obstruction.

The test is finite F11 arithmetic and does not prove the source arithmetic height comparison, an unknown cochain value, completeness of the full fine group, genuine derived h² or complex BSD.

## Decision

Stay with H1 40%, H2 15%, H3 40%, H5 5%, H4/H6 parked. **Cheapest decisive arithmetic next test:** evaluate the two normalized pairings 〈β₂(x;c₁),Z1〉 and 〈β₂(x;c₁),Z2〉 for a **genuine** first globally supported c₁ (and independently ordinary-localize it). A single certified nonzero result would block the corresponding second **global** lift. Zero results would NOT establish that an A₃ lift exists. The task is to construct/evaluate the first arithmetic correction and its Selmer cone, not merely refine formal group calculations. **New proved BSD implication: NONE.**
