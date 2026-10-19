# Session 17 — Canonical sigma modulo 121 and three anticyclotomic height digits

**2026-10-19 · AI-assisted, exact arithmetic and published-theorem dependencies; not an independent Sage/Magma computation or external human peer review.**

## Whole-BSD orientation and scope

The original complex analytic rank-four bottleneck remains unproved: **\(L''(E,1)=0\)** for the Hasse–Weil complex L-function of 234446.a1. Computing anticyclotomic \(11\)-adic heights improves a *different arithmetic invariant* and neither settles analytic rank nor general Birch–Swinnerton–Dyer. Sha finiteness and the full leading-coefficient formula are also open. This is a continuation of C-0012, **not** evidence of a new complex comparison theorem.

## Second canonical Mazur–Tate coefficient digit

**Convention correction:** throughout the exact symbolic polynomial and anticyclotomic height formulas below, `c` denotes the *series coefficient* `u=E2/12`, not the Mazur–Stein–Tate/PARI slope `s2=(b2−E2)/12`. Our model has b2=−3. Thus u=26 modulo121 corresponds to E2=70 and to independent PARI `ellpadics2` value s2=4, and E37/p5 series u=6 corresponds to PARI s2=19. Earlier C-0012/Session16 prose equated these conventions; that was incorrect and is explicitly corrected, with numerical heights unchanged.

Use the exact standard-library formal sigma-family construction in [Session 16](canonical_sigma_integrality_11.py) and Mazur–Stein–Tate (2006), Algorithms 3.1/3.3, which state that the canonical sigma coefficients are \(p\)-adically integral.

We previously derived \(u_{11}\equiv4\pmod{11}\) from integrality at \(t^{13}\). Write \(u=4+11k\), \(k\in\{0,\ldots,10\}\). In the target curve \(E:y^2+xy=x^3-x^2-79x+289\), the next informative obstruction appears at \([t^{23}]\sigma_c(t)\); its common rational-polynomial denominator has \(11\)-adic valuation **two**. A direct exact computation gives the low-digit *residue identity*
\[
\boxed{11[t^{23}]\sigma_{4+11k}(t)\equiv 8-4k\pmod{11}.}
\]
Since a canonical integral coefficient requires this residual fraction to vanish, \(k=2\) is the **unique** permissible second digit:
\[
\boxed{u_{11}=E_2/12\equiv26\pmod{121},\qquad E_2\equiv70\pmod{121},\qquad s_2=b_2/12-u_{11}\equiv4\pmod{121}.}
\]
All coefficients \([t^j]\sigma_c(t)\) for \(1\le j<23\) are 11-adically integral for *all* 11 candidates \(u\equiv4\pmod{11}\); the script checks each coefficient, rather than assuming only the two boundary degrees matter.

**Published independent sanity oracle at the same precision:** On \(y^2+y=x^3-x\), \(p=5\), Mazur–Stein–Tate §4.1 explicitly report \(c_5=1+5+O(5^2)\), i.e. \(c_5\equiv6\pmod{25}\). Our *same code* checks integrality at every degree \(1\le j\le11\); the unique surviving \(c=1+5k\) at \(t^{11}\) is **6 mod25**, agreeing with their published computation. Both target and control are exact rational coefficients, not floating point.

[Executable integrality and published-control check](canonical_sigma_integrality_121.py).

## Third anticyclotomic height digit modulo 1331

For the original minimal model the sigma-family expansion is
\[
\boxed{\frac{\sigma_{11}(t)}t =
1+\frac t2+\frac{c_{11}}2 t^2+\frac{3c_{11}-1}{4}t^3+O(t^4),\quad c_{11}=26\bmod121.}
\]
The \([36]\)-multiple \(T=[36]Q\) of each point used below lies in the 11-adic formal group at both primes over 11, with \(v_{11}(t)=1\). Since the sigma coefficients are 11-adically integral, the \(O(t^4)\) contribution after dividing by \(t\) lies in \(11^4\mathbb Z_{11}\), which cannot alter \((1/11)\log\) modulo \(11^3\).

As in BCLMN Proposition 2.4, let \(D\) be the **primitive global square-root denominator ideal generator** of \(x(T)\). The exact rational-affine implementation verifies \(x(T)D^2,y(T)D^3\in\mathcal O_K\) and \(\gcd_{\mathbb Z}(N(x(T)D^2),N(D))=1\), at **all ten** inputs. At the two fixed split embeddings of \(K=\mathbb Q(\sqrt{-7})\) into \(\mathbb Q_{11}\) compute
\[
u_\pm=\frac{t_\pm}{D_\pm}
\left(1+\frac{t_\pm}{2}+\frac{c_{11}t_\pm^2}{2}
 +\frac{(3c_{11}-1)t_\pm^3}{4}\right)\!\!\pmod{11^4},
\]
\(q=u_+/u_-\), and \(h_\rho(Q)=36^{-2}\frac1{11}\log_{11}(q)\pmod{1331}\). With \(z=q^{10}-1\pmod{11^4}\), compute \(\log(q)/11\) by \((z-z^2/2+z^3/3)/(11\cdot10)\pmod{1331}\).

