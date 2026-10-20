#!/usr/bin/env python3
"""Independent first-digit BCLMN oracle: direct coordinates and denominator IDEAL.

No project imports, division polynomials, stored denominator generators, sigma
parameters or existing height residues are used to calculate the outputs.
Only Python's exact Fraction is required. This is AI-authored corroboration,
not independently maintained Sage/Magma code or a Howard-height comparison.
The formula and normalization remain shared published mathematical inputs.
"""
from fractions import Fraction as F
from math import lcm, isqrt
from functools import lru_cache


class Quadratic:
    """Q(omega), omega^2-omega+m=0; m=2 or 3 (norm Euclidean)."""
    def __init__(self, m):
        assert m in (2, 3)
        self.m = m

    def elt(self, a=0, b=0):
        return (F(a), F(b))

    def add(self, z, w):
        return (z[0]+w[0], z[1]+w[1])

    def neg(self, z):
        return (-z[0], -z[1])

    def sub(self, z, w):
        return self.add(z, self.neg(w))

    def mul(self, z, w):
        a, b = z; c, d = w
        return (a*c-self.m*b*d, a*d+b*c+b*d)

    def conj(self, z):
        a, b = z
        return (a+b, -b)

    def norm(self, z):
        a, b = z
        return a*a+a*b+self.m*b*b

    def div(self, z, w):
        n = self.norm(w)
        assert n
        a, b = self.mul(z, self.conj(w))
        return (a/n, b/n)

    def pow(self, z, n):
        out = self.elt(1)
        while n:
            if n & 1: out = self.mul(out, z)
            n //= 2
            if n: z = self.mul(z, z)
        return out

    def integral(self, z):
        return all(v.denominator == 1 for v in z)

    def gcd(self, z, w):
        assert self.integral(z) and self.integral(w)
        while w != self.elt():
            # Compare squared distances as INTEGERS; repeated Fraction norm
            # reductions here would dominate the large-coordinate runtime.
            A,B=(int(v) for v in self.mul(z,self.conj(w)))
            n=int(self.norm(w)); i,j=A//n,B//n
            def distance(pair):
                c,d=pair; a,b=A-c*n,B-d*n
                return a*a+a*b+self.m*b*b
            c,d=min(((c,d) for c in range(i-1,i+3) for d in range(j-1,j+3)),key=distance)
            q=self.elt(c,d)
            r = self.sub(z, self.mul(q,w))
            assert self.integral(r) and self.norm(r) < self.norm(w)
            z, w = w, r
        return z


class Curve:
    def __init__(self, k, a):
        self.k, self.a = k, tuple(k.elt(v) for v in a)

    def oncurve(self, P):
        if P is None: return True
        k=self.k; x,y=P; a1,a2,a3,a4,a6=self.a
        lhs=k.add(k.add(k.pow(y,2),k.mul(a1,k.mul(x,y))),k.mul(a3,y))
        rhs=k.add(k.add(k.pow(x,3),k.mul(a2,k.pow(x,2))),k.add(k.mul(a4,x),a6))
        return lhs==rhs

    def add(self, P, Q):
        if P is None: return Q
        if Q is None: return P
        k=self.k; x,y=P; u,v=Q; a1,a2,a3,a4,_=self.a
        if x==u:
            if k.add(k.add(y,v),k.add(k.mul(a1,x),a3))==k.elt(): return None
            num=k.sub(k.add(k.mul(k.elt(3),k.pow(x,2)),
                            k.add(k.mul(k.elt(2),k.mul(a2,x)),a4)),k.mul(a1,y))
            den=k.add(k.mul(k.elt(2),y),k.add(k.mul(a1,x),a3))
        else:
            num=k.sub(v,y); den=k.sub(u,x)
        slope=k.div(num,den)
        intercept=k.sub(y,k.mul(slope,x))
        z=k.sub(k.sub(k.add(k.pow(slope,2),k.mul(a1,slope)),a2),k.add(x,u))
        w=k.neg(k.add(k.add(k.mul(k.add(slope,a1),z),intercept),a3))
        assert self.oncurve((z,w))
        return z,w

    @lru_cache(maxsize=None)
    def scale(self, n, P):
        out=None
        while n:
            if n&1: out=self.add(out,P)
            n//=2
            if n: P=self.add(P,P)
        return out


@lru_cache(maxsize=None)
def denominator_square(k, x):
    """(delta) is the FULL denominator ideal of x, so (delta)=(d)^2.

    If x=N/D, then denom(x)=(D)/(N,D). No factorization, square root,
    point-division recurrence or candidate denominator is involved.
    """
    D=lcm(*(v.denominator for v in x))
    N=k.mul(x,k.elt(D))
    g=k.gcd(N,k.elt(D))
    delta=k.div(k.elt(D),g)
    X=k.mul(x,delta)
    assert k.integral(delta) and k.integral(X)
    assert k.norm(k.gcd(X,delta))==1
    assert k.norm(delta).denominator==1
    n=int(k.norm(delta))
    assert isqrt(n)**2==n
    return delta


def valuation(n,p):
    assert n
    e=0
    while n%p==0: e+=1; n//=p
    return e


def roots(k,p,root,guard):
    assert (root*root-root+k.m)%p==0
    for e in range(1,guard):
        choices=[root+c*p**e for c in range(p)
                 if ((root+c*p**e)**2-(root+c*p**e)+k.m)%p**(e+1)==0]
        assert len(choices)==1
        root=choices[0]
    return root,(1-root)%p**guard


