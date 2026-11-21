#!/usr/bin/env python3
"""Actual p=11 local division witnesses for TWO fine MW test points.

Exact rational curve arithmetic -> 11-adic formal inversion -> independent
11-division-polynomial check modulo 11^4. This is finite local arithmetic,
NOT an evaluated global secondary Bockstein, local cochain or BSD result.
"""
from fractions import Fraction as F
from functools import lru_cache

P=11
N=4
MOD=P**N
A=-1267
B=17230
POINTS=((F(15),F(40)),(F(19),F(4)),(F(23),F(16)),(F(31),F(88)))


def ec_add(Pt,Qt):
    if Pt is None:return Qt
    if Qt is None:return Pt
    x,y=Pt;z,w=Qt
    if x==z and y==-w:return None
    slope=((3*x*x+A)/(2*y) if Pt==Qt else (w-y)/(z-x))
    xx=slope*slope-x-z
    return xx,slope*(x-xx)-y


def ec_mul(n,Pt):
    if n<0:return ec_mul(-n,(Pt[0],-Pt[1]))
    out=None
    while n:
        if n&1:out=ec_add(out,Pt)
        Pt=ec_add(Pt,Pt)
        n>>=1
    return out


def reduce_point(Pt):
    assert Pt is not None
    out=[]
    for v in Pt:
        assert v.denominator%P!=0,"non-integral at 11"
        out.append(v.numerator*pow(v.denominator,-1,MOD)%MOD)
    return tuple(out)


def on_curve(xy):
    x,y=xy
    return (y*y-x*x*x-A*x-B)%MOD==0


def jac_double(U):
    if U is None:return None
    x,y,z=U
    if y%MOD==0:return None
    aa=x*x%MOD
    bb=y*y%MOD
    cc=bb*bb%MOD
    d=2*((x+bb)**2-aa-cc)%MOD
    e=(3*aa+A*pow(z,4,MOD))%MOD
    return ((e*e-2*d)%MOD,
            (e*(d-(e*e-2*d))-8*cc)%MOD,
            2*y*z%MOD)


def jac_add(U,V):
    if U is None:return V
    if V is None:return U
    x,y,z=U
    a,b,c=V
    z2=z*z%MOD
    c2=c*c%MOD
    u1=x*c2%MOD
    u2=a*z2%MOD
    s1=y*c*c2%MOD
    s2=b*z*z2%MOD
    h=(u2-u1)%MOD
    r=(s2-s1)%MOD
    if h==0:
        return jac_double(U) if r==0 else None
    hh=h*h%MOD
    hhh=h*hh%MOD
    uhh=u1*hh%MOD
    xx=(r*r-hhh-2*uhh)%MOD
    yy=(r*(uhh-xx)-s1*hhh)%MOD
    return xx,yy,h*z*c%MOD


def jac_mul(n,U):
    out=None
    while n:
        if n&1:out=jac_add(out,U)
        U=jac_double(U)
        n>>=1
    return out


def formal_parameter(U):
    assert U is not None
    x,y,z=U
    assert z%P==0 and y%P!=0, "expected primitive formal Jacobian point"
    return (-x*z*pow(y,-1,MOD))%MOD


def formal_translate(xy,t):
    """Add formal point of logarithm t, through degree 3 modulo 11^4.

    For short Weierstrass y²=x³+Ax+B, log_E(t)=t+O(t^5),
    and t is divisible by 11, so degree >=4 terms vanish mod 11^4.
    """
    assert t%P==0
    x,y=xy
    xx=(x+2*y*t+(3*x*x+A)*t*t+4*x*y*t**3)%MOD
    yy=(y+(3*x*x+A)*t+6*x*y*t*t+
        (10*x*x*x+6*A*x+4*B)*t**3)%MOD
    return xx,yy


