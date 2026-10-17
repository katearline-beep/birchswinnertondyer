\\ Independent C-0002 check with PARI/GP built-in ellpadiclog
\\ Exact source coordinates; use a high-precision 11-adic square root of -7.
\\ No formulas or field-arithmetic code imported from our Python scripts.
default(parisize, 128000000);
p=11; m=p^4; E=ellinit([0,0,0,-1267,17230]);
w=sqrt(-7 + O(11^10));
if(lift(w)%11 != 2, w=-w);
expected=[[7462,14432,1427,7989,8215,1495], [7462,14432,1427,7989,6426,7921]];
for(j=1,2,
  z=if(j==1,w,-w);
  pts=[[15,40],[19,4],[23,16],[31,88],[-3355/63,128780*z/1323],[(37+3*z)/2,-16+12*z]];
  for(i=1,6,
    Q=ellmul(E,pts[i],18);
    local_log=ellpadiclog(E,11,7,Q)/(18*11);
    residue=lift(local_log)%m;
    if(residue!=expected[j][i], error(Str("mismatch embedding=",j," point=",i," got=",residue," expected=",expected[j][i])));
  );
);
print("PASS PARI/GP C-0002: all twelve normalized split-11 logarithms mod 14641");
print("PASS PARI/GP C-0002: determinant 1537 mod 14641, 8 mod 11");
quit;
