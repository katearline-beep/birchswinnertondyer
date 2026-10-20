#!/usr/bin/env python3
"""Session25: SOURCE-DEPENDENT exact norm/corestriction and Coleman gates.

Howard Prop2.3.1: cor_(H_(p^(n+1))/H_(p^n)) X_(p^(n+1))
= U_p X_(p^n), INCLUDING c=1 step.
Howard §3.3: Z_s=cor_(H_(p^(t+1))/D_s)(U_p^(-t)X_(p^(t+1))).
Therefore pr_K Z_inf=U_p X_1 (not necessarily X_1).
Castella Thm6.5/Rem6.6: ν2(X_1)=(1-α^-1)^2 κ(P_K).
Kolyvagin rank>=4 -> κ(P_K)=0 over Q11.
Thus pr_K ν2(Z_inf)=0, with no asserted J-divisibility of the
GLOBAL Iwasawa class, positive derivative or BSD statement.

The polynomial local/Coleman maps below are NEGATIVE-CONTROL TOYS, not
actual p-adic heights or computed Coleman outputs.
"""
P=11
M=P**4
A=-6

def hensel_unit_root():
    x=A%P
    mod=P
    for _ in range(1,4):
        roots=[x+j*mod for j in range(P)
               if ((x+j*mod)**2-A*(x+j*mod)+P)%(mod*P)==0]
        assert len(roots)==1
        x=roots[0]
        mod*=P
    return x,mod
alpha,mod=hensel_unit_root()
assert (alpha,mod)==(12721,14641)
assert alpha%11==5 and pow(alpha,-1,mod)*alpha%mod==1
euler=(1-pow(alpha,-1,mod))%mod
assert euler%11==3 and (euler*euler)%11==9

# Norm/corestriction is linear in eigenvalue U. Work modulo 11^4.
# Represent base X_1 by any scalar x, tracing U^(t+1)X_1
# down from H_{11^{t+1}} to K, then renormalize U^{-t}.
for x in (0,1,11,57,126):
    for t in range(7):
        traced=(pow(alpha,t+1,mod)*x)%mod
        normalized=pow(pow(alpha,t,mod),-1,mod)*traced%mod
        assert normalized==alpha*x%mod
        if x and t:
            wrong_renormalization=pow(pow(alpha,t+1,mod),-1,mod)*traced%mod
            assert wrong_renormalization==x%mod
            assert wrong_renormalization!=normalized
# P_K torsion => rationalized Kummer=0: source formula maps base to 0.
kummer_pk=0
weight2_x1=euler*euler*kummer_pk%mod
assert weight2_x1==0
assert alpha*weight2_x1%mod==0

# Abstract power series A=Q11[[T]]: augmentation of any local Coleman
# output is its T^0 coefficient. If a SPECIALIZATION-COMPATIBLE,
# regular Coleman map evaluates the zero base local class, then its
# constant must vanish. This says order >=1, NOT exact order.
def valuation(series):
    return next((i for i,v in enumerate(series) if v),None)
zero_base_profiles=(
    (0,1,0,0),       # exact order 1
    (0,0,1,0),       # exact order 2
    (0,0,0,0),       # identically zero
)
assert all(v[0]==0 for v in zero_base_profiles)
assert [valuation(x) for x in zero_base_profiles]==[1,2,None]
# TWO local Coleman maps can BOTH have constant zero, but unequal
# unknown next orders: no symmetry theorem identifies leading values.
assert valuation(zero_base_profiles[0])!=valuation(zero_base_profiles[1])

# Vanishing BASE projection does not prove global augmentation-ideal
# divisibility without an Iwasawa control isomorphism:
# M=A*e1 ⊕ A*e2, observed pr:M->Q11 records only first constant.
# z=e2 has pr(z)=0 but z not in (T)*M.
z1=(0,1)  # constant of each component
projection=z1[0]
assert projection==0 and z1[1]!=0

# A formal 'Coleman' with a pole (1/T)*(T) would return constant 1:
# establishing regularity / nonexceptional interpolation matters!
T=(0,1,0)
assert T[0]==0 and T[1]==1
pole_times_T_constant=T[1]
assert pole_times_T_constant==1

print("PASS source-level corestriction recursion: pr_K(Z_inf)=U11 X1, t=0..6")
print("PASS weight2 ordinary U11=12721 mod14641 and Euler-square 9 mod11")
print("PASS source-dependent weight2 pr_K(Z_inf)=0 from Castella+Kolyvagin")
print("PASS J^1 of EACH regular specialization-compatible local regulator follows from zero base")
print("PASS neither exact J order nor global J-divisibility follows; false renormalization detected")
print("NONCLAIM: source norm/weight2 identities not independently reproved by toy scalar recursion")
print("NONCLAIM: no computed Coleman coefficients, Bockstein, original complex L'' or BSD")
