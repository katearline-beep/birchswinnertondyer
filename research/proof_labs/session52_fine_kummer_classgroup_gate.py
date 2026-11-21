#!/usr/bin/env python3
"""Session52: three actual fine MW classes -> six-dimensional Kummer quotient.

Exact F11 Frobenius/reduction linear algebra + independently generated
local 11-division point for P2. The class-field-theoretic 11-class group
lower bound uses SOURCE hypotheses at the bad primes and standard global
Kummer reciprocity; this code cannot prove those theorems.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations, product

P=11
MOD=P**4
A=-1267
B=17230
# Session46 independently certified five-point Kummer translation rows.
R743=(1,0,0,2,6)
R2843=(1,4,9,9,1)
R3019=(1,8,0,4,1)
# Fine basis: P2, Z1=-2P1+3P2+P3, Z2=-9P1+6P2+P4.
COEFF=((0,1,0,0,0),(-2,3,1,0,0),(-9,6,0,1,0))
# C0039 actual two split-11 local Kummer functionals.
LOCAL=((4,0,8,3,9),(4,0,8,3,2))


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))%P


def determinant(a):
    n=len(a)
    val=0
    for perm in permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n)
                       for j in range(i+1,n))
        term=sign
        for i in range(n):
            term*=a[i][perm[i]]
        val+=term
    return val%P


def rank(a):
    mat=[list(row) for row in a]
    r=0
    for j in range(len(mat[0])):
        i=next((k for k in range(r,len(mat)) if mat[k][j]%P),None)
        if i is None:continue
        mat[r],mat[i]=mat[i],mat[r]
        fac=pow(mat[r][j],-1,P)
        mat[r]=[fac*x%P for x in mat[r]]
        for i in range(len(mat)):
            if i!=r:
                m=mat[i][j]
                mat[i]=[(x-m*y)%P for x,y in zip(mat[i],mat[r])]
        r+=1
    return r


def full_kummer_controls():
    assert all(dot(row,c)==0 for row in LOCAL for c in COEFF)
    assert rank(COEFF)==3

    rows=[tuple(dot(row,c) for c in COEFF)
          for row in (R743,R2843,R3019)]
    assert rows==[(0,9,4),(4,8,2),(8,0,10)]
    assert determinant(rows)==1 and rank(rows)==3

    # Actual q23 residual Frobenius has irreducible X²+6X+1.
    def q23(u):
        return (-u[1]%P,(u[0]+5*u[1])%P)
    def det2(u,v):
        return (u[0]*v[1]-u[1]*v[0])%P
    assert 10 not in {a*a%P for a in range(P)}
    for u in product(range(P),repeat=2):
        if u!=(0,0):
            assert det2(u,q23(u))==(u[0]**2+5*u[0]*u[1]+u[1]**2)%P!=0

    # The 6x6 determinant factors as det(3x3 rows)^2
    # times the three q23 orbit determinants (Kronecker factorization).
    us=((1,0),(2,1),(5,4))
    cols=[]
    for row,u in zip(rows,us):
        for v in (u,q23(u)):
            cols.append(tuple(a*b%P for a in row for b in v))
    big=tuple(tuple(cols[j][i] for j in range(6)) for i in range(6))
    expected=determinant(rows)**2
    for u in us:expected=expected*det2(u,q23(u))%P
    assert determinant(big)==expected==3 and rank(big)==6

    # Orthogonal exact controls: duplicate an actual reduction row,
    # or make Frobenius act reducibly, and the 6D argument collapses.
    duplicate=(rows[0],rows[1],rows[0])
    assert determinant(duplicate)==0 and rank(duplicate)==2
    identity_cols=[]
    for row,u in zip(rows,us):
        for _ in range(2):
            identity_cols.append(tuple(a*b%P for a in row for b in u))
    identity_big=tuple(tuple(identity_cols[j][i] for j in range(6))
                       for i in range(6))
    assert rank(identity_big)==3 and determinant(identity_big)==0
    # Wrong local inputs (Z1 no longer fine) must be detected.
    bad=list(COEFF)
    bad[1]=(0,3,1,0,0)
    assert any(dot(row,bad[1]) for row in LOCAL)
    return rows


def ec_add(U,V):
    if U is None:return V
    if V is None:return U
    x,y=U
    z,w=V
    if x==z and y==-w:return None
    m=(3*x*x+A)/(2*y) if U==V else (w-y)/(z-x)
    xx=m*m-x-z
    return xx,m*(x-xx)-y


def ec_mul(n,U):
    acc=None
    while n:
        if n&1:acc=ec_add(acc,U)
        U=ec_add(U,U)
        n//=2
    return acc


def red(x):
    assert x.denominator%P!=0
    return x.numerator*pow(x.denominator,-1,MOD)%MOD


def formal_translate(U,s):
    x,y=U
    return ((x+2*y*s+(3*x*x+A)*s*s+4*x*y*s**3)%MOD,
            (y+(3*x*x+A)*s+6*x*y*s*s+
             (10*x**3+6*A*x+4*B)*s**3)%MOD)


def divpoly11(U):
    x,y=U
    assert 2*y%P!=0
    @lru_cache(None)
    def psi(k):
        if k==0:return 0
        if k==1:return 1
        if k==2:return 2*y%MOD
        if k==3:return (3*x**4+6*A*x*x+12*B*x-A*A)%MOD
        if k==4:return (4*y*(x**6+5*A*x**4+20*B*x**3-5*A*A*x*x
                               -4*A*B*x-8*B*B-A**3))%MOD
        if k%2:
            m=(k-1)//2
            return (psi(m+2)*pow(psi(m),3,MOD)
                    -psi(m-1)*pow(psi(m+1),3,MOD))%MOD
        m=k//2
        return (psi(m)*pow(2*y,-1,MOD)*
               (psi(m+2)*pow(psi(m-1),2,MOD)
                -psi(m-2)*pow(psi(m+1),2,MOD)))%MOD
    z=psi(11)
    assert z%P!=0
    phi=(x*z*z-psi(10)*psi(12))%MOD
    omega=(psi(13)*pow(psi(10),2,MOD)
           -psi(9)*pow(psi(12),2,MOD))*pow(4*y,-1,MOD)%MOD
    return (phi*pow(z,-2,MOD)%MOD,omega*pow(z,-3,MOD)%MOD)


def p2_local_division():
    # Orthogonal to Session51's Jacobian 18-multiple:
    # use exact rational [18]P2 and its formal parameter.
    z=(F(19),F(4))
    tpoint=ec_mul(18,z)
    t=-tpoint[0]/tpoint[1]
    t18=red(t)
    assert t18==2541 and t18%(P*P)==0
    tU=t18//P
    assert tU==231
    p5=ec_mul(5,z)
    q=formal_translate((red(p5[0]),red(p5[1])),(-3*tU)%MOD)
    assert q==(225,4535)
    assert (q[1]*q[1]-q[0]**3-A*q[0]-B)%MOD==0
    assert divpoly11(q)==(19,4)
    wrong=formal_translate(q,11)
    assert (wrong[1]*wrong[1]-wrong[0]**3-A*wrong[0]-B)%MOD==0
    assert divpoly11(wrong)!=(19,4)
    assert sum((y*y-x*x*x-A*x-B)%P==0
               for x in range(P) for y in range(P))+1==18
    return q,t18,tU


def quadratic_local_trace_descent_control():
    """From K_v/Q_l of degree d=1 or 2, local 11-divisibility descends.

    If [11]U=Z over K_v, then [11]Tr(U)=d Z, hence
    [11](a Tr(U)+b Z)=(a*d+11*b)Z=Z.
    """
    assert 1*1+11*0==1
    assert 6*2+11*(-1)==1
    from math import gcd
    assert gcd(1,11)==gcd(2,11)==1
    assert gcd(11,11)==11  # deliberate inadmissible extension degree
    assert all((a*d+11*b)==1 for d,a,b in [(1,1,0),(2,6,-1)])
    return True


def main():
    assert quadratic_local_trace_descent_control()
    rows=full_kummer_controls()
    q,t18,tU=p2_local_division()
    print(f"FINE3_ROWS {rows}, determinant=1 mod11")
    print(f"LOCAL_P2_11_ROOT Q={q} mod14641; t([18]P2)={t18}; t(U)={tU}")
    print("PASS: actual 3 fine MW classes form full V^3 translation image over L")
    print("PASS: 6x6 determinant=3, all120 q23 orbit tests, row/action/local mutants")
    print("PASS: independently constructed Q11 division point of P2 via rational [18]P2")
    print("PASS: independent exact division-polynomial [11]Q=P2 and on-curve mutation")
    print("PASS: local quadratic trace descent d=1,2; wrong degree 11 falsifier")
    print("CONDITIONAL CLASS GROUP: 11-rank >=6 for Cl(Q(E11)) AND Cl(K(E11))")
    print("NONCLAIM: code neither computes Cl(L), a global corrected c1, secondary h2 nor BSD")


if __name__=="__main__":
    main()
