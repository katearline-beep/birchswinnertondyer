\\ Genuine class field oracle; run from repository root, gp -s 128000000 -q -f.
\\ GP can exit zero after errors: caller MUST reject every *** diagnostic.
check(c,s)={if(!c,error(s));};
artin_formula(a,b,m)={
  my(modulus=11^(m+1),r=5,s,u);
  for(j=2,m+1,r=r+11^(j-1)*lift(-Mod((r^2-r+2)/11^(j-1),11)/Mod(2*r-1,11)));
  check((r^2-r+2)%modulus==0,"Hensel root failure");s=1-r;
  u=Mod(a+b*r,modulus)/Mod(a+b*s,modulus);
  lift(znlog(u^10,Mod(12,modulus)))
};
{
b=bnfinit(y^2-y+2,1);
check(bnfcertify(b)==1,"uncertified base class group");
check(b.no==1 && b.disc==-7 && b.zk==[1,y],"wrong base field");
for(m=1,2,
  n=11^m;modulus=11^(m+1);r=bnrinit(b,modulus,1);
  check(r.cyc==[10*n,5*n],"unexpected ray class group");
  h=mathnf(concat(n*matid(#r.cyc),bnrisprincipal(r,2,0)));
  check(h==[n,0;0,1] && matdet(h)==n,"wrong diagonal quotient");
  conductor=bnrconductor(r,h);
  check(conductor[1]==matdiagonal([modulus,modulus]),"wrong conductor");
  tau=bnrgaloismatrix(r,1-y);
  check(bnrisgalois(r,tau,h)==1 && lift(Mod(tau[1,1],n))==n-1 && tau[1,2]%n==0,"not anticyclotomic");
  d=bnrdisc(r,h);check(d==[2*n,0,(-7)^n*11^sum(j=1,m,2*(j+1)*(11^j-11^(j-1)))],"wrong class field discriminant");
  print("LAYER ",m," ",n," ",modulus," ",d[3]);
  ow=bnrisprincipal(r,y,0)[1];
  scale=lift(Mod(artin_formula(0,1,m),n)/Mod(ow,n));
  forprime(l=2,500,if(l!=11,
    ps=idealprimedec(b,l);
    for(i=1,#ps,
      pp=ps[i];ab=bnfisprincipal(b,pp)[2];
      v=bnrisprincipal(r,pp,0);ell=lift(Mod(scale*v[1],n));
      check(ell==artin_formula(ab[1],ab[2],m),"ideal/residue Artin disagreement");
      print("PRIME ",m," ",l," ",i," ",pp.f," ",ab[1]," ",ab[2]," ",ell);
    );
  ));
);
r=bnrinit(b,121,1);h=[11,0;0,1];
p=bnrclassfield(r,h,1);
q=rnfpolredbest(b,p,2);
check(polisirreducible(q) && poldegree(q)==22,"class field not degree22");
check(nfdisc(q)==(-7)^11*11^40,"polynomial field discriminant mismatch");
g=galoisinit(q);check(galoisidentify(g)==[22,1],"not D11 over Q");
\\ Compact reflection-fixed degree11 field; its compositum with K must be q.
f=x^11-33*x^9-176*x^8+418*x^7+11649*x^6+108009*x^5+711337*x^4+3244989*x^3+9160173*x^2+14938803*x+11133855;
check(polisirreducible(f) && nfdisc(f)==-7^5*11^20,"wrong fixed field");
cs=polcompositum(f,x^2-x+2);
check(#cs==1 && poldegree(cs[1])==22 && nfisisom(cs[1],q)!=0,"fixed field compositum mismatch");
\\ Independently compare polynomial splitting and Artin on unramified primes.
nf=nfinit(f);check(nf.sign==[1,5],"wrong fixed field signature");
forprime(l=2,200,if(l!=7 && l!=11,
  fac=idealprimedec(nf,l);degrees=vecsort(vector(#fac,j,fac[j].f));
  if(kronecker(-7,l)==-1,check(degrees==concat([1],vector(5,j,2)),"inert splitting wrong"),
    pp=idealprimedec(b,l)[1];ab=bnfisprincipal(b,pp)[2];
    ell=artin_formula(ab[1],ab[2],1);
    check(degrees==if(ell==0,vector(11,j,1),[11]),"split Frobenius pattern wrong");
  );
));
print("PASS CLASSFIELD degree22 dihedral22 fixed11 discriminant conductor");
quit;
}
