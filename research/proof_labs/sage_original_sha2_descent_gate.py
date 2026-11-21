#!/usr/bin/env python3
"""Session53: rigorously typed two-descent gate for ORIGINAL E234446a1.

Runs REAL Sage10.6 PARI and eclib/mwrank 2-Selmer implementations. The
conditional logic is independent of BSD/complex L''/analytic Sha. An
uncomputed rank is NOT printed or asserted as an arithmetic result.
"""
import sys
from sage.all import QQ, ZZ, EllipticCurve, PolynomialRing


def check_one(curve, label, expected=None):
    a = ZZ(curve.selmer_rank(algorithm="pari"))
    b = ZZ(curve.selmer_rank(algorithm="mwrank"))
    print(f"SELMER2 {label} PARI={a} MWRANK={b}", flush=True)
    assert a == b, f"independent 2-descent disagreement for {label}"
    if expected is not None:
        assert a == expected, f"known {label} negative control changed"
    return int(a)


def main():
    E = EllipticCurve(QQ, [1, -1, 0, -79, 289])
    assert E.conductor() == 234446
    assert E.discriminant() == 468892
    A = PolynomialRing(QQ, "X")
    X = A.gen()
    f = X**3 - 1267*X + 17230
    assert f.is_irreducible(), "rational 2-torsion unexpected"
    assert f.discriminant() == 1024 * 117223
    # Five exact historical points include four LMFDB-proven MW generators.
    # This script verifies only their rational coordinates, NOT their
    # independent generation; the certified rank4 is a sourced database input.
    for Pt in [(15,40),(19,4),(23,16),(31,88)]:
        x,y=Pt
        assert y*y == x*x*x-1267*x+17230

    # A 2-Selmer rank can exceed the MW rank: 571a1 is a mandatory
    # known example (rank0 but dim Sel2=2 due to Sha[2]=(Z/2)^2).
    C = EllipticCurve(QQ, [0,-1,1,-929,-10595])
    assert check_one(C, "571a1-Sha2-control", expected=2) == 2
    # Standard rank2 control; distinguishes arithmetic rank2 from rank0.
    B = EllipticCurve(QQ, [0,1,1,-2,0])
    assert check_one(B, "389a1-rank2-control", expected=2) == 2

    n = check_one(E,"234446a1")
    assert n >= 4, "Selmer dimension violates four known independent points"

    # This equivalence is a standard exact sequence, not a BSD theorem:
    # dim Sel2 = rank E(Q) + dim E(Q)[2] + dim Sha[2].
    # Rank(E/Q)=4 and E(Q)[2]=0 are externally certified/checked inputs.
    # No finiteness of Sha is assumed.
    if n == 4:
        print("CERTIFICATE_CONCLUSION Sha(E/Q)[2]=0 (conditional on standard"
              " Selmer exact sequence and certified E(Q) rank4)",flush=True)
        print("CERTIFICATE_CONCLUSION Sha(E/Q)[2^infinity]=0",flush=True)
    else:
        print(f"NO_SHA2_VANISHING_CERTIFICATE Sel2 dimension={n} > MW rank4",
              flush=True)
    print("NONCLAIM: no 11-Selmer upper bound; no Sha-finiteness at odd primes;"
          " no exact complex L''=0; no general BSD proof",flush=True)


if __name__=="__main__":
    main()
