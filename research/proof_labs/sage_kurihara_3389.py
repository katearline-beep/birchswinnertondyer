#!/usr/bin/env python3
"""Bounded Sage/eclib producer. Run with sage -python; no BSD assertion.

Output is a complete rational transcript, not an independently verified proof.
Sage/eclib period normalization is an explicit trusted-library obligation.
"""
import hashlib
import json
import os
import time
from sage.all import EllipticCurve, QQ
from sage.env import SAGE_VERSION
from sage.libs.eclib.newforms import ECModularSymbol

CHI = (1, 1, -1, 1, -1, -1)
Q, P = 3389, 11


def need(ok, msg):
    if not ok:
        raise AssertionError(msg)


def rat(x):
    return str(x.numerator())+'/'+str(x.denominator())


def residue(x):
    need(int(x.denominator()) % P != 0, 'nonintegral symbol at11')
    return int(x.numerator()) * pow(int(x.denominator()),-1,P) % P


def emit(kind, data):
    print(kind+' '+json.dumps(data,sort_keys=True,separators=(',',':')),flush=True)


def main():
    start = time.monotonic()
    emit('S35META', {'sage':SAGE_VERSION,'source_head':os.environ.get('SOURCE_HEAD','unknown'),
                     'curve':[1,-1,0,-79,289],'q':Q,'p':P,'sign_space':'numerical_no_basis','evaluation_sign':-1,'backend':'sage_num_proven_rational'})
    c = EllipticCurve([0,0,1,-1,0])
    ct = EllipticCurve([0,0,1,-49,-86])
    cm, ctp = ECModularSymbol(c,0), ECModularSymbol(ct,1)
    direct, twisted, wrong = [], [], []
    for a in range(1,7):
        r = QQ(a)/13
        direct.append(ctp(r,1))
        twisted.append(sum(CHI[b-1]*cm(r+QQ(b)/7,-1) for b in range(1,7)))
        wrong.append(sum(CHI[b-1]*cm(r+QQ(b)/7,1) for b in range(1,7)))
    # eclib's native convention may differ from PARI's by a common factor2.
    pari = [1,1,1,-2,1,-2]
    scale_plus = direct[0]/pari[0]
    scale_twist = twisted[0]/pari[0]
    need(all(d == scale_plus*v for d,v in zip(direct,pari)), 'direct PARI control failed')
    need(all(d == scale_twist*v for d,v in zip(twisted,pari)), 'minus twisting control failed')
    need(residue(scale_plus) != 0 and residue(scale_twist) != 0, 'control scaling not11-unit')
    need(all(d != w for d,w in zip(twisted,wrong)), 'wrong sign survived')
    try:
        ECModularSymbol(c,-1)
    except ValueError:
        pass
    else:
        raise AssertionError('unsupported sign accepted')
    emit('S35CONTROL', {'direct':list(map(rat,direct)),'twisted':list(map(rat,twisted)),
                        'wrong':list(map(rat,wrong)),'scale_plus':rat(scale_plus),
                        'scale_twist':rat(scale_twist)})
    e = EllipticCurve([1,-1,0,-79,289])
    need(e.conductor() == 234446, 'wrong original conductor')
    emit('S35PROGRESS', {'stage':'focal initialization','elapsed':time.monotonic()-start})
    need(e.conductor().is_squarefree(), 'numerical theorem needs semistable original curve')
    need(len(e.isogeny_class().curves) == 1, 'outside-table optimality gate unresolved')
    m = e.modular_symbol(sign=-1, implementation='num')
    emit('S35ALGORITHM', {'backend':'sage_num_proven_rational','isogeny_class_size':1,
                          'semistable':True,'denominator':7*Q,
                          'manin_constant_input':'Cesnavicius semistable optimal theorem'})
    need(m(0,-1) == 0, 'minus base cusp fails')
    emit('S35PROGRESS', {'stage':'focal initialized','elapsed':time.monotonic()-start})
    for ell,r in ((3,QQ(1)/13),(5,QQ(2)/17),(13,QQ(5)/19)):
        v = m(r,-1)
        terms = [m(ell*r,-1)] + [m((r+b)/ell,-1) for b in range(ell)]
        ap = int(e.ap(ell))
        need(sum(terms) == ap*v, 'Hecke relation failed')
        emit('S35HECKE', {'ell':ell,'r':str(r),'ap':ap,'value':rat(v),'terms':list(map(rat,terms))})
    # Wuthrich exact rational algorithm: controlled integration plus proven
    # denominator bounds, not unbounded rational reconstruction from a decimal.
    table = m.all_values_for_one_denominator(7*Q, sign=-1)
    emit('S35PROGRESS', {'stage':'all denominator23723 values computed','entries':len(table),
                       'elapsed':time.monotonic()-start})
    logs = {}
    for j in range(Q-1):
        logs[pow(3,j,Q)] = j % P
    need(len(logs) == Q-1, 'generator3 is not primitive')
    delta, digest = 0, hashlib.sha256()
    for a in range(1,Q):
        values = [table[(QQ(a)/Q+QQ(b)/7) % 1] for b in range(1,7)]
        v = sum(chi*x for chi,x in zip(CHI,values))
        for x in values:
            residue(x)
        delta = (delta+logs[a]*residue(v)) % P
        line = 'S35ROW '+str(a)+' '+' '.join(map(rat,values+[v]))
        digest.update((line+'\n').encode())
        print(line,flush=True)
    emit('S35RESULT', {'delta':delta,'rows':Q-1,'rows_sha256':digest.hexdigest(),
                       'elapsed_seconds':time.monotonic()-start,'status':'computed_unreviewed'})
    print('S35COMPLETE no actual h2 or original complex BSD assertion',flush=True)


if __name__ == '__main__':
    main()
