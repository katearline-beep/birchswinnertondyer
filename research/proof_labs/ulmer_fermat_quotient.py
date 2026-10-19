#!/usr/bin/env python3
"""Ulmer 2002 Section 4.2 Fermat-to-elliptic surface map, exact certificate.

Proves polynomial identity over Z and finite symmetry-group checks.
It DOES NOT prove Tate, a global zeta formula, rank or BSD.
"""
def mon(*v):
    assert len(v)==4
    return tuple(v)
def add(a,b):
    return tuple(x+y for x,y in zip(a,b))
def power(a,k):
    return tuple(k*x for x in a)
def evaluate(exponents,coords,p):
    result=1
    for n,x in zip(exponents,coords):
        if n<0:
            assert x%p
            result=result*pow(pow(x,-1,p),-n,p)%p
        else:
            result=result*pow(x,n,p)%p
    return result

def verify(d):
    # Ulmer (2002), Section 4.2:
    # X=(x0*x1*x2)^d, Y=(x0^2*x2)^d, Z=-x1^(3d),
    # t=x0^3*x2^2*x3/x1^6.
    X=mon(d,d,d,0)
    Y=mon(2*d,0,d,0)
    Z=mon(0,3*d,0,0)
    t=mon(3,-6,2,1)
    C=mon(3*d,3*d,2*d,0)
    observed=[add(power(Y,2),Z),add(add(X,Y),Z),
              power(X,3),add(power(Z,3),power(t,d))]
    predicted=[add(C,mon(d,0,0,0)),add(C,mon(0,d,0,0)),
               add(C,mon(0,0,d,0)),add(C,mon(0,0,0,d))]
    assert observed==predicted and len(set(observed))==4
    # Consequently Y^2 Z+XYZ-X^3+Z^3 t^d
    # = -(x0^3*x1^3*x2^2)^d *(x0^d+x1^d+x2^d+x3^d)
    for action in (mon(2,1,0,0),mon(0,1,3,0)):
        for term in (X,Y,Z,t):
            assert sum(x*y for x,y in zip(action,term))%d==0
    gamma={((2*a)%d,(a+b)%d,(3*b)%d,0)
           for a in range(d) for b in range(d)}
    assert len(gamma)==d*d
    # A wrong exponent of x3 in t fails the symbolic identity.
    assert add(power(Z,3),power(mon(3,-6,2,2),d))!=predicted[3]
    return X,Y,Z,t

def example(p,d,point):
    assert all(x%p for x in point)
    assert sum(pow(x,d,p) for x in point)%p==0
    X,Y,Z,t=verify(d)
    x=evaluate(X,point,p)
    y=evaluate(Y,point,p)
    z=-evaluate(Z,point,p)%p
    tv=evaluate(t,point,p)
    assert z
    assert (y*y*z+x*y*z-x*x*x+pow(z,3,p)*pow(tv,d,p))%p==0
    xx=x*pow(z,-1,p)%p
    yy=y*pow(z,-1,p)%p
    assert (yy*yy+xx*yy-xx*xx*xx+pow(tv,d,p))%p==0
    if p==5:
        bad_t=tv*point[3]%p
        assert (yy*yy+xx*yy-xx*xx*xx+pow(bad_t,d,p))%p!=0
    print(f"PASS F_{p}: d={d}, Fermat {point} maps to (x,y,t)={(xx,yy,tv)}")

if __name__=="__main__":
    for d in (6,8,26):
        verify(d)
        print(f"PASS d={d}: integral polynomial identity and Gamma order {d*d}")
    example(5,6,(1,1,2,2))
    example(7,8,(2,1,1,1))
    print("PASS exact polynomial map over Z, including characteristic-zero identity")
    print("NONCLAIM: map identity and Gamma order alone do not prove birationality, Tate, ranks or BSD")
