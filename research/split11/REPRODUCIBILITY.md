# Reproduce C-0001: split-11 local logarithm calculation

## Scope

This verifies an exact finite congruence for *normalized local elliptic logarithms*, conditional on the standard formal-group interpretation of the parameter `t=-x/y` for the invariant differential `dx/(2y)`.

No external data downloads, randomness, or non-standard Python packages are required.

## Commands

From the repository root (Python 3.11–3.13):

```bash
python3 -I -B research/split11/verify.py
python3 -I -B research/split11/independent_check.py
```

Both should exit 0, print a passing message and agree that the determinant is **85 modulo 121**, hence **8 modulo 11**. The expected embeddings of √−7 modulo 11³=1331 are 1058 and 273.

The primary script performs exact fraction arithmetic in Q(√−7) and elliptic addition before reducing modulo 11³. The independent script performs projective Jacobian arithmetic *directly* in Z/(11³), without constructing high-height rational multiples. It checks five of the six points; P₄ is omitted from this second script because its naïve projective coordinates become nonprimitive. Both compute the decisive P₁/H minor. This limitation must not be hidden.

The script result is a reproducible computational check, not a formal proof of its own implementation. In particular, interpreting the residues as normalized local elliptic logarithms depends on the formal-group expansion and on 18 being prime to 11 and annihilating the reduction group.

## Reviewer checklist

1. Independently verify E has good reduction at 11 and #E(F₁₁)=18.
2. Check that the embeddings are indeed both roots of X²+7 mod 1331.
3. Verify P₁ and H lie on E and are 11-adically integral.
4. Check log_E(t) = t + O(t⁵) here, including denominators and normalization by 18 × 11.
5. Audit exceptional addition/doubling cases and projective ring operations; compare against Sage or PARI.
6. Check the determinant and clarify the exact domain/codomain of the induced map.

**Review status:** independently implemented with two AI-authored algorithms; independent human mathematical review outstanding. See [C-0001](../../CLAIMS.md).
