#!/usr/bin/env python3
"""Independent direct Jacobi sum for Ulmer (2002), p=7, d=8, F_49.

For Gamma^perp a=(3,-6,2,1)=(3,2,2,1) mod8, orbit length 2.
Ulmer Prop8.1 predicts J(a)=q^u=49. Direct character enumeration over
F_49 evaluates the entire numerator in Z[zeta8]. Published Tate/BSD,
the other Jacobi orbits and complex comparison are NOT proved.
"""
p=7;q=49;d=8

def pair(x):
    return x%p,x//p
def encode(a,b):
    return a%p+p*(b%p)
def add(x,y):
    a,b=pair(x);c,e=pair(y)
    return encode(a+c,b+e)
def neg(x):
    a,b=pair(x)
    return encode(-a,-b)
def mul(x,y):
    a,b=pair(x);c,e=pair(y)
    return encode(a*c-b*e,a*e+b*c)  # i^2=-1, irreducible over F7
def power(x,n):
    result=1
    while n:
        if n&1:result=mul(result,x)
        x=mul(x,x);n//=2
    return result

def logs_for(g):
    assert power(g,48)==1 and power(g,24)!=1 and power(g,16)!=1
    log={};v=1
    for k in range(48):
        assert v not in log
        log[v]=k;v=mul(v,g)
    assert v==1 and len(log)==48
    return log

def jacobi_numerator(log,a):
    assert len(a)==4 and sum(a)%d==0 and all(z%d for z in a)
    counts=[0]*d
    for x0 in range(1,q):
        for x1 in range(1,q):
            partial=neg(add(x0,x1))
            for x2 in range(1,q):
                x3=add(partial,neg(x2))
                if x3:
                    k=(a[0]*log[x0]+a[1]*log[x1]+a[2]*log[x2]+a[3]*log[x3])%d
                    counts[k]+=1
    # Mod the cyclotomic equation zeta8^4=-1.
    assert sum(counts)==48**3-(48**2-48)
    return tuple(counts[k]-counts[k+4] for k in range(4))

a=(3,2,2,1)
assert sum(a)%8==0
assert (3*7%8,2*7%8,2*7%8,7%8)!=(3,2,2,1)
assert (3*7*7%8,2*7*7%8,2*7*7%8,7*7%8)==a
g=next(x for x in range(2,q) if power(x,48)==1 and
       power(x,24)!=1 and power(x,16)!=1)
first=jacobi_numerator(logs_for(g),a)
# A different primitive generator changes the character embedding,
# but the expected Jacobi eigenvalue 49 is rational and unchanged.
second=jacobi_numerator(logs_for(power(g,5)),a)
assert first==second==(48*49,0,0,0),(first,second)
try:jacobi_numerator(logs_for(g),(3,2,2,2))
except AssertionError:pass
else:raise AssertionError("invalid nontrivial-product character was accepted")
print("PASS F49 exact field, two primitive generator choices, full character sum")
print("PASS Ulmer d8 orbit length2, exact Jacobi numerator 48*49 -> J(a)=49")
print("PASS wrong-character precondition rejected")
print("NONCLAIM: one Jacobi sum is not all Fermat zeta factors, Tate, BSD or original complex L''")
