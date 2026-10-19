#!/usr/bin/env python3
"""Canonical sigma-series auxiliary u11=E2/12 modulo 11^2 via t^23 integrality.

Reuses exact formal sigma-family constructor from Session 16, and extends its
precision and the published MST conductor-37/p5 control to the second digit.
All rational arithmetic, no Sage dependency. The canonical integrality
theorem is mathematical input, not proved by this script; no BSD theorem.
"""
from pathlib import Path
from fractions import Fraction as F
import contextlib,importlib.util,io,math

source=Path(__file__).with_name("canonical_sigma_integrality_11.py")
spec=importlib.util.spec_from_file_location("_s16_sigma",source)
s=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(s)

def integral_at(v,p):
    return v.denominator%p != 0

def evaluate(poly,c):
    return sum(coeff*c**i for i,coeff in enumerate(poly))

# Independent published MST 2006 Section 4.1 second-digit control:
# c_5 = 1 + 5 + O(5^2); sigma(t) t^11 integrality selects 6 mod25.
choices5=[1+5*k for k in range(5)]
for degree in range(1,12):
    polynomial=s.sigma_c_polynomial(0,0,1,-1,0,degree)
    roots=[c for c in choices5 if integral_at(evaluate(polynomial,c),5)]
    if degree<11:assert roots==choices5,(degree,roots)
    else:assert roots==[6],roots
print("PASS published MST E37 p=5 series u_5=6 mod25, PARI s2=19")

# Target E=[1,-1,0,-79,289] at p=11:
# c_11=4 mod11 from t^13; t^23 is next discriminating integrality condition.
choices11=[4+11*k for k in range(11)]
for degree in range(1,24):
    polynomial=s.sigma_c_polynomial(1,-1,0,-79,289,degree)
    roots=[c for c in choices11 if integral_at(evaluate(polynomial,c),11)]
    if degree<23:assert roots==choices11,(degree,roots)
    else:assert roots==[26],roots
numer_den=math.lcm(*(v.denominator for v in polynomial))
assert numer_den%121==0 and (numer_den//121)%11!=0
# Stronger independent residual fingerprint:
# 11*[t^23]sigma_{c=4+11*k} = (8-4*k) modulo 11.
for k in range(11):
    value=11*evaluate(polynomial,4+11*k)
    assert value.denominator%11
    residue=value.numerator*pow(value.denominator,-1,11)%11
    assert residue==(8-4*k)%11,(k,residue)
assert (12*26)%121==70
assert ((-3-70)*pow(12,-1,121))%121==4
print("PASS target t^23 sigma integrality, unique canonical series u_11=26 mod121")
print("PASS E2=12*u=70 and PARI s2=b2/12-u=4 mod121; 11*sigma23=(8-4k) mod11")
print("NONCLAIM: canonical sigma integrality is a published theorem,")
print("NONCLAIM: no external Sage/Magma sigma, complex L'' or BSD proof")
