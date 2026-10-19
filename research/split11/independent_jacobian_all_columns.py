#!/usr/bin/env python3
"""Independent check by Jacobian arithmetic modulo 11^25.

No rational-quadratic elliptic arithmetic, no affine point inversions in
calculating [18]P: all point multiplications are in projective coordinates.
This is corroboration of a local-log calculation, NOT a global height.
"""
from fractions import Fraction
p=11
M=p**25
L=p**4
A=-1267
B=17230

# Hensel lifting independent of K arithmetic and group law.
def root():
    r=2
    for k in range(1,25):
        for v in range(11):
            cand=r+v*(11**k)
            if (cand*cand+7)%(11**(k+1))==0:
                r=cand
                break
        else: raise AssertionError('No Hensel lift')
    return r

def modq(x):
    f=Fraction(x)
    return (f.numerator*pow(f.denominator,-1,M))%M

def jac(P):
    return (P[0]%M,P[1]%M,1)

def double(P):
    if P is None:return None
    x,y,z=P
    if y%M==0:return None
    Y2=y*y%M
    S=(4*x*Y2)%M
    V=(3*x*x+A*pow(z,4,M))%M
    xx=(V*V-2*S)%M
    yy=(V*(S-xx)-8*Y2*Y2)%M
    zz=(2*y*z)%M
    return xx,yy,zz

def add(P,Q):
    if P is None:return Q
    if Q is None:return P
    x1,y1,z1=P;x2,y2,z2=Q
    z12=z1*z1%M;z22=z2*z2%M
    U1=x1*z22%M;U2=x2*z12%M
    S1=y1*z22*z2%M;S2=y2*z12*z1%M
    H=(U2-U1)%M; R=(S2-S1)%M
    if H==0:
        return double(P) if R==0 else None
    H2=H*H%M;H3=H*H2%M
    xx=(R*R-H3-2*U1*H2)%M
    yy=(R*(U1*H2-xx)-S1*H3)%M
    zz=(H*z1*z2)%M
    return (xx,yy,zz)

def times(n,P):
    Q=None
    while n:
        if n&1:Q=add(Q,P)
        P=double(P)
        n//=2
    return Q

points={
 'P1': lambda w: (15,40),
 'P2': lambda w: (19,4),
 'P3': lambda w: (23,16),
 'P4': lambda w: (31,88),
 'R': lambda w: (modq(Fraction(-3355,63)),modq(Fraction(128780,1323))*w%M),
 'H': lambda w: ((modq(Fraction(37,2))+modq(Fraction(3,2))*w)%M,(-16+12*w)%M)
}
expected={
 'P1': (7462,7462),'P2':(14432,14432),'P3':(1427,1427),
 'P4':(7989,7989),'R':(8215,6426),'H':(1495,7921)
}
result={name:[] for name in points}
for w in (root(), -root()%M):
    for name,getP in points.items():
        x,y=getP(w);x%=M;y%=M
        assert (y*y-x*x*x-A*x-B)%M==0
        X,Y,Z=times(18,jac((x,y)))
        numerator=(-X*Z)%M
        vy=0
        while Y%p==0 and Y!=0:
            Y//=p
            vy+=1
        assert Y%p!=0 and vy<15, (name,vy)
        assert numerator%(p**vy)==0
        t=((numerator//(p**vy))*pow(Y,-1,p**5))%(p**5)
        assert t%p==0, (name,vy,t)
        value=(t//p*pow(18,-1,L))%L
        result[name].append(value)
assert all(tuple(result[name])==expected[name] for name in result)
print('INDEPENDENT MODULAR JACOBIAN CHECK PASSED')
for name,pair in result.items():print(name,*pair)
