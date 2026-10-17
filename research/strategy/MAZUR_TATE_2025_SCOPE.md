# H4 leapfrog kill test: the 2025 Burns–Kurihara–Sano Mazur–Tate theorem

**Source-level applicability audit** (2026-10-17). **This is a negative result for one proposed *proof strategy*, not a negative theorem about elliptic curves or the Mazur–Tate conjecture.** It does not make the 2025 paper less important.

## Source and version

David Burns, Masato Kurihara and Takamichi Sano, *On Derivatives of Kato's Euler System and the Mazur–Tate Conjecture*, **International Mathematics Research Notices** (2025), no. 4, rnaf012, DOI [10.1093/imrn/rnaf012](https://doi.org/10.1093/imrn/rnaf012). The **publicly accessible arXiv:2103.11535v1**, §§1.1–1.2 [PDF](https://arxiv.org/pdf/2103.11535), contains the statements numbered **Theorem 1.1** and **Corollary 1.2** quoted for this audit. The final published version may contain changes; verify final numbering/wording before a formal citation in a manuscript.

The abstract describes unconditional theoretical evidence for the Mazur–Tate conjecture in strictly positive rank. **The headline does not mean the paper proves full Mazur–Tate or BSD in all positive ranks.**

## The exact circularity

In the arXiv version, **Theorem 1.1** assumes technical conditions (a)–(c) on an elliptic curve E and real abelian F/Q, **and** requires

- (d) **BSD for E/Q**, and
- (e) the Generalized Perrin–Riou Conjecture for E in the relevant cyclotomic \(\mathbb Z_p\)-extensions.

Only **then** does it deduce the Mazur–Tate conjecture for F/Q.

It is logically invalid to use that implication to **prove BSD**, particularly for our rank-four E: the desired result is part of the premise. A toy proof checker that drops assumption (d) would assert a circular theorem; [our negative control](mazur_tate_scope_test.py) explicitly rejects this.

## What the unconditional part really concerns

**Corollary 1.2** in arXiv v1 assumes \(\operatorname{ord}_{s=1}L(E,s)=1\), squarefree E-conductor, and supersingular reduction at each prime divisor of \([F:\mathbb Q]\), in addition to technical field/image hypotheses. It proves the order statement and leading term **up to an automorphism of the finite Galois group**, and notes a potential consequence for BSD failure in its range.

Our E=234446.a1 has documented algebraic rank **four**, not one; moreover, for prime \(p=11\), \(\#E(\mathbb F_{11})=18\), \(a_{11}=-6\not\equiv0\pmod{11}\), so 11 is **ordinary**, not supersingular. We therefore cannot apply the specific unconditional corollary to our E and chosen C11 fields. This is an applicability statement, **not** evidence against BSD.

## Field-choice gate

For the two real cyclic degree-11 fields investigated:

| Field | Conductor of F/Q | Squarefree? | Theorem 1.1 condition (a) |
|---|---:|---|---|
| F23=Q(ζ23)^+ | 23 | Yes | Could satisfy (a), other hypotheses must be checked |
| Q1, first layer of cyclotomic Z11 tower | 121 | **No** | **Fails (a)** as stated |

The theorem's general method may admit extensions to nonsquarefree ramified conductor (the preprint comments on this possibility), but that is **not** permission to invoke the theorem as published. Conditions (b)–(c) are **not certified** by our simple checker even for F23.

## Implications for the leapfrog portfolio

- **Reject this shortcut:** “Use the unconditional positive-rank Mazur–Tate theorem to prove BSD at rank four.”
- **Retain as prior art:** Modular-symbol integral congruences, determinantal zeta elements and Selmer-complex Bockstein calculations may inform H4 and H1, but need an independent theorem pointing *toward* the **complex derivative** rather than presupposing BSD.
- **Stop condition:** If the only available implication begins with BSD as a hypothesis, do not pursue it as a BSD proof route. Record the limitation and reallocate effort to derived-height or geometric third-derivative bridges.
- **Next possible falsifier:** isolate a claim about an explicit algebraic modular element over F23, test the actual finite integral congruence and necessary normalization, and demand a non-circular comparison to complex L'' before investing in a large implementation.

Reproduce the limited exact hypothesis checks using `python3 -I -B research/strategy/mazur_tate_scope_test.py`. **Passing the script does not prove the assumptions or conclusion of any cited theorem.**

**Sources:** [2025 published metadata](https://doi.org/10.1093/imrn/rnaf012); [accessible 2021 arXiv proof manuscript, first three pages](https://arxiv.org/pdf/2103.11535). Status: internally audited, not externally peer-reviewed.
