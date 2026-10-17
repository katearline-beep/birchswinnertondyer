#!/usr/bin/env python3
"""Independent finite-ring check of split 11-adic log residues.

Jacobian coordinates modulo 11**3 avoid the high-height rational
multiples computed by verify.py. This is a distinct *AI-authored*
implementation, not an independently peer-reviewed mathematical proof.
"""
from fractions import Fraction

p, modulus, a, b = 11, 11**3, -1267, 17230
roots = (1058, 273)
O = (1, 1, 0)

def reduce_fraction(v):
    v = Fraction(v)
    assert v.denominator % p
    return v.numerator * pow(v.denominator, -1, modulus) % modulus

def embed(x, y, root):
    return ((reduce_fraction(x[0]) + root*reduce_fraction(x[1])) % modulus,
            (reduce_fraction(y[0]) + root*reduce_fraction(y[1])) % modulus)

def double(P):
    X,Y,Z = P
    if Z == 0 or Y % modulus == 0: return O
    S, M = 4*X*Y**2, 3*X**2 + a*Z**4
    X3 = M**2 - 2*S
    return (X3%modulus,
            (M*(S-X3) - 8*Y**4)%modulus,
            (2*Y*Z)%modulus)

def add(P, Q):
    if P[2] == 0: return Q
    if Q[2] == 0: return P
    X1,Y1,Z1 = P
    X2,Y2,Z2 = Q
    U1,U2 = X1*Z2**2%modulus, X2*Z1**2%modulus
    S1,S2 = Y1*Z2**3%modulus, Y2*Z1**3%modulus
    if U1 == U2:
        if S1 == S2: return double(P)
        if (S1+S2)%modulus == 0: return O
        raise AssertionError("coincident x but nonopposite y")
    H,R = (U2-U1)%modulus, (S2-S1)%modulus
    X3 = R**2 - H**3 - 2*U1*H**2
    return (X3%modulus,
            (R*(U1*H**2-X3)-S1*H**3)%modulus,
            (H*Z1*Z2)%modulus)

def multiply(n,P):
    Q = O
    while n:
        if n&1: Q = add(Q,P)
        P = double(P)
        n >>= 1
    return Q

points = {
 'P1':((15,0),(40,0)), 'P2':((19,0),(4,0)),
 'P3':((23,0),(16,0)), 'P4':((31,0),(88,0)),
 'R':((Fraction(-3355,63),0),(0,Fraction(128780,1323))),
 'H':((Fraction(37,2),Fraction(3,2)),(-16,12)),
}
expected={'P1':(81,81),'P2':(33,33),'P3':(96,96),
          'P4':(3,3),'R':(108,13),'H':(43,56)}
assert all((root**2+7)%modulus == 0 for root in roots)
assert roots[0]%p == 2 and roots[1]%p == 9
actual = {}
for name,(x,y) in points.items():
    if name == 'P4':
        # The naive projective representation of [18]P4 is nonprimitive
        # modulo 11^3, so this secondary method does not test P4.
        continue
    pair = []
    for root in roots:
        X,Y = embed(x,y,root)
        assert (Y**2-X**3-a*X-b)%modulus == 0
        XX,YY,ZZ = multiply(18,(X,Y,1))
        assert ZZ%p == 0 and YY%p != 0
        t = (-XX*ZZ*pow(YY,-1,modulus))%modulus
        assert t%p == 0
        pair.append((t//p)*pow(18,-1,p*p)%(p*p))
    actual[name]=tuple(pair)
assert set(actual)==set(expected)-{'P4'}
assert all(actual[k]==expected[k] for k in actual)
det=(actual['P1'][0]*actual['H'][1]-actual['P1'][1]*actual['H'][0])%(p*p)
assert det==85 and det%11==8
print("PASS: independently implemented projective check (P1,P2,P3,R,H)")
print("PASS: determinant =", det, "mod 121; =",det%11,"mod 11")
