#!/usr/bin/env python3
"""Actual local norm certificate: exact formal series, traces and infinite tail.

The local point is t=pi, where pi is a root of the Eisenstein polynomial g.
This supplies a residual LOCAL reference class by Kummer/Shapiro. It is not
an evaluated supported global correction or a second derived height.
"""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import re
import sys

P = 11
F_POLY = [11133855, 14938803, 9160173, 3244989, 711337, 108009,
          11649, 418, -176, -33, 0, 1]  # ascending, C0033
EXPECTED_G = [756406651, 616891275, 214003625, 39930605, 4598605, 725153,
              240185, 60258, 9196, 847, 44, 1]


def need(ok, message):
    if not ok:
        raise ValueError(message)


def rejected(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError('mutation was accepted')


def vp(n):
    n = F(n)
    if not n:
        return 10**9
    a, b = abs(n.numerator), n.denominator
    v = 0
    while a % P == 0:
        a //= P
        v += 1
    while b % P == 0:
        b //= P
        v -= 1
    return v


def residue(x, m=121):
    x = F(x)
    need(x.denominator % P != 0, 'nonintegral rational reduced without precision control')
    return x.numerator * pow(x.denominator, -1, m) % m


def shifted_polynomial():
    roots = [a for a in range(P) if sum(c*a**i for i, c in enumerate(F_POLY)) % P == 0]
    need(roots == [4], 'wrong residual root')
    g = [sum(F_POLY[j]*comb(j, i)*4**(j-i) for j in range(i, 12)) for i in range(12)]
    need(g == EXPECTED_G, 'changed field polynomial')
    need(g[-1] == 1 and vp(g[0]) == 1 and all(vp(c) >= 1 for c in g[:-1]),
         'not an Eisenstein uniformizer')
    weights = [11*vp(i*g[i])+i-1 for i in range(1, 12)]
    need(min(weights) == 20 and weights.count(20) == 1, 'different derivative valuation')
    return g


def logarithm_coefficients(N=33):
    # w=t^3*u, u=1+(t-t^2)u-79*t^4*u^2+289*t^6*u^3.
    u = [1]
    for n in range(1, N):
        square = lambda k: sum(u[i]*u[k-i] for i in range(k+1)) if k >= 0 else 0
        cube = lambda k: sum(u[i]*u[j]*u[k-i-j] for i in range(k+1)
                             for j in range(k-i+1)) if k >= 0 else 0
        u.append(u[n-1]-(u[n-2] if n >= 2 else 0)-79*square(n-4)+289*cube(n-6))
    inv = [1]
    for n in range(1, N):
        inv.append(-sum(u[j]*inv[n-j] for j in range(1, n+1)))
    omega = []
    for n in range(N):
        numerator = 2 if n == 0 else sum(j*u[j]*inv[n-j] for j in range(1, n+1))
        omega.append((F(numerator)+(omega[n-1] if n else 0))/2)
    need(omega[:5] == [1, 1, 0, -1, -159], 'wrong minimal-model differential')
    need(all(x.denominator % 11 for x in omega), 'differential not11-integral')
    return [F(0)]+[omega[n-1]/n for n in range(1, N+1)]


def newton_traces(g, N=33):
    s = [11]
    for n in range(1, N+1):
        if n <= 11:
            s.append(-sum(g[11-j]*s[n-j] for j in range(1, n))-n*g[11-n])
        else:
            s.append(-sum(g[11-j]*s[n-j] for j in range(1, 12)))
    return s


def companion_traces(g, N=33):
    # Independent: trace of multiplication by pi^n on Q[X]/g, no Newton sums.
    def times_pi(v):
        return [-v[-1]*g[0]]+[v[i-1]-v[-1]*g[i] for i in range(1, 11)]
    power = [[int(i == j) for i in range(11)] for j in range(11)]
    traces = [11]
    for _ in range(N):
        power = [times_pi(v) for v in power]
        traces.append(sum(power[i][i] for i in range(11)))
    return traces


def infinite_tail_certificate(g, traces):
    # Initial11 power traces and ALL periodic induction inequalities imply
    # v11(S_n)>=floor((n+20)/11) for EVERY n>=1, not merely sampled n.
    need(all(vp(traces[n]) >= (n+20)//11 for n in range(1, 12)), 'initial trace bound fails')
    for r in range(11):
        for j in range(1, 12):
            need(vp(g[11-j])+(r-j+20)//11 >= (r+20)//11,
                 'Newton trace induction inequality fails')
    # If n>=23 and k=v11(n): k=0 gives >=3; k=1 has n>=33,
    # giving >=4-1=3; k>=2 gives >=11^(k-1)+1-k >=10.
    need((23+20)//11 >= 3 and (33+20)//11-1 >= 3, 'tail low cases')
    need(11**(2-1)+1-2 >= 3 and 10*11-1 > 0, 'tail higher-valuation induction')
    # Thus lambda_n*S_n is in11^3 Z11 for every omitted n>=23.


def calculate():
    g = shifted_polynomial()
    log = logarithm_coefficients()
    traces = newton_traces(g)
    need(traces == companion_traces(g), 'independent trace algorithms disagree')
    infinite_tail_certificate(g, traces)
    rows = [(n, log[n], traces[n], residue(log[n]*traces[n]/11)) for n in range(1, 34)]
    norm = residue(sum((log[n]*traces[n] for n in range(1, 23)), F(0))/11)
    need(norm == 115 and norm % 11 == 5, 'wrong actual elliptic norm')
    need(all(term == 0 for n, _, _, term in rows if n >= 23), 'tail cross-check fails')
    z = 11*norm
    tnorm = residue(F(z)-F(z*z, 2), 1331)
    need(tnorm == 418, 'wrong norm formal parameter')
    # C0039 uses SHORT differential; MINIMAL differential is twice it.
    short_p = [4, 0, 8, 3]
    p_refs = [2*a*pow(norm, -1, 11) % 11 for a in short_p]
    r_refs = [2*a*pow(norm, -1, 11) % 11 for a in (9, 2)]
    kernel_refs = [(p_refs[j]-a*p_refs[0]) % 11 for j, a in ((1, 2), (2, 7), (3, 8))]
    need(p_refs == [6, 0, 1, 10] and r_refs == [8, 3] and kernel_refs == [10, 3, 6],
         'minimal/short reference normalization mismatch')
    # Dangerous shortcuts are observably wrong on this actual point.
    need(residue(F(traces[1], 11), 11) == 7, 'linear norm control')
    need((norm-rows[10][3]) % 11 == 7 != norm % 11, 'missing degree11 term not detected')
    need([11 % 11, 11 % 121] == [0, 11], 'C11/mod121 T2 fidelity boundary')
    bad = list(traces)
    bad[2] = 1
    rejected(lambda: infinite_tail_certificate(g, bad))
    rejected(lambda: residue(F(1, 11)))
    return g, rows, norm, tnorm, p_refs, r_refs, kernel_refs


def check_pari(text, expected):
    g, rows, norm, tnorm, p_refs, r_refs, kernel_refs = expected
    lines = text.strip().splitlines()
    need(lines and lines[0] == 'BEGIN_LOCAL_NORM37', 'missing PARI start or interpreter diagnostics')
    need(lines[-1] == 'END_LOCAL_NORM37', 'missing PARI completion')
    need(not any('***' in line for line in lines), 'PARI interpreter error')
    need(len(lines) == 44, 'incomplete/duplicate PARI transcript')
    need(re.fullmatch(r'VERSION \[\d+, \d+, \d+\]', lines[1]) is not None, 'missing GP version')
    need(lines[2] == 'G '+str(g), 'shifted polynomial mismatch')
    need(lines[3] == 'DISC11 20', 'different/discriminant mismatch')
    got = []
    for line in lines[4:37]:
        parts = line.split()
        need(len(parts) == 5 and parts[0] == 'ROW', 'bad PARI row')
        got.append((int(parts[1]), F(parts[2]), int(parts[3]), int(parts[4])))
    need(got == rows, 'PARI formal coefficients, power traces or contributions disagree')
    need(lines[37:43] == ['NORM '+str(norm), 'TNORM '+str(tnorm), 'LONGSUM '+str(norm),
                         'PREF '+str(p_refs), 'RREF '+str(r_refs), 'KREF '+str(kernel_refs)],
         'PARI norm or precision cross-check mismatch')


def main():
    expected = calculate()
    if len(sys.argv) > 1:
        text = Path(sys.argv[1]).read_text()
        check_pari(text, expected)
        rejected(lambda: check_pari(text.replace('NORM 115\n', 'NORM 114\n', 1), expected))
        rejected(lambda: check_pari(text.replace('END_LOCAL_NORM37', ''), expected))
        rejected(lambda: check_pari(text+'\n*** error', expected))
        rejected(lambda: check_pari(text.replace('ROW 11 ', 'ROW 10 ', 1), expected))
        print('PASS independent PARI formal logarithm, all33 traces/contributions, two truncations and mutations')
    _, _, norm, tnorm, p, r, k = expected
    print('PASS Eisenstein root pi=xi-4; derivative valuation20; Newton trace proof covers EVERY omitted n')
    print('ACTUAL local norm log/11 mod121 =', norm, '; norm parameter mod1331 =', tnorm)
    print('RESIDUAL local reference scalars P1..P4 =', p, '; R plus/minus-place =', r, '; three kernel combinations =', k)
    print('NONCLAIM: point/Shapiro LOCAL residual references only; no evaluated global c1, mod121 T2 lift, h2 or complex BSD.')


if __name__ == '__main__':
    main()
