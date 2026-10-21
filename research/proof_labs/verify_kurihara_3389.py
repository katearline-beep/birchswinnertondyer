#!/usr/bin/env python3
"""Independent standard-library transcript arithmetic checker.

Does not independently evaluate the focal modular symbols or prove their
normalization. Completeness, symmetry, Hecke relations and weighted sums
are checked from the exact producer transcript. Malformed data fail closed.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

Q,P = 3389,11
CHI = (1,1,-1,1,-1,-1)


def need(ok,msg):
    if not ok:
        raise ValueError(msg)


def res(v):
    need(v.denominator % P != 0,'denominator divisible by11')
    return v.numerator*pow(v.denominator,-1,P) % P


def count(ell):
    # Original short model, independent of Sage/GP point counting.
    return 1+sum(1 for x in range(ell) for y in range(ell)
                 if (y*y-x*x*x+1267*x-17230) % ell == 0)


def canonical_lines(text):
    lines=[]
    for line in text.splitlines():
        # GitHub logs prepend UTC timestamps. Require the marker at line start
        # or directly after one timestamp, never inside printed shell commands.
        fields=line.split(' ',1)
        if fields[0].startswith('20') and fields[0].endswith('Z') and len(fields)==2:
            line=fields[1]
        if line.startswith('S35'):
            lines.append(line)
    return lines


def verify(text):
    lines=canonical_lines(text)
    need(not any('Traceback (most recent call last)' in s or '***' in s for s in text.splitlines()),'interpreter error')
    def one(tag):
        vals=[json.loads(s[len(tag)+1:]) for s in lines if s.startswith(tag+' ')]
        need(len(vals)==1,'missing/duplicate '+tag)
        return vals[0]
    meta,control,result=one('S35META'),one('S35CONTROL'),one('S35RESULT')
    alg=one('S35ALGORITHM')
    need(alg['backend']=='sage_num_proven_rational' and alg['semistable'] is True
         and alg['isogeny_class_size']==1 and alg['denominator']==7*Q, 'numerical theorem input gate')
    need(meta['sage'].startswith('10.6') and meta['curve']==[1,-1,0,-79,289], 'runtime/curve mismatch')
    need(meta['q']==Q and meta['p']==P and meta['sign_space']=='numerical_no_basis' and meta['backend']=='sage_num_proven_rational' and meta['evaluation_sign']==-1,'wrong problem/sign')
    need(len(meta['source_head'])==40 and all(c in '0123456789abcdef' for c in meta['source_head']),'missing source provenance')
    expected=[1,1,1,-2,1,-2]
    for name,scale in (('direct','scale_plus'),('twisted','scale_twist')):
        data=list(map(F,control[name])); factor=F(control[scale])
        need(len(data)==6 and res(factor)!=0 and data==[factor*x for x in expected], 'small control mismatch')
    need(all(F(a)!=F(b) for a,b in zip(control['twisted'],control['wrong'])),'wrong sign not rejected')
    heckes=[json.loads(s[len('S35HECKE '):]) for s in lines if s.startswith('S35HECKE ')]
    need([d['ell'] for d in heckes]==[3,5,13], 'incomplete Hecke checks')
    for d in heckes:
        ell=d['ell']; ap=ell+1-count(ell)
        need(d['ap']==ap and len(d['terms'])==ell+1 and sum(map(F,d['terms']))==ap*F(d['value']),'Hecke relation or trace mismatch')
    rows=[s for s in lines if s.startswith('S35ROW ')]
    need(len(rows)==Q-1 and result['rows']==Q-1, 'incomplete transcript')
    digest=hashlib.sha256(('\n'.join(rows)+'\n').encode()).hexdigest()
    need(digest==result['rows_sha256'],'transcript hash mismatch')
    values={}
    for a,line in enumerate(rows,1):
        fields=line.split()
        need(len(fields)==9 and int(fields[1])==a,'missing/reordered/duplicate row')
        v=list(map(F,fields[2:])); reduced=list(map(res,v))
        need(v[-1]==sum(c*x for c,x in zip(CHI,v[:6])),'twisting rational sum mismatch')
        need(reduced[-1]==sum(c*x for c,x in zip(CHI,reduced[:6])) % P,'twisting residue mismatch')
        values[a]=v
    for a,v in values.items():
        w=values[Q-a]
        need(w[-1]==v[-1] and w[:6]==[-x for x in reversed(v[:6])],'parity/conjugation mismatch')
    # Table logs and an independent running-power weighted sum.
    logs={};x=1
    for j in range(Q-1):
        need(x not in logs,'generator not primitive');logs[x]=j % P;x=x*3 % Q
    need(x==1 and len(logs)==Q-1,'incomplete discrete logs')
    direct=sum(logs[a]*res(v[-1]) for a,v in values.items()) % P
    running=0;x=1
    for j in range(Q-1):
        running=(running+j*res(values[x][-1])) % P;x=x*3 % Q
    # Independent generator h=3^5; its log coordinates differ by5^-1 mod11.
    alternate=0;x=1
    for j in range(Q-1):
        alternate=(alternate+j*res(values[x][-1])) % P;x=x*pow(3,5,Q) % Q
    need(x==1 and direct==running==result['delta'] and alternate==pow(5,-1,P)*direct % P,'weighted sum mismatch')
    need(sum(s.startswith('S35COMPLETE ') for s in lines)==1,'missing completion')
    return direct,digest,meta


def main():
    need(len(sys.argv)==2,'usage: verifier transcript')
    text=Path(sys.argv[1]).read_text()
    d,h,m=verify(text)
    print('PASS all3388 rational rows, symmetry, character, denominator units, Hecke traces and two-generator sums')
    print('VERIFIED_TRANSCRIPT delta='+str(d)+' sha256='+h+' source_head='+m['source_head'])
    for bad in (text.replace('S35ROW 1 ','S35ROW 2 ',1),text+'\n*** synthetic error',text.replace('S35COMPLETE ','INCOMPLETE ',1)):
        try:
            verify(bad)
        except (ValueError,KeyError,ZeroDivisionError):
            pass
        else:
            raise AssertionError('mutated transcript accepted')
    print('PASS duplicate-row, interpreter-error and incomplete-transcript mutations rejected')
    print('BOUNDARY focal modular-symbol evaluation and period normalization remain trusted inputs; no h2 or original BSD')


if __name__=='__main__':
    main()
