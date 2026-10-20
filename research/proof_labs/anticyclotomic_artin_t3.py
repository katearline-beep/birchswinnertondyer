#!/usr/bin/env python3
"""Actual K=-7 Artin-character arithmetic; NOT E Tate-module cochains.

Class field theory and the ring-class exact sequence are mathematical inputs.
Two compatible layers suffice for the coefficient actions mod11 and mod121
through T^2. Optional PARI output independently tests ideal Artin arithmetic.
"""
from math import gcd
from pathlib import Path
import sys

P = 11


def roots(m):
    """Chosen embedding omega=5 mod11, omega^2-omega+2=0."""
    r, modulus = 5, P
    while modulus < P ** (m + 1):
        lifts = [r + t * modulus for t in range(P)
                 if ((r + t * modulus) ** 2 - (r + t * modulus) + 2)
                 % (modulus * P) == 0]
        assert len(lifts) == 1
        r, modulus = lifts[0], modulus * P
    return r, (1 - r) % modulus


class Artin:
    def __init__(self, m):
        assert m in (1, 2)
        self.m, self.n, self.modulus = m, P ** m, P ** (m + 1)
        self.r, self.s = roots(m)
        # log_{1+11}(ratio^10); powers give an exact finite discrete log.
        self.log = {pow(12, j, self.modulus): j for j in range(self.n)}
        assert len(self.log) == self.n
        assert pow(12, self.n, self.modulus) == 1

    def ratio(self, a, b):
        u, v = (a + self.r * b) % self.modulus, (a + self.s * b) % self.modulus
        if gcd(u * v, P) != 1:
            raise ValueError("Ideal generator must be prime to 11")
        return u * pow(v, -1, self.modulus) % self.modulus

    def of_ratio(self, ratio):
        return self.log[pow(ratio, 10, self.modulus)]

    def __call__(self, a, b):
        return self.of_ratio(self.ratio(a, b))

    def by_log_series(self, ratio):
        """Separate exact logarithm formula at these two precisions."""
        u = pow(ratio, 10, self.modulus)
        z = (u - 1) // P
        if self.m == 1:
            return z % P
        half = pow(2, -1, self.n)
        numerator = (z - P * z * z * half) % self.n
        denominator = (1 - P * half) % self.n
        return numerator * pow(denominator, -1, self.n) % self.n


def multiply(x, y, modulus):
    return tuple(sum(x[j] * y[i - j] for j in range(i + 1)) % modulus
                 for i in range(3))


