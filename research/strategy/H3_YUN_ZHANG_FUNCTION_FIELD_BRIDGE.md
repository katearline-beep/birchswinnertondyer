# H3 Yun–Zhang (2019) source audit

**2026-10-18; AI-assisted internal literature audit. Not a theorem about E/Q.**

Yun and Zhang, *Shtukas and the Taylor expansion of L-functions (II)*, Annals of Mathematics 189 (2019), 393–526, Theorems 1.2 and 1.3 (pp. 397–398), DOI: https://doi.org/10.4007/annals.2019.189.2.2. Published PDF: https://annals.math.princeton.edu/wp-content/uploads/annals-v189-n2-p02-s.pdf.

**Actual output:** for PGL2 automorphic representations over a **function field** F=k(X), squarefree Steinberg level, and a quadratic cover unramified at level, Theorem 1.3 equates a nonzero scalar times the product of normalized central derivatives of orders (r1,r-r1) with a projected Heegner–Drinfeld-cycle self-intersection. For r=3,r1=2 this is precisely a **second derivative times a first derivative**. This is a genuine higher-derivative theorem, unlike first-derivative results for higher-weight forms.

**Scope limitation:** It does not apply to elliptic curves over Q. Theorem 1.2 requires r congruent to the number of inert Steinberg level places modulo 2; its Sigma-infinity denotes those inert *function-field* places, not Q's archimedean place. Both bad primes 2 and 117223 of E=234446.a1 split in Q(sqrt(-7)), while the number-field imaginary archimedean sign contributes to the odd base-change root number. The 2017 precursor handles even r; the 2019 paper admits odd r. Number-field higher-leg shtuka geometry is not constructed by either theorem.

**Critical missing arrows:** (A) a number-field analogue constructing a three-leg cycle, character projector, pairing and explicit reciprocity for the original completed complex L-functions; (B) a separate arithmetic theorem forcing the relevant projected pairing to vanish from four independent rational points, without assuming BSD or analytic rank four. The 2019 paper's Conjecture 1.6 about exterior powers and Frobenius eigenspaces is **conjectural** and function-field-specific. Even an analogue of the pairing identity alone would not imply vanishing.

**Next test:** identify a number-field arithmetic construction of the precise three-leg object and a noncircular rank-to-vanishing map, or park H3 computations. Exact algebraic and adversarial tests are in h3_mixed_projector.py. No proof of L''(E,1)=0, analytic rank four, Sha finiteness or BSD is claimed.
