# Claim and validation ledger

This ledger covers claims **in this repository**. Historical conversation experiments from sessions 1–9 are **not imported as verified results**; those need fresh audits before inclusion.

| ID | Precise scope | Type | Review state | Evidence / dependencies | Missing validation |
|---|---|---|---|---|---|
| C-0001 | For E: y²=x³−1267x+17230 over K=Q(√−7), at the two split embeddings over 11, the normalized local elliptic-log columns of P₁=(15,40), H=((37+3√−7)/2,−16+12√−7) have determinant 85 mod 121, hence a unit mod 11. | Computational certificate, conditional on the documented formal-group interpretation | Two distinct AI-authored implementations reproduce the decisive minor; **not expert-reviewed** | [note](research/split11/NOTE.md), [main check](research/split11/verify.py), [projective check](research/split11/independent_check.py) | Independent human audit of formal-group normalization and local reduction assumptions; check against Sage/PARI |
| Q-0001 | Can the anticyclotomic derived 11-adic heights on this curve be computed and their hypotheses verified? | Open research question | No computation or theorem claimed | [research standards](RESEARCH_STANDARDS.md) | Literature audit, local/global Selmer assumptions, a precise algorithm and an independent check |

| C-0002 | For the coefficient module on P1–P4,H, the two normalized split-11 local logarithms modulo 11^4 have a rank-three kernel with explicit generators P2−8690P1, P3−14082P1, P4−12835P1 (mod 14641). | Exact finite-precision computational certificate conditional on formal-log normalization | Two AI-authored algorithms agree on P1,P2,P3,R,H; all six columns corroborated by independent PARI/GP ellpadiclog; no external mathematical peer review | [note](research/split11/KERNEL.md), [verifier](research/split11/kernel_mod11_4.py), [PARI corroboration](research/split11/PARI_VALIDATION.md), [LMFDB](https://www.lmfdb.org/EllipticCurve/Q/234446/a/1) | Independent Sage/PARI reproduction, external review of local group-law details; no identification with derived-height radical |

**NOT CLAIMED:** proof of BSD; complex analytic rank four for the rank-four curve; a nonzero derived p-adic height; identification of the local-log kernel with a derived-height radical; novelty of C-0001; expert/peer review.

When adding a claim, give it a new immutable ID, preserve its scope, and file a linked correction entry for any change in status or value.
