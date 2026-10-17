# Split 11-adic local logarithms: reproducible calculation

**Status:** finite exact arithmetic, based on standard elliptic formal-group formulas. Not a proof of a new case of BSD, a derived-height calculation, or a claim of mathematical novelty. This is a research example awaiting independent expert review.

Let E be y² = x³ - 1267x + 17230 over K = Q(sqrt(-7)). Eleven splits, with the two roots of -7 modulo 1331 given by 1058 and 273. Reduction yields #E(F₁₁) = 18, so [18]P is in the formal group for each integral local point considered here.

Using t = -x/y and the invariant differential dx/(2y), the formal logarithm is t + O(t⁵). Since t([18]P) belongs to 11 Z₁₁, the normalized log modulo 121 can be evaluated from t([18]P)/(18 × 11) modulo 121.

For P1=(15,40) and H=((37+3√-7)/2,-16+12√-7), the calculated two local columns are (81,81) and (43,56), respectively, modulo 121.

Thus the determinant is 81×56 - 81×43 = 1053 ≡ 85 (mod 121), which is 8 (mod 11) and a unit. Conditional on the stated standard formal-group identification, these two normalized local-log images generate Z₁₁². This is not an identification with the kernel of a global derived-height pairing.

Run `python3 research/split11/verify.py` (Python standard library only) to verify the point identities, reduction count, logarithm congruences, and determinant. The script checks its complete set of expected residues; the key claim is the unit minor.

**References:** Silverman, *The Arithmetic of Elliptic Curves*, Ch. IV; SageMath elliptic formal-group reference https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/formal_group.html ; Agboola–Castella, *On anticyclotomic variants of the p-adic Birch and Swinnerton-Dyer conjecture*, https://web.math.ucsb.edu/~castella/BSD-BDP.pdf .

**Provenance:** Interactive human–AI mathematical exploration, October 2026. Please report errors, missing assumptions, or prior appearances of this computation.
