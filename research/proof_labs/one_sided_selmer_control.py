#!/usr/bin/env python3
"""Exact linear-algebra controls for the Session29 one-sided Selmer lemma.

F11 examples illustrate a characteristic-zero proof; not computed Galois
cohomology or an actual height kernel. Full negative dimension ONE is vital;
full positive dimension FOUR is not needed for the three exact MW classes.
"""
P=11


def dot(x,y): return sum(a*b for a,b in zip(x,y))%P


def rank(A):
    A=[[v%P for v in r] for r in A]; i=0
    for j in range(len(A[0])):
        k=next((k for k in range(i,len(A)) if A[k][j]),None)
        if k is None: continue
        A[i],A[k]=A[k],A[i]
        z=pow(A[i][j],-1,P); A[i]=[z*v%P for v in A[i]]
        for k in range(len(A)):
            if i!=k:
                z=A[k][j]; A[k]=[(v-z*w)%P for v,w in zip(A[k],A[i])]
        i+=1
        if i==len(A): break
    return i


def cross_height(A):
    a,b=len(A),len(A[0])
    return [[0]*a+row for row in A]+[
        [A[i][j] for i in range(a)]+[0]*b for j in range(b)]


def frame(v,total):
    assert len(v)==4 and v[0]%P
    out=[]
    for j in range(1,4):
        z=[0]*total; z[j]=1; z[0]=-v[j]*pow(v[0],-1,P)%P
        out.append(z)
    return out


def main():
    # Actual normalized first-digit profile is only an INPUT to these models.
    v=[1,2,7,8]
    for plus in (4,6,8):
        row=v+list(range(3,plus-1))
        assert len(row)==plus
        H=cross_height([[a] for a in row])
        U=frame(v,plus+1)
        assert rank(U)==3 and rank(H)==2
        assert all(dot(r,x)==0 for r in H for x in U)
        assert plus+1-rank(H)==plus-1
        print('PASS plus dimension',plus,'minus1: three MW classes in full radical;',
              'full radical dimension',plus-1)
    # All four mixed MW/R measurements stay IDENTICAL, but extra negative
    # directions can invalidate the proposed S2 membership.
    A=[[v[i],int(i==1),int(i==2)] for i in range(4)]
    H=cross_height(A); U=frame(v,7)
    assert [H[i][4] for i in range(4)]==v
    assert rank(H)==6 and 7-rank(H)==1
    assert any(dot(r,x) for r in H for x in U)
    assert H[5][1]==1 and dot(H[5],U[0])==1
    print('PASS minus3 countermodel preserves all measured MW/R heights but defeats S2 membership')
    # A common normalization sign/unit cancels in a_j/a_1.
    for scalar in range(1,P):
        assert frame([scalar*a%P for a in v],5)==frame(v,5)
    print('PASS all nonzero common normalization scalars preserve the exact-kernel recipe')
    # Finite Sha can have p-torsion while its p-adic Tate module is zero:
    # for A=Z/11, transition p:A[p^(n+1)]->A[p^n] is identically zero.
    assert all((P*a)%P==0 for a in range(P))
    print('PASS finite Sha does not mean Sha[11]=0; only its Tate module vanishes')
    print('NONCLAIM: source GZK theorem, analytic certificate and actual heights are separate inputs.')
    print('NONCLAIM: no arithmetic second Bockstein, full positive Selmer bound or complex BSD.')


if __name__=='__main__': main()
