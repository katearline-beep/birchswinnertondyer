#!/usr/bin/env python3
"""Second Bockstein for a GIVEN two-term finite-free complex over F_p[[T]].

This implements lift-and-quotient algebra, not Galois/Selmer presentations.
Examples below are deliberately synthetic. A cohomology obstruction becomes
a height only after supplying arithmetic local conditions and duality maps.
See Macias Castillo--Sano 2603.23978, Appendix A, Def A.1/Prop A.4.
"""


def transpose(A): return [list(x) for x in zip(*A)]
def eye(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def zero(m,n): return [[0]*n for _ in range(m)]
def add(A,B,p): return [[(a+b)%p for a,b in zip(r,s)] for r,s in zip(A,B)]
def mul(A,B,p):
    return [[sum(a*b for a,b in zip(r,c))%p for c in zip(*B)] for r in A]
def mv(A,x,p): return [sum(a*b for a,b in zip(r,x))%p for r in A]


def rref(A,p):
    A=[[v%p for v in row] for row in A]; piv=[]; i=0
    for j in range(len(A[0])):
        k=next((k for k in range(i,len(A)) if A[k][j]),None)
        if k is None: continue
        A[i],A[k]=A[k],A[i]
        u=pow(A[i][j],-1,p); A[i]=[v*u%p for v in A[i]]
        for k in range(len(A)):
            if k!=i:
                u=A[k][j]; A[k]=[(v-u*w)%p for v,w in zip(A[k],A[i])]
        piv.append(j); i+=1
        if i==len(A): break
    return A,piv


def kernel(A,p):
    R,piv=rref(A,p); n=len(A[0]); out=[]
    for j in range(n):
        if j in piv: continue
        x=[0]*n; x[j]=1
        for i,c in enumerate(piv): x[c]=-R[i][j]%p
        out.append(x)
    return out  # list of column vectors, possibly empty


def solve(A,b,p):
    n=len(A[0]); R,piv=rref([row+[v] for row,v in zip(A,b)],p)
    if n in piv: raise ValueError('first Bockstein obstruction has not vanished')
    x=[0]*n
    for i,j in enumerate(piv): x[j]=R[i][-1]
    assert mv(A,x,p)==[v%p for v in b]
    return x


def beta2(D0,D1,D2,p=11):
    """Return S2 basis, first-order lifts, target quotient rows and beta2.

    S2=ker(beta1) inside ker D0. Target is C2/(im D0+D1 ker D0).
    Each x1 solves D0*x1=-D1*x; beta2(x)=[D2*x+D1*x1].
    This function refuses the zero-cohomology cases to keep empty matrices
    explicit; it does not pretend to be a general spectral-sequence library.
    """
    m,n=len(D0),len(D0[0])
    assert all(len(A)==m and all(len(r)==n for r in A) for A in (D0,D1,D2))
    K=kernel(D0,p); L=kernel(transpose(D0),p)
    if not K or not L: raise ValueError('no degree-one or degree-two cohomology')
    first=mul(L,mul(D1,transpose(K),p),p)
    coefficients=kernel(first,p)
    if not coefficients: raise ValueError('no first Bockstein survivors')
    S=[mv(transpose(K),v,p) for v in coefficients]
    lifts=[solve(D0,[-v%p for v in mv(D1,x,p)],p) for x in S]
    DK=mul(D1,transpose(K),p)
    W=[a+b for a,b in zip(D0,DK)]
    Q=kernel(transpose(W),p)
    if not Q: raise ValueError('second Bockstein target is zero')
    residues=[]
    for x,x1 in zip(S,lifts):
        r=[(a+b)%p for a,b in zip(mv(D2,x,p),mv(D1,x1,p))]
        residues.append(mv(Q,r,p))
        # Every alternate lift x1+k changes the residue by D1*k,
        # which MUST vanish in the quotient (not necessarily in C2).
        for k in K:
            assert mv(Q,mv(D1,k,p),p)==[0]*len(Q)
    return S,lifts,Q,transpose(residues)


def main():
    p=11; n=5
    D0=zero(n,n); D0[0][0]=D0[1][1]=1
    D1=zero(n,n)
    D1[0][2]=D1[1][3]=1
    D1[2][1]=1; D1[3][0]=-1
    D2=zero(n,n)
    S,lifts,Q,B=beta2(D0,D1,D2)
    expected=[[0,10,0],[1,0,0],[0,0,0]]
    assert B==expected and len(rref(B,p)[1])==2
    assert not any(any(v for v in row) for row in mul(Q,mul(D2,transpose(S),p),p))
    # The RAW T^2 coefficient is zero but the genuine LIFT obstruction is not.
    print('PASS raw D2=0, corrected second obstruction rank2:',B)
    # Same D0 AND D1; distinct D2 cancels the second obstruction entirely.
    cancel=zero(n,n)
    for i in range(3):
        for j in range(3): cancel[i+2][j+2]=-expected[i][j]
    assert beta2(D0,D1,cancel)[3]==zero(3,3)
    print('PASS identical first-order complex, either zero or rank2 second obstruction')
    # Independent check: directly multiply D(T)(x+T*x1) coefficientwise.
    for x,x1,col in zip(S,lifts,transpose(B)):
        assert mv(D0,x,p)==[0]*n
        assert [(a+b)%p for a,b in zip(mv(D1,x,p),mv(D0,x1,p))]==[0]*n
        coeff=[(a+b)%p for a,b in zip(mv(D2,x,p),mv(D1,x1,p))]
        assert mv(Q,coeff,p)==col
    # Identity-at-T=0 basis changes V(T) D(T) U(T) preserve beta2.
    U=[[((i+2)*(j+1))%p for j in range(n)] for i in range(n)]
    V=[[((i+1)**2+3*j)%p for j in range(n)] for i in range(n)]
    E1=add(add(D1,mul(D0,U,p),p),mul(V,D0,p),p)
    E2=add(add(add(D2,mul(D1,U,p),p),mul(V,D1,p),p),mul(mul(V,D0,p),U,p),p)
    assert beta2(D0,E1,E2)[3]==B
    print('PASS first-order lift ambiguity and T-dependent source/target basis changes')
    # A first-order non-survivor cannot be fed to the lifting equation.
    try: solve([[0]],[1],p)
    except ValueError: pass
    else: raise AssertionError('invalid lift accepted')
    # mod11 ZERO does not imply Q11 ZERO: 11*J is nonzero mod121.
    assert 11%11==0 and 11%121!=0
    print('PASS finite-zero is inconclusive: 11*T^2*J vanishes mod11, not mod121')
    print('NONCLAIM: matrices are synthetic; no actual Selmer D(T), h2 or BSD computed.')


if __name__=='__main__': main()
