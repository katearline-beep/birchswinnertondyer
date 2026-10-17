# C-0002: independent PARI/GP validation (2026-10-17)

**Status:** a third-party arithmetic library (`ellpadiclog` in PARI/GP 2.15.4) reproduces all six columns at both split 11-adic embeddings, modulo 11^4, including P4. This is **independent computational corroboration**, not a Lean formalization or mathematical peer review.

## Reproduction

[Source](pari_split11.gp), run in GitHub Actions on `ubuntu-24.04`, with Ubuntu's `pari-gp 2.15.4`:

```bash
gp -q -f research/split11/pari_split11.gp
```

Expect output:

```
PASS PARI/GP C-0002: all twelve normalized split-11 logarithms mod 14641
PASS PARI/GP C-0002: determinant 1537 mod 14641, 8 mod 11
```

The script initializes `y²=x³−1267x+17230`, embeds `sqrt(-7)` into the two roots in `Q_11`, multiplies each input point by 18 to land in the kernel of reduction, calls PARI's **`ellpadiclog(E,11,7,Q)`** on that point, and divides by `18·11` to normalize. It checks the complete 2×6 output matrix from C-0002, not just a determinant copied from the previous scripts. The GitHub workflow fails if output contains a GP interpreter error or omits expected success lines.

**Important correction:** The first version of the workflow gave a *false green* because GP emitted parse errors, then printed success messages. We inspected the raw logs, repaired the GP parsing, and strengthened the workflow to reject interpreter errors. The initial green run is **invalid evidence**. This note records that failure to preserve provenance. Use only the final post-fix successful CI run when reviewing C-0002.

## What follows and what does not

This independently supports the finite-precision **local logarithm computation** and closes the prior one-implementation-only gap for P4. The full arithmetic theorem and the formal-group hypotheses still need mathematical review. In particular, no anticyclotomic height pairing, derived height, Selmer-theoretic regulator, complex analytic rank, or BSD result has been calculated or proved. See [RESEARCH_STANDARDS.md](../../RESEARCH_STANDARDS.md) and [C-0002](../../CLAIMS.md).

Reference for library semantics: [PARI/GP documentation for ellpadiclog](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html).
