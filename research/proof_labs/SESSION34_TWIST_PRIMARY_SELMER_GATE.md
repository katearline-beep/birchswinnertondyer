# Session34 — predeclared twist-primary Selmer gate

2026-10-20 America/New_York, main07f8902 / PR67; issue68. AI-assisted unreviewed.

Before arithmetic: audit Zhang Theorems1.6/10.3 for the additive -7 twist, checking residual image, good ordinary11, multiplicative ramification and nonsquarefree-conductor conditions. Screen the numerical period/regulator/known-point quotient; no real near-integer observation may certify11-adic valuation. Require an explicit denominator/integrality or p-adic alternative before asserting Sha11=0. Safe lemma: a full residual negative Selmer line gives three first-Bockstein survivors on known positive MW classes by finite duality. Credible leapfrog: certify that line via a valid rank-one p-primary theorem and bounded arithmetic. Wild option: level lowering or geometric cycle comparisons, still without an original complex bridge. Stop if theorem applicability or exact valuation cannot be supplied.

Predeclared alternate exact experiment: the existing q3389 also satisfies q=1 mod11 and a_q(Et)=2 mod11. Audit the Kurihara-number residual Selmer theorem, then attempt an exact one-prime modular-symbol quantity for the twist using the original curve's minus modular symbol and a conductor7 twisting sum. First resource gate: PARI msfromell on the ORIGINAL conductor234446 only, capped at60 seconds and2GiB address space. A timeout/resource refusal is a computational limit, not a zero symbol or arithmetic nonexistence. No Selmer claim without exact period-unit, residual-theorem hypotheses and a nonzero mod11 certificate.

## Outcome and source-derived implications

The decisive arithmetic certificate is **still uncomputed**. This session supplies an applicable published theorem, an exact alternative certificate target, and independently checked inputs/control calculations. It does not establish a new Selmer upper bound. All deductions below are AI-assisted, unreviewed source specializations; the programs do not prove the cited theorems.

### 1. A rank-one p-primary theorem that permits this additive twist

