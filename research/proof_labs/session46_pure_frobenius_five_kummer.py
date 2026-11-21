#!/usr/bin/env python3
"""Session46: five real pure Frobenius translations span all five Kummer torsors.

Proves a SOURCE-DEPENDENT relative Galois image using finite arithmetic,
classical local Kummer exactness and the original anticyclotomic character.
No global c1/c2, Selmer height, original complex L'' or general BSD theorem.
"""
from itertools import permutations, product
from pathlib import Path
import sys

P = 11
A, B = -1267, 17230
POINTS = ((15, 40), (19, 4), (23, 16), (31, 88))
# q, principal ideal generator a+b*omega, sqrt(-7) mod q,
# #E(Fq), residual Frobenius order, short-model projection [n/11]P1,
# five-point reduction signature P1,P2,P3,P4,R.
DATA = (
    (743, 13, 14, 634, 770, 10, (114, 527), (1, 0, 0, 2, 6)),
    (2843, 43, 14, 399, 2893, 5, (2693, 2385), (1, 4, 9, 9, 1)),
    (3019, 23, 30, 400, 2959, 5, (1325, 2149), (1, 8, 0, 4, 1)),
    (5147, 15, 46, 4474, 5236, 2, (4813, 1927), (1, 2, 9, 8, 1)),
    (5737, 71, 8, 4284, 5632, 10, (832, 2511), (1, 5, 5, 0, 9)),
)


def prime(n):
    return n >= 2 and all(n % x for x in range(2, int(n**0.5)+1))


def count(q):
    # Legendre count on the short model. PARI uses ellcard on the minimal one.
    total = q+1
    for x in range(q):
        a = (x*x*x+A*x+B) % q
        if a:
            total += 1 if pow(a, (q-1)//2, q) == 1 else -1
    return total


def add(u, v, q):
    if u is None: return v
    if v is None: return u
    x,y = u
    z,w = v
    if x == z and (y+w) % q == 0: return None
    slope = (((3*x*x+A)*pow(2*y,-1,q)) if u == v else
             ((w-y)*pow(z-x,-1,q))) % q
    xx = (slope*slope-x-z) % q
    return xx, (slope*(x-xx)-y) % q


def mul(n, u, q):
    z = None
    while n:
        if n & 1: z = add(z,u,q)
        u = add(u,u,q)
        n >>= 1
    return z


def rho(q, n):
    t = (q+1-n) % P
    return ((0, -q % P), (1,t))


def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) % P
                       for j in range(2)) for i in range(2))


def mv(a,u):
    return tuple(sum(a[i][j]*u[j] for j in range(2)) % P for i in range(2))


def mpower(a,n):
    out=((1,0),(0,1))
    for _ in range(n):out=mm(out,a)
    return out


def artin_zero(a,b):
    # Source-defined C0033 principal Artin character, not a new proof
    # of the class-field identification of the anticyclotomic layer.
    omega = 16
    num = (a+b*omega)%121
    den = (a+b*(1-omega))%121
    ratio = num*pow(den,-1,121)%121
    unit = pow(ratio,10,121)
    assert unit == 1, (a,b,ratio,unit)
    return ratio


def rank(rows, cols):
    mat=[list(row) for row in rows]
    r=0
    for col in range(cols):
        j=next((i for i in range(r,len(mat)) if mat[i][col]%P),None)
        if j is None:continue
        mat[r],mat[j]=mat[j],mat[r]
        z=pow(mat[r][col],-1,P)
        mat[r]=[z*v%P for v in mat[r]]
        for i in range(len(mat)):
            if i!=r:
                t=mat[i][col]
                mat[i]=[(x-t*y)%P for x,y in zip(mat[i],mat[r])]
        r+=1
    return r


def determinant(m):
    n=len(m)
    answer=0
    for perm in permutations(range(n)):
        sign=(-1)**sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        t=sign
        for i in range(n):t*=m[i][perm[i]]
        answer+=t
    return answer%P