def action(k, modulus):
    return 1, k % modulus, (k * (k - 1) // 2) % modulus


def norm(a, b):
    return a * a + a * b + 2 * b * b


def conjugate(a, b):
    return a + b, -b


def controls():
    maps = [Artin(1), Artin(2)]
    for A in maps:
        modulus, n = A.modulus, A.n
        assert gcd(A.r - A.s, modulus) == 1
        assert (A.r * A.r - A.r + 2) % modulus == 0
        # 2 generates the entire CRT ratio group: exhaustive, not samples.
        ratios = {pow(2, j, modulus) for j in range(10 * n)}
        assert len(ratios) == 10 * n
        assert ratios == {u for u in range(modulus) if gcd(u, P) == 1}
        for u in sorted(ratios):
            ell = A.of_ratio(u)
            assert ell == A.by_log_series(u)
            assert A.of_ratio(2 * u % modulus) == (A.of_ratio(2) + ell) % n
            assert A.of_ratio(pow(u, -1, modulus)) == -ell % n
            # CRT lift of pair (u,1) to a+b*omega.
            b = (u - 1) * pow(A.r - A.s, -1, modulus) % modulus
            a = (1 - b * A.s) % modulus
            assert A(a, b) == ell
            assert A(*conjugate(a, b)) == -ell % n
            assert A(-a, -b) == ell  # unit ambiguity in principal generator
        assert {A.of_ratio(u) for u in ratios} == set(range(n))
        # Exact quadratic term is essential for the group law.
        for k in range(n):
            for l in range(n):
                assert multiply(action(k, n), action(l, n), n) == action(k + l, n)
        assert multiply(action(1, n), action(1, n), n) != (1, 2, 0)
        assert A(2, 0) == 0  # rational principal ideals are killed
        # Cyclotomic norm character fails anti-invariance already on alpha=2.
        cyclo = A.of_ratio(4)
        assert cyclo != -cyclo % n
        print(f"PASS layer m={A.m}: conductor={modulus}, quotient={n}, "
              f"roots={(A.r, A.s)}, all {10*n} ratios, log and group action")
    for a in range(-7, 8):
        for b in range(-7, 8):
            if norm(a, b) % P:
                assert maps[1](a, b) % P == maps[0](a, b)
    # Finite C11 is faithful mod11 through T^2, but not mod121.
    assert action(11, 11) == (1, 0, 0)
    assert action(11, 121) == (1, 11, 55)
    assert action(121, 121) == (1, 0, 0)
    # Multiplying the C11 relation 11T+55T^2 by T kills 11T^2.
    finite_c11_relation = (0, 11, 55)
    assert multiply(finite_c11_relation, (0, 1, 0), 121) == (0, 0, 11)
    assert (0, 0, 11) != (0, 0, 0)  # nonzero in the TRUE free T3 module
    print("PASS tower reduction; C11 loses integral 11*T^2, C121 retains mod121 T3 action")
    print("PASS negative controls: cyclotomic norm, missing binomial term, shallow finite layer")
    return maps


def validate_pari_lines(lines, maps):
    """Strict typed output; GP errors cannot be ignored by a zero exit code."""
    assert lines and not any("***" in line for line in lines), "GP interpreter error"
    headers, rows, tails = {}, {}, []
    for line in lines:
        parts = line.split()
        assert parts, "Empty oracle row"
        if parts[0] == "LAYER":
            assert len(parts) == 5
            m, degree, conductor, delta = map(int, parts[1:])
            assert m not in headers
            A = maps[m - 1]
            assert degree == A.n and conductor == A.modulus
            assert delta == (-7) ** A.n * P ** sum(2 * (j + 1) * (P**j - P**(j-1)) for j in range(1, m+1))
            headers[m] = degree
        elif parts[0] == "PRIME":
            assert len(parts) == 8
            m, prime, i, f, a, b, ell = map(int, parts[1:])
            A = maps[m - 1]
            assert norm(a, b) == prime ** f
            assert A(a, b) == ell
            key = m, prime, i
            assert key not in rows
            rows[key] = f, ell
        else:
            assert line == "PASS CLASSFIELD degree22 dihedral22 fixed11 discriminant conductor"
            tails.append(line)
    assert set(headers) == {1, 2} and len(tails) == 1
    primes = [n for n in range(2, 501) if all(n % d for d in range(2, int(n**.5)+1)) and n != 11]
    for prime in primes:
        split = prime != 7 and pow(-7 % prime, (prime - 1)//2, prime) == 1
        # At p=2 the Kronecker symbol (-7/2)=+1.
        split = split or prime == 2
        for m in (1, 2):
            expected = 2 if split else 1
            found = [(i, rows[(m, prime, i)]) for i in range(1, expected+1)]
            assert all(f == (1 if split or prime == 7 else 2) for _, (f, _) in found)
            if split:
                assert sum(ell for _, (_, ell) in found) % (P**m) == 0
            else:
                assert found[0][1][1] == 0
    expected_keys = {(m, prime, i) for m in (1, 2) for prime in primes
                     for i in range(1, (2 if prime == 2 or (prime != 7 and
                     pow(-7 % prime, (prime-1)//2, prime) == 1) else 1)+1)}
    assert set(rows) == expected_keys, "Incomplete or surplus prime coverage"
    print(f"PASS PARI: {len(rows)} ideal Artin values, two certified conductors and discriminants")
    return len(rows)


def compare_pari(path, maps):
    lines = Path(path).read_text(encoding="utf8").splitlines()
    validate_pari_lines(lines, maps)
    bad = lines[:]
    index = next(i for i, line in enumerate(bad) if line.startswith("PRIME "))
    fields = bad[index].split()
    m = int(fields[1])
    fields[7] = str((int(fields[7]) + 1) % (P**m))
    bad[index] = " ".join(fields)
    try:
        validate_pari_lines(bad, maps)
    except AssertionError:
        print("PASS negative control: mutated PARI Artin value rejected")
    else:
        raise AssertionError("Artin mutation escaped")


def main():
    maps = controls()
    if len(sys.argv) == 2:
        compare_pari(sys.argv[1], maps)
    else:
        assert len(sys.argv) == 1
    print("NONCLAIM: no elliptic Tate-module cocycle, Selmer lift, height or complex BSD")


if __name__ == "__main__":
    main()
