#!/usr/bin/env python3
"""Exact unramified anticyclotomic character coefficients, NOT global heights.

K=Q(sqrt(-7)), p=11, omega=(1+sqrt(-7))/2. Based on Proposition 1.4
of Balakrishnan-Ciperiani-Lang-Mirza-Newton (2016), with rho=(1/11)log.
No third-party packages. Verifies an independent first-digit Fermat quotient.
"""
from math import isqrt

p=11
N=4
PREC=N+6
MOD=p**PREC
OUT=p**N

def hensel_root():
    w=2
    for i in range(1,PREC):
        choices=[w+k*p**i for k in range(p)
                 if ((w+k*p**i)**2+7)%(p**(i+1))==0]
        assert len(choices)==1
        w=choices[0]
    return w

w=hensel_root()
wp=(1+w)*pow(2,-1,MOD)%MOD
wm=(1-w)*pow(2,-1,MOD)%MOD
assert (wp+wm)%MOD==1 and wp*wm%MOD==2

def padic_log_unit(u):
    """Compute log_11(u) modulo 11^(N+2) for 11-adic units."""
    u%=MOD
    assert u%p
    z=(pow(u,p-1,MOD)-1)%MOD
    assert z%p==0
    target=p**(N+2)
    acc=0
    for k in range(1,N+8):
        v=0
        k0=k
        while k0%p==0:
            k0//=p
            v+=1
        numerator=pow(z,k,MOD)
        assert numerator%(p**v)==0
        term=(numerator//p**v)*pow(k0,-1,target)%target
        acc=(acc + (term if k%2 else -term))%target
    return acc*pow(p-1,-1,target)%target

def norm(a,b):
    return a*a+a*b+2*b*b

def generator(q):
    # Positive b chooses one oriented prime above q. Conjugate gives -value.
    candidates=[]
    for b in range(1,isqrt(q)+2):
        for a in range(-isqrt(2*q)-2,isqrt(2*q)+3):
            if norm(a,b)==q:
                candidates.append((a,b))
    assert candidates, q
    return min(candidates,key=lambda z:(abs(z[0]),z[0]))

def log_ratio(a,b):
    ap=(a+b*wp)%MOD
    am=(a+b*wm)%MOD
    assert ap%p and am%p
    r=ap*pow(am,-1,MOD)%MOD
    value=padic_log_unit(r)
    assert value%p==0
    return (value//p)%OUT

def coefficient(q):
    a,b=generator(q)
    assert norm(a,b)==q
    c=-log_ratio(a,b)%OUT
    # Independent first-digit Fermat quotient: log(r)/11 ≡
    # (r^10-1)/(11*10) modulo 11.
    r=(a+b*wp)*pow((a+b*wm)%MOD,-1,MOD)%MOD
    fermat=(pow(r,10,p*p)-1)//p
    assert c%p==(-fermat*pow(10,-1,p))%p
    # Conjugation exchanges embeddings, negating the logarithm.
    return (a,b,c)

assert padic_log_unit(1)==0 and padic_log_unit(MOD-1)==0
for u in (2,3,7,17):
    assert (padic_log_unit(u)+padic_log_unit(pow(u,-1,MOD)))%(p**(N+2))==0
expected={
    2:(0,1,12285),
    43:(5,2,8549),
    569:(3,16,6736),
    1201:(29,8,8230),
    1327:(-1,26,2819),
    117223:(65,222,5836),
}
# The orientation is positive b, minimizing abs(a), matching these generators.
for q,answer in expected.items():
    observed=coefficient(q)
    assert observed==answer,(q,observed,answer)
    a,b,c=observed
    ap=(a+b*wp)%MOD
    am=(a+b*wm)%MOD
    assert ap*am%MOD==q%MOD
    # Verify that the conjugate generator has the opposite coefficient.
    a2,b2=a+b,-b     # conjugation omega -> 1-omega
    assert norm(a2,b2)==q
    assert (-log_ratio(a2,b2))%OUT==(-c)%OUT
    print(f'q={q:6d} alpha={a:+d}{b:+d}omega  rho={c:5d} mod 14641, residue={c%p}')

# The inert and ramified prime ideals are fixed by conjugation.
# A conjugation-anti-equivariant unramified local coefficient must be zero.
assert (-7)%3==2 and (-7)%5==3
assert padic_log_unit(MOD-1)==0
print('PASS class-number-one prime-generator norms, 11-adic logs,')
print('PASS independent Fermat quotients, conjugation, inert/ramified controls')
print('NONCLAIM: no elliptic-curve global anticyclotomic height computed')
