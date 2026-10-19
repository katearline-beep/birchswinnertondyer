#!/usr/bin/env python3
"""Exact 6000-coefficient comparison: PARI ellan vs separate Python recursion.

PARI derives coefficients from a mature elliptic arithmetic library.
This test does NOT prove that the common mathematical model/normalization
is correctly tied to the derivative series, but eliminates an important
independent-input discrepancy.
"""
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
from pathlib import Path
import runpy
import sys

ROOT=Path(__file__).resolve().parents[2]
TARGET=ROOT / "research/anticyclotomic_11/independent_rational_derivative_6000.py"
N=6000

def parse_pari(path):
    text=Path(path).read_text(encoding="utf8").strip()
    assert "***" not in text, "PARI interpreter errors are not acceptable"
    lines=text.splitlines()
    assert len(lines)==N, f"PARI produced {len(lines)} coefficients instead of {N}"
    assert all(x.lstrip("-").isdigit() for x in lines), "Unexpected GP output"
    return [int(x) for x in lines]

def crosscheck(gp,py):
    assert len(gp)==N and len(py)==N+1
    mismatches=[n for n in range(1,N+1) if gp[n-1]!=py[n]]
    assert not mismatches, "Fourier mismatch at "+str(mismatches[:15])

def main():
    assert len(sys.argv)==2, "Usage: compare_fourier_coefficients.py GP_OUTPUT"
    out=StringIO()
    with redirect_stdout(out):
        data=runpy.run_path(str(TARGET),run_name="__main__")
    py=data["a"]
    gp=parse_pari(sys.argv[1])
    crosscheck(gp,py)
    digest=sha256(",".join(map(str,gp)).encode("ascii")).hexdigest()
    print("PASS: PARI ellan matches all 6000 Python Fourier coefficients")
    print("SHA256 canonical CSV of 2000 coefficients:",digest)
    mutated=gp[:]
    mutated[16]+=1
    try:
        crosscheck(mutated,py)
    except AssertionError:
        print("PASS negative control: a_17 mismatch correctly rejected")
    else:
        raise AssertionError("Mutated independent coefficient not detected")
    print("NONCLAIM: does not certify Mellin identity, root number or full BSD")

if __name__=="__main__":
    main()
