#!/usr/bin/env python3
"""Actual good-reduction certificate for five focal Kummer classes mod11.

No Selmer completeness or global height input. Independent GP oracle optional.
Search cap20000 is only a resource bound; a failed search proves nothing.
"""
from math import isqrt
from pathlib import Path
import sys

A, B, P = -1267, 17230, 11
POINTS = [(15,40),(19,4),(23,16),(31,88)]


def prime(n):
    return n >= 2 and all(n % d for d in range(2,isqrt(n)+1))


def add(U, V, q):
    if U is None: return V
    if V is None: return U
    x,y = U; z,w = V
    if x == z and (y+w) % q == 0: return None
    slope = ((3*x*x+A)*pow(2*y,-1,q) if U == V else (w-y)*pow(z-x,-1,q)) % q
    xx = (slope*slope-x-z) % q
    return xx, (slope*(x-xx)-y) % q


def mul(n, U, q):
    assert n >= 0
    V = None
    while n:
        if n & 1: V = add(V,U,q)
        U = add(U,U,q); n //= 2
    return V


def count(q):
    # Direct square-frequency count, not the GP ellcard algorithm.
    squares = [0]*q
    for y in range(q): squares[y*y % q] += 1
    return 1 + sum(squares[(x*x*x+A*x+B) % q] for x in range(q))


def reduced_points(q, root):
    points = [(x % q,y % q) for x,y in POINTS]
    points += [(-3355*pow(63,-1,q) % q, 128780*pow(1323,-1,q)*root % q)]
    assert all((y*y-x*x*x-A*x-B) % q == 0 for x,y in points)
    return points


def rank(rows):
    if not rows: return 0
    m = [[x % P for x in row] for row in rows]
    r = 0
    for c in range(len(m[0])):
        pivot = next((i for i in range(r,len(m)) if m[i][c]),None)
        if pivot is None: continue
        m[r],m[pivot] = m[pivot],m[r]
        scale = pow(m[r][c],-1,P)
        m[r] = [x*scale % P for x in m[r]]
        for i in range(len(m)):
            if i != r:
                t = m[i][c]; m[i] = [(x-t*y) % P for x,y in zip(m[i],m[r])]
        r += 1
        if r == len(m): break
    return r


def determinant(matrix):
    # Independent permutation formula, five rows only.
    from itertools import permutations
    total = 0
    for perm in permutations(range(len(matrix))):
        inv = sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
        term = (-1)**inv
        for i,j in enumerate(perm): term *= matrix[i][j]
        total += term
    return total % P


def row_at(q, root):
    assert prime(q) and q > 3 and q not in (7,11,117223)
    assert (root*root+7) % q == 0
    n = count(q)
    assert n % P == 0 and n % (P*P) != 0, 'Need valuation exactly one'
    points = reduced_points(q,root)
    projections = [mul(n//P,U,q) for U in points]
    T = next((U for U in projections if U is not None),None)
    if T is None: return None
    assert mul(P,T,q) is None
    table = {mul(k,T,q):k for k in range(P)}
    assert len(table) == P
    row = [table[U] for U in projections]
    return {'q':q,'root':root,'order':n,'generator':list(T),'row':row}


def certificate():
    chosen, rows = [], []
    for q in range(5,20001):
        if q in (7,11,117223) or not prime(q) or pow(-7 % q,(q-1)//2,q) != 1:
            continue
        n = count(q)
        if n % P or n % (P*P) == 0: continue
        root = next(x for x in range(q) if x*x % q == -7 % q)
        item = row_at(q,root)
        if item is not None and rank(rows+[item['row']]) > len(rows):
            chosen.append(item); rows.append(item['row'])
        if len(rows) == 5: break
    assert len(rows) == 5, 'No certificate in declared range; no dependence conclusion'
    assert count(23) == 30 and pow(-7 % 23,11,23) == 1
    print('PASS split prime23 has order30, so E(K)[11]=0 by good reduction')
    bad_root = next(x for x in range(911) if (x*x+7) % 911 == 0)
    assert count(911) == 968
    try: row_at(911,bad_root)
    except AssertionError as exc:
        assert str(exc) == 'Need valuation exactly one'
        print('PASS negative control: actual q911 with order8*121 refused')
    else: raise AssertionError('Wrong group valuation accepted')
    det = determinant(rows)
    assert det != 0 and rank(rows) == 5
    for item in chosen: print('WITNESS',item)
    print('PASS actual five-point reduction matrix determinant',det,'mod11')
    # Replace P4 with P1+P2 at EVERY place, using the finite group law.
    bad = []
    for item in chosen:
        q = item['q']; points = reduced_points(q,item['root'])
        points[3] = add(points[0],points[1],q)
        T = tuple(item['generator']); table = {mul(k,T,q):k for k in range(P)}
        bad.append([table[mul(item['order']//P,U,q)] for U in points])
    assert rank(bad) == 4 and determinant(bad) == 0
    assert all(row[3] == (row[0]+row[1]) % P for row in bad)
    print('PASS negative control: actual dependent point replacement forces rank4')
    # The three residual height-kernel recipes are nonzero, independent classes
    # if their coefficients are those of the accepted characteristic-zero recipe.
    combinations = [[-r, int(j==0), int(j==1), int(j==2), 0]
                    for j,r in enumerate((2,7,8))]
    signatures = [[sum(x*y for x,y in zip(row,v)) % P for v in combinations] for row in rows]
    assert rank(signatures) == 3
    print('PASS three residual combinations have independent actual reduction signatures')
    return chosen


def validate_pari(lines, chosen):
    assert len(lines) == len(chosen) and not any('***' in line for line in lines)
    for line,item in zip(lines,chosen):
        parts = line.split()
        assert len(parts) == 12 and parts[0] == 'REDUCTION'
        values = list(map(int,parts[1:]))
        expected = [item['q'],item['root'],item['order'],*item['generator'],*item['row'],11]
        assert values == expected, 'PARI reduction mismatch'


def compare(path, chosen):
    lines = Path(path).read_text(encoding='utf8').splitlines()
    validate_pari(lines,chosen)
    bad = lines[:]; parts = bad[0].split(); parts[7] = str((int(parts[7])+1) % P)
    bad[0] = ' '.join(parts)
    try: validate_pari(bad,chosen)
    except AssertionError: print('PASS negative control: changed independent oracle residue rejected')
    else: raise AssertionError('Mutation escaped')
    print('PASS PARI all point counts, torsion generators and25 discrete logs agree')


def main():
    chosen = certificate()
    if len(sys.argv) == 2: compare(sys.argv[1],chosen)
    else: assert len(sys.argv) == 1
    print('CONCLUSION: five known MW classes independent mod11; their subgroup is11-saturated in E(K)')
    print('NONCLAIM: no full Selmer upper bound, first lift, second height or complex BSD')


if __name__ == '__main__': main()