Use Wei Zhang, *Selmer groups and the indivisibility of Heegner points* (2014), [author PDF](https://math.mit.edu/~wz2113/math/online/Kconj.pdf), Theorems1.4 and1.6, equivalently10.3. Unlike the semistable hypotheses of Jetchev–Skinner–Wan and Berti–Bertolini–Venerucci, these hypotheses allow our conductor to contain a square factor. They require residual surjectivity, ordinary p>=5, ramification at multiplicative primes congruent to plus/minus1 modp, and a nonsquarefree-conductor ramification/parity condition.

For A=E^(-7), p=11:

| Object | Exact input and obligation |
|---|---|
| Short model | [0,0,0,-62083,-5909890] |
| Minimal model | [1,-1,0,-3880,-91372] |
| Conductor | 11487854 = 2 * 7^2 * 117223 |
| Multiplicative primes | 2 and117223, residues2 and7 mod11; neither is plus/minus1 |
| Additive prime | 7, Kodaira I0*, Tamagawa1; does not invalidate this theorem |
| Other Tamagawas | c2=2, c117223=1, product2 |
| Residual image | Recorded C0036 GL2 over GK; twist is trivial on GK, hence surjectivity over GQ also |
| Ramification | I1 at117223, valuation of minimal discriminant1, gives nontrivial mod11 inertia; at least one ramified multiplicative prime |
| Nonsquarefree parity | Exactly two primes ell||N; Zhang's even-count condition holds even if only one residual ramified prime is used |
| Good ordinary11 | a11=-6, #A(F11)=18; also nonanomalous |
| Analytic rank1 | Accept C0032's nonzero derivative certificate and root number-1, with its analytic/source review boundary |

Therefore, accepting these recorded inputs, Zhang's theorem gives the **11-part leading-term identity for A/Q**. This is a specialization of a published rank-one theorem, not a claim about the original rank-four curve. It gives an identity of valuations, not the value of the normalized quotient.

### 2. Real quotient screening does not determine that valuation

The known point in short coordinates is (3355/9,128780/27), or Q=(841/9,14836/27) on the minimal model. PARI2.15.4 gives height approximately7.05782307761663 and

    Lprime(A,1) / (ellbsd(A) * ellheight(A,Q)) = 4.000... .

The predeclared guess 'near1' was incorrect; the diagnostic is near4. `ellbsd` includes the real-period, Tamagawa and torsion normalization. The display is a numerical diagnostic, **not an exact rational reconstruction**. Reproduce the screening expression after initializing the minimal model: `ellL1(A,1)/(ellbsd(A)*ellheight(A,[841/9,14836/27]))`. C0035 makes Q eleven-primitive but is not an all-prime MW-basis certificate. Under a fully justified normalized identity the regulator index contributes a square, and its eleven-part is a unit here. None of that turns a real approximation into an exact11-adic unit.

The executable constructs rationals arbitrarily close to4 with valuation exactly2, alongside4 of valuation0. Denominators are prime to11. It also checks that a nonprimitive point-index square can hide a factor121, and that finite Sha=(Z/11)^2 enlarges residual Selmer dimension from1 to3 while rational corank stays1. Thus neither finite Sha nor a near-integer decimal certifies Sha[11]=0.

### 3. A better exact target: one-prime Kurihara number

Use Ryotaro Sakamoto, *p-Selmer group and modular symbols*, Documenta Math27(2022),1891–1922, [published PDF](https://ems.press/content/serial-article-files/29299?nt=1), hypotheses(a)–(c), Theorem1.5/4.8 and **Remark1.6**. These require p>3 ordinary, surjective residual representation, and p not dividing #A(Fp) times the Tamagawa product. All pass the same recorded inputs. No separate main-conjecture assumption is needed for the implication from a computed nonzero Kurihara number.

At the existing prime q=3389, direct point enumeration gives #A(Fq)=3498=11*318, and a_q=-108 congruent2 mod11. Since q=1 mod11 and the order has valuation exactly1, A(Fq)[11] is one-dimensional. Thus q belongs to Sakamoto's P_1,0. With primitive generator h=3, define

\[
\widetilde\delta_q(A)=\sum_{a=1}^{q-1}\log_h(a)\,
 \frac{\operatorname{Re}(2\pi i\int_{i\infty}^{a/q}f_A(z)\,dz)}{\Omega_A^+}
 \pmod {11}.
\]

Sakamoto's published integrality statement makes the summands11-integral under residual surjectivity. A **nonzero exact** value would give dim Sel_11(A/Q)<=1. C0035's nonzero Kummer point then gives equality and Sha(A/Q)[11]=0. A zero value at this particular q would be inconclusive. Prime eligibility, point counts or a small-curve control alone do not compute this value.

### 4. Lower-level twisting algorithm and actual control

Initializing full modular symbols directly at the twist conductor11,487,854 is avoidable. Let chi be the primitive quadratic character of conductor7. Its Gauss sum is i*sqrt7, and the q-expansion twisting identity gives

\[
 f_A(z)=\tau(\chi)^{-1}\sum_{b=1}^6\chi(b)f_E(z+b/7).
\]

Consequently twist plus symbols come from original **minus** symbols at a/q+b/7. At11 the differential/period factor is a unit: the twist isomorphism identifies integral anti-invariant homology with invariant homology over C, its differential scales by1/sqrt(-7), and both displayed short-to-minimal changes have u=2. Any connected/full-real-period convention introduces only a factor2. Neither7 nor2 affects nonvanishing mod11. For exact scalar values keep the same connected-period convention as PARI; only nonvanishing is used here. See [PARI modular-symbol documentation](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Modular_symbols.html), `msfromell`, for its normalized plus/minus periods. This argument is a normalization proof obligation for a future focal certificate, not something inferred from floating periods.

**Executed orthogonal control:** original curve37a1=[0,0,1,-1,0], twist [0,0,1,-49,-86] of conductor1813. PARI computes both original minus symbols and direct twist plus symbols. At a/13 for a=1,...,6, the twisted sums and direct values agree exactly:

    (1,1,1,-2,1,-2).

Using the original plus sign instead gives (-2,-2,-2,1,-2,-1), rejected at every test. This is an exact small-curve control, not a focal-symbol computation. Upstream [Ghitza–Kim implementation](https://github.com/aghitza/kurihara_numbers/blob/master/kurihara.sage) was inspected read-only: it uses eclib's curve modular symbols and discrete-log weights. Inspected upstream blob SHA a027af150faadc8fbf3f6377851030dd3846664a. No eclib/Sage runtime is available locally; no upstream contact was made and no code was copied.

**Resource experiments:** PARI `msfromell(E,-1)` at original conductor234446 was capped first at60s/2GiB and then at300s/2GiB, using fixed stacks256MB and512MB respectively. The first timed out without a symbol. The second stopped after125.4s with an explicit PARI stack overflow at512000000 bytes, before the300s time cap. GP returned process exit0 despite the interpreter error; this is a failed computation, not successful output. No usable symbol cache was written. Resource refusal is not an arithmetic zero. No focal symbol, delta value, or Selmer bound may be inferred from it. Repeating resource runs without a better algorithm is deprioritized; use sparse/eclib curve-specific symbols for the next attempt.

### 5. Conditional finite Selmer bridge to first lifts

Let S=Sel_11(E/K) with its complex-conjugation decomposition. **If** the complete negative residual part is the line generated by R, and the integral self-dual Selmer complex has the asserted finite first-Bockstein/height comparison and perfect obstruction duality, then a positive class has zero first Selmer Bockstein exactly when its first pairing with R vanishes. The anti-invariant character forces same-sign first pairings to vanish. There is no need to bound the full positive dimension.

With the verified/provisional first row(1,2,7,8), the known positive kernel frame is

    P2-2P1, P3-7P1, P4-8P1  (mod11).

Under the full stated hypotheses these are **residual first-stage Selmer survivors**, not exact Q11 S2 representatives, supplied cochains, T3 lifts or nonzero second pairings. A hidden negative Sha direction defeats the inference; the executable deliberately supplies such a countermodel. This is why the exact Kurihara certificate would matter.

## Reproduction and scope

Run:

    python3 -I -B research/proof_labs/twist_primary_selmer_gate.py
    gp -q -f -s 128000000 research/proof_labs/pari_twist_selmer_gate.gp > /tmp/selmer34.txt
    python3 -I -B research/proof_labs/twist_primary_selmer_gate.py --pari /tmp/selmer34.txt

The parser rejects interpreter errors, incomplete/mutated symbol values and missing completion. CI runs both implementations. The Python program independently enumerates focal finite-field points and complete discrete logs; it does not certify minimal-model reduction or any published theorem.

**Whole-BSD review:** no new implication to original complex L''=0, exact analytic rank4, original Sha finiteness or leading coefficient. H1 remains prioritized toward actual arithmetic lifts with a better residual-domain certificate; H2 actual h2 remains limited/open; H3 retains its separately scoped geometric comparison investigation; H4/H6 remain parked and H5 diagnostic. The source-derived rank-one p-BSD specialization and Kurihara certificate criterion are useful reductions, not discoveries of BSD proofs or peer-reviewed new mathematics.
