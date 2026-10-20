#!/usr/bin/env python3
"""Exact algebraic controls. These are abstract modules, not elliptic curves."""
from math import prod

def rank2(A):
    (a,b),(c,d)=A
    if a*d-b*c: return 2
    return int(any(v for row in A for v in row))

def charpoly(A):
    (a,b),(c,d)=A
    return (1,-a-d,a*d-b*c)

