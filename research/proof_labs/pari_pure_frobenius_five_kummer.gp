\\ Session46 independent PARI: ray-class character and minimal-model group arithmetic.
\\ A certificate of finite input only, NOT a global corrected Galois cocycle.
check(c,s)={if(!c,error(s));};
{
  bnf=bnfinit(y^2-y+2,1);
  check(bnfcertify(bnf)==1 && bnf.no==1,"K not certified");
  ray=bnrinit(bnf,121,1);
  check(ray.cyc==[110,55],"wrong ray group");
  subgroup=mathnf(concat(11*matid(2),bnrisprincipal(ray,2,0)));
  check(subgroup==[11,0;0,1],"wrong anticyclotomic quotient");
  ratio=Mod(16,121)/Mod(-15,121);
  ellomega=lift(znlog(ratio^10,Mod(12,121)));
  scale=Mod(ellomega,11)/Mod(bnrisprincipal(ray,y,0)[1],11);
  data=[[743,13,14,634,770,10],
        [2843,43,14,399,2893,5],
        [3019,23,30,400,2959,5],
        [5147,15,46,4474,5236,2],
        [5737,71,8,4284,5632,10]];
  mat=matrix(5,5);
  check(ellcard(ellinit([1,-1,0,-79,289],23))==30,"bad q23 count");
  for(i=1,#data,
    q=data[i][1];a=data[i][2];b=data[i][3];
    root=data[i][4];n0=data[i][5];m0=data[i][6];
    check(a^2+a*b+2*b^2==q && (root^2+7)%q==0,"bad ideal norm/root");
    check(lift(Mod(a+b*(1+root)/2,q))==0,"wrong split-prime orientation");
    ee=ellinit([1,-1,0,-79,289],q);
    n=ellcard(ee);tr=q+1-n;
    check(n==n0 && n%11==0 && n%121!=0 && q%11!=1,"bad count/eigenvalue gate");
    aa=Mod([0,-q;1,tr],11);order=1;bb=aa;
    while(bb!=matid(2),bb=bb*aa;order++;check(order<=12,"bad order bound"));
    check(order==m0,"bad residual Frobenius order");
    ell=lift(scale*bnrisprincipal(ray,a+b*y,0)[1]);
    check(ell==0,"character-zero input failed");
    pts=[[15,40],[19,4],[23,16],[31,88],[-3355/63,128780/1323*root]];
    pts=vector(5,j,[Mod((pts[j][1]+1)/4,q),Mod((pts[j][2]-pts[j][1]-1)/8,q)]);
    check(vecprod(vector(5,j,ellisoncurve(ee,pts[j])))==1,"off minimal curve");
    vs=vector(5,j,ellmul(ee,pts[j],n/11));
    tt=vs[1];
    check(#tt==2 && ellmul(ee,tt,11)==[0],"no nonzero P1 projection");
    logs=vector(5,j,-1);
    for(j=1,5,for(k=0,10,if(ellmul(ee,tt,k)==vs[j],logs[j]=k)));
    check(vecmin(logs)>=0 && logs[1]==1,"discrete log failed");
    for(j=1,5,mat[i,j]=logs[j]);
    print1("PURE ",q," ",a," ",b," ",root," ",n," ",tr," ",order," ",ell,
      " ",lift(4*tt[1]-1)," ",lift(8*tt[2]+4*tt[1]));
    for(j=1,5,print1(" ",logs[j]));
    print("");
  );
  check(lift(matdet(Mod(mat,11)))==5,"determinant is not 5 mod11");
}
quit;
