\\ Independent numerical check of E^(-7): y^2=x^3-62083*x-5909890
\\ NOT a rigorous zero-free proof. Compares a saved separate rational bound.
default(realprecision,38);
E=ellinit([0,0,0,-62083,-5909890]);
c=ellglobalred(E)[1];
s=ellrootno(E);
if(c!=11487854,error(Str("unexpected conductor ",c)));
if(s!=-1,error(Str("unexpected global root sign ",s)));
a=ellanalyticrank(E);
if(a[1]!=1,error(Str("PARI analytic rank unexpectedly ",a[1])));
d=ellL1(E,1);
if(!(d>19 && d<49),error(Str("PARI derivative outside certified coarse interval ",d)));
if(abs(d-a[2])>10^(-18),error(Str("ellanalyticrank and ellL1 disagree ",a," ",d)));
print(Str("PARI_NUMERIC rank=",a[1]," derivative=",d," conductor=",c," rootno=",s));
print("PASS PARI twist sign/conductor/analytic derivative independently corroborated");
quit;
