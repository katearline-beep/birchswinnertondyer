\\ Independent local inputs on the different minimal model.
E=ellinit([1,-1,0,-79,289]);
p=11; m=121; w=sqrt(-7+O(p^8));
names=["P1","P2","P3","P4","R"];
out=matrix(2,5);
for(j=1,2,z=if(j==1,w,-w); shortpts=[[15,40],[19,4],[23,16],[31,88],[-3355/63,128780*z/1323]]; for(i=1,5,P=shortpts[i]; Q=[(P[1]+1)/4,(P[2]-P[1]-1)/8]; if(!ellisoncurve(E,Q),error("point conversion")); Q18=ellmul(E,Q,18); local_log=ellpadiclog(E,p,7,Q18)/(36*p); out[j,i]=lift(local_log)%m));
\\ omega_min=2*omega_short, hence36*p above matches old18*p normalization.
for(i=1,5,print("LOCAL ",names[i]," ",out[1,i]," ",out[2,i]));
L=Mod(out,p); F=[0,9,2;1,0,0;0,1,0;0,0,1;0,0,0];
if(matrank(L)!=2 || L*F!=matrix(2,3),error("fine kernel failure"));
if(lift(L[1,2])!=0 || lift(L[2,2])!=0,error("P2 not locally divisible"));
if(matrank(Mod(F,p))!=3,error("fine frame dependent"));
print("PASS PARI fine-localization inputs");
{
q=3389; ee=ellinit([1,-1,0,-79,289],q); n=ellcard(ee);
if(n!=3498 || n%121==0,error("auxiliary order changed"));
sr=lift(sqrt(Mod(-7,q))); sr=min(sr,q-sr);
pts=[[15,40],[19,4],[23,16],[31,88],[-3355/63,128780/1323*sr]];
pts=vector(5,j,[Mod((pts[j][1]+1)/4,q),Mod((pts[j][2]-pts[j][1]-1)/8,q)]);
if(vecprod(vector(5,j,ellisoncurve(ee,pts[j])))!=1,error("auxiliary point conversion"));
vs=vector(5,j,ellmul(ee,pts[j],n/11));tt=vs[1];
if(#tt!=2 || ellmul(ee,tt,11)!=[0],error("auxiliary generator"));
logs=vector(5,j,-1);
for(j=1,5,for(k=0,10,if(ellmul(ee,tt,k)==vs[j],logs[j]=k)));
if(vecmin(logs)<0,error("auxiliary discrete logarithm missing"));
print1("AUX ",q," ",sr," ",n," ",lift(4*tt[1]-1)," ",lift(8*tt[2]+4*tt[1]));
for(j=1,5,print1(" ",logs[j]));print("");
}