def division_poly_mul(xy,n):
    """Independent division-polynomial formula: [n](x,y) mod 11^4."""
    x,y=xy
    two_y=2*y%MOD
    assert two_y%P!=0
    @lru_cache(None)
    def psi(k):
        if k==0:return 0
        if k==1:return 1
        if k==2:return two_y
        if k==3:return (3*x**4+6*A*x*x+12*B*x-A*A)%MOD
        if k==4:return (4*y*(x**6+5*A*x**4+20*B*x**3
                               -5*A*A*x*x-4*A*B*x-8*B*B-A**3))%MOD
        if k%2:
            m=(k-1)//2
            return (psi(m+2)*pow(psi(m),3,MOD)
                    -psi(m-1)*pow(psi(m+1),3,MOD))%MOD
        m=k//2
        return (psi(m)*pow(two_y,-1,MOD)
                *(psi(m+2)*pow(psi(m-1),2,MOD)
                  -psi(m-2)*pow(psi(m+1),2,MOD)))%MOD

    dn=psi(n)
    assert dn%P!=0,"division polynomial not unit"
    phi=(x*dn*dn-psi(n+1)*psi(n-1))%MOD
    omega=((psi(n+2)*pow(psi(n-1),2,MOD)
             -psi(n-2)*pow(psi(n+1),2,MOD))
           *pow(4*y,-1,MOD))%MOD
    return phi*pow(dn,-2,MOD)%MOD,omega*pow(dn,-3,MOD)%MOD


def build_classes():
    p1,p2,p3,p4=POINTS
    z1=ec_add(ec_add(ec_mul(-2,p1),ec_mul(3,p2)),p3)
    z2=ec_add(ec_add(ec_mul(-9,p1),ec_mul(6,p2)),p4)
    return z1,z2


def arithmetic():
    count=1+sum((y*y-x*x*x-A*x-B)%P==0
                for x in range(P) for y in range(P))
    assert count==18 and count%P!=0

    z1,z2=build_classes()
    actual=[]
    for label,Z,expectedZ,expectedQ,expectedT,expectedU in (
        ("Z1",z1,(1963,11547),(3612,6189),14520,1320),
        ("Z2",z2,(12587,6055),(13874,12447),12584,1144),
    ):
        z=reduce_point(Z)
        assert z==expectedZ and on_curve(z)
        # 18 kills E(F11). The residual local Kummer obstruction
        # is exactly t([18]Z)/11 mod11. Its zero is certified.
        formal18=jac_mul(18,(*z,1))
        t18=formal_parameter(formal18)
        assert t18==expectedT and t18%(P*P)==0
        # Because log(t)=t+O(t^5) for this short Weierstrass model,
        # there is a unique U in E1(Q11) with [11]U=[18]Z,
        # and its t parameter mod 11^3 is t18/11.
        tU=(t18//P)%(P**3)
        assert tU==expectedU and tU%P==0

        # [11]([5]Z - [3]U)=[55]Z-[54]Z=Z.
        # Translate the EXACT rational [5]Z by formal -3U to
        # construct a local 11-division point modulo 11^4.
        q=formal_translate(reduce_point(ec_mul(5,Z)),(-3*tU)%MOD)
        assert q==expectedQ and on_curve(q)
        # Independent verification, not using Jacobian or the
        # formal-addition routine: classical division polynomials.
        assert division_poly_mul(q,11)==z
        assert division_poly_mul(q,2)!=z

        # Meaningful negative control: translate the division point
        # by a nonzero formal group element of log 11; remains ON
        # THE CURVE but no longer divides the target.
        mutant=formal_translate(q,11)
        assert on_curve(mutant) and division_poly_mul(mutant,11)!=z
        actual.append((label,z,q,t18,tU))

    assert actual[0][2]!=actual[1][2]
    assert division_poly_mul(actual[0][2],11)!=actual[1][1]
    assert division_poly_mul(actual[1][2],11)!=actual[0][1]
    return actual


def main():
    entries=arithmetic()
    for label,z,q,t18,tU in entries:
        print(f"{label} Z mod 14641={z}; local Q mod 14641={q}; "
              f"t([18]Z)={t18}; t(U) mod 1331={tU}")
    print("PASS: exact rational MW combinations, #E(F11)=18 and local 11-divisibility")
    print("PASS: formal 11-division construction and orthogonal division-polynomial [11] check")
    print("PASS: on-curve nondivision mutants and swapped-target controls")
    print("NONCLAIM: finite-precision local division ≠ global c1, PT compact-support pairing or BSD")


if __name__=="__main__":
    main()