def local_unit(z,p,root,guard):
    """Return exact valuation and unit modulo p^2 with checked guard loss."""
    D=lcm(*(v.denominator for v in z))
    N=(int(z[0]*D)+int(z[1]*D)*root)%p**guard
    assert N, 'increase guard precision'
    en=valuation(N,p); ed=valuation(D,p)
    assert guard-en>=2, 'insufficient unit precision'
    return en-ed,(N//p**en)*pow(D//p**ed,-1,p*p)%(p*p)


def self_height(E,Q,p,n,root,guard=16,wrong_sigma=False,delta_factor=1):
    """BCLMN Prop2.4, class number1, squared to avoid choosing sqrt(delta)."""
    k=E.k
    assert E.oncurve(Q) and n%p
    x,y=E.scale(n,Q)
    delta=denominator_square(k,x)
    # For the adversarial all-place test only: alter the denominator ideal.
    delta=k.mul(delta,k.elt(delta_factor[0],delta_factor[1])) if isinstance(delta_factor,tuple) else k.mul(delta,k.elt(delta_factor))
    assert k.integral(k.mul(k.pow(y,2),k.pow(delta,3)))
    t=k.neg(k.div(x,y))
    local=[]
    for rt in roots(k,p,root,guard):
        vt,ut=local_unit(t,p,rt,guard)
        vd,ud=local_unit(delta,p,rt,guard)
        assert vt>=1 and vd==2*vt
        tm=ut*p**vt%(p*p)
        # Integral sigma(t)=t+(a1/2)t^2+O(t^3).
        # (sigma(t)/t)^2 = 1+a1*t+O(p^2); no E2 needed at this precision.
        a1=0 if wrong_sigma else int(E.a[0][0])
        local.append(ut*ut*pow(ud,-1,p*p)*(1+a1*tm)%(p*p))
    q2=local[0]*pow(local[1],-1,p*p)%(p*p)
    # log(q2)/p modulo p via Fermat quotient; q2 is a unit.
    log_over_p=((pow(q2,p-1,p*p)-1)//p)*pow(p-1,-1,p)%p
    return log_over_p*pow(2*n*n,-1,p)%p,q2


def main():
    k=Quadratic(2); E=Curve(k,(1,-1,0,-79,289))
    # Original short-model inputs, converted explicitly to minimal coordinates.
    points=[(k.elt(F(x+1,4)),k.elt(F(y-x-1,8)))
            for x,y in [(15,40),(19,4),(23,16),(31,88)]]
    # sqrt(-7)=2*omega-1.
    sx=k.elt(F(-3355,63)); sy=k.elt(F(-128780,1323),F(257560,1323))
    R=(k.div(k.add(sx,k.elt(1)),k.elt(4)),
       k.div(k.sub(sy,k.add(sx,k.elt(1))),k.elt(8)))
    assert all(E.oncurve(P) for P in points+[R])
    singles=[]; squares=[]; wrong=[]
    for index,P in enumerate(points):
        Q=E.add(P,R)
        h,q2=self_height(E,Q,11,18,7)
        singles.append(h); squares.append(q2)
        assert self_height(E,Q,11,18,7,guard=20)==(h,q2)
        wrong.append(self_height(E,Q,11,18,7,wrong_sigma=True)[0])
        print('computed at [18]',index+1,h,q2,flush=True)
    # Expected outputs are checked AFTER all computations, never imported.
    assert singles==[1,2,7,8],singles
    assert [pow(q,4,121) for q in squares]==[97,34,60,36],squares
    assert wrong!=singles, 'omitting minimal-model sigma correction must fail'
    mixed=[]
    for i in range(4):
        for j in range(i+1,4):
            h,_=self_height(E,E.add(E.add(points[i],points[j]),R),11,18,7)
            assert h==(singles[i]+singles[j])%11
            mixed.append(h)
    # Nonrational artificial ideal factor has nonzero anticyclotomic character.
    altered=self_height(E,E.add(points[0],R),11,18,7,delta_factor=(0,2))[0]
    assert altered!=singles[0]
    # Swap embeddings: root omega=5 corresponds to sqrt(-7)=-2 mod11.
    assert self_height(E,E.add(points[0],R),11,18,5)[0]==-singles[0]%11
    print('PASS direct-coordinate first heights mod11:',singles)
    print('PASS squared sigma/ideal ratios mod121:',squares)
    print('PASS six mixed sums:',mixed)
    print('PASS [18] vs prior [36] implementation, guard precision, sigma/ideal/orientation mutations')
    # Published BCLMN Sec5.1 example. Neither printed d([9]A) nor psi9 is used.
    j=Quadratic(3); C=Curve(j,(0,1,1,-2,0))
    S=(j.elt(F(1,4)),j.elt(F(-5,8),F(1,4)))
    controls=[self_height(C,C.add(P,S),5,9,4)[0]
              for P in [(j.elt(-1),j.elt(1)),(j.elt(),j.elt())]]
    assert controls==[3,3],controls
    print('PASS two published 389a1/K=-11/p5 controls:',controls)
    print('CONDITIONAL on BCLMN character, sigma integrality and component hypotheses.')
    print('NONCLAIM: no maintained-library/expert audit, Howard h1 equality, genuine h2 or BSD.')


if __name__=='__main__':
    main()
