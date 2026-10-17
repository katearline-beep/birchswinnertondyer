#!/usr/bin/env python3
"""C-0002: normalized split-11 local-log kernel mod 11**4.

Exact rational elliptic arithmetic and a distinct modular-projective check.
Formal-group interpretation depends on the documented good-reduction and
truncation argument; NOT an anticyclotomic height or a BSD theorem.
"""
from pathlib import Path
from importlib.util import spec_from_file_location, module_from_spec

def load_sibling(module_name):
    path = Path(__file__).resolve().with_name(module_name + ".py")
    spec = spec_from_file_location(module_name, path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

exact = load_sibling("verify")
modular = load_sibling("independent_check")

p=11
precision=4
M=p**precision
N=p**(precision+1)
exact.mod=N

# Hensel-lift sqrt(-7), starting with 2 mod 11.
root=2
for exponent in range(1, precision+1):
    q=p**(exponent+1)
    choices=[root+d*p**exponent for d in range(p)
             if ((root+d*p**exponent)**2+7)%q==0]
    assert len(choices)==1
    root=choices[0]
assert root==156785
roots=(root,(-root)%N)
assert roots==(156785,4266)
assert all((w*w+7)%N==0 for w in roots)

logs={}
for name,P in exact.points.items():
    Q=exact.mul(18,P)
    assert Q is not None
    t=-Q[0]/Q[1]
    a,b=exact.red(t.a),exact.red(t.b)
    vals=[]
    for w in roots:
        v=(a+w*b)%N
        assert v%p==0
        vals.append(((v//p)*pow(18,-1,M))%M)
    logs[name]=tuple(vals)

expected={
 'P1':(7462,7462), 'P2':(14432,14432),
 'P3':(1427,1427), 'P4':(7989,7989),
 'R':(8215,6426), 'H':(1495,7921),
}
assert logs==expected,(logs,expected)
assert all(tuple(v%121 for v in logs[k])==exact.logs[k]
           for k in logs)
assert all((2*logs['H'][j]-logs['P3'][j]-logs['P4'][j]
            -logs['R'][j])%M==0 for j in (0,1))

# The P1 coefficient (7462) is a unit. The difference of the two
# local log rows equals 6426 times the coefficient of H, also a unit.
u=pow(logs['P1'][0],-1,M)
coeff={key:(u*logs[key][0])%M for key in ('P2','P3','P4')}
assert coeff=={'P2':8690,'P3':14082,'P4':12835}
assert logs['P1'][0]%p==4
assert (logs['H'][1]-logs['H'][0])%p==2
for key,c in coeff.items():
    assert all((logs[key][j]-c*logs['P1'][j])%M==0
               for j in (0,1))
minor=(logs['P1'][0]*logs['H'][1]-logs['P1'][1]*logs['H'][0])%M
assert minor==1537 and minor%p==8

# Distinct algorithm: Jacobian projective operations over Z/(11**5).
# On this coordinate implementation P4 becomes nonprimitive, so the
# second computation explicitly covers only P1,P2,P3,R,H.
modular.modulus=N
modular.roots=roots
checked={}
for key in ('P1','P2','P3','R','H'):
    coords=modular.points[key]
    values=[]
    for w in roots:
        x,y=modular.embed(*coords,w)
        assert (y*y-x*x*x-modular.a*x-modular.b)%N==0
        X,Y,Z=modular.multiply(18,(x,y,1))
        assert Z%p==0 and Y%p!=0
        v=(-X*Z*pow(Y,-1,N))%N
        assert v%p==0
        values.append(((v//p)*pow(18,-1,M))%M)
    checked[key]=tuple(values)
assert checked=={key:expected[key] for key in checked}

print('PASS C-0002: logs modulo 14641:',logs)
print('PASS: distinct exact and projective algorithms agree (except P4)')
print('PASS: det(P1,H) = 1537 mod 14641, 8 mod 11')
print('PASS: coefficient-kernel basis modulo 14641:')
for key,c in coeff.items(): print('  '+key+' - '+str(c)+' P1')
