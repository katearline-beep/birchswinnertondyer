#!/usr/bin/env python3
"""Conditional GLOBAL anticyclotomic self-heights modulo 11^2 for E=234446.a1.

Uses BCLMN Proposition 2.4 and canonical Mazur--Tate sigma:
sigma(t)/t = 1+t/2+c*t^2/2+O(t^3), c=4 mod 11 determined by
canonical_sigma_integrality_11.py. Exact affine points over Q(sqrt(-7)).
Candidate division-polynomial denominators from Session 14 are certified
PRIMITIVE at the full [36]Q point by gcd of integral norms.
Six independent-input polarizations and intentionally bad c=0 control.
NO original complex BSD implication; independent Sage/Magma audit missing.
"""
from fractions import Fraction as F
from math import isqrt,lcm,gcd
from pathlib import Path
import contextlib,importlib.util,io,sys
sys.set_int_max_str_digits(100000)
source=Path(__file__).with_name("provisional_height_mod11.py")
spec=importlib.util.spec_from_file_location("_session14_heights",source)
m=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(m)
K=m.K
p=11;N=p**3;M=m.M

def fsqrt(z):
    if z<0:return None
    a,b=isqrt(z.numerator),isqrt(z.denominator)
    return F(a,b) if a*a==z.numerator and b*b==z.denominator else None

def sqrtK_up_to_unit(z):
    for sign in (1,-1):
        zz=z*sign;s=fsqrt(m.norm(zz))
        if s is None:continue
        for sn in (s,-s):
            aa=fsqrt((zz.a+sn)/2)
            if aa:
                v=K(aa,zz.b/(2*aa))
                if v*v==zz:return v
        if zz.b==0 and zz.a<=0:
            bb=fsqrt(-zz.a/F(7))
            if bb is not None:return K(0,bb)
    raise AssertionError("not square up to a unit")

def initial_d(Q):
    x,y=m.mincoord(Q)
    u,v=x.a-x.b,2*x.b
    D=lcm(u.denominator,v.denominator)
    G=m.gcd(x*D,K(D))
    d=sqrtK_up_to_unit(K(D)/G)
    m.cert(Q,d)
    return d

def big_d(Q):
    doubled=m.add(Q,Q)
    g=initial_d(Q)
    candidates=[]
    for factor in (1,2,4,8,16):
        d=(Q[1]/4)*g*g*g*g/factor
        try:m.cert(doubled,d)
        except AssertionError:continue
        candidates.append((factor,d))
    assert len(candidates)==1,"bad component correction not unique"
    return m.division(doubled,candidates[0][1],18)*candidates[0][1]

def punit(z,w):
    # z is an 11-adic unit at both embeddings.
    def rat(f):
        assert f.denominator%p
        return f.numerator*pow(f.denominator,-1,M)%M
    return (rat(z.a)+w*rat(z.b))%M

def height(Q,d,c=4):
    # BCLMN sigma + global ideal contribution, precision 11^2.
    T=m.scale(36,Q)
    x,y=m.mincoord(T)
    X=x*d*d;Y=y*d*d*d
    assert m.integer(X) and m.integer(Y)
    assert gcd(int(m.norm(X)),int(m.norm(d)))==1
    t=-x/y;u=t/d
    units=[]
    for root in (m.wroot(),(-m.wroot())%M):
        tv=punit(t,root);uv=punit(u,root)
        assert tv%p==0 and uv%p!=0
        units.append(uv*(1+tv*pow(2,-1,M)+c*pow(2,-1,M)*tv*tv)%M)
    q=units[0]*pow(units[1],-1,N)%N
    z=(pow(q,10,N)-1)%N
    assert z%11==0
    logdiv=((z-z*z*pow(2,-1,N))%N)//11
    h36=logdiv*pow(10,-1,p*p)%(p*p)
    return h36*pow(36*36,-1,p*p)%(p*p),q

P=m.points;R=m.R
heights=[];ratios=[]
for i,Pi in enumerate(P):
    Q=m.add(Pi,R)
    h,q=height(Q,big_d(Q))
    assert h%11==m.expected_height[i]
    heights.append(h);ratios.append(q)
    print("P%d+R: h mod121=%d, q mod1331=%d"%(i+1,h,q),flush=True)
assert heights==[100,90,7,8]
assert ratios==[1147,925,675,236]

# The deliberately incorrect c=0 preserves the first digit but not the second.
wrong=[]
for Pi in P:
    Q=m.add(Pi,R)
    wrong.append(height(Q,big_d(Q),c=0)[0])
assert wrong!=heights
assert [v%p for v in wrong]==[v%p for v in heights]

expected={(0,1):(69,168),(0,2):(107,914),(0,3):(108,499),
          (1,2):(97,136),(1,3):(98,16),(2,3):(15,911)}
for (i,j),(wanted,wantedq) in expected.items():
    Q=m.add(m.add(P[i],P[j]),R)
    h,q=height(Q,big_d(Q))
    assert (h,q)==(wanted,wantedq),(i,j,h,q)
    assert h==(heights[i]+heights[j])%121
    print("P%d+P%d+R: h mod121=%d, six-pair identity PASS"%(i+1,j+1,h),flush=True)
radical=[v*pow(heights[0],-1,121)%121 for v in heights]
assert radical==[1,13,40,63]
assert [r%11 for r in radical]==[1,2,7,8]
print("PASS ten exact primitive global denominator ideals, all six mixed polarizations")
print("PASS incorrect canonical coefficient c=0 modifies second but not first digits")
print("height vector mod121",heights,"positive radical ratios",radical)
print("NONCLAIM: BCLMN global normalization, Mazur--Tate integrality theorem,")
print("NONCLAIM: no independent third-party height package, higher derived height, original complex Lpp or BSD proof")
