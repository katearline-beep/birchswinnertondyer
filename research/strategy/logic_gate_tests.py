#!/usr/bin/env python3
"""Logic nonimplication test for BKS derived Kato order vs complex analytic rank.

Finite polynomial model ONLY. These are NOT Euler system classes or genuine L
functions, just an explicit countermodel to a purported logical inference
without any comparison map.
"""
from math import factorial

def order(poly):
    return next((i for i,c in enumerate(poly) if c),None)

def derivative(poly,k):
    return factorial(k)*poly[k] if k<len(poly) else 0

# I=(u); "derived norm is in I^3" is a statement in Z_11[u].
derived_norm=[0,0,0,1,7]
assert order(derived_norm)==3
assert all(c==0 for c in derived_norm[:3])

# Unrelated real-complex Taylor germs of the uncompleted L(s) at s=1.
# Both could be paired with exactly the SAME u^3 class unless an
# additional reciprocity comparison constrains the pair.
complex_order2=[0,0,1,0,3]
complex_order4=[0,0,0,0,1]
assert derivative(complex_order2,2)==2
assert derivative(complex_order4,2)==0
assert derivative(complex_order4,4)==24

# Stronger arbitrary augmentation divisibility still does not bridge.
for r in [3,4,7,11]:
    higher_class=[0]*r+[1]
    assert order(higher_class)==r
    assert derivative(complex_order2,2)!=0

# Negative control: if a purported certificate tests the wrong I^3
# containment, it must reject u^2.
bad_class=[0,0,1,0]
assert order(bad_class)==2
assert not all(c==0 for c in bad_class[:3])

print("PASS: I^3 Kato-like containment is compatible with both t^2 and t^4 complex germs")
print("PASS: arbitrary I^r divisibility cannot imply a complex Taylor zero without comparison")
print("PASS: incorrect I^2 class fails the I^3 containment test")
print("NONCLAIM: toy polynomials are not zeta elements or elliptic L-functions")
