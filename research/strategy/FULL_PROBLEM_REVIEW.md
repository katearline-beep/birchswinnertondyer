# Whole-problem review protocol — WPR-1

**Mandatory recurring research habit.** A paper, script, or PR can be perfectly valid and still be irrelevant to our ultimate goal. This protocol prevents local technical success from being mistaken for progress toward BSD.

## Three separate levels of success

**Level A — the chosen curve:** for E=234446.a1 over Q, whose algebraic rank is four, prove analytically that `ord_(s=1) L(E,s)=4`. The exact missing *order-at-least-four* equation is `L''(E,1)=0`; after that, prove `L^(4)(E,1) != 0`. Be precise: parity is a symmetry of the **completed** L-function. The raw L is not generally even, but if L=L'=L''=0 the completed parity forces L'''=0.

**Level B — the full BSD formula for this curve:** prove finiteness of Sha(E/Q), the height/regulator and Tamagawa/period/torsion quantities in compatible normalizations, and
```
L^(4)(E,1)/4! = Omega(E) * Reg(E) * |Sha(E/Q)| * product(c_l) / |E(Q)_tors|^2.
```
An *approximate* quotient close to 1 is not proof of Sha finiteness, its order, or exact equality.

**Level C — the Clay problem:** establish the BSD rank equality and leading-term formula **generally**, not only for the single curve. A certified rank-four example could be valuable, but it is not the Millennium Prize solution. All manuscripts and project summaries must state which level they address.

Our focal curve is the **minimum-conductor rank-four curve** `234446.a1` (LMFDB); its displayed numerical analytic rank is four, but the [LMFDB reliability statement](https://www.lmfdb.org/L/2/94192/1.1/c1/0/20/Reliability) says rigorous analytic rank is known to be *either two or four*. LMFDB also lists an **analytic** order of Sha approximately 1; it is not a proof of the actual Tate–Shafarevich group's order. The [Clay problem](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/) remains unsolved.

## Review cadence and triggers

- **At the beginning of each scheduled autonomous research sprint** or when resuming from a substantial break: read the latest snapshot and ask what changed across Levels A–C.
- **After every three merged research pull requests, or at least weekly during active research**, publish another *dated* whole-problem snapshot in [reviews.json](../harness/reviews.json). Review immediately after any supposed major theorem, source correction, a failed conjecture, a new model/field, or a shift in priority.
- **Before expensive computation or upstream outreach:** explicitly compare likely impact against the full BSD dependency map. Escalate early if a route has no rigorous bridge to Level A or B.
- **After each reviewed milestone:** mark what has actually been proved that was not known before, versus reproduced prior art or improved infrastructure. Do not count scripts, green badges, digits or speculative conjectures as mathematical proofs.

This is a human/research-agent **operating cadence**. GitHub Actions validates the *presence, structure, and consistency* of review snapshots; it does not know how many intellectual decisions occurred, and cannot prove that a review is honest or that BSD has been solved. Research agents must comply even where the software cannot enforce frequency.

## The whole-problem checkpoint

For each review, answer **all** of the following in prose and a structured snapshot.

1. **North Star:** What exact statement is unsolved now? State it in terms of the complex L-function, not a different p-adic height or twist L-function.
2. **Strong BSD:** Have we independently established a finite Sha and exact leading term? If not, say no.
3. **Generality:** Is there a proof for *all* elliptic curves, a demonstrably new theorem for a family, a one-curve computational certificate, or none?
4. **Existing prior art:** What was already documented by LMFDB, Sage/PARI, or published theorems? Cite it; duplicate computations are validation, not novelty.
5. **Dependency graph:** For each active track, trace `verified input → theorem with checked hypotheses → resulting statement → missing bridge → BSD level`. Do not count parallel unverified arrows as a single proved path.
6. **Failure review:** Which attractive shortcut was killed, which hypotheses remain unverified, and which negative control exposed it?
7. **Effort allocation:** Compare the cheapest decisive experiment on three routes (incremental, credible leapfrog, wild). Park a track when it has no feasible next theorem or falsifier.
8. **Evidence hygiene:** Disentangle rigorous proofs of old theorems, independently checked numerical evidence, conditional consequences, and conjecture sketches. Log correction decisions.
9. **Choice:** Identify the next 1–2 actions most likely to eliminate a mathematical proof obligation, *not* the ones likely to generate the most code.

## Review scorekeeping without gamification

Use `research/harness/reviews.json` (append-only snapshots). Each snapshot has:
- the three BSD levels and individual status flags;
- a concise summary of **newly established theorems**, if any, versus replicated calculations and research operations;
- verified primary reference links;
- the deepest still-unproven mathematical arrow;
- priorities for H1–H6 and the next falsifiable action;
- date, exact base commit and owner `internal_research_agent`; external mathematical review is false until independently corroborated.

A mandatory [validator](../harness/validate_reviews.py) and [negative controls](../harness/test_reviews.py) reject promoted theorem status without independent review evidence, a missing Level C, omitted bottlenecks, stale decision logs and self-contradictory progress assertions. These are **structural** guardrails, not proof checkers.

## Special warning: seductive non-progress

A computation of `L'(E^(-7),1) != 0`, a finite `11\)-adic logarithm kernel, or `I^3\) divisibility of a derived Kato class can be entirely correct **without** proving `L''(E,1)=0`. The derived Kato theorem in [BKS 2024](https://doi.org/10.2969/jmsj/90699069) is not automatically an equality of complex analytic and algebraic rank. Full-problem reviews must **trace an actual published or proved comparison map** or assign "no established bridge."

## Sources

- [LMFDB 234446.a1](https://www.lmfdb.org/EllipticCurve/Q/234446/a/1), including numeric BSD invariants and a root-number/local-reduction record.
- [LMFDB L-function reliability](https://www.lmfdb.org/L/2/94192/1.1/c1/0/20/Reliability).
- [Clay Mathematics Institute](https://www.claymath.org/millennium/birch-and-swinnerton-dyer-conjecture/), the general BSD Millennium problem.
- [Burns–Kurihara–Sano 2024](https://doi.org/10.2969/jmsj/90699069), a genuine developed Euler-system framework with separately stated conjectural comparison.

**No review snapshot, CI run or research agent may claim the BSD problem has been solved.**
