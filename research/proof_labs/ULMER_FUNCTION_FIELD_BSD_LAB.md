# Proof laboratory B: Ulmer's proved function-field BSD mechanism

**2026-10-19. The BSD/rank results below are ALREADY PUBLISHED THEOREMS by Douglas Ulmer, not new project results.** The first local-fibre script checks local arithmetic; the new Session 20 program also reconstructs the published *global Fermat quotient cohomology factor* using Ulmer's Jacobi-sum theorem. Neither program proves Tate or BSD.

Primary source: D. Ulmer, [*Elliptic curves with large rank over function fields*](https://annals.math.princeton.edu/2002/155-1/p09), Annals of Mathematics **155** (2002), 295–315, [arXiv:math/0109163](https://arxiv.org/abs/math/0109163), especially Theorem 1.5, Remarks 1.6, and proof outline §1.7.

## Three mathematically proved high-rank cases

For any prime \(p\), integer \(n\ge1\) and \(d=p^n+1\), Ulmer studies the nonisotrivial curve
\[
E_d/\mathbb F_p(t):\quad y^2+xy=x^3-t^d.
\]
Ulmer proves BSD for this family. **Important correction to Session 19:** the simple formula \(p^n\) (or \(p^n-2\) if \(6\mid d\)) is the **geometric rank**, attained over \(\mathbb F_{p^{2n}}(t)\); it is **not generally the rank over \(\mathbb F_p(t)\)**. Exact ranks over \(\mathbb F_q(t)\) require **Theorem 9.2** with Frobenius orbit lengths and special-fibre corrections.

| Case | d | Published rank over \(\mathbb F_p(t)\) | Published geometric rank (attained over \(\mathbb F_{p^{2n}}(t)\)) | Good \(\mathbb F_p\)-rational finite fibres | Sum local traces |
|---|---:|---:|---:|---:|---:|
| p=5,n=1 | 6 | **2** | 3 | 4 | −6 |
| p=7,n=1 | 8 | **3** | 7 | 6 | +6 |
| p=5,n=2 | 26 | **7** | 25 | 4 | −6 |

The \(p=5,n=2\) and \(p=5,n=1\) examples have identical \(\mathbb F_5\)-rational finite-fibre traces, but different global ranks (**7 versus 2** over \(\mathbb F_5(t)\), or **25 versus 3** geometrically). This is the intended negative control: finite local counts cannot establish global rank. The [Session 20 erratum and global orbit audit](SESSION20_FERMAT_ORBITS_AUDIT.md) derives the correct prime-field and extended-field values directly from Ulmer's published Theorem 9.2.


## Why BSD is provable here: the typed mechanism

The original proof uses a chain of genuinely mathematical *global* objects:

1. Construct the elliptic surface \(\mathscr E_d\to\mathbb P^1_{\mathbb F_p}\) with generic fibre \(E_d\).
2. Construct a dominant rational map from the Fermat surface \(F_d\) to \(\mathscr E_d\), and identify a suitable quotient \(F_d/\Gamma\) birationally with \(\mathscr E_d\). Surface cohomology and the Néron–Severi group encode algebraic cycles and sections.
3. Use the known **Tate conjecture** for the corresponding Fermat surfaces, and its transfer to \(\mathscr E_d\), to obtain the arithmetic cycle/pole equality. Under the established surface-BSD equivalence in this setting, BSD follows for the generic elliptic curve.
4. Compute the surface's zeta function from the Fermat-surface zeta data (Weil/Gauss sums), and count suitable Frobenius eigenvalues, yielding the order of vanishing/pole and ultimately the formula for Mordell–Weil rank.

The key mechanism is **not an 11-adic height**. It is an exact algebraic-cycle ↔ Frobenius-eigenspace bridge, validated by an established Tate theorem for a highly structured family of surfaces. This offers a different kind of laboratory from our rank-four \(\mathbb Q\)-curve.

## What can and cannot transfer to characteristic zero

**Valid transferable questions:** Can a geometric correspondence give an explicit cohomological realization of special \(L\)-values? Are there algebraic cycles whose independence detects analytic vanishing in an independently proved comparison theorem? Can a rank-two or other characteristic-zero control invalidate a proposed cycle-counting argument?

**Non-transferable without a new theorem:** The surface over \(\mathbb F_p\), its geometric Frobenius, finite-field zeta-function poles and the positive-characteristic Tate equivalence do **not** directly compute the central Taylor coefficient of the complex \(L(E/\mathbb Q,s)\). One cannot simply replace \(\mathbb F_p(t)\) by \(\mathbb Q(t)\) and claim ranks persist: Ulmer explicitly notes in Remark 1.6(4) that the *same displayed Weierstrass family over* \(\mathbb Q(t)\) has rank **bounded independently of \(d\)**. This is a critical **negative transfer control**. The mechanism is instructive precisely because its simplest characteristic-zero transplantation fails.

Do not overstate a similarity between étale cohomology/Frobenius in positive characteristic and complex Hasse–Weil Taylor coefficients: a genuine comparison theorem is required.

## Computational exhibit and its limits

Run [ulmer_function_field_fibres.py](ulmer_function_field_fibres.py):

- For each \(p,d\), verify \(432\not\equiv0\bmod p\) and use the explicit discriminant \(\Delta(t)=t^d(1-432t^d)\) and \(j=1/\Delta\), a nonconstant rational function.
- Exclude **singular fibres** before applying Hasse's bound to a smooth elliptic fibre.
- Compute \(\#E_t(\mathbb F_p)\) using **two independent methods**: enumerate solutions of \(y^2+xy=x^3-t^d\), and sum the quadratic character of the \(y\)-discriminant \(x^2+4(x^3-t^d)\).
- Verify Hasse's bound for each good fibre.
- Demonstrate that different \(d=p^n+1\) can produce **identical counts on all \(\mathbb F_p\)-rational t** while the theorem gives different global ranks.

**No rank or BSD proof follows from these finite enumerations.** Rank and BSD are explicitly imported from Ulmer's theorem. Session 20 [reconstructs the exact Fermat-quotient map](ulmer_fermat_quotient.py) and [published Jacobi-sum-based global quotient zeta factors](ulmer_frobenius_orbits.py) for the small \(p=5,n=1,d=6\) example, with exact symbolic identity and Frobenius-orbit checks. The next open milestone is an **independent Jacobi-sum computation or deeper Tate/BSD mechanism audit**, not another local-fibre table.

## Novelty and decision

The family and proof are 2002 published mathematics. Our new contribution is a reproducible *comparative proof laboratory* with explicit negative-transfer gates, not a new theorem. Retain the exact 2002 reference and do not present the finite fibre computations as a proof of Ulmer's theorem.

**Stop rule:** If a proposed transfer to curves over \(\mathbb Q\) lacks a defined cohomological realization, source/target and complex comparison theorem, mark it speculative and stop. Do not equate function-field ranks, local Frobenius eigenvalues or algebraic cycles with a proved vanishing of the original complex \(L''(E,1)\) for 234446.a1.