**Full ten-point result, still provisional:**

| Point Q | q mod 14641 | height hρ(Q) mod 1331 |
|---|---:|---:|
| P1+R | 13126 | **1068** |
| P2+R | 3587 | **1300** |
| P3+R | 13985 | **854** |
| P4+R | 9553 | **8** |
| P1+P2+R | 12147 | 1037 |
| P1+P3+R | 12893 | 591 |
| P1+P4+R | 7154 | 1076 |
| P2+P3+R | 4129 | 823 |
| P2+P4+R | 6671 | 1308 |
| P3+P4+R | 14221 | 862 |

Each of the **six distinct-input mixed heights** equals \(h_\rho(P_i+R)+h_\rho(P_j+R)\pmod{1331}\). All first four values reduce to Session 16's \((100,90,7,8)\pmod{121}\) and Session 14's \((1,2,7,8)\pmod{11}\).

**Negative control:** deliberately retain the *stale* \(u_{11}=4\) instead of canonical \(u_{11}=26\). The first two digits remain unchanged, but at least one third digit changes. The third digit is therefore genuinely sensitive to the **new** canonical sigma parameter rather than an automatic repeat of earlier precision.

[Ten-height and six mixed-pair verifier](conditional_heights_mod1331.py).

## Global positive radical versus local log kernel

The conditional global self-height vector is \(a=(1068,1300,854,8)\bmod1331\) with \(1068\) a unit and
\[
\boxed{[a_1:a_2:a_3:a_4]=[1:739:766:668]\pmod{1331}.}
\]
The known two-prime local elliptic logarithm projective profile at the *same* precision is \([1:704:772:856]\pmod{1331}\). Both reduce respectively to the previously distinct profiles \([1:13:40:63]\) and \([1:99:46:9]\pmod{121}\), then \([1:2:7:8]\) and \([1:0:2:9]\pmod{11}\).

Assuming the genuine symmetric anticyclotomic height is conjugation anti-equivariant, its positive-direction coefficient-kernel generators at this finite precision are
\[
\boxed{P_2-739P_1,\quad P_3-766P_1,\quad P_4-668P_1\pmod{1331}.}
\]
These are **coefficient vectors in a finite modular approximation** to the actual \(\mathbb Q_{11}\) positive height radical; they are NOT exact rational-point identities or proof of derived height nondegeneracy. The L11 *auxiliary* local/global kernel-alignment hypothesis is conditionally contradicted, not BSD.

## Explicit reliability gates and future route

- **Published input theorems:** Mazur–Stein–Tate canonical \(\sigma\)-integrality and BCLMN anticyclotomic height formula with a fixed idele-class character, local sign, identity component, split embeddings and minimal invariant differential. The code checks algebraic ingredients, not the proofs of these theorems.
- **Not yet met:** reproduction with an independently maintained *full* Sage/Magma \`padic_sigma(11,\cdot)\` and a separate BCLMN global-height implementation; independent PARI \`ellpadics2\` *only* checks the canonical sigma slope, and expert confirmation that all source hypotheses are met. Multiple own Python scripts and controls are not peer review.
- **Stop rule:** If a distinct software package disagrees on \(c_{11}\), height normalization or global denominator ideals, downgrade and debug C-0012/C-0013 before making a height radical assertion. No exact \(\mathbb Q_{11}\)-radical is established by finite congruences.
- **Next arithmetic milestone:** external canonical sigma review, then derived-height computation on the *global* radical. **Separate H3 complex track:** seek a truly third-derivative geometric identity for complex \(L(E/K,s)\) that could constrain original complex \(L''(E,1)\). Do not present the 11-adic height as that missing comparison.

**Sources:** [MST p-adic heights and log convergence](https://ems.press/content/book-chapter-files/27479), [BCLMN shadow lines and global height algorithm](https://arxiv.org/pdf/1610.08729), [Session 16](SESSION16_CANONICAL_SIGMA_MOD121.md), and [whole-BSD review](../reviews/2026-10-19-whole-problem.md).

**What was established about the original complex BSD problem in Session 17:** **No new missing implication.**
 

**Independent PARI verification (CI):** [PARI oracle](pari_canonical_sigma_oracle.gp) uses `ellpadics2` to check **s2=4** for our curve modulo121 and **s2=19** for the published E37 curve modulo25. It converts `E2=b2−12s2=70` and `u=E2/12=26` on the target and `u=6` on the E37 control. This independent software check does **not** itself validate the full number-field anticyclotomic height or division-polynomial computation.
