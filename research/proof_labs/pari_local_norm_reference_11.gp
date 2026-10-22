\\ Independent maintained PARI formal-logarithm and multiplication-trace oracle.
\\ Local point: t=pi with pi a root of g; no actual global correction.
print("BEGIN_LOCAL_NORM37");
print("VERSION ",version());
E=ellinit([1,-1,0,-79,289]);
f=x^11-33*x^9-176*x^8+418*x^7+11649*x^6+108009*x^5+711337*x^4+3244989*x^3+9160173*x^2+14938803*x+11133855;
g=subst(f,x,x+4);
print("G ",vector(12,i,polcoef(g,i-1)));
print("DISC11 ",valuation(poldisc(g),11));
lg=ellformallog(E,34,'t);
for(n=1,33, s=trace(Mod(x,g)^n); a=polcoef(lg,n); print("ROW ",n," ",a," ",s," ",lift(Mod(a*s/11,121))));
z=sum(n=1,22,polcoef(lg,n)*trace(Mod(x,g)^n));
print("NORM ",lift(Mod(z/11,121)));
ex=ellformalexp(E,5,'t);
print("TNORM ",lift(Mod(subst(truncate(ex),t,z),1331)));
print("LONGSUM ",lift(Mod(sum(n=1,33,polcoef(lg,n)*trace(Mod(x,g)^n))/11,121)));
cv(P)=[(P[1]+1)/4,(P[2]-P[1]-1)/8];
sc(P)=lift(Mod(lift(ellpadiclog(E,11,7,ellmul(E,cv(P),18))/(18*11)),11)/5);
pts=[[15,40],[19,4],[23,16],[31,88]];
pr=vector(4,i,sc(pts[i]));
zz=sqrt(-7+O(11^8)); if(lift(zz)%11!=2,zz=-zz);
rr=vector(2,j,sc([-3355/63,128780/1323*if(j==1,zz,-zz)]));
kr=[lift(Mod(pr[2]-2*pr[1],11)),lift(Mod(pr[3]-7*pr[1],11)),lift(Mod(pr[4]-8*pr[1],11))];
print("PREF ",pr); print("RREF ",rr); print("KREF ",kr);
print("END_LOCAL_NORM37");
quit;
