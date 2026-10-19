#!/usr/bin/env python3
"""Conditional first-height radical mod11, NOT a computed derived height.

Uses provisional C-0011 global self-height vector (1,2,7,8).
If the height normalization and actual global height values are correct,
anti-invariance forces a rank-2 first height pairing over Q_11, with a
three-dimensional radical. This computation is elementary linear algebra.
"""
p=11
a=[1,2,7,8]  # provisional h_rho(P_i+R), up to a common nonzero scalar
# Eigenbasis P1,P2,P3,P4,R. Gram pairing has off-diagonal cross vector;
# h_rho(A_i)=-<P_i,R>_rho in the paper's self-height normalization.
B=[[0]*5 for _ in range(5)]
for i in range(4):
    B[i][4]=B[4][i]=-a[i]%p

def pair(x,y):
    return sum(x[i]*B[i][j]*y[j] for i in range(5) for j in range(5))%p

radical=[
    [-2,1,0,0,0],
    [-7,0,1,0,0],
    [-8,0,0,1,0],
]
for v in radical:
    assert all(pair(v,[int(i==j) for i in range(5)])==0 for j in range(5))
# These three radicals are independent, visibly via coordinates 2-4.
# A unit 2x2 minor on (P1,R) forces full rank 2 (global symmetry upper bound 2).
assert B[0][4]*B[4][0]%p == 1
# The old local-log kernel contains P2, but global height pairing does not:
P2=[0,1,0,0,0];R=[0,0,0,0,1]
assert pair(P2,R)==(-2)%p != 0
print('PASS conditional rank 2, radical dimension 3 over Q_11')
print('PASS conditional radical mod11: P2-2P1, P3-7P1, P4-8P1')
print('PASS old local-log kernel P2 fails actual global-height condition')
print('NONCLAIM: C-0011 still provisional; no global derived pairing or complex BSD theorem')
