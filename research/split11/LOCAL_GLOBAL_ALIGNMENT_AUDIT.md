# Session 12 — Primitive 11-adic height-alignment falsification gate

**2026-10-19 · AI-assisted internal mathematical audit · no external peer review.**  
**Scope:** an elementary, checkable consequence of C-0002, **not** a global anticyclotomic height computation or a new BSD theorem.

## Re-anchor to the actual BSD bottleneck

For the rank-four curve 234446.a1, the key missing analytic implication remains **L''(E,1)=0 for the original complex Hasse–Weil L-function**. The established split-11 local-log computation is subsidiary: its completed Mordell–Weil kernel does not automatically equal a global p-adic height radical, and neither supplies a complex comparison theorem. See the [whole-problem review](../reviews/2026-10-19-whole-problem.md) and [LCP-1](../strategy/LEAPFROG_PROTOCOL.md).

## A necessary projective condition if L11 held

On the rational directions P1,...,P4, the local-log functional has finite residues

```
u = (7462, 14432, 1427, 7989) mod 11^4
```

and u1 is an 11-adic unit. Thus its projective mod-11 coordinates are exactly

```
[u1:u2:u3:u4] = [1:0:2:9] in P^3(F_11).
```

Let a=(a1,a2,a3,a4), where ai denotes a **genuine, as yet uncomputed** global anticyclotomic cross-height h_ac(Pi,R), evaluated with one fixed, documented height normalization and character. Assuming a is nonzero, equality of the two hyperplane kernels over Q_11 is equivalent to the three wedge equations

```
u1*a2-u2*a1 = 0
u1*a3-u3*a1 = 0
u1*a4-u4*a1 = 0.
```

Consequently, *if* the L11 kernel-alignment hypothesis is true, then after dividing the vector a by its common 11-adic valuation, a1 must be a unit, and

```
[a1:a2:a3:a4] = [1:0:2:9] (mod 11).
```

In particular, a2/a1 must be divisible by 11, while a3/a1 ≡ 2 and a4/a1 ≡ 9 (mod 11). A different primitive projective residue **kills L11**. This is a necessary condition, not sufficient evidence: finitely many agreeing digits cannot show exact equality of Q_11-hyperplanes.

## The precision/scale trap

Anticyclotomic height vectors need not arrive as integral 11-adic units; a global character scaling or a common 11-power can obscure their first informative digit. For observations only known modulo 11^n:

1. Determine the minimum common valuation k among the *nonzero observed* coordinates.
2. Divide by 11^k and keep only n-k reliable digits.
3. If every coordinate vanishes mod 11^n, return **indeterminate**, never aligned.
4. Compare the resulting *primitive* vector with u by its projective ratios or the wedge equations.
5. Record the chosen logarithm/idele-class character, p-adic splitting, local heights, and precise error bounds. An unnormalized comparison is not decisive.

A symmetry-compatible toy height with cross vector (0,1,0,0) has a different first radical although it shares the expected rank-two block shape. Multiplying this bad vector by 11^3 makes **every raw wedge vanish modulo 11^3**, a false positive; primitive normalization recovers the obstruction 4 mod 11 immediately.

The executable [scale gate](../methodology/height_alignment_scale_gate.py) checks these countermodels, the positive alignment control, and the all-zero/indeterminate control. Its vectors are *formal test vectors*, **not computed heights**.

## Reproduction and independent arithmetic

```bash
python3 -I -B research/methodology/height_alignment_scale_gate.py
python3 -I -B research/split11/independent_jacobian_all_columns.py
python3 -I -B research/split11/kernel_mod11_4.py
```

The new independent Jacobian implementation checks P1,P2,P3,**P4**,R,H with no affine inversions during [18] multiplication, strengthening C-0002's independence coverage. The repository already contains a separate PARI/GP `ellpadiclog` check of all columns; this adds a further independently coded route, not a novel mathematical theorem. The implementation uses guard precision and should still receive an external mathematical/software audit.

**Next decisive task:** obtain even one genuinely global anticyclotomic cross-height vector at p=11, document its normalization/precision, and apply the primitive projective test. Do not increase local precision in place of global height computation. If L11 fails, construct the *actual* radical and investigate the alternating second derived height; neither path proves complex BSD.

**Provenance:** based on earlier AI-assisted sessions and the GitHub C-0002 exact computation; no human mathematical peer review or claim of novel mathematics.
