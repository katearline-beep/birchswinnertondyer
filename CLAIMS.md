# Claim and validation ledger

This ledger covers claims **in this repository**. Historical conversation experiments from sessions 1–9 are **not imported as verified results**; those need fresh audits before inclusion.

| ID | Precise scope | Type | Review state | Evidence / dependencies | Missing validation |
|---|---|---|---|---|---|
| C-0001 | For E: y²=x³−1267x+17230 over K=Q(√−7), at the two split embeddings over 11, the normalized local elliptic-log columns of P₁=(15,40), H=((37+3√−7)/2,−16+12√−7) have determinant 85 mod 121, hence a unit mod 11. | Computational certificate, conditional on the documented formal-group interpretation | Two distinct AI-authored implementations reproduce the decisive minor; **not expert-reviewed** | [note](research/split11/NOTE.md), [main check](research/split11/verify.py), [projective check](research/split11/independent_check.py) | Independent human audit of formal-group normalization and local reduction assumptions; check against Sage/PARI |
| Q-0001 | Can the anticyclotomic derived 11-adic heights on this curve be computed and their hypotheses verified? | Open research question | No computation or theorem claimed | [research standards](RESEARCH_STANDARDS.md) | Literature audit, local/global Selmer assumptions, a precise algorithm and an independent check |

**NOT CLAIMED:** proof of BSD; complex analytic rank four for the rank-four curve; a nonzero derived p-adic height; identification of the local-log kernel with a derived-height radical; novelty of C-0001; expert/peer review.

When adding a claim, give it a new immutable ID, preserve its scope, and file a linked correction entry for any change in status or value.
