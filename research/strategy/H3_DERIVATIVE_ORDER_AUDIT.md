# H3 literature stress test: "higher" geometry is not a third derivative

**2026-10-17 · Internal source-applicability review · No new theorem.**
Research target: for rank-four E=234446.a1 and an odd-sign quadratic twist E^D with nonzero first derivative, is there an **independently established geometric vanishing theorem** for the third derivative of the complex weight-two base-change L-function \(L(E/K_D,s)\)?

## Typed formula and true missing arrow

We know \(L(E/K_D,s)=L(E,s)L(E^D,s)\) for the quadratic base change. Suppose \(L(E,1)=L'(E,1)=L(E^D,1)=0\). The product rule gives
\[
L'''(E/K_D,1)=3L''(E,1)L'(E^D,1).
\]
The known positive candidate for \(L'(E^{-7},1)\) is still awaiting a full expert audit; we cannot silently use it as proved.

**If** one independently proves \(L'''(E/K_D,1)=0\) and \(L'(E^D,1)\ne0\), **then** \(L''(E,1)=0\). This is a *correct conditional algebraic implication*, but its valuable premise is entirely **missing**. Simply deriving the product rule doesn't establish the premise.

## Targeted literature: actual derivative orders

| Work | What its central statement computes | Why it does **not** yet provide H3 |
|---|---|---|
| Gross–Zagier (1986), weight-two Heegner height formula | A **FIRST** derivative of Rankin/base-change L-functions | Our missing object is the **THIRD** derivative after lower-order zeros. |
| D. T.-B. G. Lilienfeldt & A. Shnidman, [*Derivatives of Rankin–Selberg L-functions and heights of generalized Heegner cycles*](https://arxiv.org/abs/2408.04375), theorem 1.1 | A **FIRST** derivative \(L'(f,\chi,k+t)\) of a higher-weight Rankin–Selberg L-function, equal to a generalized Heegner-cycle Beilinson–Bloch height | "Higher" refers to modular **weight** \(2k\) and cycle codimension, not third derivative. In their stated main range \(0<t\le k-1\), taking weight 2 (\(k=1\)) leaves **no admissible t**. |
| T. Du & Z. Peng, [*On the central derivatives of L-functions and modularity of Heegner cycles*](https://arxiv.org/abs/2603.15795) (2026 preprint) | Central **FIRST** derivative represented by an arithmetic intersection formula, generalized in **weight** and modularity of Heegner-cycle generating series | It does not directly state a geometric vanishing theorem for the **THIRD** derivative of our weight-two quadratic base change. |

These statements were compared from the publicly available paper descriptions and Lilienfeldt–Shnidman's explicit introduction/theorem. This was a **targeted** search, not an exhaustive classification of all higher Gross–Zagier literature; do **not** claim no relevant theorem exists anywhere.

## A new, useful negative-control implication

Under our hypotheses the base-change product already has order at least three (order \(\ge2\) for E, odd twist order \(\ge1\)). Hence
\[
L'(E/K_D,1)=0
\]
**regardless of whether \(L''(E,1)\) vanishes.** Assuming the ordinary classical Gross–Zagier formula applies for a Heegner field, the associated first-derivative Heegner height vanishes; a vanishing first height is therefore **not** a discriminator between analytic ranks two and four in this setting.

For an exact countermodel, let \(f(t)=t^2\) and \(g(t)=t\). Then
\[
(fg)'(0)=0,\qquad (fg)'''(0)=6\ne0.
\]
This is a direct falsifier for the shortcut: **“Heegner first-height zero implies third derivative zero.”** The geometry would need a genuinely *higher-order* arithmetic pairing or new cycle invariant that is not the standard Gross–Zagier first derivative in disguise.

See [kill_tests.py](kill_tests.py) for the rank-two/rank-four product Taylor countermodel. This is not itself evidence that a new higher pairing exists.

## Decision and kill criterion

**H3 stays a high-upside mathematical bet, but its *computation budget* is restricted until a precise candidate theorem or cycle construction is named.** The next experiment is a primary-source search for a **third**-derivative formula or a proposed higher regulator specific enough to define a map, prove its properties, and test it against rank-two controls.

Reject/pause any candidate that:
- describes a FIRST derivative in higher weight as if it were a third derivative;
- derives only \(L'(E/K_D,1)=0\), which already follows for either rank-two or rank-four E;
- uses the unproved rank equality \(\operatorname{ord}_{s=1}L(E,s)=4\) as a hypothesis;
- replaces a complex L-derivative with an unrelated anticyclotomic p-adic L-function;
- invokes a toy matching rank or numerical near-zero without an exact comparison theorem.

This audit advances **research selection accuracy**, not BSD. No novel theorem, L'' zero, or external expert review is claimed.
