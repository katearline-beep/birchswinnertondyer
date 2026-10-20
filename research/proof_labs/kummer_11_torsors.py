#!/usr/bin/env python3
"""Concrete [11]^{-1}(P) torsors on focal E in its short model.

Uses exact FLINT polynomial arithmetic (python-flint==0.9.0), no heights or
repository division-polynomial implementations. NOT evaluated Galois actions,
not Selmer lifts, and not derived-height values.
"""
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import sys
import flint
from flint import fmpz_poly, fmpq_poly, fmpq

A, B, N = -1267, 17230, 11
X = fmpz_poly([0, 1])
CUBIC = X**3 + A*X + B


def division_polynomials():
    # Odd d_n=psi_n; even d_n=psi_n/(2y), with y^2=CUBIC.
    d = {0: fmpz_poly([]), 1: fmpz_poly([1]), 2: fmpz_poly([1]),
         3: 3*X**4 + 6*A*X**2 + 12*B*X - A*A,
         4: 2*(X**6+5*A*X**4+20*B*X**3-5*A*A*X**2
               -4*A*B*X-8*B*B-A**3)}

    def get(n):
        if n not in d:
            m = n//2
            if n % 2:
                u, v = get(m+2)*get(m)**3, get(m-1)*get(m+1)**3
                d[n] = u - 16*CUBIC**2*v if m % 2 else 16*CUBIC**2*u - v
            else:
                d[n] = get(m)*(get(m+2)*get(m-1)**2-get(m-2)*get(m+1)**2)
        return d[n]

    psi = get(N)
    phi = X*psi**2 - 4*CUBIC*get(N+1)*get(N-1)
    assert psi.degree() == 60 and psi.leading_coefficient() == 11
    assert phi.degree() == 121 and phi.leading_coefficient() == 1
    return phi, psi


def digest(poly):
    return sha256(','.join(map(str,poly.coeffs())).encode('ascii')).hexdigest()


def validate_torsor(phi, psi, name, px, py_squared):
    px = Fraction(px)
    assert py_squared == px**3 + A*px + B, 'Input point is not on E'
    F = px.denominator*phi - px.numerator*psi**2
    Fq, psiq = fmpq_poly(F), fmpq_poly(psi)
    assert F.degree() == 121
    assert Fq.gcd(Fq.derivative()).degree() == 0, 'Division fibre is not etale'
    # [11]^*(dx/(2y))=11 dx/(2y), so y([11]Q)=y(Q)*H/(11*psi^3).
    H = fmpq_poly(phi.derivative()*psi - 2*phi*psi.derivative())
    assert Fq.gcd(H).degree() == 0, 'Cannot reconstruct division-point y'
    rhs = fmpq_poly(CUBIC)*H**2
    numerator = N*N*py_squared.numerator*psiq**6
    residual = numerator - py_squared.denominator*rhs
    assert residual % Fq == 0, 'Reconstructed division point is not on E'
    # Obtain an actual polynomial y(Q)/y(P) in Q[x]/F, not only a fraction.
    common, inverse, _ = H.xgcd(Fq)
    assert common == 1 and (H*inverse) % Fq == 1
    y_ratio = (N*psiq**3*inverse) % Fq
    c = fmpq_poly([fmpq(py_squared.numerator, py_squared.denominator)])
    assert (c*y_ratio**2-fmpq_poly(CUBIC)) % Fq == 0
    assert (y_ratio*H-N*psiq**3) % Fq == 0
    print(f'PASS {name}: etale degree121 torsor, reconstructed Q, [11]Q=P; SHA256 {digest(F)}')
    return F


def validate_pari_lines(lines, phi, psi):
    assert len(lines) == 3 and not any('***' in x for x in lines)
    expected = [phi, psi, psi**2]
    for line, label, poly in zip(lines, ['PHI','PSI','DEN'], expected):
        prefix, data = line.split(' ',1)
        assert prefix == label
        oracle = [int(x) for x in data.split(',')]
        assert oracle == [int(x) for x in poly.coeffs()], f'PARI {label} mismatch'


def compare_pari(path, phi, psi):
    lines = Path(path).read_text(encoding='utf8').splitlines()
    validate_pari_lines(lines, phi, psi)
    bad = lines[:]
    coeffs = bad[0].split(' ',1)[1].split(',')
    coeffs[17] = str(int(coeffs[17])+1)
    bad[0] = 'PHI ' + ','.join(coeffs)
    try:
        validate_pari_lines(bad, phi, psi)
    except AssertionError as exc:
        assert str(exc) == 'PARI PHI mismatch'
        print('PASS negative control: changed multiplication coefficient rejected')
    else:
        raise AssertionError('Coefficient mutation escaped')
    print('PASS all PARI ellxn/elldivpol coefficients agree')


def main():
    assert flint.__version__ == '0.9.0', 'Use pinned python-flint==0.9.0'
    phi, psi = division_polynomials()
    for name, px, py in [('P1',15,40),('P2',19,4),('P3',23,16),('P4',31,88)]:
        validate_torsor(phi, psi, name, Fraction(px), Fraction(py*py))
    validate_torsor(phi, psi, 'R', Fraction(-3355,63), -7*Fraction(128780,1323)**2)
    try:
        validate_torsor(phi, psi, 'MUTATED', Fraction(15), Fraction(40*40+1))
    except AssertionError as exc:
        assert str(exc) == 'Input point is not on E'
        print('PASS negative control: changed point y^2 rejected')
    else:
        raise AssertionError('Point mutation escaped')
    # A more structural mutation bypasses point-input validation but must break
    # the group-map y identity on a genuine fibre.
    bad_phi = phi + 1
    try:
        validate_torsor(bad_phi, psi, 'BAD_MAP', Fraction(15), Fraction(40*40))
    except AssertionError as exc:
        assert str(exc) == 'Reconstructed division point is not on E'
        print('PASS negative control: wrong multiplication map fails actual point identity')
    else:
        raise AssertionError('Multiplication mutation escaped')
    if len(sys.argv) == 2:
        compare_pari(sys.argv[1], phi, psi)
    else:
        assert len(sys.argv) == 1
    print('NONCLAIM: explicit torsors define Kummer classes, but no evaluated Galois matrices, Selmer lift or h2')


if __name__ == '__main__':
    main()
