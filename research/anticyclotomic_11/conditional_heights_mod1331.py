#!/usr/bin/env python3
"""Provisional anticyclotomic heights modulo 11^3 on ten exact E(K) points.

The canonical sigma parameter c_11=26 mod121 is derived separately by
canonical_sigma_integrality_121.py. This script extends BCLMN height
calculations by one digit and rechecks all ten primitive denominator ideals
and all six genuinely mixed inputs. Conditional on published Mazur--Tate and
BCLMN mathematics; no third-party Sage/Magma height audit or BSD theorem.
"""
from pathlib import Path
import contextlib,importlib.util,io,math

source=Path(__file__).with_name("conditional_heights_mod121.py")
spec=importlib.util.spec_from_file_location("_s16_heights",source)
s=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(s)
m=s.m;P=m.points;R=m.R
p=11;N=p**4;M=m.M

def height(Q,d,c=26):
    T=m.scale(36,Q)
    x,y=m.mincoord(T)
    X=x*d*d;Y=y*d*d*d
    assert m.integer(X) and m.integer(Y)
    assert math.gcd(int(m.norm(X)),int(m.norm(d)))==1
    t=-x/y;u=t/d
    units=[]
    for root in (m.wroot(),(-m.wroot())%M):
        tv=s.punit(t,root);uv=s.punit(u,root)
        assert tv%p==0 and uv%p
        # sigma(t)/t = 1+t/2+c*t^2/2+(3c-1)*t^3/4+O(t^4).
        units.append(uv*(1+tv*pow(2,-1,M)
                        +c*pow(2,-1,M)*tv*tv
                        +(3*c-1)*pow(4,-1,M)*tv*tv*tv)%M)
    q=units[0]*pow(units[1],-1,N)%N
    z=(pow(q,10,N)-1)%N
    assert z%p==0
    logdiv=((z-z*z*pow(2,-1,N)+z*z*z*pow(3,-1,N))%N)//p
    h36=logdiv*pow(10,-1,p**3)%(p**3)
    return h36*pow(36*36,-1,p**3)%(p**3),q

singles=[];qs=[]
for i,Pi in enumerate(P):
    Q=m.add(Pi,R)
    value,q=height(Q,s.big_d(Q))
    assert value%121==[100,90,7,8][i]
    singles.append(value);qs.append(q)
    print("A%d: h mod1331=%d, q mod14641=%d"%(i+1,value,q),flush=True)
assert singles==[1068,1300,854,8],singles
assert qs==[13126,3587,13985,9553],qs

# A deliberately stale sigma value (c=4) leaves first two digits intact
# but must alter at least one third digit.
wrong=[]
for Pi in P:
    Q=m.add(Pi,R)
    wrong.append(height(Q,s.big_d(Q),c=4)[0])
assert wrong!=singles
assert [v%121 for v in wrong]==[v%121 for v in singles]

expected={(0,1):(1037,12147),(0,2):(591,12893),(0,3):(1076,7154),
          (1,2):(823,4129),(1,3):(1308,6671),(2,3):(862,14221)}
for (i,j),(want,wantq) in expected.items():
    Q=m.add(m.add(P[i],P[j]),R)
    value,q=height(Q,s.big_d(Q))
    assert (value,q)==(want,wantq),(i,j,value,q)
    assert value==(singles[i]+singles[j])%1331
    print("A%d%d: h mod1331=%d, mixed bilinearity PASS"%(i+1,j+1,value),flush=True)

global_profile=[value*pow(singles[0],-1,1331)%1331 for value in singles]
local_logs=[7462,14432,1427,7989]
local_profile=[value*pow(local_logs[0],-1,1331)%1331 for value in local_logs]
assert global_profile==[1,739,766,668]
assert [r%121 for r in global_profile]==[1,13,40,63]
assert local_profile==[1,704,772,856]
assert [r%11 for r in global_profile]!=[r%11 for r in local_profile]
print("PASS ten primitive ideals and six mixed height identities modulo 1331")
print("PASS c=4 stale sigma changes only third digits")
print("conditional global profile",global_profile,"local-log profile",local_profile)
print("NONCLAIM: two different Q11 functionals, no proven derived p-adic pairing")
print("NONCLAIM: no original complex L'' zero, Sha finiteness, BSD or human peer review")
