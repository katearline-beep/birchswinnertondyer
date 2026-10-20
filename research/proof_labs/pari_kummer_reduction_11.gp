\\ Independent model: minimal y^2+xy=x^3-x^2-79x+289.
check(c,s)={if(!c,error(s));};
{
qs=[127,743,907,1087,1117];mat=matrix(5,5);
check(ellcard(ellinit([1,-1,0,-79,289],23))==30 && kronecker(-7,23)==1,"torsion check failed");
check(ellcard(ellinit([1,-1,0,-79,289],911))==968,"negative order control changed");
for(i=1,#qs,
  q=qs[i];ee=ellinit([1,-1,0,-79,289],q);n=ellcard(ee);
  check(n%11==0 && n%121!=0,"wrong order valuation");
  sr=lift(sqrt(Mod(-7,q)));sr=min(sr,q-sr);
  pts=[[15,40],[19,4],[23,16],[31,88],[-3355/63,128780/1323*sr]];
  pts=vector(5,j,[Mod((pts[j][1]+1)/4,q),Mod((pts[j][2]-pts[j][1]-1)/8,q)]);
  check(vecprod(vector(5,j,ellisoncurve(ee,pts[j])))==1,"off curve");
  vs=vector(5,j,ellmul(ee,pts[j],n/11));
  idx=1;while(#vs[idx]==1,idx++);tt=vs[idx];
  check(ellmul(ee,tt,11)==[0],"generator not eleven torsion");
  logs=vector(5,j,-1);
  for(j=1,5,for(k=0,10,if(ellmul(ee,tt,k)==vs[j],logs[j]=k)));
  check(vecmin(logs)>=0,"discrete log missing");
  for(j=1,5,mat[i,j]=logs[j]);
  zz=lift(4*tt[1]-1);ww=lift(8*tt[2]+4*tt[1]);
  print1("REDUCTION ",q," ",sr," ",n," ",zz," ",ww);
  for(j=1,5,print1(" ",logs[j]));print(" 11");
);
check(lift(matdet(Mod(mat,11)))==5,"determinant mismatch");
}
quit;
