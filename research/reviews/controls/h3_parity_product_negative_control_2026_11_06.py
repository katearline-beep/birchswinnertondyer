"""Exact formal Taylor negative control: sign +1 and twist sign -1 do not force third base-change derivative zero."""
from fractions import Fraction
from math import factorial

def derivative_product_at_zero(f, g, n):
    return factorial(n)*sum(f.get(i, Fraction(0))*g.get(n-i, Fraction(0)) for i in range(n+1))

def main():
    # F represents L(E,1+t), G represents L(E^D,1+t). Their parity is formal.
    # Nonzero F(t)=t^2+a*t^4 has even parity and analytic order two.
    # Nonzero G(t)=t+b*t^3 has odd parity and analytic order one.
    for a in (-3,0,2):
        for b in (-2,0,5):
            f={2:Fraction(1),4:Fraction(a)}
            g={1:Fraction(1),3:Fraction(b)}
            assert derivative_product_at_zero(f,g,3)==6
            assert derivative_product_at_zero(f,g,3)==3*(2)*(1)
    # A genuinely order-four even F gives zero third derivative of product.
    assert derivative_product_at_zero({4:Fraction(1)},{1:Fraction(1)},3)==0
    # Deliberately invalid shortcut must be rejected.
    shortcut_claim = derivative_product_at_zero({2:Fraction(1)},{1:Fraction(1)},3)==0
    assert not shortcut_claim
    print('PASS: 9 rank-two parity controls have nonzero third derivative = 6; rank-four control zero; invalid shortcut rejected')

if __name__=='__main__':main()
