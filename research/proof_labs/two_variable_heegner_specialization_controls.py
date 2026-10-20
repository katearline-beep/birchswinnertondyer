#!/usr/bin/env python3
"""Exact algebraic negative controls for two-variable Heegner specializations.

TOY MODELS ONLY, NOT ACTUAL HEegner/Kato classes. Coefficients F_11;
W=Hida weight parameter, T=anticyclotomic augmentation parameter.
Full nonzero over F_11[[W,T]] does NOT establish weight-2 or base nonzero.
A control map and both Coleman orders are separate information.
"""
P=11
MAX=5

def poly(**terms):
    # names w<weight_exponent>_<anticyclotomic_exponent>
    out={}
    for k,a in terms.items():
        x,y=map(int,k.replace('w','').split('_'))
        assert x>=0 and y>=0 and x+y<MAX
        if a%P:out[x,y]=a%P
    return out

def special(f,variable):
    assert variable in ('W','T')
    index=0 if variable=='W' else 1
    return {mon:a for mon,a in f.items() if mon[index]==0}

def ord_ideal(f):
    return min((sum(mon) for mon,a in f.items() if a%P),default=None)

def coeff(f,w,t):return f.get((w,t),0)

def jets(f):return coeff(f,0,0),coeff(f,1,0),coeff(f,0,1)

def add(*fs):
    out={}
    for f in fs:
        for k,a in f.items():
            out[k]=(out.get(k,0)+a)%P
    return {k:a for k,a in out.items() if a}

def times(f,other):
    out={}
    for (a,b),v in f.items():
        for (c,d),u in other.items():
            if a+b+c+d<MAX:
                k=(a+c,b+d)
                out[k]=(out.get(k,0)+v*u)%P
    return {k:a for k,a in out.items() if a}

one=poly(w0_0=1)
W=poly(w1_0=1)
T=poly(w0_1=1)
TW=times(T,W)
T2=times(T,T)
assert ord_ideal(one)==0 and ord_ideal(W)==ord_ideal(T)==1
assert ord_ideal(T2)==ord_ideal(TW)==2

examples={
    'weight_only':W,
    'anticyclotomic_linear':T,
    'anticyclotomic_quadratic':T2,
    'mixed_first':add(W,T),
    'mixed_second':TW,
}
assert all(jets(f)[0]==0 and f for f in examples.values())
assert special(W,'W')=={}  # big nonzero but whole weight-2 fibre ZERO
assert special(T,'W')==T
assert special(T2,'W')==T2
assert special(add(W,T),'W')==T
assert special(TW,'W')=={}
assert jets(W)==(0,1,0) and jets(T)==(0,0,1)
assert jets(T2)==(0,0,0) and ord_ideal(T2)==2
assert ord_ideal(add(W,T2))==1
assert ord_ideal(special(add(W,T2),'W'))==2

# Without INJECTIVE cohomological control from M/(W,T)M to base H^1,
# a torsion classical Kummer base class does not imply 2-variable ideal
# divisibility. Toy M=Ae1(+)Ae2, base observation projects to first slot.
zero_base_not_in_max_ideal=({},one)
assert coeff(zero_base_not_in_max_ideal[0],0,0)==0
assert coeff(zero_base_not_in_max_ideal[1],0,0)==1

# Even after T divisibility, a derivative is NOT unique if T-torsion
# survives: M=Ae (+) (A/(T))f. Both e and e+f divide z=T*e.
def action_T(module_element):
    u,v=module_element
    assert all(k[1]==0 for k in v)
    return times(T,u),{}
e=(one,{})
f=({},one)
e_plus_f=(one,one)
assert action_T(e)==action_T(e_plus_f)==(T,{})
assert jets(e[1]) != jets(e_plus_f[1])
assert action_T(f)==({},{})

# The two local Coleman maps require INDEPENDENT augmentation tests.
# These are toy linear maps, NOT the actual Coleman regulators.
class_vector=(add(W,T),T2)
col_p=class_vector[0]
col_pbar=class_vector[1]
assert ord_ideal(col_p)==1 and ord_ideal(col_pbar)==2
assert ord_ideal(special(col_p,'W'))==1
assert ord_ideal(special(col_pbar,'W'))==2
# A nonzero cohomology class may be annihilated by both local maps.
nonzero_vector=({},one)
col_p_on_vector=nonzero_vector[0]
col_pbar_on_vector=times(W,nonzero_vector[0])
assert nonzero_vector[1] and col_p_on_vector==col_pbar_on_vector=={}

print('PASS toy F11[W,T] / (W,T)^5: base-zero examples have distinct leading directions')
for name,f in examples.items():
    print('EXAMPLE',name,'big order',ord_ideal(f),
          'weight2 order',ord_ideal(special(f,'W')),'jets',jets(f))
print('PASS big nonzero DOES NOT force weight2 or base-field nonzero')
print('PASS base cohomology zero without injective control DOES NOT prove ideal divisibility')
print('PASS T torsion creates distinct divided Bockstein representatives')
print('PASS two local Coleman outputs can have distinct orders, or both be zero')
print('NONCLAIM: no actual Howard class, two-variable Taylor coefficient, Coleman or complex L result')