def arithmetic():
    rows=[]
    result=[]
    for q,a,b,root,n,order,t,expected in DATA:
        assert prime(q) and q not in (7,11,117223)
        assert a*a+a*b+2*b*b == q
        assert (root*root+7)%q==0
        assert (a+b*(1+root)*pow(2,-1,q))%q==0
        assert artin_zero(a,b) in range(1,121)
        assert count(q)==n and n%P==0 and n%(P*P)!=0
        assert q%P!=1, 'Exclude double-root residue and possible Frobenius norm zero'
        F=rho(q,n)
        assert (1-F[0][0]-F[1][1]+q)%P==0  # charpoly(1)=#E(Fq)=0
        assert mpower(F,order)==((1,0),(0,1))
        assert all(mpower(F,k)!=((1,0),(0,1)) for k in range(1,order))
        # The eigenvalues are 1 and q mod 11; the eigenvalue 1 is simple.
        assert order == next(k for k in range(1,11) if pow(q,k,P)==1)
        # Source-critical norm bridge: the unramified local Kummer
        # coinvariant V/(Frob-I)V is carried isomorphically onto the
        # fixed line by the mth Frobenius norm. Exhaust all 121 vectors.
        zero=((0,0),(0,0))
        N=zero
        T=((1,0),(0,1))
        for _ in range(order):
            N=tuple(tuple((N[i][j]+T[i][j])%P for j in range(2))
                    for i in range(2))
            T=mm(T,F)
        assert T==((1,0),(0,1))
        FmI=((F[0][0]-1)%P,F[0][1],F[1][0],(F[1][1]-1)%P)
        im={( (FmI[0]*u[0]+FmI[1]*u[1])%P,
              (FmI[2]*u[0]+FmI[3]*u[1])%P )
            for u in product(range(P),repeat=2)}
        ker={u for u in product(range(P),repeat=2) if mv(N,u)==(0,0)}
        assert im==ker and len(im)==P
        assert len({mv(N,u) for u in product(range(P),repeat=2)})==P
        R=(-3355*pow(63,-1,q)%q,
           128780*pow(1323,-1,q)*root%q)
        points=[(x%q,y%q) for x,y in POINTS]+[R]
        assert all((y*y-x*x*x-A*x-B)%q==0 for x,y in points)
        projected=[mul(n//P,x,q) for x in points]
        T=projected[0]
        assert T==t and T is not None and mul(P,T,q) is None
        table={mul(j,T,q):j for j in range(P)}
        assert len(table)==P
        row=tuple(table[x] for x in projected)
        assert row==expected
        rows.append(row)
        result.append(f'PURE {q} {a} {b} {root} {n} {q+1-n} {order} 0 '
                      f'{T[0]} {T[1]} ' + ' '.join(map(str,row)))
    assert rank(rows,5)==5 and determinant(rows)==5

    # Irreducible q23 Frobenius acts on ANY nonzero translation vector
    # through a two-dimensional orbit. No full GL2-surjectivity needed.
    sigma=rho(23,30)
    assert sigma==((0,10),(1,5))
    assert mpower(sigma,12)==((1,0),(0,1))
    assert all(mpower(sigma,j)!=((1,0),(0,1)) for j in range(1,12))
    assert (6*6-4)%P==10
    assert 10 not in {j*j%P for j in range(P)}
    for u in product(range(P),repeat=2):
        if u==(0,0):continue
        Au=mv(sigma,u)
        assert (u[0]*Au[1]-u[1]*Au[0])%P !=0

    # The five rank-one pure Frobenius vectors (row_i tensor u_i),
    # together with their q23 conjugates, span all V^5 for ANY
    # nonzero u_i, not just the chosen local torsion generators.
    sample_u=((1,0),(2,1),(4,3),(6,5),(10,9))
    columns=[]
    for row,u in zip(rows,sample_u):
        for z in (u,mv(sigma,u)):
            columns.append(tuple(x for scalar in row for x in
                                 ((scalar*z[0])%P,(scalar*z[1])%P)))
    assert rank(columns,10)==10

    # Deliberately failing controls.
    assert rank(rows[:-1]+[rows[0]],5)==4
    assert rank(columns[:8],10)==8
    # Actual q3851 has q≡1 mod11; a valuation-one residual row
    # cannot be used in this proof without an exact integral Frobenius
    # action/order test. The nonanomalous-eigenvalue gate rejects it.
    assert 3851%P==1
    # A genuine countermodel to the invalid q=1 eigenvalue shortcut:
    # J has the actual possible polynomial (X-1)^2, order 11,
    # nonzero unramified coinvariant, but its 11th Frobenius norm is ZERO.
    J=((1,1),(0,1))
    assert mpower(J,P)==((1,0),(0,1))
    assert all(mpower(J,k)!=((1,0),(0,1)) for k in range(1,P))
    N=((0,0),(0,0))
    T=((1,0),(0,1))
    for _ in range(P):
        N=tuple(tuple((N[i][j]+T[i][j])%P for j in range(2))
                for i in range(2))
        T=mm(T,J)
    assert N==((0,0),(0,0))
    imj={((u[1])%P,0) for u in product(range(P),repeat=2)}
    assert (0,1) not in imj
    # q127's actual anticyclotomic character is nonzero:
    r127=(((-11+6*16)%121) *
          pow((-11-6*15)%121,-1,121))%121
    assert pow(r127,10,121)!=1
    # Without a nonzero anticyclotomic h=Frob23^12 the joint image
    # could cover only the 10-dimensional Kummer part, not C11.
    assert (12*2)%P==2
    return result


def compare(expected,actual):
    if expected!=actual:raise ValueError('PARI certificate incomplete/mutated/error-bearing')


def main():
    rows=arithmetic()
    for row in rows:print(row)
    bad=[rows[:-1],rows+[rows[0]],
         ['*** GP error']+rows[1:],
         [rows[0].replace(' 2 6',' 2 5')]+rows[1:]]
    for v in bad:
        try:compare(rows,v)
        except ValueError:pass
        else:raise AssertionError('Accepted a corrupted independent oracle')
    if len(sys.argv)==2:
        compare(rows,Path(sys.argv[1]).read_text(encoding='utf8').splitlines())
        print('PASS independent PARI ray-class and minimal-model 5-prime arithmetic')
    else:
        assert len(sys.argv)==1
    print('PASS exact Frobenius norm image/kernel identity at all five primes')
    print('PASS q3851 repeated-eigen Jordan countermodel and q127 character mutation')
    print('PASS five actual chi=0 good split primes, n11=1, rho order coprime11')
    print('PASS independent rank5 and determinant5; all120 irreducible Frobenius orbits')
    print('PASS Kummer translation image V^5 over L D1 (source-dependent local Kummer theorem)')
    print('NONCLAIM: no full residual GL2 assumption or actual first correction required')
    print("NONCLAIM: no Greenberg lift, 2nd height, complex L'', Sha or general BSD proof")


if __name__=='__main__':
    main()
