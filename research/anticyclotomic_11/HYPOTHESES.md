# C-0003 — A conditional, published anticyclotomic vanishing bound

**Status:** specialization of **existing theorems**, with a reproducible exact local arithmetic check. It does **not** establish a new general theorem, independently prove BSD, or prove a complex analytic rank. Mathematical expert review of the Galois-image and theorem-applicability arguments remains outstanding.

## Setup and source

Let E/Q be the curve with [LMFDB label 234446.a1](https://www.lmfdb.org/EllipticCurve/Q/234446/a/1), given by the **minimal** equation

```
y² + x y = x³ - x² - 79 x + 289.
```

Let K=Q(√−7), discriminant D_K=−7, and p=11. The conductor is N=234446=2·117223 (squarefree). LMFDB records rank E(Q)=4. The change Z=4x−1, W=4(2y+x) gives W²=Z³−1267Z+17230, used only for reduction computations at odd primes. The short model is **not minimal at 2**; all minimal discriminant and ramification statements below use the original model.

**Primary literature:** A. Agboola and F. Castella, *On anticyclotomic variants of the p-adic Birch and Swinnerton-Dyer conjecture*, J. Théor. Nombres Bordeaux **33** (2021), 629–658, DOI [10.5802/jtnb.1174](https://doi.org/10.5802/jtnb.1174), specifically **Hypotheses 6.1**, **Theorem 6.2**, **Corollary 6.4**, and **Conjecture 4.2**. Refer to the [author's manuscript](https://web.math.ucsb.edu/~castella/BSD-BDP.pdf) for full notations and exact claims.

## Local hypotheses audit (Hypotheses 6.1)

| Condition | Evidence |
|---|---|
| (1) p>2, p∤N, good ordinary | p=11; minimal Δ=468892=4·117223, so 11 is good. #E(F11)=18, hence a11=11+1−18=−6; a11 ≠0 mod11. |
| (2) E[11] ramified at each ℓ∣N | c4=3801 is an ℓ-adic unit at both ℓ=2 and 117223. Their minimal discriminant valuations are 2 and 1, so both reductions are multiplicative (Kodaira I2, I1). By the standard Tate-curve inertia description, inertia acts nontrivially on E[11] whenever 11∤ord_ℓ(Δ_min); holds at both primes. |
| (3) every ℓ∣N splits in K | 2 splits since D_K=−7≡1 mod8 (equivalently u²−u+2 splits into distinct linear factors modulo 2 for u=(1+√−7)/2). For 117223, x=43297 satisfies x²≡−7 mod117223. |
| (4) ρ_E,11 surjective | #E(F3)=7 and a3=−3. At 3, the Frobenius polynomial T²−a3 T+3=T²+3T+3 has discriminant −3≡8 mod11, a nonsquare; therefore the representation E[11] is irreducible over F11. The multiplicative I1 prime 117223 supplies a nontrivial transvection in the image. By the standard irreducible-subgroup-with-transvection lemma for GL2(F_p), p=11, the image contains SL2(F11). Its determinant is the mod-11 cyclotomic character, surjective, hence it equals GL2(F11). **This step uses published Tate-curve and finite-subgroup classification theorems; the Python script does not verify them.** |
| (5) p splits in K | √−7≡2 or 9 modulo 11; both roots are simple. |
| (6) a_p(E)≢1 mod p | a11=−6≡5 mod11, not 1; equivalently 11∤#E(F11)=18. |

**Further hypothesis (⋆) in Corollary 6.4:** N is squarefree (true), so its alternative condition is automatic.

No claim is made that a successful Python run proves the Galois-image lemma or literature theorem.

## Published theorem specialized to E/K

Write J for the augmentation ideal of the anticyclotomic Iwasawa algebra of K at 11 and `L_p(f)` for the **Bertolini–Darmon–Prasanna anticyclotomic p-adic L-function** in the conventions of Agboola–Castella. (Their `L_p(f)` is the *square* of a square-root p-adic L-function; it is not the complex Hasse–Weil L-function.)

**Conditional corollary:** If

1. **finiteness of the 11-primary Tate–Shafarevich subgroup** `Sha(E/K)[11^∞]` holds, and
2. the recorded rational rank `rank E(Q)=4` is accepted,

then Agboola–Castella, **Corollary 6.4**, applies and gives

```
ord_J L_p(f) >= 2(max(r_+, r_-)-1) >= 2(4-1) = 6.
```

Here `r_+` and `r_-` are the dimensions of the plus/minus eigenspaces under Gal(K/Q); `r_+=rank E(Q)=4`. **We do not need an independently certified rank-one calculation for the -7 twist to obtain the lower bound 6.** Even if r_- is greater than expected, the bound is at least six.

The inequality **does not certify equality** `ord_J L_p(f)=6`. Equality, nonvanishing of the derived regulator, and the predicted filtration `5 → 3 → 1` are **conjectural** under the corresponding additional nondegeneracy hypotheses. The complex analytic rank of E over Q or K is not determined by this p-adic conditional consequence.

## Unresolved barriers and our next falsifiable questions

- **Most important missing hypothesis:** `Sha(E/K)[11^∞]` finite. Rank-1 twist finiteness alone would not settle the rank-4 part or the K-primary statement. We have no proof of this missing hypothesis.
- The global anticyclotomic height character, Iwasawa filtration, universal norms, local height corrections, and a nonzero cross-height value have **not** been computed.
- Earlier interactive proofs of a complete rank-five K-basis have **not yet been independently audited**; they are not needed for this weaker conditional bound.
- An exact check of published source hypotheses by a qualified arithmetic geometer, including mod-11 image and normalization, should precede any claim of independent mathematical review.
- This deduction is **not a new BSD advance**. It records that existing published machinery fits a specific curve extremely well.

## Reproduce the exact arithmetic

Run:

```bash
python3 -I -B research/anticyclotomic_11/verify_local_hypotheses.py
```

No dependencies beyond the Python standard library; no randomness or floating point. The script checks exact minimal invariants, primality of 117223, local splitting, reduction counts, Frobenius irreducibility, and the local data needed for the cited standard lemmas. The *Tate-curve inertia theorem*, finite-subgroup classification, and Corollary 6.4 are external mathematical results, not algorithmically proved by this script.

**Provenance:** Human–AI exploration, 17 October 2026. Status: internal review only, external expert review outstanding.
