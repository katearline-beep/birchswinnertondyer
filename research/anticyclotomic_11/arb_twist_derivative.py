#!/usr/bin/env python3
"""Independent FLINT/Arb ball check of the EXISTING 6000-term certificate.

Requires python-flint==0.9.0. In CI, read PARI ellan coefficients from a file;
otherwise enumerate finite-field squares and reconstruct Euler coefficients.
No repository imports, hand-coded E1 series, gamma enclosure or Machin pi.
Same modularity, twist/conductor/root-sign and Mellin identity are inputs.
Purpose: validate a subsidiary analytic-rank-one input to one-sided Selmer
control, not improve precision or claim original rank-four BSD.
"""
import hashlib
import sys
from math import isqrt
import flint
from flint import arb, ctx

TERMS=6000
N=234446
TWIST_CONDUCTOR=49*N
DIGEST='3b4d1fb4039c5f18e339566cd7f9a8e395ee0e4c6af2c92f7b69addf094f11ea'


def coefficients():
    """Exact independent point-count organization: square frequencies."""
    primes=[]
    sieve=[True]*(TERMS+1)
    for q in range(2,TERMS+1):
        if not sieve[q]: continue
        primes.append(q)
        for t in range(q*q,TERMS+1,q): sieve[t]=False
    a=[0]*(TERMS+1); a[1]=1
    powers={}
    for q in primes:
        if q==2:
            solutions=sum((y*y+x*y-x*x*x+x*x+79*x-289)%q==0
                          for x in range(q) for y in range(q))
        else:
            squares=[0]*q
            for y in range(q): squares[y*y%q]+=1
            # (2y+x)^2 = 4x^3-3x^2-316x+1156.
            solutions=sum(squares[(4*x*x*x-3*x*x-316*x+1156)%q]
                          for x in range(q))
        trace=q-solutions
        seq=[1,trace]; power=q
        while power*q<=TERMS:
            seq.append(trace*seq[-1]-(0 if N%q==0 else q)*seq[-2])
            power*=q
        powers[q]=seq
    for n in range(2,TERMS+1):
        q=next(q for q in primes if n%q==0)
        k=0; t=n
        while t%q==0: k+=1; t//=q
        a[n]=a[t]*powers[q][k]
    return a[1:]


def validate_coefficients(a):
    if len(a)!=TERMS: raise ValueError('expected exactly 6000 coefficients')
    digest=hashlib.sha256(','.join(map(str,a)).encode()).hexdigest()
    if digest!=DIGEST: raise ValueError('coefficient digest disagrees with PARI-checked input')


def enclose(a):
    ctx.prec=160
    c=2*arb.pi()/arb(TWIST_CONDUCTOR).sqrt()
    partial=arb(0)
    for n,an in enumerate(a,1):
        r=n%7
        chi=0 if r==0 else (1 if r in (1,2,4) else -1)
        if chi and an:
            partial+=2*an*chi*(c*n).expint(1)/n
    # Same all-n bound |a_n|<=2n and elementary E1(x)<=exp(-x)/x.
    # Use the OLD rational c0 and geometric tail, not new extra terms/digits.
    c0=arb('1853789485821/1000000000000000')
    assert c>c0
    q=1/(1+c0)
    tail=4*q**(TERMS+1)/(c0*(TERMS+1)*(1-q))
    assert tail>0 and tail<arb('2895/1000000')
    certificate=partial+arb(0,tail.upper())
    assert certificate.is_finite() and certificate>0
    assert certificate>arb('34.1691') and certificate<arb('34.1750')
    return partial,tail,certificate


def main():
    if len(sys.argv)==2:
        with open(sys.argv[1],encoding='utf8') as source:
            a=[int(line.strip()) for line in source if line.strip()]
        mode='external PARI coefficient file'
    elif len(sys.argv)==1:
        a=coefficients(); mode='independent square-frequency finite-field counts'
    else: raise SystemExit('usage: arb_twist_derivative.py [pari-coefficients.txt]')
    validate_coefficients(a)
    bad=a.copy(); bad[16]+=1
    try: validate_coefficients(bad)
    except ValueError: pass
    else: raise AssertionError('mutated coefficient was accepted')
    partial,tail,certificate=enclose(a)
    # A positive midpoint is insufficient if the full error ball crosses 0.
    inflated=partial+arb(0,40)
    assert inflated.contains(0) and not inflated>0
    print('python-flint',flint.__version__,'precision',ctx.prec,'bits')
    print('COEFFICIENT INPUT:',mode,'SHA256',DIGEST)
    print('FINITE ARB BALL',partial.str(25))
    print('INFINITE TAIL UPPER',tail.upper().str(15))
    print('PASS strict rational enclosure: 34.1691 < Lprime < 34.1750')
    print('PASS coefficient mutation and positive-midpoint/uncertain-radius negative controls')
    print('CONDITIONAL on modularity, twist local data, Mellin identity and coefficient bound.')
    print('NONCLAIM: no expert review, Sha[11] triviality, original complex Lpp or BSD.')


if __name__=='__main__': main()
